import pytest

from src import Error
from src.monads import Result


class ResultTests:
    def test_success_should_create_success_result(self) -> None:
        result = Result.success()

        assert result.is_success is True
        assert result.is_failure is False
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

        assert result.is_success is False
        assert result.is_failure is True
        assert result.error == error

    def test_success_results_should_be_equal(self) -> None:
        assert Result.success() == Result.success()

    def test_failure_results_with_same_error_should_be_equal(self) -> None:
        error = Error.invalid("invalid operation")
        assert Result.failure(error) == Result.failure(error)

    def test_failure_results_with_different_errors_should_not_be_equal(self) -> None:
        error1 = Error.invalid("invalid operation")
        error2 = Error.invalid("invalid operation2")

        assert Result.failure(error1) != Result.failure(error2)

    def test_success_result_should_not_equal_to_failure_result(self) -> None:
        assert Result.success() != Result.failure(Error.invalid("invalid operation"))
