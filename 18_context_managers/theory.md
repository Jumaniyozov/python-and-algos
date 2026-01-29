# Theory: Context Managers

## 1. Introduction to Context Managers

Context managers provide a way to allocate and release resources precisely when you want to. The most common example is file handling:

```python
# Without context manager
f = open('file.txt', 'r')
try:
    data = f.read()
finally:
    f.close()

# With context manager
with open('file.txt', 'r') as f:
    data = f.read()
# File automatically closed
```

##  2. The Context Manager Protocol

A context manager implements two methods:
- `__enter__()`: Setup, returns resource
- `__exit__()`: Cleanup, handles exceptions

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return True to suppress exception, False to propagate
        return False

# Usage
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
```

## 3. contextlib Module

### 3.1 @contextmanager Decorator

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()

with file_manager('test.txt', 'r') as f:
    data = f.read()
```

### 3.2 closing()

```python
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://example.com')) as page:
    for line in page:
        print(line)
```

### 3.3 suppress()

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('nonexistent.txt')
# No exception raised
```

### 3.4 redirect_stdout/redirect_stderr

```python
from contextlib import redirect_stdout
import io

f = io.StringIO()
with redirect_stdout(f):
    print('Hello')
    print('World')

output = f.getvalue()
```

## 4. ExitStack for Dynamic Context Management

```python
from contextlib import ExitStack

def process_files(filenames):
    with ExitStack() as stack:
        files = [stack.enter_context(open(fn)) for fn in filenames]
        # All files automatically closed on exit
        for f in files:
            process(f.read())
```

Advanced ExitStack usage:

```python
with ExitStack() as stack:
    # Register cleanup callbacks
    stack.callback(cleanup_function, arg1, arg2)

    # Conditionally add context managers
    if need_database:
        db = stack.enter_context(get_database())

    # Pop contexts early if needed
    file = stack.enter_context(open('file.txt'))
    stack.pop_all()  # Remove all contexts from stack
```

## 5. Exception Handling in Context Managers

```python
class Transaction:
    def __init__(self, connection):
        self.connection = connection

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.connection.commit()
        else:
            self.connection.rollback()
        return False  # Don't suppress exceptions

with Transaction(conn):
    execute_query("UPDATE ...")
    # Committed if successful, rolled back on exception
```

## 6. Async Context Managers

```python
class AsyncResource:
    async def __aenter__(self):
        self.resource = await acquire_resource()
        return self.resource

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.resource.release()
        return False

async def main():
    async with AsyncResource() as resource:
        await resource.use()
```

Using asynccontextmanager:

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_resource():
    resource = await acquire()
    try:
        yield resource
    finally:
        await resource.close()

async with async_resource() as r:
    await r.use()
```

## 7. ContextDecorator Pattern

```python
from contextlib import ContextDecorator

class debug(ContextDecorator):
    def __enter__(self):
        print("Entering debug mode")
        return self

    def __exit__(self, *exc):
        print("Exiting debug mode")
        return False

# As context manager
with debug():
    print("Debugging")

# As decorator
@debug()
def my_function():
    print("Function code")

my_function()  # Wrapped in debug context
```

## 8. Real-World Patterns

### Database Transaction

```python
@contextmanager
def transaction(connection):
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
```

### Timer Context

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"{label}: {end - start:.4f}s")

with timer("Processing"):
    # Long operation
    pass
```

### Thread Locking

```python
from threading import Lock
from contextlib import contextmanager

lock = Lock()

@contextmanager
def acquire_lock(lock, timeout=10):
    if not lock.acquire(timeout=timeout):
        raise TimeoutError("Could not acquire lock")
    try:
        yield
    finally:
        lock.release()

with acquire_lock(lock):
    # Critical section
    pass
```

## 9. Best Practices

1. **Always use context managers for resources** that need cleanup
2. **Return False from __exit__** unless you specifically want to suppress exceptions
3. **Use contextlib.contextmanager** for simple cases instead of class-based approach
4. **Use ExitStack** when managing dynamic number of resources
5. **Handle exceptions appropriately** in __exit__
6. **Document context manager behavior** clearly
7. **Make context managers reusable** when possible
8. **Use suppress()** for ignoring specific exceptions
9. **Consider thread-safety** for concurrent usage
10. **Test exception paths** thoroughly

## 10. Common Use Cases

- File handling
- Database connections and transactions
- Network sockets
- Thread/process locks
- Temporary state changes
- Resource pools
- Logging contexts
- Testing fixtures
- Configuration management
- Timing and profiling

Context managers make resource management clean, safe, and Pythonic. They're essential for writing robust production code.
