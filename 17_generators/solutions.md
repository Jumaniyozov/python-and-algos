# Solutions: Generators & Iterators

## Solution 1: Range Iterator

```python
class Range:
    """Custom range iterator"""

    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop

        self.step = step
        self.current = self.start

        # Validate step
        if step == 0:
            raise ValueError("step cannot be zero")

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.current >= self.stop:
                raise StopIteration
        else:
            if self.current <= self.stop:
                raise StopIteration

        value = self.current
        self.current += self.step
        return value

# Test
print(list(Range(5)))           # [0, 1, 2, 3, 4]
print(list(Range(1, 6)))        # [1, 2, 3, 4, 5]
print(list(Range(0, 10, 2)))    # [0, 2, 4, 6, 8]
print(list(Range(10, 0, -2)))   # [10, 8, 6, 4, 2]
```

## Solution 2: Prime Number Generator

```python
def primes(limit):
    """Generate prime numbers up to limit"""
    if limit < 2:
        return

    yield 2

    for num in range(3, limit + 1, 2):
        is_prime = True
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

# More efficient: Sieve of Eratosthenes
def primes_sieve(limit):
    """Generate primes using sieve algorithm"""
    if limit < 2:
        return

    # Create boolean array
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            # Mark multiples as not prime
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False

    # Yield primes
    for num, prime in enumerate(is_prime):
        if prime:
            yield num

# Test
print(list(primes(30)))
print(list(primes_sieve(30)))
```

## Solution 3: File Line Counter

```python
def numbered_lines(filename):
    """Yield line numbers and content for non-empty lines"""
    with open(filename) as f:
        for line_num, line in enumerate(f, 1):
            stripped = line.strip()
            if stripped:
                yield (line_num, stripped)

# Alternative with error handling
def safe_numbered_lines(filename):
    """Safe version with error handling"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                stripped = line.strip()
                if stripped:
                    yield (line_num, stripped)
    except FileNotFoundError:
        print(f"File {filename} not found")
    except IOError as e:
        print(f"Error reading file: {e}")

# Test
for num, content in numbered_lines('test.txt'):
    print(f"{num}: {content}")
```

## Solution 4: Moving Average

```python
from collections import deque

def moving_average(iterable, window=3):
    """Calculate moving average over sliding window"""
    window_deque = deque(maxlen=window)

    for value in iterable:
        window_deque.append(value)
        if len(window_deque) == window:
            yield sum(window_deque) / window

# Alternative: More memory efficient
def moving_average_v2(iterable, window=3):
    """Moving average maintaining running sum"""
    values = deque(maxlen=window)
    total = 0

    for value in iterable:
        if len(values) == window:
            total -= values[0]

        values.append(value)
        total += value

        if len(values) == window:
            yield total / window

# Test
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(moving_average(data, 3)))
```

## Solution 5: Permutations Generator

```python
def permutations(items):
    """Generate all permutations of items"""
    if len(items) <= 1:
        yield items
    else:
        for i in range(len(items)):
            for perm in permutations(items[:i] + items[i+1:]):
                yield [items[i]] + perm

# Alternative: Iterative approach
def permutations_iterative(items):
    """Iterative permutation generator"""
    if not items:
        yield []
        return

    for i in range(len(items)):
        rest = items[:i] + items[i+1:]
        for p in permutations_iterative(rest):
            yield [items[i]] + p

# Test
print(list(permutations([1, 2, 3])))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

## Solution 6: Merge Sorted Iterables

```python
import heapq

def merge(*iterables):
    """Merge multiple sorted iterables"""
    # Using heapq.merge (efficient built-in)
    yield from heapq.merge(*iterables)

# Manual implementation
def merge_manual(*iterables):
    """Manual merge implementation"""
    heap = []

    # Initialize heap with first element from each iterable
    for idx, iterable in enumerate(iterables):
        iterator = iter(iterable)
        try:
            value = next(iterator)
            heapq.heappush(heap, (value, idx, iterator))
        except StopIteration:
            pass

    # Process heap
    while heap:
        value, idx, iterator = heapq.heappop(heap)
        yield value

        try:
            next_value = next(iterator)
            heapq.heappush(heap, (next_value, idx, iterator))
        except StopIteration:
            pass

# Test
a = [1, 4, 7, 10]
b = [2, 5, 8, 11]
c = [3, 6, 9, 12]
print(list(merge(a, b, c)))
```

## Solution 7: Coroutine Log Processor

```python
def log_processor():
    """Process log entries by level"""
    logs = {'INFO': [], 'WARNING': [], 'ERROR': []}

    while True:
        entry = yield
        if entry is None:
            break

        # Parse log entry
        parts = entry.split(':', 1)
        if len(parts) == 2:
            level = parts[0].strip().upper()
            message = parts[1].strip()

            if level in logs:
                logs[level].append(message)
                print(f"[{level}] {message}")

    return logs

# Usage
processor = log_processor()
next(processor)  # Prime

processor.send("INFO: Application started")
processor.send("WARNING: Low memory")
processor.send("ERROR: Connection failed")
processor.send("INFO: Request completed")

try:
    processor.send(None)
except StopIteration as e:
    summary = e.value
    print("\nSummary:")
    for level, messages in summary.items():
        print(f"{level}: {len(messages)} messages")
```

## Solution 8: Flatten Nested Structure

```python
def flatten(nested):
    """Recursively flatten nested lists, tuples, and sets"""
    for item in nested:
        if isinstance(item, (list, tuple, set)):
            yield from flatten(item)
        else:
            yield item

# Alternative with type checking
def flatten_deep(nested, types=(list, tuple, set)):
    """Flatten with customizable types"""
    for item in nested:
        if isinstance(item, types) and not isinstance(item, (str, bytes)):
            yield from flatten_deep(item, types)
        else:
            yield item

# Test
nested = [1, [2, (3, 4)], {5, 6}, [[7, 8]]]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6, 7, 8]
```

## Solution 9: Lazy JSON Parser

```python
import json
import re

def parse_json_array(filename):
    """Parse JSON array lazily, yielding objects one at a time"""
    with open(filename, 'r') as f:
        # Skip opening bracket
        depth = 0
        obj_start = None
        buffer = []

        for line in f:
            for char in line:
                if char == '{':
                    if depth == 0:
                        buffer = []
                        obj_start = True
                    depth += 1
                    buffer.append(char)
                elif char == '}':
                    buffer.append(char)
                    depth -= 1
                    if depth == 0 and obj_start:
                        obj_str = ''.join(buffer)
                        yield json.loads(obj_str)
                        obj_start = False
                elif depth > 0:
                    buffer.append(char)

# Simpler version for well-formatted JSON
def parse_json_stream(filename):
    """Parse JSON array from file"""
    import ijson  # pip install ijson

    with open(filename, 'rb') as f:
        parser = ijson.items(f, 'item')
        for obj in parser:
            yield obj

# Test (create test file first)
# with open('test.json', 'w') as f:
#     json.dump([{'id': i, 'name': f'Item {i}'} for i in range(5)], f)
#
# for obj in parse_json_array('test.json'):
#     print(obj)
```

## Solution 10: Generator Pipeline Framework

```python
from functools import wraps

def source(func):
    """Decorator for data source"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.is_source = True
    return wrapper

def filter_stage(predicate):
    """Decorator for filter stage"""
    def decorator(func):
        @wraps(func)
        def wrapper(iterable):
            for item in iterable:
                if predicate(item):
                    yield func(item)
        return wrapper
    return decorator

def transform(func):
    """Decorator for transformation"""
    @wraps(func)
    def wrapper(iterable):
        for item in iterable:
            yield func(item)
    return wrapper

def sink(func):
    """Decorator for output sink"""
    @wraps(func)
    def wrapper(iterable):
        results = []
        for item in iterable:
            result = func(item)
            if result is not None:
                results.append(result)
        return results
    return wrapper

class Pipeline:
    """Pipeline composition"""
    def __init__(self, source):
        self.source = source
        self.stages = []

    def pipe(self, stage):
        self.stages.append(stage)
        return self

    def run(self):
        data = self.source()
        for stage in self.stages:
            data = stage(data)
        return data

# Usage
@source
def numbers():
    return range(1, 11)

@transform
def square(x):
    return x ** 2

@transform
def add_one(x):
    return x + 1

def is_even(x):
    return x % 2 == 0

@sink
def collect(x):
    return x

# Build and run pipeline
pipeline = Pipeline(numbers)
pipeline.pipe(square).pipe(add_one)
results = pipeline.pipe(lambda iterable: (x for x in iterable if is_even(x))).run()
print(list(results))
```

## Solutions 11-15: Advanced Problems

Solutions for exercises 11-15 would include:

- **11. Paginated API**: Using `requests` with generator yield
- **12. Lexer**: Token generation with regex patterns
- **13. Circular Buffer**: Using `collections.deque` with `send()`
- **14. Tree Walker**: Control flow with generator state
- **15. Async Scraper**: `aiohttp` with async generators

Each solution demonstrates different aspects of generator mastery and real-world application patterns.

## Key Techniques Demonstrated

1. **Iterator Protocol**: Manual implementation with `__iter__` and `__next__`
2. **Generator Functions**: Using `yield` for lazy evaluation
3. **Generator State**: Maintaining state between yields
4. **Two-way Communication**: Using `send()` for coroutines
5. **Delegation**: Using `yield from` for subgenerators
6. **Pipeline Architecture**: Chaining generators for data processing
7. **Memory Efficiency**: Processing large datasets incrementally
8. **Error Handling**: Graceful exception handling in generators
9. **Async Generators**: Combining generators with async/await
10. **Real-world Patterns**: File processing, API pagination, data transformation

These solutions provide a comprehensive foundation for using generators in production code.
