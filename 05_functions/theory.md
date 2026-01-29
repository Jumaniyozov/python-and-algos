# Functions: Theory and Concepts

## 5.1 Function Definition and Calling

### Basic Function

```python
def greet(name):
    """Greet someone by name."""
    return f"Hello, {name}!"

# Calling
message = greet("Alice")  # "Hello, Alice!"
```

**Components**:
- `def` - keyword to define function
- `greet` - function name
- `(name)` - parameters
- `"""docstring"""` - documentation
- `return` - return value

### Function Without Return

```python
def print_greeting(name):
    """Print greeting (returns None)."""
    print(f"Hello, {name}!")

result = print_greeting("Bob")  # None
```

Functions without explicit `return` return `None`.

### Multiple Return Values

```python
def get_user():
    """Return multiple values as tuple."""
    return "Alice", 30, "NYC"

name, age, city = get_user()  # Tuple unpacking
```

### Docstrings

```python
def calculate_area(length, width):
    """
    Calculate area of rectangle.

    Args:
        length (float): Length of rectangle
        width (float): Width of rectangle

    Returns:
        float: Area of rectangle

    Examples:
        >>> calculate_area(5, 3)
        15.0
    """
    return length * width
```

---

## 5.2 Arguments (positional, keyword, *args, **kwargs)

### Positional Arguments

```python
def greet(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

greet("Alice", "Smith")  # Order matters
```

### Keyword Arguments

```python
greet(last_name="Smith", first_name="Alice")  # Order doesn't matter
```

### Default Parameters

```python
def power(base, exponent=2):
    """Raise base to exponent (default: 2)."""
    return base ** exponent

power(5)      # 25 (uses default exponent=2)
power(5, 3)   # 125 (overrides default)
```

### Positional-Only Parameters (Python 3.8+)

```python
def func(a, b, /, c, d):
    """
    a, b - positional-only (before /)
    c, d - positional or keyword
    """
    pass

func(1, 2, 3, 4)         # OK
func(1, 2, c=3, d=4)     # OK
func(a=1, b=2, c=3, d=4) # Error! a, b must be positional
```

### Keyword-Only Parameters

```python
def func(a, b, *, c, d):
    """
    a, b - positional or keyword
    c, d - keyword-only (after *)
    """
    pass

func(1, 2, c=3, d=4)  # OK
func(1, 2, 3, 4)      # Error! c, d must be keyword
```

### *args (Variable Positional Arguments)

```python
def sum_all(*args):
    """Sum any number of arguments."""
    return sum(args)

sum_all(1, 2, 3)        # 6
sum_all(1, 2, 3, 4, 5)  # 15

# args is a tuple
def print_args(*args):
    print(type(args))  # <class 'tuple'>
    for arg in args:
        print(arg)
```

### **kwargs (Variable Keyword Arguments)

```python
def print_info(**kwargs):
    """Accept any keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
# name: Alice
# age: 30
# city: NYC

# kwargs is a dict
```

### Combining All Parameter Types

**Order must be**: positional-only, positional/keyword, *args, keyword-only, **kwargs

```python
def func(pos_only, /, standard, *args, kw_only, **kwargs):
    """Demonstrate all parameter types."""
    print(f"pos_only: {pos_only}")
    print(f"standard: {standard}")
    print(f"args: {args}")
    print(f"kw_only: {kw_only}")
    print(f"kwargs: {kwargs}")

func(1, 2, 3, 4, kw_only=5, extra1=6, extra2=7)
# pos_only: 1
# standard: 2
# args: (3, 4)
# kw_only: 5
# kwargs: {'extra1': 6, 'extra2': 7}
```

### Unpacking Arguments

```python
def func(a, b, c):
    return a + b + c

# Unpack list/tuple
args = [1, 2, 3]
func(*args)  # Same as func(1, 2, 3)

# Unpack dict
kwargs = {"a": 1, "b": 2, "c": 3}
func(**kwargs)  # Same as func(a=1, b=2, c=3)
```

---

## 5.3 Lambda Functions and Functional Programming

### Lambda Syntax

**Syntax**: `lambda arguments: expression`

```python
# Regular function
def square(x):
    return x ** 2

# Lambda (anonymous function)
square = lambda x: x ** 2

square(5)  # 25
```

### Common Uses

**Sorting**:
```python
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

# Sort by score
students.sort(key=lambda x: x[1])
# [('Charlie', 78), ('Alice', 85), ('Bob', 92)]
```

**Map, Filter, Reduce**:
```python
# map: apply function to each item
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# filter: keep items where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# reduce: accumulate values
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
# 120 (1 * 2 * 3 * 4 * 5)
```

### Lambda Limitations

- Only single expression
- No statements (no `if/else` statements, only expressions)
- No annotations
- Less readable for complex logic

```python
# Good use
small_func = lambda x: x * 2

# Bad use (use def instead)
complex_func = lambda x: x * 2 if x > 0 else x / 2 if x < 0 else 0
```

---

## 5.4 Decorators and Functools

### What is a Decorator?

A decorator wraps a function to modify its behavior.

```python
def my_decorator(func):
    """Decorator that adds behavior."""
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Before function
# Hello!
# After function
```

### Decorators with Arguments

```python
def repeat(times):
    """Decorator factory - returns decorator."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

### Preserving Function Metadata

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves func's metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### Common Decorators

**Timer**:
```python
import time
from functools import wraps

def timer(func):
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
```

**Memoization (Cache)**:
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Much faster with caching!
```

**functools.cache (Python 3.9+)**:
```python
from functools import cache

@cache  # Unlimited cache
def expensive_computation(n):
    return n ** 2
```

### Class Method Decorators

```python
class MyClass:
    @staticmethod
    def static_method():
        """No self/cls parameter."""
        return "Static"

    @classmethod
    def class_method(cls):
        """Receives class as first parameter."""
        return f"Class: {cls.__name__}"

    @property
    def computed_value(self):
        """Access like attribute, not method."""
        return self._value * 2
```

---

## 5.5 Closures and Nonlocal

### What is a Closure?

A closure is a function that remembers values from its enclosing scope.

```python
def outer(x):
    """Outer function."""
    def inner(y):
        """Inner function - closure."""
        return x + y  # Accesses x from outer scope
    return inner

add_5 = outer(5)
add_5(3)  # 8 (remembers x=5)
add_5(10)  # 15
```

### nonlocal Keyword

Modify variables from enclosing scope:

```python
def counter():
    """Create a counter function."""
    count = 0

    def increment():
        nonlocal count  # Modify outer scope variable
        count += 1
        return count

    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

**Without nonlocal** (error):
```python
def counter():
    count = 0
    def increment():
        count += 1  # UnboundLocalError!
        return count
    return increment
```

### Closure Example: Function Factory

```python
def make_multiplier(factor):
    """Create a multiplier function."""
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

double(5)  # 10
triple(5)  # 15
```

---

## 5.6 Generators and Yield

### What is a Generator?

A generator is a function that yields values one at a time, pausing between each.

```python
def count_up_to(n):
    """Generator that counts from 0 to n."""
    i = 0
    while i < n:
        yield i
        i += 1

# Use in for loop
for num in count_up_to(5):
    print(num)  # 0, 1, 2, 3, 4

# Or create iterator
counter = count_up_to(3)
next(counter)  # 0
next(counter)  # 1
next(counter)  # 2
next(counter)  # StopIteration
```

### Why Use Generators?

**Memory efficient**: Don't create entire sequence in memory

```python
# List - creates all values in memory
def squares_list(n):
    return [x**2 for x in range(n)]

# Generator - creates values on demand
def squares_gen(n):
    for x in range(n):
        yield x**2

# Memory comparison
import sys
list_size = sys.getsizeof(squares_list(10000))
gen_size = sys.getsizeof(squares_gen(10000))
# gen_size is much smaller!
```

### Generator Expressions

Like list comprehensions but with parentheses:

```python
# List comprehension
squares_list = [x**2 for x in range(10)]

# Generator expression
squares_gen = (x**2 for x in range(10))

# Use in sum, max, etc.
total = sum(x**2 for x in range(1000000))  # Memory efficient
```

### yield from (Python 3.3+)

Delegate to another generator:

```python
def generator1():
    yield 1
    yield 2

def generator2():
    yield 3
    yield 4

def combined():
    yield from generator1()
    yield from generator2()

list(combined())  # [1, 2, 3, 4]
```

### Generator Methods

```python
def echo():
    """Generator with send/throw/close."""
    value = None
    while True:
        value = yield value

gen = echo()
next(gen)       # Initialize
gen.send(10)    # Send value: 10
gen.throw(ValueError)  # Raise exception in generator
gen.close()     # Stop generator
```

---

## 5.7 Async Functions and Coroutines

### What is an Async Function?

Async functions allow concurrent execution without blocking.

```python
import asyncio

async def fetch_data():
    """Async function (coroutine)."""
    await asyncio.sleep(1)  # Non-blocking sleep
    return "Data"

# Run async function
asyncio.run(fetch_data())
```

### await Keyword

`await` pauses execution until awaitable completes:

```python
async def main():
    print("Start")
    result = await fetch_data()  # Wait for completion
    print(f"Got: {result}")
    print("End")

asyncio.run(main())
# Start
# (1 second pause)
# Got: Data
# End
```

### Running Multiple Coroutines

```python
async def task1():
    await asyncio.sleep(1)
    return "Task 1"

async def task2():
    await asyncio.sleep(1)
    return "Task 2"

async def main():
    # Sequential (2 seconds total)
    result1 = await task1()
    result2 = await task2()

    # Concurrent (1 second total)
    results = await asyncio.gather(task1(), task2())
    # ['Task 1', 'Task 2']

asyncio.run(main())
```

### Async Context Managers

```python
class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource")
        await asyncio.sleep(0.1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        await asyncio.sleep(0.1)

async def main():
    async with AsyncResource() as resource:
        print("Using resource")

asyncio.run(main())
```

### Async Generators

```python
async def async_range(n):
    """Async generator."""
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def main():
    async for num in async_range(5):
        print(num)

asyncio.run(main())
```

---

## Key Concepts Summary

1. **Functions**: Reusable blocks of code
2. **Parameters**: Positional, keyword, default, *args, **kwargs
3. **Lambdas**: Anonymous single-expression functions
4. **Decorators**: Wrap functions to add behavior
5. **Closures**: Functions that remember enclosing scope
6. **Generators**: Yield values one at a time (memory efficient)
7. **Async**: Non-blocking concurrent execution
8. **Type hints**: Document expected types
9. **Docstrings**: Document what function does

---

## Best Practices

1. **Use descriptive names**: `calculate_total` not `calc`
2. **Keep functions small**: Do one thing well
3. **Use type hints**: Improve readability and tooling
4. **Write docstrings**: Explain purpose, args, returns
5. **Avoid side effects**: Pure functions are easier to test
6. **Use generators**: For large sequences
7. **Prefer async**: For I/O-bound operations
8. **Don't overuse lambdas**: Use `def` for complex logic
9. **Cache expensive functions**: Use `@lru_cache`
10. **Use keyword arguments**: For clarity

---

## Next Steps

1. Practice writing functions with various parameter types
2. Create decorators for common patterns
3. Use generators for memory-efficient iteration
4. Learn async/await for concurrent programming
5. Move on to examples.md for practical code
