# Chapter 23: Testing with pytest

## Overview

This chapter covers comprehensive testing with pytest, Python's most popular testing framework. You'll learn how to write effective unit tests, use fixtures, parametrize tests, mock dependencies, and integrate testing into your development workflow.

## What You'll Learn

- **pytest Basics**: Writing and running tests
- **Assertions**: Testing conditions and expectations
- **Fixtures**: Setting up test data and environments
- **Parametrized Tests**: Testing multiple scenarios efficiently
- **Mocking**: Isolating code under test
- **Test Organization**: Structuring test suites
- **Coverage**: Measuring test completeness
- **pytest Plugins**: Extending functionality

## Why It Matters

Testing ensures:
- Code works as expected
- Changes don't break existing functionality
- Edge cases are handled properly
- Bugs are caught early
- Documentation through examples
- Confidence in refactoring
- Professional code quality

## Prerequisites

- Python fundamentals (Chapters 1-7)
- Functions and classes
- Basic command-line skills
- Understanding of imports and modules

## Installation

```bash
# Install pytest
pip install pytest

# Install with coverage
pip install pytest pytest-cov

# Or with Poetry
poetry add --group dev pytest pytest-cov
```

## Chapter Structure

1. **Theory** (`theory.md`): Testing concepts and pytest features
2. **Examples** (`examples.md`): Practical, runnable test examples
3. **Exercises** (`exercises.md`): Progressive testing challenges
4. **Solutions** (`solutions.md`): Complete solutions with explanations
5. **Tips** (`tips.md`): Best practices and workflows

## Quick Start

### Write Your First Test

```python
# test_example.py
def test_addition():
    assert 2 + 2 == 4

def test_string():
    assert "hello".upper() == "HELLO"
```

### Run Tests

```bash
# Run all tests
pytest

# Run specific file
pytest test_example.py

# Run with verbose output
pytest -v

# Show print statements
pytest -s

# Generate coverage report
pytest --cov=myproject
```

### Use Fixtures

```python
import pytest

@pytest.fixture
def sample_data():
    return {'name': 'John', 'age': 30}

def test_with_fixture(sample_data):
    assert sample_data['name'] == 'John'
```

### Parametrize Tests

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert input * 2 == expected
```

## Real-World Applications

- Unit testing for all Python projects
- Integration testing for APIs
- Test-driven development (TDD)
- Continuous integration pipelines
- Regression testing
- Automated quality assurance
- Documentation through tests

## Key Takeaways

By the end of this chapter, you'll be able to:
1. Write effective unit tests with pytest
2. Use fixtures for test setup and teardown
3. Parametrize tests for multiple scenarios
4. Mock external dependencies
5. Organize test suites effectively
6. Measure and improve test coverage
7. Integrate tests into development workflow

## Next Steps

After mastering this chapter:
- Learn Chapter 24: Package Management
- Explore Chapter 25: Code Quality Tools
- Study test-driven development (TDD)
- Learn integration and end-to-end testing
- Master debugging techniques

---

**Time to Complete**: 4-6 hours
**Difficulty**: Beginner to Intermediate
**Practice Projects**: 5-10 test suites recommended
