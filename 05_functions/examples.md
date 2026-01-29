# Functions: Code Examples

## Example 1: Function Parameters

```python
def create_user(username, email, age=None, *, active=True, **metadata):
    """Demonstrate various parameter types."""
    user = {
        "username": username,
        "email": email,
        "age": age,
        "active": active,
        "metadata": metadata
    }
    return user

# Usage
user1 = create_user("alice", "alice@example.com")
user2 = create_user("bob", "bob@example.com", 30, active=False, role="admin")
print(user1)
print(user2)
```

## Example 2: Decorator Pattern

```python
from functools import wraps
import time

def timing_decorator(func):
    """Measure function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timing_decorator
def fibonacci(n):
    """Calculate nth Fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
```

## Example 3: Closures

```python
def make_counter(start=0, step=1):
    """Create a counter with configurable start and step."""
    count = start

    def increment():
        nonlocal count
        count += step
        return count

    def decrement():
        nonlocal count
        count -= step
        return count

    def reset():
        nonlocal count
        count = start

    def get_value():
        return count

    return increment, decrement, reset, get_value

# Usage
inc, dec, reset, get = make_counter(start=10, step=5)
print(inc())   # 15
print(inc())   # 20
print(dec())   # 15
print(get())   # 15
reset()
print(get())   # 10
```

## Example 4: Generator for Large Datasets

```python
def read_large_file(filename):
    """Generator to read file line by line."""
    with open(filename) as f:
        for line in f:
            yield line.strip()

def process_numbers(limit):
    """Generate squares without storing all in memory."""
    for i in range(limit):
        yield i ** 2

# Use generators
for square in process_numbers(10):
    print(square)

# Generator expression
sum_of_squares = sum(x**2 for x in range(1000000))
print(f"Sum: {sum_of_squares}")
```

## Example 5: Async Functions

```python
import asyncio

async def fetch_data(url, delay):
    """Simulate async data fetching."""
    print(f"Fetching {url}...")
    await asyncio.sleep(delay)
    return f"Data from {url}"

async def main():
    """Run multiple async tasks concurrently."""
    # Sequential (slow)
    # result1 = await fetch_data("api.com/1", 2)
    # result2 = await fetch_data("api.com/2", 2)  # Total: 4 seconds

    # Concurrent (fast)
    results = await asyncio.gather(
        fetch_data("api.com/1", 2),
        fetch_data("api.com/2", 2),
        fetch_data("api.com/3", 2)
    )  # Total: 2 seconds
    print(results)

# Run
asyncio.run(main())
```

## Example 6: Function Composition

```python
def compose(*functions):
    """Compose multiple functions."""
    def inner(arg):
        result = arg
        for func in reversed(functions):
            result = func(result)
        return result
    return inner

# Helper functions
def add_10(x):
    return x + 10

def multiply_2(x):
    return x * 2

def square(x):
    return x ** 2

# Compose: square(multiply_2(add_10(x)))
pipeline = compose(square, multiply_2, add_10)
print(pipeline(5))  # ((5 + 10) * 2) ** 2 = 900
```

## Example 7: Memoization

```python
from functools import lru_cache, cache

# Manual memoization
def memoize(func):
    """Manual memoization decorator."""
    cache_dict = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)
        return cache_dict[args]
    return wrapper

@memoize
def fibonacci_manual(n):
    if n < 2:
        return n
    return fibonacci_manual(n-1) + fibonacci_manual(n-2)

# Using lru_cache
@lru_cache(maxsize=128)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)

# Using cache (Python 3.9+, unlimited)
@cache
def fibonacci_cache(n):
    if n < 2:
        return n
    return fibonacci_cache(n-1) + fibonacci_cache(n-2)

# Performance comparison
import time

for fib_func in [fibonacci_manual, fibonacci_lru, fibonacci_cache]:
    start = time.time()
    result = fib_func(35)
    print(f"{fib_func.__name__}: {time.time() - start:.4f}s")
```

## Example 8: Partial Functions

```python
from functools import partial

def power(base, exponent):
    """Calculate base^exponent."""
    return base ** exponent

# Create specialized functions
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))    # 125

# Practical use: callback with fixed parameters
def process_data(data, multiplier, offset):
    return [x * multiplier + offset for x in data]

# Create specialized processor
double_plus_10 = partial(process_data, multiplier=2, offset=10)
result = double_plus_10([1, 2, 3])  # [12, 14, 16]
```

## Example 9: Decorator with Arguments

```python
def retry(max_attempts=3, delay=1):
    """Retry decorator with configurable attempts and delay."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_api_call():
    """Simulate unreliable API."""
    import random
    if random.random() < 0.7:
        raise ConnectionError("API unavailable")
    return "Success"
```

## Example 10: Real-World Function Patterns

```python
def validate_and_process(data, validators, processors):
    """
    Validate data with multiple validators,
    then process with multiple processors.
    """
    # Validation phase
    for validator in validators:
        if not validator(data):
            raise ValueError(f"Validation failed: {validator.__name__}")

    # Processing phase
    result = data
    for processor in processors:
        result = processor(result)

    return result

# Validators
def is_not_empty(data):
    return bool(data)

def is_string(data):
    return isinstance(data, str)

def min_length_5(data):
    return len(data) >= 5

# Processors
def uppercase(data):
    return data.upper()

def add_prefix(data):
    return f"PREFIX_{data}"

# Usage
try:
    result = validate_and_process(
        "hello",
        validators=[is_not_empty, is_string, min_length_5],
        processors=[uppercase, add_prefix]
    )
    print(result)  # PREFIX_HELLO
except ValueError as e:
    print(f"Error: {e}")
```

See solutions.md for more practical examples!
