# Concurrency - Theory

## Core Concepts

### 1. Concurrency vs Parallelism

**Concurrency**: Multiple tasks making progress (not necessarily simultaneously)
- Can run on single CPU
- About structure and design
- Example: Handling multiple user requests

**Parallelism**: Multiple tasks executing simultaneously
- Requires multiple CPUs/cores
- About execution
- Example: Processing large dataset across cores

### 2. The Global Interpreter Lock (GIL)

**What is GIL?**:
- Mutex that protects Python objects
- Only one thread executes Python bytecode at a time
- Present in CPython (standard Python implementation)

**Implications**:
- Threading doesn't help with CPU-bound tasks
- Threading IS useful for I/O-bound tasks
- Multiprocessing bypasses GIL (separate processes)

**Why GIL Exists**:
- Simplifies memory management
- Makes C extension integration easier
- Protects internal data structures

### 3. Threading

**Thread Basics**:
- Lightweight execution context
- Shares memory with other threads
- Context switching managed by OS
- Good for I/O-bound operations

**Thread States**:
- New: Thread created but not started
- Runnable: Ready to run
- Running: Currently executing
- Blocked: Waiting for I/O or lock
- Terminated: Finished execution

**Thread Safety**:
- Problem: Race conditions from shared state
- Solution: Locks, semaphores, thread-local storage

### 4. Multiprocessing

**Process Basics**:
- Separate memory space
- True parallelism (no GIL)
- Higher overhead than threads
- Good for CPU-bound operations

**Process Communication**:
- Pipes: One-way or two-way communication
- Queues: Thread and process-safe queues
- Shared Memory: Direct memory sharing
- Manager: Shared Python objects

**Process Pool**:
- Reusable worker processes
- Reduces process creation overhead
- Automatic work distribution

### 5. Asyncio

**Core Concepts**:
- Event loop: Heart of asyncio
- Coroutines: async/await functions
- Tasks: Scheduled coroutines
- Futures: Placeholder for future result

**How It Works**:
- Cooperative multitasking
- Single-threaded event loop
- Yields control at I/O operations
- Non-blocking I/O

**When to Use**:
- High-concurrency I/O (web servers)
- Network clients making many requests
- Real-time applications (WebSockets)
- Not for CPU-bound tasks

### 6. concurrent.futures

**Purpose**: High-level interface for threading and multiprocessing

**Executors**:
- ThreadPoolExecutor: Thread-based execution
- ProcessPoolExecutor: Process-based execution
- Common interface for both

**Features**:
- Future objects: Represent pending operations
- map(): Apply function to iterables concurrently
- submit(): Submit individual tasks
- Automatic cleanup with context manager

## Synchronization Primitives

### Locks
```python
# Ensure only one thread accesses resource
lock = threading.Lock()
with lock:
    # Critical section
    shared_resource.modify()
```

### RLock (Reentrant Lock)
```python
# Same thread can acquire multiple times
rlock = threading.RLock()
with rlock:
    with rlock:  # OK - same thread
        pass
```

### Semaphore
```python
# Limit concurrent access
sem = threading.Semaphore(3)  # Max 3 threads
with sem:
    # At most 3 threads here
    pass
```

### Event
```python
# Signal between threads
event = threading.Event()
event.wait()  # Block until set
event.set()   # Wake waiting threads
event.clear() # Reset
```

### Condition
```python
# Wait for condition to be true
cv = threading.Condition()
with cv:
    cv.wait()    # Release lock and wait
    cv.notify()  # Wake one waiting thread
```

## Common Patterns

### Producer-Consumer (Threading)
```python
import threading
import queue

q = queue.Queue()

def producer():
    for i in range(10):
        q.put(i)

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        process(item)
        q.task_done()
```

### Map-Reduce (Multiprocessing)
```python
from multiprocessing import Pool

def mapper(data):
    return process(data)

def reducer(results):
    return combine(results)

with Pool() as pool:
    mapped = pool.map(mapper, data)
    result = reducer(mapped)
```

### Async Request Pattern
```python
async def fetch_all(urls):
    tasks = [fetch(url) for url in urls]
    return await asyncio.gather(*tasks)
```

## Decision Tree: Which Model?

### Use Threading When:
- I/O-bound operations (file, network, database)
- Waiting time dominates execution time
- Need shared state between workers
- Moderate number of concurrent operations

### Use Multiprocessing When:
- CPU-bound operations (computation, data processing)
- Need true parallelism
- Can divide work into independent chunks
- Have multiple CPU cores available

### Use Asyncio When:
- High-concurrency I/O (thousands of connections)
- Network servers or clients
- Need to handle many simultaneous operations
- Operations are mostly waiting

### Use Sequential When:
- Simple, fast operations
- Operation order matters strictly
- Debugging is critical
- Overhead outweighs benefits

## Performance Characteristics

### Thread Overhead:
- Creation: ~1 KB memory, microseconds
- Context switch: ~1-10 microseconds
- Limited by GIL for CPU tasks
- Memory: Shared with main process

### Process Overhead:
- Creation: ~10 MB memory, milliseconds
- Context switch: ~10-100 microseconds
- No GIL limitations
- Memory: Separate copy per process

### Asyncio Overhead:
- Coroutine: ~1 KB memory, nanoseconds
- Context switch: ~100 nanoseconds
- Single-threaded (no true parallelism)
- Memory: Very efficient for many tasks

## Common Pitfalls

### 1. Race Conditions
Multiple threads accessing shared data without synchronization
```python
# BAD: Race condition
counter = 0
def increment():
    global counter
    counter += 1  # Not atomic!

# GOOD: Protected
lock = threading.Lock()
def increment():
    with lock:
        global counter
        counter += 1
```

### 2. Deadlocks
Threads waiting for each other's locks
```python
# BAD: Potential deadlock
def thread1():
    with lock_a:
        with lock_b:
            pass

def thread2():
    with lock_b:  # Different order!
        with lock_a:
            pass

# GOOD: Consistent order
def both_threads():
    with lock_a:
        with lock_b:
            pass
```

### 3. Forgetting to Close Pools
```python
# BAD: Resource leak
pool = Pool()
pool.map(func, data)
# Pool never closed!

# GOOD: Use context manager
with Pool() as pool:
    pool.map(func, data)
# Automatically cleaned up
```

### 4. Mixing Async and Sync Code
```python
# BAD: Blocking in async function
async def bad():
    time.sleep(1)  # Blocks event loop!

# GOOD: Use async version
async def good():
    await asyncio.sleep(1)
```

### 5. Not Handling Exceptions in Workers
```python
# BAD: Exception kills thread silently
def worker():
    risky_operation()  # May raise

# GOOD: Handle exceptions
def worker():
    try:
        risky_operation()
    except Exception as e:
        log_error(e)
```

## Best Practices

1. **Start Simple**: Use sequential code unless you need concurrency
2. **Measure First**: Profile to find actual bottlenecks
3. **Choose Right Model**: Threading vs multiprocessing vs asyncio
4. **Minimize Shared State**: Reduces synchronization needs
5. **Use High-Level APIs**: concurrent.futures, asyncio, not raw threads
6. **Handle Errors**: Exceptions in concurrent code are tricky
7. **Test Thoroughly**: Race conditions are hard to reproduce
8. **Use Context Managers**: Ensure proper cleanup
9. **Limit Concurrency**: Don't create unlimited workers
10. **Monitor Resources**: Watch memory and CPU usage

## Thread Safety in Python

**Thread-Safe Built-ins**:
- List/Dict operations (mostly)
- queue.Queue
- collections.deque (append/pop)
- File objects (individual operations)

**Not Thread-Safe**:
- Counter increments (use locks)
- Complex operations on built-ins
- Most third-party libraries (check docs)

## Testing Concurrent Code

**Challenges**:
- Non-deterministic execution
- Race conditions may not appear in tests
- Timing-dependent bugs

**Strategies**:
- Use threading/multiprocessing test utilities
- Add deliberate delays to expose races
- Run tests multiple times
- Use thread-safety analysis tools
- Test with different numbers of workers
