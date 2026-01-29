# Package Management - Examples

Examples extracted from Poetry-related content in 25_dev_tools/examples.md.
See lines 265-343 of original examples.md for complete Poetry examples.

## Example 1: Creating Project with Poetry

```bash
poetry new myproject
cd myproject
poetry add requests flask sqlalchemy
poetry add --group dev pytest black ruff mypy
```

## Example 2: Managing Dependencies

```bash
poetry add requests  
poetry add --group dev pytest
poetry install
poetry run python script.py
```

## Example 3: pyproject.toml Configuration

```toml
[tool.poetry]
name = "myproject"
version = "0.1.0"
description = "My awesome project"
authors = ["John Doe <john@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.28.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.2"
black = "^23.1"
```

For complete examples, see theory.md sections on Poetry Commands and pyproject.toml.
