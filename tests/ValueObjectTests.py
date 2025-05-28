from typing import Iterable

from richillcapital_shared_kernel import ValueObject


class TestValueObject(ValueObject):
    def __init__(self, string_value: str, int_value: int):
        self.__string_value = string_value
        self.__int_value = int_value

    @property
    def string_value(self) -> str:
        return self.__string_value

    @property
    def int_value(self) -> int:
        return self.__int_value

    def _get_atomic_values(self) -> Iterable[object]:
        return [self.__string_value, self.__int_value]


class ValueObjectTests:
    def test_equal_operator_when_values_are_equal_should_return_true(self) -> None:
        value_object1 = TestValueObject("string", 1)
        value_object2 = TestValueObject("string", 1)

        assert (value_object1 == value_object2) is True

    def test_equal_operator_when_values_are_not_equal_should_return_false(self) -> None:
        value_object1 = TestValueObject("string", 1)
        value_object2 = TestValueObject("different string", 1)

        assert (value_object1 == value_object2) is False

    def test_not_equal_operator_when_values_are_not_equal_should_return_true(
        self,
    ) -> None:
        value_object1 = TestValueObject("string", 1)
        value_object2 = TestValueObject("different string", 1)

        assert (value_object1 != value_object2) is True

    def test_not_equal_operator_when_values_are_equal_should_return_false(self) -> None:
        value_object1 = TestValueObject("string", 1)
        value_object2 = TestValueObject("string", 1)

        assert (value_object1 != value_object2) is False

    def test_get_hash_code_when_values_are_equal_should_return_same_hash(self) -> None:
        value_object1 = TestValueObject("string", 1)
        value_object2 = TestValueObject("string", 1)

        assert hash(value_object1) == hash(value_object2)

    def test_get_hash_code_when_values_are_not_equal_should_return_different_hash(
        self,
    ) -> None:
        value_object1 = TestValueObject("string", 1)
        value_object2 = TestValueObject("different string", 1)

        assert hash(value_object1) != hash(value_object2)
