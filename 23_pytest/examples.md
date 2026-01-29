# Testing with pytest - Examples

## 15 Practical, Runnable Examples

### Example 1: Simple Unit Tests

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

---

### Example 2: Using Fixtures

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

---

### Example 3: Parametrized Tests

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

### Example 4: Testing Exceptions

```python
# calculator.py
class Calculator:
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numbers")
        return a / b

# test_calculator.py
import pytest
from calculator import Calculator

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)

def test_divide_type_error():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.divide("10", 5)

def test_divide_success():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
```

---

### Example 5: Using tmp_path Fixture

```python
# test_file_operations.py
def test_create_file(tmp_path):
    """Test file creation"""
    file = tmp_path / "test.txt"
    file.write_text("Hello, World!")
    assert file.read_text() == "Hello, World!"

def test_create_directory(tmp_path):
    """Test directory creation"""
    dir = tmp_path / "subdir"
    dir.mkdir()
    assert dir.exists()
    assert dir.is_dir()

def test_multiple_files(tmp_path):
    """Test multiple file operations"""
    files = []
    for i in range(3):
        file = tmp_path / f"file{i}.txt"
        file.write_text(f"Content {i}")
        files.append(file)

    assert len(list(tmp_path.iterdir())) == 3
    assert files[1].read_text() == "Content 1"
```

---

### Example 6: Fixture Scopes

```python
# conftest.py
import pytest

@pytest.fixture(scope="function")
def function_fixture():
    """Runs once per test function"""
    print("\nSetup function fixture")
    yield "function_data"
    print("\nTeardown function fixture")

@pytest.fixture(scope="module")
def module_fixture():
    """Runs once per module"""
    print("\nSetup module fixture")
    yield "module_data"
    print("\nTeardown module fixture")

@pytest.fixture(scope="session")
def session_fixture():
    """Runs once per test session"""
    print("\nSetup session fixture")
    yield "session_data"
    print("\nTeardown session fixture")

# test_fixtures.py
def test_one(function_fixture, module_fixture, session_fixture):
    assert function_fixture == "function_data"
    assert module_fixture == "module_data"
    assert session_fixture == "session_data"

def test_two(function_fixture, module_fixture, session_fixture):
    # function_fixture recreated, others reused
    assert function_fixture == "function_data"
    assert module_fixture == "module_data"
    assert session_fixture == "session_data"
```

---

### Example 7: Mocking with pytest-mock

```python
# api_client.py
import requests

def fetch_user(user_id):
    """Fetch user from API"""
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

# test_api_client.py
def test_fetch_user(mocker):
    """Test API call with mocked response"""
    # Mock requests.get
    mock_get = mocker.patch('api_client.requests.get')
    mock_get.return_value.json.return_value = {
        'id': 1,
        'name': 'John Doe'
    }

    # Test
    result = fetch_user(1)

    # Verify
    assert result['id'] == 1
    assert result['name'] == 'John Doe'
    mock_get.assert_called_once_with("https://api.example.com/users/1")
```

---

### Example 8: Using monkeypatch

```python
# config.py
import os

def get_api_key():
    return os.getenv("API_KEY", "default_key")

def get_config():
    return {
        'api_key': get_api_key(),
        'debug': os.getenv("DEBUG", "False") == "True"
    }

# test_config.py
def test_api_key_from_env(monkeypatch):
    """Test with environment variable set"""
    monkeypatch.setenv("API_KEY", "test_key_123")
    assert get_api_key() == "test_key_123"

def test_api_key_default(monkeypatch):
    """Test with no environment variable"""
    monkeypatch.delenv("API_KEY", raising=False)
    assert get_api_key() == "default_key"

def test_config(monkeypatch):
    """Test full config"""
    monkeypatch.setenv("API_KEY", "test_key")
    monkeypatch.setenv("DEBUG", "True")

    config = get_config()
    assert config['api_key'] == "test_key"
    assert config['debug'] is True
```

---

### Example 9: Class-Based Tests

```python
# test_user.py
import pytest

class TestUser:
    """Group related user tests"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup for each test method"""
        self.user_data = {
            'name': 'John',
            'email': 'john@example.com',
            'age': 30
        }

    def test_user_name(self):
        assert self.user_data['name'] == 'John'

    def test_user_email(self):
        assert self.user_data['email'] == 'john@example.com'

    def test_user_age(self):
        assert self.user_data['age'] == 30

class TestUserValidation:
    """Test user validation logic"""

    @pytest.mark.parametrize("age,valid", [
        (0, False),
        (17, False),
        (18, True),
        (100, True),
        (-1, False),
    ])
    def test_age_validation(self, age, valid):
        result = validate_age(age)
        assert result == valid
```

---

### Example 10: Testing with capsys

```python
# printer.py
def print_report(data):
    """Print formatted report"""
    print("=" * 40)
    print(f"Report: {data['title']}")
    print("=" * 40)
    for item in data['items']:
        print(f"- {item}")
    print("=" * 40)

# test_printer.py
def test_print_report(capsys):
    """Test console output"""
    data = {
        'title': 'Test Report',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }

    print_report(data)

    captured = capsys.readouterr()
    output = captured.out

    assert "Test Report" in output
    assert "Item 1" in output
    assert "Item 2" in output
    assert "Item 3" in output
    assert "=" * 40 in output
```

---

### Example 11: Parametrize with IDs

```python
# test_string_operations.py
import pytest

@pytest.mark.parametrize("input,expected", [
    pytest.param("hello", "HELLO", id="lowercase"),
    pytest.param("WORLD", "WORLD", id="uppercase"),
    pytest.param("MiXeD", "MIXED", id="mixed"),
    pytest.param("", "", id="empty"),
])
def test_uppercase(input, expected):
    assert input.upper() == expected

# Run with: pytest test_string_operations.py -v
# Output shows IDs:
# test_string_operations.py::test_uppercase[lowercase] PASSED
# test_string_operations.py::test_uppercase[uppercase] PASSED
# test_string_operations.py::test_uppercase[mixed] PASSED
# test_string_operations.py::test_uppercase[empty] PASSED
```

---

### Example 12: Testing with Markers

```python
# test_performance.py
import pytest
import time

@pytest.mark.slow
def test_slow_operation():
    """This test takes a while"""
    time.sleep(2)
    assert True

@pytest.mark.fast
def test_fast_operation():
    """This test is quick"""
    assert 1 + 1 == 2

@pytest.mark.integration
def test_api_integration():
    """Integration test"""
    # Test API integration
    assert True

# Configure markers in pyproject.toml:
# [tool.pytest.ini_options]
# markers = [
#     "slow: marks tests as slow",
#     "fast: marks tests as fast",
#     "integration: marks tests as integration",
# ]

# Run only fast tests:
# pytest -m fast

# Skip slow tests:
# pytest -m "not slow"
```

---

### Example 13: Testing with Coverage

```python
# calculator.py
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# test_calculator_coverage.py
import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12

def test_divide(calc):
    assert calc.divide(10, 2) == 5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)

# Run with coverage:
# pytest --cov=calculator --cov-report=term-missing
#
# Output shows:
# calculator.py      100%   (all lines covered)
```

---

### Example 14: Shared Fixtures in conftest.py

```python
# tests/conftest.py
import pytest
from pathlib import Path
import json

@pytest.fixture
def sample_json_file(tmp_path):
    """Create sample JSON file"""
    data = {'users': [{'id': 1, 'name': 'Alice'}]}
    file = tmp_path / "data.json"
    file.write_text(json.dumps(data))
    return file

@pytest.fixture
def sample_users():
    """Provide sample user list"""
    return [
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
        {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
    ]

# tests/test_data_processing.py
def test_read_json(sample_json_file):
    """Test reading JSON file"""
    data = json.loads(sample_json_file.read_text())
    assert 'users' in data
    assert len(data['users']) == 1

def test_filter_users(sample_users):
    """Test filtering users"""
    result = [u for u in sample_users if u['id'] > 1]
    assert len(result) == 1
    assert result[0]['name'] == 'Bob'
```

---

### Example 15: Complete Test Suite Example

```python
# user_manager.py
class UserManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def add_user(self, name, email):
        if not name or not email:
            raise ValueError("Name and email required")
        if '@' not in email:
            raise ValueError("Invalid email")

        user_id = self.next_id
        self.users[user_id] = {'id': user_id, 'name': name, 'email': email}
        self.next_id += 1
        return user_id

    def get_user(self, user_id):
        return self.users.get(user_id)

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def count_users(self):
        return len(self.users)

# test_user_manager.py
import pytest
from user_manager import UserManager

@pytest.fixture
def manager():
    """Create fresh UserManager for each test"""
    return UserManager()

class TestUserManager:
    """Complete test suite for UserManager"""

    def test_add_user(self, manager):
        user_id = manager.add_user("John", "john@example.com")
        assert user_id == 1
        assert manager.count_users() == 1

    def test_add_multiple_users(self, manager):
        id1 = manager.add_user("Alice", "alice@example.com")
        id2 = manager.add_user("Bob", "bob@example.com")
        assert id1 == 1
        assert id2 == 2
        assert manager.count_users() == 2

    def test_get_user(self, manager):
        user_id = manager.add_user("John", "john@example.com")
        user = manager.get_user(user_id)
        assert user['name'] == "John"
        assert user['email'] == "john@example.com"

    def test_get_nonexistent_user(self, manager):
        user = manager.get_user(999)
        assert user is None

    def test_delete_user(self, manager):
        user_id = manager.add_user("John", "john@example.com")
        assert manager.delete_user(user_id) is True
        assert manager.count_users() == 0

    def test_delete_nonexistent_user(self, manager):
        assert manager.delete_user(999) is False

    @pytest.mark.parametrize("name,email", [
        ("", "test@example.com"),
        ("John", ""),
        ("", ""),
    ])
    def test_add_user_missing_fields(self, manager, name, email):
        with pytest.raises(ValueError, match="Name and email required"):
            manager.add_user(name, email)

    def test_add_user_invalid_email(self, manager):
        with pytest.raises(ValueError, match="Invalid email"):
            manager.add_user("John", "invalid-email")

# Run all tests:
# pytest test_user_manager.py -v
```

---

## Command Reference

### Running Tests

```bash
# Run all tests
pytest

# Run specific file
pytest test_example.py

# Run specific test
pytest test_example.py::test_function

# Run tests matching pattern
pytest -k "test_add"

# Run with markers
pytest -m slow
pytest -m "not slow"

# Verbose output
pytest -v

# Show print statements
pytest -s

# Stop on first failure
pytest -x

# Run last failed
pytest --lf

# Run tests in parallel (requires pytest-xdist)
pytest -n auto
```

### Coverage Commands

```bash
# Run with coverage
pytest --cov=myproject

# HTML coverage report
pytest --cov=myproject --cov-report=html

# Show missing lines
pytest --cov=myproject --cov-report=term-missing

# Fail if coverage below 80%
pytest --cov=myproject --cov-fail-under=80
```

---

## Integration Example

Complete workflow for testing:

```bash
# 1. Write tests
vim test_module.py

# 2. Run tests
pytest -v

# 3. Check coverage
pytest --cov=myproject --cov-report=html

# 4. Open coverage report
open htmlcov/index.html

# 5. Fix uncovered code, repeat
```
