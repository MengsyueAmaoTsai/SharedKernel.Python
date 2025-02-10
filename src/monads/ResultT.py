from .. import Error


class ResultT[TValue]:
    def __init__(self, is_success: bool, error: Error, value: TValue) -> None:
        self.__is_success = is_success
        self.__error = error
        self.__value = value

    @property
    def is_success(self) -> bool:
        return self.__is_success

    @property
    def is_failure(self) -> bool:
        return not self.__is_success

    @property
    def error(self) -> Error:
        if self.is_success:
            raise RuntimeError("Cannot access error on success result")

        return self.__error

    @property
    def value(self) -> TValue:
        if self.is_failure:
            raise RuntimeError("Cannot access value on failure result")

        return self.__value

    @staticmethod
    def success(value: TValue) -> "ResultT[TValue]":
        return ResultT(True, Error.Null, value)

    @staticmethod
    def failure(error: Error) -> "ResultT[TValue]":
        if error is Error.Null:
            raise ValueError("Error cannot be Error.Null")

        return ResultT(False, error, None)

    def __eq__(self, other: object) -> bool:
        """
        Compares the Maybe with another object for equality.
        Returns True if both Maybes have values and their values are equal,
        or if both Maybes are null. Returns False otherwise.
        """
        if not isinstance(other, ResultT):
            return False

        if self.is_success and other.is_success:
            return self.value == other.value

        return self.is_failure and other.is_failure and self.error == other.error
