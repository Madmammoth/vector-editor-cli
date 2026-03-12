from dataclasses import dataclass

from .base import Shape


@dataclass
class Circle(Shape):
    x: float
    y: float
    radius: float

    def describe(self) -> str:
        return f"Circle(center=({self.x}, {self.y}), r={self.radius})"
