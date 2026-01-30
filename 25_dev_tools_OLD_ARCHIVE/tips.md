# Developer Tools - Tips and Best Practices

## Black Tips

### 1. Integrate with Your Editor

```bash
# Install Black integration
pip install black[jupyter,d]

# VS Code: Install Python extension
# Settings: "python.formatting.provider": "black"

# PyCharm: Settings → Tools → Python Integrated Tools
# → Default Test Runner → Python Integrated Tools
```

### 2. Use Black in Pre-commit

```yaml
# .pre-commit-config.yaml
- repo: https://github.com/psf/black
  rev: 23.3.0
  hooks:
    - id: black
      args: ['--line-length=88']
```

### 3. Common Black Issues and Solutions

```python
# Issue: Line too long for Black's limit
# Black will automatically break into multiple lines
very_long_function_name_that_exceeds_limit(parameter1, parameter2, parameter3)

# Black formats to:
very_long_function_name_that_exceeds_limit(
    parameter1, parameter2, parameter3
)

# Issue: Want different line length
# Use configuration:
[tool.black]
line-length = 100
```

---

## Ruff Tips

### 1. Use Ruff to Fix Imports

```bash
# Ruff can organize and fix imports automatically
ruff check --fix .

# This fixes:
# - Unused imports
# - Unsorted imports (with isort compatibility)
# - Multiple statements on one line
```

### 2. Understand Error Codes

```
F: PyFlakes
  F401: imported but unused
  F841: local variable assigned but never used

E: pycodestyle errors
  E501: line too long
  E701: multiple statements on one line

W: Warnings
  W292: no newline at end of file

I: isort
  I001: unsorted imports
```

### 3. Performance

```bash
# Ruff is very fast (written in Rust)
# Typical project check: <100ms

# Check only changed files (in pre-commit)
ruff check src/
```

### 4. Disable Rules Selectively

```python
# Ignore rule for a single line
x = 1  # noqa: F841

# Ignore multiple rules
import unused  # noqa: F401

# In pyproject.toml
[tool.ruff.lint.per-file-ignores]
"tests/*" = ["F401", "F841"]
"__init__.py" = ["F401"]
```

---

## pytest Tips

### 1. Test Organization

```
tests/
├── unit/
│   ├── test_module1.py
│   └── test_module2.py
├── integration/
│   └── test_api.py
├── conftest.py              # Shared fixtures
└── fixtures/
    ├── user.py
    └── database.py
```

### 2. Pytest Configuration

```toml
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"
addopts = """
    -v
    --strict-markers
    --cov=myproject
    --cov-report=term-missing
"""
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration",
]
```

### 3. Running Specific Tests

```bash
# Run specific test file
pytest tests/test_module.py

# Run specific test class
pytest tests/test_module.py::TestClass

# Run specific test function
pytest tests/test_module.py::test_function

# Run by marker
pytest -m slow
pytest -m "not slow"

# Run by keyword
pytest -k "test_add"

# Show print statements
pytest -s

# Stop on first failure
pytest -x

# Run last failed
pytest --lf

# Run N times (for flaky tests)
pytest --count=5
```

### 4. Test Fixtures Scope

```python
import pytest

@pytest.fixture(scope="function")  # Default: once per test
def fixture_func():
    return "data"

@pytest.fixture(scope="class")  # Once per test class
def fixture_class():
    return "data"

@pytest.fixture(scope="module")  # Once per module
def fixture_module():
    return "data"

@pytest.fixture(scope="session")  # Once per test session
def fixture_session():
    return "data"

@pytest.fixture(autouse=True)  # Automatically used by all tests
def setup():
    # Setup code
    yield
    # Teardown code
```

### 5. Mocking and Patching

```python
from unittest.mock import Mock, patch, MagicMock

def test_with_mock():
    # Create mock
    mock_func = Mock(return_value=42)
    result = mock_func()
    assert result == 42

@patch('module.function')
def test_with_patch(mock_function):
    mock_function.return_value = 100
    # Use function that calls module.function
    assert mock_function.called

def test_with_context_manager():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'key': 'value'}
        # Test code using requests.get
        assert mock_get.called
```

---

## Poetry Tips

### 1. Virtual Environment Management

```bash
# Poetry creates and manages venv automatically
# Run command in venv
poetry run python script.py
poetry run pytest
poetry run black .

# Activate venv shell (less common)
poetry shell
python script.py
exit
```

### 2. Lock File Management

```bash
# Lock file (poetry.lock) should be committed
# Never manually edit poetry.lock

# Update all dependencies
poetry update

# Update specific package
poetry update requests

# Show what would change
poetry update --dry-run
```

### 3. Development Groups

```toml
[tool.poetry.group.dev.dependencies]
pytest = "^7.0"

[tool.poetry.group.test.dependencies]
pytest-cov = "^4.0"

[tool.poetry.group.docs.dependencies]
sphinx = "^5.0"
```

```bash
# Install all groups
poetry install

# Install without optional groups
poetry install --no-dev

# Install specific group
poetry install --with docs
```

### 4. Publishing Packages

```bash
# Build package
poetry build

# Publish to PyPI (requires token)
poetry config pypi-token.pypi YOUR_TOKEN
poetry publish

# Or upload to private repository
poetry publish --repository internal
```

---

## mypy Tips

### 1. Type Hints Best Practices

```python
from typing import Optional, Union, List, Dict, Callable

# GOOD: Clear type hints
def process_users(users: List[Dict[str, str]]) -> int:
    return len(users)

# GOOD: Use Optional for nullable
def find_user(user_id: int) -> Optional[str]:
    return "John" if user_id == 1 else None

# GOOD: Use Union for multiple types
def convert(value: Union[int, str]) -> str:
    return str(value)

# BAD: No type hints
def process_users(users):
    return len(users)
```

### 2. Ignoring Type Errors

```python
# Ignore single line
x = some_function()  # type: ignore

# Ignore specific error
x = some_function()  # type: ignore[arg-type]

# For entire function
def function():  # type: ignore
    pass
```

### 3. Checking Type Errors Only (No Output)

```bash
# Quick check
mypy . --no-error-summary

# Show only errors
mypy . --show-error-codes

# Generate HTML report
mypy --html . report/
```

### 4. TypedDict for Dictionary Types

```python
from typing import TypedDict

class UserDict(TypedDict):
    id: int
    name: str
    email: str

def process_user(user: UserDict) -> None:
    print(user['name'])  # mypy validates
```

---

## Pre-commit Tips

### 1. Common Configurations

```yaml
# Skip specific files
exclude: |
  (?x)^(
      setup\.py|
      migrations/|
      vendor/
  )$

# Run only on Python files
files: \.py$

# Don't run on commits to master
branches:
  - "!master"
```

### 2. Performance Optimization

```yaml
# Run faster hooks first
repos:
  - repo: local
    hooks:
      - id: check-syntax      # Fast
        ...
      - id: mypy              # Slow
        ...
```

### 3. Skip Hooks on Commit

```bash
# Skip all hooks
git commit --no-verify

# Skip specific hook (if configured)
# Add SKIP environment variable
SKIP=mypy,pytest git commit -m "message"
```

### 4. Test Hooks Locally

```bash
# Run all hooks on all files
pre-commit run --all-files

# Run specific hook
pre-commit run black --all-files

# Debug hook
pre-commit run --all-files --verbose

# Update hook versions
pre-commit autoupdate
```

---

## Integration Best Practices

### 1. Full Development Workflow

```bash
# 1. Setup project
poetry install
pre-commit install

# 2. Make changes
vim src/myproject/main.py

# 3. Format code
poetry run black .

# 4. Fix linting
poetry run ruff check --fix .

# 5. Type check
poetry run mypy src/

# 6. Test
poetry run pytest

# 7. Commit (hooks verify)
git add .
git commit -m "Add feature"
```

### 2. CI/CD Integration

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: 3.9
      - run: pip install poetry
      - run: poetry install
      - run: poetry run black --check .
      - run: poetry run ruff check .
      - run: poetry run mypy .
      - run: poetry run pytest --cov
```

### 3. Pre-push Checks

```bash
# Create script: check.sh
#!/bin/bash
set -e

poetry run black .
poetry run ruff check --fix .
poetry run mypy .
poetry run pytest

echo "All checks passed!"
```

### 4. Documentation

```python
# Always include docstrings
def calculate(x: int, y: int) -> int:
    """
    Calculate sum of two numbers.

    Args:
        x: First number
        y: Second number

    Returns:
        Sum of x and y

    Raises:
        TypeError: If arguments are not integers
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Arguments must be integers")
    return x + y
```

---

## Debugging Tips

### 1. Check Tool Versions

```bash
poetry show
black --version
ruff --version
mypy --version
pytest --version
```

### 2. Test Individual Tools

```bash
# Test one tool at a time
poetry run black --check .          # Passes?
poetry run ruff check .             # Passes?
poetry run mypy .                   # Passes?
poetry run pytest                   # Passes?
```

### 3. Pre-commit Debugging

```bash
# Run with verbose output
pre-commit run --all-files --verbose

# Debug specific hook
pre-commit try-repo . black --all-files

# Check hook files
pre-commit validate-config
pre-commit validate-manifest
```

### 4. Common Issues

```
Issue: Black and Ruff conflict
Solution: Configure both to use same line length
[tool.black]
line-length = 88
[tool.ruff]
line-length = 88

Issue: mypy complains about imports
Solution: Install type stubs
poetry add --group dev types-requests
# Or ignore missing imports
mypy --ignore-missing-imports .

Issue: pytest can't find modules
Solution: Add src to PYTHONPATH
export PYTHONPATH=src:$PYTHONPATH pytest

Issue: Pre-commit hooks slow
Solution: Move slow hooks to CI only
stages: [commit]  # Fast
stages: [push]    # Slow (CI)
```

---

## Quality Checklist

Before committing:
- [ ] Code formatted with Black
- [ ] No Ruff issues
- [ ] Type hints complete (mypy clean)
- [ ] All tests passing
- [ ] Test coverage > 80%
- [ ] No console.log / print statements
- [ ] Docstrings present
- [ ] No commented code

Before pushing:
- [ ] All CI checks pass
- [ ] No merge conflicts
- [ ] Documentation updated
- [ ] CHANGELOG updated
- [ ] Version bumped if needed

---

## Resources

- Black: https://github.com/psf/black
- Ruff: https://github.com/astral-sh/ruff
- pytest: https://docs.pytest.org/
- Poetry: https://python-poetry.org/
- mypy: https://mypy.readthedocs.io/
- pre-commit: https://pre-commit.com/

---

## Time Savers

### Shortcuts for Common Tasks

```bash
# Format, lint, type-check, test all at once
alias check='poetry run black . && poetry run ruff check --fix . && poetry run mypy . && poetry run pytest'

# Then just run:
check
```

### Watch Mode for Development

```bash
# Install pytest-watch
poetry add --group dev pytest-watch

# Auto-run tests on file changes
ptw
```

### Pre-commit Magic

```bash
# Install all and run once
pre-commit install && pre-commit run --all-files

# Then commits are automatic
```
