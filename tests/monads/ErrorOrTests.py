import pytest

from src.shared_kernel import Error
from src.shared_kernel.monads import ErrorOr


class ErrorOrTests:
    def test_with_value_should_create_error_or_with_value(self) -> None:
        value = 20

        errorOr = ErrorOr[int].with_value(value)

        assert not errorOr.has_error
        assert errorOr.is_value
        assert errorOr.value == value
        with pytest.raises(RuntimeError, match=r"Cannot access errors on value"):
            errorOr.errors

    def test_with_error_should_create_error_or_with_error(self) -> None:
        error = Error.invalid("error")
        errorOr = ErrorOr[int].with_error(error)

        assert errorOr.has_error
        assert not errorOr.is_value
        assert errorOr.errors == [error]
        with pytest.raises(RuntimeError, match=r"Cannot access value on error"):
            errorOr.value

    def test_with_errors_should_create_error_or_with_errors(self) -> None:
        errors = [Error.invalid("error"), Error.invalid("error2")]
        errorOr = ErrorOr[int].with_errors(errors)

        assert errorOr.has_error
        assert not errorOr.is_value
        assert errorOr.errors == errors
        with pytest.raises(RuntimeError, match=r"Cannot access value on error"):
            errorOr.value

    def test_with_error_given_null_error_should_raise_value_error(self) -> None:
        with pytest.raises(ValueError, match=r"Error cannot be Error.Null"):
            ErrorOr.with_error(Error.Null)

    def test_with_errors_given_errors_contains_null_error_should_raise_value_error(
        self,
    ) -> None:
        with pytest.raises(ValueError, match=r"Error cannot be Error.Null"):
            ErrorOr.with_errors([Error.Null])

    def test_error_ors_with_same_value_should_be_equal(self) -> None:
        assert ErrorOr[int].with_value(20) == ErrorOr[int].with_value(20)

    def test_error_ors_with_same_error_should_be_equal(self) -> None:
        error = Error.invalid("error")
        assert ErrorOr[int].with_error(error) == ErrorOr[int].with_error(error)

    def test_error_ors_with_same_errors_should_be_equal(self) -> None:
        errors = [Error.invalid("error"), Error.invalid("error2")]
        assert ErrorOr[int].with_errors(errors) == ErrorOr[int].with_errors(errors)

    def test_error_ors_with_different_values_should_not_be_equal(self) -> None:
        assert ErrorOr[int].with_value(20) != ErrorOr[int].with_value(30)

    def test_error_ors_with_different_errors_should_not_be_equal(self) -> None:
        error1 = Error.invalid("error")
        error2 = Error.invalid("error2")
        assert ErrorOr[int].with_error(error1) != ErrorOr[int].with_errors([error1, error2])
