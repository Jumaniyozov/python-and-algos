# Chapter 21: Niche Features - Theory

## 1. The Ellipsis (...) Object

### What is Ellipsis?
The ellipsis `...` is a built-in singleton object in Python, accessible via the `Ellipsis` constant or the `...` literal.

### Type Hints
Used to indicate "something goes here" in type annotations:
```python
from typing import Callable

# Function that takes any arguments
def process(func: Callable[..., int]) -> int:
    return func()
```

### NumPy Slicing
In NumPy and similar libraries, ellipsis represents "all remaining dimensions":
```python
import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arr[..., 0]  # Equivalent to arr[:, :, 0]
```

### Placeholder in Development
Used as a pass-like placeholder:
```python
def future_function():
    ...  # More meaningful than 'pass' for stub functions
```

### Custom Uses
Can be used in custom classes with `__getitem__`:
```python
class MyClass:
    def __getitem__(self, key):
        if key is Ellipsis:
            return "Got ellipsis!"
```

## 2. The Walrus Operator (:=)

### Basic Concept
Assignment expression - assigns AND returns a value in the same expression.

### Common Use Cases

**In While Loops:**
```python
# Before
line = file.readline()
while line:
    process(line)
    line = file.readline()

# After
while (line := file.readline()):
    process(line)
```

**In List Comprehensions:**
```python
# Avoid recalculating expensive operations
results = [y for x in data if (y := expensive_func(x)) > 0]
```

**In If Statements:**
```python
# Before
match = pattern.search(text)
if match:
    print(match.group(0))

# After
if (match := pattern.search(text)):
    print(match.group(0))
```

## 3. Positional-Only (/) and Keyword-Only (*) Parameters

### Positional-Only Parameters (/)
Parameters before `/` must be passed positionally, not as keywords:

```python
def func(a, b, /, c, d):
    # a, b: positional-only
    # c, d: positional or keyword
    pass

func(1, 2, 3, 4)        # OK
func(1, 2, c=3, d=4)    # OK
func(a=1, b=2, c=3, d=4)  # ERROR
```

**Why use it?**
- Allows renaming parameters without breaking API
- Prevents confusion with **kwargs
- Mirrors C API behavior

### Keyword-Only Parameters (*)
Parameters after `*` must be passed as keywords:

```python
def func(a, b, *, c, d):
    # a, b: positional or keyword
    # c, d: keyword-only
    pass

func(1, 2, c=3, d=4)    # OK
func(1, 2, 3, 4)        # ERROR
```

**Why use it?**
- Forces explicit parameter naming for clarity
- Prevents errors from positional argument order

### Combined Usage
```python
def func(pos_only, /, pos_or_kwd, *, kwd_only):
    pass

func(1, 2, kwd_only=3)          # OK
func(1, pos_or_kwd=2, kwd_only=3)  # OK
func(pos_only=1, pos_or_kwd=2, kwd_only=3)  # ERROR
```

## 4. __missing__ Method for Dict Subclasses

### Purpose
Called when a key is not found during `__getitem__` lookup (not for `.get()` or `__contains__`).

### Basic Implementation
```python
class DefaultDict(dict):
    def __init__(self, default_factory):
        super().__init__()
        self.default_factory = default_factory

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        value = self.default_factory()
        self[key] = value
        return value
```

### Use Cases
- Custom default values
- Lazy initialization
- Auto-vivification (nested dict creation)
- Logging access to missing keys

## 5. Enum and Flag Types

### Basic Enum
```python
from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Or use auto()
class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    COMPLETE = auto()
```

### Enum Features
- Iteration: `for color in Color: ...`
- Membership: `Color.RED in Color`
- By value: `Color(1)  # Returns Color.RED`
- By name: `Color['RED']`
- Comparison: `Color.RED == Color.RED` (True), `Color.RED is Color.RED` (True)

### Flag for Bit Flags
```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()     # 1
    WRITE = auto()    # 2
    EXECUTE = auto()  # 4

# Combine flags
user_perms = Permission.READ | Permission.WRITE

# Check flags
if user_perms & Permission.READ:
    print("Can read")
```

### IntEnum and IntFlag
```python
from enum import IntEnum, IntFlag

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

# Can compare with integers
Priority.LOW < 2  # True
```

## 6. Sentinel Values Pattern

### Purpose
Distinguish between "no value provided" and `None`.

### Implementation
```python
# Sentinel object
_MISSING = object()

def function(value=_MISSING):
    if value is _MISSING:
        # No value was provided
        value = expensive_default_calculation()
    elif value is None:
        # None was explicitly provided
        pass
```

### Common Uses
- Default parameter values when None is valid
- Cache miss indicators
- End-of-stream markers

### Using Enum for Sentinels
```python
from enum import Enum

class Sentinel(Enum):
    MISSING = object()
    NOT_SET = object()

def func(x=Sentinel.MISSING):
    if x is Sentinel.MISSING:
        print("Not provided")
```

## 7. Attribute Access Magic Methods

### __getattr__
Called when attribute is NOT found through normal lookup:

```python
class DynamicAttributes:
    def __getattr__(self, name):
        # Only called if 'name' not found normally
        return f"Dynamic: {name}"

obj = DynamicAttributes()
obj.anything  # Returns "Dynamic: anything"
```

### __getattribute__
Called for EVERY attribute access (dangerous!):

```python
class LoggedAccess:
    def __getattribute__(self, name):
        print(f"Accessing: {name}")
        # Must use super() to avoid infinite recursion
        return super().__getattribute__(name)
```

### __setattr__
Called when setting any attribute:

```python
class ValidatedAttrs:
    def __setattr__(self, name, value):
        if name.startswith('_'):
            raise AttributeError("Cannot set private attrs")
        super().__setattr__(name, value)
```

### __delattr__
Called when deleting an attribute:

```python
class ProtectedDelete:
    def __delattr__(self, name):
        if name == 'important':
            raise AttributeError("Cannot delete important")
        super().__delattr__(name)
```

### Key Differences
- `__getattr__`: Fallback only (attribute not found)
- `__getattribute__`: Always called (can cause recursion)
- Both are overridden in `__setattr__` and `__delattr__`

## 8. Module-Level __getattr__ and __dir__

### Module __getattr__ (Python 3.7+)
Enables lazy loading and deprecation warnings:

```python
# mymodule.py
def __getattr__(name):
    if name == "old_function":
        import warnings
        warnings.warn("old_function is deprecated", DeprecationWarning)
        return new_function
    raise AttributeError(f"module has no attribute {name}")

def __dir__():
    return ['new_function', 'old_function']
```

### Use Cases
- Lazy import of heavy dependencies
- Deprecation warnings
- Dynamic attribute generation
- Plugin systems

### Example: Lazy Import
```python
# module.py
_heavy_lib = None

def __getattr__(name):
    if name == "heavy_lib":
        global _heavy_lib
        if _heavy_lib is None:
            import heavy_library
            _heavy_lib = heavy_library
        return _heavy_lib
    raise AttributeError(f"module has no attribute {name}")
```

## 9. __slots__ Advanced Usage

### Basic Concept
Declare a fixed set of attributes, preventing `__dict__` creation.

### Benefits
- Memory savings (no `__dict__` per instance)
- Faster attribute access
- Prevents typos (attribute errors instead of silent bugs)

### Basic Usage
```python
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### Advanced Features

**Slots with Inheritance:**
```python
class Base:
    __slots__ = ('a',)

class Derived(Base):
    __slots__ = ('b',)  # Total slots: a, b
```

**Empty Slots in Child:**
```python
class Child(Base):
    __slots__ = ()  # Inherits parent's slots, adds none
```

**Slots with __dict__:**
```python
class Hybrid:
    __slots__ = ('x', 'y', '__dict__')  # Fixed + dynamic attrs
```

**Slots with __weakref__:**
```python
class Weakrefable:
    __slots__ = ('x', '__weakref__')  # Enable weak references
```

### Gotchas
- Can't add attributes not in `__slots__`
- Multiple inheritance requires compatible slots
- Default values need `__init__` or descriptors
- Pickles differently (may need custom pickle methods)

## 10. Other Lesser-Known Features

### __init_subclass__
Called when a class is subclassed:

```python
class PluginBase:
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.plugins.append(cls)

class Plugin1(PluginBase):
    pass

# PluginBase.plugins now contains Plugin1
```

### __set_name__
Descriptors can know their attribute name:

```python
class Descriptor:
    def __set_name__(self, owner, name):
        self.name = name  # Called automatically
```

### contextlib.suppress
Cleaner than try/except for ignoring exceptions:

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('file.txt')  # No error if file doesn't exist
```

### functools.singledispatch
Type-based function overloading:

```python
from functools import singledispatch

@singledispatch
def process(arg):
    print(f"Generic: {arg}")

@process.register(int)
def _(arg):
    print(f"Integer: {arg}")

@process.register(str)
def _(arg):
    print(f"String: {arg}")
```

### __prepare__
Customize class namespace during creation:

```python
class OrderedMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict()  # Use OrderedDict instead of dict
```

### __class_getitem__
Enable generic types:

```python
class MyList:
    def __class_getitem__(cls, item):
        return f"{cls.__name__}[{item}]"

MyList[int]  # Returns "MyList[int]"
```

### __format__
Custom string formatting:

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __format__(self, spec):
        if spec == 'polar':
            r = (self.x**2 + self.y**2)**0.5
            theta = atan2(self.y, self.x)
            return f"({r:.2f}, {theta:.2f})"
        return f"({self.x}, {self.y})"

p = Point(3, 4)
f"{p:polar}"  # Uses custom format
```

## Summary

These niche features provide powerful tools for:
- Code clarity (walrus operator, keyword-only params)
- Performance optimization (__slots__)
- API design (positional-only params, sentinels)
- Metaprogramming (magic methods, __init_subclass__)
- Type safety (Enum, Flag)
- Lazy loading (module __getattr__)

Use them judiciously - they solve specific problems but can make code harder to understand if overused.
