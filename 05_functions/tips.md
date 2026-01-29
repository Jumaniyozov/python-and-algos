# Functions: Tips, Tricks, and Gotchas

## Function Definition Tips

### Tip 1: Use Type Hints

**Good**:
```python
def add(a: int, b: int) -> int:
    return a + b
```

**Better** (Python 3.14):
```python
def add[T: (int, float)](a: T, b: T) -> T:
    return a + b
```

### Tip 2: Write Docstrings

```python
def calculate_discount(price: float, percent: float) -> float:
    """
    Calculate discounted price.

    Args:
        price: Original price
        percent: Discount percentage (0-100)

    Returns:
        Discounted price

    Raises:
        ValueError: If percent not in 0-100
    """
    if not 0 <= percent <= 100:
        raise ValueError("Percent must be 0-100")
    return price * (1 - percent / 100)
```

### Gotcha 1: Mutable Default Arguments

**Dangerous**:
```python
def add_item(item, items=[]):  # Bad!
    items.append(item)
    return items

add_item(1)  # [1]
add_item(2)  # [1, 2] - Unexpected!
```

**Safe**:
```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Gotcha 2: Late Binding in Closures

**Unexpected**:
```python
functions = []
for i in range(3):
    functions.append(lambda: i)

[f() for f in functions]  # [2, 2, 2] - All return 2!
```

**Fixed**:
```python
functions = []
for i in range(3):
    functions.append(lambda i=i: i)  # Capture i now

[f() for f in functions]  # [0, 1, 2] - Correct!
```

## Parameter Tips

### Tip 1: Use Keyword-Only for Clarity

```python
# Confusing
def create_user(name, email, True, False):  # What are these?
    pass

# Clear
def create_user(name, email, *, active=True, admin=False):
    pass

create_user("Alice", "a@x.com", active=True, admin=False)
```

### Tip 2: Unpack with * and **

```python
def func(a, b, c):
    return a + b + c

args = [1, 2, 3]
func(*args)  # Same as func(1, 2, 3)

kwargs = {"a": 1, "b": 2, "c": 3}
func(**kwargs)  # Same as func(a=1, b=2, c=3)
```

## Decorator Tips

### Tip 1: Use @wraps

**Always use `@wraps`** to preserve function metadata:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### Tip 2: Stack Decorators

```python
@decorator1
@decorator2
@decorator3
def func():
    pass

# Equivalent to:
# func = decorator1(decorator2(decorator3(func)))
```

### Gotcha: Decorator Order Matters

```python
@timer
@cache
def expensive_func():  # Caches, then times
    pass

@cache
@timer
def expensive_func():  # Times, then caches (different!)
    pass
```

## Generator Tips

### Tip 1: Use Generators for Large Data

**Memory efficient**:
```python
# Generator - one at a time
def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# List - all in memory
def read_large_file_bad(filename):
    with open(filename) as f:
        return [line.strip() for line in f]  # OOM for huge files
```

### Tip 2: Generator Expressions

```python
# Use generator expression for sum, any, all
total = sum(x**2 for x in range(1000000))  # Memory efficient

# Don't convert to list unnecessarily
has_even = any(x % 2 == 0 for x in huge_list)  # Stops early
```

### Gotcha: Generators Are One-Time Use

```python
gen = (x for x in range(5))
list(gen)  # [0, 1, 2, 3, 4]
list(gen)  # [] - Exhausted!

# Create new generator each time
def make_gen():
    return (x for x in range(5))
```

## Async Tips

### Tip 1: Use asyncio.gather for Concurrent Tasks

```python
# Sequential (slow)
result1 = await task1()
result2 = await task2()

# Concurrent (fast)
results = await asyncio.gather(task1(), task2())
```

### Tip 2: Don't Mix Blocking and Async

**Bad**:
```python
async def bad():
    time.sleep(1)  # Blocks event loop!
    return "done"
```

**Good**:
```python
async def good():
    await asyncio.sleep(1)  # Non-blocking
    return "done"
```

### Gotcha: Forgetting await

```python
async def fetch():
    return "data"

async def main():
    result = fetch()  # Returns coroutine, not "data"!
    result = await fetch()  # Correct - returns "data"
```

## Performance Tips

### Tip 1: Use Built-ins Over Lambdas

**Slower**:
```python
map(lambda x: x**2, numbers)
```

**Faster**:
```python
from operator import mul
from functools import partial
map(partial(pow, exp=2), numbers)
# Or just use list comprehension:
[x**2 for x in numbers]
```

### Tip 2: Cache Expensive Functions

```python
from functools import cache

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# First call: slow
# Subsequent calls: instant
```

## Best Practices

### Do:
- ✅ Use type hints for clarity
- ✅ Write docstrings
- ✅ Use `None` for mutable defaults
- ✅ Use `@wraps` in decorators
- ✅ Use generators for large data
- ✅ Use keyword-only parameters for clarity
- ✅ Keep functions small and focused
- ✅ Cache expensive computations

### Don't:
- ❌ Use mutable default arguments
- ❌ Make functions too long (>50 lines)
- ❌ Overuse lambdas (use `def` for complex logic)
- ❌ Forget `await` in async functions
- ❌ Mix blocking and async code
- ❌ Ignore function metadata (use `@wraps`)
- ❌ Create side effects unnecessarily

## Common Patterns

### Pattern 1: Validation

```python
def validate_input(data):
    """Validate and return cleaned data."""
    if not isinstance(data, str):
        raise TypeError("Expected string")
    if len(data) < 3:
        raise ValueError("Too short")
    return data.strip().lower()
```

### Pattern 2: Factory Functions

```python
def create_multiplier(factor):
    """Create a multiplier function."""
    def multiply(x):
        return x * factor
    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)
```

### Pattern 3: Callback Functions

```python
def process_items(items, callback):
    """Process items with callback."""
    return [callback(item) for item in items]

def uppercase(s):
    return s.upper()

process_items(["a", "b"], uppercase)  # ["A", "B"]
```

## Quick Reference

### Function Signature
```python
def func(
    pos_only, /,           # Positional-only
    standard,              # Positional or keyword
    *args,                 # Variable positional
    kw_only,               # Keyword-only
    **kwargs               # Variable keyword
) -> ReturnType:
    """Docstring."""
    pass
```

### Decorator Template
```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Before
        result = func(*args, **kwargs)
        # After
        return result
    return wrapper
```

### Generator Template
```python
def generator():
    """Yield values one at a time."""
    for item in items:
        yield process(item)
```

See examples.md for practical applications!
