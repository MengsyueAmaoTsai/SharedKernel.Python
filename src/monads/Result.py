from .. import Error


class Result:
    def __init__(self, is_success: bool, error: Error) -> None:
        self.__is_success = is_success
        self.__error = error

    @property
    def is_success(self) -> bool:
        return self.__is_success

    @property
    def is_failure(self) -> bool:
        return not self.__is_success

    @property
    def error(self) -> Error:
        if self.__is_success:
            raise RuntimeError("Can not access error on a successful result.")
        return self.__error

    @staticmethod
    def success() -> "Result":
        return Result(True, Error.Null)

    @staticmethod
    def failure(error: Error) -> "Result":
        if error is Error.Null:
            raise ValueError("Error cannot be Error.Null")
        return Result(False, error)

    def __eq__(self, other):
        if not isinstance(other, Result):
            return False

        if self.is_failure and other.is_failure:
            return self.error == other.error

        if self.is_success and other.is_failure or self.is_failure and other.is_success:
            return False

        return True
