# Tips & Best Practices: Context Managers

## Best Practices

### Tip 1: Always Cleanup in __exit__
```python
class ResourceManager:
    def __enter__(self):
        self.resource = acquire_resource()
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        # ALWAYS cleanup, even if exception occurred
        if self.resource:
            self.resource.close()
        return False  # Don't suppress exceptions

# Even if exception occurs, resource is cleaned up
with ResourceManager() as resource:
    raise ValueError("Error!")  # Resource still closed
```

### Tip 2: Use @contextmanager for Simple Cases
```python
from contextlib import contextmanager

# Instead of writing a class...
@contextmanager
def temp_setting(config, key, value):
    """Temporarily change a config value"""
    old_value = config.get(key)
    config[key] = value
    try:
        yield config
    finally:
        if old_value is None:
            del config[key]
        else:
            config[key] = old_value

# Much cleaner than a full class
config = {'debug': False}
with temp_setting(config, 'debug', True):
    print(config)  # {'debug': True}
```

### Tip 3: Return False from __exit__ Unless Suppressing
```python
class FileProcessor:
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()

        # Return False (or None) to propagate exceptions
        # Return True ONLY if you want to suppress the exception
        if exc_type is IOError:
            print("Handled IO error")
            return True  # Suppress IOError
        return False  # Propagate all other exceptions
```

### Tip 4: Use ExitStack for Dynamic Resources
```python
from contextlib import ExitStack

def process_files(filenames):
    """Open variable number of files"""
    with ExitStack() as stack:
        # Dynamically open files
        files = [stack.enter_context(open(fname)) for fname in filenames]

        # Process all files
        for f in files:
            process(f)
        # All files automatically closed in reverse order
```

### Tip 5: Register Callbacks with ExitStack
```python
from contextlib import ExitStack

with ExitStack() as stack:
    # Register cleanup callbacks
    stack.callback(print, "Cleanup step 1")
    stack.callback(lambda: print("Cleanup step 2"))

    # Do work
    resource = acquire_resource()
    stack.callback(resource.close)

    # All callbacks executed in LIFO order on exit
```

## Common Pitfalls

### Pitfall 1: Forgetting to Return Resource from __enter__
```python
# WRONG - Doesn't return the resource
class BadManager:
    def __enter__(self):
        self.resource = open('file.txt')
        # Forgot to return!

with BadManager() as f:
    # f is None!
    f.read()  # AttributeError

# CORRECT - Return the resource
class GoodManager:
    def __enter__(self):
        self.resource = open('file.txt')
        return self.resource  # Return it!

with GoodManager() as f:
    f.read()  # Works!
```

### Pitfall 2: Suppressing Exceptions Unintentionally
```python
# WRONG - Returns True, suppresses ALL exceptions
def __exit__(self, exc_type, exc_val, exc_tb):
    self.cleanup()
    return True  # BAD! Hides exceptions

# CORRECT - Only suppress specific exceptions
def __exit__(self, exc_type, exc_val, exc_tb):
    self.cleanup()
    if exc_type is IOError:
        log_error(exc_val)
        return True  # OK to suppress IOError
    return False  # Propagate everything else
```

### Pitfall 3: Not Handling Exceptions in __exit__
```python
# WRONG - Exception in __exit__ replaces original
class BadCleanup:
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()  # May raise if file is None
        return False

# CORRECT - Protect cleanup code
class GoodCleanup:
    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.file:
                self.file.close()
        except Exception as e:
            print(f"Cleanup error: {e}")
        return False
```

### Pitfall 4: Modifying __enter__ Return After Yield
```python
# WRONG - List is mutable, changes persist
@contextmanager
def temp_list():
    lst = []
    yield lst  # Yields mutable object
    # Caller may have modified lst

# BETTER - Return a copy or use immutable
@contextmanager
def temp_list():
    lst = []
    yield lst
    # Clear it explicitly
    lst.clear()
```

## Performance Considerations

### Performance Tip 1: Reuse Context Managers When Possible
```python
# Instead of creating new context manager each time
for i in range(1000):
    with DatabaseConnection() as conn:  # New connection each time
        conn.query()

# Better - Reuse connection
conn = DatabaseConnection()
with conn:
    for i in range(1000):
        conn.query()
```

### Performance Tip 2: Use contextlib.suppress Instead of try/except
```python
# Slower - Creates exception frame
try:
    os.remove('file.txt')
except FileNotFoundError:
    pass

# Faster - contextlib.suppress is optimized
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove('file.txt')
```

### Performance Tip 3: Avoid Heavy Work in __enter__
```python
# SLOW - Does expensive work in __enter__
class SlowManager:
    def __enter__(self):
        self.data = load_huge_file()  # Blocks
        return self

# BETTER - Lazy load when needed
class FastManager:
    def __enter__(self):
        self.file = open('huge.dat')  # Just open
        return self

    def load_data(self):
        return self.file.read()  # Load on demand
```

## Real-World Patterns

### Pattern 1: Database Transaction
```python
@contextmanager
def transaction(connection):
    """Database transaction pattern"""
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise

with transaction(db_conn):
    db_conn.execute("INSERT ...")
    db_conn.execute("UPDATE ...")
    # Auto-commit on success, rollback on error
```

### Pattern 2: Timing and Profiling
```python
@contextmanager
def timed_block(name):
    """Time a code block"""
    import time
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{name}: {elapsed:.4f}s")

with timed_block("Data processing"):
    process_large_dataset()
```

### Pattern 3: Temporary State Change
```python
@contextmanager
def patch_object(obj, **attrs):
    """Temporarily modify object attributes"""
    original = {}
    for key, value in attrs.items():
        original[key] = getattr(obj, key, None)
        setattr(obj, key, value)
    try:
        yield obj
    finally:
        for key, value in original.items():
            setattr(obj, key, value)

# Usage
api = APIClient(timeout=30)
with patch_object(api, timeout=5, retries=3):
    api.call()  # Uses timeout=5, retries=3
# Back to timeout=30
```

### Pattern 4: Resource Pool
```python
class ConnectionPool:
    def __init__(self, size):
        self.pool = Queue(maxsize=size)
        for _ in range(size):
            self.pool.put(create_connection())

    @contextmanager
    def connection(self):
        conn = self.pool.get()
        try:
            yield conn
        finally:
            self.pool.put(conn)

pool = ConnectionPool(10)
with pool.connection() as conn:
    conn.query("SELECT ...")
```

### Pattern 5: Atomic File Operations
```python
@contextmanager
def atomic_write(filename):
    """Write to temp file, move on success"""
    temp_file = f"{filename}.tmp"
    f = open(temp_file, 'w')
    try:
        yield f
        f.close()
        os.rename(temp_file, filename)
    except Exception:
        f.close()
        os.remove(temp_file)
        raise

with atomic_write('config.json') as f:
    json.dump(config, f)
    # Only replaces file if no exception
```

## Debugging Tips

### Debug Tip 1: Log Entry/Exit for Troubleshooting
```python
@contextmanager
def logged_context(name):
    """Context manager with entry/exit logging"""
    print(f">>> Entering {name}")
    import traceback
    try:
        yield
        print(f"<<< Exiting {name} (success)")
    except Exception as e:
        print(f"!!! Error in {name}: {e}")
        traceback.print_exc()
        raise
```

### Debug Tip 2: Check Exception Parameters
```python
class DebugManager:
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            print(f"Traceback: {exc_tb}")
            import traceback
            traceback.print_tb(exc_tb)
        return False
```

### Debug Tip 3: Use ExitStack.callback for Debugging
```python
from contextlib import ExitStack

with ExitStack() as stack:
    stack.callback(print, "Exiting context")

    resource = acquire_resource()
    stack.callback(print, f"Releasing {resource}")
    stack.callback(resource.close)

    # Callbacks show cleanup order
```

## Async Context Manager Tips

### Async Tip 1: Use async with for Async Resources
```python
class AsyncDatabase:
    async def __aenter__(self):
        self.conn = await create_connection()
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()
        return False

async def main():
    async with AsyncDatabase() as db:
        await db.query("SELECT ...")
```

### Async Tip 2: Use asynccontextmanager
```python
from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def async_timer(name):
    start = asyncio.get_event_loop().time()
    try:
        yield
    finally:
        elapsed = asyncio.get_event_loop().time() - start
        print(f"{name}: {elapsed:.4f}s")

async with async_timer("Async operation"):
    await some_async_task()
```

## Key Takeaways

1. **Always cleanup**: Use `__exit__` to ensure resources are released
2. **Return False**: Unless you specifically want to suppress exceptions
3. **Use @contextmanager**: For simple context managers to avoid boilerplate
4. **ExitStack for dynamic**: When number of resources is not known in advance
5. **LIFO cleanup order**: Resources are cleaned up in reverse order of acquisition
6. **Exception safety**: Ensure cleanup happens even when exceptions occur
7. **Async support**: Use `async with` and `__aenter__`/`__aexit__` for async code
8. **Test exception paths**: Ensure your context manager works correctly with exceptions
9. **Document behavior**: Clarify what the context manager does and any exceptions it suppresses
10. **Prefer built-ins**: Use `contextlib.closing`, `suppress`, `redirect_stdout` when applicable
