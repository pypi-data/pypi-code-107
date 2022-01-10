import re
import logging

from numpy.testing import assert_equal
import pytest

from brian2 import *
from brian2.utils.logger import catch_logs
from brian2.core.variables import ArrayVariable, Variable, Constant
from brian2.stateupdaters.base import UnsupportedEquationsException
from brian2.tests.utils import assert_allclose, exc_isinstance

@pytest.mark.codegen_independent
def test_explicit_stateupdater_parsing():
    """
    Test the parsing of explicit state updater descriptions.
    """
    # These are valid descriptions and should not raise errors
    updater = ExplicitStateUpdater('x_new = x + dt * f(x, t)')
    updater(Equations('dv/dt = -v / tau : 1'))
    updater = ExplicitStateUpdater("""x2 = x + dt * f(x, t)
                                      x_new = x2""")
    updater(Equations('dv/dt = -v / tau : 1'))
    updater = ExplicitStateUpdater("""x1 = g(x, t) * dW
                                      x2 = x + dt * f(x, t)
                                      x_new = x1 + x2""",
                                   stochastic='multiplicative')
    updater(Equations('dv/dt = -v / tau + v * xi * tau**-.5: 1'))
    
    updater = ExplicitStateUpdater("""x_support = x + dt*f(x, t) + dt**.5 * g(x, t)
                                      g_support = g(x_support, t)
                                      k = 1/(2*dt**.5)*(g_support - g(x, t))*(dW**2)
                                      x_new = x + dt*f(x,t) + g(x, t) * dW + k""",
                                   stochastic='multiplicative')
    updater(Equations('dv/dt = -v / tau + v * xi * tau**-.5: 1'))

    
    # Examples of failed parsing
    # No x_new = ... statement
    with pytest.raises(SyntaxError):
        ExplicitStateUpdater('x = x + dt * f(x, t)')
    # Not an assigment
    with pytest.raises(SyntaxError):
        ExplicitStateUpdater("""2 * x
                                x_new = x + dt * f(x, t)""")
    
    # doesn't separate into stochastic and non-stochastic part
    updater = ExplicitStateUpdater("""x_new = x + dt * f(x, t) * g(x, t) * dW""")
    with pytest.raises(ValueError):
        updater(Equations(''))

@pytest.mark.codegen_independent
def test_non_autonomous_equations():
    # Check that non-autonmous equations are handled correctly in multi-step
    # updates
    updater = ExplicitStateUpdater('x_new = f(x, t + 0.5*dt)')
    update_step = updater(Equations('dv/dt = t : 1'))  # Not a valid equation but...
    # very crude test
    assert '0.5*dt' in update_step

@pytest.mark.codegen_independent
def test_str_repr():
    """
    Assure that __str__ and __repr__ do not raise errors 
    """
    for integrator in [linear, euler, rk2, rk4]:
        assert len(str(integrator))
        assert len(repr(integrator))


@pytest.mark.codegen_independent
def test_multiple_noise_variables_basic():
    # Very basic test, only to make sure that stochastic state updaters handle
    # multiple noise variables at all
    eqs = Equations("""dv/dt = -v / (10*ms) + xi_1 * ms ** -.5 : 1
                       dw/dt = -w / (10*ms) + xi_2 * ms ** -.5 : 1""")
    for method in [euler, heun, milstein]:
        code = method(eqs, {})
        assert 'xi_1' in code
        assert 'xi_2' in code


def test_multiple_noise_variables_extended():
    # Some actual simulations with multiple noise variables
    eqs = """dx/dt = y : 1
             dy/dt = - 1*ms**-1*y - 40*ms**-2*x : Hz
            """
    all_eqs_noise = ["""dx/dt = y : 1
                        dy/dt = noise_factor*ms**-1.5*xi_1 + noise_factor*ms**-1.5*xi_2
                           - 1*ms**-1*y - 40*ms**-2*x : Hz
                     """,
                     """dx/dt = y + noise_factor*ms**-0.5*xi_1: 1
                        dy/dt = noise_factor*ms**-1.5*xi_2
                            - 1*ms**-1*y - 40*ms**-2*x : Hz
                     """]
    G = NeuronGroup(2, eqs, method='euler')
    G.x = [0.5, 1]
    G.y = [0, 0.5] * Hz
    mon = StateMonitor(G, ['x', 'y'], record=True)
    net = Network(G, mon)
    net.run(10*ms)
    no_noise_x, no_noise_y = mon.x[:], mon.y[:]

    for eqs_noise in all_eqs_noise:
        for method_name, method in [('euler', euler), ('heun', heun)]:
            with catch_logs('WARNING'):
                G = NeuronGroup(2, eqs_noise, method=method)
                G.x = [0.5, 1]
                G.y = [0, 0.5] * Hz
                mon = StateMonitor(G, ['x', 'y'], record=True)
                net = Network(G, mon)
                # We run it deterministically, but still we'd detect major errors (e.g.
                # non-stochastic terms that are added twice, see #330
                net.run(10*ms, namespace={'noise_factor': 0})
            assert_allclose(mon.x[:], no_noise_x,
                            err_msg=f'Method {method_name} gave incorrect results')
            assert_allclose(mon.y[:], no_noise_y,
                            err_msg=f'Method {method_name} gave incorrect results')


def test_multiple_noise_variables_deterministic_noise(fake_randn_randn_fixture):
    all_eqs = ["""dx/dt = y : 1
                          dy/dt = -y / (10*ms) + dt**-.5*0.5*ms**-1.5 + dt**-.5*0.5*ms**-1.5: Hz
                     """,
                     """dx/dt = y + dt**-.5*0.5*ms**-0.5: 1
                        dy/dt = -y / (10*ms) + dt**-.5*0.5 * ms**-1.5 : Hz
                """]
    all_eqs_noise = ["""dx/dt = y : 1
                          dy/dt = -y / (10*ms) + xi_1 * ms**-1.5 + xi_2 * ms**-1.5: Hz
                     """,
                     """dx/dt = y + xi_1*ms**-0.5: 1
                        dy/dt = -y / (10*ms) + xi_2 * ms**-1.5 : Hz
                     """]
    for eqs, eqs_noise in zip(all_eqs, all_eqs_noise):
        G = NeuronGroup(2, eqs, method='euler')
        G.x = [5,  17]
        G.y = [25, 5 ] * Hz
        mon = StateMonitor(G, ['x', 'y'], record=True)
        net = Network(G, mon)
        net.run(10*ms)
        no_noise_x, no_noise_y = mon.x[:], mon.y[:]

        for method_name, method in [('euler', euler), ('heun', heun)]:
            with catch_logs('WARNING'):
                G = NeuronGroup(2, eqs_noise, method=method)
                G.x = [5,  17]
                G.y = [25, 5 ] * Hz
                mon = StateMonitor(G, ['x', 'y'], record=True)
                net = Network(G, mon)
                net.run(10*ms)
            assert_allclose(mon.x[:], no_noise_x,
                            err_msg=f'Method {method_name} gave incorrect results')
            assert_allclose(mon.y[:], no_noise_y,
                            err_msg=f'Method {method_name} gave incorrect results')


@pytest.mark.codegen_independent
def test_multiplicative_noise():
    # Noise is not multiplicative (constant over time step)
    ta = TimedArray([0, 1], dt=defaultclock.dt*10)
    Eq = Equations('dv/dt = ta(t)*xi*(5*ms)**-0.5 :1')
    group = NeuronGroup(1, Eq, method='euler')
    net = Network(group)
    net.run(0*ms)  # no error
    
    # Noise is multiplicative (multiplied with time-varying variable)
    Eq1 = Equations('dv/dt = v*xi*(5*ms)**-0.5 :1')
    group1 = NeuronGroup(1, Eq1, method='euler')
    net1 = Network(group1)
    with pytest.raises(BrianObjectException) as exc:
        net1.run(0*ms)
    assert exc_isinstance(exc, UnsupportedEquationsException)

    # Noise is multiplicative (multiplied with time)
    Eq2 = Equations('dv/dt = (t/ms)*xi*(5*ms)**-0.5 :1')
    group2 = NeuronGroup(1, Eq2, method='euler')
    net2 = Network(group2)
    with pytest.raises(BrianObjectException) as exc:
        net2.run(0*ms)
    assert exc_isinstance(exc, UnsupportedEquationsException)

    # Noise is multiplicative (multiplied with time-varying variable)
    Eq3 = Equations("""dv/dt = w*xi*(5*ms)**-0.5 :1
                       dw/dt = -w/(10*ms) : 1""")
    group3 = NeuronGroup(1, Eq3, method='euler')
    net3 = Network(group3)
    with pytest.raises(BrianObjectException) as exc:
        net3.run(0*ms)
    assert exc_isinstance(exc, UnsupportedEquationsException)

    # One of the equations has multiplicative noise
    Eq4 = Equations("""dv/dt = xi_1*(5*ms)**-0.5 : 1
                       dw/dt = (t/ms)*xi_2*(5*ms)**-0.5 :1""")
    group4 = NeuronGroup(1, Eq4, method='euler')
    net4 = Network(group4)
    with pytest.raises(BrianObjectException) as exc:
        net4.run(0*ms)
    assert exc_isinstance(exc, UnsupportedEquationsException)

    # One of the equations has multiplicative noise
    Eq5 = Equations("""dv/dt = xi_1*(5*ms)**-0.5 : 1
                       dw/dt = v*xi_2*(5*ms)**-0.5 :1""")
    group5 = NeuronGroup(1, Eq5, method='euler')
    net5 = Network(group4)
    with pytest.raises(BrianObjectException) as exc:
        net5.run(0*ms)
    assert exc_isinstance(exc, UnsupportedEquationsException)


def test_pure_noise_deterministic(fake_randn_randn_fixture):
    sigma = 3
    eqs = Equations('dx/dt = sigma*xi/sqrt(ms) : 1')
    dt = 0.1*ms
    for method in ['euler', 'heun', 'milstein']:
        G = NeuronGroup(1, eqs, dt=dt, method=method)
        run(10*dt)
        assert_allclose(G.x, sqrt(dt)*sigma*0.5/sqrt(1*ms)*10,
                        err_msg=f'method {method} did not give the expected result')


@pytest.mark.codegen_independent
def test_temporary_variables():
    """
    Make sure that the code does the distinction between temporary variables
    in the state updater description and external variables used in the
    equations.
    """
    # Use a variable name that is used in the state updater description
    k_2 = 5
    eqs = Equations('dv/dt = -(v + k_2)/(10*ms) : 1')
    converted = rk4(eqs)

    # Use a non-problematic name
    k_var = 5
    eqs = Equations('dv/dt = -(v + k_var)/(10*ms) : 1')
    converted2 = rk4(eqs)

    # Make sure that the two formulations result in the same code
    assert converted == converted2.replace('k_var', 'k_2')


@pytest.mark.codegen_independent
def test_temporary_variables2():
    """
    Make sure that the code does the distinction between temporary variables
    in the state updater description and external variables used in the
    equations.
    """
    tau = 10*ms
    # Use a variable name that is used in the state updater description
    k = 5
    eqs = Equations('dv/dt = -v/tau + k*xi*tau**-0.5: 1')
    converted = milstein(eqs)

    # Use a non-problematic name
    k_var = 5
    eqs = Equations('dv/dt = -v/tau + k_var*xi*tau**-0.5: 1')
    converted2 = milstein(eqs)

    # Make sure that the two formulations result in the same code
    assert converted == converted2.replace('k_var', 'k')


@pytest.mark.codegen_independent
def test_integrator_code():
    """
    Check whether the returned abstract code is as expected.
    """
    # A very simple example where the abstract code should always look the same
    eqs = Equations('dv/dt = -v / (1 * second) : 1')
    
    # Only test very basic stuff (expected number of lines and last line)
    for integrator, lines in zip([linear, euler, rk2, rk4], [2, 2, 3, 6]):
        code_lines = integrator(eqs).split('\n')
        err_msg = f'Returned code for integrator {integrator.__class__.__name__} had {len(code_lines)} lines instead of {int(lines)}'
        assert len(code_lines) == lines, err_msg
        assert code_lines[-1] == 'v = _v'
    
    # Make sure that it isn't a problem to use 'x', 'f' and 'g'  as variable
    # names, even though they are also used in state updater descriptions.
    # The resulting code should be identical when replacing x by x0 (and ..._x by
    # ..._x0)
    for varname in ['x', 'f', 'g']:
        # We use a very similar names here to avoid slightly re-arranged
        # expressions due to alphabetical sorting of terms in
        # multiplications, etc.
        eqs_v = Equations(f'd{varname}0/dt = -{varname}0 / (1 * second) : 1')
        eqs_var = Equations(f'd{varname}/dt = -{varname} / (1 * second) : 1')
        for integrator in [linear, euler, rk2, rk4]:
            code_v = integrator(eqs_v)
            code_var = integrator(eqs_var)
            # Re-substitute the variable names in the output
            code_var = re.sub(rf'\b{varname}\b',
                              f'{varname}0', code_var)
            code_var = re.sub(rf'\b(\w*)_{varname}\b',
                              rf'\1_{varname}0', code_var)
            assert code_var == code_v, f"'{code_var}' does not match '{code_v}'"


@pytest.mark.codegen_independent
def test_integrator_code2():
    """
    Test integration for a simple model with several state variables.
    """
    eqs = Equations("""
    dv/dt=(ge+gi-v)/tau : volt
    dge/dt=-ge/taue : volt
    dgi/dt=-gi/taui : volt
    """)
    euler_integration = euler(eqs)
    lines = sorted(euler_integration.split('\n'))
    # Do a very basic check that the right variables are used in every line
    for varname, line in zip(['_ge', '_gi', '_v', 'ge', 'gi', 'v'], lines):
        assert line.startswith(f"{varname} = "), f'line "{line}" does not start with {varname}'
    for variables, line in zip([['dt', 'ge', 'taue'],
                                ['dt', 'gi', 'taui'],
                                ['dt', 'ge', 'gi', 'v', 'tau'],
                                ['_ge'], ['_gi'], ['_v']],
                               lines):
        rhs = line.split('=')[1]
        for variable in variables:
            assert variable in rhs, f'{variable} not in RHS: "{rhs}"'

@pytest.mark.codegen_independent
def test_illegal_calls():
    eqs = Equations('dv/dt = -v / (10*ms) : 1')
    clock = Clock(dt=0.1*ms)
    variables = {'v': ArrayVariable(name='name', size=10,
                                    owner=None, device=None, dtype=np.float64,
                                    constant=False),
                 't': clock.variables['t'],
                 'dt': clock.variables['dt']}
    with pytest.raises(TypeError):
        StateUpdateMethod.apply_stateupdater(eqs, variables, object())
    with pytest.raises(TypeError):
        StateUpdateMethod.apply_stateupdater(eqs,
                                             variables,
                                             group_name='my_name',
                                             method=object())
    with pytest.raises(TypeError):
        StateUpdateMethod.apply_stateupdater(eqs, variables, [object(), 'euler'])
    with pytest.raises(TypeError):
        StateUpdateMethod.apply_stateupdater(eqs,
                                             variables,
                                             group_name='my_name',
                                             method=[object(), 'euler'])

def check_integration(eqs, variables, can_integrate):
    # can_integrate maps integrators to True/False/None
    # True/False means that the integrator should/should not integrate the equations
    # None means that it *might* integrate the equations (only needed for the
    # exact integration, since it can depend on the sympy version)
    for integrator, able in can_integrate.items():
        try:
            integrator(eqs, variables)
            if able is False:
                raise AssertionError(f"Should not be able to integrate these "
                                     f"equations (equations: '{eqs}') with "
                                     f"integrator {integrator.__class__.__name__}")
        except UnsupportedEquationsException:
            if able is True:
                raise AssertionError(f"Should be able to integrate these "
                                     f"equations (equations: '{eqs}') with "
                                     f"integrator {integrator.__class__.__name__}")

@pytest.mark.codegen_independent
def test_priority():
    updater = ExplicitStateUpdater('x_new = x + dt * f(x, t)')
    # Equations that work for the state updater
    eqs = Equations('dv/dt = -v / (10*ms) : 1')
    clock = Clock(dt=0.1*ms)
    variables = {'v': ArrayVariable(name='name', size=10,
                                    owner=None, device=None, dtype=np.float64,
                                    constant=False),
                 'w': ArrayVariable(name='name', size=10,
                                    owner=None, device=None, dtype=np.float64,
                                    constant=False),
                 't': clock.variables['t'],
                 'dt': clock.variables['dt']}
    updater(eqs, variables)  # should not raise an error

    # External parameter in the coefficient, linear integration should work
    param = 1
    eqs = Equations('dv/dt = -param * v / (10*ms) : 1')
    updater(eqs, variables)  # should not raise an error
    can_integrate = {linear: True, euler: True, exponential_euler: True,
                     rk2: True, rk4: True, heun: True, milstein: True}

    check_integration(eqs, variables, can_integrate)

    # Constant equation, should work for all except linear (see #1010)
    param = 1
    eqs = Equations("""dv/dt = 10*Hz : 1
                       dw/dt = -v/(10*ms) : 1""")
    updater(eqs, variables)  # should not raise an error
    can_integrate = {linear: None, euler: True, exponential_euler: True,
                     rk2: True, rk4: True, heun: True, milstein: True}

    check_integration(eqs, variables, can_integrate)

    # Equations resulting in complex linear solution for older versions of sympy
    eqs = Equations("""dv/dt      = (ge+gi-(v+49*mV))/(20*ms) : volt
            dge/dt     = -ge/(5*ms) : volt
            dgi/dt     = Dgi/(5*ms) : volt
            dDgi/dt    = ((-2./5) * Dgi - (1./5**2)*gi)/(10*ms) : volt""")
    can_integrate = {linear: None, euler: True, exponential_euler: True,
                     rk2: True, rk4: True, heun: True, milstein: True}
    check_integration(eqs, variables, can_integrate)


    # Equation with additive noise
    eqs = Equations('dv/dt = -v / (10*ms) + xi/(10*ms)**.5 : 1')
    with pytest.raises(UnsupportedEquationsException):
        updater(eqs, variables)
    
    can_integrate = {linear: False, euler: True, exponential_euler: False,
                     rk2: False, rk4: False, heun: True, milstein: True}

    check_integration(eqs, variables, can_integrate)
    
    # Equation with multiplicative noise
    eqs = Equations('dv/dt = -v / (10*ms) + v*xi/(10*ms)**.5 : 1')
    with pytest.raises(UnsupportedEquationsException):
        updater(eqs, variables)
    
    can_integrate = {linear: False, euler: False, exponential_euler: False,
                     rk2: False, rk4: False, heun: True, milstein: True}
                     
    check_integration(eqs, variables, can_integrate)


@pytest.mark.codegen_independent
def test_registration():
    """
    Test state updater registration.
    """
    # Save state before tests
    before = dict(StateUpdateMethod.stateupdaters)
    
    lazy_updater = ExplicitStateUpdater('x_new = x')
    StateUpdateMethod.register('lazy', lazy_updater)
    
    # Trying to register again
    with pytest.raises(ValueError):
        StateUpdateMethod.register('lazy', lazy_updater)
    
    # Trying to register something that is not a state updater
    with pytest.raises(ValueError):
        StateUpdateMethod.register('foo', 'just a string')
    
    # Trying to register with an invalid index
    with pytest.raises(TypeError):
        StateUpdateMethod.register('foo', lazy_updater, index='not an index')
    
    # reset to state before the test
    StateUpdateMethod.stateupdaters = before 


@pytest.mark.codegen_independent
def test_determination():
    """
    Test the determination of suitable state updaters.
    """
    # To save some typing
    apply_stateupdater = StateUpdateMethod.apply_stateupdater
    
    eqs = Equations('dv/dt = -v / (10*ms) : 1')
    # Just make sure that state updaters know about the two state variables
    variables = {'v': Variable(name='v'),
                 'w': Variable(name='w')}
    
    # all methods should work for these equations.
    # First, specify them explicitly (using the object)
    for integrator in (linear, euler, exponential_euler, #TODO: Removed "independent" here due to the issue in sympy 0.7.4
                       rk2, rk4, heun, milstein):
        with catch_logs() as logs:
            returned = apply_stateupdater(eqs, variables,
                                          method=integrator)
            assert len(logs) == 0, f'Got {len(logs)} unexpected warnings: {str([l[2] for l in logs])}'
    
    # Equation with multiplicative noise, only milstein and heun should work
    eqs = Equations('dv/dt = -v / (10*ms) + v*xi*second**-.5: 1')
    for integrator in (linear, independent, euler, exponential_euler, rk2, rk4):
        with pytest.raises(UnsupportedEquationsException):
            apply_stateupdater(eqs, variables, integrator)

    for integrator in (heun, milstein):
        with catch_logs() as logs:
            returned = apply_stateupdater(eqs, variables,
                                          method=integrator)
            assert len(logs) == 0, f'Got {len(logs)} unexpected warnings: {str([l[2] for l in logs])}'
    
    # Arbitrary functions (converting equations into abstract code) should
    # always work
    my_stateupdater = lambda eqs, vars, options: 'x_new = x'
    with catch_logs() as logs:
        returned = apply_stateupdater(eqs, variables, method=my_stateupdater)
        # No warning here
        assert len(logs) == 0
    
    
    # Specification with names
    eqs = Equations('dv/dt = -v / (10*ms) : 1')
    for name, integrator in [('exact', exact), ('linear', linear), ('euler', euler),
                             #('independent', independent), #TODO: Removed "independent" here due to the issue in sympy 0.7.4
                             ('exponential_euler', exponential_euler),
                             ('rk2', rk2), ('rk4', rk4),
                             ('heun', heun), ('milstein', milstein)]:
        with catch_logs() as logs:
            returned = apply_stateupdater(eqs, variables,
                                              method=name)
            # No warning here
            assert len(logs) == 0

    # Now all except heun and milstein should refuse to work
    eqs = Equations('dv/dt = -v / (10*ms) + v*xi*second**-.5: 1')
    for name in ['linear', 'exact', 'independent', 'euler', 'exponential_euler',
                 'rk2', 'rk4']:
        with pytest.raises(UnsupportedEquationsException):
            apply_stateupdater(eqs, variables, method=name)

    # milstein should work
    with catch_logs() as logs:
        apply_stateupdater(eqs, variables, method='milstein')
        assert len(logs) == 0
        
    # heun should work
    with catch_logs() as logs:
        apply_stateupdater(eqs, variables, method='heun')
        assert len(logs) == 0
    
    # non-existing name
    with pytest.raises(ValueError):
        apply_stateupdater(eqs, variables, method='does_not_exist')
    
    # Automatic state updater choice should return linear for linear equations,
    # euler for non-linear, non-stochastic equations and equations with
    # additive noise, heun for equations with multiplicative noise
    # Because it is somewhat fragile, the "independent" state updater is not
    # included in this list
    all_methods = ['linear', 'exact', 'exponential_euler', 'euler', 'heun', 'milstein']
    eqs = Equations('dv/dt = -v / (10*ms) : 1')
    with catch_logs(log_level=logging.INFO) as logs:
        apply_stateupdater(eqs, variables, all_methods)
        assert len(logs) == 1
        assert ('linear' in logs[0][2]) or ('exact' in logs[0][2])
    
    # This is conditionally linear
    eqs = Equations("""dv/dt = -(v + w**2)/ (10*ms) : 1
                       dw/dt = -w/ (10*ms) : 1""")
    with catch_logs(log_level=logging.INFO) as logs:
        apply_stateupdater(eqs, variables, all_methods)
        assert len(logs) == 1
        assert 'exponential_euler' in logs[0][2]

    # # Do not test for now
    # eqs = Equations('dv/dt = sin(t) / (10*ms) : 1')
    # assert apply_stateupdater(eqs, variables) is independent

    eqs = Equations('dv/dt = -sqrt(v) / (10*ms) : 1')
    with catch_logs(log_level=logging.INFO) as logs:
        apply_stateupdater(eqs, variables, all_methods)
        assert len(logs) == 1
        assert "'euler'" in logs[0][2]

    eqs = Equations('dv/dt = -v / (10*ms) + 0.1*second**-.5*xi: 1')
    with catch_logs(log_level=logging.INFO) as logs:
        apply_stateupdater(eqs, variables, all_methods)
        assert len(logs) == 1
        assert "'euler'" in logs[0][2]

    eqs = Equations('dv/dt = -v / (10*ms) + v*0.1*second**-.5*xi: 1')
    with catch_logs(log_level=logging.INFO) as logs:
        apply_stateupdater(eqs, variables, all_methods)
        assert len(logs) == 1
        assert "'heun'" in logs[0][2]

@pytest.mark.standalone_compatible
def test_subexpressions_basic():
    """
    Make sure that the integration of a (non-stochastic) differential equation
    does not depend on whether it's formulated using subexpressions.
    """
    # no subexpression
    eqs1 = 'dv/dt = (-v + sin(2*pi*100*Hz*t)) / (10*ms) : 1'
    # same with subexpression
    eqs2 = """dv/dt = I / (10*ms) : 1
              I = -v + sin(2*pi*100*Hz*t): 1"""
    method = 'euler'
    G1 = NeuronGroup(1, eqs1, method=method)
    G1.v = 1
    G2 = NeuronGroup(1, eqs2, method=method)
    G2.v = 1
    mon1 = StateMonitor(G1, 'v', record=True)
    mon2 = StateMonitor(G2, 'v', record=True)
    run(10*ms)
    assert_equal(mon1.v, mon2.v, f'Results for method {method} differed!')


def test_subexpressions():
    """
    Make sure that the integration of a (non-stochastic) differential equation
    does not depend on whether it's formulated using subexpressions.
    """
    # no subexpression
    eqs1 = 'dv/dt = (-v + sin(2*pi*100*Hz*t)) / (10*ms) : 1'
    # same with subexpression
    eqs2 = """dv/dt = I / (10*ms) : 1
              I = -v + sin(2*pi*100*Hz*t): 1"""
    
    methods = ['exponential_euler', 'rk2', 'rk4']  # euler is tested in test_subexpressions_basic
    for method in methods:
        G1 = NeuronGroup(1, eqs1, method=method)
        G1.v = 1
        G2 = NeuronGroup(1, eqs2, method=method)
        G2.v = 1
        mon1 = StateMonitor(G1, 'v', record=True)
        mon2 = StateMonitor(G2, 'v', record=True)
        net = Network(G1, mon1, G2, mon2)
        net.run(10*ms)
        assert_equal(mon1.v, mon2.v, f'Results for method {method} differed!')


@pytest.mark.codegen_independent
def test_locally_constant_check():
    default_dt = defaultclock.dt
    # The linear state update can handle additive time-dependent functions
    # (e.g. a TimedArray) but only if it can be safely assumed that the function
    # is constant over a single time check
    ta0 = TimedArray(np.array([1]), dt=default_dt)  # ok
    ta1 = TimedArray(np.array([1]), dt=2*default_dt)  # ok
    ta2 = TimedArray(np.array([1]), dt=default_dt/2)  # not ok
    ta3 = TimedArray(np.array([1]), dt=default_dt*1.5)  # not ok

    for ta_func, ok in zip([ta0, ta1, ta2, ta3], [True, True, False, False]):
        # additive
        G = NeuronGroup(1, 'dv/dt = -v/(10*ms) + ta(t)*Hz : 1',
                        method='exact', namespace={'ta': ta_func})
        net = Network(G)
        if ok:
            # This should work
            net.run(0*ms)
        else:
            # This should not
            with catch_logs():
                with pytest.raises(BrianObjectException) as exc:
                    net.run(0 * ms)
                    assert exc.errisinstance(UnsupportedEquationsException)

        # multiplicative
        G = NeuronGroup(1, 'dv/dt = -v*ta(t)/(10*ms) : 1',
                        method='exact', namespace={'ta': ta_func})
        net = Network(G)
        if ok:
            # This should work
            net.run(0*ms)
        else:
            # This should not
            with catch_logs():
                with pytest.raises(BrianObjectException) as exc:
                    net.run(0*ms)
                    assert exc.errisinstance(UnsupportedEquationsException)

    # If the argument is more than just "t", we cannot guarantee that it is
    # actually locally constant
    G = NeuronGroup(1, 'dv/dt = -v*ta(t/2.0)/(10*ms) : 1',
                        method='exact', namespace={'ta': ta0})
    net = Network(G)
    with pytest.raises(BrianObjectException) as exc:
        net.run(0*ms)
    assert exc_isinstance(exc, UnsupportedEquationsException)

    # Arbitrary functions are not constant over a time step
    G = NeuronGroup(1, 'dv/dt = -v/(10*ms) + sin(2*pi*100*Hz*t)*Hz : 1',
                    method='exact')
    net = Network(G)
    with pytest.raises(BrianObjectException) as exc:
        net.run(0*ms)
    assert exc_isinstance(exc, UnsupportedEquationsException)

    # Stateful functions aren't either
    G = NeuronGroup(1, 'dv/dt = -v/(10*ms) + rand()*Hz : 1',
                    method='exact')
    net = Network(G)
    with pytest.raises(BrianObjectException) as exc:
        net.run(0*ms)
    assert exc_isinstance(exc, UnsupportedEquationsException)

    # Neither is "t" itself
    G = NeuronGroup(1, 'dv/dt = -v/(10*ms) + t/second**2 : 1', method='exact')
    net = Network(G)
    with pytest.raises(BrianObjectException) as exc:
        net.run(0*ms)
    assert exc_isinstance(exc, UnsupportedEquationsException)

    # But if the argument is not referring to t, all should be well
    G = NeuronGroup(1, 'dv/dt = -v/(10*ms) + sin(2*pi*100*Hz*5*second)*Hz : 1',
                    method='exact')
    net = Network(G)
    net.run(0*ms)


def test_refractory():
    # Compare integration with and without the addition of refractoriness --
    # note that the cell here is not spiking, so it should never be in the
    # refractory period and therefore the results should be exactly identical
    # with and without (unless refractory)
    eqs_base = 'dv/dt = -v/(10*ms) : 1'
    for method in ['linear', 'exact', 'independent', 'euler', 'exponential_euler', 'rk2', 'rk4']:
        G_no_ref = NeuronGroup(10, eqs_base, method=method)
        G_no_ref.v = '(i+1)/11.'
        G_ref = NeuronGroup(10, f"{eqs_base}(unless refractory)",
                            refractory=1*ms, method=method)
        G_ref.v = '(i+1)/11.'
        net = Network(G_ref, G_no_ref)
        net.run(10*ms)
        assert_allclose(G_no_ref.v[:], G_ref.v[:],
                        err_msg=('Results with and without refractoriness '
                                 'differ for method %s.') % method)


def test_refractory_stochastic(fake_randn_randn_fixture):

    eqs_base = 'dv/dt = -v/(10*ms) + second**-.5*xi : 1'

    for method in ['euler', 'heun', 'milstein']:
        G_no_ref = NeuronGroup(10, eqs_base, method=method)
        G_no_ref.v = '(i+1)/11.'
        G_ref = NeuronGroup(10, f"{eqs_base} (unless refractory)",
                            refractory=1*ms, method=method)
        G_ref.v = '(i+1)/11.'
        net = Network(G_ref, G_no_ref)
        net.run(10*ms)
        assert_allclose(G_no_ref.v[:], G_ref.v[:],
                        err_msg=('Results with and without refractoriness '
                                 'differ for method %s.') % method)

@pytest.mark.standalone_compatible
def test_check_for_invalid_values_linear_integrator():
    # A differential equation that cannot be solved by the linear
    # integrator should return nan values to warn the user, and not silently
    # return incorrect values. See discussion on
    # https://github.com/brian-team/brian2/issues/626
    a = 0.0 / ms
    b = 1.0 / ms
    c = -0.5 / ms
    d = -0.1 / ms
    eqs = """
    dx/dt = a * x + b * y : 1
    dy/dt = c * x + d * y : 1
    """
    G = NeuronGroup(1, eqs, threshold='x > 100', reset='x = 0', method='exact',
                    method_options={'simplify': False})
    G.x = 1
    BrianLogger._log_messages.clear() # because the log message is set to be shown only once
    with catch_logs() as clog:
        try:
            run(1*ms)
            # this check allows for the possibility that we improve the linear
            # integrator in the future so that it can handle this equation
            if numpy.isnan(G.x[0]):
                assert 'invalid_values' in repr(clog)
            else:
                assert G.x[0] != 0
        except BrianObjectException as exc:
            assert isinstance(exc.__cause__, UnsupportedEquationsException)


if __name__ == '__main__':
    from brian2 import prefs

    import time
    start = time.time()

    test_determination()
    test_explicit_stateupdater_parsing()
    test_non_autonomous_equations()
    test_str_repr()
    test_multiplicative_noise()
    test_multiple_noise_variables_basic()
    test_multiple_noise_variables_extended()
    test_temporary_variables()
    test_temporary_variables2()
    test_integrator_code()
    test_integrator_code2()
    test_illegal_calls()
    test_priority()
    test_registration()
    test_subexpressions()
    test_locally_constant_check()
    test_refractory()
    # # Need the fake random number generator from tests/conftest.py
    # test_refractory_stochastic()
    # test_multiple_noise_variables_deterministic_noise()
    # test_pure_noise_deterministic()
    test_check_for_invalid_values_linear_integrator()
    print('Tests took', time.time()-start)
