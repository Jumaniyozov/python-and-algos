# Testing with pytest - Tips and Best Practices

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

### 2. pytest Configuration

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
from unittest.mock import Mock, patch

def test_with_mock():
    # Create mock
    mock_func = Mock(return_value=42)
    result = mock_func()
    assert result == 42

@patch('module.function')
def test_with_patch(mock_function):
    mock_function.return_value = 100
    assert mock_function.called

def test_with_mocker(mocker):
    mock_func = mocker.patch('module.function')
    mock_func.return_value = 'mocked'
    result = module.function()
    assert result == 'mocked'
```

## Best Practices

### Test Naming

```python
# GOOD: Descriptive names
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

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

### Test Independence

```python
# GOOD: Tests don't depend on each other
def test_a():
    result = function_a()
    assert result == expected

def test_b():
    result = function_b()
    assert result == expected
```

## Coverage Tips

```bash
# Run with coverage
pytest --cov=myproject

# HTML report
pytest --cov=myproject --cov-report=html

# Show missing lines
pytest --cov=myproject --cov-report=term-missing

# Fail if coverage below threshold
pytest --cov=myproject --cov-fail-under=80
```

## Common Commands

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

## Resources

- pytest documentation: https://docs.pytest.org/
- pytest-cov: https://pytest-cov.readthedocs.io/
- pytest-mock: https://pytest-mock.readthedocs.io/

## Testing Workflow

```
1. Write test (or code)
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
