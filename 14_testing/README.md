# Chapter 14: Testing

Master Python testing with unittest, pytest, mocking, and test-driven development.

## What You'll Learn

- unittest framework basics
- pytest for simpler testing
- Test fixtures and setup/teardown
- Mocking and patching
- Testing async code
- Test coverage concepts
- Test-driven development (TDD)

## Files

- [theory.md](theory.md) - Testing fundamentals
- [examples.md](examples.md) - Practical examples
- [exercises.md](exercises.md) - Practice problems
- [solutions.md](solutions.md) - Solutions
- [tips.md](tips.md) - Best practices

## Quick Reference

### Basic unittest
```python
import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()
```

### pytest
```python
def test_addition():
    assert 2 + 2 == 4

def test_string():
    assert "hello".upper() == "HELLO"
```

### Mocking
```python
from unittest.mock import Mock, patch

@patch('module.expensive_function')
def test_with_mock(mock_func):
    mock_func.return_value = 42
    result = my_function()
    assert result == 42
```

## Prerequisites

- Basic Python syntax
- Functions and classes
- Understanding of assertions

## Next Steps

- Chapter 23: Pytest Advanced
- Test-driven development
- Integration testing
