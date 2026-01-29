# Code Quality Tools - Examples

Examples extracted from Black, Ruff, mypy, and pre-commit sections of original 25_dev_tools/examples.md.

## Black Examples (Lines 6-79 of original)

### Example 1: Before and After Formatting

```python
# BEFORE.py
def calculate(x,y,z):
    result=x+y*z
    return result

# Run: black BEFORE.py

# AFTER.py  
def calculate(x, y, z):
    result = x + y * z
    return result
```

## Ruff Examples (Lines 80-145 of original)

### Example 2: Finding and Fixing Issues

```python
# issues.py
import os  # F401: unused import
x = 1  # F841: unused variable

# Run: ruff check --fix issues.py
```

## mypy Examples (Lines 346-411 of original)

### Example 3: Type Checking

```python
from typing import List, Dict

def process_numbers(numbers: List[int]) -> Dict[str, int]:
    return {'sum': sum(numbers), 'count': len(numbers)}

# Run: mypy myfile.py
```

## Pre-commit Examples (Lines 412-501 of original)

### Example 4: Pre-commit Setup

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
```

For complete examples, see original 25_dev_tools/examples.md or refer to theory.md.
