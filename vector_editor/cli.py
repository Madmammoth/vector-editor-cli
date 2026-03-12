from vector_editor.commands import execute_command
from vector_editor.repository import ShapeRepository


class CLI:
    """Command line interface for vector editor."""

    def __init__(self) -> None:
        self.repo = ShapeRepository()

    def run(self) -> None:
        print("Vector Editor CLI. Type 'help' for commands.")

        while True:
            try:
                command = input("> ").strip()

                if command in {"exit", "quit"}:
                    print("Bye!")
                    break

                if not command:
                    continue

                execute_command(command, self.repo)

            except Exception as e:
                print(f"Error: {e}")
