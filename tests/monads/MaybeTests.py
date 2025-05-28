import pytest

from src.richillcapital_shared_kernel.monads import Maybe


class MaybeTests:
    def test_with_value_given_none_should_return_null_maybe(self) -> None:
        maybe = Maybe[str].with_value(None)

        assert not maybe.has_value
        assert maybe.is_null is True
        with pytest.raises(RuntimeError, match=r"Can not access value on a null Maybe"):
            maybe.value

    def test_with_value_given_value_should_return_maybe_with_value(self) -> None:
        maybe = Maybe[str].with_value("value")

        assert maybe.has_value
        assert maybe.is_null is False
        assert maybe.value == "value"

    def test_null_should_return_null_maybe(self) -> None:
        maybe = Maybe[str].null()

        assert not maybe.has_value
        assert maybe.is_null is True
        with pytest.raises(RuntimeError, match=r"Can not access value on a null Maybe"):
            maybe.value

    def test_maybes_with_same_value_should_be_equal(self) -> None:
        maybe1 = Maybe[str].with_value("value")
        maybe2 = Maybe[str].with_value("value")

        assert maybe1 == maybe2

    def test_maybes_with_different_values_should_not_be_equal(self) -> None:
        maybe1 = Maybe[str].with_value("value1")
        maybe2 = Maybe[str].with_value("value2")

        assert maybe1 != maybe2

    def test_null_maybes_should_be_equal(self) -> None:
        maybe1 = Maybe[str].null()
        maybe2 = Maybe[str].null()

        assert maybe1 == maybe2

    def test_maybe_should_not_be_equal_to_null_maybe(self) -> None:
        maybeValue = Maybe[str].with_value("value")
        maybeNull = Maybe[str].null()

        assert maybeValue != maybeNull
