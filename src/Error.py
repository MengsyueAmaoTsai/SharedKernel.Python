from dataclasses import dataclass
from enum import Enum
from typing import overload


class ErrorType(Enum):
    """
    Enum representing different types of errors.
    """

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


@dataclass(frozen=True)
class Error:
    """
    Represents an error with a specific type, code, and message.
    """

    type: ErrorType
    code: str
    message: str

    Null: "Error" = None

    @staticmethod
    def create(type: ErrorType, code: str, message: str) -> "Error":
        """
        Creates an instance of Error with the specified type, code, and message.

        Args:
            type (ErrorType): The type of the error.
            code (str): The error code.
            message (str): The error message.

        Returns:
            Error: An instance of Error.

        Raises:
            ValueError: If the type is ErrorType.Null or the code is empty.
        """
        if type == ErrorType.Null:
            raise ValueError("Error type cannot be Null.")

        if not code:
            raise ValueError("Error code cannot be null or empty.")

        return Error(type, code, message)

    @overload
    @classmethod
    def invalid(cls, code: str, message: str) -> "Error":
        """
        Creates a new validation error with the specified code and message.

        Args:
            code (str): The error code.
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @overload
    @classmethod
    def invalid(cls, message: str) -> "Error":
        """
        Creates a new validation error with the specified message.

        Args:
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @classmethod
    def invalid(cls, code_or_message: str, message: str = "") -> "Error":
        if not message:
            return cls.create(
                ErrorType.Validation, ErrorType.Validation.value, code_or_message
            )
        return cls.create(ErrorType.Validation, code_or_message, message)

    @overload
    @classmethod
    def unauthorized(cls, code: str, message: str) -> "Error":
        """
        Creates a new unauthorize error with the specified message.

        Args:
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @overload
    @classmethod
    def unauthorized(cls, message: str) -> "Error":
        """
        Creates a new unauthorize error with the specified message.

        Args:
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @classmethod
    def unauthorized(cls, code_or_message: str, message: str = "") -> "Error":
        if not message:
            return cls.create(
                ErrorType.Unauthorized, ErrorType.Unauthorized.value, code_or_message
            )
        return cls.create(ErrorType.Unauthorized, code_or_message, message)

    @overload
    @classmethod
    def access_denied(cls, code: str, message: str) -> "Error":
        """
        Creates a new access denied error with the specified code and message.

        Args:
            code (str): The error code.
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @overload
    @classmethod
    def access_denied(cls, message: str) -> "Error":
        """
        Creates a new access denied error with the specified message.

        Args:
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @classmethod
    def access_denied(cls, code_or_message: str, message: str = "") -> "Error":
        if not message:
            return cls.create(
                ErrorType.AccessDenied, ErrorType.AccessDenied.value, code_or_message
            )
        return cls.create(ErrorType.AccessDenied, code_or_message, message)

    @overload
    @classmethod
    def not_found(cls, code: str, message: str) -> "Error":
        """
        Creates a new not found error with the specified code and message.

        Args:
            code (str): The error code.
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @overload
    @classmethod
    def not_found(cls, message: str) -> "Error":
        """
        Creates a new not found error with the specified message.

        Args:
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @classmethod
    def not_found(cls, code_or_message: str, message: str = "") -> "Error":
        if not message:
            return cls.create(
                ErrorType.NotFound, ErrorType.NotFound.value, code_or_message
            )
        return cls.create(ErrorType.NotFound, code_or_message, message)

    @overload
    @classmethod
    def method_not_allowed(cls, code: str, message: str) -> "Error":
        """
        Creates a new method not allowed error with the specified code and message.

        Args:
            code (str): The error code.
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @overload
    @classmethod
    def method_not_allowed(cls, message: str) -> "Error":
        """
        Creates a new method not allowed error with the specified message.

        Args:
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @classmethod
    def method_not_allowed(cls, code_or_message: str, message: str = "") -> "Error":
        if not message:
            return cls.create(
                ErrorType.MethodNotAllowed,
                ErrorType.MethodNotAllowed.value,
                code_or_message,
            )
        return cls.create(ErrorType.MethodNotAllowed, code_or_message, message)

    @overload
    @classmethod
    def conflict(cls, code: str, message: str) -> "Error":
        """
        Creates a new conflict error with the specified code and message.

        Args:
            code (str): The error code.
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @overload
    @classmethod
    def conflict(cls, message: str) -> "Error":
        """
        Creates a new conflict error with the specified message.

        Args:
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @classmethod
    def conflict(cls, code_or_message: str, message: str = "") -> "Error":
        if not message:
            return cls.create(
                ErrorType.Conflict, ErrorType.Conflict.value, code_or_message
            )
        return cls.create(ErrorType.Conflict, code_or_message, message)

    @overload
    @classmethod
    def unsupported_media_type(cls, code: str, message: str) -> "Error":
        """
        Creates a new unsupported media type error with the specified code and message.

        Args:
            code (str): The error code.
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @overload
    @classmethod
    def unsupported_media_type(cls, message: str) -> "Error":
        """
        Creates a new unsupported media type error with the specified message.

        Args:
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @classmethod
    def unsupported_media_type(cls, code_or_message: str, message: str = "") -> "Error":
        if not message:
            return cls.create(
                ErrorType.UnsupportedMediaType,
                ErrorType.UnsupportedMediaType.value,
                code_or_message,
            )
        return cls.create(ErrorType.UnsupportedMediaType, code_or_message, message)

    @overload
    @classmethod
    def unexpected(cls, code: str, message: str) -> "Error":
        """
        Creates a new unexpected error with the specified code and message.

        Args:
            code (str): The error code.
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @overload
    @classmethod
    def unexpected(cls, message: str) -> "Error":
        """
        Creates a new unexpected error with the specified message.

        Args:
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @classmethod
    def unexpected(cls, code_or_message: str, message: str = "") -> "Error":
        if not message:
            return cls.create(
                ErrorType.Unexpected, ErrorType.Unexpected.value, code_or_message
            )
        return cls.create(ErrorType.Unexpected, code_or_message, message)

    @overload
    @classmethod
    def unavailable(cls, code: str, message: str) -> "Error":
        """
        Creates a new unavailable error with the specified code and message.

        Args:
            code (str): The error code.
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @overload
    @classmethod
    def unavailable(cls, message: str) -> "Error":
        """
        Creates a new unavailable error with the specified message.

        Args:
            message (str): The error message.

        Returns:
            Error: An instance of Error.
        """

    @classmethod
    def unavailable(cls, code_or_message: str, message: str = "") -> "Error":
        if not message:
            return cls.create(
                ErrorType.Unavailable, ErrorType.Unavailable.value, code_or_message
            )
        return cls.create(ErrorType.Unavailable, code_or_message, message)


Error.Null = Error(type=ErrorType.Null, code=ErrorType.Null.name, message="")
