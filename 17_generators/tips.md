# Tips & Best Practices: Generators & Iterators

## Core Best Practices

### Tip 1: Always Use Generator Expressions Over List Comprehensions for Large Data

```python
# BAD: Creates entire list in memory
total = sum([x**2 for x in range(10000000)])

# GOOD: Generator expression - memory efficient
total = sum(x**2 for x in range(10000000))

# The difference:
import sys
list_comp = [x for x in range(1000)]
gen_exp = (x for x in range(1000))

print(sys.getsizeof(list_comp))  # ~9KB
print(sys.getsizeof(gen_exp))    # ~200 bytes
```

### Tip 2: Prime Generators Before Using send()

```python
# BAD: Will raise TypeError
def my_gen():
    while True:
        x = yield
        print(x)

gen = my_gen()
gen.send(42)  # TypeError: can't send non-None value to a just-started generator

# GOOD: Prime first
gen = my_gen()
next(gen)  # or gen.send(None)
gen.send(42)  # Works!
```

### Tip 3: Use yield from for Delegation

```python
# BAD: Manual iteration
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            for sub_item in flatten(item):  # Verbose
                yield sub_item
        else:
            yield item

# GOOD: Use yield from
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)  # Clean and efficient
        else:
            yield item
```

### Tip 4: Generators Are Single-Use

```python
# Gotcha: Generator exhaustion
gen = (x**2 for x in range(5))

print(list(gen))  # [0, 1, 4, 9, 16]
print(list(gen))  # [] - Exhausted!

# Solution 1: Create new generator
def get_squares():
    return (x**2 for x in range(5))

print(list(get_squares()))
print(list(get_squares()))

# Solution 2: Use itertools.tee for multiple iterators
from itertools import tee

gen = (x**2 for x in range(5))
gen1, gen2 = tee(gen, 2)

print(list(gen1))
print(list(gen2))
```

### Tip 5: close() Triggers finally Blocks

```python
def resource_manager():
    """Generator with cleanup"""
    try:
        resource = acquire_resource()
        while True:
            data = yield
            process(resource, data)
    finally:
        # This WILL run when close() is called
        release_resource(resource)
        print("Cleanup complete")

gen = resource_manager()
next(gen)
gen.send("data")
gen.close()  # Triggers finally block
```

## Performance Tips

### Tip 6: Generator Expressions for Chaining

```python
# Efficient chaining - each step is lazy
lines = (line for line in open('file.txt'))
stripped = (line.strip() for line in lines)
non_empty = (line for line in stripped if line)
uppercase = (line.upper() for line in non_empty)

# Only processes one line at a time through entire chain
for line in uppercase:
    print(line)
```

### Tip 7: Use islice() Instead of Slicing

```python
from itertools import islice

# BAD: Converts to list first
gen = (x**2 for x in range(10000))
first_ten = list(gen)[:10]  # Computes all 10000!

# GOOD: Use islice
gen = (x**2 for x in range(10000))
first_ten = list(islice(gen, 10))  # Only computes 10
```

### Tip 8: Generators Have Lower Overhead Than Classes

```python
import time

# Class-based iterator
class Counter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i

# Generator function
def counter(n):
    for i in range(1, n + 1):
        yield i

# Generator is simpler and often faster for simple iteration
```

### Tip 9: Cache Results When Needed

```python
# If you need to iterate multiple times
data = expensive_generator()

# Option 1: Convert to list (if memory allows)
cached = list(data)

# Option 2: Use itertools.tee for multiple passes
from itertools import tee
iter1, iter2 = tee(data, 2)

# Option 3: Generator function that recreates
def get_data():
    return expensive_generator()

for item in get_data():  # First pass
    process(item)

for item in get_data():  # Second pass
    analyze(item)
```

## Common Pitfalls

### Pitfall 1: Forgetting Generators Are Lazy

```python
# Pitfall: Nothing happens!
gen = (print(x) for x in range(5))  # No output

# Fix: Consume the generator
list(gen)  # Now prints 0, 1, 2, 3, 4

# Or iterate
for _ in (print(x) for x in range(5)):
    pass
```

### Pitfall 2: Modifying Iterated Collection

```python
# BAD: Dangerous with generators from mutable sources
items = [1, 2, 3, 4, 5]

def process_items():
    for item in items:
        yield item
        items.remove(item)  # Modifies during iteration!

# GOOD: Work with a copy or indices
def process_items_safe():
    for item in list(items):  # Copy first
        yield item
        items.remove(item)
```

### Pitfall 3: StopIteration in Python 3.7+

```python
# Python 3.6 and earlier: Okay
def old_gen():
    yield 1
    raise StopIteration  # This was okay

# Python 3.7+: Warning/Error
def new_gen():
    yield 1
    raise StopIteration  # RuntimeError: generator raised StopIteration

# CORRECT: Use return instead
def correct_gen():
    yield 1
    return  # Proper way to stop
```

### Pitfall 4: Generator Expression Scope

```python
# Gotcha: Late binding in generator expressions
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# But:
funcs = [lambda: x**2 for x in range(5)]
print([f() for f in funcs])  # [16, 16, 16, 16, 16] - Oops!

# Generator expressions bind immediately
gens = (x**2 for x in range(5))
# But lambda still has late binding issue

# Fix for lambdas:
funcs = [lambda x=x: x**2 for x in range(5)]
print([f() for f in funcs])  # [0, 1, 4, 9, 16] - Correct!
```

### Pitfall 5: Exceptions in Generators

```python
# Unhandled exceptions stop generator
def risky_gen():
    for i in range(10):
        if i == 5:
            raise ValueError("Oops")
        yield i

gen = risky_gen()
try:
    for item in gen:
        print(item)  # Prints 0-4, then exception
except ValueError:
    pass

# Generator is now closed
try:
    next(gen)
except StopIteration:
    print("Generator exhausted after exception")

# Handle exceptions inside generator if needed
def safe_gen():
    for i in range(10):
        try:
            if i == 5:
                raise ValueError("Oops")
            yield i
        except ValueError:
            continue  # Skip this value
```

## Real-World Patterns

### Pattern 1: File Processing Pipeline

```python
def read_file(filename):
    """Read file line by line"""
    with open(filename) as f:
        for line in f:
            yield line

def parse_csv(lines):
    """Parse CSV lines"""
    import csv
    reader = csv.reader(lines)
    for row in reader:
        yield row

def filter_rows(rows, column, value):
    """Filter rows by column value"""
    for row in rows:
        if row[column] == value:
            yield row

# Build pipeline
lines = read_file('data.csv')
rows = parse_csv(lines)
filtered = filter_rows(rows, 2, 'active')

# Process lazily
for row in filtered:
    process(row)
```

### Pattern 2: Infinite Sequences

```python
def fibonacci():
    """Infinite Fibonacci generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def take(n, iterable):
    """Take first n items"""
    from itertools import islice
    return islice(iterable, n)

# Use with infinite sequence
for fib in take(10, fibonacci()):
    print(fib)
```

### Pattern 3: Stateful Generators

```python
def running_stats():
    """Maintain running statistics"""
    count = 0
    total = 0
    min_val = float('inf')
    max_val = float('-inf')

    while True:
        value = yield {
            'count': count,
            'mean': total / count if count > 0 else 0,
            'min': min_val if count > 0 else None,
            'max': max_val if count > 0 else None
        }

        if value is not None:
            count += 1
            total += value
            min_val = min(min_val, value)
            max_val = max(max_val, value)

stats = running_stats()
next(stats)  # Prime

print(stats.send(10))
print(stats.send(20))
print(stats.send(5))
```

### Pattern 4: Context-Aware Generator

```python
from contextlib import contextmanager

@contextmanager
def database_cursor():
    """Generator as context manager"""
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

# Usage
with database_cursor() as cursor:
    cursor.execute("SELECT * FROM users")
    # Automatic cleanup and commit/rollback
```

## Debugging Tips

### Debug Tip 1: Add Logging to Generators

```python
def debug_gen(gen):
    """Wrapper that logs generator values"""
    for i, value in enumerate(gen):
        print(f"Debug: yielding {value} (item {i})")
        yield value

# Wrap any generator
data = debug_gen(range(5))
list(data)
```

### Debug Tip 2: Use send() for Inspection

```python
def inspectable_gen():
    """Generator that can report its state"""
    state = {'processed': 0}

    while True:
        command = yield state
        if command == 'stop':
            break
        elif command is not None:
            # Process command
            state['processed'] += 1

gen = inspectable_gen()
next(gen)
gen.send('data')
print(gen.send('inspect'))  # Check state
```

### Debug Tip 3: Test Generator Consumption

```python
def test_generator():
    """Test that generator produces expected values"""
    gen = my_generator()

    # Check first few values
    assert next(gen) == expected_1
    assert next(gen) == expected_2

    # Check length
    remaining = list(gen)
    assert len(remaining) == expected_count
```

## Advanced Techniques

### Technique 1: Generator Decorators

```python
from functools import wraps

def trace_generator(func):
    """Decorator that traces generator execution"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        print(f"Starting {func.__name__}")
        try:
            while True:
                value = next(gen)
                print(f"Yielded: {value}")
                yield value
        except StopIteration:
            print(f"Finished {func.__name__}")
    return wrapper

@trace_generator
def numbers():
    for i in range(3):
        yield i
```

### Technique 2: Bidirectional Generators

```python
def echo_generator():
    """Bidirectional communication"""
    received_count = 0

    while True:
        received = yield received_count
        if received == 'stop':
            break
        received_count += 1
        print(f"Received: {received}")

gen = echo_generator()
print(next(gen))      # 0
print(gen.send('a'))  # Received: a, yields 1
print(gen.send('b'))  # Received: b, yields 2
gen.send('stop')      # Stops generator
```

### Technique 3: Generator Composition

```python
def compose(*generators):
    """Compose multiple generators"""
    def composed(iterable):
        for gen in generators:
            iterable = gen(iterable)
        return iterable
    return composed

# Individual generators
def double(iterable):
    for item in iterable:
        yield item * 2

def add_one(iterable):
    for item in iterable:
        yield item + 1

# Compose them
pipeline = compose(double, add_one)
result = pipeline(range(5))
print(list(result))  # [1, 3, 5, 7, 9]
```

## Key Takeaways

1. **Generators are lazy**: Values computed only when needed
2. **Memory efficient**: Process one item at a time
3. **Single-use**: Generators exhaust after iteration
4. **Prime before send()**: Always call `next()` or `send(None)` first
5. **Use yield from**: For delegating to subgenerators
6. **Generator expressions**: Prefer over list comprehensions for large data
7. **Cleanup with finally**: Always triggers on close() or exception
8. **Cannot slice**: Use `itertools.islice()` instead
9. **No len()**: Generators don't know their length
10. **Excellent for pipelines**: Chain operations efficiently

## When to Use Generators

**Use generators when:**
- Processing large files or datasets
- Memory is constrained
- You need lazy evaluation
- Building data pipelines
- Working with infinite sequences
- Processing streaming data

**Don't use generators when:**
- You need random access (use list)
- You need the length upfront
- You need to iterate multiple times (convert to list or use `tee`)
- The data fits comfortably in memory and you need speed

## Performance Checklist

- [ ] Using generator expressions instead of list comprehensions
- [ ] Chaining generators instead of creating intermediate lists
- [ ] Using `islice()` instead of slicing
- [ ] Avoiding unnecessary conversions to list
- [ ] Processing data in chunks/batches
- [ ] Using `yield from` for delegation
- [ ] Considering memory vs. speed tradeoffs

Generators are one of Python's most powerful features. Master them to write efficient, elegant, and memory-conscious code.
