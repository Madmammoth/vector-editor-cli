from dataclasses import dataclass

from .base import Shape


@dataclass
class Point(Shape):
    x: float
    y: float

    def describe(self) -> str:
        return f"Point({self.x}, {self.y})"
