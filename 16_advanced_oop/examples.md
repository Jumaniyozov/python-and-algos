# Examples: Advanced OOP & Metaclasses

## Example 1: Simple Metaclass - Class Registry

```python
class RegistryMeta(type):
    """Metaclass that automatically registers classes"""
    registry = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        # Don't register the base class itself
        if bases:
            mcs.registry[name] = cls
        return cls

class Plugin(metaclass=RegistryMeta):
    """Base plugin class"""
    pass

class JSONPlugin(Plugin):
    def process(self, data):
        return f"Processing JSON: {data}"

class XMLPlugin(Plugin):
    def process(self, data):
        return f"Processing XML: {data}"

# Access registered plugins
print("Registered plugins:", RegistryMeta.registry.keys())
# Output: Registered plugins: dict_keys(['JSONPlugin', 'XMLPlugin'])

# Create instances dynamically
for name, plugin_class in RegistryMeta.registry.items():
    plugin = plugin_class()
    print(f"{name}: {plugin.process('test data')}")
```

## Example 2: Singleton Using Metaclass

```python
class SingletonMeta(type):
    """Metaclass for creating singleton classes"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Initializing database connection")
        self.connection = "Connected"

# Both variables refer to the same instance
db1 = Database()  # Prints: Initializing database connection
db2 = Database()  # No print - returns existing instance

print(db1 is db2)  # True
print(id(db1) == id(db2))  # True
```

## Example 3: `__init_subclass__` for Validation

```python
class ValidatedModel:
    """Base class that validates required attributes"""
    required_fields = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Check that all required fields are class variables
        missing = []
        for field in cls.required_fields:
            if not hasattr(cls, field):
                missing.append(field)

        if missing:
            raise TypeError(
                f"{cls.__name__} missing required fields: {', '.join(missing)}"
            )

class User(ValidatedModel):
    required_fields = ['username', 'email']
    username = None
    email = None

    def __init__(self, username, email):
        self.username = username
        self.email = email

# This works
user = User("alice", "alice@example.com")
print(f"User: {user.username}, {user.email}")

# This would raise TypeError at class definition:
# class InvalidUser(ValidatedModel):
#     required_fields = ['username', 'email']
#     username = None
#     # Missing email field!
```

## Example 4: Plugin System with `__init_subclass__`

```python
class PluginSystem:
    """Base class for plugin system"""
    plugins = {}

    def __init_subclass__(cls, plugin_name=None, enabled=True, **kwargs):
        super().__init_subclass__(**kwargs)

        if plugin_name and enabled:
            cls.plugins[plugin_name] = cls
            print(f"Registered plugin: {plugin_name}")

    @classmethod
    def get_plugin(cls, name):
        return cls.plugins.get(name)

    @classmethod
    def list_plugins(cls):
        return list(cls.plugins.keys())

class ImagePlugin(PluginSystem, plugin_name="image"):
    def process(self, data):
        return f"Processing image: {data}"

class VideoPlugin(PluginSystem, plugin_name="video"):
    def process(self, data):
        return f"Processing video: {data}"

class DisabledPlugin(PluginSystem, plugin_name="disabled", enabled=False):
    def process(self, data):
        return "This won't be registered"

# Use the plugin system
print("\nAvailable plugins:", PluginSystem.list_plugins())

plugin = PluginSystem.get_plugin("image")
if plugin:
    processor = plugin()
    print(processor.process("vacation.jpg"))
```

## Example 5: Class Decorator for Auto-repr

```python
def auto_repr(*attrs):
    """Decorator that automatically generates __repr__ method"""
    def decorator(cls):
        def __repr__(self):
            values = ', '.join(f"{attr}={getattr(self, attr)!r}" for attr in attrs)
            return f"{cls.__name__}({values})"

        cls.__repr__ = __repr__
        return cls
    return decorator

@auto_repr('name', 'age', 'email')
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

person = Person("Alice", 30, "alice@example.com")
print(person)
# Output: Person(name='Alice', age=30, email='alice@example.com')
```

## Example 6: Class Decorator for Method Timing

```python
import time
from functools import wraps

def time_methods(cls):
    """Decorator that adds timing to all methods"""
    for name, method in cls.__dict__.items():
        if callable(method) and not name.startswith('_'):
            setattr(cls, name, _time_method(method))
    return cls

def _time_method(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = method(*args, **kwargs)
        end = time.time()
        print(f"{method.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@time_methods
class DataProcessor:
    def process_data(self):
        time.sleep(0.1)
        return "Data processed"

    def analyze_data(self):
        time.sleep(0.05)
        return "Data analyzed"

processor = DataProcessor()
processor.process_data()  # Prints timing
processor.analyze_data()  # Prints timing
```

## Example 7: Validated Attribute Descriptor

```python
class TypedProperty:
    """Descriptor for type-validated properties"""

    def __init__(self, name, expected_type, default=None):
        self.name = name
        self.expected_type = expected_type
        self.default = default

    def __set_name__(self, owner, name):
        # Python 3.6+ automatically calls this
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name[1:]} must be {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        setattr(instance, self.name, value)

class Person:
    name = TypedProperty("name", str, default="Unknown")
    age = TypedProperty("age", int, default=0)
    height = TypedProperty("height", (int, float), default=0.0)

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

person = Person("Alice", 30, 165.5)
print(f"{person.name}, {person.age} years, {person.height}cm")

# This raises TypeError:
try:
    person.age = "thirty"
except TypeError as e:
    print(f"Error: {e}")
```

## Example 8: Lazy Property Descriptor

```python
class LazyProperty:
    """Descriptor that computes value only once"""

    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self

        # Compute and cache the value
        value = self.function(instance)
        # Replace descriptor with the actual value
        setattr(instance, self.name, value)
        return value

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    @LazyProperty
    def mean(self):
        print("Computing mean...")
        return sum(self.data) / len(self.data)

    @LazyProperty
    def sum_values(self):
        print("Computing sum...")
        return sum(self.data)

analyzer = DataAnalyzer([1, 2, 3, 4, 5])

# First access computes the value
print(f"Mean: {analyzer.mean}")  # Prints "Computing mean..." then result

# Second access returns cached value
print(f"Mean: {analyzer.mean}")  # Just returns result, no computation

print(f"Sum: {analyzer.sum_values}")  # Computes sum
print(f"Sum: {analyzer.sum_values}")  # Returns cached sum
```

## Example 9: Range Validator Descriptor

```python
class RangeValidator:
    """Descriptor that validates numeric ranges"""

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        self.data = {}

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(id(instance))

    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(
                f"{self.name} must be >= {self.min_value}, got {value}"
            )
        if self.max_value is not None and value > self.max_value:
            raise ValueError(
                f"{self.name} must be <= {self.max_value}, got {value}"
            )
        self.data[id(instance)] = value

    def __delete__(self, instance):
        del self.data[id(instance)]

class Product:
    price = RangeValidator(min_value=0)
    quantity = RangeValidator(min_value=0, max_value=1000)
    discount = RangeValidator(min_value=0, max_value=100)

    def __init__(self, price, quantity, discount=0):
        self.price = price
        self.quantity = quantity
        self.discount = discount

product = Product(19.99, 50, 10)
print(f"Price: ${product.price}, Quantity: {product.quantity}, "
      f"Discount: {product.discount}%")

# Test validation
try:
    product.price = -5  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

try:
    product.discount = 150  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
```

## Example 10: Dynamic Class Factory

```python
def create_dataclass(name, fields):
    """Factory function to create simple data classes"""

    def __init__(self, **kwargs):
        for field in fields:
            setattr(self, field, kwargs.get(field))

    def __repr__(self):
        values = ', '.join(f"{field}={getattr(self, field)!r}"
                          for field in fields)
        return f"{name}({values})"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return all(getattr(self, f) == getattr(other, f) for f in fields)

    namespace = {
        '__init__': __init__,
        '__repr__': __repr__,
        '__eq__': __eq__,
        'fields': fields
    }

    return type(name, (object,), namespace)

# Create classes dynamically
User = create_dataclass('User', ['name', 'email', 'age'])
Product = create_dataclass('Product', ['name', 'price', 'sku'])

user = User(name='Alice', email='alice@example.com', age=30)
print(user)

product = Product(name='Laptop', price=999.99, sku='LAP-001')
print(product)

# Test equality
user2 = User(name='Alice', email='alice@example.com', age=30)
print(f"user == user2: {user == user2}")  # True
```

## Example 11: Method Injection via Metaclass

```python
class InjectMethodsMeta(type):
    """Metaclass that injects common methods"""

    def __new__(mcs, name, bases, namespace):
        # Inject a to_dict method if not present
        if 'to_dict' not in namespace:
            def to_dict(self):
                return {
                    key: value
                    for key, value in self.__dict__.items()
                    if not key.startswith('_')
                }
            namespace['to_dict'] = to_dict

        # Inject a from_dict class method if not present
        if 'from_dict' not in namespace:
            def from_dict(cls, data):
                return cls(**data)
            namespace['from_dict'] = classmethod(from_dict)

        return super().__new__(mcs, name, bases, namespace)

class Model(metaclass=InjectMethodsMeta):
    pass

class User(Model):
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Use injected methods
user = User("Alice", "alice@example.com")
print("User dict:", user.to_dict())

# Create from dict
user_data = {'name': 'Bob', 'email': 'bob@example.com'}
user2 = User.from_dict(user_data)
print("Created from dict:", user2.to_dict())
```

## Example 12: Abstract Base Class with Template Method

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """Abstract template for data processing"""

    def process(self, data):
        """Template method defining the algorithm structure"""
        print("Starting processing...")
        validated = self.validate(data)
        transformed = self.transform(validated)
        result = self.save(transformed)
        print("Processing complete.")
        return result

    @abstractmethod
    def validate(self, data):
        """Validate the data - must be implemented"""
        pass

    @abstractmethod
    def transform(self, data):
        """Transform the data - must be implemented"""
        pass

    def save(self, data):
        """Save the data - can be overridden"""
        print(f"Saving: {data}")
        return data

class CSVProcessor(DataProcessor):
    def validate(self, data):
        print("Validating CSV data...")
        if not isinstance(data, str):
            raise ValueError("Data must be a string")
        return data

    def transform(self, data):
        print("Transforming CSV data...")
        return data.upper()

class JSONProcessor(DataProcessor):
    def validate(self, data):
        print("Validating JSON data...")
        if not isinstance(data, dict):
            raise ValueError("Data must be a dict")
        return data

    def transform(self, data):
        print("Transforming JSON data...")
        return {k.upper(): v for k, v in data.items()}

# Use the processors
csv = CSVProcessor()
result1 = csv.process("name,age\nalice,30")

print("\n" + "="*50 + "\n")

json_proc = JSONProcessor()
result2 = json_proc.process({"name": "alice", "age": 30})
```

## Example 13: Virtual Subclass Registration

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        """Allow duck-typed classes to be recognized"""
        if cls is Drawable:
            if any("draw" in B.__dict__ for B in subclass.__mro__):
                return True
        return NotImplemented

# Traditional subclass
class Circle(Drawable):
    def draw(self):
        return "Drawing a circle"

# Duck-typed class (not inheriting from Drawable)
class Square:
    def draw(self):
        return "Drawing a square"

# Manually register as virtual subclass
Drawable.register(Square)

def render(shape: Drawable):
    print(shape.draw())

circle = Circle()
square = Square()

print(f"Circle is Drawable: {isinstance(circle, Drawable)}")  # True
print(f"Square is Drawable: {isinstance(square, Drawable)}")  # True

render(circle)
render(square)
```

## Example 14: Combining Metaclass with Descriptors

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
        pass

class StringField(Field):
    def __init__(self, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.max_length = max_length

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string")
        if self.max_length and len(value) > self.max_length:
            raise ValueError(f"{self.name} exceeds max length")

class IntField(Field):
    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")

class ModelMeta(type):
    """Metaclass that collects field definitions"""
    def __new__(mcs, name, bases, namespace):
        fields = {}
        for key, value in namespace.items():
            if isinstance(value, Field):
                fields[key] = value

        namespace['_fields'] = fields
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for name, field in self._fields.items():
            value = kwargs.get(name, field.default)
            if value is not None:
                setattr(self, name, value)

    def __repr__(self):
        values = ', '.join(
            f"{name}={getattr(self, name)!r}"
            for name in self._fields
        )
        return f"{self.__class__.__name__}({values})"

class User(Model):
    name = StringField(max_length=50)
    age = IntField()
    email = StringField()

user = User(name="Alice", age=30, email="alice@example.com")
print(user)
print(f"Fields: {User._fields.keys()}")
```

## Example 15: Advanced Class Decorator with State

```python
def counted(cls):
    """Decorator that counts instances created"""
    original_init = cls.__init__

    def __init__(self, *args, **kwargs):
        cls.instance_count += 1
        original_init(self, *args, **kwargs)

    cls.instance_count = 0
    cls.__init__ = __init__

    @classmethod
    def get_instance_count(cls):
        return cls.instance_count

    cls.get_instance_count = get_instance_count

    return cls

@counted
class User:
    def __init__(self, name):
        self.name = name

@counted
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Create instances
users = [User(f"User{i}") for i in range(5)]
products = [Product(f"Product{i}", i * 10) for i in range(3)]

print(f"Users created: {User.get_instance_count()}")      # 5
print(f"Products created: {Product.get_instance_count()}")  # 3
```

## Running the Examples

All examples are self-contained and can be run directly. They demonstrate:

1. **Metaclasses** for class registration and singleton pattern
2. **`__init_subclass__`** for validation and plugin systems
3. **Class decorators** for auto-repr, timing, and instance counting
4. **Descriptors** for validation, type checking, and lazy evaluation
5. **Dynamic class creation** with factory patterns
6. **ABC** for template methods and virtual subclasses
7. **Combined techniques** for building sophisticated frameworks

These patterns are used extensively in popular Python frameworks like Django, SQLAlchemy, and pytest.
