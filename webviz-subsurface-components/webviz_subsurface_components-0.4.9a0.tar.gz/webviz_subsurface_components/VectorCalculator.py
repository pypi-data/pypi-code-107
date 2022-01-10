# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class VectorCalculator(Component):
    """A VectorCalculator component.
VectorCalculator is a component that allows to calculate new vectors by creating a mathematical expression
based existing vectors.

New calcualted vectors are created by writing a mathematical equation with single character variables,
where each variable is assigned a vector from the set of existing vectors.

The component provides a list of valid expressions which can be used externally to calculate the wanted
vector data.

The component can handle validation of the mathematical equations internally or externally. External
validation can be utilized to obtain coherent parsing in the component and the user.

Keyword arguments:

- id (string; required):
    The ID used to identify this component in Dash callbacks.

- expressions (list of dicts; required):
    Pre-defined vector calculator expressions. Each expression consist
    of an expression name, mathematical expression string with
    variables and a map of characther variables and the corresponding
    vector name.

    `expressions` is a list of dicts with keys:

    - description (string; optional)

    - expression (string; required)

    - id (string; required)

    - isDeletable (boolean; required)

    - isValid (boolean; required)

    - name (string; required)

    - variableVectorMap (list of dicts; required)

        `variableVectorMap` is a list of dicts with keys:

        - variableName (string; required)

        - vectorName (string; required)

- externalParseData (dict; optional):
    Data for external parsing of mathematical expression.

    `externalParseData` is a dict with keys:

    - expression (string; required)

    - id (string; required)

    - isValid (boolean; required)

    - variables (list of strings; required)

- isDashControlled (boolean; default False):
    Set True when component is utilized by Dash plugin. When
    controlled in Dash, the user must provide an external expression
    parser responsible for validation of the active mathematical
    expression and provide the parsing data for the externalParseData
    prop. If set to False, an internal JS-parser library is utilized
    for validation of the mathematical expressions.

- maxExpressionDescriptionLength (number; default 50):
    Set maximal number of characters for expression description text.

- vectors (list; required):
    Existing vectors for vector selector."""
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, vectors=Component.REQUIRED, expressions=Component.REQUIRED, isDashControlled=Component.UNDEFINED, maxExpressionDescriptionLength=Component.UNDEFINED, externalParseData=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'expressions', 'externalParseData', 'isDashControlled', 'maxExpressionDescriptionLength', 'vectors']
        self._type = 'VectorCalculator'
        self._namespace = 'webviz_subsurface_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'expressions', 'externalParseData', 'isDashControlled', 'maxExpressionDescriptionLength', 'vectors']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['id', 'vectors', 'expressions']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(VectorCalculator, self).__init__(**args)
