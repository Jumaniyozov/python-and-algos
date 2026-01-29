# Debugging and Profiling - Exercises

## Exercise 1: Debug Factorial Bug
Find and fix the bug in this factorial function.

```python
def factorial(n):
    if n == 0:
        return 0  # Bug here!
    return n * factorial(n - 1)

# Test
print(factorial(5))  # Should be 120
```

## Exercise 2: Add Logging
Add appropriate logging to this function.

```python
def process_file(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    processed = []
    for line in lines:
        if line.strip():
            processed.append(line.upper())

    return processed

# Add DEBUG, INFO, WARNING, ERROR logs as appropriate
```

## Exercise 3: Profile and Optimize
Profile these two functions and determine which is faster.

```python
def method1(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result

def method2(n):
    return [i for i in range(n) if i % 2 == 0]

# Use timeit to compare performance
```

## Exercise 4: Find Memory Leak
Use tracemalloc to find the memory leak.

```python
class Cache:
    _cache = {}

    def add(self, key, value):
        self._cache[key] = value

# This will leak memory
cache = Cache()
for i in range(10000):
    cache.add(i, "x" * 1000)

# Identify and fix the issue
```

## Exercise 5: Add Timing Decorator
Create a decorator that times function execution.

```python
def timing_decorator(func):
    # Implement decorator
    pass

@timing_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Done"

# Should print execution time
```

## Exercise 6: Debug Stack Overflow
Fix the stack overflow error.

```python
def count_down(n):
    print(n)
    count_down(n - 1)

count_down(10)  # Causes RecursionError
```

## Exercise 7: Conditional Logging
Implement logging that only logs in debug mode.

```python
import logging

class DataProcessor:
    def __init__(self, debug=False):
        # Setup logging based on debug flag
        pass

    def process(self, data):
        # Add conditional logging
        return data.upper()
```

## Exercise 8: Profile Memory Usage
Profile memory usage of different data structures.

```python
# Compare memory usage of:
# 1. List of integers
# 2. Set of integers
# 3. Dict with integer keys
# Use tracemalloc to measure
```

## Exercise 9: Debug Race Condition
Find and fix the race condition (if you can reproduce it).

```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Counter: {counter}")  # Should be 1000000
```

## Exercise 10: Create Performance Report
Create a function that generates a performance report.

```python
def performance_report(func, *args, **kwargs):
    """
    Run function and return performance metrics:
    - Execution time
    - Memory usage
    - Number of calls (if recursive)

    Returns dict with metrics
    """
    pass

# Test
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

metrics = performance_report(fibonacci, 10)
print(metrics)
```
