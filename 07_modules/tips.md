# Modules: Tips

## Tip 1: Avoid `from module import *`

**Bad**:
```python
from math import *
sqrt(16)  # Where does this come from?
```

**Good**:
```python
from math import sqrt
sqrt(16)  # Clear!
```

## Tip 2: Use `__all__`

```python
# module.py
__all__ = ['public_func', 'public_var']

def public_func():
    pass

def _private_func():  # Not in __all__
    pass
```

## Gotcha: Circular Imports

**Problem**:
```python
# a.py
from b import func_b

def func_a():
    func_b()

# b.py
from a import func_a  # Circular!

def func_b():
    func_a()
```

**Solution**: Restructure or use import inside function.

See examples.md!
