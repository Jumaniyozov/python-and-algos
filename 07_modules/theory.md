# Modules and Packages: Theory

## 7.1 Importing and Module System

### What is a Module?

A module is a Python file (.py) containing code.

```python
# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159
```

### Importing

```python
# Import entire module
import math_utils
math_utils.add(2, 3)

# Import specific items
from math_utils import add, PI
add(2, 3)

# Import all (avoid!)
from math_utils import *

# Import with alias
import math_utils as mu
mu.add(2, 3)

from math_utils import multiply as mult
mult(2, 3)
```

### Module Search Path

Python searches for modules in:
1. Current directory
2. PYTHONPATH
3. Standard library
4. Site-packages

```python
import sys
print(sys.path)  # List of search paths
```

## 7.2 Creating Packages

### Package Structure

```
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

### __init__.py

Marks directory as package. Can be empty or contain initialization code:

```python
# mypackage/__init__.py
from .module1 import func1
from .module2 import func2

__all__ = ['func1', 'func2']
```

## 7.3 Relative vs Absolute Imports

### Absolute Imports

```python
from mypackage.module1 import func
from mypackage.subpackage.module3 import func
```

### Relative Imports

```python
# From module2.py in mypackage
from . import module1  # Same level
from .. import parent_module  # Parent level
from .subpackage import module3
```

## 7.4 if __name__ == "__main__"

```python
# my_module.py
def main():
    print("Running as script")

if __name__ == "__main__":
    main()  # Only runs when executed directly
```

## Best Practices

- Use absolute imports in most cases
- Keep __init__.py simple
- Avoid circular imports
- Use `if __name__ == "__main__"` pattern

See examples.md!
