"""Function library module, implementing facilities for adding user defined functions to the Classiq platform."""

from typing import Dict, Tuple

from classiq_interface.generator.functions import (
    DEFAULT_FUNCTION_LIBRARY_NAME,
    FunctionData,
    FunctionLibraryData,
    FunctionType,
)
from classiq_interface.generator.user_defined_function_params import CustomFunction

from classiq.exceptions import ClassiqValueError


class FunctionLibrary:
    """Facility to manage functions."""

    def __init__(self, name: str = DEFAULT_FUNCTION_LIBRARY_NAME):
        """
        Args:
            name (:obj:`str`, optional): The name of the function library.
        """
        self._data = FunctionLibraryData(name=name)
        self._params: Dict[str, CustomFunction] = dict()

    def get_function(self, function_name: str) -> CustomFunction:
        return self._params[function_name]

    def add_function(
        self, function_data: FunctionData, override_existing_functions: bool = False
    ) -> CustomFunction:
        """Adds a function to the function library.

        Args:
            function_data (FunctionData): The function data object.
            override_existing_functions (:obj:`bool`, optional): Defaults to False.

        Returns:
            The custom function parameters.
        """

        function_name = function_data.name
        if (
            not override_existing_functions
            and function_name in self._data.function_dict
        ):
            raise ClassiqValueError("Cannot override existing functions.")

        if function_data.function_type == FunctionType.CompositeFunction:
            for call in function_data.logic_flow:
                if not isinstance(call.function_params, CustomFunction):
                    continue
                FunctionLibraryData.validate_function_in_library(
                    library=self._data,
                    function_params=call.function_params,
                    error_handler=ClassiqValueError,
                )

        self._data.function_dict[function_name] = function_data
        self._params[function_name] = self._to_params(function_data)
        return self.get_function(function_name=function_name)

    def remove_function(self, function_name: str) -> FunctionData:
        """Removes a function from the function library.

        Args:
            function_name (str): The name of the function.

        Returns:
            The removed function data.
        """
        self._params.pop(function_name)
        return self._data.function_dict.pop(function_name)

    @property
    def name(self) -> str:
        """The library name."""
        return self._data.name

    @property
    def function_names(self) -> Tuple[str, ...]:
        """Get a tuple of the names of the functions in the library.

        Returns:
            The names of the functions in the library.
        """
        return tuple(self._data.function_dict.keys())

    @property
    def data(self) -> FunctionLibraryData:
        return self._data

    @staticmethod
    def _to_params(data: FunctionData) -> CustomFunction:
        params = CustomFunction(name=data.name)
        params.generate_io_names(
            input_set=data.input_set,
            output_set=data.output_set,
        )
        return params
