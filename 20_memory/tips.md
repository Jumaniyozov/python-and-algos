# Tips & Best Practices: Memory Management

## Best Practices

### Tip 1: Use __slots__ for Data Classes with Many Instances

When creating classes that will have many instances (thousands+), use `__slots__` to reduce memory overhead by 40-60%.

```python
# BAD: High memory overhead
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# GOOD: Minimal memory overhead
class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

# When to use:
# - Creating 1000+ instances
# - Fixed set of attributes
# - Memory is constrained
# - Performance-critical code

# When NOT to use:
# - Few instances (< 100)
# - Need dynamic attributes
# - Multiple inheritance
# - Need __dict__ or __weakref__
```

### Tip 2: Prefer Generators Over Lists for Large Sequences

Generators use constant memory regardless of sequence length, while lists store everything in memory.

```python
# BAD: Loads entire sequence into memory
def process_large_file(filepath):
    with open(filepath) as f:
        lines = f.readlines()  # All lines in memory!
    return [process_line(line) for line in lines]

# GOOD: Processes one line at a time
def process_large_file(filepath):
    with open(filepath) as f:
        for line in f:
            yield process_line(line)

# Usage remains clean:
for result in process_large_file('huge.txt'):
    handle_result(result)

# Memory savings example:
# List:      1GB file = ~1GB RAM
# Generator: 1GB file = ~few KB RAM
```

### Tip 3: Use Weak References for Caches and Observers

Prevent memory leaks in caches, event systems, and parent-child relationships using `weakref`.

```python
import weakref

# BAD: Cache prevents garbage collection
class Cache:
    def __init__(self):
        self.cache = {}  # Strong references

    def set(self, key, obj):
        self.cache[key] = obj  # Keeps obj alive!

# GOOD: Cache allows garbage collection
class Cache:
    def __init__(self):
        self.cache = weakref.WeakValueDictionary()

    def set(self, key, obj):
        self.cache[key] = obj  # Cleaned up automatically

# Use cases:
# 1. Caches - don't prevent GC
# 2. Event listeners - auto-cleanup
# 3. Parent references in trees
# 4. Observer pattern implementations
```

### Tip 4: Choose the Right Data Structure

Different structures have vastly different memory footprints.

```python
import sys
import array

data = list(range(10000))

# Compare memory usage:
as_list = list(data)           # ~87 KB
as_tuple = tuple(data)         # ~80 KB (slightly better)
as_set = set(data)             # ~327 KB (hash table overhead)
as_dict = {i: i for i in data} # ~368 KB (key-value pairs)
as_array = array.array('i', data)  # ~40 KB (typed, compact!)

# Guidelines:
# - Homogeneous numbers → array.array
# - Fixed data → tuple
# - Membership testing → set
# - Key-value pairs → dict
# - General purpose → list
```

### Tip 5: Profile Before Optimizing

Always measure memory usage before and after optimization attempts.

```python
import tracemalloc

def profile_memory(func):
    """Decorator to profile memory usage"""
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"{func.__name__}:")
        print(f"  Current: {current / 1024 / 1024:.2f} MB")
        print(f"  Peak: {peak / 1024 / 1024:.2f} MB")

        return result
    return wrapper

@profile_memory
def my_function():
    data = [i**2 for i in range(1000000)]
    return sum(data)

# Profiling workflow:
# 1. Profile baseline
# 2. Identify hotspots
# 3. Apply optimization
# 4. Profile again
# 5. Compare results
```

### Tip 6: Use Context Managers for Resources

Always use context managers or weak finalizers for cleanup, never rely solely on `__del__`.

```python
# BAD: Unreliable cleanup
class FileHandler:
    def __init__(self, path):
        self.file = open(path)

    def __del__(self):
        self.file.close()  # May not be called!

# GOOD: Guaranteed cleanup
class FileHandler:
    def __init__(self, path):
        self.file = open(path)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.file.close()  # Always called

# BETTER: Use weakref.finalize for automatic cleanup
import weakref

class Resource:
    def __init__(self, name):
        self.name = name
        self._finalizer = weakref.finalize(
            self, self.cleanup, name
        )

    @staticmethod
    def cleanup(name):
        print(f"Cleaning up {name}")
```

### Tip 7: Intern Strings When Appropriate

String interning saves memory when you have many identical strings.

```python
import sys

# Without interning: separate objects
def create_labels(n):
    return ['label'] * n  # Multiple string objects

# With interning: single object
def create_labels_interned(n):
    label = sys.intern('label')
    return [label] * n  # Single string object

# Memory savings:
# 10,000 strings without interning: ~500 KB
# 10,000 strings with interning: ~80 KB

# Use when:
# - Many identical strings
# - Comparing strings frequently
# - Building string-heavy data structures
```

### Tip 8: Lazy Evaluation with Properties

Defer expensive computations until actually needed.

```python
# BAD: Computes everything upfront
class DataAnalyzer:
    def __init__(self, data):
        self.data = data
        self.mean = self._compute_mean()  # Always computed
        self.std = self._compute_std()    # Even if never used!

# GOOD: Computes only when accessed
class DataAnalyzer:
    def __init__(self, data):
        self.data = data
        self._mean = None
        self._std = None

    @property
    def mean(self):
        if self._mean is None:
            self._mean = self._compute_mean()
        return self._mean

    @property
    def std(self):
        if self._std is None:
            self._std = self._compute_std()
        return self._std

# Memory savings: Only stores computed values that are used
```

## Common Pitfalls

### Pitfall 1: Circular References with __del__

Circular references prevent `__del__` from being called, causing memory leaks.

```python
# PROBLEM: Circular reference prevents cleanup
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __del__(self):
        print(f"Deleting {self.value}")  # Never called!

node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1  # Circular!

del node1, node2  # __del__ not called due to cycle

# SOLUTION 1: Use weak references
import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._next = None

    @property
    def next(self):
        return self._next() if self._next else None

    @next.setter
    def next(self, node):
        self._next = weakref.ref(node) if node else None

# SOLUTION 2: Explicitly break cycles
def cleanup_nodes(node1, node2):
    node1.next = None
    node2.next = None
    del node1, node2

# SOLUTION 3: Let garbage collector handle it
import gc
del node1, node2
gc.collect()  # Cleans up circular references
```

### Pitfall 2: Hidden References in Closures

Closures can keep references to objects you think you've deleted.

```python
# PROBLEM: Closure keeps reference
def create_callbacks():
    large_data = [i for i in range(1000000)]

    def callback():
        return len(large_data)  # Keeps large_data alive!

    return callback

cb = create_callbacks()
# large_data still in memory because callback references it!

# SOLUTION 1: Extract only what you need
def create_callbacks():
    large_data = [i for i in range(1000000)]
    data_len = len(large_data)  # Extract value

    def callback():
        return data_len  # Only small int in closure

    return callback

# SOLUTION 2: Delete after use
def create_callbacks():
    large_data = [i for i in range(1000000)]
    result = process(large_data)
    del large_data  # Explicit deletion

    def callback():
        return result

    return callback
```

### Pitfall 3: Mutable Default Arguments

Mutable defaults are shared between all calls, causing unexpected memory growth.

```python
# PROBLEM: Shared mutable default
def add_item(item, items=[]):  # BAD!
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - Unexpected!
# List keeps growing in memory

# SOLUTION: Use None as default
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [2] - Correct!
```

### Pitfall 4: Keeping References in Exception Handlers

Exception tracebacks can keep large objects alive.

```python
# PROBLEM: Traceback keeps references
def process_data():
    large_data = [i for i in range(1000000)]
    try:
        result = risky_operation(large_data)
    except Exception as e:
        log_error(e)  # Traceback keeps large_data alive!
        raise

# SOLUTION: Clear references explicitly
def process_data():
    large_data = [i for i in range(1000000)]
    try:
        result = risky_operation(large_data)
    except Exception as e:
        log_error(e)
        large_data = None  # Explicit clear
        raise
    finally:
        large_data = None  # Or in finally block

# SOLUTION 2: Use del in Python 3
def process_data():
    large_data = [i for i in range(1000000)]
    try:
        result = risky_operation(large_data)
    except Exception as e:
        log_error(e)
        raise
    finally:
        del large_data  # Ensures cleanup
```

### Pitfall 5: Global Variables and Module-Level Collections

Global collections that grow indefinitely cause memory leaks.

```python
# PROBLEM: Global cache grows forever
CACHE = {}  # Never cleaned up!

def get_data(key):
    if key not in CACHE:
        CACHE[key] = expensive_computation(key)
    return CACHE[key]

# Over time, CACHE grows without bound

# SOLUTION 1: Use LRU cache with size limit
from functools import lru_cache

@lru_cache(maxsize=1000)  # Limits size
def get_data(key):
    return expensive_computation(key)

# SOLUTION 2: Use weak references
import weakref

CACHE = weakref.WeakValueDictionary()

# SOLUTION 3: Manual cleanup
from collections import OrderedDict

CACHE = OrderedDict()
MAX_CACHE_SIZE = 1000

def get_data(key):
    if key not in CACHE:
        if len(CACHE) >= MAX_CACHE_SIZE:
            CACHE.popitem(last=False)  # Remove oldest
        CACHE[key] = expensive_computation(key)
    return CACHE[key]
```

## Performance Considerations

### Performance Tip 1: Batch Allocations

Allocating many small objects is slower and uses more memory than batch allocation.

```python
# SLOW: Many small allocations
result = []
for i in range(1000000):
    result.append(i)  # Many reallocs

# FAST: Pre-allocate
result = [0] * 1000000
for i in range(1000000):
    result[i] = i

# FASTEST: List comprehension (single allocation)
result = [i for i in range(1000000)]

# Memory overhead comparison:
# Many appends: ~2x memory during growth
# Pre-allocate: Exact size needed
# Comprehension: Optimized by interpreter
```

### Performance Tip 2: Use Memory Views for Large Buffers

Memory views provide zero-copy slicing for large data.

```python
import array

# BAD: Creates copies
data = array.array('i', range(1000000))
slice1 = data[100:200]  # Copies 100 elements
slice2 = data[200:300]  # Copies 100 elements

# GOOD: No copying
data = array.array('i', range(1000000))
view = memoryview(data)
slice1 = view[100:200]  # No copy!
slice2 = view[200:300]  # No copy!

# Modify through view
data_bytes = bytearray(b'Hello World')
view = memoryview(data_bytes)
view[0:5] = b'HELLO'
print(data_bytes)  # bytearray(b'HELLO World')

# Use cases:
# - Large binary data
# - Image/audio processing
# - Network buffers
# - File I/O
```

### Performance Tip 3: Object Pooling for Frequent Creation/Destruction

Reuse objects instead of creating new ones when possible.

```python
# Pattern: Object pooling
class ObjectPool:
    def __init__(self, factory, size=10):
        self.factory = factory
        self.pool = [factory() for _ in range(size)]
        self.available = self.pool.copy()

    def acquire(self):
        if self.available:
            return self.available.pop()
        return self.factory()  # Create new if empty

    def release(self, obj):
        obj.reset()  # Clear state
        self.available.append(obj)

# Use for:
# - Database connections
# - Thread pools
# - Buffer objects
# - Expensive resource allocations

# Benchmark:
# Without pooling: 100k allocations = 2.5s, 500MB
# With pooling:    100k reuses = 0.3s, 50MB
```

## Profiling Workflow

### Step 1: Identify Memory Hotspots

```python
import tracemalloc

# Take snapshots at key points
tracemalloc.start()

snapshot1 = tracemalloc.take_snapshot()

# Code to profile
data = load_large_dataset()
process_data(data)

snapshot2 = tracemalloc.take_snapshot()

# Compare
top_stats = snapshot2.compare_to(snapshot1, 'lineno')

print("Top 10 memory increases:")
for stat in top_stats[:10]:
    print(stat)
```

### Step 2: Analyze Object Counts

```python
import gc
from collections import defaultdict

def count_objects():
    """Count objects by type"""
    counts = defaultdict(int)
    for obj in gc.get_objects():
        counts[type(obj).__name__] += 1
    return counts

# Before
before = count_objects()

# Your code
create_many_objects()

# After
after = count_objects()

# Compare
for obj_type in set(before.keys()) | set(after.keys()):
    diff = after[obj_type] - before[obj_type]
    if diff > 0:
        print(f"{obj_type}: +{diff}")
```

### Step 3: Find Memory Leaks

```python
import gc
import tracemalloc

class LeakDetector:
    def __init__(self):
        self.snapshots = []

    def snapshot(self):
        gc.collect()
        self.snapshots.append(tracemalloc.take_snapshot())

    def analyze(self):
        if len(self.snapshots) < 2:
            return

        # Compare first and last
        stats = self.snapshots[-1].compare_to(
            self.snapshots[0], 'lineno'
        )

        print("Potential memory leaks:")
        for stat in stats[:10]:
            if stat.size_diff > 0:
                print(f"{stat}")

# Usage:
detector = LeakDetector()

detector.snapshot()
# Run your code multiple times
for _ in range(100):
    potentially_leaky_function()
detector.snapshot()

detector.analyze()
```

## Optimization Strategies

### Strategy 1: Use Iterators and Generators

```python
# Memory-efficient data pipeline
def read_large_file(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()

def parse_lines(lines):
    for line in lines:
        if line:
            yield line.split(',')

def filter_valid(rows):
    for row in rows:
        if len(row) >= 3:
            yield row

# Chained pipeline (constant memory)
pipeline = filter_valid(
    parse_lines(
        read_large_file('huge.csv')
    )
)

for row in pipeline:
    process(row)
```

### Strategy 2: Implement Custom Memory Management

```python
class MemoryManagedList:
    """List that enforces memory limits"""

    def __init__(self, max_memory_mb=100):
        self.items = []
        self.max_memory = max_memory_mb * 1024 * 1024

    def append(self, item):
        import sys

        item_size = sys.getsizeof(item)
        current_size = sum(sys.getsizeof(i) for i in self.items)

        if current_size + item_size > self.max_memory:
            # Evict oldest items
            while current_size + item_size > self.max_memory:
                evicted = self.items.pop(0)
                current_size -= sys.getsizeof(evicted)

        self.items.append(item)

    def __len__(self):
        return len(self.items)
```

### Strategy 3: Use Slots Judiciously

```python
# When __slots__ helps most:
class Particle:
    __slots__ = ['x', 'y', 'vx', 'vy', 'mass']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.mass = 1.0

# Create millions of particles
particles = [Particle(i, i) for i in range(1000000)]

# Savings: ~60% memory compared to regular class
# 1M objects: 88MB (slots) vs 220MB (dict)
```

## Key Takeaways

1. **Measure before optimizing** - Use profiling tools to identify real issues
2. **Choose appropriate data structures** - array.array, tuple, and generators can save significant memory
3. **Use weak references** - For caches, observers, and parent references
4. **Prefer generators** - For large sequences and data pipelines
5. **Apply __slots__** - When creating many instances of a class
6. **Break circular references** - Use weak refs or explicit cleanup
7. **Lazy evaluation** - Compute expensive values only when needed
8. **Profile continuously** - Memory issues compound over time
9. **Use context managers** - For reliable resource cleanup
10. **Batch operations** - Reduce allocation overhead with bulk operations
