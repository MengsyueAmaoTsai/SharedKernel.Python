from typing import Iterable

from .. import Error


class ErrorOr[TValue]:
    """
    Represents a monadic type that can hold either a value or an error.
    """

    def __init__(self, has_error: bool, errors: Iterable[Error], value: TValue) -> None:
        self.__has_error = has_error
        self.__errors = errors
        self.__value = value

    @property
    def has_error(self) -> bool:
        """
        Returns a boolean indicating whether the ErrorOr has an error.

        Returns:
            True if the ErrorOr has an error, False otherwise.
        """
        return self.__has_error

    @property
    def is_value(self) -> bool:
        """
        Returns a boolean indicating whether the ErrorOr has a value.

        Returns:
            True if the ErrorOr has a value, False otherwise.
        """
        return not self.__has_error

    @property
    def errors(self) -> Iterable[Error]:
        """
        Returns the errors held by the ErrorOr. Raises a RuntimeError if the ErrorOr is a value.

        Returns:
            The errors held by the ErrorOr.

        Raises:
            RuntimeError: If the ErrorOr is a value.
        """
        if self.is_value:
            raise RuntimeError("Cannot access errors on value")

        return self.__errors

    @property
    def value(self) -> "TValue":
        """
        Returns the value held by the ErrorOr. Raises a RuntimeError if the ErrorOr has an error.

        Returns:
            The value held by the ErrorOr.

        Raises:
            RuntimeError: If the ErrorOr has an error.
        """
        if self.has_error:
            raise RuntimeError("Cannot access value on error")

        return self.__value

    @staticmethod
    def with_value(value: TValue) -> "ErrorOr[TValue]":
        """
        Creates a new ErrorOr instance with the specified value.

        Args:
            value: The value to hold in the ErrorOr.

        Returns:
            A new ErrorOr instance with the specified value.
        """
        return ErrorOr(False, [], value)

    @staticmethod
    def with_error(error: Error) -> "ErrorOr[TValue]":
        """
        Creates a new ErrorOr instance with the specified error.

        Args:
            error: The error to hold in the ErrorOr.

        Returns:
            A new ErrorOr instance with the specified error.
        """
        if error is Error.Null:
            raise ValueError("Error cannot be Error.Null")

        return ErrorOr(True, [error], None)

    @staticmethod
    def with_errors(errors: Iterable[Error]) -> "ErrorOr[TValue]":
        """
        Creates a new ErrorOr instance with the specified errors.

        Args:
            errors: The errors to hold in the ErrorOr.

        Returns:
            A new ErrorOr instance with the specified errors.
        """
        if Error.Null in errors:
            raise ValueError("Error cannot be Error.Null")

        return ErrorOr(True, errors, None)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ErrorOr):
            return False

        if self.has_error and other.has_error:
            return self.errors == other.errors

        return self.is_value and other.is_value and self.value == other.value
