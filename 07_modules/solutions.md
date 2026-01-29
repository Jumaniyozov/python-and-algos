# Modules and Packages: Exercise Solutions

## Solution 1: Math Module

```python
# my_math.py
"""Custom math module."""

def square(x):
    """Return x squared."""
    return x ** 2

def cube(x):
    """Return x cubed."""
    return x ** 3

def factorial(n):
    """Return n factorial."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Test functions
    print(f"square(5) = {square(5)}")
    print(f"cube(3) = {cube(3)}")
    print(f"factorial(5) = {factorial(5)}")
```

## Solution 2: Temperature Converter

```python
# temperature.py
"""Temperature conversion module."""

__all__ = [
    'celsius_to_fahrenheit',
    'fahrenheit_to_celsius',
    'celsius_to_kelvin',
    'kelvin_to_celsius'
]

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    """Convert Celsius to Kelvin."""
    return c + 273.15

def kelvin_to_celsius(k):
    """Convert Kelvin to Celsius."""
    return k - 273.15

def _helper_function():
    """Private helper (not exported)."""
    pass
```

## Solution 3: Calculator Package

**calculator/__init__.py**:
```python
"""Calculator package."""
from .basic import add, subtract, multiply, divide
from .advanced import power, sqrt, factorial

__all__ = [
    'add', 'subtract', 'multiply', 'divide',
    'power', 'sqrt', 'factorial'
]
```

**calculator/basic.py**:
```python
"""Basic arithmetic operations."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

**calculator/advanced.py**:
```python
"""Advanced math operations."""
import math

def power(base, exponent):
    return base ** exponent

def sqrt(x):
    return math.sqrt(x)

def factorial(n):
    return math.factorial(n)
```

Usage:
```python
from calculator import add, power
print(add(5, 3))  # 8
print(power(2, 3))  # 8
```

## Solution 4: Relative Imports

**myproject/core.py**:
```python
"""Core module."""
from .utils.helpers import helper_function

def main_function():
    result = helper_function()
    return f"Main using: {result}"
```

**myproject/utils/helpers.py**:
```python
"""Helper utilities."""

def helper_function():
    return "Helper result"
```

## Solution 5: Module with __all__

```python
# public_private.py
"""Module demonstrating __all__."""

__all__ = ['public1', 'public2', 'public3']

def public1():
    return "Public 1"

def public2():
    return "Public 2"

def public3():
    return "Public 3"

def _private1():
    """Private function 1."""
    return "Private 1"

def _private2():
    """Private function 2."""
    return "Private 2"

# Test
if __name__ == "__main__":
    # All functions accessible here
    print(public1())
    print(_private1())
```

Test:
```python
from public_private import *
public1()  # Works
# _private1()  # NameError - not imported

# But can import explicitly
from public_private import _private1
_private1()  # Works
```

## Solution 6: Plugin Loader

**plugin_loader.py**:
```python
"""Plugin loading system."""
import importlib
import pkgutil
from pathlib import Path

def load_plugins(plugin_dir='plugins'):
    """Load all plugins from directory."""
    plugins = []
    plugin_path = Path(plugin_dir)

    # Ensure it's a package
    if not (plugin_path / '__init__.py').exists():
        (plugin_path / '__init__.py').touch()

    # Import the plugins package
    plugins_package = importlib.import_module(plugin_dir)

    # Iterate over modules in package
    for importer, modname, ispkg in pkgutil.iter_modules(plugins_package.__path__):
        module = importlib.import_module(f"{plugin_dir}.{modname}")

        if hasattr(module, 'register'):
            module.register()
            plugins.append(module)
            print(f"Loaded plugin: {modname}")

    return plugins

if __name__ == "__main__":
    loaded = load_plugins()
    print(f"Loaded {len(loaded)} plugins")
```

**plugins/plugin1.py**:
```python
"""Sample plugin 1."""

def register():
    print("Plugin 1 registered!")

def execute():
    return "Plugin 1 executing"
```

**plugins/plugin2.py**:
```python
"""Sample plugin 2."""

def register():
    print("Plugin 2 registered!")

def execute():
    return "Plugin 2 executing"
```

## Solution 7: Lazy Import

```python
# lazy_import.py
"""Demonstrate lazy import performance."""
import time

# Global import (slow startup)
def with_global_import():
    import pandas as pd  # Always imported
    return pd.__version__

# Lazy import (fast startup)
def with_lazy_import(data):
    import pandas as pd  # Only imported when called
    return pd.DataFrame(data)

# Measure
if __name__ == "__main__":
    # Startup time
    start = time.time()
    # No imports yet for lazy version
    lazy_time = time.time() - start
    print(f"Lazy startup: {lazy_time:.4f}s")

    # Actually use it
    result = with_lazy_import({'a': [1, 2, 3]})
    print(result)
```

## Solution 8: Singleton Module

```python
# counter_module.py
"""Module that maintains state."""

_counter = 0

def increment():
    """Increment and return counter."""
    global _counter
    _counter += 1
    return _counter

def get_count():
    """Get current count."""
    return _counter

def reset():
    """Reset counter."""
    global _counter
    _counter = 0
```

Test:
```python
# file1.py
import counter_module
print(counter_module.increment())  # 1
print(counter_module.increment())  # 2

# file2.py
import counter_module
print(counter_module.get_count())  # 2 (persists!)
print(counter_module.increment())  # 3
```

## Solution 9: Fix Circular Import

**Solution: Import inside method**:

```python
# user.py
class User:
    def create_post(self):
        from post import Post  # Import when needed
        return Post(self)

# post.py
class Post:
    def __init__(self, user):
        # Type hint with string to avoid import
        self.user = user  # user: 'User'
```

**Alternative: Restructure**:

```python
# models.py
class User:
    def create_post(self):
        return Post(self)

class Post:
    def __init__(self, user):
        self.user = user

# Usage
from models import User, Post
```

## Solution 10: Package with Subpackages

**data_processor/__init__.py**:
```python
"""Data processor package."""
from .readers.csv_reader import read_csv
from .readers.json_reader import read_json
from .writers.csv_writer import write_csv
from .writers.json_writer import write_json

__all__ = ['read_csv', 'read_json', 'write_csv', 'write_json']
```

**data_processor/readers/csv_reader.py**:
```python
"""CSV reader."""
import csv

def read_csv(filename):
    with open(filename) as f:
        return list(csv.DictReader(f))
```

**data_processor/writers/csv_writer.py**:
```python
"""CSV writer."""
import csv

def write_csv(filename, data, fieldnames):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
```

Usage:
```python
from data_processor import read_csv, write_csv
```

## Challenge 1: Dynamic Module Loading

```python
import importlib.util
import sys

def load_module_from_path(path, module_name=None):
    """Load module from arbitrary path."""
    if module_name is None:
        module_name = Path(path).stem

    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module

# Usage
module = load_module_from_path('/path/to/my_module.py')
module.some_function()
```

## Challenge 2: Module Hot Reload

```python
import importlib
import time
from pathlib import Path

def watch_and_reload(module_path, check_interval=1):
    """Watch module and reload on changes."""
    path = Path(module_path)
    module_name = path.stem

    # Initial import
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    last_modified = path.stat().st_mtime

    while True:
        time.sleep(check_interval)
        current_modified = path.stat().st_mtime

        if current_modified > last_modified:
            print(f"Reloading {module_name}...")
            importlib.reload(module)
            last_modified = current_modified

# Usage (in background thread)
# watch_and_reload('my_module.py')
```

## Challenge 3: Namespace Package

No `__init__.py` needed!

**location1/mypkg/module1.py**:
```python
def func1():
    return "Function from module 1"
```

**location2/mypkg/module2.py**:
```python
def func2():
    return "Function from module 2"
```

Setup sys.path:
```python
import sys
sys.path.extend(['location1', 'location2'])

from mypkg import module1, module2
print(module1.func1())
print(module2.func2())
```

Excellent work! Check examples.md for more patterns.
