
import os

import pytest
from numpy.testing import assert_equal

from brian2 import *
from brian2.devices.device import reinit_and_delete, set_device, reset_device
from brian2.tests.utils import assert_allclose
from brian2.utils.logger import catch_logs


@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_cpp_standalone():
    set_device('cpp_standalone', build_on_run=False)
    ##### Define the model
    tau = 1*ms
    eqs = """
    dV/dt = (-40*mV-V)/tau : volt (unless refractory)
    """
    threshold = 'V>-50*mV'
    reset = 'V=-60*mV'
    refractory = 5*ms
    N = 1000
    
    G = NeuronGroup(N, eqs,
                    reset=reset,
                    threshold=threshold,
                    refractory=refractory,
                    name='gp')
    G.V = '-i*mV'
    M = SpikeMonitor(G)
    S = Synapses(G, G, 'w : volt', on_pre='V += w')
    S.connect('abs(i-j)<5 and i!=j')
    S.w = 0.5*mV
    S.delay = '0*ms'

    net = Network(G, M, S)
    net.run(100*ms)
    device.build(directory=None, with_output=False)
    # we do an approximate equality here because depending on minor details of how it was compiled, the results
    # may be slightly different (if -ffast-math is on)
    assert len(M.i)>=17000 and len(M.i)<=18000
    assert len(M.t) == len(M.i)
    assert M.t[0] == 0.
    reset_device()

@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_multiple_connects():
    set_device('cpp_standalone', build_on_run=False)
    G = NeuronGroup(10, 'v:1')
    S = Synapses(G, G, 'w:1')
    S.connect(i=[0], j=[0])
    S.connect(i=[1], j=[1])
    run(0*ms)
    device.build(directory=None, with_output=False)
    assert len(S) == 2 and len(S.w[:]) == 2
    reset_device()

@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_storing_loading():
    set_device('cpp_standalone', build_on_run=False)
    G = NeuronGroup(10, """v : volt
                           x : 1
                           n : integer
                           b : boolean""")
    v = np.arange(10)*volt
    x = np.arange(10, 20)
    n = np.arange(20, 30)
    b = np.array([True, False]).repeat(5)
    G.v = v
    G.x = x
    G.n = n
    G.b = b
    S = Synapses(G, G, """v_syn : volt
                          x_syn : 1
                          n_syn : integer
                          b_syn : boolean""")
    S.connect(j='i')
    S.v_syn = v
    S.x_syn = x
    S.n_syn = n
    S.b_syn = b
    run(0*ms)
    device.build(directory=None, with_output=False)
    assert_allclose(G.v[:], v)
    assert_allclose(S.v_syn[:], v)
    assert_allclose(G.x[:], x)
    assert_allclose(S.x_syn[:], x)
    assert_allclose(G.n[:], n)
    assert_allclose(S.n_syn[:], n)
    assert_allclose(G.b[:], b)
    assert_allclose(S.b_syn[:], b)
    reset_device()


@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
@pytest.mark.openmp
def test_openmp_consistency():
    previous_device = get_device()
    n_cells    = 100
    n_recorded = 10
    numpy.random.seed(42)
    taum       = 20 * ms
    taus       = 5 * ms
    Vt         = -50 * mV
    Vr         = -60 * mV
    El         = -49 * mV
    fac        = (60 * 0.27 / 10)
    gmax       = 20*fac
    dApre      = .01
    taupre     = 20 * ms
    taupost    = taupre
    dApost     = -dApre * taupre / taupost * 1.05
    dApost    *=  0.1*gmax
    dApre     *=  0.1*gmax

    connectivity = numpy.random.randn(n_cells, n_cells)
    sources      = numpy.random.randint(0, n_cells-1, 10*n_cells)
    # Only use one spike per time step (to rule out that a single source neuron
    # has more than one spike in a time step)
    times        = numpy.random.choice(numpy.arange(10*n_cells), 10*n_cells,
                                       replace=False)*ms
    v_init       = Vr + numpy.random.rand(n_cells) * (Vt - Vr)

    eqs  = Equations("""
    dv/dt = (g-(v-El))/taum : volt
    dg/dt = -g/taus         : volt
    """)

    results = {}

    for (n_threads, devicename) in [(0, 'runtime'),
                                    (0, 'cpp_standalone'),
                                    (1, 'cpp_standalone'),
                                    (2, 'cpp_standalone'),
                                    (3, 'cpp_standalone'),
                                    (4, 'cpp_standalone')]:
        set_device(devicename, build_on_run=False, with_output=False)
        Synapses.__instances__().clear()
        if devicename == 'cpp_standalone':
            reinit_and_delete()
        prefs.devices.cpp_standalone.openmp_threads = n_threads
        P    = NeuronGroup(n_cells, model=eqs, threshold='v>Vt', reset='v=Vr', refractory=5 * ms)
        Q    = SpikeGeneratorGroup(n_cells, sources, times)
        P.v  = v_init
        P.g  = 0 * mV
        S    = Synapses(P, P, 
                            model = """dApre/dt=-Apre/taupre    : 1 (event-driven)    
                                       dApost/dt=-Apost/taupost : 1 (event-driven)
                                       w                        : 1""", 
                            pre = """g     += w*mV
                                     Apre  += dApre
                                     w      = w + Apost""",
                            post = """Apost += dApost
                                      w      = w + Apre""")
        S.connect()
        
        S.w       = fac*connectivity.flatten()

        T         = Synapses(Q, P, model = "w : 1", on_pre="g += w*mV")
        T.connect(j='i')
        T.w       = 10*fac

        spike_mon = SpikeMonitor(P)
        rate_mon  = PopulationRateMonitor(P)
        state_mon = StateMonitor(S, 'w', record=np.arange(n_recorded), dt=0.1*second)
        v_mon     = StateMonitor(P, 'v', record=np.arange(n_recorded))

        run(0.2 * second, report='text')

        if devicename == 'cpp_standalone':
            device.build(directory=None, with_output=False)

        results[n_threads, devicename]      = {}
        results[n_threads, devicename]['w'] = state_mon.w
        results[n_threads, devicename]['v'] = v_mon.v
        results[n_threads, devicename]['s'] = spike_mon.num_spikes
        results[n_threads, devicename]['r'] = rate_mon.rate[:]

    for key1, key2 in [((0, 'runtime'), (0, 'cpp_standalone')),
                       ((1, 'cpp_standalone'), (0, 'cpp_standalone')),
                       ((2, 'cpp_standalone'), (0, 'cpp_standalone')),
                       ((3, 'cpp_standalone'), (0, 'cpp_standalone')),
                       ((4, 'cpp_standalone'), (0, 'cpp_standalone'))
                       ]:
        assert_allclose(results[key1]['w'], results[key2]['w'])
        assert_allclose(results[key1]['v'], results[key2]['v'])
        assert_allclose(results[key1]['r'], results[key2]['r'])
        assert_allclose(results[key1]['s'], results[key2]['s'])
    reset_device(previous_device)

@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_duplicate_names_across_nets():
    set_device('cpp_standalone', build_on_run=False)
    # In standalone mode, names have to be globally unique, not just unique
    # per network
    obj1 = BrianObject(name='name1')
    obj2 = BrianObject(name='name2')
    obj3 = BrianObject(name='name3')
    obj4 = BrianObject(name='name1')
    net1 = Network(obj1, obj2)
    net2 = Network(obj3, obj4)
    net1.run(0*ms)
    net2.run(0*ms)
    with pytest.raises(ValueError):
        device.build()

    reset_device()


@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
@pytest.mark.openmp
def test_openmp_scalar_writes():
    # Test that writing to a scalar variable only is done once in an OpenMP
    # setting (see github issue #551)
    set_device('cpp_standalone', build_on_run=False)
    prefs.devices.cpp_standalone.openmp_threads = 4
    G = NeuronGroup(10, 's : 1 (shared)')
    G.run_regularly('s += 1')
    run(defaultclock.dt)
    device.build(directory=None, with_output=False)
    assert_equal(G.s[:], 1.0)

    reset_device()


@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_time_after_run():
    set_device('cpp_standalone', build_on_run=False)
    # Check that the clock and network time after a run is correct, even if we
    # have not actually run the code yet (via build)
    G = NeuronGroup(10, 'dv/dt = -v/(10*ms) : 1')
    net = Network(G)
    assert_allclose(defaultclock.dt, 0.1*ms)
    assert_allclose(defaultclock.t, 0.*ms)
    assert_allclose(G.t, 0.*ms)
    assert_allclose(net.t, 0.*ms)
    net.run(10*ms)
    assert_allclose(defaultclock.t, 10.*ms)
    assert_allclose(G.t, 10.*ms)
    assert_allclose(net.t, 10.*ms)
    net.run(10*ms)
    assert_allclose(defaultclock.t, 20.*ms)
    assert_allclose(G.t, 20.*ms)
    assert_allclose(net.t, 20.*ms)
    device.build(directory=None, with_output=False)
    # Everything should of course still be accessible
    assert_allclose(defaultclock.t, 20.*ms)
    assert_allclose(G.t, 20.*ms)
    assert_allclose(net.t, 20.*ms)

    reset_device()

@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_array_cache():
    # Check that variables are only accessible from Python when they should be
    set_device('cpp_standalone', build_on_run=False)
    G = NeuronGroup(10, """dv/dt = -v / (10*ms) : 1
                           w : 1
                           x : 1
                           y : 1
                           z : 1 (shared)""",
                    threshold='v>1')
    S = Synapses(G, G, 'weight: 1', on_pre='w += weight')
    S.connect(p=0.2)
    S.weight = 7
    # All neurongroup values should be known
    assert_allclose(G.v, 0)
    assert_allclose(G.w, 0)
    assert_allclose(G.x, 0)
    assert_allclose(G.y, 0)
    assert_allclose(G.z, 0)
    assert_allclose(G.i, np.arange(10))

    # But the synaptic variable is not -- we don't know the number of synapses
    with pytest.raises(NotImplementedError):
        S.weight[:]

    # Setting variables with explicit values should not change anything
    G.v = np.arange(10)+1
    G.w = 2
    G.y = 5
    G.z = 7
    assert_allclose(G.v, np.arange(10)+1)
    assert_allclose(G.w, 2)
    assert_allclose(G.y, 5)
    assert_allclose(G.z, 7)

    # But setting with code should invalidate them
    G.x = 'i*2'
    with pytest.raises(NotImplementedError):
        G.x[:]

    # Make sure that the array cache does not allow to use incorrectly sized
    # values to pass
    with pytest.raises(ValueError):
        setattr(G, 'w', [0, 2])
    with pytest.raises(ValueError):
        G.w.__setitem__(slice(0, 4), [0, 2])

    run(10*ms)
    # v is now no longer known without running the network
    with pytest.raises(NotImplementedError):
        G.v[:]
    # Neither is w, it is updated in the synapse
    with pytest.raises(NotImplementedError):
        G.w[:]
    # However, no code touches y or z
    assert_allclose(G.y, 5)
    assert_allclose(G.z, 7)
    # i is read-only anyway
    assert_allclose(G.i, np.arange(10))

    # After actually running the network, everything should be accessible
    device.build(directory=None, with_output=False)
    assert all(G.v > 0)
    assert all(G.w > 0)
    assert_allclose(G.x, np.arange(10)*2)
    assert_allclose(G.y, 5)
    assert_allclose(G.z, 7)
    assert_allclose(G.i, np.arange(10))
    assert_allclose(S.weight, 7)

@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_run_with_debug():
    # We just want to make sure that it works for now (i.e. not fails with a
    # compilation or runtime error), capturing the output is actually
    # a bit involved to get right.
    set_device('cpp_standalone', build_on_run=True, debug=True,
               directory=None)
    group = NeuronGroup(1, 'v: 1', threshold='False')
    syn = Synapses(group, group, on_pre='v += 1')
    syn.connect()
    mon = SpikeMonitor(group)
    run(defaultclock.dt)


@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_run_with_synapses_and_profile():
    set_device('cpp_standalone', build_on_run=True, directory=None)
    group = NeuronGroup(1, 'v: 1', threshold='False', reset='')
    syn = Synapses(group, group, on_pre='v += 1')
    syn.connect()
    mon = SpikeMonitor(group)
    run(defaultclock.dt, profile=True)


@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_changing_profile_arg():
    set_device('cpp_standalone', build_on_run=False)
    G = NeuronGroup(10000, 'v : 1')
    op1 = G.run_regularly('v = exp(-v)', name='op1')
    op2 = G.run_regularly('v = exp(-v)', name='op2')
    op3 = G.run_regularly('v = exp(-v)', name='op3')
    op4 = G.run_regularly('v = exp(-v)', name='op4')
    # Op 1 is active only during the first profiled run
    # Op 2 is active during both profiled runs
    # Op 3 is active only during the second profiled run
    # Op 4 is never active (only during the unprofiled run)
    op1.active = True
    op2.active = True
    op3.active = False
    op4.active = False
    run(1000*defaultclock.dt, profile=True)
    op1.active = True
    op2.active = True
    op3.active = True
    op4.active = True
    run(1000*defaultclock.dt, profile=False)
    op1.active = False
    op2.active = True
    op3.active = True
    op4.active = False
    run(1000*defaultclock.dt, profile=True)
    device.build(directory=None, with_output=False)
    profiling_dict = dict(magic_network.profiling_info)
    # Note that for now, C++ standalone creates a new CodeObject for every run,
    # which is most of the time unnecessary (this is partly due to the way we
    # handle constants: they are included as literals in the code but they can
    # change between runs). Therefore, the profiling info is potentially
    # difficult to interpret
    assert len(profiling_dict) == 4  # 2 during first run, 2 during last run
    # The two code objects that were executed during the first run
    assert ('op1_codeobject' in profiling_dict and
            profiling_dict['op1_codeobject'] > 0*second)
    assert ('op2_codeobject' in profiling_dict and
            profiling_dict['op2_codeobject'] > 0*second)
    # Four code objects were executed during the second run, but no profiling
    # information was saved
    for name in ['op1_codeobject_1', 'op2_codeobject_1', 'op3_codeobject',
                 'op4_codeobject']:
        assert name not in profiling_dict
    # Two code objects were exectued during the third run
    assert ('op2_codeobject_2' in profiling_dict and
            profiling_dict['op2_codeobject_2'] > 0*second)
    assert ('op3_codeobject_1' in profiling_dict and
            profiling_dict['op3_codeobject_1'] > 0*second)


@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_profile_via_set_device_arg():
    set_device('cpp_standalone', build_on_run=False, profile=True)
    G = NeuronGroup(10000, 'v : 1')
    op1 = G.run_regularly('v = exp(-v)', name='op1')
    op2 = G.run_regularly('v = exp(-v)', name='op2')
    op3 = G.run_regularly('v = exp(-v)', name='op3')
    op4 = G.run_regularly('v = exp(-v)', name='op4')
    # Op 1 is active only during the first profiled run
    # Op 2 is active during both profiled runs
    # Op 3 is active only during the second profiled run
    # Op 4 is never active (only during the unprofiled run)
    op1.active = True
    op2.active = True
    op3.active = False
    op4.active = False
    run(1000*defaultclock.dt)  # Should use profile=True via set_device
    op1.active = True
    op2.active = True
    op3.active = True
    op4.active = True
    run(1000*defaultclock.dt, profile=False)
    op1.active = False
    op2.active = True
    op3.active = True
    op4.active = False
    run(1000*defaultclock.dt, profile=True)
    device.build(directory=None, with_output=False)
    profiling_dict = dict(magic_network.profiling_info)
    # Note that for now, C++ standalone creates a new CodeObject for every run,
    # which is most of the time unnecessary (this is partly due to the way we
    # handle constants: they are included as literals in the code but they can
    # change between runs). Therefore, the profiling info is potentially
    # difficult to interpret
    assert len(profiling_dict) == 4  # 2 during first run, 2 during last run
    # The two code objects that were executed during the first run
    assert ('op1_codeobject' in profiling_dict and
            profiling_dict['op1_codeobject'] > 0*second)
    assert ('op2_codeobject' in profiling_dict and
            profiling_dict['op2_codeobject'] > 0*second)
    # Four code objects were executed during the second run, but no profiling
    # information was saved
    for name in ['op1_codeobject_1', 'op2_codeobject_1', 'op3_codeobject',
                 'op4_codeobject']:
        assert name not in profiling_dict
    # Two code objects were exectued during the third run
    assert ('op2_codeobject_2' in profiling_dict and
            profiling_dict['op2_codeobject_2'] > 0*second)
    assert ('op3_codeobject_1' in profiling_dict and
            profiling_dict['op3_codeobject_1'] > 0*second)


@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_delete_code_data():
    set_device('cpp_standalone', build_on_run=True, directory=None)
    group = NeuronGroup(10, 'dv/dt = -v / (10*ms) : volt', method='exact')
    group.v = np.arange(10)*mV  # uses the static array mechanism
    run(defaultclock.dt)
    results_dir = os.path.join(device.project_dir, 'results')
    assert os.path.exists(results_dir) and os.path.isdir(results_dir)
    # There should be 3 files for the clock, 2 for the neurongroup (index + v),
    # and the "last_run_info.txt" file
    assert len(os.listdir(results_dir)) == 6
    device.delete(data=True, code=False, directory=False)
    assert os.path.exists(results_dir) and os.path.isdir(results_dir)
    assert len(os.listdir(results_dir)) == 0
    assert len(os.listdir(os.path.join(device.project_dir, 'static_arrays'))) > 0
    assert len(os.listdir(os.path.join(device.project_dir, 'code_objects'))) > 0
    device.delete(data=False, code=True, directory=False)
    assert len(os.listdir(os.path.join(device.project_dir, 'static_arrays'))) == 0
    assert len(os.listdir(os.path.join(device.project_dir, 'code_objects'))) == 0


@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_delete_directory():
    set_device('cpp_standalone', build_on_run=True, directory=None)
    group = NeuronGroup(10, 'dv/dt = -v / (10*ms) : volt', method='exact')
    group.v = np.arange(10)*mV  # uses the static array mechanism
    run(defaultclock.dt)
    # Add a new file
    dummy_file = os.path.join(device.project_dir, 'results', 'dummy.txt')
    open(dummy_file, 'w').flush()
    assert os.path.isfile(dummy_file)
    with catch_logs() as logs:
        device.delete(directory=True)
    assert len(logs) == 1
    assert os.path.isfile(dummy_file)
    with catch_logs() as logs:
        device.delete(directory=True, force=True)
    assert len(logs) == 0
    # everything should be deleted
    assert not os.path.exists(device.project_dir)

@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_multiple_standalone_runs():
    # see github issue #1189
    set_device('cpp_standalone', directory=None)

    network = Network()
    Pe = NeuronGroup(1, 'v : 1', threshold='False')
    C_ee = Synapses(Pe, Pe, on_pre='v += 1')
    C_ee.connect()
    network.add(Pe, C_ee)
    network.run(defaultclock.dt)

    device.reinit()
    device.activate(directory=None)

    network2 = Network()
    Pe = NeuronGroup(1, 'v : 1', threshold='False')
    C_ee = Synapses(Pe, Pe, on_pre='v += 1')
    C_ee.connect()
    network2.add(Pe, C_ee)
    network2.run(defaultclock.dt)


@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_continued_standalone_runs():
    # see github issue #1237
    set_device('cpp_standalone', build_on_run=False)

    source = SpikeGeneratorGroup(1, [0], [0]*ms)
    target = NeuronGroup(1, 'v : 1')
    C_ee = Synapses(source, target, on_pre='v += 1', delay=2*ms)
    C_ee.connect()
    run(1*ms)
    # Spike has not been delivered yet
    run(2*ms)

    device.build(directory=None)
    assert target.v[0] == 1  # Make sure the spike got delivered


@pytest.mark.cpp_standalone
@pytest.mark.standalone_only
def test_constant_replacement():
    # see github issue #1276
    set_device('cpp_standalone')
    x = 42
    G = NeuronGroup(1, 'y : 1')
    G.y = 'x'
    run(0*ms)
    assert G.y[0] == 42.


if __name__=='__main__':
    for t in [
             test_cpp_standalone,
             test_multiple_connects,
             test_storing_loading,
             test_openmp_consistency,
             test_duplicate_names_across_nets,
             test_openmp_scalar_writes,
             test_time_after_run,
             test_array_cache,
             test_run_with_debug,
             test_changing_profile_arg,
             test_profile_via_set_device_arg,
             test_delete_code_data,
             test_delete_directory,
             test_multiple_standalone_runs
             ]:
        t()
        reinit_and_delete()
