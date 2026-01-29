# Testing with pytest - Theory

## Table of Contents

1. [Introduction to Testing](#introduction-to-testing)
2. [pytest Basics](#pytest-basics)
3. [Assertions](#assertions)
4. [Fixtures](#fixtures)
5. [Parametrized Tests](#parametrized-tests)
6. [Test Organization](#test-organization)
7. [Mocking and Patching](#mocking-and-patching)
8. [Test Coverage](#test-coverage)
9. [pytest Configuration](#pytest-configuration)
10. [Best Practices](#best-practices)

---

## Introduction to Testing

### What is Software Testing?

Software testing verifies that code behaves as expected. Tests:
- Catch bugs before production
- Document expected behavior
- Enable safe refactoring
- Improve code design
- Build confidence

### Types of Tests

```
Unit Tests
  ├─ Test individual functions/methods
  ├─ Fast, isolated, numerous
  └─ Example: Test a calculation function

Integration Tests
  ├─ Test multiple components together
  ├─ Slower, more comprehensive
  └─ Example: Test database interactions

End-to-End Tests
  ├─ Test complete user workflows
  ├─ Slowest, most realistic
  └─ Example: Test full API request/response
```

### Why pytest?

pytest advantages:
- Simple, Pythonic syntax
- Powerful features (fixtures, parametrization)
- Excellent error messages
- Rich plugin ecosystem
- Scales from simple to complex projects

---

## pytest Basics

### Test Discovery

pytest automatically finds tests:

```python
# pytest discovers:
test_*.py        # Files starting with "test_"
*_test.py        # Files ending with "_test"
test_*()         # Functions starting with "test_"
Test*            # Classes starting with "Test"
```

### Simple Test Example

```python
# test_example.py
def test_addition():
    """Test that addition works"""
    assert 2 + 2 == 4

def test_string_methods():
    """Test string operations"""
    text = "hello"
    assert text.upper() == "HELLO"
    assert text.capitalize() == "Hello"
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific file
pytest test_example.py

# Run specific test
pytest test_example.py::test_addition

# Verbose output
pytest -v

# Show print statements
pytest -s
```

---

## Assertions

### Basic Assertions

```python
# Equality
assert x == y
assert x != y

# Comparison
assert x > y
assert x >= y
assert x < y
assert x <= y

# Identity
assert x is y
assert x is not y
assert x is None
assert x is not None

# Membership
assert x in [1, 2, 3]
assert x not in [1, 2, 3]

# Boolean
assert x
assert not x
assert x is True
assert x is False
```

### Type Assertions

```python
# Type checking
assert isinstance(x, int)
assert isinstance(x, (int, float))
assert callable(func)
assert hasattr(obj, 'method')
```

### Exception Testing

```python
import pytest

def test_exception():
    """Test that function raises expected exception"""
    with pytest.raises(ValueError):
        int("not a number")

    with pytest.raises(ValueError, match="invalid"):
        raise ValueError("invalid input")
```

### Approximate Comparisons

```python
import pytest

def test_float_comparison():
    """Test floating point equality"""
    # Use pytest.approx for float comparisons
    assert 0.1 + 0.2 == pytest.approx(0.3)

    # Specify relative tolerance
    assert 3.14159 == pytest.approx(3.14, rel=1e-2)

    # Specify absolute tolerance
    assert 100.001 == pytest.approx(100, abs=0.01)
```

---

## Fixtures

### What are Fixtures?

Fixtures provide:
- Test data setup
- Resource initialization
- Cleanup after tests
- Reusable test components
- Dependency injection

### Basic Fixtures

```python
import pytest

@pytest.fixture
def sample_data():
    """Provide sample data for tests"""
    return {'name': 'John', 'age': 30}

def test_with_fixture(sample_data):
    """Test using fixture"""
    assert sample_data['name'] == 'John'
    assert sample_data['age'] == 30
```

### Fixture Scope

```python
@pytest.fixture(scope="function")  # Default: once per test
def fixture_function():
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
```

### Fixture Cleanup

```python
import pytest
from pathlib import Path
import tempfile

@pytest.fixture
def temp_file():
    """Create temporary file, cleanup after test"""
    # Setup
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"test content")
        temp_path = Path(f.name)

    # Provide to test
    yield temp_path

    # Cleanup (runs after test)
    temp_path.unlink()

def test_file_operations(temp_file):
    assert temp_file.exists()
    assert temp_file.read_bytes() == b"test content"
    # temp_file automatically cleaned up after test
```

### Built-in Fixtures

```python
def test_with_tmp_path(tmp_path):
    """Use pytest's tmp_path fixture"""
    # tmp_path is a Path object to temporary directory
    file = tmp_path / "test.txt"
    file.write_text("content")
    assert file.read_text() == "content"

def test_with_capsys(capsys):
    """Capture stdout/stderr"""
    print("Hello, World!")
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"

def test_with_monkeypatch(monkeypatch):
    """Modify environment, attributes temporarily"""
    monkeypatch.setenv("API_KEY", "test_key")
    monkeypatch.setattr("module.function", lambda: "mocked")
```

---

## Parametrized Tests

### Basic Parametrization

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
    (10, 20),
])
def test_double(input, expected):
    """Test doubling with multiple inputs"""
    assert input * 2 == expected
```

### Multiple Parameters

```python
@pytest.mark.parametrize("x,y,result", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_addition(x, y, result):
    assert x + y == result
```

### Naming Test Cases

```python
@pytest.mark.parametrize("input,expected", [
    pytest.param(2, 4, id="positive"),
    pytest.param(0, 0, id="zero"),
    pytest.param(-2, -4, id="negative"),
])
def test_double_with_ids(input, expected):
    assert input * 2 == expected
```

### Multiple Parametrize Decorators

```python
@pytest.mark.parametrize("x", [0, 1, 2])
@pytest.mark.parametrize("y", [0, 1, 2])
def test_multiplication(x, y):
    """Runs 9 times (3 x 3)"""
    result = x * y
    assert isinstance(result, int)
```

---

## Test Organization

### Directory Structure

```
project/
├── src/
│   └── mymodule/
│       ├── __init__.py
│       ├── calculator.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Shared fixtures
│   ├── test_calculator.py
│   ├── test_utils.py
│   ├── unit/                # Unit tests
│   │   ├── test_functions.py
│   │   └── test_classes.py
│   └── integration/         # Integration tests
│       └── test_api.py
└── pyproject.toml
```

### conftest.py

```python
# tests/conftest.py
import pytest

@pytest.fixture
def shared_fixture():
    """Available to all tests in this directory and subdirectories"""
    return {'key': 'value'}

@pytest.fixture(scope="session")
def database_connection():
    """Setup once for all tests"""
    # Setup database
    conn = setup_db()
    yield conn
    # Teardown
    conn.close()
```

### Test Classes

```python
class TestCalculator:
    """Group related tests"""

    def test_add(self):
        assert 2 + 2 == 4

    def test_subtract(self):
        assert 5 - 3 == 2

    @pytest.fixture(autouse=True)
    def setup_method_fixture(self):
        """Runs before each test method"""
        self.calculator = Calculator()
```

---

## Mocking and Patching

### Why Mock?

Mocking isolates code under test:
- Avoid external dependencies (APIs, databases)
- Control test conditions
- Speed up tests
- Test error conditions

### Basic Mocking

```python
from unittest.mock import Mock

def test_with_mock():
    # Create mock object
    mock_function = Mock(return_value=42)

    # Use mock
    result = mock_function()

    # Verify
    assert result == 42
    assert mock_function.called
    assert mock_function.call_count == 1
```

### Patching

```python
from unittest.mock import patch

@patch('requests.get')
def test_api_call(mock_get):
    """Mock external API call"""
    # Configure mock
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'data': 'test'}

    # Test code that calls requests.get
    response = fetch_data()

    # Verify
    assert response == {'data': 'test'}
    assert mock_get.called
```

### pytest-mock Plugin

```python
# More Pythonic mocking with pytest-mock
def test_with_mocker(mocker):
    # Mock function
    mock_func = mocker.patch('module.function')
    mock_func.return_value = 'mocked'

    # Test
    result = module.function()
    assert result == 'mocked'
```

---

## Test Coverage

### What is Coverage?

Test coverage measures which code lines are executed during tests:
- Identifies untested code
- Guides test writing
- Quality metric (not perfection)
- Typical target: 80-90%

### Using pytest-cov

```bash
# Install
pip install pytest-cov

# Run with coverage
pytest --cov=myproject

# HTML report
pytest --cov=myproject --cov-report=html

# Show missing lines
pytest --cov=myproject --cov-report=term-missing

# Fail if coverage below threshold
pytest --cov=myproject --cov-fail-under=80
```

### Coverage Configuration

```toml
# pyproject.toml
[tool.pytest.ini_options]
addopts = """
    --cov=myproject
    --cov-report=term-missing
    --cov-report=html
"""

[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*", "*/migrations/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
]
```

---

## pytest Configuration

### pyproject.toml Configuration

```toml
[tool.pytest.ini_options]
# Test discovery
testpaths = ["tests"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"

# Output options
addopts = """
    -v
    --strict-markers
    --tb=short
    --cov=myproject
    --cov-report=term-missing
"""

# Custom markers
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
]
```

### Using Markers

```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    """Takes a long time"""
    pass

@pytest.mark.integration
def test_api_integration():
    """Integration test"""
    pass

# Run only unit tests
# pytest -m unit

# Skip slow tests
# pytest -m "not slow"
```

---

## Best Practices

### Test Naming

```python
# GOOD: Descriptive names
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_raises_type_error_for_strings():
    with pytest.raises(TypeError):
        add("2", "3")

# BAD: Vague names
def test_1():
    pass
```

### Arrange-Act-Assert Pattern

```python
def test_user_creation():
    # Arrange: Set up test data
    name = "John"
    email = "john@example.com"

    # Act: Perform action
    user = User(name, email)

    # Assert: Verify outcome
    assert user.name == name
    assert user.email == email
```

### One Assertion Per Test (When Possible)

```python
# GOOD: Focused tests
def test_user_name():
    user = User("John", "john@example.com")
    assert user.name == "John"

def test_user_email():
    user = User("John", "john@example.com")
    assert user.email == "john@example.com"

# ACCEPTABLE: Related assertions
def test_user_properties():
    user = User("John", "john@example.com")
    assert user.name == "John"
    assert user.email == "john@example.com"
    assert user.is_active is True
```

### Test Independence

```python
# GOOD: Tests don't depend on each other
def test_a():
    result = function_a()
    assert result == expected

def test_b():
    result = function_b()
    assert result == expected

# BAD: Tests depend on order
shared_state = None

def test_setup():
    global shared_state
    shared_state = setup()

def test_use_state():  # Fails if test_setup doesn't run first
    assert shared_state is not None
```

---

## Summary

### Key Testing Concepts

1. **Unit Tests**: Test individual components in isolation
2. **Fixtures**: Reusable setup and teardown code
3. **Parametrization**: Test multiple scenarios efficiently
4. **Mocking**: Isolate code from external dependencies
5. **Coverage**: Measure test completeness
6. **Organization**: Structure tests logically

### pytest Command Reference

```bash
pytest                          # Run all tests
pytest test_file.py             # Run specific file
pytest test_file.py::test_func  # Run specific test
pytest -v                       # Verbose output
pytest -s                       # Show print statements
pytest -x                       # Stop on first failure
pytest -k "test_name"           # Run tests matching pattern
pytest -m marker                # Run tests with marker
pytest --lf                     # Run last failed
pytest --cov                    # Coverage report
```

### Testing Workflow

```
1. Write test (TDD) or code (test after)
   ↓
2. Run tests (pytest)
   ↓
3. Tests fail? → Fix code/tests
   ↓
4. Tests pass? → Check coverage
   ↓
5. Low coverage? → Add tests
   ↓
6. Commit with confidence
```

---

## Next Steps

After understanding pytest basics:
1. Practice writing tests for existing code
2. Try test-driven development (TDD)
3. Learn integration testing techniques
4. Explore pytest plugins
5. Set up continuous integration
