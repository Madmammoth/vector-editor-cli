from typing import Callable

from vector_editor.repository import ShapeRepository
from vector_editor.shapes import Circle, Point, Segment, Shape, Square

CommandHandler = Callable[[list[str], ShapeRepository], None]
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


def create_command(args: list[str], repo: ShapeRepository) -> None:
    shape_type = args[0]
    factory = SHAPE_FACTORIES.get(shape_type)

    if not factory:
        print("Unknown shape")
        return

    shape = factory(args[1:])
    shape_id = repo.add(shape)
    print(f"Created shape id={shape_id}")


def list_command(_: list[str], repo: ShapeRepository) -> None:
    shapes = repo.list()

    if not shapes:
        print("No shapes")
        return

    for shape_id, shape in shapes.items():
        print(f"{shape_id}: {shape.describe()}")


def delete_command(args: list[str], repo: ShapeRepository) -> None:
    shape_id = int(args[0])

    if repo.delete(shape_id):
        print("Deleted")

    else:
        print("Shape not found")


def help_command(_: list[str], __: ShapeRepository) -> None:
    print(
        """
Commands:

create point x y
create segment x1 y1 x2 y2
create circle x y r
create square x y side

list
delete id
exit
"""
    )


COMMANDS: dict[str, CommandHandler] = {
    "create": create_command,
    "list": list_command,
    "delete": delete_command,
    "help": help_command,
}


def execute_command(command: str, repo: ShapeRepository) -> None:
    parts = command.split()

    if not parts:
        return

    cmd = parts[0]
    args = parts[1:]

    handler = COMMANDS.get(cmd)

    if not handler:
        print("Unknown command")
        return

    handler(args, repo)
