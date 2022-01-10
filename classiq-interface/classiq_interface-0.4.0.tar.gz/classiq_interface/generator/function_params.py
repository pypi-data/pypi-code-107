import abc
from enum import Enum
from typing import Any, List, Type

import pydantic

DEFAULT_OUTPUT_NAME = "OUT"
DEFAULT_INPUT_NAME = "IN"


class DefaultInputEnum(Enum):
    pass


class DefaultOutputEnum(Enum):
    OUT = DEFAULT_OUTPUT_NAME


class IO(Enum):
    Input = "Input"
    Output = "Output"


def input_io(is_inverse: bool) -> IO:
    if is_inverse:
        return IO.Output
    return IO.Input


def output_io(is_inverse: bool) -> IO:
    if is_inverse:
        return IO.Input
    return IO.Output


class FunctionParams(pydantic.BaseModel, abc.ABC):
    _input_enum: Type[Enum] = pydantic.PrivateAttr(default=None)
    _output_enum: Type[Enum] = pydantic.PrivateAttr(default=None)

    _input_names: List[str] = pydantic.PrivateAttr(default_factory=list)
    _output_names: List[str] = pydantic.PrivateAttr(default=[DEFAULT_OUTPUT_NAME])

    def __init__(self, **data: Any):
        super().__init__(**data)
        self.create_io_enums()
        self._create_io_names()

    def get_io_enum(self, io: IO) -> Type[Enum]:
        if io == IO.Input:
            return self._input_enum
        elif io == IO.Output:
            return self._output_enum
        raise AssertionError("Unsupported IO type")

    def get_io_names(self, io: IO, is_inverse: bool = False) -> List[str]:
        assert io == IO.Input or io == IO.Output, "Unsupported IO type"
        if (io == IO.Input) ^ is_inverse:
            return self._input_names
        else:
            return self._output_names

    def create_io_enums(self) -> None:
        pass

    def _create_io_names(self) -> None:
        if self._input_enum is None and self._output_enum is None:
            return

        self._input_names = list(self._input_enum.__members__.keys())
        self._output_names = list(self._output_enum.__members__.keys())

    def is_valid_io_name(self, name: str, io: IO) -> bool:
        return name in self.get_io_names(io)
