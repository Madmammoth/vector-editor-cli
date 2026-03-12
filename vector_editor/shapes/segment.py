from dataclasses import dataclass

from .base import Shape


@dataclass
class Segment(Shape):
    x1: float
    y1: float
    x2: float
    y2: float

    def describe(self) -> str:
        return f"Segment(({self.x1}, {self.y1}) -> ({self.x2}, {self.y2}))"
