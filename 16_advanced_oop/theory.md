# Theory: Advanced OOP & Metaclasses

## 1. Understanding Metaclasses

### What Are Metaclasses?

In Python, everything is an object, including classes. A metaclass is the class of a class - it defines how classes behave.

```python
# Classes are instances of their metaclass
class MyClass:
    pass

print(type(MyClass))  # <class 'type'>
print(type(type))     # <class 'type'>
```

The default metaclass is `type`. When you define a class, Python actually calls:
```python
MyClass = type('MyClass', (object,), {'attribute': value})
```

### Creating Custom Metaclasses

```python
class Meta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        # Called when creating the class
        print(f"Creating class {name}")
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, namespace, **kwargs):
        # Called after the class is created
        print(f"Initializing class {name}")
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        # Called when creating instances of the class
        print(f"Creating instance of {cls.__name__}")
        return super().__call__(*args, **kwargs)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
```

### When to Use Metaclasses

Use metaclasses for:
- Automatic registration of classes
- API validation
- Modifying class attributes automatically
- Adding methods to classes dynamically
- Enforcing coding standards

**Rule of thumb**: If you're not sure whether you need a metaclass, you probably don't. They're powerful but often overkill.

## 2. The `__init_subclass__` Hook

Python 3.6+ introduced a simpler alternative to metaclasses for many use cases.

```python
class Base:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"Subclass {cls.__name__} created")

        # Validate or modify the subclass
        if not hasattr(cls, 'required_attribute'):
            raise TypeError(f"{cls.__name__} must define 'required_attribute'")

class Valid(Base):
    required_attribute = "value"

# This will raise TypeError:
# class Invalid(Base):
#     pass
```

### Use Cases for `__init_subclass__`

1. **Plugin Registration**:
```python
class PluginBase:
    plugins = {}

    def __init_subclass__(cls, plugin_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if plugin_name:
            cls.plugins[plugin_name] = cls

class JSONPlugin(PluginBase, plugin_name='json'):
    pass

print(PluginBase.plugins)  # {'json': <class 'JSONPlugin'>}
```

2. **Abstract Method Enforcement**:
```python
class RequiresMethods:
    required_methods = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        for method in cls.required_methods:
            if not hasattr(cls, method):
                raise TypeError(f"Must implement {method}")
```

## 3. Class Decorators

Class decorators modify or enhance class definitions.

```python
def add_str_method(cls):
    """Decorator that adds a __str__ method"""
    def __str__(self):
        return f"{cls.__name__} instance"
    cls.__str__ = __str__
    return cls

@add_str_method
class MyClass:
    pass

obj = MyClass()
print(obj)  # MyClass instance
```

### Parametrized Class Decorators

```python
def register(registry):
    """Register classes in a registry"""
    def decorator(cls):
        registry[cls.__name__] = cls
        return cls
    return decorator

CLASSES = {}

@register(CLASSES)
class MyClass:
    pass

print(CLASSES)  # {'MyClass': <class 'MyClass'>}
```

### Class Decorators vs Metaclasses

Use class decorators when:
- You need to modify a single class
- The modification is straightforward
- You want explicit, readable code

Use metaclasses when:
- You need to affect all subclasses
- You need to control class creation
- You're building a framework

## 4. Descriptors Protocol

Descriptors control attribute access. They define `__get__`, `__set__`, and/or `__delete__` methods.

### Data Descriptors

Data descriptors define both `__get__` and `__set__`:

```python
class Validator:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        self.data = {}

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(id(instance), None)

    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be <= {self.max_value}")
        self.data[id(instance)] = value

    def __delete__(self, instance):
        del self.data[id(instance)]

class Person:
    age = Validator(min_value=0, max_value=150)

    def __init__(self, age):
        self.age = age

person = Person(30)
# person.age = 200  # Raises ValueError
```

### Non-Data Descriptors

Non-data descriptors only define `__get__`:

```python
class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self

        # Compute value and cache it
        value = self.function(instance)
        setattr(instance, self.name, value)
        return value

class DataProcessor:
    @LazyProperty
    def expensive_operation(self):
        print("Computing...")
        return sum(range(1000000))

processor = DataProcessor()
print(processor.expensive_operation)  # Computing... then result
print(processor.expensive_operation)  # Just result (cached)
```

### Descriptor Use Cases

- Property validation
- Lazy evaluation
- Type checking
- Logging attribute access
- Database field definitions (ORMs)

## 5. Dynamic Class Creation

### Using `type()` Directly

```python
# Dynamically create a class
def method(self):
    return "Hello"

DynamicClass = type(
    'DynamicClass',           # Class name
    (object,),                # Base classes
    {                         # Namespace
        'attribute': 42,
        'method': method
    }
)

obj = DynamicClass()
print(obj.method())  # Hello
print(obj.attribute)  # 42
```

### Using `types.new_class()`

```python
import types

def class_callback(namespace):
    namespace['attribute'] = 42

DynamicClass = types.new_class(
    'DynamicClass',
    (object,),
    exec_body=class_callback
)
```

### Practical Use: Factory Pattern

```python
def create_model_class(name, fields):
    """Factory for creating model classes"""
    def __init__(self, **kwargs):
        for field in fields:
            setattr(self, field, kwargs.get(field))

    def __repr__(self):
        values = ', '.join(f"{f}={getattr(self, f)}" for f in fields)
        return f"{name}({values})"

    namespace = {
        '__init__': __init__,
        '__repr__': __repr__,
        'fields': fields
    }

    return type(name, (object,), namespace)

User = create_model_class('User', ['name', 'email'])
user = User(name='Alice', email='alice@example.com')
print(user)  # User(name=Alice, email=alice@example.com)
```

## 6. Abstract Base Classes (Advanced)

### Beyond Basic ABC

```python
from abc import ABC, abstractmethod, ABCMeta
from typing import Protocol

class AdvancedABC(ABC):
    @abstractmethod
    def required_method(self):
        """Must be implemented by subclasses"""
        pass

    @abstractmethod
    def another_required_method(self):
        """Another required method"""
        pass

    def optional_method(self):
        """Can be optionally overridden"""
        return "default implementation"

    @classmethod
    def __subclasshook__(cls, subclass):
        """Allow duck typing - check if subclass has required methods"""
        if cls is AdvancedABC:
            has_methods = (
                hasattr(subclass, 'required_method') and
                callable(subclass.required_method) and
                hasattr(subclass, 'another_required_method') and
                callable(subclass.another_required_method)
            )
            return has_methods
        return NotImplemented
```

### Virtual Subclasses

```python
from abc import ABC

class MyABC(ABC):
    @abstractmethod
    def method(self):
        pass

class UnrelatedClass:
    def method(self):
        return "implemented"

# Register as virtual subclass
MyABC.register(UnrelatedClass)

obj = UnrelatedClass()
print(isinstance(obj, MyABC))  # True (virtual subclass)
```

### Protocol Classes (Python 3.8+)

For structural subtyping (duck typing with type checking):

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

# Circle satisfies Drawable protocol (structural typing)
def render(obj: Drawable) -> None:
    obj.draw()

render(Circle())  # Type checker accepts this
```

## 7. Combining Techniques

### Example: ORM-like Field System

```python
class Field:
    """Base descriptor for fields"""
    def __init__(self, default=None):
        self.default = default
        self.data = {}

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(id(instance), self.default)

    def __set__(self, instance, value):
        self.validate(value)
        self.data[id(instance)] = value

    def validate(self, value):
        pass

class IntegerField(Field):
    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")

class StringField(Field):
    def __init__(self, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.max_length = max_length

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string")
        if self.max_length and len(value) > self.max_length:
            raise ValueError(f"{self.name} exceeds max length {self.max_length}")

class ModelMeta(type):
    """Metaclass for models"""
    def __new__(mcs, name, bases, namespace):
        # Collect fields
        fields = {}
        for key, value in namespace.items():
            if isinstance(value, Field):
                fields[key] = value

        namespace['_fields'] = fields
        return super().__new__(mcs, name, bases, namespace)

class Model(metaclass=ModelMeta):
    """Base model class"""
    def __init__(self, **kwargs):
        for name in self._fields:
            setattr(self, name, kwargs.get(name, self._fields[name].default))

    def __repr__(self):
        values = ', '.join(f"{k}={getattr(self, k)}" for k in self._fields)
        return f"{self.__class__.__name__}({values})"

# Usage
class User(Model):
    name = StringField(max_length=50)
    age = IntegerField()
    email = StringField()

user = User(name="Alice", age=30, email="alice@example.com")
print(user)  # User(name=Alice, age=30, email=alice@example.com)
```

## Key Takeaways

1. **Metaclasses** control class creation and are the most powerful customization mechanism
2. **`__init_subclass__`** provides a simpler alternative for many metaclass use cases
3. **Class decorators** offer explicit, readable class modification
4. **Descriptors** control attribute access and enable sophisticated property systems
5. **Dynamic class creation** enables runtime flexibility and factory patterns
6. **Abstract base classes** enforce contracts and enable both nominal and structural typing

## When to Use Each Tool

| Tool | Use When |
|------|----------|
| Metaclass | Affecting all subclasses, controlling class creation, framework design |
| `__init_subclass__` | Validating subclasses, plugin registration, simpler than metaclasses |
| Class decorator | Modifying single classes, explicit modifications |
| Descriptor | Controlling attribute access, validation, lazy properties |
| Dynamic classes | Runtime class generation, factory patterns |
| ABC | Enforcing interfaces, structural typing |

## Common Pitfalls

1. **Overusing metaclasses**: They're powerful but complex. Use simpler alternatives when possible.
2. **Descriptor naming**: Forgetting `__set_name__` can cause issues with attribute names.
3. **Memory leaks**: Descriptors using `self.data = {}` with instance IDs can leak memory without proper cleanup.
4. **Order matters**: Metaclass resolution follows MRO (Method Resolution Order).
5. **Type checking**: Dynamic classes may not play well with static type checkers.

Understanding these advanced concepts will help you read sophisticated Python code and design better APIs and frameworks.
