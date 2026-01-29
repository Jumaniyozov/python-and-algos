# Chapter 22: Performance Optimization - Theory

## Introduction

Performance optimization is crucial for building efficient Python applications. This chapter covers profiling, benchmarking, and optimization techniques to make your code faster and more memory-efficient.

**Key principle**: Always profile before optimizing. Premature optimization is the root of all evil.

## 1. Profiling with cProfile

### What is Profiling?
Profiling measures where your program spends time, helping identify bottlenecks.

### Using cProfile

```python
import cProfile
import pstats

def profile_function():
    # Code to profile
    result = sum(i**2 for i in range(10000))
    return result

# Profile and print stats
cProfile.run('profile_function()', sort='cumulative')
```

### Saving Profile Data

```python
import cProfile
import pstats

# Save profile data
cProfile.run('my_function()', 'profile_output.stats')

# Load and analyze
stats = pstats.Stats('profile_output.stats')
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 functions
```

### Key Metrics
- **ncalls**: Number of times function was called
- **tottime**: Total time in function (excluding subcalls)
- **cumtime**: Cumulative time (including subcalls)
- **percall**: Time per call

## 2. Benchmarking with timeit

### Basic Usage

```python
import timeit

# Time a statement
time = timeit.timeit('sum(range(100))', number=10000)
print(f"Time: {time:.6f} seconds")

# Time with setup
time = timeit.timeit(
    stmt='func(data)',
    setup='from __main__ import func; data = list(range(1000))',
    number=1000
)
```

### Comparing Approaches

```python
import timeit

# Compare list comprehension vs map
list_comp = timeit.timeit('[x*2 for x in range(100)]', number=10000)
map_time = timeit.timeit('list(map(lambda x: x*2, range(100)))', number=10000)

print(f"List comprehension: {list_comp:.6f}s")
print(f"Map: {map_time:.6f}s")
print(f"Faster: {' list comp' if list_comp < map_time else 'map'}")
```

### Using Timer Object

```python
import timeit

timer = timeit.Timer('sum(range(1000))')
result = timer.repeat(repeat=5, number=10000)
print(f"Min: {min(result):.6f}s")
print(f"Avg: {sum(result)/len(result):.6f}s")
```

## 3. Line-by-Line Profiling

### Using line_profiler (external package)

```python
# Install: pip install line_profiler

@profile  # Decorator when running with kernprof
def slow_function():
    total = 0
    for i in range(1000):
        total += i**2
    return total

# Run with: kernprof -l -v script.py
```

### Memory Profiling

```python
# Install: pip install memory_profiler

@profile
def memory_heavy():
    large_list = [i for i in range(1000000)]
    return sum(large_list)

# Run with: python -m memory_profiler script.py
```

## 4. Algorithmic Optimization

### Time Complexity Matters

```python
# O(n²) - Slow
def has_duplicate_slow(items):
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] == items[j]:
                return True
    return False

# O(n) - Fast
def has_duplicate_fast(items):
    return len(items) != len(set(items))

# Benchmark
import timeit
data = list(range(1000))

slow = timeit.timeit(lambda: has_duplicate_slow(data), number=100)
fast = timeit.timeit(lambda: has_duplicate_fast(data), number=100)
print(f"Slow: {slow:.4f}s, Fast: {fast:.4f}s, Speedup: {slow/fast:.1f}x")
```

### Choose Right Data Structure

```python
# List lookup: O(n)
large_list = list(range(10000))
'abc' in large_list  # Slow

# Set lookup: O(1)
large_set = set(range(10000))
'abc' in large_set  # Fast

# Dict lookup: O(1)
large_dict = {i: i for i in range(10000)}
'abc' in large_dict  # Fast
```

## 5. String Optimization

### String Concatenation

```python
import timeit

# Slow: += creates new string each time (O(n²))
def concat_slow(n):
    s = ''
    for i in range(n):
        s += str(i)
    return s

# Fast: join is O(n)
def concat_fast(n):
    return ''.join(str(i) for i in range(n))

# Benchmark
n = 1000
slow = timeit.timeit(lambda: concat_slow(n), number=100)
fast = timeit.timeit(lambda: concat_fast(n), number=100)
print(f"Speedup: {slow/fast:.1f}x")
```

### String Building

```python
# Use f-strings (fastest)
name = "Alice"
age = 30
f"{name} is {age} years old"

# Format strings (fast)
"{} is {} years old".format(name, age)

# %-formatting (slower)
"%s is %d years old" % (name, age)
```

## 6. Loop Optimization

### List Comprehensions vs Loops

```python
# Slower: Regular loop with append
def loop_append(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

# Faster: List comprehension
def list_comp(n):
    return [i**2 for i in range(n)]

# Even faster for specific operations: map
def using_map(n):
    return list(map(lambda x: x**2, range(n)))
```

### Avoid Repeated Lookups

```python
# Slow: Repeated attribute lookup
def slow(data):
    result = []
    for item in data:
        result.append(item)  # append looked up each time
    return result

# Fast: Cache attribute
def fast(data):
    result = []
    append = result.append  # Cache method
    for item in data:
        append(item)
    return result
```

### Use Built-in Functions

```python
# Slower: Manual implementation
def manual_sum(items):
    total = 0
    for item in items:
        total += item
    return total

# Faster: Built-in (C implementation)
def builtin_sum(items):
    return sum(items)
```

## 7. Function Call Overhead

### Minimize Function Calls

```python
# Slower: Many function calls
def slow_process(data):
    return [expensive_func(x) for x in data]

# Faster: Batch processing
def fast_process(data):
    # Process in batches if possible
    return batch_expensive_func(data)
```

### Inline Simple Functions

```python
# Slower: Function call overhead
def square(x):
    return x * x

result = [square(x) for x in range(1000)]

# Faster: Inline operation
result = [x * x for x in range(1000)]
```

## 8. Import Optimization

### Import at Module Level

```python
# Slow: Import inside loop
def slow():
    for i in range(1000):
        import math
        result = math.sqrt(i)

# Fast: Import at top
import math

def fast():
    for i in range(1000):
        result = math.sqrt(i)
```

### Import Specific Names

```python
# Slower: Module attribute lookup
import math
for i in range(1000):
    result = math.sqrt(i)

# Faster: Direct import
from math import sqrt
for i in range(1000):
    result = sqrt(i)
```

### Lazy Imports for Heavy Modules

```python
# Only import when needed
def process_image(image_path):
    import PIL.Image  # Import only when function is called
    img = PIL.Image.open(image_path)
    return img.size
```

## 9. Caching Strategies

### functools.lru_cache

```python
from functools import lru_cache

# Without cache: O(2^n)
def fibonacci_slow(n):
    if n < 2:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)

# With cache: O(n)
@lru_cache(maxsize=None)
def fibonacci_fast(n):
    if n < 2:
        return n
    return fibonacci_fast(n-1) + fibonacci_fast(n-2)

# Benchmark
import timeit
print(timeit.timeit(lambda: fibonacci_slow(20), number=1))  # ~4s
print(timeit.timeit(lambda: fibonacci_fast(20), number=1))   # ~0.00001s
```

### Custom Caching

```python
class ComputationCache:
    def __init__(self):
        self.cache = {}

    def get_or_compute(self, key, compute_func):
        if key not in self.cache:
            self.cache[key] = compute_func(key)
        return self.cache[key]
```

### Cache Invalidation

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(x, y):
    return x ** y

# Clear cache when needed
expensive_computation.cache_clear()

# Get cache stats
print(expensive_computation.cache_info())
```

## 10. Dictionary and Set Operations

### Dictionary get() vs try/except

```python
import timeit

d = {'a': 1, 'b': 2}

# Faster for keys that exist
def use_get():
    return d.get('a', 0)

# Faster for keys that don't exist
def use_try():
    try:
        return d['a']
    except KeyError:
        return 0

# Rule: Use try/except when key usually exists
# Use get() when key often doesn't exist
```

### Set Operations for Membership Testing

```python
# Slow: List membership O(n)
items_list = list(range(10000))
5000 in items_list

# Fast: Set membership O(1)
items_set = set(range(10000))
5000 in items_set

# Use sets for:
# - Uniqueness checking
# - Fast membership testing
# - Set operations (union, intersection)
```

## 11. Generator vs List

### Memory Efficiency

```python
import sys

# List: All items in memory
list_data = [i for i in range(1000000)]
print(f"List size: {sys.getsizeof(list_data)} bytes")

# Generator: One item at a time
gen_data = (i for i in range(1000000))
print(f"Generator size: {sys.getsizeof(gen_data)} bytes")
```

### When to Use Each

```python
# Use generators for:
# - Large datasets
# - One-time iteration
# - Pipeline processing

def process_large_file(filename):
    with open(filename) as f:
        for line in f:  # Generator
            yield process_line(line)

# Use lists for:
# - Multiple iterations
# - Random access
# - Small datasets
```

## 12. Local vs Global Variables

### Lookup Speed

```python
import timeit

# Global variable (slower lookup)
global_var = 10

def use_global():
    return global_var + 1

# Local variable (faster lookup)
def use_local():
    local_var = 10
    return local_var + 1

# Local is ~20% faster
```

### Optimization Technique

```python
# Slow: Global lookups
import math

def compute(x):
    return math.sqrt(math.pow(x, 2))

# Fast: Localize
import math

def compute_fast(x):
    sqrt = math.sqrt
    pow = math.pow
    return sqrt(pow(x, 2))
```

## 13. Pre-allocation

### List Pre-allocation

```python
# Slower: Growing list
def slow(n):
    result = []
    for i in range(n):
        result.append(i)
    return result

# Faster: Pre-allocate
def fast(n):
    result = [None] * n
    for i in range(n):
        result[i] = i
    return result
```

## 14. Lazy Evaluation

### Generator Expressions

```python
# Eager: All computed immediately
squares_list = [x**2 for x in range(1000000)]
first_10 = squares_list[:10]

# Lazy: Computed on demand
squares_gen = (x**2 for x in range(1000000))
first_10 = list(itertools.islice(squares_gen, 10))
```

### Property Caching

```python
class ExpensiveObject:
    def __init__(self):
        self._cached_value = None

    @property
    def expensive_property(self):
        if self._cached_value is None:
            # Compute only once
            self._cached_value = self._expensive_computation()
        return self._cached_value

    def _expensive_computation(self):
        return sum(i**2 for i in range(10000))
```

## 15. NumPy Vectorization

### Array Operations

```python
import numpy as np
import timeit

# Python list: Slow (interpreted loop)
def python_loop(n):
    data = list(range(n))
    return [x**2 for x in data]

# NumPy: Fast (vectorized C code)
def numpy_vectorized(n):
    data = np.arange(n)
    return data ** 2

# Benchmark
n = 100000
py_time = timeit.timeit(lambda: python_loop(n), number=10)
np_time = timeit.timeit(lambda: numpy_vectorized(n), number=10)
print(f"Speedup: {py_time/np_time:.1f}x")
```

## 16. C Extensions Overview

### When to Consider C Extensions
- CPU-intensive operations
- Performance-critical loops
- Existing C libraries
- After Python optimization exhausted

### Tools
- **ctypes**: Call C functions from Python
- **Cython**: Python-like language compiled to C
- **Numba**: JIT compiler for Python
- **PyBind11**: C++ bindings

### Example: Numba

```python
from numba import jit
import numpy as np

# Regular Python: Slow
def python_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

# Numba JIT: Fast
@jit(nopython=True)
def numba_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

# Can be 100x+ faster for numerical code
```

## Performance Optimization Workflow

1. **Measure first**: Profile to find bottlenecks
2. **Algorithmic optimization**: Better algorithm > micro-optimizations
3. **Python optimizations**: Built-ins, comprehensions, caching
4. **Consider external tools**: NumPy, Numba, Cython
5. **Measure again**: Verify improvements

## Summary

Key principles:
- **Profile before optimizing** - Don't guess
- **Algorithm matters most** - O(n) vs O(n²) > micro-optimizations
- **Use right data structures** - Lists, sets, dicts for different needs
- **Built-ins are fast** - Implemented in C
- **Cache expensive computations** - Trade memory for speed
- **Generators for large data** - Memory efficient
- **Localize lookups** - Local > global > builtin
- **String operations** - Use join(), not +=
- **NumPy for numbers** - Vectorization is much faster

Remember: **Readable code > optimized code** unless performance is critical!
