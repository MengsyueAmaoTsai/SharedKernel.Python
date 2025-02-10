import pytest

from src import Error
from src.monads import ResultT


class ResultTTests:
    def test_success_should_create_success_result_with_value(self) -> None:
        result = ResultT.success(1)

        assert result.is_success is True
        assert result.is_failure is False
        assert result.value == 1

    def test_failure_should_create_failure_result_with_error(self) -> None:
        error = Error.invalid("error")
        result = ResultT.failure(error)

        assert result.is_success is False
        assert result.is_failure is True
        assert result.error == error

    def test_failure_given_null_error_should_raise_value_error(self) -> None:
        with pytest.raises(ValueError, match="Error cannot be Error.Null"):
            ResultT.failure(Error.Null)

    def test_results_with_same_value_should_be_equal(self) -> None:
        assert ResultT.success(1) == ResultT.success(1)

    def test_results_with_same_error_should_be_equal(self) -> None:
        error = Error.invalid("error")
        assert ResultT.failure(error) == ResultT.failure(error)

    def test_results_with_different_values_should_not_be_equal(self) -> None:
        assert ResultT.success(1) != ResultT.success(2)

    def test_results_with_different_errors_should_not_be_equal(self) -> None:
        error1 = Error.invalid("error")
        error2 = Error.invalid("error2")
        assert ResultT.failure(error1) != ResultT.failure(error2)
