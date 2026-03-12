from abc import ABC, abstractmethod


class Shape(ABC):
    """Base class for all shapes."""

    @abstractmethod
    def __str__(self) -> str:
        """Return human-readable description of the shape."""
        raise NotImplementedError
