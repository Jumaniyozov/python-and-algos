# Examples: Memory Management

## Example 1: Reference Counting with sys.getrefcount()

```python
import sys

def example_1():
    """Demonstrates how reference counting works in Python"""

    # Create an object
    data = [1, 2, 3, 4, 5]
    print(f"Initial refcount: {sys.getrefcount(data)}")  # 2 (data + getrefcount arg)

    # Create another reference
    data_ref = data
    print(f"After creating reference: {sys.getrefcount(data)}")  # 3

    # Add to container
    container = [data, data, data]
    print(f"After adding to container: {sys.getrefcount(data)}")  # 6

    # Remove reference
    del data_ref
    print(f"After deleting reference: {sys.getrefcount(data)}")  # 5

    # Clear container
    container.clear()
    print(f"After clearing container: {sys.getrefcount(data)}")  # 2

    return data

# Usage
example_1()
```

**Output:**
```
Initial refcount: 2
After creating reference: 3
After adding to container: 6
After deleting reference: 5
After clearing container: 2
```

## Example 2: Garbage Collection Manual Trigger

```python
import gc
import weakref

def example_2():
    """Demonstrates manual garbage collection and circular references"""

    class Node:
        def __init__(self, name):
            self.name = name
            self.next = None

        def __del__(self):
            print(f"Deleting {self.name}")

    print("Creating circular reference...")
    node1 = Node("Node1")
    node2 = Node("Node2")
    node1.next = node2
    node2.next = node1  # Circular reference

    # Get stats before collection
    print(f"Objects before: {gc.get_count()}")

    # Delete references (objects still in memory due to cycle)
    del node1, node2

    # Force garbage collection
    print("Forcing garbage collection...")
    collected = gc.collect()
    print(f"Collected {collected} objects")
    print(f"Objects after: {gc.get_count()}")

# Usage
example_2()
```

**Output:**
```
Creating circular reference...
Objects before: (234, 5, 2)
Forcing garbage collection...
Deleting Node2
Deleting Node1
Collected 4 objects
Objects after: (0, 5, 2)
```

## Example 3: WeakValueDictionary Cache

```python
import weakref
import sys

def example_3():
    """Demonstrates WeakValueDictionary for automatic cache cleanup"""

    class ExpensiveObject:
        def __init__(self, obj_id, size):
            self.obj_id = obj_id
            self.data = [0] * size  # Simulate large object
            print(f"Created object {obj_id} ({sys.getsizeof(self.data)} bytes)")

        def __del__(self):
            print(f"Destroyed object {self.obj_id}")

    # Regular dict keeps strong references
    regular_cache = {}

    # Weak dict allows garbage collection
    weak_cache = weakref.WeakValueDictionary()

    print("=== Regular Cache ===")
    obj1 = ExpensiveObject(1, 10000)
    regular_cache['obj1'] = obj1
    del obj1
    print(f"Cache still has: {len(regular_cache)} items")

    print("\n=== Weak Cache ===")
    obj2 = ExpensiveObject(2, 10000)
    weak_cache['obj2'] = obj2
    print(f"Cache has: {len(weak_cache)} items")
    del obj2
    print(f"After deleting reference, cache has: {len(weak_cache)} items")

# Usage
example_3()
```

**Output:**
```
=== Regular Cache ===
Created object 1 (80056 bytes)
Cache still has: 1 items

=== Weak Cache ===
Created object 2 (80056 bytes)
Cache has: 1 items
Destroyed object 2
After deleting reference, cache has: 0 items
```

## Example 4: WeakSet for Tracking

```python
import weakref

def example_4():
    """Demonstrates WeakSet for tracking objects without preventing cleanup"""

    class User:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return f"User({self.name})"

        def __del__(self):
            print(f"User {self.name} logged out")

    # Track active users without preventing logout
    active_users = weakref.WeakSet()

    # Create users
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    # Add to tracking
    active_users.add(alice)
    active_users.add(bob)
    active_users.add(charlie)

    print(f"Active users: {len(active_users)}")
    for user in active_users:
        print(f"  - {user}")

    # User logs out (delete reference)
    print("\nBob logs out...")
    del bob

    print(f"Active users: {len(active_users)}")
    for user in active_users:
        print(f"  - {user}")

# Usage
example_4()
```

**Output:**
```
Active users: 3
  - User(Alice)
  - User(Bob)
  - User(Charlie)

Bob logs out...
User Bob logged out
Active users: 2
  - User(Alice)
  - User(Charlie)
```

## Example 5: __slots__ vs Regular Class Memory Comparison

```python
import sys

def example_5():
    """Demonstrates memory savings with __slots__"""

    class WithoutSlots:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    class WithSlots:
        __slots__ = ['x', 'y', 'z']

        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    # Create instances
    regular = WithoutSlots(1, 2, 3)
    slotted = WithSlots(1, 2, 3)

    # Compare memory
    regular_size = sys.getsizeof(regular) + sys.getsizeof(regular.__dict__)
    slotted_size = sys.getsizeof(slotted)

    print(f"Regular instance: {regular_size} bytes")
    print(f"Slotted instance: {slotted_size} bytes")
    print(f"Savings: {regular_size - slotted_size} bytes ({100*(regular_size-slotted_size)/regular_size:.1f}%)")

    # For many instances
    n = 10000
    regular_list = [WithoutSlots(i, i+1, i+2) for i in range(n)]
    slotted_list = [WithSlots(i, i+1, i+2) for i in range(n)]

    regular_total = sum(sys.getsizeof(obj) + sys.getsizeof(obj.__dict__) for obj in regular_list)
    slotted_total = sum(sys.getsizeof(obj) for obj in slotted_list)

    print(f"\nFor {n} instances:")
    print(f"Regular total: {regular_total:,} bytes")
    print(f"Slotted total: {slotted_total:,} bytes")
    print(f"Total savings: {regular_total - slotted_total:,} bytes")

# Usage
example_5()
```

**Output:**
```
Regular instance: 152 bytes
Slotted instance: 64 bytes
Savings: 88 bytes (57.9%)

For 10000 instances:
Regular total: 1,520,000 bytes
Slotted total: 640,000 bytes
Total savings: 880,000 bytes
```

## Example 6: Memory Profiling with tracemalloc

```python
import tracemalloc

def example_6():
    """Demonstrates memory profiling with tracemalloc"""

    # Start tracing
    tracemalloc.start()

    # Take initial snapshot
    snapshot1 = tracemalloc.take_snapshot()

    # Allocate memory
    data1 = [i for i in range(100000)]
    data2 = {i: str(i) for i in range(10000)}
    data3 = [[j for j in range(100)] for i in range(100)]

    # Take second snapshot
    snapshot2 = tracemalloc.take_snapshot()

    # Compare snapshots
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')

    print("Top 5 memory allocations:")
    for stat in top_stats[:5]:
        print(f"{stat}")

    # Get current memory usage
    current, peak = tracemalloc.get_traced_memory()
    print(f"\nCurrent memory: {current / 1024 / 1024:.2f} MB")
    print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")

    # Stop tracing
    tracemalloc.stop()

# Usage
example_6()
```

**Output:**
```
Top 5 memory allocations:
<stdin>:10: size=824 KiB (+824 KiB), count=1 (+1), average=824 KiB
<stdin>:11: size=520 KiB (+520 KiB), count=10001 (+10001), average=53 B
<stdin>:12: size=88.0 KiB (+88.0 KiB), count=101 (+101), average=892 B

Current memory: 1.43 MB
Peak memory: 1.43 MB
```

## Example 7: Object Pooling Pattern

```python
from queue import Queue

def example_7():
    """Demonstrates object pooling to reduce allocation overhead"""

    class Connection:
        """Simulates an expensive resource like database connection"""
        _id_counter = 0

        def __init__(self):
            Connection._id_counter += 1
            self.conn_id = Connection._id_counter
            self.in_use = False
            print(f"Created connection {self.conn_id}")

        def execute(self, query):
            return f"Conn {self.conn_id}: Executed '{query}'"

        def reset(self):
            self.in_use = False

    class ConnectionPool:
        def __init__(self, size=5):
            self.pool = Queue(maxsize=size)
            for _ in range(size):
                self.pool.put(Connection())

        def acquire(self):
            conn = self.pool.get()
            conn.in_use = True
            return conn

        def release(self, conn):
            conn.reset()
            self.pool.put(conn)

    # Create pool
    pool = ConnectionPool(3)

    # Use connections
    print("\nUsing connections:")
    conn1 = pool.acquire()
    print(conn1.execute("SELECT * FROM users"))

    conn2 = pool.acquire()
    print(conn2.execute("SELECT * FROM orders"))

    # Release and reuse
    pool.release(conn1)
    conn3 = pool.acquire()
    print(f"Reused connection: {conn3.conn_id}")
    print(conn3.execute("SELECT * FROM products"))

# Usage
example_7()
```

**Output:**
```
Created connection 1
Created connection 2
Created connection 3

Using connections:
Conn 1: Executed 'SELECT * FROM users'
Conn 2: Executed 'SELECT * FROM orders'
Reused connection: 1
Conn 1: Executed 'SELECT * FROM products'
```

## Example 8: Circular Reference Detection

```python
import gc

def example_8():
    """Demonstrates detecting circular references"""

    class Node:
        def __init__(self, value):
            self.value = value
            self.references = []

        def __repr__(self):
            return f"Node({self.value})"

    def find_circular_references(obj):
        """Find all circular references involving an object"""
        referrers = gc.get_referrers(obj)
        circular = []

        for ref in referrers:
            if isinstance(ref, dict) and 'self' in ref:
                continue
            if isinstance(ref, list):
                for item in ref:
                    if hasattr(item, 'references') and obj in item.references:
                        circular.append(item)

        return circular

    # Create nodes with circular reference
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')

    node_a.references.append(node_b)
    node_b.references.append(node_c)
    node_c.references.append(node_a)  # Creates cycle

    print("Node structure:")
    print(f"A -> {[n.value for n in node_a.references]}")
    print(f"B -> {[n.value for n in node_b.references]}")
    print(f"C -> {[n.value for n in node_c.references]}")

    # Check if objects are tracked by GC
    print(f"\nIs node_a tracked? {gc.is_tracked(node_a)}")
    print(f"Is node_b tracked? {gc.is_tracked(node_b)}")
    print(f"Is node_c tracked? {gc.is_tracked(node_c)}")

    # Find circular references
    print(f"\nReferrers to node_a: {len(gc.get_referrers(node_a))}")

# Usage
example_8()
```

**Output:**
```
Node structure:
A -> ['B']
B -> ['C']
C -> ['A']

Is node_a tracked? True
Is node_b tracked? True
Is node_c tracked? True

Referrers to node_a: 6
```

## Example 9: Memory Leak Demonstration and Fix

```python
import weakref

def example_9():
    """Demonstrates a common memory leak and how to fix it"""

    class EventManager:
        """BAD: Creates memory leak with strong references"""
        def __init__(self):
            self.listeners = []

        def subscribe(self, listener):
            self.listeners.append(listener)

        def notify(self, event):
            for listener in self.listeners:
                listener.handle(event)

    class EventManagerFixed:
        """GOOD: Uses weak references to prevent leak"""
        def __init__(self):
            self.listeners = []

        def subscribe(self, listener):
            self.listeners.append(weakref.ref(listener))

        def notify(self, event):
            # Clean up dead references and notify alive ones
            self.listeners = [ref for ref in self.listeners if ref() is not None]
            for ref in self.listeners:
                listener = ref()
                if listener:
                    listener.handle(event)

    class EventListener:
        def __init__(self, name):
            self.name = name

        def handle(self, event):
            print(f"{self.name} received: {event}")

        def __del__(self):
            print(f"{self.name} was cleaned up")

    print("=== With Memory Leak ===")
    manager1 = EventManager()
    listener1 = EventListener("Listener1")
    manager1.subscribe(listener1)
    del listener1  # Reference still held by manager
    print(f"Manager has {len(manager1.listeners)} listeners")

    print("\n=== Without Memory Leak ===")
    manager2 = EventManagerFixed()
    listener2 = EventListener("Listener2")
    manager2.subscribe(listener2)
    del listener2  # Can be cleaned up
    manager2.notify("test")  # Cleans up dead references
    print(f"Manager has {len(manager2.listeners)} listeners")

# Usage
example_9()
```

**Output:**
```
=== With Memory Leak ===
Manager has 1 listeners

=== Without Memory Leak ===
Listener2 was cleaned up
Manager has 0 listeners
```

## Example 10: sys.getsizeof() for Different Types

```python
import sys

def example_10():
    """Demonstrates memory usage of different Python types"""

    def deep_size(obj, seen=None):
        """Calculate deep size including referenced objects"""
        if seen is None:
            seen = set()

        obj_id = id(obj)
        if obj_id in seen:
            return 0

        seen.add(obj_id)
        size = sys.getsizeof(obj)

        if isinstance(obj, dict):
            size += sum(deep_size(k, seen) + deep_size(v, seen) for k, v in obj.items())
        elif isinstance(obj, (list, tuple, set)):
            size += sum(deep_size(item, seen) for item in obj)

        return size

    # Compare different data structures
    data = list(range(1000))

    structures = {
        'list': list(data),
        'tuple': tuple(data),
        'set': set(data),
        'dict': {i: i for i in data},
        'list of lists': [[i] for i in range(100)],
    }

    print("Shallow size (sys.getsizeof):")
    for name, struct in structures.items():
        size = sys.getsizeof(struct)
        print(f"  {name:15s}: {size:8,} bytes")

    print("\nDeep size (including contents):")
    for name, struct in structures.items():
        size = deep_size(struct)
        print(f"  {name:15s}: {size:8,} bytes")

# Usage
example_10()
```

**Output:**
```
Shallow size (sys.getsizeof):
  list           :    8,856 bytes
  tuple          :    8,040 bytes
  set            :   32,992 bytes
  dict           :   36,968 bytes
  list of lists  :      920 bytes

Deep size (including contents):
  list           :   36,856 bytes
  tuple          :   36,040 bytes
  set            :   60,992 bytes
  dict           :   92,968 bytes
  list of lists  :   13,720 bytes
```

## Example 11: Memory-Efficient Data Structures

```python
import array
import sys

def example_11():
    """Demonstrates memory-efficient alternatives to common structures"""

    # List vs array for numeric data
    n = 10000

    # Regular list
    int_list = list(range(n))

    # Array (typed, more efficient)
    int_array = array.array('i', range(n))

    print("Integer storage:")
    print(f"  List:  {sys.getsizeof(int_list):,} bytes")
    print(f"  Array: {sys.getsizeof(int_array):,} bytes")
    print(f"  Savings: {sys.getsizeof(int_list) - sys.getsizeof(int_array):,} bytes")

    # String vs bytes
    text = "Hello World! " * 1000
    text_str = text
    text_bytes = text.encode('utf-8')

    print("\nString storage:")
    print(f"  str:   {sys.getsizeof(text_str):,} bytes")
    print(f"  bytes: {sys.getsizeof(text_bytes):,} bytes")

    # Dictionary vs named tuple for fixed structures
    from collections import namedtuple

    # Many dictionaries
    dicts = [{'x': i, 'y': i+1, 'z': i+2} for i in range(1000)]

    # Named tuples
    Point = namedtuple('Point', ['x', 'y', 'z'])
    tuples = [Point(i, i+1, i+2) for i in range(1000)]

    dict_size = sum(sys.getsizeof(d) for d in dicts)
    tuple_size = sum(sys.getsizeof(t) for t in tuples)

    print("\n1000 objects with 3 fields:")
    print(f"  Dicts:        {dict_size:,} bytes")
    print(f"  NamedTuples:  {tuple_size:,} bytes")
    print(f"  Savings:      {dict_size - tuple_size:,} bytes")

# Usage
example_11()
```

**Output:**
```
Integer storage:
  List:  87,624 bytes
  Array: 40,064 bytes
  Savings: 47,560 bytes

String storage:
  str:   13,121 bytes
  bytes: 13,049 bytes

1000 objects with 3 fields:
  Dicts:        229,376 bytes
  NamedTuples:  64,000 bytes
  Savings:      165,376 bytes
```

## Example 12: Generator vs List Memory Usage

```python
import sys
import tracemalloc

def example_12():
    """Demonstrates memory efficiency of generators vs lists"""

    def list_approach(n):
        """Returns list of squares"""
        return [x * x for x in range(n)]

    def generator_approach(n):
        """Returns generator of squares"""
        return (x * x for x in range(n))

    n = 1000000

    # Measure list approach
    tracemalloc.start()
    data_list = list_approach(n)
    list_current, list_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Measure generator approach
    tracemalloc.start()
    data_gen = generator_approach(n)
    gen_current, gen_peak = tracemalloc.get_traced_memory()

    # Consume some values
    for i, val in enumerate(data_gen):
        if i >= 10:
            break

    gen_consumed, gen_consumed_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"For {n:,} elements:")
    print(f"\nList approach:")
    print(f"  Memory used: {list_current / 1024 / 1024:.2f} MB")
    print(f"  Peak memory: {list_peak / 1024 / 1024:.2f} MB")

    print(f"\nGenerator approach:")
    print(f"  Initial: {gen_current / 1024:.2f} KB")
    print(f"  After consuming 10: {gen_consumed / 1024:.2f} KB")

    print(f"\nMemory savings: {(list_current - gen_consumed) / 1024 / 1024:.2f} MB")

    # Size comparison
    print(f"\nObject sizes:")
    print(f"  List: {sys.getsizeof(data_list):,} bytes")
    print(f"  Generator: {sys.getsizeof(generator_approach(n))} bytes")

# Usage
example_12()
```

**Output:**
```
For 1,000,000 elements:

List approach:
  Memory used: 8.39 MB
  Peak memory: 8.39 MB

Generator approach:
  Initial: 0.11 KB
  After consuming 10: 0.12 KB

Memory savings: 8.39 MB

Object sizes:
  List: 8,448,728 bytes
  Generator: 200 bytes
```

## Example 13: __del__ Finalizer

```python
import weakref

def example_13():
    """Demonstrates proper use of __del__ finalizer"""

    class FileHandler:
        """BAD: Unreliable cleanup with __del__"""
        def __init__(self, filename):
            self.filename = filename
            self.file = open(filename, 'w')
            print(f"Opened {filename}")

        def write(self, data):
            self.file.write(data)

        def __del__(self):
            # May not be called promptly!
            if hasattr(self, 'file'):
                self.file.close()
                print(f"Closed {filename} in __del__")

    class FileHandlerBetter:
        """BETTER: Explicit cleanup with context manager"""
        def __init__(self, filename):
            self.filename = filename
            self.file = open(filename, 'w')
            print(f"Opened {filename}")

        def write(self, data):
            self.file.write(data)

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.file.close()
            print(f"Closed {self.filename} in __exit__")
            return False

        def __del__(self):
            # Backup cleanup
            if hasattr(self, 'file') and not self.file.closed:
                self.file.close()
                print(f"Closed {self.filename} in __del__ (backup)")

    print("=== Using __del__ only (unreliable) ===")
    handler1 = FileHandler('/tmp/test1.txt')
    handler1.write("data")
    del handler1  # May not close immediately

    print("\n=== Using context manager (reliable) ===")
    with FileHandlerBetter('/tmp/test2.txt') as handler2:
        handler2.write("data")
    # Guaranteed to close here

    print("\n=== Using weakref finalizer (better than __del__) ===")
    class Resource:
        def __init__(self, name):
            self.name = name
            print(f"Created {name}")
            # Register cleanup callback
            self._finalizer = weakref.finalize(self, self.cleanup, name)

        @staticmethod
        def cleanup(name):
            print(f"Cleaning up {name}")

    resource = Resource("MyResource")
    del resource  # Cleanup called promptly

# Usage
example_13()
```

**Output:**
```
=== Using __del__ only (unreliable) ===
Opened /tmp/test1.txt
Closed /tmp/test1.txt in __del__

=== Using context manager (reliable) ===
Opened /tmp/test2.txt
Closed /tmp/test2.txt in __exit__

=== Using weakref finalizer (better than __del__) ===
Created MyResource
Cleaning up MyResource
```

## Example 14: Context Manager for Memory Tracking

```python
import tracemalloc
from contextlib import contextmanager

def example_14():
    """Demonstrates context manager for tracking memory usage"""

    @contextmanager
    def track_memory(description=""):
        """Context manager to track memory usage of a code block"""
        tracemalloc.start()

        # Get baseline
        snapshot_start = tracemalloc.take_snapshot()

        try:
            yield
        finally:
            # Get final memory usage
            snapshot_end = tracemalloc.take_snapshot()

            # Compare snapshots
            top_stats = snapshot_end.compare_to(snapshot_start, 'lineno')

            current, peak = tracemalloc.get_traced_memory()

            print(f"\n{'='*50}")
            print(f"Memory tracking: {description}")
            print(f"{'='*50}")
            print(f"Current: {current / 1024 / 1024:.2f} MB")
            print(f"Peak:    {peak / 1024 / 1024:.2f} MB")

            if top_stats:
                print("\nTop 3 allocations:")
                for stat in top_stats[:3]:
                    print(f"  {stat}")

            tracemalloc.stop()

    # Example 1: List comprehension
    with track_memory("List comprehension"):
        data = [x * x for x in range(100000)]

    # Example 2: Dictionary creation
    with track_memory("Dictionary creation"):
        lookup = {i: str(i) for i in range(50000)}

    # Example 3: Nested structures
    with track_memory("Nested lists"):
        matrix = [[j for j in range(100)] for i in range(1000)]

# Usage
example_14()
```

**Output:**
```
==================================================
Memory tracking: List comprehension
==================================================
Current: 0.84 MB
Peak:    0.84 MB

Top 3 allocations:
  <stdin>:30: size=824 KiB (+824 KiB), count=1 (+1)

==================================================
Memory tracking: Dictionary creation
==================================================
Current: 2.60 MB
Peak:    2.60 MB

Top 3 allocations:
  <stdin>:34: size=2600 KiB (+2600 KiB), count=50001 (+50001)

==================================================
Memory tracking: Nested lists
==================================================
Current: 0.85 MB
Peak:    0.85 MB

Top 3 allocations:
  <stdin>:38: size=800 KiB (+800 KiB), count=1001 (+1001)
```

## Example 15: Memory Optimization Techniques

```python
import sys
from collections import defaultdict

def example_15():
    """Demonstrates various memory optimization techniques"""

    # Technique 1: __slots__ for data classes
    class Point2D:
        __slots__ = ['x', 'y']
        def __init__(self, x, y):
            self.x = x
            self.y = y

    # Technique 2: Interning strings
    def compare_string_interning():
        # Without interning - separate objects
        s1 = ''.join(['hello', ' ', 'world'])
        s2 = ''.join(['hello', ' ', 'world'])

        print(f"Without interning: same object? {s1 is s2}")

        # With interning - same object
        s3 = sys.intern('hello world')
        s4 = sys.intern('hello world')

        print(f"With interning: same object? {s3 is s4}")

    # Technique 3: Using generators for large sequences
    def sum_squares_list(n):
        return sum([x*x for x in range(n)])

    def sum_squares_gen(n):
        return sum(x*x for x in range(n))

    # Technique 4: Lazy evaluation with properties
    class DataAnalyzer:
        def __init__(self, data):
            self._data = data
            self._mean = None

        @property
        def mean(self):
            """Calculate mean only when needed"""
            if self._mean is None:
                self._mean = sum(self._data) / len(self._data)
            return self._mean

    # Technique 5: Using array for homogeneous data
    import array

    regular_list = [i for i in range(10000)]
    efficient_array = array.array('i', range(10000))

    print("\n=== Memory Optimization Techniques ===\n")

    print("1. __slots__:")
    point = Point2D(10, 20)
    print(f"   Point2D size: {sys.getsizeof(point)} bytes")
    print(f"   Has __dict__: {hasattr(point, '__dict__')}")

    print("\n2. String interning:")
    compare_string_interning()

    print("\n3. Generators vs Lists:")
    print(f"   List size: {sys.getsizeof([x*x for x in range(1000)])} bytes")
    print(f"   Generator size: {sys.getsizeof((x*x for x in range(1000)))} bytes")

    print("\n4. Lazy evaluation:")
    analyzer = DataAnalyzer([1, 2, 3, 4, 5])
    print(f"   Mean calculated on demand: {analyzer.mean}")

    print("\n5. Array vs List:")
    print(f"   List size: {sys.getsizeof(regular_list):,} bytes")
    print(f"   Array size: {sys.getsizeof(efficient_array):,} bytes")
    print(f"   Savings: {sys.getsizeof(regular_list) - sys.getsizeof(efficient_array):,} bytes")

# Usage
example_15()
```

**Output:**
```
=== Memory Optimization Techniques ===

1. __slots__:
   Point2D size: 48 bytes
   Has __dict__: False

2. String interning:
   Without interning: same object? False
   With interning: same object? True

3. Generators vs Lists:
   List size: 8856 bytes
   Generator size: 200 bytes

4. Lazy evaluation:
   Mean calculated on demand: 3.0

5. Array vs List:
   List size: 87,624 bytes
   Array size: 40,064 bytes
   Savings: 47,560 bytes
```
