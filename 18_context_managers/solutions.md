# Solutions: Context Managers

## Solutions 1-5: Basic Context Managers

```python
# Solution 1: Logger Context Manager
import time
from contextlib import contextmanager

@contextmanager
def logger(name):
    """Context manager that logs entry/exit with timing"""
    print(f"Entering {name}")
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"Exiting {name} (took {elapsed:.2f} seconds)")

# Usage
with logger("database_query"):
    time.sleep(0.1)


# Solution 2: Temporary File Writer
import tempfile
import os

class TempFileWriter:
    """Context manager for temporary file with auto-deletion"""
    def __init__(self, prefix='tmp_'):
        self.prefix = prefix
        self.file = None
        self.filename = None

    def __enter__(self):
        # Create temporary file
        fd, self.filename = tempfile.mkstemp(prefix=self.prefix, text=True)
        self.file = os.fdopen(fd, 'w')
        print(f"Created temporary file: {self.filename}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close and delete file
        if self.file:
            self.file.close()
        if self.filename and os.path.exists(self.filename):
            os.unlink(self.filename)
            print(f"Deleted temporary file: {self.filename}")
        return False

# Usage
with TempFileWriter('test_') as f:
    f.write('temporary data')
    print(f"Writing to: {f.name}")


# Solution 3: List State Tracker
class ListStateTracker:
    """Context manager that tracks and can rollback list changes"""
    def __init__(self, lst):
        self.list = lst
        self.original_state = None

    def __enter__(self):
        # Save original state
        self.original_state = self.list.copy()
        print(f"Before: {self.list}")
        return self.list

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # Rollback on exception
            self.list.clear()
            self.list.extend(self.original_state)
            print(f"Rolled back to: {self.list}")
        else:
            print(f"After: {self.list}")
        return False

# Usage
data = [1, 2, 3]
try:
    with ListStateTracker(data) as tracked_list:
        tracked_list.append(4)
        tracked_list.append(5)
        raise ValueError("Error!")
except ValueError:
    pass
print(f"Final state: {data}")  # [1, 2, 3]


# Solution 4: Retry Context Manager
class retry_on_exception:
    """Context manager that retries on specific exceptions"""
    def __init__(self, max_retries=3, exceptions=(Exception,)):
        self.max_retries = max_retries
        self.exceptions = exceptions
        self.attempt = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.exceptions):
            self.attempt += 1
            if self.attempt < self.max_retries:
                print(f"Attempt {self.attempt} failed, retrying...")
                return True  # Suppress exception and retry
            else:
                print(f"Max retries ({self.max_retries}) exceeded")
                return False  # Propagate exception
        return False

# Usage
attempt = 0
while True:
    try:
        with retry_on_exception(max_retries=3, exceptions=(ValueError,)):
            attempt += 1
            print(f"Attempt {attempt}")
            if attempt < 3:
                raise ValueError("Not yet")
            print("Success!")
            break
    except ValueError:
        if attempt >= 3:
            break


# Solution 5: Environment Variable Context Manager
import os

@contextmanager
def temp_env(env_vars):
    """Temporarily set environment variables"""
    original_env = {}
    missing_vars = set()

    # Save original values
    for key in env_vars:
        if key in os.environ:
            original_env[key] = os.environ[key]
        else:
            missing_vars.add(key)

    # Set new values
    for key, value in env_vars.items():
        os.environ[key] = value
        print(f"Set {key}={value}")

    try:
        yield
    finally:
        # Restore original values
        for key in env_vars:
            if key in missing_vars:
                del os.environ[key]
                print(f"Removed {key}")
            else:
                os.environ[key] = original_env[key]
                print(f"Restored {key}={original_env[key]}")

# Usage
original_debug = os.environ.get('DEBUG')
with temp_env({'DEBUG': 'True', 'API_KEY': 'test123'}):
    print(f"DEBUG={os.environ['DEBUG']}")
print(f"DEBUG after context: {os.environ.get('DEBUG')}")
```

## Solutions 6-10: Intermediate Context Managers

```python
# Solution 6: Multi-Lock Context Manager
from threading import Lock

class MultiLock:
    """Acquire multiple locks in a deadlock-safe manner"""
    def __init__(self, *locks):
        # Sort locks by id to ensure consistent ordering
        self.locks = sorted(locks, key=id)

    def __enter__(self):
        # Acquire locks in order
        for lock in self.locks:
            lock.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Release in reverse order
        for lock in reversed(self.locks):
            lock.release()
        return False

# Usage
lock1, lock2, lock3 = Lock(), Lock(), Lock()
with MultiLock(lock3, lock1, lock2):
    print("All locks acquired safely")


# Solution 7: Cache Context Manager
from functools import wraps

class function_cache:
    """Context manager for function caching"""
    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.hits = 0
        self.misses = 0

    def __call__(self, *args):
        if args in self.cache:
            self.hits += 1
            return self.cache[args]
        else:
            self.misses += 1
            result = self.func(*args)
            self.cache[args] = result
            return result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Cache statistics: {self.hits} hits, {self.misses} misses")
        self.cache.clear()
        return False

# Usage
def expensive_func(n):
    import time
    time.sleep(0.01)
    return n ** 2

with function_cache(expensive_func) as cached_func:
    result1 = cached_func(5)  # Miss
    result2 = cached_func(5)  # Hit
    result3 = cached_func(10)  # Miss


# Solution 8: Database Connection Pool
from queue import Queue, Empty

class ConnectionPool:
    """Simple connection pool implementation"""
    def __init__(self, max_connections=3):
        self.max_connections = max_connections
        self.pool = Queue(maxsize=max_connections)
        self.active_connections = 0

        # Initialize pool
        for i in range(max_connections):
            self.pool.put({'id': i, 'active': False})

    @contextmanager
    def get_connection(self):
        """Get a connection from pool"""
        try:
            conn = self.pool.get(timeout=5)
            conn['active'] = True
            self.active_connections += 1
            print(f"Acquired connection {conn['id']} "
                  f"({self.active_connections}/{self.max_connections} active)")
            yield conn
        except Empty:
            raise RuntimeError("Connection pool exhausted")
        finally:
            conn['active'] = False
            self.active_connections -= 1
            self.pool.put(conn)
            print(f"Released connection {conn['id']}")

# Usage
pool = ConnectionPool(max_connections=2)
with pool.get_connection() as conn:
    print(f"Using connection {conn['id']}")


# Solution 9: Atomic File Writer
import shutil

class AtomicFileWriter:
    """Write to file atomically using temp file"""
    def __init__(self, filename):
        self.filename = filename
        self.temp_filename = f"{filename}.tmp"
        self.file = None

    def __enter__(self):
        self.file = open(self.temp_filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

        if exc_type is None:
            # Success - move temp to target
            shutil.move(self.temp_filename, self.filename)
            print(f"Atomically wrote to {self.filename}")
        else:
            # Error - remove temp file
            if os.path.exists(self.temp_filename):
                os.unlink(self.temp_filename)
            print(f"Removed temporary file due to error")

        return False

# Usage
import json
config = {'version': '1.0', 'debug': True}
with AtomicFileWriter('config.json') as f:
    json.dump(config, f)


# Solution 10: Profiler Context Manager
import cProfile
import pstats
from io import StringIO

class profiler:
    """Context manager for code profiling"""
    def __init__(self, top=10, sort_by='time'):
        self.top = top
        self.sort_by = sort_by
        self.profiler = cProfile.Profile()

    def __enter__(self):
        self.profiler.enable()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.profiler.disable()

        # Generate statistics
        stream = StringIO()
        stats = pstats.Stats(self.profiler, stream=stream)
        stats.sort_stats(self.sort_by)
        stats.print_stats(self.top)

        print(f"\nProfile Report (top {self.top} by {self.sort_by}):")
        print(stream.getvalue())

        return False

# Usage
def process_data():
    return sum(i**2 for i in range(10000))

with profiler(top=5, sort_by='cumulative'):
    result = process_data()
```

## Solutions 11-15: Advanced Context Managers

```python
# Solution 11: Async Rate Limiter
import asyncio
import time

class AsyncRateLimiter:
    """Async context manager implementing token bucket rate limiting"""
    def __init__(self, max_rate):
        self.max_rate = max_rate
        self.tokens = max_rate
        self.last_update = time.time()
        self.lock = asyncio.Lock()
        self.acquired_count = 0

    async def acquire(self):
        """Acquire a token, waiting if necessary"""
        async with self.lock:
            # Refill tokens
            now = time.time()
            elapsed = now - self.last_update
            self.tokens = min(self.max_rate,
                            self.tokens + elapsed * self.max_rate)
            self.last_update = now

            # Wait if no tokens available
            if self.tokens < 1:
                wait_time = (1 - self.tokens) / self.max_rate
                await asyncio.sleep(wait_time)
                self.tokens = 1

            self.tokens -= 1
            self.acquired_count += 1

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"Rate limiter: {self.acquired_count} operations completed")
        return False

# Usage
async def api_call():
    await asyncio.sleep(0.01)

async def main():
    async with AsyncRateLimiter(max_rate=10) as limiter:
        tasks = []
        for i in range(20):
            await limiter.acquire()
            tasks.append(asyncio.create_task(api_call()))
        await asyncio.gather(*tasks)

# asyncio.run(main())


# Solution 12: Transactional Dictionary
from copy import deepcopy

class Transaction:
    """Context manager providing transaction support for dictionaries"""
    _transaction_stack = []

    def __init__(self, data):
        self.data = data
        self.snapshot = None
        self.changes = {}
        self.committed = False

    def __enter__(self):
        # Save snapshot
        self.snapshot = deepcopy(self.data)
        Transaction._transaction_stack.append(self)

        # Return a proxy that tracks changes
        return TransactionProxy(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        Transaction._transaction_stack.pop()

        if exc_type is None:
            # Commit changes
            self.data.update(self.changes)
            self.committed = True
            print(f"Transaction committed: {self.changes}")
        else:
            # Rollback
            self.data.clear()
            self.data.update(self.snapshot)
            print(f"Transaction rolled back")

        return False

class TransactionProxy:
    """Proxy object that tracks dictionary changes"""
    def __init__(self, transaction):
        self.transaction = transaction

    def __setitem__(self, key, value):
        self.transaction.changes[key] = value
        self.transaction.data[key] = value

    def __getitem__(self, key):
        return self.transaction.data[key]

# Usage
data = {'balance': 100}
try:
    with Transaction(data) as txn:
        txn['balance'] = txn['balance'] - 50
        with Transaction(data) as nested_txn:
            nested_txn['balance'] = nested_txn['balance'] - 20
        print(f"After nested: {data}")
except:
    pass
print(f"Final: {data}")


# Solution 13: Resource Pool with Priorities
from enum import IntEnum
from heapq import heappush, heappop
import threading

class Priority(IntEnum):
    HIGH = 0
    NORMAL = 1
    LOW = 2

class PriorityResourcePool:
    """Resource pool with priority-based allocation"""
    def __init__(self, max_resources):
        self.max_resources = max_resources
        self.available = list(range(max_resources))
        self.waiting = []  # Min heap of (priority, request_id, event)
        self.lock = threading.Lock()
        self.next_request_id = 0
        self.stats = {'high': 0, 'normal': 0, 'low': 0}

    @contextmanager
    def acquire(self, priority=Priority.NORMAL, timeout=None):
        """Acquire resource with priority"""
        resource = None
        request_id = None

        with self.lock:
            if self.available:
                # Resource immediately available
                resource = self.available.pop()
                priority_name = Priority(priority).name.lower()
                self.stats[priority_name] += 1
            else:
                # Need to wait
                request_id = self.next_request_id
                self.next_request_id += 1
                event = threading.Event()
                heappush(self.waiting, (priority, request_id, event))

        if resource is None:
            # Wait for resource
            if not event.wait(timeout):
                raise TimeoutError("Resource acquisition timeout")
            resource = event.resource

        try:
            yield {'id': resource}
        finally:
            with self.lock:
                if self.waiting:
                    # Give to highest priority waiter
                    _, _, event = heappop(self.waiting)
                    event.resource = resource
                    event.set()
                else:
                    self.available.append(resource)

# Usage
pool = PriorityResourcePool(max_resources=2)
with pool.acquire(priority=Priority.HIGH, timeout=5.0) as resource:
    print(f"Using resource {resource['id']}")


# Solution 14: Distributed Lock
import fcntl
import os
import time

class DistributedLock:
    """File-based distributed lock"""
    def __init__(self, name, timeout=30):
        self.name = name
        self.timeout = timeout
        self.lockfile = f"/tmp/{name}.lock"
        self.fd = None

    def __enter__(self):
        start_time = time.time()

        while True:
            try:
                # Try to acquire lock
                self.fd = os.open(self.lockfile, os.O_CREAT | os.O_EXCL | os.O_WRONLY)

                # Write PID and timestamp
                os.write(self.fd, f"{os.getpid()}:{time.time()}".encode())
                print(f"Acquired distributed lock: {self.name}")
                return self

            except FileExistsError:
                # Check if lock is stale
                if os.path.exists(self.lockfile):
                    try:
                        with open(self.lockfile, 'r') as f:
                            content = f.read()
                            if content:
                                _, lock_time = content.split(':')
                                if time.time() - float(lock_time) > self.timeout:
                                    # Stale lock, remove it
                                    os.unlink(self.lockfile)
                                    print("Removed stale lock")
                                    continue
                    except:
                        pass

                # Check timeout
                if time.time() - start_time > self.timeout:
                    raise TimeoutError(f"Could not acquire lock within {self.timeout}s")

                time.sleep(0.1)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fd is not None:
            os.close(self.fd)
        if os.path.exists(self.lockfile):
            os.unlink(self.lockfile)
            print(f"Released distributed lock: {self.name}")
        return False

# Usage
with DistributedLock('my_resource', timeout=10):
    print("In critical section")
    time.sleep(1)


# Solution 15: Async Context Manager Chain
class AsyncContextChain:
    """Chain multiple async context managers"""
    def __init__(self, managers):
        self.managers = managers
        self.entered = []

    async def __aenter__(self):
        results = []
        try:
            for manager in self.managers:
                result = await manager.__aenter__()
                self.entered.append(manager)
                results.append(result)
            return tuple(results)
        except Exception as e:
            # Cleanup already entered managers
            await self._cleanup_entered()
            raise

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Exit all in reverse order
        exceptions = []
        for manager in reversed(self.entered):
            try:
                await manager.__aexit__(exc_type, exc_val, exc_tb)
            except Exception as e:
                exceptions.append(e)

        if exceptions:
            print(f"Errors during cleanup: {len(exceptions)}")

        return False

    async def _cleanup_entered(self):
        """Cleanup managers that were successfully entered"""
        for manager in reversed(self.entered):
            try:
                await manager.__aexit__(None, None, None)
            except:
                pass

# Mock async context managers for testing
class AsyncDatabase:
    async def __aenter__(self):
        print("Database connected")
        return self

    async def __aexit__(self, *args):
        print("Database closed")
        return False

    async def query(self):
        await asyncio.sleep(0.01)

class AsyncCache:
    async def __aenter__(self):
        print("Cache connected")
        return self

    async def __aexit__(self, *args):
        print("Cache closed")
        return False

    async def set(self, key, value):
        await asyncio.sleep(0.01)

class AsyncLogger:
    async def __aenter__(self):
        print("Logger initialized")
        return self

    async def __aexit__(self, *args):
        print("Logger closed")
        return False

    async def log(self, message):
        print(f"LOG: {message}")

# Usage
async def main():
    async with AsyncContextChain([
        AsyncDatabase(),
        AsyncCache(),
        AsyncLogger()
    ]) as (db, cache, logger):
        await db.query()
        await cache.set('key', 'value')
        await logger.log('Operation complete')

# asyncio.run(main())
```

## Key Concepts Demonstrated

### Resource Management
- Automatic cleanup with `__exit__`
- Exception handling and propagation
- State restoration on error

### Advanced Patterns
- Nested context managers
- Priority-based resource allocation
- Distributed locking
- Async context managers

### Best Practices
- Always return False from `__exit__` unless suppressing exceptions
- Use `@contextmanager` for simple cases
- Handle cleanup in reverse order (LIFO)
- Ensure cleanup happens even on exceptions
