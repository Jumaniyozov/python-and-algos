# Testing - Examples

## Example 1: Basic unittest

```python
import unittest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

## Example 2: pytest Tests

```python
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)
```

## Example 3: Test Fixtures

```python
import pytest

class Database:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

@pytest.fixture
def db():
    database = Database()
    database.connect()
    yield database
    database.disconnect()

def test_database_query(db):
    assert db.connected
    # Use db for testing
```

## Example 4: Mocking with unittest.mock

```python
from unittest.mock import Mock, patch
import requests

def get_user_data(user_id):
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()

def test_get_user_data():
    with patch('requests.get') as mock_get:
        # Configure mock
        mock_get.return_value.json.return_value = {'name': 'Alice', 'id': 1}

        # Call function
        result = get_user_data(1)

        # Verify
        assert result == {'name': 'Alice', 'id': 1}
        mock_get.assert_called_once_with('https://api.example.com/users/1')
```

## Example 5: Parametrized Tests

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50),
])
def test_add_multiple(a, b, expected):
    assert add(a, b) == expected
```

## Example 6: Testing Classes

```python
import unittest

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_initial_balance(self):
        account = BankAccount(50)
        self.assertEqual(account.balance, 50)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)
```

## Example 7: Mocking External API

```python
from unittest.mock import patch
import requests

class WeatherClient:
    def get_temperature(self, city):
        response = requests.get(f'https://api.weather.com/{city}')
        return response.json()['temperature']

def test_weather_client():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'temperature': 25}

        client = WeatherClient()
        temp = client.get_temperature('London')

        assert temp == 25
```

## Example 8: Testing Async Code

```python
import pytest
import asyncio

async def fetch_data():
    await asyncio.sleep(0.1)
    return {'data': 'value'}

@pytest.mark.asyncio
async def test_fetch_data():
    result = await fetch_data()
    assert result == {'data': 'value'}
```

## Example 9: doctest

```python
def factorial(n):
    """
    Calculate factorial of n.

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

## Example 10: Test Coverage

```bash
# Install coverage
pip install pytest-cov

# Run tests with coverage
pytest --cov=mymodule tests/

# Generate HTML report
pytest --cov=mymodule --cov-report=html tests/
```
