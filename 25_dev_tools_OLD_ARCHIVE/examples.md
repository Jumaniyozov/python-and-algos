# Developer Tools - Examples

## 15 Practical, Runnable Examples

### Black Examples

#### Example 1: Before and After Formatting

```python
# BEFORE.py (messy code)
def calculate_total(items,tax_rate,discount=0):
    total=0
    for item in items:
        total+=item['price']*item['quantity']
    if discount>0:
        total=total*(1-discount)
    final_total=total*(1+tax_rate)
    return final_total

data = [{'price':10,'quantity':2},{'price':20,'quantity':1}]
result = calculate_total(data,0.08,0.1)
print('Total:',result)
```

```bash
# Format with Black
black BEFORE.py
```

```python
# AFTER.py (formatted by Black)
def calculate_total(items, tax_rate, discount=0):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    if discount > 0:
        total = total * (1 - discount)
    final_total = total * (1 + tax_rate)
    return final_total


data = [{"price": 10, "quantity": 2}, {"price": 20, "quantity": 1}]
result = calculate_total(data, 0.08, 0.1)
print("Total:", result)
```

#### Example 2: Black Configuration

```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py39', 'py310']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.venv
  | build
  | dist
)/
'''

[tool.poetry]
name = "myproject"
version = "0.1.0"
```

```bash
# Check without modifying
black --check myfile.py

# Format entire project
black .

# Diff without modifying
black --diff myfile.py
```

---

### Ruff Examples

#### Example 3: Finding and Fixing Issues

```python
# issues.py (contains several Ruff violations)
import os
import sys
from typing import List

x = 1  # Unused variable
y = "unused"  # Unused variable

def get_items():
    items = [1, 2, 3, 4, 5]
    print(items)  # T201: print in code
    return items

class MyClass:
    pass  # OK

# Missing newline at end
```

```bash
# Check for issues
ruff check issues.py

# Output:
# issues.py:1:1: F401 [*] `os` imported but unused
# issues.py:2:1: F401 [*] `sys` imported but unused
# issues.py:5:1: F841 [*] Local variable `x` is assigned to but never used
# issues.py:6:1: F841 [*] Local variable `y` is assigned to but never used
# issues.py:9:5: T201 `print` found
# issues.py:14:1: W292 No newline at end of file

# Fix auto-fixable issues
ruff check --fix issues.py
```

#### Example 4: Ruff Configuration

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
    "T201", # print statements
]
ignore = ["E501"]  # Ignore line too long

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]   # Allow unused imports
"tests/*" = ["F401"]       # Allow unused imports in tests
"scripts/*" = ["T201"]     # Allow print in scripts
```

---

### pytest Examples

#### Example 5: Simple Unit Tests

```python
# math_functions.py
def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

```python
# test_math_functions.py
import pytest
from math_functions import add, subtract, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5

def test_divide():
    assert divide(10, 2) == 5
    assert divide(1, 3) == pytest.approx(0.333, rel=1e-3)

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

```bash
# Run tests
pytest test_math_functions.py

# Output:
# test_math_functions.py::test_add PASSED
# test_math_functions.py::test_subtract PASSED
# test_math_functions.py::test_divide PASSED
# test_math_functions.py::test_divide_by_zero PASSED
```

#### Example 6: Using Fixtures

```python
# test_database.py
import pytest
from pathlib import Path
import tempfile

@pytest.fixture
def temp_db():
    """Create temporary database file for testing"""
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as f:
        db_path = f.name
    yield db_path
    # Cleanup
    Path(db_path).unlink()

@pytest.fixture
def sample_data():
    """Provide sample test data"""
    return {
        'users': [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'}
        ]
    }

def test_database_creation(temp_db):
    assert Path(temp_db).exists()

def test_data_processing(sample_data):
    assert len(sample_data['users']) == 2
    assert sample_data['users'][0]['name'] == 'Alice'
```

#### Example 7: Parametrized Tests

```python
# test_validation.py
import pytest

@pytest.mark.parametrize("email,valid", [
    ("user@example.com", True),
    ("invalid.email", False),
    ("test@domain.co.uk", True),
    ("", False),
    ("@example.com", False),
])
def test_email_validation(email, valid):
    from email_validator import validate_email_format
    result = validate_email_format(email)
    assert result == valid

@pytest.mark.parametrize("x,y,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_addition(x, y, expected):
    assert x + y == expected
```

---

### Poetry Examples

#### Example 8: Creating Project with Poetry

```bash
# Create new project
poetry new myproject

# Output:
# Created package myproject in myproject
# myproject/
# ├── README.md
# ├── pyproject.toml
# ├── myproject/
# │   └── __init__.py
# └── tests/
#     └── __init__.py

# Initialize existing project
cd myproject
poetry init
```

#### Example 9: Managing Dependencies

```bash
# Add dependencies
poetry add requests flask

# Add dev dependencies
poetry add --group dev pytest black ruff mypy

# Install dependencies
poetry install

# Show installed packages
poetry show

# Update dependencies
poetry update

# Update specific package
poetry update requests
```

#### Example 10: pyproject.toml Configuration

```toml
[tool.poetry]
name = "myproject"
version = "0.1.0"
description = "My awesome project"
authors = ["John Doe <john@example.com>"]
readme = "README.md"
license = "MIT"
homepage = "https://github.com/user/myproject"
repository = "https://github.com/user/myproject"

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.28.0"
fastapi = "^0.95.0"
sqlalchemy = ">=1.4,<2.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.2"
black = "^23.1"
ruff = "^0.1.0"
mypy = "^1.0"
pytest-cov = "^4.0"

[tool.poetry.scripts]
myapp = "myproject.main:main"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---

### mypy Examples

#### Example 11: Type Hints and Checking

```python
# calculator.py
from typing import Union, List, Dict

def add(a: int, b: int) -> int:
    """Add two integers"""
    return a + b

def process_numbers(numbers: List[int]) -> Dict[str, Union[int, float]]:
    """Process list of numbers and return statistics"""
    if not numbers:
        raise ValueError("List cannot be empty")

    total = sum(numbers)
    count = len(numbers)
    average = total / count

    return {
        'sum': total,
        'average': average,
        'count': count
    }

# Type checking
result: int = add(5, 3)  # OK
data: Dict[str, int] = process_numbers([1, 2, 3])  # Error: type mismatch
```

```bash
# Run mypy
mypy calculator.py

# Output:
# calculator.py:21: error: Incompatible types in assignment
# (expression has type "Dict[str, Union[int, float]]", variable has type "Dict[str, int]")
```

#### Example 12: mypy Configuration

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
strict_equality = true

[[tool.mypy.overrides]]
module = "tests.*"
ignore_errors = true

[[tool.mypy.overrides]]
module = "external_library"
ignore_missing_imports = true
```

---

### Pre-commit Examples

#### Example 13: Setting Up Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
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
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
        args: [--ignore-missing-imports]
        additional_dependencies: [types-requests, types-flask]

  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        types: [python]
        stages: [commit]
        pass_filenames: false

      - id: check-added-large-files
        name: Check for added large files
        entry: check-added-large-files
        language: system
        stages: [commit]
```

```bash
# Install hooks
pre-commit install

# Run all hooks on all files
pre-commit run --all-files

# Run specific hook
pre-commit run black --all-files

# Update hook versions
pre-commit autoupdate
```

#### Example 14: Git Workflow with Pre-commit

```bash
# Make changes to files
vim mymodule.py
vim tests/test_module.py

# Stage files
git add mymodule.py tests/test_module.py

# Commit (hooks run automatically)
git commit -m "Add new feature"

# If hooks fail, you see output like:
# black....................................................................Failed
# - hook id: black
# - exit code: 1
# Files were modified by this hook.

# Fix the issues (black already formatted, ruff may need manual fixes)
git add mymodule.py tests/test_module.py
git commit -m "Add new feature"  # Try again

# If all hooks pass:
# black....................................................................Passed
# ruff.....................................................................Passed
# mypy.....................................................................Passed
# pytest...................................................................Passed
```

---

### Complete Project Setup Example

#### Example 15: Full Development Workflow

```bash
# 1. Create new project
poetry new myproject
cd myproject

# 2. Add dependencies
poetry add requests fastapi uvicorn sqlalchemy
poetry add --group dev pytest pytest-cov black ruff mypy pre-commit

# 3. Initialize pre-commit
pre-commit install

# 4. Create directory structure
mkdir -p src/myproject tests/unit tests/integration

# 5. Create files
cat > pyproject.toml << 'EOF'
[tool.poetry]
name = "myproject"
version = "0.1.0"
description = "My project"
authors = ["Author <author@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.28"
fastapi = "^0.95"
uvicorn = "^0.20"

[tool.poetry.group.dev.dependencies]
pytest = "^7.2"
pytest-cov = "^4.0"
black = "^23.1"
ruff = "^0.1"
mypy = "^1.0"
pre-commit = "^3.0"

[tool.black]
line-length = 88

[tool.ruff]
line-length = 88

[tool.mypy]
python_version = "3.9"
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "--cov=myproject --cov-report=html"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
EOF

# 6. Run development workflow
poetry install
pre-commit run --all-files
poetry run pytest
poetry run black .
poetry run ruff check --fix .
poetry run mypy src/
```

---

## Example Commands Reference

### Black
```bash
black myfile.py                    # Format file
black .                            # Format entire project
black --check .                    # Check without modifying
black --diff myfile.py             # Show changes
```

### Ruff
```bash
ruff check .                       # Check for issues
ruff check --fix .                 # Fix auto-fixable issues
ruff check --select E501 .         # Check specific rule
ruff format .                      # Format code
```

### pytest
```bash
pytest                             # Run all tests
pytest tests/test_module.py        # Run specific file
pytest -v                          # Verbose output
pytest -s                          # Show print statements
pytest --cov=myproject .           # Coverage report
pytest -k test_name                # Run specific test
```

### Poetry
```bash
poetry new myproject               # Create project
poetry add requests                # Add dependency
poetry add --group dev pytest      # Add dev dependency
poetry install                     # Install dependencies
poetry run python script.py        # Run in virtual env
poetry show                        # List dependencies
poetry update                      # Update dependencies
poetry build                       # Build package
poetry publish                     # Publish to PyPI
```

### mypy
```bash
mypy .                             # Check project
mypy myfile.py                     # Check file
mypy --show-error-codes .          # Show error codes
mypy --strict .                    # Strict mode
```

### Pre-commit
```bash
pre-commit install                 # Install hooks
pre-commit run --all-files         # Run all hooks
pre-commit run black --all-files   # Run specific hook
pre-commit autoupdate              # Update hooks
```

---

## Integration Example

Complete flow for checking and committing code:

```bash
# 1. Make changes
vim src/myproject/main.py

# 2. Format code
poetry run black src/

# 3. Fix linting issues
poetry run ruff check --fix src/

# 4. Type check
poetry run mypy src/

# 5. Run tests
poetry run pytest

# 6. Stage and commit
git add src/myproject/main.py
git commit -m "Add feature"  # Pre-commit hooks verify

# 7. Push (optional CI runs)
git push origin main
```
