# Debugging and Profiling - Solutions

## Solution 1: Debug Factorial Bug

```python
def factorial(n):
    if n == 0:
        return 1  # Fixed: 0! = 1, not 0
    return n * factorial(n - 1)

# Test
print(factorial(5))  # 120
print(factorial(0))  # 1
```

## Solution 2: Add Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_file(filepath):
    logger.info(f"Processing file: {filepath}")

    try:
        with open(filepath) as f:
            lines = f.readlines()
        logger.debug(f"Read {len(lines)} lines")
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        return []

    processed = []
    for i, line in enumerate(lines):
        if line.strip():
            processed.append(line.upper())
        else:
            logger.debug(f"Skipping empty line {i+1}")

    logger.info(f"Processed {len(processed)} lines")

    if len(processed) == 0:
        logger.warning("No content to process")

    return processed
```

## Solution 3: Profile and Optimize

```python
import timeit

def method1(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result

def method2(n):
    return [i for i in range(n) if i % 2 == 0]

# Profile
n = 100000
time1 = timeit.timeit(lambda: method1(n), number=100)
time2 = timeit.timeit(lambda: method2(n), number=100)

print(f"Method 1: {time1:.4f}s")
print(f"Method 2: {time2:.4f}s")
print(f"Method 2 is {time1/time2:.2f}x faster")

# Result: Method 2 (list comprehension) is faster
```

## Solution 4: Find Memory Leak

```python
import tracemalloc

class Cache:
    def __init__(self):
        self._cache = {}  # Fixed: Instance variable, not class variable

    def add(self, key, value):
        self._cache[key] = value

    def clear(self):
        self._cache.clear()

# Test with tracemalloc
tracemalloc.start()

snapshot1 = tracemalloc.take_snapshot()

# Create multiple cache instances
caches = []
for _ in range(10):
    cache = Cache()
    for i in range(1000):
        cache.add(i, "x" * 1000)
    caches.append(cache)

snapshot2 = tracemalloc.take_snapshot()

# Show memory difference
stats = snapshot2.compare_to(snapshot1, 'lineno')
for stat in stats[:3]:
    print(stat)

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory: {current / 1024 / 1024:.2f} MB")

# Clean up
for cache in caches:
    cache.clear()
caches.clear()

current, peak = tracemalloc.get_traced_memory()
print(f"After cleanup: {current / 1024 / 1024:.2f} MB")

tracemalloc.stop()
```

## Solution 5: Add Timing Decorator

```python
import time
import functools

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f}s")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Done"

@timing_decorator
def fast_function():
    return sum(range(1000))

# Test
print(slow_function())  # Prints timing
print(fast_function())  # Prints timing
```

## Solution 6: Debug Stack Overflow

```python
def count_down(n):
    if n < 0:  # Fixed: Add base case
        return
    print(n)
    count_down(n - 1)

count_down(10)  # Works now

# Alternative: Use iteration
def count_down_iter(n):
    while n >= 0:
        print(n)
        n -= 1

count_down_iter(10)
```

## Solution 7: Conditional Logging

```python
import logging

class DataProcessor:
    def __init__(self, debug=False):
        self.logger = logging.getLogger(self.__class__.__name__)

        # Set level based on debug flag
        if debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)

        # Add handler if not already configured
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def process(self, data):
        self.logger.debug(f"Processing data: {data}")
        result = data.upper()
        self.logger.info(f"Processed data length: {len(result)}")
        return result

# Test
processor_debug = DataProcessor(debug=True)
processor_debug.process("hello")  # Shows DEBUG messages

processor_normal = DataProcessor(debug=False)
processor_normal.process("world")  # Only INFO messages
```

## Solution 8: Profile Memory Usage

```python
import tracemalloc
import sys

def profile_data_structure(name, create_func, n=10000):
    tracemalloc.start()
    snapshot1 = tracemalloc.take_snapshot()

    data = create_func(n)

    snapshot2 = tracemalloc.take_snapshot()
    stats = snapshot2.compare_to(snapshot1, 'lineno')

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"\n{name}:")
    print(f"  Memory: {current / 1024:.2f} KB")
    print(f"  Size: {sys.getsizeof(data) / 1024:.2f} KB")

# Test different structures
n = 10000

profile_data_structure(
    "List",
    lambda n: list(range(n)),
    n
)

profile_data_structure(
    "Set",
    lambda n: set(range(n)),
    n
)

profile_data_structure(
    "Dict",
    lambda n: {i: i for i in range(n)},
    n
)
```

## Solution 9: Debug Race Condition

```python
import threading

counter = 0
lock = threading.Lock()  # Fixed: Add lock

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Fixed: Protect shared resource
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Counter: {counter}")  # Now correctly 1000000
```

## Solution 10: Create Performance Report

```python
import time
import tracemalloc
import functools

def performance_report(func, *args, **kwargs):
    """Generate performance metrics for function."""

    # Track call count for recursive functions
    call_count = [0]

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        call_count[0] += 1
        return func(*args, **kwargs)

    # Start tracking
    tracemalloc.start()
    start_time = time.time()
    start_memory = tracemalloc.get_traced_memory()[0]

    # Run function
    result = wrapper(*args, **kwargs)

    # Collect metrics
    end_time = time.time()
    end_memory = tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()

    return {
        'result': result,
        'execution_time': end_time - start_time,
        'memory_used': end_memory - start_memory,
        'call_count': call_count[0]
    }

# Test
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

metrics = performance_report(fibonacci, 20)
print(f"Result: {metrics['result']}")
print(f"Time: {metrics['execution_time']:.4f}s")
print(f"Memory: {metrics['memory_used'] / 1024:.2f} KB")
print(f"Calls: {metrics['call_count']}")

# Better fibonacci with memoization
@functools.lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

metrics2 = performance_report(fibonacci_cached, 20)
print(f"\nWith caching:")
print(f"Time: {metrics2['execution_time']:.4f}s")
print(f"Calls: {metrics2['call_count']}")
print(f"Speedup: {metrics['execution_time']/metrics2['execution_time']:.2f}x")
```
