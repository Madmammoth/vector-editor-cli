from typing import Callable

from vector_editor.repository import ShapeRepository
from vector_editor.shape_factories import SHAPE_FACTORIES

CommandHandler = Callable[[list[str], ShapeRepository], None]


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
