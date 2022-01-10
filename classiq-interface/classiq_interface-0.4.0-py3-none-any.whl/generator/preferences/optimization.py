from enum import Enum

import pydantic

from classiq_interface.helpers.custom_pydantic_types import (
    pydanticNonOneProbabilityFloat,
)


class StatePrepOptimizationMethod(str, Enum):
    KL = "KL"
    L2 = "L2"
    L1 = "L1"
    MAX_PROBABILITY = "MAX_PROBABILITY"
    RANDOM = "RANDOM"


class OptimizationType(str, Enum):
    DEPTH = "depth"
    TWO_QUBIT_GATES = "two_qubit_gates"


class Optimization(pydantic.BaseModel):
    approximation_error: pydanticNonOneProbabilityFloat = 0.0
    optimization_type: OptimizationType = OptimizationType.DEPTH
