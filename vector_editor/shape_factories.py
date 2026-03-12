from typing import Callable

from vector_editor.shapes import Circle, Point, Segment, Shape, Square

ShapeFactory = Callable[[list[str]], Shape]


def create_point(args: list[str]) -> Point:
    x, y = map(float, args)
    return Point(x, y)


def create_segment(args: list[str]) -> Segment:
    x1, y1, x2, y2 = map(float, args)
    return Segment(x1, y1, x2, y2)


def create_circle(args: list[str]) -> Circle:
    x, y, r = map(float, args)
    return Circle(x, y, r)


def create_square(args: list[str]) -> Square:
    x, y, side = map(float, args)
    return Square(x, y, side)


SHAPE_FACTORIES: dict[str, ShapeFactory] = {
    "point": create_point,
    "segment": create_segment,
    "circle": create_circle,
    "square": create_square,
}
