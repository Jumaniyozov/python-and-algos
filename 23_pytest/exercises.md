# Testing with pytest - Exercises

## 15 Progressive Challenges

### Basic Testing (Exercises 1-3)

#### Exercise 1: Write Simple Unit Tests

Create test file for calculator functions:
```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Write tests covering:
- Normal cases
- Edge cases
- Error conditions

**Tasks:**
1. Create `calculator.py` with the functions
2. Create `test_calculator.py` with at least 10 tests
3. Test positive numbers, negative numbers, zero
4. Test division by zero raises ValueError
5. Run tests with `pytest -v`

---

#### Exercise 2: Test String Operations

Write tests for these string functions:
```python
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')
```

**Requirements:**
- At least 3 tests per function
- Test empty strings
- Test edge cases
- Use descriptive test names

---

#### Exercise 3: Exception Testing

Create a `validator.py` module with validation functions:
```python
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age unrealistic")
    return True

def validate_email(email):
    if not isinstance(email, str):
        raise TypeError("Email must be string")
    if '@' not in email or '.' not in email:
        raise ValueError("Invalid email format")
    return True
```

**Tasks:**
1. Write tests for valid inputs
2. Write tests for each exception type
3. Use `pytest.raises()` with match parameter
4. Test multiple invalid scenarios

---

### Fixtures (Exercises 4-6)

#### Exercise 4: Create and Use Fixtures

**Tasks:**
1. Create fixture that provides sample user data
2. Create fixture that provides sample product list
3. Create fixture for temporary directory
4. Write tests using these fixtures
5. Create fixture with cleanup (using yield)

**Example structure:**
```python
@pytest.fixture
def sample_user():
    # Return user data
    pass

def test_user_name(sample_user):
    # Test using fixture
    pass
```

---

#### Exercise 5: Fixture Scopes

**Tasks:**
1. Create function-scoped fixture
2. Create module-scoped fixture
3. Create session-scoped fixture
4. Add print statements to see when they run
5. Run with `pytest -s` to observe behavior

**Requirements:**
- Demonstrate each scope with examples
- Document when each fixture is created/destroyed
- Create at least 5 tests using different scopes

---

#### Exercise 6: conftest.py Organization

**Tasks:**
1. Create `tests/conftest.py` with shared fixtures
2. Create fixtures for:
   - Database connection (mock)
   - API client (mock)
   - Sample data sets
3. Organize tests in subdirectories
4. Use fixtures from conftest.py in multiple test files

**Directory structure:**
```
tests/
├── conftest.py
├── unit/
│   └── test_functions.py
└── integration/
    └── test_api.py
```

---

### Parametrization (Exercises 7-8)

#### Exercise 7: Basic Parametrized Tests

Create parametrized tests for:

1. **Email validation** - Test multiple email formats
2. **Password strength** - Test various passwords
3. **Number formatting** - Test different number formats

**Requirements:**
- Use `@pytest.mark.parametrize`
- Test at least 5 cases per function
- Include valid and invalid cases
- Use descriptive parameter names

**Example:**
```python
@pytest.mark.parametrize("email,valid", [
    ("user@example.com", True),
    ("invalid", False),
    # Add more cases
])
def test_email_validation(email, valid):
    # Your test here
    pass
```

---

#### Exercise 8: Advanced Parametrization

**Tasks:**
1. Use multiple `@pytest.mark.parametrize` decorators
2. Add custom IDs to test cases with `pytest.param(id="...")`
3. Parametrize fixture arguments
4. Create test matrix (multiple parameters)

**Example test matrix:**
```python
@pytest.mark.parametrize("operation", ["add", "subtract"])
@pytest.mark.parametrize("a,b", [(1, 2), (10, 5), (0, 0)])
def test_operations(operation, a, b):
    # Test all combinations
    pass
```

---

### Mocking (Exercises 9-10)

#### Exercise 9: Mock External Dependencies

Create module that makes API calls:
```python
# api_client.py
import requests

def get_weather(city):
    response = requests.get(f"https://api.weather.com/{city}")
    return response.json()

def get_user_data(user_id):
    response = requests.get(f"https://api.users.com/{user_id}")
    return response.json()
```

**Tasks:**
1. Write tests mocking `requests.get`
2. Test successful responses
3. Test error conditions (404, 500, timeout)
4. Verify correct URLs are called
5. Use `mocker.patch` or `unittest.mock.patch`

---

#### Exercise 10: Monkeypatch Environment

**Tasks:**
1. Create function that reads environment variables
2. Test with different environment configurations
3. Use `monkeypatch` to set/unset variables
4. Test default values when env vars missing
5. Test both development and production configurations

---

### Advanced Testing (Exercises 11-13)

#### Exercise 11: Test Organization

**Create complete test suite:**
1. Organize tests by type (unit/integration)
2. Create shared fixtures in conftest.py
3. Use test classes to group related tests
4. Add markers for slow/fast tests
5. Configure pytest.ini or pyproject.toml

**Requirements:**
- At least 20 tests
- Proper directory structure
- Documented fixtures
- Custom markers configured

---

#### Exercise 12: Test Coverage

**Tasks:**
1. Write code with <50% coverage
2. Run `pytest --cov` to see coverage
3. Identify untested lines
4. Add tests to reach 100% coverage
5. Generate HTML coverage report

**Target module:**
```python
# user_manager.py
class UserManager:
    def add_user(self, name, email):
        # Implementation
        pass

    def delete_user(self, user_id):
        # Implementation
        pass

    def update_user(self, user_id, **kwargs):
        # Implementation
        pass

    def search_users(self, query):
        # Implementation
        pass
```

---

#### Exercise 13: Testing Async Code

Write tests for async functions (requires pytest-asyncio):
```python
# async_operations.py
import asyncio

async def fetch_data(url):
    await asyncio.sleep(1)  # Simulate network delay
    return {"data": "result"}

async def process_batch(items):
    results = []
    for item in items:
        result = await fetch_data(item)
        results.append(result)
    return results
```

**Tasks:**
1. Install pytest-asyncio
2. Write async test functions
3. Use `@pytest.mark.asyncio`
4. Test concurrent operations
5. Mock async operations

---

### Integration Testing (Exercises 14-15)

#### Exercise 14: Database Testing

**Tasks:**
1. Create simple database layer (use SQLite)
2. Write fixtures for database setup/teardown
3. Test CRUD operations
4. Use transactions for test isolation
5. Test error conditions

**Example:**
```python
@pytest.fixture
def db_connection():
    # Setup database
    conn = setup_test_db()
    yield conn
    # Teardown
    conn.close()

def test_insert_user(db_connection):
    # Test user insertion
    pass
```

---

#### Exercise 15: Complete Project Test Suite

**Create full test suite for small application:**

**Application: Todo List Manager**
```python
# todo_manager.py
class TodoManager:
    def __init__(self):
        self.todos = []

    def add_todo(self, title, description=""):
        # Add todo item
        pass

    def complete_todo(self, todo_id):
        # Mark as complete
        pass

    def delete_todo(self, todo_id):
        # Delete todo
        pass

    def get_todos(self, filter="all"):
        # Get todos (all/active/completed)
        pass
```

**Requirements:**
1. Write comprehensive test suite (30+ tests)
2. Use fixtures for test data
3. Parametrize where appropriate
4. Achieve 100% coverage
5. Organize tests logically
6. Add integration tests
7. Document fixtures and setup
8. Configure pytest properly

**Test categories:**
- Unit tests for each method
- Edge cases and error conditions
- Integration tests for workflows
- Performance tests (markers)

---

## Testing Best Practices Exercises

### Exercise A: Test-Driven Development (TDD)

**Practice TDD approach:**
1. Write test first (it fails)
2. Write minimal code to pass
3. Refactor
4. Repeat

**Implement FizzBuzz using TDD:**
- Write test for 1 → "1"
- Write test for 3 → "Fizz"
- Write test for 5 → "Buzz"
- Write test for 15 → "FizzBuzz"
- Write test for range(1, 101)

---

### Exercise B: Testing Edge Cases

**Create tests for edge cases:**
1. Empty inputs
2. None values
3. Very large numbers
4. Special characters
5. Unicode strings
6. Concurrent operations

**Example function to test:**
```python
def process_list(items):
    # What edge cases exist?
    # Empty list?
    # None values in list?
    # Large list?
    # Duplicate items?
    pass
```

---

### Exercise C: Refactoring with Tests

**Given working code with tests:**
1. Run tests to verify they pass
2. Refactor code for better structure
3. Ensure tests still pass
4. Add new tests for edge cases
5. Refactor again with confidence

---

## Challenge Problems

### Challenge 1: Property-Based Testing

Use `hypothesis` library for property-based testing:
```python
from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_addition_commutative(a, b):
    assert a + b == b + a
```

**Tasks:**
1. Install hypothesis
2. Write property-based tests
3. Test invariants
4. Let hypothesis find edge cases

---

### Challenge 2: Test Performance

**Create performance benchmarks:**
1. Use pytest-benchmark
2. Measure function execution time
3. Compare different implementations
4. Set performance thresholds

---

### Challenge 3: Mutation Testing

**Use mutation testing (pytest-mutpy):**
1. Generate code mutations
2. Run tests against mutations
3. Find inadequate tests
4. Improve test suite

---

## Hints

1. **Start Simple**: Begin with basic assertions
2. **One Thing**: Test one thing per test
3. **Independence**: Tests shouldn't depend on each other
4. **Clear Names**: Use descriptive test names
5. **AAA Pattern**: Arrange, Act, Assert
6. **Coverage Goal**: Aim for 80-90%, not 100% at all costs
7. **Fast Tests**: Keep unit tests fast
8. **Mock External**: Mock APIs, databases, file I/O
9. **Document**: Comment complex test setups
10. **Refactor**: Keep tests clean and maintainable

---

## Progression Path

1. **Exercises 1-3**: Basic testing fundamentals
2. **Exercises 4-6**: Fixtures and test organization
3. **Exercises 7-8**: Parametrization techniques
4. **Exercises 9-10**: Mocking and isolation
5. **Exercises 11-13**: Advanced patterns
6. **Exercises 14-15**: Integration testing
7. **Challenges**: Advanced topics

Complete exercises in order for best learning experience.
