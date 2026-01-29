# Testing - Tips and Best Practices

## Essential Best Practices

### 1. Test One Thing Per Test

**Bad**:
```python
def test_calculator():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.subtract(5, 2) == 3
    assert calc.multiply(2, 3) == 6
    # Too many things!
```

**Good**:
```python
def test_calculator_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_calculator_subtract():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3
```

### 2. Use Descriptive Test Names

**Bad**:
```python
def test_1():
    pass

def test_user():
    pass
```

**Good**:
```python
def test_should_return_empty_list_when_no_users_exist():
    pass

def test_should_raise_error_when_email_is_invalid():
    pass
```

### 3. Follow AAA Pattern

```python
def test_user_creation():
    # Arrange
    name = "Alice"
    email = "alice@example.com"

    # Act
    user = User(name, email)

    # Assert
    assert user.name == name
    assert user.email == email
```

### 4. Don't Test Implementation Details

**Bad** (tests implementation):
```python
def test_uses_list_internally():
    obj = MyClass()
    assert isinstance(obj._internal_list, list)  # Testing private detail
```

**Good** (tests behavior):
```python
def test_stores_items():
    obj = MyClass()
    obj.add('item')
    assert 'item' in obj.get_all()  # Testing public behavior
```

### 5. Use Fixtures for Setup

**Bad**:
```python
def test_1():
    db = Database()
    db.connect()
    # test...
    db.disconnect()

def test_2():
    db = Database()
    db.connect()
    # test...
    db.disconnect()
```

**Good**:
```python
@pytest.fixture
def db():
    database = Database()
    database.connect()
    yield database
    database.disconnect()

def test_1(db):
    # Use db

def test_2(db):
    # Use db
```

## Common Pitfalls

### 1. Tests Depending on Each Other

**Bad**:
```python
class TestUser(unittest.TestCase):
    user = None

    def test_1_create_user(self):
        self.user = User("Alice")

    def test_2_user_name(self):
        assert self.user.name == "Alice"  # Fails if test_1 doesn't run first!
```

**Good**:
```python
class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Alice")

    def test_user_name(self):
        assert self.user.name == "Alice"
```

### 2. Not Cleaning Up Resources

**Bad**:
```python
def test_file():
    f = open('test.txt', 'w')
    f.write('test')
    # File never closed!
```

**Good**:
```python
def test_file():
    with open('test.txt', 'w') as f:
        f.write('test')
    # Automatically closed
```

### 3. Catching Too Many Exceptions

**Bad**:
```python
def test_error():
    with pytest.raises(Exception):  # Too broad!
        risky_function()
```

**Good**:
```python
def test_error():
    with pytest.raises(ValueError):  # Specific exception
        risky_function()
```

## Mocking Best Practices

### 1. Mock at the Right Level

**Bad** (mocking too deep):
```python
@patch('json.loads')  # Too low-level
def test_api_call(mock_json):
    pass
```

**Good** (mock the API call):
```python
@patch('requests.get')  # Right level
def test_api_call(mock_get):
    pass
```

### 2. Verify Mock Calls

```python
@patch('requests.get')
def test_api(mock_get):
    mock_get.return_value.json.return_value = {'data': 'value'}

    result = my_function()

    # Verify the call
    mock_get.assert_called_once()
    mock_get.assert_called_with('https://api.example.com/data')
```

### 3. Use return_value vs side_effect

```python
# return_value: Same value each call
mock.return_value = 42

# side_effect: Different values or raise exception
mock.side_effect = [1, 2, 3]  # Returns 1, then 2, then 3
mock.side_effect = ValueError("Error")  # Raises exception
```

## pytest Tips

### 1. Use Markers

```python
@pytest.mark.slow
def test_slow_operation():
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass

# Run only slow tests
# pytest -m slow

# Skip slow tests
# pytest -m "not slow"
```

### 2. Use Fixtures Wisely

```python
# Auto-use fixture (runs for all tests)
@pytest.fixture(autouse=True)
def setup_teardown():
    # Setup
    yield
    # Teardown

# Scope: function (default), class, module, session
@pytest.fixture(scope="module")
def expensive_resource():
    # Created once per module
    pass
```

### 3. Parametrize Complex Cases

```python
@pytest.mark.parametrize("input,expected", [
    pytest.param(valid_data, True, id="valid"),
    pytest.param(invalid_data, False, id="invalid"),
    pytest.param(edge_case, True, id="edge", marks=pytest.mark.xfail),
])
def test_validation(input, expected):
    assert validate(input) == expected
```

## Test Organization

### 1. Directory Structure

```
project/
├── src/
│   └── mymodule.py
└── tests/
    ├── __init__.py
    ├── test_mymodule.py
    └── conftest.py  # Shared fixtures
```

### 2. Naming Convention

- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_*`
- Test classes: `Test*`

### 3. Group Related Tests

```python
class TestUserAuthentication:
    def test_login_success(self):
        pass

    def test_login_invalid_password(self):
        pass

    def test_logout(self):
        pass

class TestUserProfile:
    def test_update_profile(self):
        pass

    def test_delete_profile(self):
        pass
```

## Coverage Tips

### 1. Aim for High Coverage (>80%)

```bash
# Generate coverage report
pytest --cov=mymodule --cov-report=html

# View in browser
open htmlcov/index.html
```

### 2. But Don't Chase 100%

- Some code is hard to test (edge cases)
- Some code is trivial (getters/setters)
- Focus on critical paths

### 3. Find Untested Code

```bash
# Show lines not covered
pytest --cov=mymodule --cov-report=term-missing
```

## Quick Reference

**Run tests**:
```bash
# pytest
pytest
pytest tests/test_module.py
pytest -v  # Verbose
pytest -k "test_user"  # Match pattern

# unittest
python -m unittest discover
python -m unittest tests.test_module
```

**Common assertions**:
```python
# pytest
assert x == y
assert x in y
assert x is None
with pytest.raises(ValueError):
    func()

# unittest
self.assertEqual(x, y)
self.assertIn(x, y)
self.assertIsNone(x)
with self.assertRaises(ValueError):
    func()
```

**Fixtures**:
```python
@pytest.fixture
def resource():
    r = create()
    yield r
    cleanup(r)
```

**Mocking**:
```python
from unittest.mock import patch

@patch('module.function')
def test(mock_func):
    mock_func.return_value = 42
    # test...
```
