# Tips & Best Practices: Advanced OOP & Metaclasses

## General Best Practices

### 1. The Metaclass Question

**Tim Peters' wisdom**: "Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don't."

**When you actually need metaclasses:**
- Building frameworks (Django, SQLAlchemy)
- Creating DSLs (Domain Specific Languages)
- Automatic class registration systems
- Complex API validation

**When you DON'T need metaclasses:**
- Simple attribute validation → Use descriptors or `__init_subclass__`
- Adding methods to classes → Use class decorators
- Property management → Use descriptors or `@property`
- Most application-level code

### 2. Prefer Simpler Alternatives

**Hierarchy of complexity (simplest to most complex):**

```python
# 1. Simple inheritance (usually sufficient)
class Base:
    def method(self):
        pass

# 2. Class decorators (explicit and readable)
@decorator
class MyClass:
    pass

# 3. __init_subclass__ (Python 3.6+, cleaner than metaclasses)
class Base:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

# 4. Descriptors (for attribute management)
class Descriptor:
    def __get__(self, instance, owner):
        pass

# 5. Metaclasses (most powerful, most complex)
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        pass
```

## Metaclass Tips

### Tip 1: Understand the Creation Process

```python
# When you write:
class MyClass(Base, metaclass=Meta):
    attribute = value

# Python does approximately this:
namespace = Meta.__prepare__('MyClass', (Base,), {})
namespace['attribute'] = value
MyClass = Meta.__new__(Meta, 'MyClass', (Base,), namespace)
Meta.__init__(MyClass, 'MyClass', (Base,), namespace)
```

### Tip 2: Use `__prepare__` for Custom Namespaces

```python
class OrderedMeta(type):
    """Metaclass that preserves attribute definition order"""

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        # Return custom namespace (before Python 3.7 this was necessary)
        from collections import OrderedDict
        return OrderedDict()

    def __new__(mcs, name, bases, namespace, **kwargs):
        # namespace is now an OrderedDict
        cls = super().__new__(mcs, name, bases, dict(namespace))
        cls._field_order = list(namespace.keys())
        return cls
```

**Note**: In Python 3.7+, regular dicts maintain insertion order, making this less necessary.

### Tip 3: Handle Multiple Inheritance Correctly

```python
class Meta1(type):
    pass

class Meta2(type):
    pass

# This will fail - metaclass conflict
# class MyClass(metaclass=Meta1):
#     pass
# class SubClass(MyClass, metaclass=Meta2):
#     pass

# Solution: Create a metaclass that inherits from both
class CombinedMeta(Meta1, Meta2):
    pass

class MyClass(metaclass=CombinedMeta):
    pass
```

### Tip 4: Don't Forget super()

```python
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        # ALWAYS call super().__new__
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, namespace):
        # ALWAYS call super().__init__
        super().__init__(name, bases, namespace)
```

## Descriptor Tips

### Tip 5: Use `__set_name__` (Python 3.6+)

```python
# Old way (manual name setting)
class OldDescriptor:
    def __init__(self, name):
        self.name = name

class MyClass:
    attr = OldDescriptor('attr')  # Redundant!

# New way (automatic)
class NewDescriptor:
    def __set_name__(self, owner, name):
        self.name = name  # Automatically set

class MyClass:
    attr = NewDescriptor()  # Clean!
```

### Tip 6: Avoid Memory Leaks in Descriptors

```python
# BAD: Memory leak - instances never garbage collected
class LeakyDescriptor:
    def __init__(self):
        self.data = {}  # Keyed by instance id

    def __get__(self, instance, owner):
        return self.data.get(id(instance))

    def __set__(self, instance, value):
        self.data[id(instance)] = value
        # Instance is deleted but data[id] remains!

# GOOD: Use weakref to allow garbage collection
import weakref

class SafeDescriptor:
    def __init__(self):
        self.data = weakref.WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data.get(instance)

    def __set__(self, instance, value):
        self.data[instance] = value
```

### Tip 7: Data vs Non-Data Descriptors

```python
# Data descriptor (has __set__ or __delete__)
class DataDescriptor:
    def __get__(self, instance, owner):
        return "data"

    def __set__(self, instance, value):
        pass
    # Takes precedence over instance __dict__

# Non-data descriptor (only has __get__)
class NonDataDescriptor:
    def __get__(self, instance, owner):
        return "non-data"
    # Instance __dict__ takes precedence

class Example:
    data = DataDescriptor()
    non_data = NonDataDescriptor()

e = Example()
e.__dict__['data'] = 'override'
e.__dict__['non_data'] = 'override'

print(e.data)      # "data" - descriptor wins
print(e.non_data)  # "override" - instance dict wins
```

## `__init_subclass__` Tips

### Tip 8: Use for Simple Class Customization

```python
# GOOD: Simple and readable
class Base:
    def __init_subclass__(cls, required=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if required and not hasattr(cls, required):
            raise TypeError(f"Must define {required}")

class Sub(Base, required='method'):
    def method(self):
        pass

# BAD: Overkill with metaclass
class Meta(type):
    def __new__(mcs, name, bases, namespace, required=None):
        # ... complex metaclass code ...
        pass
```

### Tip 9: Always Call super().__init_subclass__()

```python
class Base:
    def __init_subclass__(cls, **kwargs):
        # ALWAYS call super() to support multiple inheritance
        super().__init_subclass__(**kwargs)
        # Your customization here
```

### Tip 10: Use Keyword Arguments

```python
class Base:
    def __init_subclass__(cls, plugin_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if plugin_name:
            # Register plugin
            pass

# Clear and explicit
class Plugin(Base, plugin_name='my_plugin'):
    pass

# vs less clear:
# class Plugin(Base, 'my_plugin'):  # Positional - avoid!
```

## Class Decorator Tips

### Tip 11: Preserve Class Metadata

```python
from functools import wraps

def my_decorator(cls):
    # Preserve original class name, docstring, etc.
    original_init = cls.__init__

    @wraps(original_init)
    def new_init(self, *args, **kwargs):
        # Custom logic
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls
```

### Tip 12: Decorators Can Return Different Classes

```python
def singleton(cls):
    """Decorator that returns a different class"""
    class SingletonClass(cls):
        _instance = None

        def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

    SingletonClass.__name__ = cls.__name__
    SingletonClass.__qualname__ = cls.__qualname__
    return SingletonClass

@singleton
class Database:
    pass

# All instances are the same
db1 = Database()
db2 = Database()
assert db1 is db2
```

## Common Gotchas

### Gotcha 1: Metaclass Inheritance

```python
# Gotcha: Metaclass is inherited
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Creating {name}")
        return super().__new__(mcs, name, bases, namespace)

class Base(metaclass=Meta):  # Prints: Creating Base
    pass

class Child(Base):  # Prints: Creating Child (inherited metaclass!)
    pass
```

### Gotcha 2: Descriptor Instance Binding

```python
# Gotcha: Descriptor is a class attribute, shared by all instances
class Descriptor:
    def __init__(self):
        self.value = None  # WRONG: Shared between instances!

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

class Example:
    attr = Descriptor()

e1 = Example()
e2 = Example()
e1.attr = 1
print(e2.attr)  # 1 (unexpected!)

# Fix: Store per-instance data
class CorrectDescriptor:
    def __init__(self):
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(id(instance))

    def __set__(self, instance, value):
        self.data[id(instance)] = value
```

### Gotcha 3: Descriptor on Instance vs Class

```python
class Descriptor:
    def __get__(self, instance, owner):
        if instance is None:
            # Accessed from class
            return self
        # Accessed from instance
        return "value"

class Example:
    attr = Descriptor()

print(Example.attr)      # <Descriptor object>
print(Example().attr)    # "value"
```

### Gotcha 4: Multiple Metaclasses

```python
# Gotcha: Can't have multiple unrelated metaclasses
class Meta1(type):
    pass

class Meta2(type):
    pass

class A(metaclass=Meta1):
    pass

# This raises TypeError: metaclass conflict
# class B(A, metaclass=Meta2):
#     pass

# Fix: Create combined metaclass
class CombinedMeta(Meta1, Meta2):
    pass

class B(A, metaclass=CombinedMeta):
    pass
```

### Gotcha 5: __init_subclass__ vs Metaclass Timing

```python
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Meta.__new__: {name}")
        return super().__new__(mcs, name, bases, namespace)

class Base(metaclass=Meta):
    def __init_subclass__(cls, **kwargs):
        print(f"Base.__init_subclass__: {cls.__name__}")
        super().__init_subclass__(**kwargs)

class Child(Base):
    pass

# Output:
# Meta.__new__: Base
# Meta.__new__: Child
# Base.__init_subclass__: Child

# __new__ runs first, then __init_subclass__
```

## Performance Tips

### Tip 13: Metaclasses Are Not Free

```python
# Metaclass adds overhead at class creation time
# Usually negligible, but matters for dynamic class generation

import time

# Without metaclass
start = time.time()
for i in range(10000):
    class A:
        pass
print(f"Without metaclass: {time.time() - start:.4f}s")

# With metaclass
class Meta(type):
    pass

start = time.time()
for i in range(10000):
    class B(metaclass=Meta):
        pass
print(f"With metaclass: {time.time() - start:.4f}s")
```

### Tip 14: Cache Descriptor Lookups

```python
# Expensive descriptor that benefits from caching
class ExpensiveDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self

        # Compute expensive value
        value = self.compute_expensive_value()

        # Cache by replacing descriptor with value
        setattr(instance, self.name, value)
        return value
```

## Debugging Tips

### Tip 15: Add Verbose Mode to Metaclasses

```python
class VerboseMeta(type):
    verbose = False  # Class attribute for debugging

    def __new__(mcs, name, bases, namespace, **kwargs):
        if mcs.verbose:
            print(f"Creating class: {name}")
            print(f"  Bases: {bases}")
            print(f"  Attributes: {list(namespace.keys())}")
        return super().__new__(mcs, name, bases, namespace)

# Enable during development
VerboseMeta.verbose = True

class MyClass(metaclass=VerboseMeta):
    x = 1
```

### Tip 16: Use `__repr__` for Descriptors

```python
class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f"<Descriptor: {self.name}>"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, f'_{self.name}', None)
```

## Real-World Patterns

### Pattern 1: Registry Pattern

```python
# Useful for plugin systems
class PluginRegistry:
    plugins = {}

    def __init_subclass__(cls, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if name:
            PluginRegistry.plugins[name] = cls
```

### Pattern 2: Validation Framework

```python
# Used in ORMs and validation libraries
class Field:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value
```

### Pattern 3: Singleton Pattern

```python
# Ensure only one instance exists
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
```

## Testing Advanced Features

### Tip 17: Test Metaclass Behavior

```python
import unittest

class TestMeta(unittest.TestCase):
    def test_metaclass_creation(self):
        """Test that metaclass properly creates classes"""
        class Meta(type):
            def __new__(mcs, name, bases, namespace):
                namespace['added_by_meta'] = True
                return super().__new__(mcs, name, bases, namespace)

        class MyClass(metaclass=Meta):
            pass

        self.assertTrue(hasattr(MyClass, 'added_by_meta'))
        self.assertTrue(MyClass.added_by_meta)
```

### Tip 18: Test Descriptor Validation

```python
def test_descriptor_validation(self):
    """Test that descriptor properly validates values"""
    class IntField:
        def __set__(self, instance, value):
            if not isinstance(value, int):
                raise TypeError("Must be int")
            instance.__dict__[self.name] = value

        def __set_name__(self, owner, name):
            self.name = name

    class Example:
        number = IntField()

    e = Example()
    e.number = 42  # Should work
    with self.assertRaises(TypeError):
        e.number = "not an int"
```

## Key Takeaways

1. **Start simple**: Use built-in features before custom metaclasses
2. **Metaclasses are powerful**: But usually overkill for application code
3. **__init_subclass__ is cleaner**: Use it instead of metaclasses when possible
4. **Descriptors for attribute control**: Perfect for validation and computed properties
5. **Class decorators for explicit modifications**: Readable and Pythonic
6. **Test thoroughly**: Advanced features can have subtle bugs
7. **Document extensively**: These features are complex and need good docs
8. **Profile if performance matters**: Some patterns have overhead

## Further Reading

- PEP 3115: Metaclasses in Python 3
- PEP 487: Simpler customization of class creation
- PEP 520: Preserving Class Attribute Definition Order
- Descriptor HowTo Guide (Python docs)
- David Beazley's "Python 3 Metaprogramming" tutorial

Understanding these advanced features will help you read sophisticated Python code and design better APIs, but remember: with great power comes great responsibility. Use these tools judiciously.
