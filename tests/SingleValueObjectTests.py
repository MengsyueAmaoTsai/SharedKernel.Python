from richillcapital_shared_kernel import SingleValueObject


class TestSingleValueObject(SingleValueObject[str]):
    def __init__(self, value: str):
        super().__init__(value)


class SingleValueObjectTests:
    def test_to_string_should_return_value_as_string(self):
        test = TestSingleValueObject("test")
        assert str(test) == "test"
