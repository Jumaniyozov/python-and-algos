# Testing - Exercises

## Exercise 1: Test String Functions
Write tests for string manipulation functions.

```python
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Write tests for both functions
```

## Exercise 2: Test Calculator Class
Create comprehensive tests for a calculator.

```python
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

# Write unittest tests for all methods
```

## Exercise 3: Test with Fixtures
Test a database class using fixtures.

```python
class UserDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, id, name):
        self.users[id] = name

    def get_user(self, id):
        return self.users.get(id)

    def delete_user(self, id):
        return self.users.pop(id, None)

# Write pytest tests with fixture
```

## Exercise 4: Mock API Calls
Test a function that makes API calls using mocks.

```python
import requests

def get_github_user(username):
    response = requests.get(f'https://api.github.com/users/{username}')
    if response.status_code == 200:
        return response.json()
    return None

# Write test using unittest.mock
```

## Exercise 5: Parametrized Tests
Write parametrized tests for input validation.

```python
def validate_email(email):
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Write parametrized tests with valid and invalid emails
```

## Exercise 6: Test Exception Handling
Test error conditions.

```python
def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return f"Age is {age}"

# Test normal and error cases
```

## Exercise 7: Test File Operations
Test file reading/writing (use temp files).

```python
def count_lines(filepath):
    with open(filepath) as f:
        return len(f.readlines())

# Write tests using temp files
```

## Exercise 8: Test Async Function
Test an async function.

```python
import asyncio

async def async_process(data):
    await asyncio.sleep(0.1)
    return data.upper()

# Write async test
```

## Exercise 9: Integration Test
Test multiple components together.

```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append({'item': item, 'price': price})

    def total(self):
        return sum(item['price'] for item in self.items)

# Write integration tests
```

## Exercise 10: Test Coverage
Write tests to achieve 100% coverage.

```python
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

# Write tests covering all branches
```
