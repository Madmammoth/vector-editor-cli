from abc import ABC, abstractmethod


class Shape(ABC):
    """Base class for all shapes."""

    @abstractmethod
    def describe(self) -> str:
        """Return human-readable description of the shape."""
        raise NotImplementedError
