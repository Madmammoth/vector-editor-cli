from dataclasses import dataclass

from .base import Shape


@dataclass
class Point(Shape):
    x: float
    y: float

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"
