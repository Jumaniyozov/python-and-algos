# Theory: Generators & Iterators

## 1. The Iterator Protocol

### Understanding Iterators

An iterator is an object that implements two methods:
- `__iter__()`: Returns the iterator object itself
- `__next__()`: Returns the next item or raises `StopIteration`

```python
class CountUp:
    """Simple iterator that counts from start to stop"""

    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Usage
counter = CountUp(1, 5)
for num in counter:
    print(num)  # 1, 2, 3, 4
```

### Iterable vs Iterator

- **Iterable**: Object that can return an iterator (has `__iter__`)
- **Iterator**: Object that produces values (has `__iter__` and `__next__`)

```python
# List is iterable but not an iterator
my_list = [1, 2, 3]
print(hasattr(my_list, '__iter__'))  # True
print(hasattr(my_list, '__next__'))  # False

# Get an iterator from an iterable
iterator = iter(my_list)
print(hasattr(iterator, '__next__'))  # True

# Manually iterate
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# next(iterator)  # Raises StopIteration
```

### Why Iterators Matter

1. **Memory Efficiency**: Process one item at a time
2. **Lazy Evaluation**: Compute values only when needed
3. **Infinite Sequences**: Can represent infinite series
4. **Uniform Interface**: Work with any iterable the same way

## 2. Generator Functions

### What Are Generators?

Generators are functions that use `yield` instead of `return`. They automatically implement the iterator protocol and maintain state between calls.

```python
def simple_generator():
    """Generator that yields three values"""
    print("Starting")
    yield 1
    print("Between yields")
    yield 2
    print("Ending")
    yield 3

# Create generator object
gen = simple_generator()
print(type(gen))  # <class 'generator'>

# Iterate through values
for value in gen:
    print(f"Got: {value}")

# Output:
# Starting
# Got: 1
# Between yields
# Got: 2
# Ending
# Got: 3
```

### Generator State Preservation

Generators preserve local variables between yields:

```python
def counter(start=0):
    """Generator that counts upward"""
    count = start
    while True:
        yield count
        count += 1

gen = counter(10)
print(next(gen))  # 10
print(next(gen))  # 11
print(next(gen))  # 12
```

### Generator vs Regular Function

```python
# Regular function - computes all at once
def get_squares_list(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Generator - computes one at a time
def get_squares_gen(n):
    for i in range(n):
        yield i ** 2

# Memory comparison
import sys

list_squares = get_squares_list(10000)
print(f"List size: {sys.getsizeof(list_squares)} bytes")

gen_squares = get_squares_gen(10000)
print(f"Generator size: {sys.getsizeof(gen_squares)} bytes")

# List size: ~80KB
# Generator size: ~200 bytes
```

## 3. Generator Expressions

Generator expressions are like list comprehensions but with parentheses:

```python
# List comprehension - creates entire list in memory
squares_list = [x**2 for x in range(1000000)]

# Generator expression - creates values on demand
squares_gen = (x**2 for x in range(1000000))

# Generator expressions are composable
even_squares = (x for x in squares_gen if x % 2 == 0)
```

### When to Use Generator Expressions

```python
# GOOD: Summing large sequence
total = sum(x**2 for x in range(1000000))

# BAD: Creating list just to sum
total = sum([x**2 for x in range(1000000)])

# GOOD: Processing file line by line
lines = (line.strip() for line in open('file.txt'))
uppercase_lines = (line.upper() for line in lines)

# GOOD: Finding first match (stops early)
first_match = next((x for x in range(1000000) if x > 500000))
```

## 4. Generator Methods

Generators have three methods for advanced control:

### 4.1 send() - Sending Values into Generator

```python
def echo_generator():
    """Generator that can receive values"""
    while True:
        received = yield
        if received is not None:
            print(f"Received: {received}")

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")  # Received: Hello
gen.send("World")  # Received: World
```

**Two-way communication:**

```python
def accumulator():
    """Generator that accumulates sent values"""
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

acc = accumulator()
print(next(acc))      # 0
print(acc.send(10))   # 10
print(acc.send(5))    # 15
print(acc.send(3))    # 18
```

### 4.2 throw() - Injecting Exceptions

```python
def resilient_generator():
    """Generator that handles exceptions"""
    try:
        while True:
            value = yield
            print(f"Processing: {value}")
    except ValueError as e:
        print(f"Caught: {e}")
        yield "Error handled"
    finally:
        print("Cleanup")

gen = resilient_generator()
next(gen)
gen.send(42)  # Processing: 42
result = gen.throw(ValueError, "Invalid value")
print(result)  # Error handled
```

### 4.3 close() - Stopping Generator

```python
def cleanup_generator():
    """Generator with cleanup logic"""
    try:
        while True:
            yield "value"
    finally:
        print("Generator closed - cleanup code runs")

gen = cleanup_generator()
print(next(gen))  # "value"
gen.close()       # Generator closed - cleanup code runs
# next(gen)       # Raises StopIteration
```

## 5. yield from - Delegating to Subgenerators

`yield from` delegates to another generator:

```python
def sub_generator():
    yield 1
    yield 2
    yield 3

def main_generator():
    yield "start"
    yield from sub_generator()
    yield "end"

for value in main_generator():
    print(value)
# Output: start, 1, 2, 3, end
```

### Why yield from?

**Before yield from:**
```python
def flatten_nested(nested):
    for item in nested:
        if isinstance(item, list):
            for sub_item in flatten_nested(item):
                yield sub_item
        else:
            yield item
```

**With yield from:**
```python
def flatten_nested(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten_nested(item)
        else:
            yield item

nested = [1, [2, 3, [4, 5]], 6]
print(list(flatten_nested(nested)))  # [1, 2, 3, 4, 5, 6]
```

### yield from with send()

`yield from` properly forwards `send()` calls:

```python
def sub_gen():
    while True:
        x = yield
        yield x * 2

def main_gen():
    yield from sub_gen()

gen = main_gen()
next(gen)
print(gen.send(10))  # 20
next(gen)
print(gen.send(5))   # 10
```

## 6. Generator Patterns

### Pattern 1: Pipeline Processing

Chain generators for data transformation:

```python
def read_lines(filename):
    """Generator that reads lines from file"""
    with open(filename) as f:
        for line in f:
            yield line.strip()

def filter_comments(lines):
    """Filter out comment lines"""
    for line in lines:
        if not line.startswith('#'):
            yield line

def parse_data(lines):
    """Parse data from lines"""
    for line in lines:
        parts = line.split(',')
        yield {
            'name': parts[0],
            'value': int(parts[1])
        }

# Build pipeline
lines = read_lines('data.txt')
no_comments = filter_comments(lines)
data = parse_data(no_comments)

# Process lazily
for record in data:
    print(record)
```

### Pattern 2: Infinite Sequences

```python
def fibonacci():
    """Infinite Fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def take(n, iterable):
    """Take first n items from iterable"""
    for i, item in enumerate(iterable):
        if i >= n:
            break
        yield item

# Get first 10 Fibonacci numbers
for num in take(10, fibonacci()):
    print(num)
```

### Pattern 3: State Machines

```python
def state_machine():
    """Generator as state machine"""
    state = 'START'

    while True:
        if state == 'START':
            command = yield 'Ready'
            state = 'RUNNING' if command == 'start' else 'START'

        elif state == 'RUNNING':
            command = yield 'Processing'
            state = 'STOPPED' if command == 'stop' else 'RUNNING'

        elif state == 'STOPPED':
            command = yield 'Stopped'
            state = 'START' if command == 'reset' else 'STOPPED'

sm = state_machine()
print(next(sm))            # Ready
print(sm.send('start'))    # Processing
print(sm.send('process'))  # Processing
print(sm.send('stop'))     # Stopped
```

### Pattern 4: Buffering and Batching

```python
def batch(iterable, size):
    """Batch items from iterable"""
    batch_items = []

    for item in iterable:
        batch_items.append(item)
        if len(batch_items) == size:
            yield batch_items
            batch_items = []

    if batch_items:
        yield batch_items

# Process data in batches
data = range(10)
for batch_items in batch(data, 3):
    print(f"Processing batch: {batch_items}")
# Output:
# Processing batch: [0, 1, 2]
# Processing batch: [3, 4, 5]
# Processing batch: [6, 7, 8]
# Processing batch: [9]
```

## 7. Async Generators (Python 3.6+)

Async generators combine generators with async/await:

```python
import asyncio

async def async_range(n):
    """Async generator"""
    for i in range(n):
        await asyncio.sleep(0.1)  # Simulate async operation
        yield i

async def main():
    async for value in async_range(5):
        print(value)

# asyncio.run(main())
```

### Async Generator Expressions

```python
async def fetch_data(n):
    """Simulate async data fetching"""
    await asyncio.sleep(0.1)
    return n * 2

async def main():
    # Async generator expression
    results = [await fetch_data(i) async for i in async_range(5)]
    print(results)
```

## 8. Memory Efficiency

### Comparison: List vs Generator

```python
import sys

# List - loads everything in memory
def sum_squares_list(n):
    numbers = list(range(n))
    squares = [x**2 for x in numbers]
    return sum(squares)

# Generator - processes one at a time
def sum_squares_gen(n):
    squares = (x**2 for x in range(n))
    return sum(squares)

# Memory usage
n = 1000000

# List approach uses ~80MB
# Generator approach uses ~200 bytes

# Time is similar, but memory usage is drastically different
```

## 9. Generator Delegation and Composition

### Composing Generators

```python
def integers(start=0):
    """Generate infinite integers"""
    i = start
    while True:
        yield i
        i += 1

def squares(start=0):
    """Generate squares"""
    yield from (x**2 for x in integers(start))

def evens(iterable):
    """Filter even numbers"""
    yield from (x for x in iterable if x % 2 == 0)

# Compose generators
even_squares = evens(squares(0))

# Get first 5 even squares
for i, value in enumerate(even_squares):
    if i >= 5:
        break
    print(value)  # 0, 4, 16, 36, 64
```

## 10. Common Use Cases

### File Processing

```python
def process_large_file(filename):
    """Process large file line by line"""
    with open(filename) as f:
        for line in f:
            # Process line
            yield line.strip().upper()
```

### API Pagination

```python
def fetch_all_pages(api_url):
    """Generator for paginated API results"""
    page = 1
    while True:
        response = requests.get(f"{api_url}?page={page}")
        data = response.json()

        if not data:
            break

        yield from data['results']
        page += 1
```

### Data Streaming

```python
def stream_csv(filename):
    """Stream CSV rows as dictionaries"""
    import csv

    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row
```

## Key Concepts Summary

1. **Iterators**: Objects implementing `__iter__` and `__next__`
2. **Generators**: Functions using `yield`, automatic iterator implementation
3. **Generator Expressions**: Memory-efficient alternative to list comprehensions
4. **Generator Methods**: `send()`, `throw()`, `close()` for control
5. **yield from**: Delegate to subgenerators
6. **Async Generators**: Combine generators with async/await
7. **Memory Efficiency**: Process items one at a time
8. **Lazy Evaluation**: Compute values only when needed
9. **Pipelines**: Chain generators for data transformation
10. **Infinite Sequences**: Represent unbounded sequences efficiently

## When to Use Generators

**Use generators when:**
- Processing large files or datasets
- Working with infinite sequences
- Building data transformation pipelines
- Memory is a concern
- You need lazy evaluation
- Processing can be done item-by-item

**Don't use generators when:**
- You need random access to items
- You need the length of the sequence
- You need to iterate multiple times (use `itertools.tee()`)
- The overhead of function calls matters more than memory

Generators are one of Python's most powerful features for writing efficient, elegant code. They enable you to work with data streams naturally while keeping memory usage minimal.
