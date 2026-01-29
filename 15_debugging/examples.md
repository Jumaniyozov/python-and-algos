# Debugging and Profiling - Examples

## Example 1: Basic pdb Usage

```python
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        import pdb; pdb.set_trace()  # Breakpoint
        total += num
    return total

# Run this and use pdb commands:
# l - list code
# n - next line
# p total - print total
# p num - print num
# c - continue
calculate_sum([1, 2, 3, 4, 5])
```

## Example 2: Python 3.7+ breakpoint()

```python
def divide(a, b):
    breakpoint()  # Easier syntax
    return a / b

result = divide(10, 2)
```

## Example 3: Basic Logging

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def process_data(data):
    logging.debug(f"Processing data: {data}")
    if not data:
        logging.warning("Empty data received")
        return None

    logging.info(f"Data length: {len(data)}")
    result = data.upper()
    logging.info("Processing complete")
    return result

# Test
process_data("hello")
process_data("")
```

## Example 4: Logging to File

```python
import logging

# Configure file logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()  # Also print to console
    ]
)

logger = logging.getLogger(__name__)

def important_operation():
    logger.info("Starting operation")
    try:
        # ... do something ...
        logger.info("Operation successful")
    except Exception as e:
        logger.error(f"Operation failed: {e}")
        raise
```

## Example 5: Multiple Log Levels

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_user(user_id):
    logger.debug(f"Fetching user {user_id}")

    if user_id < 0:
        logger.error(f"Invalid user ID: {user_id}")
        raise ValueError("User ID must be positive")

    if user_id > 1000:
        logger.warning(f"User ID {user_id} is very large")

    logger.info(f"Processing user {user_id}")
    logger.debug("Processing complete")

process_user(500)
```

## Example 6: cProfile Profiling

```python
import cProfile

def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

def fast_function():
    return sum(range(1000000))

def main():
    slow_function()
    fast_function()

# Profile the code
cProfile.run('main()')

# Output shows:
# - ncalls: number of calls
# - tottime: total time in function
# - cumtime: cumulative time (including subcalls)
```

## Example 7: timeit for Microbenchmarking

```python
import timeit

# Compare two approaches
def using_loop():
    result = []
    for i in range(1000):
        result.append(i * 2)
    return result

def using_comprehension():
    return [i * 2 for i in range(1000)]

# Time them
loop_time = timeit.timeit(using_loop, number=10000)
comp_time = timeit.timeit(using_comprehension, number=10000)

print(f"Loop: {loop_time:.4f}s")
print(f"Comprehension: {comp_time:.4f}s")
print(f"Speedup: {loop_time/comp_time:.2f}x")

# One-liner timing
time = timeit.timeit('sum(range(100))', number=10000)
print(f"Time: {time:.4f}s")
```

## Example 8: Memory Profiling with tracemalloc

```python
import tracemalloc

def create_large_list():
    return [i for i in range(1000000)]

def create_large_dict():
    return {i: i*2 for i in range(1000000)}

# Start tracking
tracemalloc.start()

# Take snapshot before
snapshot1 = tracemalloc.take_snapshot()

# Run functions
list_data = create_large_list()
dict_data = create_large_dict()

# Take snapshot after
snapshot2 = tracemalloc.take_snapshot()

# Compare snapshots
top_stats = snapshot2.compare_to(snapshot1, 'lineno')

print("Top memory allocations:")
for stat in top_stats[:5]:
    print(stat)

# Get current memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.2f} MB")
print(f"Peak: {peak / 1024 / 1024:.2f} MB")

tracemalloc.stop()
```

## Example 9: Context Manager for Timing

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(name):
    start = time.time()
    yield
    end = time.time()
    print(f"{name}: {end - start:.4f}s")

# Usage
with timer("Processing data"):
    # Slow operation
    time.sleep(1)
    result = sum(range(1000000))

with timer("Quick operation"):
    result = sum(range(100))
```

## Example 10: Decorator for Function Profiling

```python
import time
import functools

def profile(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@profile
def slow_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

@profile
def fast_function(n):
    return sum(range(n))

# Usage
slow_function(1000000)
fast_function(1000000)
```

## Example 11: Post-Mortem Debugging

```python
import pdb

def buggy_function():
    x = 5
    y = 0
    return x / y  # Will raise ZeroDivisionError

try:
    buggy_function()
except:
    # Enter debugger at point of exception
    pdb.post_mortem()
```

## Example 12: Conditional Breakpoint

```python
def process_items(items):
    for i, item in enumerate(items):
        # Only break on specific condition
        if i == 5 and item > 100:
            breakpoint()

        # Process item
        result = item * 2
        print(f"Processed: {result}")

items = list(range(10))
process_items(items)
```

## Example 13: Memory Leak Detection

```python
import tracemalloc
import gc

class LeakyClass:
    instances = []

    def __init__(self):
        # This creates a memory leak!
        LeakyClass.instances.append(self)

tracemalloc.start()

# Create many instances
for _ in range(1000):
    obj = LeakyClass()

# Check memory
current, peak = tracemalloc.get_traced_memory()
print(f"Memory after creation: {current / 1024:.2f} KB")

# Try to free memory
del obj
gc.collect()

current, peak = tracemalloc.get_traced_memory()
print(f"Memory after deletion: {current / 1024:.2f} KB")
print(f"Leaked instances: {len(LeakyClass.instances)}")

tracemalloc.stop()
```

## Example 14: Line-by-Line Timing

```python
import time

def profile_lines():
    # Manually time each section
    start = time.time()
    data = list(range(1000000))
    print(f"Create list: {time.time() - start:.4f}s")

    start = time.time()
    squares = [x**2 for x in data]
    print(f"Calculate squares: {time.time() - start:.4f}s")

    start = time.time()
    result = sum(squares)
    print(f"Sum: {time.time() - start:.4f}s")

    return result

profile_lines()
```

## Example 15: Logging Best Practices

```python
import logging
import sys

# Create custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Console handler for INFO and above
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# File handler for everything
file_handler = logging.FileHandler('debug.log')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Add handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Use logger
logger.debug("Debug message (file only)")
logger.info("Info message (both)")
logger.warning("Warning message (both)")
logger.error("Error message (both)")
```
