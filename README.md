# Vector Editor CLI

Simple vector editor with command line interface.

Supported shapes:

- Point
- Segment
- Circle
- Square

The application allows creating shapes, listing them and deleting by id.

---

## Installation

Clone repository:

```bash
git clone https://github.com/Madmammoth/vector-editor-cli.git
cd vector-editor-cli
```

## Quick Start

```bash
uv sync
uv run python -m vector_editor.main
```

---

## Commands

```bash
create point x y  
create segment x1 y1 x2 y2  
create circle x y r  
create square x y side  

list  
delete id  
help  
exit  
```

Commands are case-insensitive.

---

## Example

```
> create point 1 2  
Created shape id=1  
```

```
> create circle 5 5 10  
Created shape id=2  
```

```
> list  
1: Point(1.0, 2.0)  
2: Circle(center=(5.0, 5.0), r=10.0)  
```

```
> delete 1  
Deleted  
```

```
> list  
2: Circle(center=(5.0, 5.0), r=10.0)
```

---

## Development

Run checks:

```
uv run ruff check .
```

Format code:

```
uv run ruff format .
```

Type checking:

```
uv run mypy .
```

Run tests:

```
uv run python -m pytest
```