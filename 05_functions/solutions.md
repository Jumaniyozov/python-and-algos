# Functions: Exercise Solutions

## Solution 1: Calculate Average

```python
def calculate_average(*numbers):
    """Calculate average of any number of arguments."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Tests
print(calculate_average(1, 2, 3, 4, 5))  # 3.0
print(calculate_average())  # 0
```

## Solution 2: Create Profile

```python
def create_profile(name, age, *, city, country="USA", **interests):
    """Create user profile with flexible interests."""
    profile = {
        "name": name,
        "age": age,
        "city": city,
        "country": country,
        "interests": interests
    }
    return profile

# Test
profile = create_profile(
    "Alice", 30,
    city="NYC",
    hobby="photography",
    skill="Python"
)
print(profile)
```

## Solution 3: Lambda Sorting

```python
employees = [
    ("Alice", 30, 75000),
    ("Bob", 25, 65000),
    ("Charlie", 35, 85000)
]

# Sort by age (ascending)
by_age = sorted(employees, key=lambda x: x[1])

# Sort by salary (descending)
by_salary = sorted(employees, key=lambda x: x[2], reverse=True)

# Sort by name (alphabetically)
by_name = sorted(employees, key=lambda x: x[0])

print("By age:", by_age)
print("By salary:", by_salary)
print("By name:", by_name)
```

## Solution 4: Log Calls Decorator

```python
from functools import wraps

def log_calls(func):
    """Log function calls with arguments."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(str, args))
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"Calling {func.__name__}({all_args})")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")
greet("Bob", greeting="Hi")
```

## Solution 5: Timer Decorator

```python
import time
from functools import wraps

def timer(func):
    """Time function execution."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()
```

## Solution 6: Closure-Based Counter

```python
def make_counter(start=0):
    """Create counter with closure."""
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    def get_count():
        return count

    return increment, decrement, get_count

# Test
inc, dec, get = make_counter(10)
print(inc())   # 11
print(inc())   # 12
print(dec())   # 11
print(get())   # 11
```

## Solution 7: Prime Generator

```python
def primes():
    """Generate infinite sequence of primes."""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Get first 10 primes
import itertools
first_10 = list(itertools.islice(primes(), 10))
print(first_10)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

## Solution 8: Memoization Decorator

```python
from functools import wraps

def memoize(func):
    """Cache function results."""
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Fast with memoization
print(fibonacci(100))
```

## Solution 9: Retry Decorator

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    """Retry function on exception."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success"

unreliable_function()
```

## Solution 10: Async Data Fetcher

```python
import asyncio

async def fetch_url(url, delay):
    """Simulate async URL fetch."""
    print(f"Fetching {url}...")
    await asyncio.sleep(delay)
    return f"Data from {url}"

async def fetch_all(urls):
    """Fetch all URLs concurrently."""
    tasks = [fetch_url(url, 1) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

# Test
async def main():
    urls = ["api.com/1", "api.com/2", "api.com/3"]
    results = await fetch_all(urls)
    print(results)

asyncio.run(main())
```

## Solution 11: Function Composition

```python
def compose(*funcs):
    """Compose functions: compose(f, g, h)(x) = f(g(h(x)))."""
    def composed(arg):
        result = arg
        for func in reversed(funcs):
            result = func(result)
        return result
    return composed

# Test
def add_10(x):
    return x + 10

def multiply_2(x):
    return x * 2

def square(x):
    return x ** 2

# square(multiply_2(add_10(5))) = square(multiply_2(15)) = square(30) = 900
pipeline = compose(square, multiply_2, add_10)
print(pipeline(5))  # 900
```

## Solution 12: Partial Application

```python
from functools import partial

def greet(greeting, name, punctuation):
    """Flexible greeting function."""
    return f"{greeting}, {name}{punctuation}"

# Create specialized versions
hello = partial(greet, "Hello")
hi_enthusiastic = partial(greet, "Hi", punctuation="!")

print(hello("Alice", "."))  # Hello, Alice.
print(hi_enthusiastic("Bob"))  # Hi, Bob!
```

## Challenge 1: Decorator with Optional Arguments

```python
from functools import wraps

def debug(func=None, *, prefix="DEBUG"):
    """Decorator that can be used with or without arguments."""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Calling {f.__name__}")
            result = f(*args, **kwargs)
            print(f"{prefix}: {f.__name__} returned {result}")
            return result
        return wrapper

    if func is None:
        # Called with arguments: @debug(prefix="INFO")
        return decorator
    else:
        # Called without arguments: @debug
        return decorator(func)

# Both work
@debug
def add(a, b):
    return a + b

@debug(prefix="INFO")
def multiply(a, b):
    return a * b

add(2, 3)
multiply(2, 3)
```

## Challenge 2: Context Manager Generator

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name="Code block"):
    """Time code execution using generator."""
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name} took {elapsed:.4f}s")

# Usage
with timer("Data processing"):
    time.sleep(0.5)
    total = sum(range(1000000))
```

## Challenge 3: Async Rate Limiter

```python
import asyncio
import time
from functools import wraps

def rate_limit(calls_per_second):
    """Limit async function to N calls per second."""
    min_interval = 1.0 / calls_per_second
    last_called = [0.0]

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < min_interval:
                await asyncio.sleep(min_interval - elapsed)
            last_called[0] = time.time()
            return await func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(calls_per_second=2)
async def api_call(n):
    print(f"API call {n} at {time.time():.2f}")
    return f"Result {n}"

async def main():
    # Will be rate-limited to 2 calls/second
    tasks = [api_call(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
```

Excellent work! Check examples.md for more patterns.
