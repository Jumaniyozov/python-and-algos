# Exercises: Memory Management

## Exercise 1: Measure Object Size (Easy)

Create a function that measures and compares the memory usage of different Python data structures storing the same data.

**Requirements**:
- Compare list, tuple, set, dict, and array.array
- Calculate both shallow and deep size
- Include the size of contained objects
- Present results in a formatted table

**Example**:
```python
def measure_structure_sizes(data):
    """
    Compare memory usage of different structures containing the same data.

    Args:
        data: List of integers to store in different structures

    Returns:
        Dictionary with structure names and their memory usage
    """
    # Your implementation here
    pass

# Test
data = list(range(1000))
results = measure_structure_sizes(data)
# Should show size comparison between list, tuple, set, dict, array
```

## Exercise 2: Demonstrate Reference Counting (Easy)

Build a tool that demonstrates how reference counting works in Python by tracking references to an object.

**Requirements**:
- Create an object and track its reference count
- Show how different operations affect the count
- Include: variable assignment, function calls, container storage, deletion
- Display results in a clear format

**Example**:
```python
def track_references(obj):
    """
    Track and display reference count changes for an object.

    Args:
        obj: Any Python object

    Returns:
        List of tuples (operation, ref_count)
    """
    # Your implementation here
    pass

# Test
data = [1, 2, 3]
history = track_references(data)
# Should show ref count increasing/decreasing with operations
```

## Exercise 3: Use Weak References (Easy)

Implement a simple cache that uses weak references to automatically clean up unused entries.

**Requirements**:
- Use WeakValueDictionary for the cache
- Add and retrieve cached objects
- Demonstrate automatic cleanup when objects are no longer referenced
- Show the difference from a regular dictionary cache

**Example**:
```python
class WeakCache:
    """Simple cache using weak references for automatic cleanup"""

    def __init__(self):
        # Your implementation here
        pass

    def set(self, key, value):
        """Add item to cache"""
        pass

    def get(self, key):
        """Retrieve item from cache"""
        pass

    def size(self):
        """Return number of cached items"""
        pass

# Test
cache = WeakCache()
obj = SomeObject()
cache.set('key1', obj)
# After deleting obj, cache should auto-cleanup
```

## Exercise 4: Compare __slots__ Memory Usage (Easy)

Create two versions of a class (with and without __slots__) and measure the memory difference when creating many instances.

**Requirements**:
- Implement both versions of a data class
- Create 10,000 instances of each
- Measure total memory usage
- Calculate percentage savings with __slots__

**Example**:
```python
def compare_slots_memory(n=10000):
    """
    Compare memory usage between regular class and __slots__ class.

    Args:
        n: Number of instances to create

    Returns:
        Dictionary with memory statistics
    """
    # Your implementation here
    pass

# Test
stats = compare_slots_memory(10000)
# Should show significant memory savings with __slots__
```

## Exercise 5: Track Memory Usage (Easy)

Create a decorator that tracks and reports memory usage of a function.

**Requirements**:
- Use tracemalloc to measure memory
- Track current and peak memory usage
- Display results after function execution
- Handle exceptions properly

**Example**:
```python
def memory_tracker(func):
    """
    Decorator to track memory usage of a function.

    Args:
        func: Function to track

    Returns:
        Wrapped function that reports memory usage
    """
    # Your implementation here
    pass

# Test
@memory_tracker
def create_large_list():
    return [i for i in range(1000000)]

result = create_large_list()
# Should print memory usage statistics
```

## Exercise 6: Build Weak Cache with TTL (Medium)

Implement a cache that uses weak references and also supports time-to-live (TTL) for entries.

**Requirements**:
- Use WeakValueDictionary for automatic cleanup
- Add TTL support for each entry
- Clean up expired entries on access
- Provide statistics (hits, misses, evictions)

**Example**:
```python
class TTLWeakCache:
    """Cache with weak references and time-to-live"""

    def __init__(self, default_ttl=60):
        # Your implementation here
        pass

    def set(self, key, value, ttl=None):
        """Add item with optional custom TTL"""
        pass

    def get(self, key):
        """Get item if not expired"""
        pass

    def stats(self):
        """Return cache statistics"""
        pass

# Test
cache = TTLWeakCache(default_ttl=5)
cache.set('key1', obj, ttl=10)
# Should handle both weak ref cleanup and TTL expiration
```

## Exercise 7: Find Circular References (Medium)

Create a tool that detects and reports circular references in a data structure.

**Requirements**:
- Traverse object graph using gc.get_referrers()
- Detect cycles in the reference graph
- Report all objects involved in cycles
- Visualize the circular reference chain

**Example**:
```python
class CircularReferenceDetector:
    """Detect circular references in object graphs"""

    def __init__(self):
        # Your implementation here
        pass

    def find_cycles(self, obj):
        """
        Find all circular references involving obj.

        Args:
            obj: Object to analyze

        Returns:
            List of cycle chains
        """
        pass

    def report(self, cycles):
        """Generate human-readable report of cycles"""
        pass

# Test
detector = CircularReferenceDetector()
# Create objects with circular references
node_a = Node('A')
node_b = Node('B')
node_a.ref = node_b
node_b.ref = node_a
cycles = detector.find_cycles(node_a)
```

## Exercise 8: Optimize Memory Usage (Medium)

Take a memory-intensive program and optimize it to use 50% less memory.

**Requirements**:
- Start with an inefficient implementation
- Apply multiple optimization techniques
- Measure memory before and after each optimization
- Document which techniques had the biggest impact

**Example**:
```python
def process_data_inefficient(data):
    """Memory-inefficient data processing"""
    # Store everything in memory
    results = []
    for item in data:
        results.append(expensive_operation(item))
    return results

def process_data_optimized(data):
    """
    Memory-optimized version using generators, slots, etc.

    Args:
        data: Input data to process

    Yields:
        Processed items one at a time
    """
    # Your implementation here
    pass

# Test and compare memory usage
with track_memory("Inefficient"):
    result1 = process_data_inefficient(large_dataset)

with track_memory("Optimized"):
    result2 = list(process_data_optimized(large_dataset))
```

## Exercise 9: Create Memory Profiler (Medium)

Build a memory profiler that identifies memory hotspots in code.

**Requirements**:
- Use tracemalloc to track allocations
- Identify top memory consumers by line
- Show memory growth over time
- Generate a summary report

**Example**:
```python
class MemoryProfiler:
    """Profile memory usage of code"""

    def __init__(self):
        # Your implementation here
        pass

    def start(self):
        """Start profiling"""
        pass

    def snapshot(self, label):
        """Take a memory snapshot"""
        pass

    def stop(self):
        """Stop profiling and return report"""
        pass

    def top_allocations(self, n=10):
        """Get top N memory allocations"""
        pass

# Test
profiler = MemoryProfiler()
profiler.start()

# Code to profile
data1 = [i for i in range(100000)]
profiler.snapshot("After list")

data2 = {i: str(i) for i in range(50000)}
profiler.snapshot("After dict")

report = profiler.stop()
```

## Exercise 10: Implement Object Pool (Medium)

Create a robust object pool implementation with auto-scaling and health checks.

**Requirements**:
- Pool grows when all objects are in use
- Pool shrinks when objects are idle
- Health check mechanism for pooled objects
- Thread-safe implementation

**Example**:
```python
class ObjectPool:
    """Thread-safe object pool with auto-scaling"""

    def __init__(self, factory, min_size=5, max_size=20):
        """
        Args:
            factory: Callable that creates new objects
            min_size: Minimum pool size
            max_size: Maximum pool size
        """
        # Your implementation here
        pass

    def acquire(self, timeout=None):
        """Get object from pool"""
        pass

    def release(self, obj):
        """Return object to pool"""
        pass

    def health_check(self, obj):
        """Verify object is still usable"""
        pass

    def stats(self):
        """Return pool statistics"""
        pass

# Test
pool = ObjectPool(lambda: Connection(), min_size=3, max_size=10)
conn = pool.acquire()
# Use connection
pool.release(conn)
```

## Exercise 11: Build Memory Leak Detector (Hard)

Create a tool that detects memory leaks by monitoring object creation and garbage collection over time.

**Requirements**:
- Track object creation by type
- Monitor objects that aren't being collected
- Detect growing collections that may indicate leaks
- Generate report with suspected leak sources
- Include code location of leak

**Example**:
```python
class MemoryLeakDetector:
    """Detect memory leaks in running application"""

    def __init__(self):
        # Your implementation here
        pass

    def start_monitoring(self):
        """Start monitoring for leaks"""
        pass

    def take_snapshot(self):
        """Take snapshot of current memory state"""
        pass

    def compare_snapshots(self, snap1, snap2):
        """Compare two snapshots to find leaks"""
        pass

    def find_leaks(self):
        """
        Analyze snapshots and identify leaks.

        Returns:
            List of suspected leaks with details
        """
        pass

    def report(self):
        """Generate detailed leak report"""
        pass

# Test
detector = MemoryLeakDetector()
detector.start_monitoring()

detector.take_snapshot()
# Run code that may leak
for i in range(1000):
    create_leaky_object()
detector.take_snapshot()

leaks = detector.find_leaks()
detector.report()
```

## Exercise 12: Optimize Large Dataset Processing (Hard)

Optimize a program that processes a large dataset (1GB+) to use minimal memory while maintaining performance.

**Requirements**:
- Process data in chunks/streams
- Use memory-mapped files where appropriate
- Implement efficient data structures
- Maintain processing speed within 10% of naive approach
- Use less than 100MB RAM for 1GB dataset

**Example**:
```python
class DatasetProcessor:
    """Memory-efficient large dataset processor"""

    def __init__(self, chunk_size=10000):
        """
        Args:
            chunk_size: Number of records to process at once
        """
        # Your implementation here
        pass

    def process_file(self, filepath):
        """
        Process large file efficiently.

        Args:
            filepath: Path to large data file

        Yields:
            Processed results one chunk at a time
        """
        pass

    def aggregate_results(self, results_iterator):
        """
        Aggregate results without loading all in memory.

        Args:
            results_iterator: Iterator of partial results

        Returns:
            Final aggregated result
        """
        pass

    def memory_usage(self):
        """Return current memory usage statistics"""
        pass

# Test
processor = DatasetProcessor(chunk_size=1000)
results = processor.process_file('large_file.csv')
final = processor.aggregate_results(results)
print(f"Peak memory: {processor.memory_usage()}")
```

## Exercise 13: Weak Callback System (Hard)

Implement an event system using weak references that doesn't prevent listeners from being garbage collected.

**Requirements**:
- Use weak references for all listeners
- Support method callbacks (need WeakMethod)
- Auto-cleanup dead listeners
- Thread-safe implementation
- Support priority and filtering

**Example**:
```python
class WeakEventSystem:
    """Event system with weak references to listeners"""

    def __init__(self):
        # Your implementation here
        pass

    def subscribe(self, event_type, callback, priority=0, filter_func=None):
        """
        Subscribe to event with weak reference.

        Args:
            event_type: Type of event to listen for
            callback: Function/method to call (stored weakly)
            priority: Higher priority callbacks called first
            filter_func: Optional filter for events
        """
        pass

    def unsubscribe(self, event_type, callback):
        """Remove subscription"""
        pass

    def publish(self, event_type, *args, **kwargs):
        """
        Publish event to all live listeners.

        Args:
            event_type: Type of event
            *args, **kwargs: Event data
        """
        pass

    def cleanup(self):
        """Remove dead listener references"""
        pass

# Test
events = WeakEventSystem()

class Listener:
    def handle(self, data):
        print(f"Received: {data}")

listener = Listener()
events.subscribe('update', listener.handle, priority=1)
events.publish('update', data={'value': 42})

del listener  # Should be collected, auto-removed from events
events.publish('update', data={'value': 43})  # No error
```

## Exercise 14: Memory-Efficient Cache (Hard)

Build a production-ready cache with multiple eviction strategies, memory limits, and weak references.

**Requirements**:
- Multiple eviction policies (LRU, LFU, FIFO)
- Memory limit enforcement
- Optional weak references
- Persistence support
- Thread-safe
- Comprehensive statistics

**Example**:
```python
class AdvancedCache:
    """Production-ready cache with multiple features"""

    def __init__(self, max_memory_mb=100, eviction_policy='LRU', use_weak_refs=False):
        """
        Args:
            max_memory_mb: Maximum memory usage in MB
            eviction_policy: 'LRU', 'LFU', or 'FIFO'
            use_weak_refs: Use weak references for values
        """
        # Your implementation here
        pass

    def set(self, key, value, ttl=None):
        """Add item to cache"""
        pass

    def get(self, key):
        """Retrieve item from cache"""
        pass

    def delete(self, key):
        """Remove item from cache"""
        pass

    def clear(self):
        """Clear entire cache"""
        pass

    def current_memory_usage(self):
        """Return current memory usage in bytes"""
        pass

    def evict_if_needed(self):
        """Evict items if over memory limit"""
        pass

    def stats(self):
        """
        Return cache statistics.

        Returns:
            Dict with hits, misses, evictions, memory usage, etc.
        """
        pass

    def save_to_disk(self, filepath):
        """Persist cache to disk"""
        pass

    def load_from_disk(self, filepath):
        """Load cache from disk"""
        pass

# Test
cache = AdvancedCache(max_memory_mb=50, eviction_policy='LRU', use_weak_refs=True)

# Add items
for i in range(10000):
    cache.set(f'key{i}', f'value{i}' * 100)

# Should evict old items when memory limit reached
print(cache.stats())
```

## Exercise 15: Advanced Memory Profiling (Hard)

Create a comprehensive memory profiling tool that tracks allocations, detections leaks, and suggests optimizations.

**Requirements**:
- Track memory allocations by type and location
- Detect memory leaks automatically
- Compare snapshots over time
- Identify optimization opportunities
- Generate detailed reports with graphs
- Suggest specific code improvements

**Example**:
```python
class AdvancedMemoryProfiler:
    """Comprehensive memory profiling and analysis tool"""

    def __init__(self):
        # Your implementation here
        pass

    def start(self):
        """Start profiling"""
        pass

    def stop(self):
        """Stop profiling"""
        pass

    def take_snapshot(self, label=None):
        """Take labeled snapshot"""
        pass

    def analyze_growth(self):
        """
        Analyze memory growth between snapshots.

        Returns:
            List of objects with growing memory usage
        """
        pass

    def detect_leaks(self):
        """
        Detect memory leaks.

        Returns:
            List of suspected leaks with evidence
        """
        pass

    def suggest_optimizations(self):
        """
        Analyze code and suggest optimizations.

        Returns:
            List of optimization suggestions
        """
        pass

    def generate_report(self, output_file):
        """
        Generate comprehensive HTML report.

        Args:
            output_file: Path to output HTML file
        """
        pass

    def plot_memory_timeline(self):
        """Create memory usage timeline graph"""
        pass

# Test
profiler = AdvancedMemoryProfiler()
profiler.start()

profiler.take_snapshot("Initial")

# Code to profile
data = []
for i in range(100):
    data.append([j for j in range(10000)])
    if i % 20 == 0:
        profiler.take_snapshot(f"Iteration {i}")

profiler.stop()

# Analysis
growth = profiler.analyze_growth()
leaks = profiler.detect_leaks()
suggestions = profiler.suggest_optimizations()

# Generate report
profiler.generate_report("memory_report.html")
profiler.plot_memory_timeline()
```
