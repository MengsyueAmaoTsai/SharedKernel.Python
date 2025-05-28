from abc import ABCMeta
from typing import Iterable, Protocol

from .DomainEvent import IDomainEvent


class IEntity(Protocol):
    """
    Represents an entity in the domain model.
    """

    def get_domain_events(self) -> Iterable[IDomainEvent]:
        """
        Gets the domain events.

        Returns:
            Iterable[IDomainEvent]: The domain events.
        """
        ...

    def raise_domain_event(self, event: IDomainEvent) -> None:
        """
        Raises a domain event.

        Args:
            event (IDomainEvent): The domain event.
        """
        ...

    def clear_domain_events(self) -> None:
        """
        Clears the domain events.
        """
        ...


class Entity[TId](IEntity, metaclass=ABCMeta):
    """
    Base class for entities in the domain model.
    """

    def __init__(self, id: TId) -> None:
        self.__id = id
        self.__domain_events: list[IDomainEvent] = []

    @property
    def id(self) -> TId:
        """
        Returns the entity ID.

        Returns:
            TId: The entity ID.
        """
        return self.__id

    def get_domain_events(self) -> Iterable[IDomainEvent]:
        """
        Returns the list of domain events associated with the entity.

        Returns:
            Iterable[IDomainEvent]: The list of domain events.
        """
        return self.__domain_events

    def raise_domain_event(self, event: IDomainEvent) -> None:
        """
        Raises a domain event for the entity.

        Args:
            event (IDomainEvent): The domain event to raise.
        """
        self.__domain_events.append(event)

    def clear_domain_events(self) -> None:
        """
        Clears the list of domain events associated with the entity.
        """
        self.__domain_events.clear()

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True

        if not isinstance(other, Entity):
            return False

        return self.id == other.id  # type: ignore

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)

    def __hash__(self) -> int:
        return hash(self.id) * 41
