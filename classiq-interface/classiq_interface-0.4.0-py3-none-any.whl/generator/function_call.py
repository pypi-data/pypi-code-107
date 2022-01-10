from __future__ import annotations

import random
import string
from typing import Dict, KeysView, List, Optional

import pydantic

from classiq_interface.generator import function_param_list, function_params as f_params
from classiq_interface.generator.user_defined_function_params import CustomFunction
from classiq_interface.helpers.custom_pydantic_types import pydanticNonEmptyString

_SUFFIX_LEN = 6
BAD_FUNCTION_ERROR_MSG = "Unknown function"
BAD_INPUT_ERROR_MSG = "Bad input name given"
BAD_OUTPUT_ERROR_MSG = "Bad output name given"


class FunctionCall(pydantic.BaseModel):
    function: str = pydantic.Field(
        default="", description="The function that is called"
    )
    function_params: f_params.FunctionParams = pydantic.Field(
        description="The parameters necessary for defining the function"
    )
    is_inverse: bool = pydantic.Field(
        default=False, description="call to function inverse"
    )
    inputs: Dict[pydanticNonEmptyString, pydanticNonEmptyString] = pydantic.Field(
        default_factory=dict,
        description="A mapping from the input name to the wire it connects to",
    )
    outputs: Dict[pydanticNonEmptyString, pydanticNonEmptyString] = pydantic.Field(
        default_factory=dict,
        description="A mapping from the output name to the wire it connects to",
    )

    name: Optional[pydanticNonEmptyString] = pydantic.Field(
        default=None,
        description="The name of the function call. Determined automatically.",
    )

    @pydantic.validator("name", always=True)
    def create_name(cls, name, values):
        function = values.get("function")
        params = values.get("function_params")
        if not function or params is None:
            return name

        suffix = "".join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(_SUFFIX_LEN)
        )
        if isinstance(params, CustomFunction):
            return f"{params.name}_{suffix}"
        return f"{function}_{suffix}"

    @pydantic.validator("function_params", pre=True)
    def parse_function_params(cls, function_params, values):
        if isinstance(function_params, f_params.FunctionParams):
            values["function"] = type(function_params).__name__
            return function_params

        function = values.get("function")
        if not function:
            raise ValueError(
                "The function field must be provided to deduce function type"
            )

        func_class = [
            seg
            for seg in function_param_list.get_function_param_list()
            if seg.__name__ == function
        ]

        if not func_class:
            raise ValueError(f"{BAD_FUNCTION_ERROR_MSG}: {function}")

        return func_class[0].parse_obj(function_params)

    @staticmethod
    def _validate_input_names(
        params: f_params.FunctionParams, inputs: Dict[str, str], is_inverse: bool
    ) -> None:
        invalid_names = FunctionCall._get_invalid_io_names(
            inputs.keys(), params, f_params.input_io(is_inverse)
        )
        if invalid_names:
            raise ValueError(f"{BAD_INPUT_ERROR_MSG}: {invalid_names}")

    @pydantic.validator("inputs")
    def validate_inputs(cls, inputs, values):
        params = values.get("function_params")
        is_inverse = values.get("is_inverse")
        if params is None:
            return inputs
        if isinstance(params, CustomFunction):
            return inputs
        cls._validate_input_names(params=params, inputs=inputs, is_inverse=is_inverse)
        return inputs

    @staticmethod
    def _validate_output_names(
        params: f_params.FunctionParams, outputs: Dict[str, str], is_inverse: bool
    ) -> None:
        invalid_names = FunctionCall._get_invalid_io_names(
            outputs.keys(), params, f_params.output_io(is_inverse)
        )
        if invalid_names:
            raise ValueError(f"{BAD_OUTPUT_ERROR_MSG}: {invalid_names}")

    @pydantic.validator("outputs")
    def validate_outputs(cls, outputs, values):
        params = values.get("function_params")
        is_inverse = values.get("is_inverse")
        if params is None:
            return outputs
        if isinstance(params, CustomFunction):
            return outputs
        cls._validate_output_names(
            params=params, outputs=outputs, is_inverse=is_inverse
        )
        return outputs

    @staticmethod
    def _get_invalid_io_names(
        names: KeysView[str], params: f_params.FunctionParams, io: f_params.IO
    ) -> List[str]:
        return [name for name in names if not params.is_valid_io_name(name, io)]

    def validate_custom_function_io(self) -> None:
        if not isinstance(self.function_params, CustomFunction):
            raise AssertionError("CustomFunction object expected.")
        FunctionCall._validate_input_names(
            params=self.function_params, inputs=self.inputs, is_inverse=self.is_inverse
        )
        FunctionCall._validate_output_names(
            params=self.function_params,
            outputs=self.outputs,
            is_inverse=self.is_inverse,
        )

    def inverse(self) -> FunctionCall:
        return FunctionCall(
            function=self.function,
            function_params=self.function_params,
            inputs=self.outputs,
            outputs=self.inputs,
            name=self.name,
            is_inverse=not self.is_inverse,
        )
