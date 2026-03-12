from typing import Dict

from vector_editor.shapes.base import Shape


class ShapeRepository:
    """In-memory storage for shapes."""

    def __init__(self) -> None:
        self._shapes: Dict[int, Shape] = {}
        self._next_id: int = 1

    def add(self, shape: Shape) -> int:
        shape_id = self._next_id
        self._shapes[shape_id] = shape
        self._next_id += 1
        return shape_id

    def delete(self, shape_id: int) -> bool:
        if shape_id in self._shapes:
            del self._shapes[shape_id]
            return True
        return False

    def list(self) -> Dict[int, Shape]:
        return self._shapes
