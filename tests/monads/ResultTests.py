import pytest

from src import Error
from src.monads import Result


class ResultTests:
    def test_success_should_create_success_result(self) -> None:
        result = Result.success()

        assert result.isSuccess is True
        assert result.isFailure is False
        with pytest.raises(
            RuntimeError, match="Can not access error on a successful result."
        ):
            result.error

    def test_failure_when_given_null_error_should_raise_value_error(self) -> None:
        with pytest.raises(ValueError, match="Error cannot be Error.Null"):
            Result.failure(Error.Null)

    def test_failure_should_create_failure_result(self) -> None:
        error = Error.invalid("invalid operation")
        result = Result.failure(error)

        assert result.isSuccess is False
        assert result.isFailure is True
        assert result.error == error
