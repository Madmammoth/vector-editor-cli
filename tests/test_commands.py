import pytest
from _pytest.capture import CaptureFixture

from vector_editor.commands import execute_command
from vector_editor.repository import ShapeRepository


@pytest.mark.parametrize(
    "command,expected",
    [
        ("create point 1 2", "Point"),
        ("create segment 1 2 3 4", "Segment"),
        ("create circle 1 2 3", "Circle"),
        ("create square 1 2 3", "Square"),
    ],
)
def test_create_shapes(
    command: str,
    expected: str,
    capsys: CaptureFixture[str],
) -> None:
    repo = ShapeRepository()

    execute_command(command, repo)
    execute_command("list", repo)

    out = capsys.readouterr().out

    assert expected in out


def test_list_shapes(capsys: CaptureFixture[str]) -> None:
    repo = ShapeRepository()

    execute_command("create point 1 2", repo)
    execute_command("list", repo)

    out = capsys.readouterr().out
    assert "Point" in out


def test_delete_shape(capsys: CaptureFixture[str]) -> None:
    repo = ShapeRepository()

    execute_command("create point 1 2", repo)
    execute_command("delete 1", repo)

    out = capsys.readouterr().out
    assert "Deleted" in out


def test_invalid_point_args(capsys: CaptureFixture[str]) -> None:
    repo = ShapeRepository()

    execute_command("create point a b", repo)

    out = capsys.readouterr().out
    assert "Error" in out


def test_missing_args(capsys: CaptureFixture[str]) -> None:
    repo = ShapeRepository()

    execute_command("create point", repo)

    out = capsys.readouterr().out
    assert "Error" in out


def test_invalid_delete(capsys: CaptureFixture[str]) -> None:
    repo = ShapeRepository()

    execute_command("delete abc", repo)

    out = capsys.readouterr().out
    assert "Error" in out


def test_unknown_command(capsys: CaptureFixture[str]) -> None:
    repo = ShapeRepository()

    execute_command("foobar", repo)

    out = capsys.readouterr().out
    assert "Unknown command" in out


def test_case_insensitive(capsys: CaptureFixture[str]) -> None:
    repo = ShapeRepository()

    execute_command("CREATE point 1 2", repo)

    out = capsys.readouterr().out
    assert "Created shape id=1" in out
