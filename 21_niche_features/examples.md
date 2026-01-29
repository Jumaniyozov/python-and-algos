# Chapter 21: Niche Features - Examples

## Example 1: Ellipsis in Type Hints

```python
from typing import Callable, Any

def apply_function(func: Callable[..., int], *args: Any) -> int:
    """Accepts any callable that returns int, regardless of parameters."""
    return func(*args)

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int, c: int) -> int:
    return a * b * c

# Both work despite different signatures
print(apply_function(add, 5, 3))         # 8
print(apply_function(multiply, 2, 3, 4)) # 24
```

## Example 2: Ellipsis as Placeholder

```python
class DatabaseModel:
    """Ellipsis is more semantic than 'pass' for unimplemented methods."""

    def save(self):
        """Save model to database."""
        ...  # To be implemented

    def delete(self):
        """Delete model from database."""
        ...  # To be implemented

    def update(self, **kwargs):
        """Update model fields."""
        ...  # To be implemented

# More readable than 'pass' - shows intentional placeholder
```

## Example 3: Custom Ellipsis Handler

```python
class FlexibleArray:
    """Array-like class that handles ellipsis for 'all elements'."""

    def __init__(self, data):
        self.data = list(data)

    def __getitem__(self, key):
        if key is Ellipsis:
            return self.data[:]  # Return all elements
        elif isinstance(key, slice):
            return self.data[key]
        return self.data[key]

    def __setitem__(self, key, value):
        if key is Ellipsis:
            self.data = [value] * len(self.data)
        else:
            self.data[key] = value

arr = FlexibleArray([1, 2, 3, 4, 5])
print(arr[...])       # [1, 2, 3, 4, 5]
arr[...] = 0
print(arr[...])       # [0, 0, 0, 0, 0]
```

## Example 4: Walrus Operator in While Loop

```python
import random

def generate_data():
    """Simulates reading data from a stream."""
    num = random.randint(1, 100)
    return num if num != 42 else None

# Without walrus operator (verbose)
def process_old_way():
    data = generate_data()
    while data is not None:
        print(f"Processing: {data}")
        data = generate_data()

# With walrus operator (concise)
def process_new_way():
    while (data := generate_data()) is not None:
        print(f"Processing: {data}")

process_new_way()
```

## Example 5: Walrus Operator in List Comprehension

```python
def expensive_operation(x):
    """Simulates expensive computation."""
    return x ** 2 + 2 * x + 1

# Without walrus: calls expensive_operation twice per item
def old_way(data):
    return [expensive_operation(x) for x in data
            if expensive_operation(x) > 50]

# With walrus: calls expensive_operation once per item
def new_way(data):
    return [result for x in data
            if (result := expensive_operation(x)) > 50]

data = list(range(1, 10))
print(new_way(data))  # [51, 64, 79, 96]
```

## Example 6: Walrus Operator with Regex

```python
import re

def extract_emails(text):
    """Extract emails from text using walrus operator."""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = []

    # More readable than assigning match before if statement
    lines = text.split('\n')
    for line in lines:
        if (match := re.search(pattern, line)):
            emails.append(match.group(0))

    return emails

text = """
Contact us at support@example.com
Sales: sales@company.org
No email here
Admin: admin@website.net
"""

print(extract_emails(text))
# ['support@example.com', 'sales@company.org', 'admin@website.net']
```

## Example 7: Positional-Only Parameters

```python
def create_user(user_id, name, /, *, email, age=None):
    """
    Create user with strict parameter requirements.

    user_id, name: positional-only (can be renamed in future)
    email: keyword-only (prevents positional errors)
    age: keyword-only with default
    """
    return {
        'id': user_id,
        'name': name,
        'email': email,
        'age': age
    }

# Valid calls
user1 = create_user(1, "Alice", email="alice@example.com")
user2 = create_user(2, "Bob", email="bob@example.com", age=30)

# Invalid calls (will raise TypeError)
# user3 = create_user(user_id=3, name="Charlie", email="charlie@example.com")
# user4 = create_user(4, "Dave", "dave@example.com")  # email must be keyword

print(user1)
print(user2)
```

## Example 8: Keyword-Only Parameters

```python
def send_email(recipient, subject, body, *,
               cc=None, bcc=None, priority='normal',
               attachments=None):
    """
    Send email with clear, explicit optional parameters.

    Forces callers to name optional params, preventing errors
    from wrong argument order.
    """
    email = {
        'to': recipient,
        'subject': subject,
        'body': body,
        'cc': cc or [],
        'bcc': bcc or [],
        'priority': priority,
        'attachments': attachments or []
    }
    print(f"Sending email to {recipient}")
    return email

# Clear, explicit calls
email1 = send_email("user@example.com", "Hello", "Welcome!",
                    priority='high')
email2 = send_email("admin@site.com", "Report", "See attached",
                    cc=['manager@site.com'],
                    attachments=['report.pdf'])

# This would fail (priority must be keyword):
# send_email("user@example.com", "Hello", "Welcome!", 'high')
```

## Example 9: __missing__ for Auto-Vivification

```python
class AutoVivification(dict):
    """Dict that automatically creates nested dicts."""

    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

# Create nested structure without pre-initialization
tree = AutoVivification()
tree['animals']['mammals']['dog'] = 'Canis familiaris'
tree['animals']['mammals']['cat'] = 'Felis catus'
tree['animals']['birds']['eagle'] = 'Aquila chrysaetos'
tree['plants']['flowers']['rose'] = 'Rosa'

print(tree)
# Nested dicts created automatically!
```

## Example 10: __missing__ with Logging

```python
class LoggingDict(dict):
    """Dict that logs access to missing keys."""

    def __init__(self, default_value=None):
        super().__init__()
        self.default_value = default_value
        self.missing_keys = []

    def __missing__(self, key):
        self.missing_keys.append(key)
        print(f"Warning: Key '{key}' not found, using default")
        return self.default_value

config = LoggingDict(default_value='UNDEFINED')
config['timeout'] = 30
config['debug'] = True

print(config['timeout'])    # 30
print(config['max_retries']) # Warning logged, returns 'UNDEFINED'
print(config['host'])        # Warning logged, returns 'UNDEFINED'

print(f"Missing keys accessed: {config.missing_keys}")
```

## Example 11: Enum for Status Management

```python
from enum import Enum, auto

class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()

    def can_cancel(self):
        """Check if order can be cancelled."""
        return self in (OrderStatus.PENDING, OrderStatus.PROCESSING)

    def next_status(self):
        """Get next valid status."""
        transitions = {
            OrderStatus.PENDING: OrderStatus.PROCESSING,
            OrderStatus.PROCESSING: OrderStatus.SHIPPED,
            OrderStatus.SHIPPED: OrderStatus.DELIVERED
        }
        return transitions.get(self)

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = OrderStatus.PENDING

    def advance(self):
        next_status = self.status.next_status()
        if next_status:
            self.status = next_status
            print(f"Order {self.order_id}: {self.status.name}")
        else:
            print(f"Order {self.order_id}: No more transitions")

order = Order(12345)
order.advance()  # PROCESSING
order.advance()  # SHIPPED
order.advance()  # DELIVERED
order.advance()  # No more transitions
```

## Example 12: Flag for Permissions

```python
from enum import Flag, auto

class Permission(Flag):
    NONE = 0
    READ = auto()      # 1
    WRITE = auto()     # 2
    EXECUTE = auto()   # 4
    DELETE = auto()    # 8

    # Composite permissions
    READ_WRITE = READ | WRITE
    READ_EXECUTE = READ | EXECUTE
    ALL = READ | WRITE | EXECUTE | DELETE

class User:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    def can(self, permission):
        """Check if user has permission."""
        return bool(self.permissions & permission)

    def grant(self, permission):
        """Grant permission to user."""
        self.permissions |= permission

    def revoke(self, permission):
        """Revoke permission from user."""
        self.permissions &= ~permission

# Create users with different permissions
admin = User("Alice", Permission.ALL)
viewer = User("Bob", Permission.READ)
editor = User("Charlie", Permission.READ_WRITE)

print(f"Alice can delete: {admin.can(Permission.DELETE)}")      # True
print(f"Bob can write: {viewer.can(Permission.WRITE)}")          # False
print(f"Charlie can write: {editor.can(Permission.WRITE)}")      # True

# Grant execute permission to editor
editor.grant(Permission.EXECUTE)
print(f"Charlie can execute: {editor.can(Permission.EXECUTE)}")  # True
```

## Example 13: Sentinel Values

```python
_MISSING = object()
_NOT_SET = object()

class Configuration:
    """Config class that distinguishes between None and not-provided."""

    def __init__(self):
        self.settings = {}

    def set(self, key, value=_MISSING):
        """Set configuration value."""
        if value is _MISSING:
            # No value provided - use default computation
            value = self._compute_default(key)
        elif value is None:
            # None explicitly provided - use it
            pass

        self.settings[key] = value

    def get(self, key, default=_NOT_SET):
        """Get configuration value."""
        if key in self.settings:
            return self.settings[key]

        if default is _NOT_SET:
            raise KeyError(f"Setting '{key}' not found and no default provided")

        return default

    def _compute_default(self, key):
        """Compute default value based on key."""
        defaults = {
            'timeout': 30,
            'max_retries': 3,
            'debug': False
        }
        return defaults.get(key, 'UNDEFINED')

config = Configuration()
config.set('timeout')              # Uses computed default (30)
config.set('host', None)           # Explicitly sets to None
config.set('port', 8080)           # Sets to 8080

print(config.get('timeout'))       # 30
print(config.get('host'))          # None
print(config.get('port'))          # 8080
print(config.get('unknown', 'fallback'))  # 'fallback'
```

## Example 14: __getattr__ for Dynamic Attributes

```python
class DynamicConfig:
    """Configuration with environment variable fallback."""

    def __init__(self):
        self._config = {
            'api_url': 'https://api.example.com',
            'timeout': 30
        }

    def __getattr__(self, name):
        """Look up attribute in config dict or environment variables."""
        import os

        # Try config dict first
        if name in self._config:
            return self._config[name]

        # Try environment variable
        env_name = name.upper()
        if env_name in os.environ:
            return os.environ[env_name]

        # Not found anywhere
        raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")

    def __setattr__(self, name, value):
        # Store in _config instead of instance dict
        if name == '_config':
            super().__setattr__(name, value)
        else:
            self._config[name] = value

config = DynamicConfig()
print(config.api_url)     # From _config dict
config.max_connections = 100
print(config.max_connections)  # Set and retrieved dynamically
```

## Example 15: __getattribute__ for Access Logging

```python
class TrackedObject:
    """Object that logs all attribute access."""

    def __init__(self):
        super().__setattr__('_access_log', [])
        super().__setattr__('value', 100)
        super().__setattr__('name', 'tracker')

    def __getattribute__(self, name):
        # Don't log access to _access_log itself
        if name != '_access_log':
            access_log = super().__getattribute__('_access_log')
            access_log.append(f"GET: {name}")

        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        access_log = super().__getattribute__('_access_log')
        access_log.append(f"SET: {name} = {value}")
        super().__setattr__(name, value)

    def get_log(self):
        return super().__getattribute__('_access_log')

obj = TrackedObject()
print(obj.value)      # Access logged
obj.value = 200       # Modification logged
print(obj.name)       # Access logged
print(obj.get_log())  # ['GET: value', 'SET: value = 200', 'GET: name', 'GET: get_log']
```

## Example 16: __slots__ for Memory Optimization

```python
import sys

class PointWithDict:
    """Regular class with __dict__."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointWithSlots:
    """Optimized class with __slots__."""
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Create many instances to see memory difference
regular_points = [PointWithDict(i, i*2) for i in range(1000)]
slotted_points = [PointWithSlots(i, i*2) for i in range(1000)]

# Measure memory usage
regular_size = sys.getsizeof(regular_points[0].__dict__) + sys.getsizeof(regular_points[0])
slotted_size = sys.getsizeof(slotted_points[0])

print(f"Regular point size: ~{regular_size} bytes")
print(f"Slotted point size: ~{slotted_size} bytes")
print(f"Memory saved per instance: ~{regular_size - slotted_size} bytes")

# Slots prevent arbitrary attribute assignment
try:
    slotted_points[0].z = 100
except AttributeError as e:
    print(f"Slots protection: {e}")
```

## Example 17: __init_subclass__ for Plugin System

```python
class PluginBase:
    """Base class for plugins with auto-registration."""

    plugins = {}

    def __init_subclass__(cls, plugin_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if plugin_name:
            cls.plugins[plugin_name] = cls
            print(f"Registered plugin: {plugin_name}")

    @classmethod
    def get_plugin(cls, name):
        return cls.plugins.get(name)

    def execute(self):
        raise NotImplementedError

class ImagePlugin(PluginBase, plugin_name='image'):
    def execute(self):
        return "Processing image..."

class VideoPlugin(PluginBase, plugin_name='video'):
    def execute(self):
        return "Processing video..."

class AudioPlugin(PluginBase, plugin_name='audio'):
    def execute(self):
        return "Processing audio..."

# Plugins are automatically registered!
print(f"Available plugins: {list(PluginBase.plugins.keys())}")

# Use plugins
plugin = PluginBase.get_plugin('video')
print(plugin().execute())
```

## Example 18: singledispatch for Type-Based Behavior

```python
from functools import singledispatch
from typing import List

@singledispatch
def serialize(obj):
    """Generic serialization function."""
    return str(obj)

@serialize.register(list)
def _(obj: List):
    """Serialize list to JSON-like format."""
    items = ', '.join(serialize(item) for item in obj)
    return f"[{items}]"

@serialize.register(dict)
def _(obj: dict):
    """Serialize dict to JSON-like format."""
    items = ', '.join(f'"{k}": {serialize(v)}' for k, v in obj.items())
    return f"{{{items}}}"

@serialize.register(int)
@serialize.register(float)
def _(obj):
    """Serialize numbers."""
    return str(obj)

@serialize.register(str)
def _(obj: str):
    """Serialize strings with quotes."""
    return f'"{obj}"'

# Test serialization
data = {
    'name': 'Alice',
    'age': 30,
    'scores': [95, 87, 92],
    'active': True
}

print(serialize(data))
# Output: {"name": "Alice", "age": 30, "scores": [95, 87, 92], "active": True}
```

## Example 19: contextlib.suppress for Cleaner Code

```python
from contextlib import suppress
import os

def cleanup_files(file_list):
    """Delete files, ignoring if they don't exist."""
    for file_path in file_list:
        with suppress(FileNotFoundError):
            os.remove(file_path)
            print(f"Deleted: {file_path}")

def safe_division(numbers):
    """Perform divisions, skipping any that cause ZeroDivisionError."""
    results = []
    for num in numbers:
        with suppress(ZeroDivisionError):
            result = 100 / num
            results.append(result)
    return results

# Much cleaner than try/except for ignored exceptions
files = ['temp1.txt', 'temp2.txt', 'nonexistent.txt']
cleanup_files(files)

numbers = [10, 5, 0, 2, 0, 4]
print(safe_division(numbers))  # [10.0, 20.0, 50.0, 25.0]
```

## Example 20: Custom __format__ for Flexible Display

```python
from math import sqrt, atan2, degrees

class Vector2D:
    """2D vector with custom formatting options."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __format__(self, spec):
        if spec == '':
            # Default format: (x, y)
            return f"({self.x}, {self.y})"
        elif spec == 'polar':
            # Polar coordinates: (magnitude, angle)
            magnitude = sqrt(self.x**2 + self.y**2)
            angle = degrees(atan2(self.y, self.x))
            return f"({magnitude:.2f}, {angle:.2f}°)"
        elif spec == 'unit':
            # Unit vector
            magnitude = sqrt(self.x**2 + self.y**2)
            if magnitude == 0:
                return "(0, 0)"
            ux = self.x / magnitude
            uy = self.y / magnitude
            return f"({ux:.3f}, {uy:.3f})"
        elif spec.endswith('f'):
            # Floating point precision
            precision = int(spec[:-1]) if spec[:-1] else 2
            return f"({self.x:.{precision}f}, {self.y:.{precision}f})"
        else:
            raise ValueError(f"Unknown format spec: {spec}")

v = Vector2D(3, 4)
print(f"Default: {v}")           # Default: (3, 4)
print(f"Polar: {v:polar}")       # Polar: (5.00, 53.13°)
print(f"Unit: {v:unit}")         # Unit: (0.600, 0.800)
print(f"2 decimals: {v:2f}")     # 2 decimals: (3.00, 4.00)
print(f"4 decimals: {v:4f}")     # 4 decimals: (3.0000, 4.0000)
```
