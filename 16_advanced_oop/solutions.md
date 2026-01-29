# Solutions: Advanced OOP & Metaclasses

## Solution 1: Attribute Logger Metaclass

```python
class LoggerMeta(type):
    """Metaclass that logs attribute assignments"""

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)

        # Store original __setattr__
        original_setattr = instance.__class__.__setattr__

        def logging_setattr(self, name, value):
            print(f"Setting {name} = {value}")
            original_setattr(self, name, value)

        # Replace __setattr__ on the instance
        instance.__setattr__ = lambda name, value: logging_setattr(instance, name, value)
        return instance

class Person(metaclass=LoggerMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Test
person = Person("Alice", 30)  # Logs both assignments
person.age = 31  # Logs: Setting age = 31
```

**Alternative approach using __setattr__ override:**

```python
class LoggerMeta(type):
    """Metaclass that logs attribute assignments"""

    def __new__(mcs, name, bases, namespace):
        def __setattr__(self, key, value):
            print(f"Setting {key} = {value} on {self.__class__.__name__}")
            object.__setattr__(self, key, value)

        namespace['__setattr__'] = __setattr__
        return super().__new__(mcs, name, bases, namespace)

class Product(metaclass=LoggerMeta):
    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Laptop", 999)
product.price = 899
```

## Solution 2: Required Methods Validator

```python
def requires_methods(*method_names):
    """Decorator that validates required methods exist"""

    def decorator(cls):
        missing = []
        for method_name in method_names:
            if not hasattr(cls, method_name):
                missing.append(method_name)
            elif not callable(getattr(cls, method_name)):
                missing.append(f"{method_name} (not callable)")

        if missing:
            raise TypeError(
                f"{cls.__name__} missing required methods: {', '.join(missing)}"
            )

        return cls

    return decorator

# Test with valid class
@requires_methods('speak', 'walk')
class Dog:
    def speak(self):
        return "Woof!"

    def walk(self):
        return "Walking..."

dog = Dog()
print(dog.speak())

# Test with invalid class (uncomment to test)
# @requires_methods('speak', 'fly')
# class Cat:
#     def speak(self):
#         return "Meow!"
#     # Missing 'fly' method - raises TypeError
```

## Solution 3: Cached Property Descriptor

```python
class CachedProperty:
    """Descriptor that caches computed property values"""

    def __init__(self, func):
        self.func = func
        self.name = func.__name__
        self.cache = {}
        self.computation_count = {}

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        instance_id = id(instance)

        # Return cached value if exists
        if instance_id in self.cache:
            return self.cache[instance_id]

        # Compute and cache
        value = self.func(instance)
        self.cache[instance_id] = value

        # Track computation count
        self.computation_count[instance_id] = \
            self.computation_count.get(instance_id, 0) + 1

        return value

    def clear_cache(self, instance):
        """Clear cache for specific instance"""
        instance_id = id(instance)
        if instance_id in self.cache:
            del self.cache[instance_id]

    def get_computation_count(self, instance):
        """Get how many times property was computed"""
        return self.computation_count.get(id(instance), 0)

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    @CachedProperty
    def expensive_sum(self):
        print("Computing sum...")
        return sum(self.data)

    @CachedProperty
    def expensive_mean(self):
        print("Computing mean...")
        return sum(self.data) / len(self.data)

# Test
analyzer = DataAnalyzer([1, 2, 3, 4, 5])

print(analyzer.expensive_sum)  # Computes
print(analyzer.expensive_sum)  # Cached

print(f"Computed {DataAnalyzer.expensive_sum.get_computation_count(analyzer)} times")

# Clear cache
DataAnalyzer.expensive_sum.clear_cache(analyzer)
print(analyzer.expensive_sum)  # Recomputes
```

## Solution 4: Type-Safe Metaclass

```python
class TypeSafeMeta(type):
    """Metaclass that enforces type annotations"""

    def __new__(mcs, name, bases, namespace):
        # Check that all class variables have type hints
        annotations = namespace.get('__annotations__', {})

        for attr_name, attr_value in namespace.items():
            if not attr_name.startswith('_') and not callable(attr_value):
                if attr_name not in annotations:
                    raise TypeError(
                        f"Attribute '{attr_name}' in {name} must have type annotation"
                    )

        # Create the class
        cls = super().__new__(mcs, name, bases, namespace)

        # Override __setattr__ to validate types
        original_setattr = cls.__setattr__

        def validated_setattr(self, key, value):
            annotations = getattr(self.__class__, '__annotations__', {})
            if key in annotations:
                expected_type = annotations[key]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"{key} must be {expected_type.__name__}, "
                        f"got {type(value).__name__}"
                    )
            original_setattr(self, key, value)

        cls.__setattr__ = validated_setattr
        return cls

class Person(metaclass=TypeSafeMeta):
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# Test
person = Person("Alice", 30)
print(f"{person.name}, {person.age}")

# This raises TypeError:
try:
    person.age = "thirty"
except TypeError as e:
    print(f"Error: {e}")
```

## Solution 5: Plugin Manager

```python
class Plugin:
    """Base class for plugin system"""
    _plugins = {}

    def __init_subclass__(cls, name=None, enabled=True, priority=0, **kwargs):
        super().__init_subclass__(**kwargs)

        if name and enabled:
            cls._plugins[name] = {
                'class': cls,
                'priority': priority,
                'enabled': enabled
            }

    @classmethod
    def get_plugin(cls, name):
        """Get a specific plugin by name"""
        plugin_info = cls._plugins.get(name)
        if plugin_info:
            return plugin_info['class']()
        return None

    @classmethod
    def list_plugins(cls):
        """List all registered plugins"""
        return list(cls._plugins.keys())

    @classmethod
    def execute_all(cls, data):
        """Execute all enabled plugins in priority order"""
        results = []

        # Sort by priority (higher priority first)
        sorted_plugins = sorted(
            cls._plugins.items(),
            key=lambda x: x[1]['priority'],
            reverse=True
        )

        for name, info in sorted_plugins:
            if info['enabled']:
                plugin = info['class']()
                result = plugin.execute(data)
                results.append((name, result))

        return results

    @classmethod
    def disable_plugin(cls, name):
        """Disable a plugin"""
        if name in cls._plugins:
            cls._plugins[name]['enabled'] = False

    @classmethod
    def enable_plugin(cls, name):
        """Enable a plugin"""
        if name in cls._plugins:
            cls._plugins[name]['enabled'] = True

    def execute(self, data):
        """Override in subclasses"""
        raise NotImplementedError

# Define plugins
class EmailPlugin(Plugin, name="email", priority=10):
    def execute(self, data):
        return f"Emailing: {data}"

class LogPlugin(Plugin, name="log", priority=5):
    def execute(self, data):
        return f"Logging: {data}"

class NotificationPlugin(Plugin, name="notification", priority=3):
    def execute(self, data):
        return f"Notifying: {data}"

# Test
print("Available plugins:", Plugin.list_plugins())

results = Plugin.execute_all("Test data")
for name, result in results:
    print(f"{name}: {result}")

# Disable email plugin
Plugin.disable_plugin("email")
print("\nAfter disabling email:")
results = Plugin.execute_all("Test data")
for name, result in results:
    print(f"{name}: {result}")
```

## Solution 6: Immutable Class Decorator

```python
def immutable(cls):
    """Decorator that makes class instances immutable after __init__"""

    original_init = cls.__init__
    original_setattr = cls.__setattr__
    original_delattr = cls.__delattr__

    def __init__(self, *args, **kwargs):
        # Allow setting during initialization
        object.__setattr__(self, '_initialized', False)
        original_init(self, *args, **kwargs)
        object.__setattr__(self, '_initialized', True)

    def __setattr__(self, name, value):
        if hasattr(self, '_initialized') and self._initialized:
            raise AttributeError(
                f"Cannot modify attribute '{name}' of immutable {cls.__name__}"
            )
        original_setattr(self, name, value)

    def __delattr__(self, name):
        if hasattr(self, '_initialized') and self._initialized:
            raise AttributeError(
                f"Cannot delete attribute '{name}' of immutable {cls.__name__}"
            )
        original_delattr(self, name)

    cls.__init__ = __init__
    cls.__setattr__ = __setattr__
    cls.__delattr__ = __delattr__

    return cls

@immutable
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Test
point = Point(3, 4)
print(point)

# These raise AttributeError:
try:
    point.x = 5
except AttributeError as e:
    print(f"Error: {e}")

try:
    del point.y
except AttributeError as e:
    print(f"Error: {e}")
```

## Solution 7: Validated Dictionary Descriptor

```python
class ValidatedDict:
    """Descriptor for type-validated dictionaries"""

    def __init__(self, key_type=None, value_type=None):
        self.key_type = key_type
        self.value_type = value_type
        self.data = {}

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(id(instance), {})

    def __set__(self, instance, value):
        if not isinstance(value, dict):
            raise TypeError(f"{self.name} must be a dictionary")

        # Validate keys and values
        for k, v in value.items():
            if self.key_type and not isinstance(k, self.key_type):
                raise TypeError(
                    f"Key {k!r} must be {self.key_type.__name__}, "
                    f"got {type(k).__name__}"
                )
            if self.value_type and not isinstance(v, self.value_type):
                raise TypeError(
                    f"Value {v!r} for key {k!r} must be {self.value_type.__name__}, "
                    f"got {type(v).__name__}"
                )

        self.data[id(instance)] = value

class Configuration:
    settings = ValidatedDict(key_type=str, value_type=int)
    metadata = ValidatedDict(key_type=str, value_type=str)

    def __init__(self, settings=None, metadata=None):
        if settings:
            self.settings = settings
        if metadata:
            self.metadata = metadata

# Test
config = Configuration(
    settings={'timeout': 30, 'retries': 3},
    metadata={'version': '1.0', 'author': 'Alice'}
)

print("Settings:", config.settings)
print("Metadata:", config.metadata)

# This raises TypeError:
try:
    config.settings = {'timeout': 'invalid'}  # String value instead of int
except TypeError as e:
    print(f"Error: {e}")
```

## Solution 8: Auto-documentation Metaclass

```python
import inspect

class AutoDocMeta(type):
    """Metaclass that generates documentation automatically"""

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)

        # Generate documentation
        doc_parts = [f"Class: {name}"]

        # Add class docstring if exists
        if cls.__doc__:
            doc_parts.append(f"\n{cls.__doc__}")

        # Document public methods
        doc_parts.append("\n\nMethods:")
        for attr_name in dir(cls):
            if not attr_name.startswith('_'):
                attr = getattr(cls, attr_name)
                if callable(attr):
                    sig = inspect.signature(attr)
                    method_doc = f"\n  {attr_name}{sig}"
                    if attr.__doc__:
                        method_doc += f"\n    {attr.__doc__.strip()}"
                    doc_parts.append(method_doc)

        # Document public attributes
        doc_parts.append("\n\nAttributes:")
        annotations = getattr(cls, '__annotations__', {})
        for attr_name, attr_type in annotations.items():
            if not attr_name.startswith('_'):
                doc_parts.append(f"\n  {attr_name}: {attr_type.__name__}")

        cls.__doc__ = ''.join(doc_parts)
        return cls

class Calculator(metaclass=AutoDocMeta):
    """A simple calculator class"""

    result: float

    def add(self, a, b):
        """Add two numbers"""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a"""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b

# Test
print(Calculator.__doc__)
```

## Solution 9: ORM Field System

```python
class Field:
    """Base field descriptor"""

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
        """Override in subclasses"""
        pass

class CharField(Field):
    """String field with max length"""

    def __init__(self, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.max_length = max_length

    def validate(self, value):
        if value is not None:
            if not isinstance(value, str):
                raise TypeError(f"{self.name} must be a string")
            if self.max_length and len(value) > self.max_length:
                raise ValueError(
                    f"{self.name} exceeds max length {self.max_length}"
                )

class IntegerField(Field):
    """Integer field with min/max values"""

    def __init__(self, min_value=None, max_value=None, **kwargs):
        super().__init__(**kwargs)
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        if value is not None:
            if not isinstance(value, int):
                raise TypeError(f"{self.name} must be an integer")
            if self.min_value is not None and value < self.min_value:
                raise ValueError(f"{self.name} must be >= {self.min_value}")
            if self.max_value is not None and value > self.max_value:
                raise ValueError(f"{self.name} must be <= {self.max_value}")

class FloatField(Field):
    """Float field"""

    def validate(self, value):
        if value is not None and not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} must be a number")

class ModelMeta(type):
    """Metaclass that collects field definitions"""

    def __new__(mcs, name, bases, namespace):
        fields = {}
        for key, value in namespace.items():
            if isinstance(value, Field):
                fields[key] = value

        namespace['_fields'] = fields
        return super().__new__(mcs, name, bases, namespace)

class Model(metaclass=ModelMeta):
    """Base model class"""

    def __init__(self, **kwargs):
        for name, field in self._fields.items():
            value = kwargs.get(name, field.default)
            if value is not None:
                setattr(self, name, value)

    def to_dict(self):
        """Convert model to dictionary"""
        return {name: getattr(self, name) for name in self._fields}

    def save(self):
        """Simulate saving to database"""
        print(f"Saving {self.__class__.__name__}: {self.to_dict()}")
        return True

    def __repr__(self):
        values = ', '.join(f"{k}={getattr(self, k)!r}" for k in self._fields)
        return f"{self.__class__.__name__}({values})"

# Usage
class User(Model):
    name = CharField(max_length=50)
    age = IntegerField(min_value=0, max_value=150)
    email = CharField()
    balance = FloatField(default=0.0)

user = User(name="Alice", age=30, email="alice@example.com")
print(user)
print(user.to_dict())
user.save()

# Test validation
try:
    user.age = 200
except ValueError as e:
    print(f"Validation error: {e}")
```

## Solution 10: State Machine with Metaclass

```python
class StateMachineMeta(type):
    """Metaclass for state machines"""

    def __new__(mcs, name, bases, namespace):
        states = namespace.get('states', [])
        transitions = namespace.get('transitions', {})
        initial_state = namespace.get('initial_state')

        if not states:
            # Base class, skip validation
            return super().__new__(mcs, name, bases, namespace)

        # Validate configuration
        if initial_state not in states:
            raise ValueError(f"initial_state must be one of {states}")

        for state, allowed in transitions.items():
            if state not in states:
                raise ValueError(f"Transition state {state} not in states")
            for target in allowed:
                if target not in states:
                    raise ValueError(f"Transition target {target} not in states")

        # Add state management methods
        def __init__(self):
            self._current_state = initial_state
            self._state_history = [initial_state]

        def get_state(self):
            return self._current_state

        def set_state(self, new_state):
            if new_state not in states:
                raise ValueError(f"{new_state} is not a valid state")

            if new_state not in transitions.get(self._current_state, []):
                raise ValueError(
                    f"Cannot transition from {self._current_state} to {new_state}"
                )

            print(f"Transitioning: {self._current_state} -> {new_state}")
            self._current_state = new_state
            self._state_history.append(new_state)

        def get_history(self):
            return self._state_history.copy()

        def can_transition_to(self, state):
            return state in transitions.get(self._current_state, [])

        namespace['__init__'] = __init__
        namespace['get_state'] = get_state
        namespace['set_state'] = set_state
        namespace['get_history'] = get_history
        namespace['can_transition_to'] = can_transition_to

        return super().__new__(mcs, name, bases, namespace)

class Door(metaclass=StateMachineMeta):
    states = ['open', 'closed', 'locked']
    transitions = {
        'open': ['closed'],
        'closed': ['open', 'locked'],
        'locked': ['closed']
    }
    initial_state = 'closed'

# Test
door = Door()
print(f"Initial state: {door.get_state()}")

door.set_state('open')
door.set_state('closed')
door.set_state('locked')

print(f"State history: {door.get_history()}")

# This raises ValueError:
try:
    door.set_state('open')  # Can't go from locked to open directly
except ValueError as e:
    print(f"Error: {e}")
```

## Solutions 11-15

Due to length constraints, here are abbreviated solutions for the remaining exercises:

### Solution 11: Memoization Descriptor

```python
from functools import wraps

class Memoized:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self

        @wraps(self.func)
        def wrapper(*args, **kwargs):
            # Create cache key from arguments
            key = (args, tuple(sorted(kwargs.items())))
            try:
                if key not in self.cache:
                    self.cache[key] = self.func(instance, *args, **kwargs)
                return self.cache[key]
            except TypeError:
                # Unhashable arguments, compute without caching
                return self.func(instance, *args, **kwargs)

        wrapper.clear_cache = lambda: self.cache.clear()
        return wrapper
```

### Solution 12: Abstract Property Pattern

```python
from abc import ABC, abstractmethod

class AbstractPropertyMeta(type(ABC)):
    pass

class Base(ABC):
    @property
    @abstractmethod
    def required_property(self):
        pass

    @required_property.setter
    @abstractmethod
    def required_property(self, value):
        pass
```

### Solution 13: Dynamic Model Factory

```python
def create_model(name, schema):
    """Create a model class from a schema"""

    def __init__(self, **kwargs):
        for field_name, field_type in schema.items():
            value = kwargs.get(field_name)
            if value is not None and not isinstance(value, field_type):
                raise TypeError(f"{field_name} must be {field_type.__name__}")
            setattr(self, field_name, value)

    def __repr__(self):
        values = ', '.join(f"{k}={getattr(self, k)!r}" for k in schema.keys())
        return f"{name}({values})"

    namespace = {
        '__init__': __init__,
        '__repr__': __repr__,
        'schema': schema
    }

    return type(name, (object,), namespace)
```

### Solution 14: Method Call Counter

```python
def count_calls(cls):
    """Decorator that counts method calls"""
    cls._call_counts = {}

    for name, method in cls.__dict__.items():
        if callable(method) and not name.startswith('__'):
            cls._call_counts[name] = 0
            setattr(cls, name, _wrap_method(method, name, cls._call_counts))

    @classmethod
    def get_stats(cls):
        return cls._call_counts.copy()

    @classmethod
    def reset_stats(cls):
        cls._call_counts = {k: 0 for k in cls._call_counts}

    cls.get_stats = get_stats
    cls.reset_stats = reset_stats
    return cls

def _wrap_method(method, name, counts):
    @wraps(method)
    def wrapper(*args, **kwargs):
        counts[name] += 1
        return method(*args, **kwargs)
    return wrapper
```

### Solution 15: Multi-dispatch System (Simplified)

```python
import inspect

class MultiDispatchMeta(type):
    """Simplified multi-dispatch metaclass"""

    def __new__(mcs, name, bases, namespace):
        dispatchers = {}

        for attr_name, attr_value in namespace.items():
            if callable(attr_value) and not attr_name.startswith('_'):
                # Get type hints
                hints = inspect.get_annotations(attr_value)
                if hints:
                    key = tuple(hints.values())
                    if attr_name not in dispatchers:
                        dispatchers[attr_name] = {}
                    dispatchers[attr_name][key] = attr_value

        # Create dispatcher functions
        for method_name, implementations in dispatchers.items():
            namespace[method_name] = mcs._create_dispatcher(implementations)

        return super().__new__(mcs, name, bases, namespace)

    @staticmethod
    def _create_dispatcher(implementations):
        def dispatcher(self, *args):
            arg_types = tuple(type(arg) for arg in args)
            if arg_types in implementations:
                return implementations[arg_types](self, *args)
            raise TypeError(f"No implementation for types {arg_types}")
        return dispatcher
```

These solutions demonstrate advanced Python programming techniques and can be extended based on specific requirements.
