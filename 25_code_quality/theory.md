# Code Quality Tools - Theory

## Table of Contents

1. [Introduction to Code Quality](#introduction-to-code-quality)
2. [Black - Code Formatting](#black-code-formatting)
3. [Ruff - Linting](#ruff-linting)
4. [mypy - Type Checking](#mypy-type-checking)
5. [pre-commit - Automation](#pre-commit-automation)
6. [CI/CD Integration](#cicd-integration)
7. [Complete Workflow](#complete-workflow)

---

## Introduction to Code Quality

### What is Code Quality?

Code quality encompasses:
- **Readability**: Easy to understand
- **Consistency**: Uniform style
- **Correctness**: No bugs or errors
- **Maintainability**: Easy to modify
- **Performance**: Efficient execution

### Code Quality Tools

```
Black      → Formatting (style)
Ruff       → Linting (quality)
mypy       → Type checking (safety)
pre-commit → Automation (enforcement)
```

---

## Black - Code Formatting

### What is Black?

Black is an opinionated code formatter that automatically reformats Python code to a consistent style, eliminating debates about formatting.

### Before and After Black

```python
# Before Black
def very_long_function_name(parameter_one, parameter_two,
                           parameter_three, parameter_four):
    return parameter_one + parameter_two + parameter_three

# After Black
def very_long_function_name(
    parameter_one, parameter_two, parameter_three, parameter_four
):
    return parameter_one + parameter_two + parameter_three
```

### Black Formatting Rules

1. **Line Length**: Default 88 characters
2. **Quotes**: Prefers double quotes
3. **Trailing Commas**: Added in multi-line collections
4. **Parentheses**: Added when needed for line length
5. **Strings**: Prefers double quotes, normalizes escaping

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

### Black Commands

```bash
# Format a file
black myfile.py

# Format entire project
black .

# Check without modifying
black --check .

# Show diff without modifying
black --diff myfile.py
```

---

## Ruff - Linting

### What is Ruff?

Ruff is a fast Python linter (written in Rust) that checks for:
- PEP 8 style violations
- Unused imports and variables
- Type errors
- Security issues
- Code complexity problems

### Ruff Output Example

```
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

### Ruff Commands

```bash
# Check for issues
ruff check .

# Fix auto-fixable issues
ruff check --fix .

# Check specific file
ruff check myfile.py

# Select specific rules
ruff check --select E501 .
```

---

## mypy - Type Checking

### What is mypy?

mypy performs static type checking before runtime, catching type errors early using Python's type hint system.

### Without vs With Type Hints

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

### Type Hints Basics

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
from typing import Callable

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

# Generate HTML report
mypy --html-report mypy_report .
```

---

## pre-commit - Automation

### What are Pre-commit Hooks?

Pre-commit hooks run automated checks before each commit, preventing bad code from being committed.

### Workflow

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

### Pre-commit Commands

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

## CI/CD Integration

### GitHub Actions Example

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
        run: |
          pip install poetry
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

## Complete Workflow

### Development Workflow

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
| pre-commit | Automate checks | On every commit |

### Configuration Strategy

```
pyproject.toml          - Black, Ruff, mypy, pytest config
.pre-commit-config.yaml - Pre-commit hooks
.github/workflows/      - CI/CD pipelines
```

---

## Best Practices

### 1. Use All Tools Together

```bash
# Format
black .

# Lint and fix
ruff check --fix .

# Type check
mypy .

# Test
pytest

# Or let pre-commit handle it
pre-commit run --all-files
```

### 2. Configure Tools Consistently

```toml
# pyproject.toml
[tool.black]
line-length = 88

[tool.ruff]
line-length = 88  # Same as Black

[tool.mypy]
python_version = "3.9"
```

### 3. Commit Configuration Files

```bash
git add pyproject.toml
git add .pre-commit-config.yaml
git commit -m "Add quality tools configuration"
```

### 4. Run Checks Locally First

```bash
# Before pushing
black . && ruff check . && mypy . && pytest
```

---

## Summary

### Key Tools

1. **Black**: Automatic formatting → Consistency
2. **Ruff**: Fast linting → Code quality
3. **mypy**: Type checking → Error detection
4. **pre-commit**: Automated hooks → Quality enforcement

### Typical Setup

```
project/
├── pyproject.toml           # Tool configuration
├── .pre-commit-config.yaml  # Pre-commit hooks
├── .github/
│   └── workflows/
│       └── quality.yml      # CI/CD
├── src/
│   └── myproject/
│       └── *.py
└── tests/
    └── test_*.py
```

### Command Reference

```bash
# Black
black .                 # Format
black --check .         # Check only

# Ruff
ruff check .            # Check
ruff check --fix .      # Fix

# mypy
mypy .                  # Type check
mypy --strict .         # Strict mode

# pre-commit
pre-commit install      # Install
pre-commit run --all-files  # Run all
```

---

## Next Steps

After mastering code quality tools:
1. Learn continuous integration/deployment
2. Explore code coverage analysis
3. Study security scanning tools
4. Learn performance profiling
5. Master debugging techniques
