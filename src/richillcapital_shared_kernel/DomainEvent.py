from abc import ABCMeta
from typing import Protocol


class IDomainEvent(Protocol):
    pass


class DomainEvent(metaclass=ABCMeta):
    """
    Base class for domain events.
    """
