from dataclasses import dataclass
from enum import Enum


class ErrorType(Enum):
    Null = "Null"
    Validation = "Validation"
    Unauthorized = "Unauthorized"
    Forbidden = "Forbidden"
    NotFound = "NotFound"
    MethodNotAllowed = "MethodNotAllowed"
    Conflict = "Conflict"
    UnsupportedMediaType = "UnsupportedMediaType"
    Unexpected = "Unexpected"
    Unavailable = "Unavailable"


@dataclass(frozen=True)
class Error:
    Null = 'Error(ErrorType.Null, "", "")'
    type: ErrorType
    code: str
    message: str

    @staticmethod
    def create(type: ErrorType, code: str, message: str) -> "Error":
        if type == ErrorType.Null:
            raise ValueError("Error type cannot be Null.")
        return Error(type, code, message)
