import pytest

from richillcapital_shared_kernel import Error
from richillcapital_shared_kernel.monads import ResultT


class ResultTTests:
    def test_success_should_create_success_result_with_value(self) -> None:
        result = ResultT[int].success(1)

        assert result.is_success is True
        assert result.is_failure is False
        assert result.value == 1
        with pytest.raises(RuntimeError, match=r"Cannot access error on success"):
            result.error

    def test_failure_should_create_failure_result_with_error(self) -> None:
        error = Error.invalid("error")
        result = ResultT[int].failure(error)

        assert result.is_success is False
        assert result.is_failure is True
        assert result.error == error
        with pytest.raises(RuntimeError, match=r"Cannot access value on failure"):
            result.value

    def test_failure_given_null_error_should_raise_value_error(self) -> None:
        with pytest.raises(ValueError, match=r"Error cannot be Error.Null"):
            ResultT.failure(Error.Null)

    def test_results_with_same_value_should_be_equal(self) -> None:
        assert ResultT[int].success(1) == ResultT[int].success(1)

    def test_results_with_same_error_should_be_equal(self) -> None:
        error = Error.invalid("error")
        assert ResultT[int].failure(error) == ResultT[int].failure(error)

    def test_results_with_different_values_should_not_be_equal(self) -> None:
        assert ResultT[int].success(1) != ResultT[int].success(2)

    def test_results_with_different_errors_should_not_be_equal(self) -> None:
        error1 = Error.invalid("error")
        error2 = Error.invalid("error2")
        assert ResultT[int].failure(error1) != ResultT[int].failure(error2)
