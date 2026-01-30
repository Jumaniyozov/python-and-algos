# Developer Tools - Theory

## Table of Contents

1. [Code Formatting with Black](#code-formatting-with-black)
2. [Linting with Ruff](#linting-with-ruff)
3. [Testing with pytest](#testing-with-pytest)
4. [Dependency Management with Poetry](#dependency-management-with-poetry)
5. [Type Checking with mypy](#type-checking-with-mypy)
6. [Pre-commit Hooks](#pre-commit-hooks)
7. [Development Workflows](#development-workflows)

---

## Code Formatting with Black

### What is Black?

Black is an opinionated code formatter that automatically reformats Python code to a consistent style. It enforces a single style, eliminating debates about formatting.

```
Before Black:
def very_long_function_name(parameter_one, parameter_two,
                           parameter_three, parameter_four):
    return parameter_one + parameter_two + parameter_three

After Black:
def very_long_function_name(
    parameter_one, parameter_two, parameter_three, parameter_four
):
    return parameter_one + parameter_two + parameter_three
```

### Black Configuration

```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py39']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
```

### Black Formatting Rules

1. **Line Length**: Default 88 characters
2. **Quotes**: Prefers double quotes
3. **Trailing Commas**: Added in multi-line collections
4. **Parentheses**: Added when needed for line length
5. **Strings**: Prefers double quotes, normalizes escaping

---

## Linting with Ruff

### What is Ruff?

Ruff is a fast Python linter that checks for:
- PEP 8 style violations
- Unused imports and variables
- Type errors
- Security issues
- Code complexity problems

```
Ruff Output:
main.py:1:1: F401 [*] `os` imported but unused
main.py:3:5: E741 Ambiguous variable name 'l'
main.py:10:1: W292 No newline at end of file
```

### Rule Categories

```
F: PyFlakes (logical errors)
  F401: Unused imports
  F841: Unused variables

E: pycodestyle (style)
  E501: Line too long
  E701: Multiple statements on one line

W: Warnings
  W292: No newline at end of file

C: McCabe (complexity)
  C901: Function too complex

I: isort (import sorting)
  I001: Unsorted imports

T: Type checking
  T201: `print()` used

S: Security
  S101: Use of assert
```

### Ruff Configuration

```toml
# pyproject.toml
[tool.ruff]
line-length = 88
target-version = "py39"

[tool.ruff.lint]
select = [
    "F",    # PyFlakes
    "E",    # pycodestyle
    "W",    # Warnings
    "I",    # isort
]
ignore = ["E203", "E501"]  # Ignore some rules

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]  # Allow unused imports in __init__
"tests/*" = ["F401"]      # Allow unused imports in tests
```

---

## Testing with pytest

### What is pytest?

pytest is a framework for writing and running tests. It supports:
- Simple functions as tests
- Fixtures for setup and teardown
- Parametrized tests
- Plugins for extended functionality
- Clear assertion messages

### Test Structure

```python
# test_example.py
import pytest

def test_addition():
    assert 2 + 2 == 4

def test_string():
    assert "hello".upper() == "HELLO"

class TestMath:
    def test_multiply(self):
        assert 3 * 4 == 12

    def test_divide(self):
        assert 10 / 2 == 5
```

### Assertions

```python
# Comparison
assert x == y
assert x != y
assert x > y
assert x in [a, b, c]

# Type checking
assert isinstance(x, int)
assert callable(x)

# Boolean
assert x is True
assert x is not None

# Exception
with pytest.raises(ValueError):
    int("not a number")

# Approximate floating point
assert x == pytest.approx(3.14159, rel=1e-5)
```

### Fixtures

```python
import pytest

@pytest.fixture
def sample_data():
    """Setup data for tests"""
    return {'name': 'John', 'age': 30}

def test_with_fixture(sample_data):
    assert sample_data['name'] == 'John'

@pytest.fixture
def temp_file(tmp_path):
    """Create temporary file"""
    file = tmp_path / "test.txt"
    file.write_text("test content")
    return file

def test_file_operations(temp_file):
    assert temp_file.read_text() == "test content"
```

### Parametrized Tests

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert input * 2 == expected

@pytest.mark.parametrize("x,y,z", [
    (1, 2, 3),
    (4, 5, 6),
])
def test_sum(x, y, z):
    assert x + y == z - 2
```

### Test Organization

```
project/
├── src/
│   └── mymodule.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Shared fixtures
│   ├── test_basic.py
│   ├── test_advanced.py
│   └── unit/
│       └── test_utils.py
└── pyproject.toml
```

---

## Dependency Management with Poetry

### What is Poetry?

Poetry manages Python project dependencies and packaging. It provides:
- Dependency version management
- Virtual environment management
- Package publishing
- Lock files for reproducible builds
- Dependency conflict resolution

### Project Structure

```
myproject/
├── pyproject.toml       # Project configuration
├── poetry.lock          # Locked dependencies (auto-generated)
├── README.md
├── src/
│   └── myproject/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
└── .gitignore
```

### pyproject.toml

```toml
[tool.poetry]
name = "myproject"
version = "0.1.0"
description = "My awesome project"
authors = ["John Doe <john@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.28.0"
fastapi = "^0.95.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0"
black = "^23.0"
ruff = "^0.1.0"
mypy = "^1.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### Version Constraints

```
"2.0"      - Exact version
"^2.0"     - Compatible 2.x (>=2.0, <3.0)
"~2.0"     - Approximately 2.0 (>=2.0, <2.1)
">=2.0"    - 2.0 or higher
"<=2.0"    - 2.0 or lower
">=2.0,<3.0" - Range
```

### Poetry Commands

```bash
# Create new project
poetry new myproject

# Initialize existing project
poetry init

# Add dependency
poetry add requests fastapi

# Add dev dependency
poetry add --group dev pytest black

# Install dependencies
poetry install

# Update dependencies
poetry update

# Show dependencies
poetry show

# Build package
poetry build

# Publish to PyPI
poetry publish
```

---

## Type Checking with mypy

### What is mypy?

mypy performs static type checking before runtime. It catches type errors early.

```python
# Without type hints
def add(a, b):
    return a + b

# With type hints
def add(a: int, b: int) -> int:
    return a + b

# mypy catches this error
result: int = add(5, "10")  # Error: Incompatible types
```

### Type Hints

```python
# Basic types
def greet(name: str) -> str:
    return f"Hello, {name}"

# Collections
from typing import List, Dict, Tuple

def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

# Optional
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    return "John" if user_id == 1 else None

# Union
from typing import Union

def process(value: Union[int, str]) -> str:
    return str(value)

# Callable
def execute(func: Callable[[int], str]) -> str:
    return func(42)
```

### mypy Configuration

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
```

### mypy Commands

```bash
# Check entire project
mypy .

# Check specific file
mypy myfile.py

# Ignore missing imports
mypy --ignore-missing-imports .

# Show error codes
mypy --show-error-codes .

# Generate report
mypy --html mypy_report .
```

---

## Pre-commit Hooks

### What are Pre-commit Hooks?

Pre-commit hooks run automated checks before each commit, preventing bad code from being committed.

```
git commit
  ↓
Run hooks
  ├─ Black format check
  ├─ Ruff linting
  ├─ mypy type checking
  ├─ pytest tests
  └─ Other checks
  ↓
Pass? → Commit allowed
Fail? → Commit blocked (fix and retry)
```

### .pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        language_version: python3.9

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
        args: [--ignore-missing-imports]
        additional_dependencies: [types-requests]

  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        types: [python]
        stages: [commit]
```

### Pre-commit Setup

```bash
# Install hooks
pre-commit install

# Run on all files
pre-commit run --all-files

# Run specific hook
pre-commit run black --all-files

# Update hooks
pre-commit autoupdate

# Uninstall hooks
pre-commit uninstall
```

---

## Development Workflows

### Local Development Setup

```bash
# 1. Clone repository
git clone https://github.com/user/project.git
cd project

# 2. Create virtual environment (Poetry does this)
poetry install

# 3. Install pre-commit hooks
pre-commit install

# 4. Start developing
poetry run python main.py
poetry run pytest
```

### Development Commands

```bash
# Format code
black .

# Lint code
ruff check --fix .

# Type check
mypy .

# Run tests
pytest

# Run all checks (simulating pre-commit)
black . && ruff check . && mypy . && pytest
```

### Git Workflow with Hooks

```bash
# Make changes
# vim myfile.py

# Stage changes
git add myfile.py

# Commit (hooks run automatically)
git commit -m "Add new feature"

# If hooks fail:
# 1. Check error messages
# 2. Fix issues
# 3. Stage changes
# 4. Commit again

git add myfile.py
git commit -m "Add new feature"  # Should pass now
```

### CI/CD Integration

```yaml
# .github/workflows/quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: pip install poetry
        poetry install

      - name: Format check
        run: poetry run black --check .

      - name: Lint
        run: poetry run ruff check .

      - name: Type check
        run: poetry run mypy .

      - name: Tests
        run: poetry run pytest
```

---

## Best Practices Summary

### Code Quality Workflow

```
1. Write code
   ↓
2. Format with Black
   ↓
3. Fix with Ruff
   ↓
4. Type check with mypy
   ↓
5. Write tests
   ↓
6. Run tests with pytest
   ↓
7. Commit (pre-commit hooks verify)
```

### Tool Purposes

| Tool | Purpose | When |
|------|---------|------|
| Black | Format code | Before commit |
| Ruff | Find issues | Before commit |
| mypy | Type check | Before commit |
| pytest | Test code | Before commit |
| Poetry | Manage deps | Project setup |
| pre-commit | Automate checks | On every commit |

### Configuration Strategy

```
pyproject.toml          - Black, Ruff, mypy, pytest config
.pre-commit-config.yaml - Pre-commit hooks
.github/workflows/      - CI/CD pipelines
```

---

## Summary

### Key Tools

1. **Black**: Automatic formatting → Consistency
2. **Ruff**: Fast linting → Code quality
3. **pytest**: Testing framework → Bug prevention
4. **Poetry**: Dependency management → Reproducibility
5. **mypy**: Type checking → Error detection
6. **pre-commit**: Automated hooks → Quality enforcement

### Typical Project Structure

```
project/
├── pyproject.toml           # Project config
├── .pre-commit-config.yaml  # Pre-commit hooks
├── poetry.lock              # Locked dependencies
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_main.py
│   └── test_utils.py
├── .github/
│   └── workflows/
│       └── quality.yml
└── README.md
```

### Development Workflow

```
1. poetry install      # Setup environment
2. pre-commit install  # Setup hooks
3. Make changes        # Write code
4. poetry run pytest   # Test locally
5. git commit          # Hooks verify quality
6. git push            # CI runs full suite
```
