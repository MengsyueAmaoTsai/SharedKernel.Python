import pytest

from src import Error, ErrorType


def test_create_when_given_error_type_none_should_throw_value_error():
    with pytest.raises(ValueError, match="Error type cannot be Null."):
        Error.create(ErrorType.Null, "errorCode", "errorMessage")


@pytest.mark.parametrize(
    "error_type",
    [
        ErrorType.Validation,
        ErrorType.Unauthorized,
        ErrorType.Forbidden,
        ErrorType.NotFound,
        ErrorType.MethodNotAllowed,
        ErrorType.Conflict,
        ErrorType.UnsupportedMediaType,
        ErrorType.Unexpected,
        ErrorType.Unavailable,
    ],
)
def test_create_should_create_error(error_type):
    error_code = "Error.Code"
    error_message = "Error message"

    error = Error.create(error_type, error_code, error_message)

    assert error.type == error_type
    assert error.code == error_code
    assert error.message == error_message
