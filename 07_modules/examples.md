# Modules and Packages: Code Examples

## Example 1: Simple Module

```python
# math_utils.py
"""Math utility functions."""

PI = 3.14159

def circle_area(radius):
    """Calculate area of circle."""
    return PI * radius ** 2

def circle_circumference(radius):
    """Calculate circumference of circle."""
    return 2 * PI * radius

if __name__ == "__main__":
    # Test when run directly
    print(f"Area of circle (r=5): {circle_area(5)}")
    print(f"Circumference (r=5): {circle_circumference(5)}")
```

Usage:
```python
# main.py
import math_utils

area = math_utils.circle_area(10)
print(f"Area: {area}")

# Or
from math_utils import circle_area, PI
print(circle_area(10))
print(f"PI = {PI}")
```

## Example 2: Package Structure

```
mypackage/
    __init__.py
    module1.py
    module2.py
    utils/
        __init__.py
        helpers.py
```

**mypackage/__init__.py**:
```python
"""My package."""
from .module1 import func1
from .module2 import func2

__version__ = "1.0.0"
__all__ = ['func1', 'func2']
```

**mypackage/module1.py**:
```python
"""Module 1."""

def func1():
    return "Function 1 from module1"

def _private_func():
    """Not exported."""
    return "Private"
```

**mypackage/module2.py**:
```python
"""Module 2."""
from .module1 import func1  # Relative import

def func2():
    result = func1()  # Use func1
    return f"Function 2 calling {result}"
```

**mypackage/utils/helpers.py**:
```python
"""Helper utilities."""

def helper_func():
    return "Helper function"
```

Usage:
```python
# Import from package
from mypackage import func1, func2
print(func1())
print(func2())

# Import from subpackage
from mypackage.utils.helpers import helper_func
print(helper_func())

# Check version
import mypackage
print(mypackage.__version__)
```

## Example 3: Relative Imports

```
project/
    main.py
    package/
        __init__.py
        module_a.py
        module_b.py
        subpackage/
            __init__.py
            module_c.py
```

**package/module_a.py**:
```python
"""Module A."""

def func_a():
    return "Function A"
```

**package/module_b.py**:
```python
"""Module B using relative imports."""
from . import module_a  # Import sibling module
from .subpackage import module_c  # Import from subpackage

def func_b():
    result_a = module_a.func_a()
    result_c = module_c.func_c()
    return f"B: {result_a}, {result_c}"
```

**package/subpackage/module_c.py**:
```python
"""Module C."""
from .. import module_a  # Import from parent package

def func_c():
    return f"C using {module_a.func_a()}"
```

## Example 4: Dynamic Imports

```python
import importlib

# Import module by name (string)
module_name = "math"
math = importlib.import_module(module_name)
print(math.sqrt(16))

# Import from package
module = importlib.import_module(".module1", package="mypackage")
print(module.func1())

# Reload module (useful for development)
importlib.reload(math)
```

## Example 5: __all__ Control

**mymodule.py**:
```python
"""Module with controlled exports."""

__all__ = ['public_func', 'PublicClass']

def public_func():
    """Exported function."""
    return "Public"

def _private_func():
    """Not exported (leading underscore)."""
    return "Private"

class PublicClass:
    """Exported class."""
    pass

class _PrivateClass:
    """Not exported."""
    pass
```

Usage:
```python
# Only gets items in __all__
from mymodule import *
public_func()  # Works
# _private_func()  # NameError

# But can still import explicitly
from mymodule import _private_func
_private_func()  # Works
```

## Example 6: Module Search Path

```python
import sys

# View module search path
print("Python searches for modules in:")
for path in sys.path:
    print(f"  {path}")

# Add custom path
sys.path.append('/path/to/my/modules')

# Now can import from that path
# import my_custom_module
```

## Example 7: Lazy Imports

```python
# Defer import until needed (faster startup)

def process_data(data):
    """Only import pandas when function is called."""
    import pandas as pd  # Import inside function
    df = pd.DataFrame(data)
    return df.describe()

# pandas not imported until process_data() is called
```

## Example 8: Namespace Package (Python 3.3+)

Without `__init__.py` files, multiple directories can contribute to same namespace:

```
site-packages/
    mypkg/
        module1.py

another-location/
    mypkg/
        module2.py
```

Both contribute to `mypkg` namespace:
```python
from mypkg import module1
from mypkg import module2  # From different location!
```

## Example 9: Circular Import Solution

**Problem**:
```python
# module_a.py
from module_b import func_b

def func_a():
    return func_b()

# module_b.py
from module_a import func_a  # Circular!

def func_b():
    return func_a()
```

**Solution 1: Import inside function**:
```python
# module_a.py
def func_a():
    from module_b import func_b  # Import when needed
    return func_b()

# module_b.py
def func_b():
    from module_a import func_a
    return func_a()
```

**Solution 2: Restructure**:
```python
# shared.py
def shared_func():
    return "Shared"

# module_a.py
from shared import shared_func

def func_a():
    return shared_func()

# module_b.py
from shared import shared_func

def func_b():
    return shared_func()
```

## Example 10: Plugin System

```python
# plugins/
#     __init__.py
#     plugin1.py
#     plugin2.py

# main.py
import importlib
import pkgutil
import plugins

def load_plugins():
    """Dynamically load all plugins."""
    plugin_list = []

    for importer, modname, ispkg in pkgutil.iter_modules(plugins.__path__):
        module = importlib.import_module(f"plugins.{modname}")
        if hasattr(module, 'register'):
            plugin_list.append(module)
            module.register()

    return plugin_list

# Load all plugins automatically
loaded_plugins = load_plugins()
```

**plugins/plugin1.py**:
```python
def register():
    print("Plugin 1 registered")

def process():
    return "Plugin 1 processing"
```

**plugins/plugin2.py**:
```python
def register():
    print("Plugin 2 registered")

def process():
    return "Plugin 2 processing"
```

See solutions.md for exercise answers!
