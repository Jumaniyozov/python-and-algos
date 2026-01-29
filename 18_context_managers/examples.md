# Examples: Context Managers

## Example 1: Basic File Handling Context Manager

```python
class FileHandler:
    """Custom context manager for file handling with logging"""
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
        return False  # Don't suppress exceptions

# Usage
with FileHandler('test.txt', 'w') as f:
    f.write('Hello, Context Managers!')
```

## Example 2: Database Transaction Context Manager

```python
class DatabaseTransaction:
    """Simulates database transaction with rollback on error"""
    def __init__(self, connection):
        self.connection = connection
        self.transaction_active = False

    def __enter__(self):
        print("Starting transaction...")
        self.connection['in_transaction'] = True
        self.transaction_active = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Committing transaction...")
            self.connection['in_transaction'] = False
            self.transaction_active = False
        else:
            print(f"Rolling back transaction due to: {exc_val}")
            self.connection['in_transaction'] = False
            self.transaction_active = False
            # Return False to propagate the exception
        return False

# Usage
db_conn = {'in_transaction': False}

# Successful transaction
with DatabaseTransaction(db_conn):
    print("Executing database operations...")
    # Operations here

# Failed transaction
try:
    with DatabaseTransaction(db_conn):
        print("Executing database operations...")
        raise ValueError("Database error!")
except ValueError:
    print("Transaction was rolled back")
```

## Example 3: Timing Context Manager with contextlib

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(name):
    """Context manager to measure execution time"""
    start = time.time()
    print(f"Starting {name}...")
    try:
        yield
    finally:
        end = time.time()
        print(f"{name} took {end - start:.4f} seconds")

# Usage
with timer("Data processing"):
    # Simulate work
    time.sleep(0.1)
    numbers = [i**2 for i in range(10000)]

with timer("File operations"):
    time.sleep(0.05)
```

## Example 4: Thread Lock Context Manager

```python
import threading

class ThreadLock:
    """Context manager for thread synchronization"""
    def __init__(self, lock, name=""):
        self.lock = lock
        self.name = name

    def __enter__(self):
        print(f"Acquiring lock {self.name}...")
        self.lock.acquire()
        print(f"Lock {self.name} acquired")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Releasing lock {self.name}...")
        self.lock.release()
        return False

# Usage
lock = threading.Lock()
shared_resource = []

with ThreadLock(lock, "resource_lock"):
    shared_resource.append(1)
    shared_resource.append(2)
    print(f"Modified shared resource: {shared_resource}")
```

## Example 5: Temporary State Change with contextlib

```python
from contextlib import contextmanager
import sys

@contextmanager
def suppress_output():
    """Temporarily suppress stdout"""
    original_stdout = sys.stdout
    try:
        sys.stdout = None
        yield
    finally:
        sys.stdout = original_stdout

@contextmanager
def temp_attr(obj, attr, value):
    """Temporarily change an object attribute"""
    original = getattr(obj, attr, None)
    setattr(obj, attr, value)
    try:
        yield obj
    finally:
        if original is None:
            delattr(obj, attr)
        else:
            setattr(obj, attr, original)

# Usage
class Config:
    debug = False

config = Config()
print(f"Before: debug = {config.debug}")

with temp_attr(config, 'debug', True):
    print(f"Inside: debug = {config.debug}")

print(f"After: debug = {config.debug}")
```

## Example 6: ExitStack for Multiple Files

```python
from contextlib import ExitStack

def process_multiple_files(filenames):
    """Process multiple files with ExitStack"""
    with ExitStack() as stack:
        # Open all files
        files = [stack.enter_context(open(fname, 'w')) for fname in filenames]

        # Write to all files
        for i, file in enumerate(files):
            file.write(f"Content for file {i}\n")

        print(f"Successfully processed {len(files)} files")

# Usage
filenames = ['file1.txt', 'file2.txt', 'file3.txt']
process_multiple_files(filenames)
```

## Example 7: ExitStack with Dynamic Resources

```python
from contextlib import ExitStack, contextmanager

@contextmanager
def managed_resource(name):
    """Simulates acquiring and releasing a resource"""
    print(f"Acquiring {name}")
    try:
        yield name
    finally:
        print(f"Releasing {name}")

def use_resources(count):
    """Dynamically manage multiple resources"""
    with ExitStack() as stack:
        resources = []
        for i in range(count):
            resource = stack.enter_context(managed_resource(f"resource_{i}"))
            resources.append(resource)

        print(f"Working with {len(resources)} resources")
        # Do work with resources

# Usage
use_resources(3)
```

## Example 8: Async Context Manager

```python
import asyncio

class AsyncResource:
    """Async context manager for resource management"""
    def __init__(self, name):
        self.name = name

    async def __aenter__(self):
        print(f"Async acquiring {self.name}")
        await asyncio.sleep(0.1)  # Simulate async operation
        print(f"{self.name} acquired")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"Async releasing {self.name}")
        await asyncio.sleep(0.1)  # Simulate async cleanup
        print(f"{self.name} released")
        return False

# Usage
async def main():
    async with AsyncResource("database_connection"):
        print("Working with async resource...")
        await asyncio.sleep(0.05)

asyncio.run(main())
```

## Example 9: Async Context Manager with asynccontextmanager

```python
import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_timer(name):
    """Async context manager for timing"""
    start = asyncio.get_event_loop().time()
    print(f"Starting async {name}...")
    try:
        yield
    finally:
        end = asyncio.get_event_loop().time()
        print(f"Async {name} took {end - start:.4f} seconds")

async def fetch_data():
    """Simulate async data fetching"""
    async with async_timer("data fetch"):
        await asyncio.sleep(0.2)
        return {"data": "sample"}

# Usage
async def main():
    result = await fetch_data()
    print(f"Result: {result}")

asyncio.run(main())
```

## Example 10: Redirect Context Manager

```python
from contextlib import redirect_stdout, redirect_stderr
import io

def example_redirect():
    """Demonstrate output redirection"""
    # Redirect stdout
    stdout_buffer = io.StringIO()
    with redirect_stdout(stdout_buffer):
        print("This goes to buffer")
        print("So does this")

    captured = stdout_buffer.getvalue()
    print(f"Captured output: {captured}")

    # Redirect stderr
    stderr_buffer = io.StringIO()
    with redirect_stderr(stderr_buffer):
        import sys
        sys.stderr.write("Error message\n")

    print(f"Captured error: {stderr_buffer.getvalue()}")

# Usage
example_redirect()
```

## Example 11: Suppress Exceptions

```python
from contextlib import suppress

def example_suppress():
    """Demonstrate exception suppression"""
    # Without suppress
    try:
        int('invalid')
    except ValueError:
        pass

    # With suppress - cleaner
    with suppress(ValueError):
        int('invalid')

    with suppress(FileNotFoundError):
        with open('nonexistent.txt') as f:
            content = f.read()

    print("Code continues despite suppressed exceptions")

    # Suppress multiple exception types
    with suppress(ValueError, TypeError, KeyError):
        risky_operations = [
            lambda: int('invalid'),
            lambda: len(None),
            lambda: {}['missing_key']
        ]
        for op in risky_operations:
            op()

# Usage
example_suppress()
```

## Example 12: Closing Context Manager

```python
from contextlib import closing
import socket

def example_closing():
    """Demonstrate closing context manager"""
    # Using closing for objects with close() method
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(1)
        try:
            sock.connect(('google.com', 80))
            print("Connected")
        except:
            print("Connection failed")
    # Socket automatically closed

    # Custom class with close method
    class CustomResource:
        def __init__(self, name):
            self.name = name
            print(f"Opening {name}")

        def close(self):
            print(f"Closing {self.name}")

    with closing(CustomResource("my_resource")) as resource:
        print(f"Using {resource.name}")

# Usage
example_closing()
```

## Example 13: Nested Context Managers

```python
import tempfile
import os

class WorkingDirectory:
    """Context manager to temporarily change working directory"""
    def __init__(self, path):
        self.path = path
        self.original = None

    def __enter__(self):
        self.original = os.getcwd()
        os.chdir(self.path)
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original)
        return False

def example_nested():
    """Demonstrate nested context managers"""
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"Created temp directory: {tmpdir}")

        with WorkingDirectory(tmpdir):
            print(f"Changed to: {os.getcwd()}")

            with open('test.txt', 'w') as f:
                f.write('Nested context managers!')

            with open('test.txt', 'r') as f:
                content = f.read()
                print(f"File content: {content}")

        print(f"Back to: {os.getcwd()}")

# Usage
example_nested()
```

## Example 14: ExitStack with Callbacks

```python
from contextlib import ExitStack

def cleanup_callback(name):
    """Callback function for cleanup"""
    print(f"Cleanup callback for {name}")

def example_exitstack_callbacks():
    """Demonstrate ExitStack with callbacks"""
    with ExitStack() as stack:
        # Register cleanup callbacks
        stack.callback(cleanup_callback, "first")
        stack.callback(cleanup_callback, "second")
        stack.callback(lambda: print("Lambda cleanup"))

        # Create a resource
        file = stack.enter_context(open('test.txt', 'w'))
        file.write("ExitStack with callbacks")

        # Register more callbacks
        stack.callback(print, "Final cleanup step")

        print("Main work done")
    # All callbacks executed in LIFO order

# Usage
example_exitstack_callbacks()
```

## Example 15: Custom Reusable Context Manager

```python
from contextlib import contextmanager
import json

class ConfigManager:
    """Context manager for configuration changes"""
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = {}
        self.original_config = {}

    def __enter__(self):
        # Load config
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
                self.original_config = self.config.copy()
        except FileNotFoundError:
            self.config = {}
            self.original_config = {}
        return self.config

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            # Save modified config
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            print("Configuration saved")
        else:
            # Restore original config on error
            self.config = self.original_config
            print("Configuration changes reverted due to error")
        return False

@contextmanager
def log_context(message):
    """Context manager for logging entry/exit"""
    print(f">>> Entering: {message}")
    try:
        yield
    except Exception as e:
        print(f"!!! Error in {message}: {e}")
        raise
    finally:
        print(f"<<< Exiting: {message}")

# Usage
with log_context("Data processing pipeline"):
    with ConfigManager('app_config.json') as config:
        config['version'] = '2.0'
        config['debug'] = True
        print(f"Modified config: {config}")
```

