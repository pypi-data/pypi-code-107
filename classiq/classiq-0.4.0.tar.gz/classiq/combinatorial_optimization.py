import asyncio
from typing import List, Optional

from pyomo.core import ConcreteModel

from classiq_interface import status
from classiq_interface.backend.backend_preferences import BackendPreferences
from classiq_interface.chemistry import operator
from classiq_interface.combinatorial_optimization import (
    model_serializer,
    optimization_problem,
    sense,
)
from classiq_interface.combinatorial_optimization.encoding_types import EncodingType
from classiq_interface.combinatorial_optimization.preferences import QAOAPreferences
from classiq_interface.executor.execution_preferences import OptimizerPreferences
from classiq_interface.executor.result import ExecutionData, ExecutionStatus
from classiq_interface.generator import result as generator_result
from classiq_interface.generator.result import GeneratedCircuit

from classiq import api_wrapper
from classiq.exceptions import (
    ClassiqError,
    ClassiqExecutionError,
    ClassiqGenerationError,
)


class CombinatorialOptimization:
    def __init__(
        self,
        model: ConcreteModel,
        qaoa_preferences: Optional[QAOAPreferences] = None,
        optimizer_preferences: Optional[OptimizerPreferences] = None,
        backend_preferences: Optional[BackendPreferences] = None,
        encoding_type: Optional[EncodingType] = None,
    ):
        self.is_maximization = sense.is_maximization(model)
        self._serialized_model = model_serializer.to_json(model, return_dict=True)

        arguments = {
            "serialized_model": self._serialized_model,
            "encoding_type": encoding_type,
        }
        if qaoa_preferences is not None:
            arguments["qaoa_preferences"] = qaoa_preferences
        if optimizer_preferences is not None:
            arguments["optimizer_preferences"] = optimizer_preferences
        if backend_preferences is not None:
            arguments["backend_preferences"] = backend_preferences

        self._problem = optimization_problem.OptimizationProblem(**arguments)

    def generate(self) -> GeneratedCircuit:
        return asyncio.run(self.generate_async())

    async def generate_async(self) -> GeneratedCircuit:
        """Async version of `generate`"""
        wrapper = api_wrapper.ApiWrapper()
        result = await wrapper.call_combinatorial_optimization_generate_task(
            problem=self._problem
        )

        if result.status != generator_result.GenerationStatus.SUCCESS:
            raise ClassiqGenerationError(f"Solving failed: {result.details}")

        return result.details

    def solve(self) -> ExecutionData:
        return asyncio.run(self.solve_async())

    async def solve_async(self) -> ExecutionData:
        """Async version of `solve`"""
        wrapper = api_wrapper.ApiWrapper()
        result = await wrapper.call_combinatorial_optimization_solve_task(
            problem=self._problem
        )

        if result.status != ExecutionStatus.SUCCESS:
            raise ClassiqExecutionError(f"Solving failed: {result.details}")

        return result.details

    def get_operator(self) -> operator.OperatorResult:
        return asyncio.run(self.get_operator_async())

    async def get_operator_async(self) -> operator.PauliOperator:
        """Async version of `get_operator`"""
        wrapper = api_wrapper.ApiWrapper()
        result = await wrapper.call_combinatorial_optimization_operator_task(
            problem=self._problem
        )

        if result.status != operator.OperatorStatus.SUCCESS:
            raise ClassiqError(f"Get operator failed: {result.details}")

        return result.details

    def get_objective(self) -> str:
        return asyncio.run(self.get_objective_async())

    async def get_objective_async(self) -> str:
        """Async version of `get_operator`"""
        wrapper = api_wrapper.ApiWrapper()
        result = await wrapper.call_combinatorial_optimization_objective_task(
            problem=self._problem
        )

        if result.status != status.Status.SUCCESS:
            raise ClassiqError(f"Get objective failed: {result.details}")

        return result.details

    def get_initial_point(self) -> List[float]:
        return asyncio.run(self.get_initial_point_async())

    async def get_initial_point_async(self) -> List[float]:
        """Async version of `get_initial_point`"""
        wrapper = api_wrapper.ApiWrapper()
        result = await wrapper.call_combinatorial_optimization_initial_point_task(
            problem=self._problem
        )

        if result.status != status.Status.SUCCESS:
            raise ClassiqError(f"Get inital point failed: {result.details}")

        return result.details
