import logging

_logger = logging.getLogger(__name__)


class ClassiqError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        _logger.error(f"{message}\n")


class ClassiqExecutionError(ClassiqError):
    pass


class ClassiqGenerationError(ClassiqError):
    pass


class ClassiqAnalyzerError(ClassiqError):
    pass


class ClassiqAPIError(ClassiqError):
    pass


class ClassiqVersionError(ClassiqError):
    pass


class ClassiqValueError(ClassiqError, ValueError):
    pass


class ClassiqWiringError(ClassiqValueError):
    pass


class ClassiqQRegError(ClassiqValueError):
    pass


class ClassiqQFuncError(ClassiqValueError):
    pass


class ClassiqAuthenticationError(ClassiqError):
    pass


class ClassiqExpiredTokenError(ClassiqAuthenticationError):
    pass
