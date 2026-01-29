# Concurrency - Tips and Best Practices

## Critical Decision: Which Model to Use?

### Use Threading When:
- I/O-bound operations (network requests, file I/O, database queries)
- Need shared state between workers
- Operations spend most time waiting
- Example: Web scraping, API calls, file uploads

### Use Multiprocessing When:
- CPU-bound operations (calculations, data processing, image manipulation)
- Need true parallelism
- Can divide work into independent chunks
- Example: Image processing, numerical computing, data analysis

### Use Asyncio When:
- High-concurrency I/O (web servers, chat applications)
- Thousands of simultaneous connections
- Mostly waiting, minimal computation
- Example: WebSocket servers, async web frameworks, concurrent API clients

## Common Pitfalls

### 1. Using Threading for CPU-Bound Tasks

**Bad**:
```python
# GIL prevents parallel execution!
with ThreadPoolExecutor() as executor:
    results = executor.map(cpu_intensive_func, data)
```

**Good**:
```python
# True parallelism
with ProcessPoolExecutor() as executor:
    results = executor.map(cpu_intensive_func, data)
```

### 2. Blocking the Event Loop

**Bad**:
```python
async def bad():
    time.sleep(1)  # Blocks entire event loop!
    requests.get(url)  # Blocking I/O!
```

**Good**:
```python
async def good():
    await asyncio.sleep(1)  # Non-blocking
    async with aiohttp.ClientSession() as session:
        await session.get(url)  # Async I/O
```

### 3. Shared State Without Locks

**Bad**:
```python
counter = 0

def increment():
    global counter
    counter += 1  # Race condition!
```

**Good**:
```python
counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        counter += 1
```

### 4. Creating Too Many Workers

**Bad**:
```python
# 1000 threads/processes = huge overhead!
with ThreadPoolExecutor(max_workers=1000) as executor:
    pass
```

**Good**:
```python
import os
# Reasonable number based on cores
max_workers = min(32, (os.cpu_count() or 1) + 4)
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    pass
```

### 5. Not Using Context Managers

**Bad**:
```python
pool = ThreadPoolExecutor()
results = pool.map(func, data)
# Forgot to shutdown!
```

**Good**:
```python
with ThreadPoolExecutor() as pool:
    results = pool.map(func, data)
# Automatically cleaned up
```

## Best Practices

### 1. Always Use concurrent.futures When Possible

**Instead of raw threading**:
```python
# Low-level (harder to use)
threads = []
for item in items:
    t = threading.Thread(target=process, args=(item,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

# High-level (easier, better)
with ThreadPoolExecutor() as executor:
    executor.map(process, items)
```

### 2. Handle Exceptions in Workers

```python
def safe_worker(item):
    try:
        return process(item)
    except Exception as e:
        logger.error(f"Error processing {item}: {e}")
        return None  # or raise
```

### 3. Set Timeouts

```python
# Threading
future = executor.submit(long_running_task)
try:
    result = future.result(timeout=30)
except TimeoutError:
    print("Task timed out")

# Asyncio
try:
    result = await asyncio.wait_for(coro, timeout=30)
except asyncio.TimeoutError:
    print("Coroutine timed out")
```

### 4. Use Queues for Producer-Consumer

```python
import queue

q = queue.Queue(maxsize=100)  # Limit queue size

def producer():
    for item in items:
        q.put(item)

def consumer():
    while True:
        item = q.get()
        process(item)
        q.task_done()  # Important!
```

### 5. Limit Shared State

**Bad**: Everything shared
```python
# Multiple mutable shared objects
shared_dict = {}
shared_list = []
shared_counter = 0
```

**Good**: Minimize sharing
```python
# Pass data explicitly
def worker(input_data):
    result = process(input_data)
    return result  # Return instead of modifying shared state
```

## Performance Tips

### 1. Pool Sizes

**Threading**:
```python
# I/O-bound: More workers OK
max_workers = min(32, len(items))
```

**Multiprocessing**:
```python
# CPU-bound: Match CPU cores
import os
max_workers = os.cpu_count()
```

### 2. Batch Work

```python
# Bad: One task per item (overhead!)
for item in thousands_of_items:
    executor.submit(tiny_task, item)

# Good: Batch items
def process_batch(batch):
    return [tiny_task(item) for item in batch]

batches = [items[i:i+100] for i in range(0, len(items), 100)]
executor.map(process_batch, batches)
```

### 3. Reuse Connections/Resources

```python
# Bad: Create new session per request
async def fetch(url):
    async with aiohttp.ClientSession() as session:  # Overhead!
        async with session.get(url) as resp:
            return await resp.text()

# Good: Reuse session
async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:  # Once
        tasks = [fetch_with_session(session, url) for url in urls]
        return await asyncio.gather(*tasks)
```

### 4. Use ProcessPoolExecutor Carefully

```python
# Problem: Pickling overhead for large data
def process(huge_data):  # Huge_data copied to each process!
    pass

# Better: Share data via Manager or use shared memory
from multiprocessing import Manager
manager = Manager()
shared_data = manager.dict(huge_data)
```

## Debugging Tips

### 1. Add Logging

```python
import logging
import threading

def worker():
    logging.info(f"Worker started in thread {threading.current_thread().name}")
    # ... work
    logging.info(f"Worker finished")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(threadName)s] %(message)s'
)
```

### 2. Use Thread Names

```python
t = threading.Thread(target=worker, name="MyWorker-1")
t.start()

# In worker
print(f"Running in {threading.current_thread().name}")
```

### 3. Test with Small Datasets First

```python
# Test with 10 items, not 10000
items = items[:10]  # Debug with subset

with ThreadPoolExecutor() as executor:
    results = list(executor.map(process, items))
```

### 4. Add Delays to Expose Race Conditions

```python
import time
import random

def worker():
    # Add random delay to expose races
    time.sleep(random.random() * 0.01)
    # Critical section
    shared_resource.modify()
```

## Common Patterns

### 1. Map-Reduce

```python
from concurrent.futures import ProcessPoolExecutor

def mapper(item):
    return process(item)

def reducer(results):
    return sum(results)

with ProcessPoolExecutor() as executor:
    mapped = executor.map(mapper, items)
    result = reducer(mapped)
```

### 2. Fan-Out, Fan-In

```python
async def fan_out_fan_in(items):
    # Fan out: Start all tasks
    tasks = [process_item(item) for item in items]

    # Fan in: Collect results
    results = await asyncio.gather(*tasks)

    return results
```

### 3. Rate Limiting

```python
import asyncio
import time

class RateLimiter:
    def __init__(self, rate):
        self.rate = rate
        self.min_interval = 1.0 / rate
        self.last_call = 0
        self.lock = asyncio.Lock()

    async def acquire(self):
        async with self.lock:
            now = time.time()
            time_since_last = now - self.last_call
            if time_since_last < self.min_interval:
                await asyncio.sleep(self.min_interval - time_since_last)
            self.last_call = time.time()

# Usage
limiter = RateLimiter(rate=10)  # 10/second
async def limited_request(url):
    await limiter.acquire()
    return await fetch(url)
```

### 4. Circuit Breaker

```python
import time

class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failures = 0
        self.last_failure_time = None
        self.state = 'closed'  # closed, open, half-open

    def call(self, func, *args, **kwargs):
        if self.state == 'open':
            if time.time() - self.last_failure_time > self.timeout:
                self.state = 'half-open'
            else:
                raise Exception("Circuit breaker is open")

        try:
            result = func(*args, **kwargs)
            if self.state == 'half-open':
                self.state = 'closed'
                self.failures = 0
            return result
        except Exception as e:
            self.failures += 1
            self.last_failure_time = time.time()
            if self.failures >= self.failure_threshold:
                self.state = 'open'
            raise
```

## Testing Concurrent Code

### 1. Use unittest.mock for Threading

```python
from unittest.mock import patch
import threading

def test_concurrent_calls():
    with patch('module.expensive_function') as mock:
        with ThreadPoolExecutor() as executor:
            executor.map(worker, range(10))

        assert mock.call_count == 10
```

### 2. Test Asyncio with pytest-asyncio

```python
import pytest

@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == expected
```

### 3. Stress Test

```python
def test_thread_safety():
    """Run many times to catch race conditions."""
    for _ in range(100):
        # Run test
        pass
```

## When NOT to Use Concurrency

1. **Simple, fast operations**: Overhead outweighs benefits
2. **Sequential dependencies**: Each step depends on previous
3. **Debugging complexity**: Hard to reproduce bugs
4. **Small datasets**: Not worth the complexity
5. **Limited resources**: May cause system issues

## Memory Considerations

### Threading:
- Shared memory (efficient)
- Each thread: ~1 KB overhead
- Careful with large shared objects

### Multiprocessing:
- Separate memory (copies data)
- Each process: ~10 MB overhead
- Use shared memory for large data

### Asyncio:
- Single process, minimal overhead
- Can handle thousands of concurrent operations
- Most memory-efficient for I/O

## Quick Reference

| Task Type | Model | Tool |
|-----------|-------|------|
| Web scraping | Threading | ThreadPoolExecutor |
| API calls | Asyncio | aiohttp + gather |
| File I/O | Threading | ThreadPoolExecutor |
| Image processing | Multiprocessing | ProcessPoolExecutor |
| Data analysis | Multiprocessing | ProcessPoolExecutor |
| Web server | Asyncio | FastAPI/aiohttp |
| Simple scripts | Sequential | None |

## Resources

- Official docs: https://docs.python.org/3/library/concurrency.html
- Real Python: Threading, Multiprocessing, Asyncio guides
- Books: "Python Concurrency with asyncio" by Matthew Fowler
