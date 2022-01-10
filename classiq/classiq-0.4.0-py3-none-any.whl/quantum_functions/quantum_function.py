# type: ignore[union-attr]
import sys
from types import FunctionType
from typing import Callable, Dict, List, Tuple, _GenericAlias

if sys.version_info >= (3, 9):
    from types import GenericAlias
else:
    GenericAlias = _GenericAlias

from classiq_interface.generator.functions import (
    FunctionData,
    FunctionImplementation,
    Register,
)
from classiq_interface.generator.synthesis_metrics import WireRole as Role

from classiq.quantum_functions.annotation_parser import (
    AnnotationParser,
    get_annotation_role,
)
from classiq.quantum_functions.function_parser import (
    FunctionParser,
    convert_callable_to_function,
)


class QuantumFunction:
    def __init__(self):
        self._function_data = None

    @staticmethod
    def _generate_single_register(
        first_qubit: int, name: str, obj: GenericAlias
    ) -> Tuple[Register]:
        qreg_size = obj.size

        qubits = tuple(range(first_qubit, first_qubit + qreg_size))

        return Register(
            name=name,
            qubits=qubits,
        )

    @classmethod
    def _generate_registers(
        cls, input_names, input_values, output_values
    ) -> Dict[Role, Tuple[Register, ...]]:
        registers: Dict[Role, List[Register]] = {k: list() for k in Role}

        qubit_counter = 0
        for input_name, input_annotation in zip(input_names, input_values):
            role = get_annotation_role(
                annotation=input_annotation, default_role=Role.INPUT
            )

            registers[role].append(
                cls._generate_single_register(
                    first_qubit=qubit_counter,
                    name=input_name,
                    obj=input_annotation,
                )
            )
            qubit_counter += input_annotation.size

        qubit_counter = 0
        for input_name, output_annotation in zip(input_names, output_values):
            role = get_annotation_role(
                annotation=output_annotation, default_role=Role.OUTPUT
            )
            if role == Role.AUXILIARY:
                qubit_counter += output_annotation.size
                continue

            registers[role].append(
                cls._generate_single_register(
                    first_qubit=qubit_counter,
                    name=input_name,
                    obj=output_annotation,
                )
            )
            qubit_counter += output_annotation.size

        return {k: tuple(v) for k, v in registers.items()}

    @classmethod
    def _create_implementation_from_function(
        cls, func: FunctionType
    ) -> FunctionImplementation:
        # Return value
        fp = FunctionParser(func)
        serialized_circuit = fp.extract_function_output()

        # Annotations
        ap = AnnotationParser(func)
        ap.parse()

        registers: Dict[Role, Tuple[Register]] = cls._generate_registers(
            input_names=ap.input_names,
            input_values=ap.input_values,
            output_values=ap.output_values,
        )

        implementation = FunctionImplementation(
            name=func.__name__,
            serialized_circuit=serialized_circuit,
            input_registers=registers[Role.INPUT],
            output_registers=registers[Role.OUTPUT],
            zero_input_registers=registers[Role.ZERO],
            auxiliary_registers=registers[Role.AUXILIARY],
        )
        return implementation

    def add_implementation(self, func: Callable) -> "QuantumFunction":
        func, func_name = convert_callable_to_function(func=func)

        implementation = self._create_implementation_from_function(func=func)

        if self._function_data is None:
            self._function_data = FunctionData(
                name=func_name,
                implementations=(implementation,),
            )
        else:
            new_implementations = self._function_data.implementations + (
                implementation,
            )
            self._function_data.implementations = (
                self._function_data.validate_implementations(new_implementations)
            )

        return self

    @property
    def function_data(self):
        return self._function_data
