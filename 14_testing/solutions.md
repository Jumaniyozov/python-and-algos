# Testing - Solutions

## Solution 1: Test String Functions

```python
import unittest

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

class TestStringFunctions(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome(""))
```

## Solution 2: Test Calculator Class

```python
import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.333, places=2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
```

## Solution 3: Test with Fixtures

```python
import pytest

class UserDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, id, name):
        self.users[id] = name

    def get_user(self, id):
        return self.users.get(id)

    def delete_user(self, id):
        return self.users.pop(id, None)

@pytest.fixture
def db():
    database = UserDatabase()
    database.add_user(1, 'Alice')
    database.add_user(2, 'Bob')
    return database

def test_get_user(db):
    assert db.get_user(1) == 'Alice'
    assert db.get_user(2) == 'Bob'

def test_get_nonexistent_user(db):
    assert db.get_user(999) is None

def test_add_user(db):
    db.add_user(3, 'Charlie')
    assert db.get_user(3) == 'Charlie'

def test_delete_user(db):
    result = db.delete_user(1)
    assert result == 'Alice'
    assert db.get_user(1) is None
```

## Solution 4: Mock API Calls

```python
from unittest.mock import patch
import requests

def get_github_user(username):
    response = requests.get(f'https://api.github.com/users/{username}')
    if response.status_code == 200:
        return response.json()
    return None

def test_get_github_user_success():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'login': 'octocat',
            'name': 'The Octocat'
        }

        result = get_github_user('octocat')

        assert result == {'login': 'octocat', 'name': 'The Octocat'}
        mock_get.assert_called_once_with('https://api.github.com/users/octocat')

def test_get_github_user_not_found():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404

        result = get_github_user('nonexistent')

        assert result is None
```

## Solution 5: Parametrized Tests

```python
import pytest

def validate_email(email):
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

@pytest.mark.parametrize("email,expected", [
    ("test@example.com", True),
    ("user.name@domain.co.uk", True),
    ("invalid.email", False),
    ("@example.com", False),
    ("user@", False),
    ("", False),
])
def test_validate_email(email, expected):
    assert validate_email(email) == expected
```

## Solutions 6-10: Key Implementations

**Solution 6: Test Exception Handling**
```python
import unittest

def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return f"Age is {age}"

class TestProcessAge(unittest.TestCase):
    def test_valid_age(self):
        self.assertEqual(process_age(25), "Age is 25")

    def test_negative_age(self):
        with self.assertRaises(ValueError) as cm:
            process_age(-1)
        self.assertIn("negative", str(cm.exception))

    def test_unrealistic_age(self):
        with self.assertRaises(ValueError) as cm:
            process_age(200)
        self.assertIn("unrealistic", str(cm.exception))
```

**Solution 7: Test File Operations**
```python
import pytest
import tempfile
import os

def count_lines(filepath):
    with open(filepath) as f:
        return len(f.readlines())

def test_count_lines():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write("Line 1\nLine 2\nLine 3\n")
        filepath = f.name

    try:
        assert count_lines(filepath) == 3
    finally:
        os.unlink(filepath)
```

**Solution 8: Test Async Function**
```python
import pytest
import asyncio

async def async_process(data):
    await asyncio.sleep(0.1)
    return data.upper()

@pytest.mark.asyncio
async def test_async_process():
    result = await async_process("hello")
    assert result == "HELLO"
```

**Solution 10: Test Coverage**
```python
import unittest

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

class TestGrade(unittest.TestCase):
    def test_grade_a(self):
        self.assertEqual(grade(95), 'A')
        self.assertEqual(grade(90), 'A')

    def test_grade_b(self):
        self.assertEqual(grade(85), 'B')
        self.assertEqual(grade(80), 'B')

    def test_grade_c(self):
        self.assertEqual(grade(75), 'C')
        self.assertEqual(grade(70), 'C')

    def test_grade_d(self):
        self.assertEqual(grade(65), 'D')
        self.assertEqual(grade(60), 'D')

    def test_grade_f(self):
        self.assertEqual(grade(59), 'F')
        self.assertEqual(grade(0), 'F')
```
