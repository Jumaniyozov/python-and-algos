# Theory: Memory Management

## Introduction

Memory management in Python is automatic but understanding how it works enables you to write more efficient code, debug memory leaks, and optimize performance-critical applications.

## Core Concepts

### 1. Reference Counting

**Overview**: Python's primary memory management mechanism. Each object tracks how many references point to it.

**Key Points**:
- Every object has a reference count
- Count increases when assigned to variable, passed to function, or added to container
- Count decreases when references are deleted or go out of scope
- Object is deallocated when count reaches zero

**Example**:
```python
import sys

# Create object
x = [1, 2, 3]
print(sys.getrefcount(x))  # 2 (x + getrefcount's argument)

# Add reference
y = x
print(sys.getrefcount(x))  # 3

# Remove reference
del y
print(sys.getrefcount(x))  # 2

# Multiple references
container = [x, x, x]
print(sys.getrefcount(x))  # 5 (x + 3 in container + getrefcount)
```

**Caveats**:
- Cannot handle circular references alone
- Thread-safe but adds overhead (GIL)
- Immediate deallocation for most objects

### 2. Garbage Collection

**Overview**: Supplements reference counting by detecting and cleaning up circular references using generational garbage collection.

**Key Points**:
- Three generations (0, 1, 2) based on object age
- Generation 0: newly created objects
- Objects surviving collection promoted to next generation
- Older generations collected less frequently
- Can be controlled with `gc` module

**Example**:
```python
import gc

# Check current thresholds
print(gc.get_threshold())  # (700, 10, 10)

# Get collection stats
print(gc.get_count())  # (current counts for each generation)

# Force collection
collected = gc.collect()
print(f"Collected {collected} objects")

# Disable/enable
gc.disable()
gc.enable()

# Check if object is tracked
class MyClass:
    pass

obj = MyClass()
print(gc.is_tracked(obj))  # True for most objects
```

**Circular References**:
```python
import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create circular reference
a = Node(1)
b = Node(2)
a.next = b
b.next = a  # Circular!

# Delete variables but objects remain in memory
del a, b

# Garbage collector cleans them up
gc.collect()
```

### 3. Weak References

**Overview**: References that don't increase reference count, allowing objects to be garbage collected even when weak references exist.

**Key Points**:
- Use `weakref` module
- Callbacks when object is about to be destroyed
- Useful for caches, observer patterns, parent-child relationships
- Cannot be created for all object types

**Example**:
```python
import weakref

class ExpensiveResource:
    def __init__(self, name):
        self.name = name
        print(f"Created {name}")

    def __del__(self):
        print(f"Deleted {self.name}")

# Strong reference
obj = ExpensiveResource("Strong")

# Weak reference doesn't prevent deletion
weak = weakref.ref(obj)
print(weak())  # <ExpensiveResource object>

# When strong reference deleted, object dies
del obj  # Prints "Deleted Strong"
print(weak())  # None

# WeakValueDictionary for caches
cache = weakref.WeakValueDictionary()
```

**Use Cases**:
- Caches that don't prevent garbage collection
- Observer/subscriber patterns
- Parent references in tree structures

### 4. `__slots__`

**Overview**: Class attribute that restricts instance attributes to a fixed set, reducing memory overhead.

**Key Points**:
- Replaces instance `__dict__` with fixed-size structure
- Reduces memory per instance (typically 40-50%)
- Faster attribute access
- Cannot add new attributes dynamically
- Doesn't work well with multiple inheritance

**Example**:
```python
import sys

class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Memory comparison
without = WithoutSlots(1, 2)
with_slots = WithSlots(1, 2)

print(f"Without __slots__: {sys.getsizeof(without)} bytes")
print(f"With __slots__: {sys.getsizeof(with_slots)} bytes")

# __slots__ instance has no __dict__
print(hasattr(without, '__dict__'))  # True
print(hasattr(with_slots, '__dict__'))  # False
```

**When to Use**:
- Creating many instances of a class
- Memory is constrained
- Attributes are known in advance
- Don't need dynamic attributes

### 5. Memory Views

**Overview**: Allow direct access to memory buffer without copying, useful for large data manipulation.

**Key Points**:
- Zero-copy access to array data
- Supports slicing without copying
- Works with bytes, bytearray, array
- Faster for large data operations

**Example**:
```python
# Without memoryview - creates copies
data = bytearray(b'Hello World')
slice1 = data[0:5]  # Copies data

# With memoryview - no copy
data = bytearray(b'Hello World')
view = memoryview(data)
slice2 = view[0:5]  # No copy, just a view

# Modify through view
view[0:5] = b'HELLO'
print(data)  # bytearray(b'HELLO World')

# Convert to different formats
import array
numbers = array.array('i', [1, 2, 3, 4])
view = memoryview(numbers)
print(view.tobytes())
```

### 6. Memory Profiling Tools

**Overview**: Tools to measure and optimize memory usage.

**sys.getsizeof()**:
```python
import sys

x = [1, 2, 3]
print(sys.getsizeof(x))  # Size of list object

# Note: doesn't include size of referenced objects
y = [[1,2,3], [4,5,6]]
print(sys.getsizeof(y))  # Only list itself, not nested lists
```

**tracemalloc**:
```python
import tracemalloc

# Start tracing
tracemalloc.start()

# Code to profile
data = [list(range(1000)) for _ in range(100)]

# Get memory snapshot
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

# Display top consumers
for stat in top_stats[:5]:
    print(stat)

# Stop tracing
tracemalloc.stop()
```

**memory_profiler** (external package):
```python
from memory_profiler import profile

@profile
def memory_intensive():
    big_list = [0] * (10 ** 6)
    return sum(big_list)

memory_intensive()
# Shows line-by-line memory usage
```

### 7. Object Pooling

**Overview**: Reuse objects instead of creating new ones to reduce allocation overhead.

**Key Points**:
- Useful for frequently created/destroyed objects
- Reduces garbage collection pressure
- Trade memory for speed
- Must handle object state carefully

**Example**:
```python
class ObjectPool:
    def __init__(self, obj_class, size=10):
        self.obj_class = obj_class
        self.pool = [obj_class() for _ in range(size)]
        self.available = self.pool.copy()

    def acquire(self):
        if self.available:
            return self.available.pop()
        return self.obj_class()  # Create new if pool empty

    def release(self, obj):
        obj.reset()  # Must implement reset
        self.available.append(obj)

class Reusable:
    def __init__(self):
        self.value = 0

    def reset(self):
        self.value = 0

# Usage
pool = ObjectPool(Reusable)
obj = pool.acquire()
obj.value = 42
pool.release(obj)
```

## Summary

Understanding Python's memory management helps you:
- Write memory-efficient code
- Debug memory leaks
- Optimize performance-critical applications
- Choose appropriate data structures
- Use profiling tools effectively

## Key Takeaways

1. **Reference Counting**: Primary mechanism, immediate but can't handle cycles
2. **Garbage Collection**: Handles circular references, generational approach
3. **Weak References**: Enable caches and observer patterns without memory leaks
4. **__slots__**: Reduce memory for classes with many instances
5. **Memory Views**: Zero-copy operations for large data
6. **Profiling**: Use tracemalloc and memory_profiler to find issues
7. **Object Pooling**: Reuse objects to reduce allocation overhead
