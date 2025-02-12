from .. import Error


class ResultT[TValue]:
    """
    Represents a result that can either be a success or a failure.
    """

    def __init__(self, is_success: bool, error: Error, value: TValue) -> None:
        self.__is_success = is_success
        self.__error = error
        self.__value = value

    @property
    def is_success(self) -> bool:
        """
        Returns True if the result is a success, False otherwise.

        Returns:
            bool: True if the result is a success, False otherwise.
        """
        return self.__is_success

    @property
    def is_failure(self) -> bool:
        """
        Returns True if the result is a failure, False otherwise.

        Returns:
            bool: True if the result is a failure, False otherwise.
        """
        return not self.__is_success

    @property
    def error(self) -> Error:
        """
        Returns the error associated with the failure result.
        Raises a RuntimeError if called on a success result.

        Returns:
            Error: The error associated with the failure result.

        Raises:
            RuntimeError: If called on a success result.
        """
        if self.is_success:
            raise RuntimeError("Cannot access error on success result")

        return self.__error

    @property
    def value(self) -> TValue:
        """
        Returns the value associated with the success result.
        Raises a RuntimeError if called on a failure result.

        Returns:
            TValue: The value associated with the success result.

        Raises:
            RuntimeError: If called on a failure result
        """
        if self.is_failure:
            raise RuntimeError("Cannot access value on failure result")

        return self.__value

    @staticmethod
    def success(value: TValue) -> "ResultT[TValue]":
        """
        Creates a success result with the given value.

        Args:
            value (TValue): The value to be wrapped in the success result.
        Returns:
            ResultT[TValue]: The success result with the given value.
        Raises:
            ValueError: If the value is None.
        """
        return ResultT(True, Error.Null, value)

    @staticmethod
    def failure(error: Error) -> "ResultT[TValue]":
        """
        Creates a failure result with the given error.
        Raises a ValueError if the error is Error.Null.

        Args:
            error (Error): The error to be wrapped in the failure result.

        Returns:
            ResultT[TValue]: The failure result with the given error.

        Raises:
            ValueError: If the error is Error.Null.
        """
        if error is Error.Null:
            raise ValueError("Error cannot be Error.Null")

        return ResultT(False, error, None)  # type: ignore

    def __eq__(self, other: object) -> bool:
        """
        Checks if this result is equal to another result.
        Returns True if the results are equal, False otherwise.
        """
        if not isinstance(other, ResultT):
            return False

        if self.is_success and other.is_success:
            return self.value == other.value  # type: ignore

        return self.is_failure and other.is_failure and self.error == other.error
