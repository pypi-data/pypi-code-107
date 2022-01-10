import pydantic

from classiq_interface.combinatorial_optimization.solver_types import QSolver


class QAOAPreferences(pydantic.BaseModel):
    qsolver: QSolver = pydantic.Field(
        default=QSolver.QAOAPenalty,
        description="Indicates whether to use QAOA with penalty terms or constrained QAOA.",
    )
    qaoa_reps: pydantic.PositiveInt = pydantic.Field(
        default=1, description="Number of layers in qaoa ansatz."
    )
    penalty_energy: float = pydantic.Field(
        default=None,
        description="Penalty energy for invalid solutions. The value affects "
        "the converges rate. Small positive values are preferred",
    )

    @pydantic.validator("penalty_energy", pre=True, always=True)
    def check_penalty_energy(cls, penalty_energy, values):
        qsolver = values.get("qsolver")
        if penalty_energy is not None and qsolver != QSolver.QAOAPenalty:
            raise ValueError("Use penalty_energy only for QSolver.QAOAPenalty.")

        if penalty_energy is None and qsolver == QSolver.QAOAPenalty:
            penalty_energy = 2

        return penalty_energy
