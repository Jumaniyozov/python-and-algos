# Concurrency - Examples

## Example 1: Basic Threading

```python
import threading
import time

def worker(name, delay):
    """Simple worker function."""
    print(f"Worker {name} starting")
    time.sleep(delay)
    print(f"Worker {name} finished")

# Create threads
threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread-{i}", i+1))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads completed")
```

## Example 2: Thread with Return Value (Using Queue)

```python
import threading
import queue

def worker(num, result_queue):
    """Worker that returns result via queue."""
    result = num * num
    result_queue.put((num, result))

# Create queue for results
results = queue.Queue()

# Start threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i, results))
    threads.append(t)
    t.start()

# Wait for completion
for t in threads:
    t.join()

# Collect results
print("Results:")
while not results.empty():
    num, result = results.get()
    print(f"{num}^2 = {result}")
```

## Example 3: Thread-Safe Counter with Lock

```python
import threading

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1

    def get_value(self):
        with self.lock:
            return self.value

# Test with multiple threads
counter = Counter()

def increment_many(counter, count):
    for _ in range(count):
        counter.increment()

threads = []
for _ in range(10):
    t = threading.Thread(target=increment_many, args=(counter, 1000))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final count: {counter.get_value()}")  # Should be 10000
```

## Example 4: ThreadPoolExecutor for I/O Tasks

```python
from concurrent.futures import ThreadPoolExecutor
import time

def download_file(url):
    """Simulate file download."""
    print(f"Downloading {url}")
    time.sleep(1)  # Simulate network delay
    return f"Content from {url}"

urls = [
    "http://example.com/file1",
    "http://example.com/file2",
    "http://example.com/file3",
    "http://example.com/file4",
]

# Using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit all tasks
    futures = [executor.submit(download_file, url) for url in urls]

    # Collect results as they complete
    from concurrent.futures import as_completed
    for future in as_completed(futures):
        result = future.result()
        print(f"Got: {result}")

print("All downloads complete")
```

## Example 5: ThreadPoolExecutor with map()

```python
from concurrent.futures import ThreadPoolExecutor
import time

def process_item(item):
    """Process a single item."""
    time.sleep(0.5)
    return item * 2

items = list(range(10))

# Sequential processing
start = time.time()
results_seq = [process_item(item) for item in items]
seq_time = time.time() - start
print(f"Sequential: {seq_time:.2f}s")

# Concurrent processing with map
start = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    results_concurrent = list(executor.map(process_item, items))
concurrent_time = time.time() - start
print(f"Concurrent: {concurrent_time:.2f}s")
print(f"Speedup: {seq_time/concurrent_time:.2f}x")
```

## Example 6: Basic Multiprocessing

```python
from multiprocessing import Process
import os

def worker(name):
    """Worker process."""
    print(f"Worker {name} in process {os.getpid()}")

if __name__ == "__main__":
    processes = []

    for i in range(4):
        p = Process(target=worker, args=(f"Process-{i}",))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Main process: {os.getpid()}")
```

## Example 7: ProcessPoolExecutor for CPU-Bound Tasks

```python
from concurrent.futures import ProcessPoolExecutor
import time

def cpu_intensive(n):
    """CPU-intensive calculation."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

numbers = [5_000_000] * 8

if __name__ == "__main__":
    # Sequential
    start = time.time()
    results_seq = [cpu_intensive(n) for n in numbers]
    seq_time = time.time() - start
    print(f"Sequential: {seq_time:.2f}s")

    # Parallel
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results_parallel = list(executor.map(cpu_intensive, numbers))
    parallel_time = time.time() - start
    print(f"Parallel: {parallel_time:.2f}s")
    print(f"Speedup: {seq_time/parallel_time:.2f}x")
```

## Example 8: Multiprocessing with Queue

```python
from multiprocessing import Process, Queue
import time

def producer(queue, items):
    """Produce items."""
    for item in items:
        queue.put(item)
        print(f"Produced: {item}")
        time.sleep(0.1)
    queue.put(None)  # Sentinel

def consumer(queue):
    """Consume items."""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        time.sleep(0.2)

if __name__ == "__main__":
    q = Queue()

    items = list(range(5))

    prod = Process(target=producer, args=(q, items))
    cons = Process(target=consumer, args=(q,))

    prod.start()
    cons.start()

    prod.join()
    cons.join()
```

## Example 9: Basic Asyncio

```python
import asyncio

async def task(name, delay):
    """Async task."""
    print(f"Task {name} starting")
    await asyncio.sleep(delay)
    print(f"Task {name} completed")
    return f"Result from {name}"

async def main():
    """Run multiple tasks concurrently."""
    # Create tasks
    tasks = [
        task("A", 2),
        task("B", 1),
        task("C", 3),
    ]

    # Run concurrently
    results = await asyncio.gather(*tasks)

    print("Results:", results)

# Run
asyncio.run(main())
```

## Example 10: Asyncio HTTP Requests (Conceptual)

```python
import asyncio

async def fetch(url):
    """Simulate async HTTP request."""
    print(f"Fetching {url}")
    await asyncio.sleep(1)  # Simulate network delay
    return f"Content from {url}"

async def fetch_all(urls):
    """Fetch all URLs concurrently."""
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

async def main():
    urls = [
        "http://example.com/1",
        "http://example.com/2",
        "http://example.com/3",
    ]

    results = await fetch_all(urls)
    for url, content in zip(urls, results):
        print(f"{url}: {content}")

asyncio.run(main())
```

## Example 11: Asyncio with Timeout

```python
import asyncio

async def slow_operation():
    """Operation that takes too long."""
    await asyncio.sleep(5)
    return "Completed"

async def main():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out")

asyncio.run(main())
```

## Example 12: Producer-Consumer with Queue

```python
import threading
import queue
import time
import random

def producer(q, num_items):
    """Produce items."""
    for i in range(num_items):
        item = f"Item-{i}"
        q.put(item)
        print(f"Produced: {item}")
        time.sleep(random.random() * 0.5)

    # Signal completion
    q.put(None)

def consumer(q):
    """Consume items."""
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break

        print(f"Consumed: {item}")
        time.sleep(random.random() * 0.5)
        q.task_done()

# Create queue
q = queue.Queue(maxsize=5)  # Limited size

# Start threads
prod_thread = threading.Thread(target=producer, args=(q, 10))
cons_thread = threading.Thread(target=consumer, args=(q,))

prod_thread.start()
cons_thread.start()

prod_thread.join()
cons_thread.join()

print("All items processed")
```

## Example 13: Thread Local Storage

```python
import threading
import random

# Thread-local storage
thread_local = threading.local()

def initialize():
    """Initialize thread-local data."""
    thread_local.value = random.randint(1, 100)

def worker(name):
    """Worker using thread-local storage."""
    initialize()
    print(f"{name}: {thread_local.value}")

# Each thread gets its own value
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

## Example 14: Event for Thread Coordination

```python
import threading
import time

def waiter(event, name):
    """Wait for event."""
    print(f"{name} waiting for event")
    event.wait()
    print(f"{name} continuing after event")

def setter(event, delay):
    """Set event after delay."""
    print(f"Setter sleeping for {delay}s")
    time.sleep(delay)
    print("Setting event")
    event.set()

# Create event
event = threading.Event()

# Start threads
waiter1 = threading.Thread(target=waiter, args=(event, "Waiter-1"))
waiter2 = threading.Thread(target=waiter, args=(event, "Waiter-2"))
setter_thread = threading.Thread(target=setter, args=(event, 2))

waiter1.start()
waiter2.start()
setter_thread.start()

waiter1.join()
waiter2.join()
setter_thread.join()
```

## Example 15: Async Context Manager

```python
import asyncio

class AsyncResource:
    """Example async resource."""

    async def __aenter__(self):
        print("Acquiring resource")
        await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        await asyncio.sleep(1)

    async def use(self):
        print("Using resource")
        await asyncio.sleep(1)

async def main():
    async with AsyncResource() as resource:
        await resource.use()

asyncio.run(main())
```

## Example 16: Comparison of All Three Models

```python
import time
import threading
from multiprocessing import Pool
import asyncio

def io_bound_task(n):
    """I/O-bound task (simulated)."""
    time.sleep(0.1)
    return n * 2

def cpu_bound_task(n):
    """CPU-bound task."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# Test data
data = list(range(10))

print("=== I/O-Bound Tasks ===")

# Sequential
start = time.time()
results = [io_bound_task(x) for x in data]
print(f"Sequential: {time.time() - start:.2f}s")

# Threading
start = time.time()
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(io_bound_task, data))
print(f"Threading: {time.time() - start:.2f}s")

# Asyncio
async def async_io_task(n):
    await asyncio.sleep(0.1)
    return n * 2

async def run_async():
    tasks = [async_io_task(x) for x in data]
    return await asyncio.gather(*tasks)

start = time.time()
results = asyncio.run(run_async())
print(f"Asyncio: {time.time() - start:.2f}s")

print("\n=== CPU-Bound Tasks ===")

cpu_data = [1_000_000] * 4

# Sequential
start = time.time()
results = [cpu_bound_task(x) for x in cpu_data]
print(f"Sequential: {time.time() - start:.2f}s")

# Multiprocessing
if __name__ == "__main__":
    start = time.time()
    with Pool(processes=4) as pool:
        results = pool.map(cpu_bound_task, cpu_data)
    print(f"Multiprocessing: {time.time() - start:.2f}s")
```
