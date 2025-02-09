from enum import Enum


class ErrorType(Enum):
    Null = "Null"
    Validation = "Validation"
    Unauthorized = "Unauthorized"
    AccessDenied = "AccessDenied"
    NotFound = "NotFound"
    MethodNotAllowed = "MethodNotAllowed"
    Conflict = "Conflict"
    UnsupportedMediaType = "UnsupportedMediaType"
    Unexpected = "Unexpected"
    Unavailable = "Unavailable"
