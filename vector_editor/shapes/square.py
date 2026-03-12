from dataclasses import dataclass

from .base import Shape


@dataclass
class Square(Shape):
    x: float
    y: float
    side: float

    def __str__(self) -> str:
        return f"Square(top_left=({self.x}, {self.y}), side={self.side})"
