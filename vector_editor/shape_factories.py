from typing import Callable

from vector_editor.shapes import Circle, Point, Segment, Shape, Square

ShapeFactory = Callable[[list[str]], Shape]


def create_point(args: list[str]) -> Point:
    if len(args) != 2:
        raise ValueError("Point requires 2 arguments: x y")

    try:
        x, y = map(float, args)
    except ValueError:
        raise ValueError("Point coordinates must be numbers")

    return Point(x, y)


def create_segment(args: list[str]) -> Segment:
    if len(args) != 4:
        raise ValueError("Segment requires 4 arguments: x1 y1 x2 y2")

    try:
        x1, y1, x2, y2 = map(float, args)
    except ValueError:
        raise ValueError("Segment coordinates must be numbers")

    return Segment(x1, y1, x2, y2)


def create_circle(args: list[str]) -> Circle:
    if len(args) != 3:
        raise ValueError("Circle requires 3 arguments: x y r")

    try:
        x, y, r = map(float, args)
    except ValueError:
        raise ValueError("Circle parameters must be numbers")

    return Circle(x, y, r)


def create_square(args: list[str]) -> Square:
    if len(args) != 3:
        raise ValueError("Square requires 3 arguments: x y side")

    try:
        x, y, side = map(float, args)
    except ValueError:
        raise ValueError("Square parameters must be numbers")

    return Square(x, y, side)


SHAPE_FACTORIES: dict[str, ShapeFactory] = {
    "point": create_point,
    "segment": create_segment,
    "circle": create_circle,
    "square": create_square,
}
