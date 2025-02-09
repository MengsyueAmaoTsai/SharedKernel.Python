from .. import Error


class Result:
    def __init__(self, isSuccess: bool, error: Error) -> None:
        self.__isSuccess = isSuccess
        self.__error = error

    @property
    def isSuccess(self) -> bool:
        return self.__isSuccess

    @property
    def isFailure(self) -> bool:
        return not self.__isSuccess

    @property
    def error(self) -> Error:
        if self.__isSuccess:
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
