# Testing - Theory

## Core Concepts

### 1. Why Test?

**Benefits**:
- Catch bugs early
- Document code behavior
- Enable refactoring safely
- Improve code design
- Build confidence

**Types of Tests**:
- **Unit tests**: Test individual functions/classes
- **Integration tests**: Test component interactions
- **End-to-end tests**: Test entire application flow
- **Regression tests**: Ensure bugs don't return

### 2. Test Frameworks

**unittest** (built-in):
- Standard library
- Class-based tests
- xUnit style
- More verbose

**pytest** (third-party):
- Simple assert statements
- Fixtures
- Powerful features
- Community favorite

**doctest** (built-in):
- Tests in docstrings
- Documentation + tests
- Good for examples

### 3. Test Structure (AAA Pattern)

```python
def test_example():
    # Arrange: Setup test data
    calculator = Calculator()

    # Act: Perform operation
    result = calculator.add(2, 3)

    # Assert: Verify result
    assert result == 5
```

### 4. Assertions

**unittest assertions**:
- assertEqual(a, b)
- assertTrue(x)
- assertFalse(x)
- assertRaises(Exception)
- assertIn(a, b)
- assertIsNone(x)

**pytest assertions**:
- Simple: `assert x == y`
- Context: `with pytest.raises(ValueError)`
- Approximation: `assert x == pytest.approx(3.14)`

### 5. Fixtures

**Purpose**: Setup/teardown test resources

**unittest** (setUp/tearDown):
```python
class TestExample(unittest.TestCase):
    def setUp(self):
        self.resource = create_resource()

    def tearDown(self):
        self.resource.cleanup()
```

**pytest** (@pytest.fixture):
```python
@pytest.fixture
def resource():
    r = create_resource()
    yield r
    r.cleanup()
```

### 6. Mocking

**Purpose**: Replace dependencies with test doubles

**Types**:
- **Mock**: Fake object that tracks calls
- **Patch**: Temporarily replace real object
- **MagicMock**: Mock with magic methods
- **Spy**: Partial mock (real object + tracking)

**When to Mock**:
- External services (API, database)
- Slow operations
- Non-deterministic behavior (random, time)
- Difficult to test scenarios (errors)

### 7. Test Coverage

**What is it?**:
- Percentage of code executed by tests
- Line coverage, branch coverage

**Tools**:
- coverage.py: `pip install coverage`
- pytest-cov: `pip install pytest-cov`

**Goal**: High coverage (>80%), but 100% isn't always needed

### 8. Test-Driven Development (TDD)

**Process**:
1. **Red**: Write failing test
2. **Green**: Write minimal code to pass
3. **Refactor**: Improve code while keeping tests green

**Benefits**:
- Better design
- Testable code
- Living documentation

## Best Practices

1. **Test one thing**: Each test should verify one behavior
2. **Independent tests**: Tests shouldn't depend on each other
3. **Fast tests**: Keep unit tests fast (< 1s)
4. **Descriptive names**: test_should_return_empty_list_when_input_is_empty
5. **Arrange-Act-Assert**: Clear structure
6. **Don't test implementation**: Test behavior, not internals
7. **Use fixtures**: Share setup code
8. **Mock external dependencies**: Keep tests isolated
9. **Test edge cases**: Empty, null, boundary values
10. **Keep tests simple**: Tests shouldn't need tests

## Common Patterns

### Test Class Organization
```python
class TestCalculator:
    def test_add_positive_numbers(self):
        pass

    def test_add_negative_numbers(self):
        pass

    def test_divide_by_zero_raises_error(self):
        pass
```

### Parameterized Tests
```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

### Testing Exceptions
```python
# unittest
with self.assertRaises(ValueError):
    divide(10, 0)

# pytest
with pytest.raises(ValueError):
    divide(10, 0)
```
