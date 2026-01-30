# Developer Tools - Solutions

## Complete Solutions with Explanations

### Black Formatting Solutions

#### Solution 1: Format Messy Code

```python
# Original messy code
def calculate(x,y,z):
    result=x+y*z
    return result
data=[1,2,3,4,5]
for item in data:
    print('Item:',item)
```

After running `black messy.py`:

```python
# Formatted by Black
def calculate(x, y, z):
    result = x + y * z
    return result


data = [1, 2, 3, 4, 5]
for item in data:
    print("Item:", item)
```

**Changes Black Made:**
1. Added spaces around operators (x, y, z)
2. Added spaces around assignment (result =)
3. Added spaces after commas in list
4. Converted single quotes to double quotes
5. Added blank lines between logical sections
6. Added space in print function

#### Solution 2: Black Configuration

```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py39', 'py310']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | build
  | dist
)/
'''
```

```bash
# Test configuration
black --check myfile.py  # Verify would format correctly
black myfile.py          # Actually format
```

---

### Ruff Linting Solutions

#### Solution 3: Identify and Fix Issues

```python
# Original with violations
import os
import sys
import json

x = 10  # F841: assigned but never used
y = 20
unused_var = "test"  # F841: assigned but never used

def process():
    items = [1, 2, 3]; result = sum(items); print(result)  # E702: multiple statements
    pass

# Missing newline
```

After running `ruff check --fix`:

```python
# Fixed version
import json

y = 20

def process():
    items = [1, 2, 3]
    result = sum(items)
    print(result)
```

**Issues Found and Fixed:**
- F401: Unused imports (os, sys)
- F841: Unused variables (x, unused_var)
- E702: Multiple statements on one line
- W292: No newline at end of file

#### Solution 4: Ruff Configuration

```toml
# pyproject.toml
[tool.ruff]
line-length = 88
target-version = "py39"

[tool.ruff.lint]
select = [
    "E",    # pycodestyle errors
    "F",    # pyflakes
    "W",    # pycodestyle warnings
    "I",    # isort
]
ignore = [
    "E501",  # Line too long (handled by Black)
]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]      # Allow unused imports
"tests/*" = ["F401", "F841"]  # Allow unused in tests
"scripts/*" = ["T201"]        # Allow print in scripts
```

---

### pytest Testing Solutions

#### Solution 5: Write Unit Tests

```python
# calculator.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

```python
# test_calculator.py
import pytest
from calculator import add, multiply, divide

class TestAdd:
    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -1) == -2

    def test_add_mixed(self):
        assert add(-5, 10) == 5

    def test_add_zero(self):
        assert add(0, 0) == 0

class TestMultiply:
    def test_multiply_positive(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(100, 0) == 0

    def test_multiply_negative(self):
        assert multiply(-2, 3) == -6

class TestDivide:
    def test_divide_normal(self):
        assert divide(10, 2) == 5

    def test_divide_float(self):
        assert divide(10, 3) == pytest.approx(3.333, rel=1e-3)

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(10, 0)
```

```bash
# Run tests
pytest test_calculator.py -v

# Output:
# test_calculator.py::TestAdd::test_add_positive PASSED
# test_calculator.py::TestAdd::test_add_negative PASSED
# ...
```

#### Solution 6: Using Fixtures

```python
# conftest.py (shared fixtures)
import pytest
from pathlib import Path
import tempfile

@pytest.fixture
def temp_file():
    """Create temporary file for testing"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("test content")
        temp_path = Path(f.name)
    yield temp_path
    temp_path.unlink()  # Cleanup

@pytest.fixture
def sample_user():
    """Provide sample user data"""
    return {
        'id': 1,
        'name': 'John',
        'email': 'john@example.com',
        'age': 30
    }

@pytest.fixture
def sample_users():
    """Provide list of users"""
    return [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'}
    ]
```

```python
# test_fixtures.py
def test_file_creation(temp_file):
    assert temp_file.exists()
    assert temp_file.read_text() == "test content"

def test_user_data(sample_user):
    assert sample_user['name'] == 'John'
    assert sample_user['age'] == 30

def test_user_list(sample_users):
    assert len(sample_users) == 3
    assert sample_users[0]['name'] == 'Alice'
```

#### Solution 7: Parametrized Tests

```python
# test_validation.py
import pytest
import re

def validate_email(email):
    """Validate email format"""
    pattern = r'^[^@]+@[^@]+\.[^@]+$'
    return bool(re.match(pattern, email))

@pytest.mark.parametrize("email,expected", [
    ("user@example.com", True),
    ("invalid.email", False),
    ("test@domain.co.uk", True),
    ("", False),
    ("@example.com", False),
    ("user@example", False),
])
def test_email_validation(email, expected):
    assert validate_email(email) == expected

@pytest.mark.parametrize("x,y,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_addition(x, y, expected):
    assert x + y == expected
```

---

### Poetry Solutions

#### Solution 9: Create Project with Poetry

```bash
# Create project
poetry new mylearningapp
cd mylearningapp

# Add dependencies
poetry add \
    requests \
    flask \
    sqlalchemy \
    python-dotenv \
    pydantic

# Add dev dependencies
poetry add --group dev \
    pytest \
    pytest-cov \
    black \
    ruff \
    mypy \
    pre-commit
```

#### Solution 10: Dependency Constraints

```toml
# pyproject.toml
[tool.poetry.dependencies]
python = "^3.9"                    # >= 3.9, < 4.0
requests = "^2.28"                 # >= 2.28, < 3.0
flask = "~2.3"                     # >= 2.3, < 2.4
sqlalchemy = ">=1.4,<2.0"          # Specific range
python-dotenv = "^0.19"            # >= 0.19, < 1.0
pydantic = ">=1.7,!=1.8.0,<2.0"   # Range with exclusion

[tool.poetry.group.dev.dependencies]
pytest = "^7.2"
pytest-cov = "^4.0"
black = "^23.1"
ruff = "^0.1"
mypy = "^1.0"
pre-commit = "^3.0"
```

**Version Constraint Meanings:**
- `^2.0`: Compatible with 2.x (auto-updates patches/minors)
- `~2.0`: Approximately 2.0 (only patch updates)
- `>=2.0,<3.0`: Explicit range
- `*`: Any version (avoid in production)

---

### mypy Type Checking Solutions

#### Solution 11: Add Type Hints

```python
# utils.py
from typing import List, Dict, Optional

def greet(name: str) -> str:
    """Greet someone by name"""
    return f"Hello, {name}"

def sum_list(numbers: List[int]) -> int:
    """Sum a list of numbers"""
    return sum(numbers)

def get_user_by_id(user_id: int) -> Optional[Dict[str, str]]:
    """Get user by ID, or None if not found"""
    if user_id == 1:
        return {'id': '1', 'name': 'John'}
    return None

def process_items(items: List[str]) -> Dict[str, int]:
    """Count occurrences of each item"""
    counts: Dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts
```

```bash
# Check with mypy
mypy utils.py

# If you have type errors
# mypy utils.py
# utils.py:5: error: Argument 1 to "greet" has incompatible type "int"; expected "str"
```

#### Solution 12: Type Checking Configuration

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

[[tool.mypy.overrides]]
module = "tests.*"
ignore_errors = true

[[tool.mypy.overrides]]
module = "external_lib"
ignore_missing_imports = true
```

---

### Pre-commit Solutions

#### Solution 13: Set Up Pre-commit

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        language_version: python3.9
        args: ['--line-length=88']

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
        additional_dependencies:
          - types-requests
          - types-flask

  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        types: [python]
        stages: [commit]
        pass_filenames: false
```

```bash
# Install and initialize
pre-commit install
pre-commit run --all-files
```

#### Solution 14: Git Workflow

```bash
# Create file with issues
cat > mymodule.py << 'EOF'
import os
import sys
x = 1
def func( a,b ):
    return a+b
EOF

# Stage file
git add mymodule.py

# Try to commit (hooks run)
git commit -m "Add module"

# Hooks fail, showing:
# - black formats file
# - ruff finds issues
# - mypy finds type issues

# Fix the issues
cat > mymodule.py << 'EOF'
def func(a: int, b: int) -> int:
    return a + b
EOF

# Stage and commit again
git add mymodule.py
git commit -m "Add module"  # Should pass now
```

---

### Complete Project Solution

#### Solution 15: Full Workflow

```bash
# Create project structure
poetry new myproject
cd myproject

# Install tools
poetry add requests fastapi
poetry add --group dev pytest black ruff mypy pre-commit

# Create directories
mkdir -p src/myproject tests

# Create pyproject.toml with all tools
cat > pyproject.toml << 'EOF'
[tool.poetry]
name = "myproject"
version = "0.1.0"
description = "My project"
authors = ["Author <author@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.28"

[tool.poetry.group.dev.dependencies]
pytest = "^7.2"
black = "^23.1"
ruff = "^0.1"
mypy = "^1.0"
pre-commit = "^3.0"

[tool.black]
line-length = 88

[tool.ruff]
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "W"]

[tool.mypy]
python_version = "3.9"
disallow_untyped_defs = true
EOF

# Create .pre-commit-config.yaml
# ... (as shown in Solution 13)

# Initialize hooks
pre-commit install

# Create sample code
cat > src/myproject/__init__.py << 'EOF'
"""My project package"""

__version__ = "0.1.0"
EOF

cat > src/myproject/main.py << 'EOF'
from typing import List

def process_items(items: List[str]) -> int:
    """Count items"""
    return len(items)
EOF

# Create tests
cat > tests/test_main.py << 'EOF'
from myproject.main import process_items

def test_count_items():
    assert process_items(["a", "b", "c"]) == 3
EOF

# Run workflow
poetry install
poetry run black .
poetry run ruff check --fix .
poetry run mypy src/
poetry run pytest

# Commit
git add .
git commit -m "Initial project setup"  # Hooks verify everything
```

---

## Summary of Tools

| Tool | Purpose | Command |
|------|---------|---------|
| Black | Format | `black .` |
| Ruff | Lint | `ruff check --fix .` |
| mypy | Type check | `mypy .` |
| pytest | Test | `pytest` |
| Poetry | Deps | `poetry install` |
| pre-commit | Hooks | `pre-commit install` |

All solutions include working code ready to run and test.
