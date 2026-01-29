# Chapter 21: Niche Features - Tips & Best Practices

## When to Use Each Feature

### Ellipsis (...)

**Use When:**
- Defining stub functions or methods that will be implemented later
- Type hints for callables with variable arguments
- Implementing NumPy-like array slicing
- Creating placeholder values in configurations

**Avoid When:**
- Regular code flow control (use `pass` instead for simple no-ops)
- You could use `None` more clearly
- The meaning isn't obvious to other developers

**Best Practice:**
```python
# Good: Clear intention for future implementation
class BaseAPI:
    def fetch_data(self):
        """Fetch data from API."""
        ...  # Subclasses must implement

# Bad: Confusing use
def process(x):
    if x > 0:
        ...  # What does this mean?
    return x
```

### Walrus Operator (:=)

**Use When:**
- Reading and checking values in loops
- Avoiding repeated expensive computations
- Combining assignment and condition checks
- List comprehensions where you need the computed value

**Avoid When:**
- It makes code less readable
- Simple assignments are clearer
- Chaining multiple walrus operators (hard to read)
- The value is only used once anyway

**Best Practice:**
```python
# Good: Avoids duplicate computation
results = [y for x in data if (y := expensive_func(x)) > threshold]

# Good: Cleaner while loop
while (chunk := file.read(8192)):
    process(chunk)

# Bad: Overcomplicating simple code
if (x := 5) > 3:  # Just use x = 5 separately
    print(x)

# Bad: Too complex
if (a := foo()) and (b := bar(a)) and (c := baz(b)):
    # Hard to follow
    pass
```

### Positional-Only and Keyword-Only Parameters

**Use When:**
- Designing public APIs that may evolve
- Parameters where order/name is critical
- Preventing accidental keyword usage
- Many optional parameters that should be explicit

**Avoid When:**
- Internal functions with 1-2 parameters
- Parameters have obvious names that won't change
- It adds unnecessary complexity

**Best Practice:**
```python
# Good: Public API with flexibility
def create_user(user_id, /, *, email, name, age=None):
    # user_id can be renamed without breaking callers
    # email and name must be explicit
    pass

# Good: Many optional params benefit from keyword-only
def configure(*, timeout=30, retries=3, debug=False,
              max_connections=100, buffer_size=8192):
    pass

# Bad: Overkill for simple functions
def add(a, /, b, /, *, verbose=False):  # Unnecessary
    return a + b
```

### __missing__ Method

**Use When:**
- Auto-vivification (creating nested structures)
- Custom default value logic
- Logging or tracking missing key access
- Lazy initialization of dict values

**Avoid When:**
- `defaultdict` or `.setdefault()` work fine
- The logic is too complex
- You need to distinguish between missing and `None` (use sentinels instead)

**Best Practice:**
```python
# Good: Auto-vivification
class NestedDict(dict):
    def __missing__(self, key):
        self[key] = NestedDict()
        return self[key]

# Good: Lazy computation
class ComputedDict(dict):
    def __missing__(self, key):
        if key in self.factories:
            value = self.factories[key]()
            self[key] = value
            return value
        raise KeyError(key)

# Bad: Use defaultdict instead
class SimpleDefault(dict):
    def __missing__(self, key):
        return 0  # Just use defaultdict(int)
```

### Enum and Flag Types

**Use When:**
- Fixed set of related constants
- State machines
- Permissions and bit flags
- Configuration options
- Status codes

**Avoid When:**
- Values need to be dynamic
- Simple string constants are clearer
- You're just grouping unrelated constants

**Best Practice:**
```python
# Good: Related constants with behavior
class Status(Enum):
    PENDING = 'pending'
    ACTIVE = 'active'
    DONE = 'done'

    def can_transition_to(self, other):
        transitions = {
            Status.PENDING: {Status.ACTIVE},
            Status.ACTIVE: {Status.DONE},
            Status.DONE: set()
        }
        return other in transitions[self]

# Good: Bit flags for permissions
class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

# Bad: Unrelated constants
class Constants(Enum):
    MAX_SIZE = 100
    DEFAULT_NAME = "test"
    PI = 3.14  # These don't belong together
```

### Sentinel Values

**Use When:**
- Distinguishing "not provided" from `None`
- Cache miss indicators
- End-of-stream markers
- Default parameter values when `None` is valid input

**Avoid When:**
- `None` works fine
- Adds unnecessary complexity
- The distinction isn't important

**Best Practice:**
```python
# Good: Sentinel for "not provided"
_MISSING = object()

def fetch(key, default=_MISSING):
    if key in cache:
        return cache[key]  # Could be None
    if default is _MISSING:
        raise KeyError(key)
    return default

# Good: Multiple sentinels for different states
class CacheState(Enum):
    MISS = object()
    EXPIRED = object()
    COMPUTING = object()

# Bad: None works fine here
_NO_VALUE = object()

def get_name(user, default=_NO_VALUE):
    return user.name if user else (None if default is _NO_VALUE else default)
    # Just use None as default!
```

### __getattr__ and __getattribute__

**Use When:**
- Dynamic attribute generation
- Proxying or delegation
- Deprecation warnings
- Plugin systems
- API clients with dynamic endpoints

**Avoid When:**
- Normal attribute access is sufficient
- It makes debugging harder
- You're using `__getattribute__` (rarely needed and dangerous)

**Best Practice:**
```python
# Good: Dynamic attributes with clear fallback
class Config:
    def __getattr__(self, name):
        # Try environment variable
        import os
        env_var = os.getenv(name.upper())
        if env_var is not None:
            return env_var
        raise AttributeError(f"No config for {name}")

# Bad: __getattribute__ without good reason
class Tracked:
    def __getattribute__(self, name):
        print(f"Accessing {name}")  # Debugging nightmare
        return super().__getattribute__(name)

# Good: Clear delegation
class Proxy:
    def __init__(self, target):
        object.__setattr__(self, '_target', target)

    def __getattr__(self, name):
        return getattr(self._target, name)
```

### __slots__

**Use When:**
- Creating many instances (thousands+)
- Memory is constrained
- Performance is critical
- You want attribute safety

**Avoid When:**
- Few instances created
- Need dynamic attributes
- Using multiple inheritance (complicated)
- Premature optimization

**Best Practice:**
```python
# Good: Many instances, fixed attributes
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Good: Allow weak references
class Cached:
    __slots__ = ('data', '__weakref__')

# Bad: Premature optimization
class User:
    __slots__ = ('name', 'email')  # Only creating 10 users

# Bad: Need dynamic attributes
class Plugin:
    __slots__ = ('name',)  # But plugins add custom attributes!
```

### __init_subclass__

**Use When:**
- Plugin systems with auto-registration
- Enforcing subclass contracts
- Adding class-level metadata
- Framework development

**Avoid When:**
- Simple inheritance is sufficient
- It adds unnecessary magic
- Metaclasses are more appropriate

**Best Practice:**
```python
# Good: Auto-registration
class Plugin:
    _registry = {}

    def __init_subclass__(cls, plugin_id=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if plugin_id:
            cls._registry[plugin_id] = cls

# Good: Enforce contract
class Model:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, 'table_name'):
            raise TypeError(f"{cls.__name__} must define 'table_name'")

# Bad: Overengineering
class MyClass:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"Class {cls.__name__} created")  # Why?
```

## Common Pitfalls

### Pitfall 1: Walrus Operator Scope

```python
# Wrong: Variable scope issues
if condition and (x := compute()):
    process(x)
elif other_condition and (x := other_compute()):  # Redefines x
    process(x)
# x is still defined here!

# Better: Explicit scope
x = None
if condition:
    x = compute()
    process(x)
elif other_condition:
    x = other_compute()
    process(x)
```

### Pitfall 2: __getattribute__ Recursion

```python
# Wrong: Infinite recursion
class Bad:
    def __getattribute__(self, name):
        print(f"Getting {name}")
        return self.name  # Calls __getattribute__ again!

# Correct:
class Good:
    def __getattribute__(self, name):
        print(f"Getting {name}")
        return super().__getattribute__(name)
```

### Pitfall 3: Enum Value Comparison

```python
from enum import Enum

class Status(Enum):
    ACTIVE = 1
    INACTIVE = 2

# Wrong: Comparing with raw value
status = Status.ACTIVE
if status == 1:  # False! Status.ACTIVE != 1
    pass

# Correct:
if status == Status.ACTIVE:  # True
    pass

# Or use IntEnum if you need integer comparison
from enum import IntEnum

class Status(IntEnum):
    ACTIVE = 1
    INACTIVE = 2

status = Status.ACTIVE
if status == 1:  # Now True
    pass
```

### Pitfall 4: __slots__ and Inheritance

```python
# Wrong: Incompatible __slots__ in multiple inheritance
class A:
    __slots__ = ('a',)

class B:
    __slots__ = ('b',)

class C(A, B):  # Error: multiple bases have instance lay-out conflict
    pass

# Correct: Use empty slots in one parent or don't use __slots__
class A:
    __slots__ = ('a',)

class B:
    __slots__ = ()  # Empty

class C(A, B):
    __slots__ = ('c',)
```

### Pitfall 5: Mutable Default with Sentinel

```python
# Wrong: Mutable default
def process(items=_MISSING):
    if items is _MISSING:
        items = []
    items.append('new')
    return items

# If you forget the check, you're back to mutable default problems

# Better: Use None if appropriate
def process(items=None):
    if items is None:
        items = []
    items.append('new')
    return items
```

## Performance Considerations

### __slots__ Memory Savings

```python
import sys

class Regular:
    def __init__(self):
        self.x = 1
        self.y = 2

class Slotted:
    __slots__ = ('x', 'y')

    def __init__(self):
        self.x = 1
        self.y = 2

# Regular: ~56 bytes + 112 bytes (__dict__) = ~168 bytes
# Slotted: ~56 bytes (no __dict__)
# Savings: ~66% per instance
# For 1 million instances: ~112 MB saved
```

### __getattribute__ Overhead

```python
# __getattribute__ is called for EVERY attribute access
# Can slow down code by 2-3x
# Use __getattr__ instead (only called when attribute not found)

# Slow:
class Logged:
    def __getattribute__(self, name):
        log_access(name)  # Every access logged
        return super().__getattribute__(name)

# Faster: Only log dynamic attributes
class Logged:
    def __getattr__(self, name):
        log_access(name)  # Only unknown attributes logged
        raise AttributeError(name)
```

### Enum Comparison Speed

```python
# Enum comparison is fast (identity check)
# IntEnum allows integer comparison but slightly slower than Enum

from enum import Enum, IntEnum
import timeit

class Status(Enum):
    A = 1

class IntStatus(IntEnum):
    A = 1

# Status.A == Status.A: ~50ns (identity check)
# IntStatus.A == 1: ~100ns (value comparison)
# Regular int comparison: ~30ns
```

## Debugging Tips

### Tip 1: Debugging __getattr__

```python
class Debug:
    def __getattr__(self, name):
        import traceback
        print(f"__getattr__ called for {name}")
        traceback.print_stack()
        raise AttributeError(name)

# Helps identify where dynamic attribute access occurs
```

### Tip 2: Inspecting Slots

```python
class Slotted:
    __slots__ = ('x', 'y')

# Check what slots are defined
print(Slotted.__slots__)

# Check if instance has __dict__
obj = Slotted()
print(hasattr(obj, '__dict__'))  # False

# Get all slots including inherited
def get_all_slots(cls):
    slots = set()
    for c in cls.__mro__:
        if hasattr(c, '__slots__'):
            slots.update(c.__slots__)
    return slots
```

### Tip 3: Enum Debugging

```python
from enum import Enum

class Status(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'

# Get enum by value
status = Status('active')

# Get enum by name
status = Status['ACTIVE']

# List all members
for member in Status:
    print(f"{member.name} = {member.value}")

# Check membership
print('ACTIVE' in Status.__members__)
```

## Real-World Patterns

### Pattern 1: Configuration with Inheritance

```python
class Config:
    """Hierarchical configuration with ellipsis inheritance."""

    def __init__(self, values, parent=None):
        self._values = values
        self._parent = parent

    def __getattr__(self, name):
        if name in self._values:
            value = self._values[name]
            if value is Ellipsis and self._parent:
                return getattr(self._parent, name)
            return value
        if self._parent:
            return getattr(self._parent, name)
        raise AttributeError(name)

# Usage
base = Config({'timeout': 30, 'retries': 3})
prod = Config({'timeout': ..., 'retries': 5}, parent=base)
```

### Pattern 2: Smart Cache with Sentinels

```python
from enum import Enum
import time

class CacheState(Enum):
    MISS = object()
    EXPIRED = object()

class SmartCache:
    def __init__(self):
        self._cache = {}
        self._ttl = {}

    def get(self, key):
        if key not in self._cache:
            return CacheState.MISS

        if key in self._ttl and time.time() > self._ttl[key]:
            del self._cache[key]
            del self._ttl[key]
            return CacheState.EXPIRED

        return self._cache[key]

    def set(self, key, value, ttl=None):
        self._cache[key] = value
        if ttl:
            self._ttl[key] = time.time() + ttl
```

### Pattern 3: Type Registry with __init_subclass__

```python
class Serializable:
    """Base class with automatic type registration."""

    _registry = {}

    def __init_subclass__(cls, type_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if type_name:
            cls._registry[type_name] = cls
            cls.type_name = type_name

    def to_dict(self):
        return {
            '__type__': self.type_name,
            **self.__dict__
        }

    @classmethod
    def from_dict(cls, data):
        type_name = data.pop('__type__')
        obj_class = cls._registry[type_name]
        return obj_class(**data)

# Usage
class User(Serializable, type_name='user'):
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User('Alice', 'alice@example.com')
data = user.to_dict()
restored = Serializable.from_dict(data)
```

## Key Takeaways

1. **Use niche features sparingly** - They're powerful but can make code harder to understand
2. **Ellipsis is for placeholders** - Type hints, stubs, and special use cases
3. **Walrus operator reduces duplication** - But don't sacrifice readability
4. **Parameter restrictions improve APIs** - Especially for public libraries
5. **Enums are better than constants** - Type safety and methods
6. **Sentinels distinguish nothing from None** - Important for APIs
7. **__getattr__ for dynamic attributes** - Avoid __getattribute__
8. **__slots__ for many instances** - Memory and performance
9. **__init_subclass__ for frameworks** - Auto-registration and validation
10. **Profile before optimizing** - Don't use __slots__ or other tricks prematurely

## Additional Resources

- PEP 572: Assignment Expressions (Walrus Operator)
- PEP 570: Positional-Only Parameters
- PEP 3102: Keyword-Only Arguments
- PEP 435: Adding an Enum type to Python
- PEP 562: Module __getattr__ and __dir__
- Python Data Model documentation
