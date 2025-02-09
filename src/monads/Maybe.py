class Maybe[TValue]:
    """
    Represents a container that may or may not hold a value of type TValue.
    """

    def __init__(self, hasValue: bool, value: TValue | None) -> None:
        self.__has_value = hasValue
        self.__value = value

    @property
    def has_value(self) -> bool:
        """
        Returns a boolean indicating whether the Maybe has a value.

        Returns:
            True if the Maybe has a value, False otherwise.
        """
        return self.__has_value

    @property
    def is_null(self) -> bool:
        """
        Returns a boolean indicating whether the Maybe is null (has no value).

        Returns:
            True if the Maybe is null, False otherwise.
        """
        return not self.__has_value

    @property
    def value(self) -> TValue:
        """
        Returns the value held by the Maybe. Raises a RuntimeError if the Maybe is null.

        Returns:
            The value held by the Maybe.

        Raises:
            RuntimeError: If the Maybe is null.
        """
        if self.is_null:
            raise RuntimeError("Can not access value on a null Maybe")
        return self.__value

    @staticmethod
    def null() -> "Maybe[TValue]":
        """
        Creates a new Maybe instance with no value.

        Returns:
            A new Maybe instance with no value.
        """
        return Maybe(False, None)

    def with_value(value: TValue) -> "Maybe[TValue]":
        """
        Creates a new Maybe instance with the specified value.
        If the value is None, returns a null Maybe instance.

        Args:
            value: The value to hold in the Maybe.

        Returns:
            A new Maybe instance with the specified value, or a null Maybe instance if the value is None.
        """
        if value is None:
            return Maybe[TValue].null()

        return Maybe(True, value)

    def __eq__(self, other: object) -> bool:
        """
        Compares the Maybe with another object for equality.
        Returns True if both Maybes have values and their values are equal,
        or if both Maybes are null. Returns False otherwise.
        """
        if not isinstance(other, Maybe):
            return False

        if self.has_value and other.has_value:
            return self.value == other.value

        return self.is_null and other.is_null
