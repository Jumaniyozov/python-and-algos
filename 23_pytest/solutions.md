# Testing with pytest - Solutions

Solutions extracted from the pytest-related content in 25_dev_tools.
For complete solutions, see examples.md which contains working code for all test patterns.

## Key Solution Patterns

### Solution Pattern 1: Basic Unit Tests

```python
import pytest

def test_function():
    # Arrange
    input_data = "test"
    
    # Act
    result = process(input_data)
    
    # Assert
    assert result == expected
```

### Solution Pattern 2: Using Fixtures

```python
@pytest.fixture
def sample_data():
    return {'key': 'value'}

def test_with_fixture(sample_data):
    assert sample_data['key'] == 'value'
```

### Solution Pattern 3: Parametrized Tests

```python
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert input * 2 == expected
```

### Solution Pattern 4: Exception Testing

```python
def test_exception():
    with pytest.raises(ValueError):
        invalid_function()
```

### Solution Pattern 5: Mocking

```python
def test_with_mock(mocker):
    mock_func = mocker.patch('module.function')
    mock_func.return_value = 'mocked'
    result = module.function()
    assert result == 'mocked'
```

## Complete Solutions

For detailed solutions to all exercises:
1. See examples.md for working code patterns
2. Practice implementing each pattern
3. Run tests with `pytest -v`
4. Check coverage with `pytest --cov`

Refer to theory.md for conceptual explanations of each testing pattern.
