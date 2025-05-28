from typing import Callable

import pytest

from richillcapital_shared_kernel import Error, ErrorType


class ErrorTests:
    def test_create_when_given_error_type_null_should_raise_error(self):
        with pytest.raises(ValueError, match="Error type cannot be Null."):
            Error.create(ErrorType.Null, "errorCode", "errorMessage")

    def test_create_when_given_error_code_is_empty_should_raise_error(self):
        with pytest.raises(ValueError, match="Error code cannot be null or empty."):
            Error.create(ErrorType.Validation, "", "errorMessage")

    @pytest.mark.parametrize(
        "error_type",
        [
            ErrorType.Validation,
            ErrorType.Unauthorized,
            ErrorType.AccessDenied,
            ErrorType.NotFound,
            ErrorType.MethodNotAllowed,
            ErrorType.Conflict,
            ErrorType.UnsupportedMediaType,
            ErrorType.Unexpected,
            ErrorType.Unavailable,
            ErrorType.Timeout,
        ],
    )
    def test_create_should_create_error(self, error_type: ErrorType):
        error_code = "Error.Code"
        error_message = "Error message"

        error = Error.create(error_type, error_code, error_message)

        assert error.type == error_type
        assert error.code == error_code
        assert error.message == error_message

    @pytest.mark.parametrize(
        "factory_method, error_type",
        [
            (Error.invalid, ErrorType.Validation),
            (Error.unauthorized, ErrorType.Unauthorized),
            (Error.access_denied, ErrorType.AccessDenied),
            (Error.not_found, ErrorType.NotFound),
            (Error.method_not_allowed, ErrorType.MethodNotAllowed),
            (Error.conflict, ErrorType.Conflict),
            (Error.unsupported_media_type, ErrorType.UnsupportedMediaType),
            (Error.unexpected, ErrorType.Unexpected),
            (Error.unavailable, ErrorType.Unavailable),
            (Error.timeout, ErrorType.Timeout),
        ],
    )
    def test_factory_methods_should_create_correct_error(
        self, factory_method: Callable[..., Error], error_type: ErrorType
    ):
        custom_code = "Error.Code"
        error_message = "Error message"
        error1 = factory_method(custom_code, error_message)
        error2 = factory_method(error_message)

        assert error1.type == error_type
        assert error1.code == custom_code
        assert error1.message == error_message

        assert error2.type == error_type
        assert error2.code == error_type.value
        assert error2.message == error_message

    def test_null_should_return_null_error(self):
        error = Error.Null

        assert error.type == ErrorType.Null
        assert error.code == "Null"
        assert error.message == ""

    def test_errors_with_same_properties_should_be_equal(self):
        error1 = Error.invalid("Error.Code", "Error message")
        error2 = Error.invalid("Error.Code", "Error message")

        assert error1 == error2

    def test_errors_with_different_type_should_not_be_equal(self):
        error1 = Error.invalid("Error.Code", "Error message")
        error2 = Error.unauthorized("Error.Code", "Error message")

        assert error1 != error2

    def test_errors_with_different_code_should_not_be_equal(self):
        error1 = Error.invalid("Error.Code", "Error message")
        error2 = Error.invalid("Error.Code2", "Error message")

        assert error1 != error2

    def test_errors_with_different_message_should_not_be_equal(self):
        error1 = Error.invalid("Error.Code", "Error message")
        error2 = Error.invalid("Error.Code", "Error message2")

        assert error1 != error2
