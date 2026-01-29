# Concurrency - Exercises

## Exercise 1: Parallel File Download
Write a function that downloads multiple files concurrently using threading.

```python
def download_files(urls, output_dir):
    """
    Download multiple files concurrently.

    Args:
        urls: List of URLs to download
        output_dir: Directory to save files

    Returns:
        List of (url, success) tuples
    """
    pass

# Test
urls = [
    "http://example.com/file1.txt",
    "http://example.com/file2.txt",
    "http://example.com/file3.txt",
]
results = download_files(urls, "/tmp/downloads")
```

## Exercise 2: Rate-Limited API Calls
Implement a rate-limited API client using asyncio that limits requests to N per second.

```python
import asyncio

class RateLimitedClient:
    def __init__(self, rate_limit):
        """
        Args:
            rate_limit: Maximum requests per second
        """
        pass

    async def request(self, url):
        """Make rate-limited request."""
        pass

# Test
async def main():
    client = RateLimitedClient(rate_limit=5)
    urls = [f"http://api.example.com/{i}" for i in range(20)]
    results = await asyncio.gather(*[client.request(url) for url in urls])
```

## Exercise 3: Parallel Matrix Multiplication
Implement matrix multiplication using multiprocessing.

```python
def parallel_matrix_multiply(A, B, num_processes=4):
    """
    Multiply two matrices using multiprocessing.

    Args:
        A: Matrix (list of lists)
        B: Matrix (list of lists)
        num_processes: Number of worker processes

    Returns:
        Result matrix
    """
    pass

# Test
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = parallel_matrix_multiply(A, B)
```

## Exercise 4: Thread-Safe Cache
Create a thread-safe cache with get, set, and clear operations.

```python
class ThreadSafeCache:
    def __init__(self, max_size=100):
        """Initialize cache with maximum size."""
        pass

    def get(self, key):
        """Get value from cache."""
        pass

    def set(self, key, value):
        """Set value in cache."""
        pass

    def clear(self):
        """Clear all cache entries."""
        pass

# Test
cache = ThreadSafeCache(max_size=10)
# Multiple threads should be able to use cache safely
```

## Exercise 5: Web Scraper
Build an async web scraper that extracts titles from multiple web pages.

```python
async def scrape_titles(urls):
    """
    Scrape titles from multiple URLs concurrently.

    Args:
        urls: List of URLs to scrape

    Returns:
        Dict mapping URL to title
    """
    pass

# Test
urls = [
    "http://example.com/page1",
    "http://example.com/page2",
]
titles = asyncio.run(scrape_titles(urls))
```

## Exercise 6: Parallel Image Processing
Process multiple images in parallel (resize, filter, etc.).

```python
def process_images(image_paths, output_dir, operations):
    """
    Process multiple images in parallel.

    Args:
        image_paths: List of image file paths
        output_dir: Output directory
        operations: List of operations to apply

    Returns:
        List of output paths
    """
    pass

# Test
images = ["img1.jpg", "img2.jpg", "img3.jpg"]
operations = ["resize", "grayscale", "blur"]
results = process_images(images, "/tmp/output", operations)
```

## Exercise 7: Task Queue
Implement a simple task queue system with workers.

```python
import queue
import threading

class TaskQueue:
    def __init__(self, num_workers=4):
        """Initialize task queue with workers."""
        pass

    def add_task(self, func, *args, **kwargs):
        """Add task to queue."""
        pass

    def wait_completion(self):
        """Wait for all tasks to complete."""
        pass

    def shutdown(self):
        """Shutdown all workers."""
        pass

# Test
def task(n):
    return n * n

tq = TaskQueue(num_workers=4)
for i in range(10):
    tq.add_task(task, i)
tq.wait_completion()
tq.shutdown()
```

## Exercise 8: Async File I/O
Write an async function that reads multiple files concurrently.

```python
async def read_files(file_paths):
    """
    Read multiple files concurrently.

    Args:
        file_paths: List of file paths

    Returns:
        Dict mapping path to content
    """
    pass

# Test
files = ["file1.txt", "file2.txt", "file3.txt"]
contents = asyncio.run(read_files(files))
```

## Exercise 9: Parallel Data Processing Pipeline
Create a parallel pipeline: read -> process -> write.

```python
def parallel_pipeline(input_files, output_dir, process_func, num_workers=4):
    """
    Process files through parallel pipeline.

    Args:
        input_files: List of input file paths
        output_dir: Output directory
        process_func: Function to process data
        num_workers: Number of parallel workers

    Returns:
        List of output file paths
    """
    pass

# Test
def process_data(data):
    return data.upper()

results = parallel_pipeline(
    ["input1.txt", "input2.txt"],
    "/tmp/output",
    process_data
)
```

## Exercise 10: Deadlock Detection
Implement a function that detects potential deadlocks in lock acquisition.

```python
class LockManager:
    def __init__(self):
        """Initialize lock manager."""
        pass

    def acquire(self, thread_id, lock_id):
        """Record lock acquisition."""
        pass

    def release(self, thread_id, lock_id):
        """Record lock release."""
        pass

    def has_deadlock(self):
        """
        Detect if there's a potential deadlock.

        Returns:
            bool: True if deadlock detected
        """
        pass

# Test
manager = LockManager()
manager.acquire("T1", "L1")
manager.acquire("T2", "L2")
manager.acquire("T1", "L2")  # Waiting
manager.acquire("T2", "L1")  # Waiting - deadlock!
print(manager.has_deadlock())  # True
```

## Exercise 11: Semaphore Connection Pool
Implement a connection pool using semaphores.

```python
class ConnectionPool:
    def __init__(self, max_connections):
        """
        Initialize connection pool.

        Args:
            max_connections: Maximum number of connections
        """
        pass

    def acquire(self):
        """Acquire connection from pool."""
        pass

    def release(self, connection):
        """Release connection back to pool."""
        pass

# Test
pool = ConnectionPool(max_connections=5)
# Should allow max 5 concurrent connections
```

## Exercise 12: Async Retry Logic
Implement async retry logic with exponential backoff.

```python
async def retry_async(func, max_retries=3, base_delay=1):
    """
    Retry async function with exponential backoff.

    Args:
        func: Async function to retry
        max_retries: Maximum number of retries
        base_delay: Base delay in seconds

    Returns:
        Result of function or raises last exception
    """
    pass

# Test
async def flaky_operation():
    import random
    if random.random() < 0.7:
        raise Exception("Operation failed")
    return "Success"

result = asyncio.run(retry_async(flaky_operation))
```

## Exercise 13: Parallel Merge Sort
Implement parallel merge sort using multiprocessing.

```python
def parallel_merge_sort(arr, num_processes=4):
    """
    Sort array using parallel merge sort.

    Args:
        arr: List to sort
        num_processes: Number of processes to use

    Returns:
        Sorted list
    """
    pass

# Test
arr = [64, 34, 25, 12, 22, 11, 90, 88]
sorted_arr = parallel_merge_sort(arr)
print(sorted_arr)
```

## Exercise 14: Event Bus
Create a simple event bus for thread communication.

```python
class EventBus:
    def __init__(self):
        """Initialize event bus."""
        pass

    def subscribe(self, event_type, callback):
        """Subscribe to event type."""
        pass

    def publish(self, event_type, data):
        """Publish event to subscribers."""
        pass

    def unsubscribe(self, event_type, callback):
        """Unsubscribe from event type."""
        pass

# Test
bus = EventBus()
def handler(data):
    print(f"Received: {data}")

bus.subscribe("message", handler)
bus.publish("message", "Hello")
```

## Exercise 15: Async Database Query Executor
Build an async query executor that batches queries for efficiency.

```python
class AsyncQueryExecutor:
    def __init__(self, batch_size=10, batch_delay=0.1):
        """
        Initialize query executor.

        Args:
            batch_size: Max queries per batch
            batch_delay: Max delay before executing batch
        """
        pass

    async def execute(self, query):
        """
        Execute query (will be batched).

        Args:
            query: Query string

        Returns:
            Query result
        """
        pass

# Test
async def main():
    executor = AsyncQueryExecutor()
    queries = [f"SELECT * FROM table WHERE id={i}" for i in range(50)]
    results = await asyncio.gather(*[executor.execute(q) for q in queries])
```
