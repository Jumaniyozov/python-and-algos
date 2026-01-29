# Chapter 21: Niche Features - Solutions

## Solution 1: Ellipsis-Based Configuration

```python
class Config:
    """Configuration with ellipsis-based inheritance."""

    def __init__(self, config_dict, parent=None):
        self.config = config_dict
        self.parent = parent

    def resolve(self):
        """Resolve all values, inheriting from parent where ellipsis is used."""
        resolved = {}

        for key, value in self.config.items():
            if value is Ellipsis:
                # Inherit from parent
                if self.parent is None:
                    raise ValueError(f"Cannot inherit '{key}': no parent config")
                parent_resolved = self.parent.resolve()
                if key not in parent_resolved:
                    raise KeyError(f"Key '{key}' not found in parent config")
                resolved[key] = parent_resolved[key]
            elif isinstance(value, dict):
                # Nested dict - check for ellipsis in nested values
                resolved[key] = self._resolve_nested(value)
            else:
                resolved[key] = value

        return resolved

    def _resolve_nested(self, d):
        """Recursively resolve nested dictionaries."""
        resolved = {}
        for key, value in d.items():
            if value is Ellipsis:
                if self.parent is None:
                    raise ValueError(f"Cannot inherit nested '{key}': no parent")
                parent_resolved = self.parent.resolve()
                resolved[key] = parent_resolved.get(key, None)
            elif isinstance(value, dict):
                resolved[key] = self._resolve_nested(value)
            else:
                resolved[key] = value
        return resolved

    def __repr__(self):
        return f"Config({self.resolve()})"


# Test
parent = Config({'timeout': 30, 'retries': 3, 'debug': False})
child = Config({'timeout': ..., 'retries': 5, 'debug': ...}, parent=parent)
print(child.resolve())  # {'timeout': 30, 'retries': 5, 'debug': False}
```

## Solution 2: Walrus Operator File Parser

```python
import re
from pathlib import Path

def parse_log_file(filename):
    """Parse log file extracting ERROR and WARNING lines."""
    entries = []

    try:
        with open(filename, 'r') as f:
            # Walrus operator: read and check in one expression
            while (line := f.readline()):
                line = line.strip()
                if not line:
                    continue

                # Use walrus in if condition for regex match
                pattern = r'(\d{2}:\d{2}:\d{2})\s+(ERROR|WARNING)\s+(.+)'
                if (match := re.search(pattern, line)):
                    entries.append({
                        'time': match.group(1),
                        'level': match.group(2),
                        'msg': match.group(3)
                    })

        return entries

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []


# Alternative version with better pattern matching
def parse_log_file_v2(filename):
    """Enhanced log parser with walrus operator."""
    entries = []
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+'
                        r'(ERROR|WARNING)\s+(.+)')

    try:
        with open(filename, 'r') as f:
            while (line := f.readline()):
                if (match := pattern.search(line)):
                    entries.append({
                        'date': match.group(1),
                        'time': match.group(2),
                        'level': match.group(3),
                        'msg': match.group(4)
                    })
        return entries

    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error parsing file: {e}")
        return []


# Test
test_log = """2024-01-15 10:30:00 INFO System started
2024-01-15 10:30:15 ERROR Connection failed
2024-01-15 10:30:20 WARNING Low memory
2024-01-15 10:30:25 INFO Processing complete"""

# Write test file
with open('test.log', 'w') as f:
    f.write(test_log)

result = parse_log_file_v2('test.log')
for entry in result:
    print(entry)
```

## Solution 3: Smart Function Parameters

```python
def create_report(data, /, *, format='pdf', include_charts=True, template=None):
    """
    Create report with strict parameter requirements.

    Args:
        data: Report data (positional-only)
        format: Output format - 'pdf', 'html', or 'markdown' (keyword-only)
        include_charts: Whether to include charts (keyword-only)
        template: Template name or None for default (keyword-only)

    Returns:
        Dictionary with report metadata
    """
    # Validate format
    valid_formats = ('pdf', 'html', 'markdown')
    if format not in valid_formats:
        raise ValueError(f"format must be one of {valid_formats}, got '{format}'")

    # Generate report metadata
    report = {
        'data_points': len(data) if hasattr(data, '__len__') else 'unknown',
        'format': format,
        'has_charts': include_charts,
        'template': template or 'default',
        'generated_at': 'now'
    }

    return report


# Test valid calls
report1 = create_report([1, 2, 3], format='html', include_charts=False)
print(report1)

report2 = create_report({'key': 'value'}, format='pdf', template='modern')
print(report2)

# These would fail:
# create_report(data=[1, 2, 3])  # data must be positional
# create_report([1, 2, 3], 'pdf')  # format must be keyword
# create_report([1, 2, 3], format='xml')  # invalid format
```

## Solution 4: Auto-Counting Dict

```python
class CountingDict(dict):
    """Dictionary that auto-initializes counters for new keys."""

    def __init__(self):
        super().__init__()
        self.missing_key_accesses = 0

    def __missing__(self, key):
        """Initialize counter for new key."""
        self.missing_key_accesses += 1
        self[key] = 0
        return 0

    def increment(self, key, amount=1):
        """Increment counter for key."""
        self[key] += amount

    def total_accesses(self):
        """Return total accesses to missing keys."""
        return self.missing_key_accesses


# Test
counter = CountingDict()
counter['apple'] += 1
counter['banana'] += 1
counter['apple'] += 1
counter.increment('orange', 5)

print(dict(counter))  # {'apple': 2, 'banana': 1, 'orange': 5}
print(f"Missing key accesses: {counter.total_accesses()}")  # 3
```

## Solution 5: HTTP Status Enum

```python
from enum import IntEnum

class HTTPStatus(IntEnum):
    """HTTP status codes with utility methods."""

    # 2xx Success
    OK = 200
    CREATED = 201
    NO_CONTENT = 204

    # 3xx Redirection
    MOVED_PERMANENTLY = 301
    FOUND = 302

    # 4xx Client Error
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404

    # 5xx Server Error
    INTERNAL_SERVER_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503

    def is_error(self):
        """Check if status is error (>= 400)."""
        return self.value >= 400

    def category(self):
        """Get status category (2xx, 4xx, etc.)."""
        return f"{self.value // 100}xx"

    def description(self):
        """Get human-readable description."""
        descriptions = {
            200: "Request succeeded",
            201: "Resource created",
            204: "No content to return",
            301: "Resource moved permanently",
            302: "Resource found at different location",
            400: "Invalid request",
            401: "Authentication required",
            403: "Access forbidden",
            404: "Resource not found",
            500: "Server error occurred",
            502: "Bad gateway",
            503: "Service unavailable"
        }
        return descriptions.get(self.value, "Unknown status")


# Test
status = HTTPStatus.NOT_FOUND
print(f"Status: {status}")
print(f"Is error: {status.is_error()}")
print(f"Category: {status.category()}")
print(f"Description: {status.description()}")

# Iterate all statuses
print("\nAll error statuses:")
for status in HTTPStatus:
    if status.is_error():
        print(f"  {status.name} ({status.value}): {status.description()}")
```

## Solution 6: Sentinel-Based Cache

```python
import time
from enum import Enum

class CacheSentinel(Enum):
    """Sentinel values for cache states."""
    MISS = object()
    EXPIRED = object()


class Cache:
    """Cache with sentinel-based state tracking."""

    def __init__(self):
        self._cache = {}
        self._expiry = {}

    def set(self, key, value, ttl=None):
        """Set cache value with optional TTL in seconds."""
        self._cache[key] = value
        if ttl is not None:
            self._expiry[key] = time.time() + ttl
        elif key in self._expiry:
            del self._expiry[key]

    def get(self, key, default=CacheSentinel.MISS):
        """Get cache value, returning sentinel or default if missing/expired."""
        self._cleanup_expired()

        # Check if key exists
        if key not in self._cache:
            return default

        # Check if expired
        if key in self._expiry and time.time() > self._expiry[key]:
            del self._cache[key]
            del self._expiry[key]
            return CacheSentinel.EXPIRED if default is CacheSentinel.MISS else default

        return self._cache[key]

    def _cleanup_expired(self):
        """Remove all expired entries."""
        now = time.time()
        expired_keys = [k for k, exp_time in self._expiry.items()
                       if now > exp_time]
        for key in expired_keys:
            del self._cache[key]
            del self._expiry[key]

    def clear(self):
        """Clear all cache entries."""
        self._cache.clear()
        self._expiry.clear()

    def __len__(self):
        self._cleanup_expired()
        return len(self._cache)


# Test
cache = Cache()

# Test explicit None caching
cache.set('key1', None)
print(cache.get('key1'))  # None (cached)

# Test cache miss
result = cache.get('key2')
print(f"Cache miss: {result is CacheSentinel.MISS}")  # True

# Test default value
print(cache.get('key2', 'default'))  # 'default'

# Test TTL
cache.set('temp', 'value', ttl=1)
print(cache.get('temp'))  # 'value'
time.sleep(1.1)
result = cache.get('temp')
print(f"Expired: {result is CacheSentinel.EXPIRED}")  # True
```

## Solution 7: Dynamic API Client

```python
class APIEndpoint:
    """Represents an API endpoint that can be chained."""

    def __init__(self, base_url, path=''):
        self.base_url = base_url
        self.path = path

    def __getattr__(self, name):
        """Chain endpoint paths."""
        new_path = f"{self.path}/{name}" if self.path else name
        return APIEndpoint(self.base_url, new_path)

    def __call__(self, **kwargs):
        """Make API call with parameters."""
        url = f"{self.base_url}/{self.path}"
        if kwargs:
            params = '&'.join(f"{k}={v}" for k, v in kwargs.items())
            url = f"{url}?{params}"

        # Mock response (don't make real HTTP call)
        return {
            'url': url,
            'method': 'GET',
            'status': 200,
            'data': {'message': f'Mock response for {self.path}'}
        }

    def get(self, **kwargs):
        """Explicit GET request."""
        response = self(**kwargs)
        response['method'] = 'GET'
        return response

    def post(self, data=None, **kwargs):
        """Explicit POST request."""
        response = self(**kwargs)
        response['method'] = 'POST'
        response['data'] = data
        return response


class APIClient:
    """Dynamic API client with attribute-based endpoint access."""

    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def __getattr__(self, name):
        """Start endpoint chain."""
        return APIEndpoint(self.base_url, name)


# Test
api = APIClient('https://api.example.com')

# Chain attributes
response1 = api.users.list()
print(response1)

response2 = api.users.profile.get(user_id=123)
print(response2)

response3 = api.posts.create.post(data={'title': 'New Post'})
print(response3)
```

## Solution 8: Validated Attributes

```python
import re

class ValidatedUser:
    """User class with attribute validation."""

    def __init__(self):
        # Use object.__setattr__ to bypass validation during init
        object.__setattr__(self, '_data', {})
        object.__setattr__(self, '_protected', {'_id', '_created_at', '_data', '_protected'})

    def __setattr__(self, name, value):
        # Check protected attributes
        if name in self._protected:
            raise AttributeError(f"Cannot set protected attribute '{name}'")

        # Validate based on attribute name
        if name == 'email':
            if not isinstance(value, str):
                raise TypeError(f"email must be str, got {type(value).__name__}")
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, value):
                raise ValueError(f"Invalid email format: {value}")

        elif name == 'age':
            if not isinstance(value, int):
                raise TypeError(f"age must be int, got {type(value).__name__}")
            if not 0 <= value <= 150:
                raise ValueError(f"age must be between 0-150, got {value}")

        elif name == 'username':
            if not isinstance(value, str):
                raise TypeError(f"username must be str, got {type(value).__name__}")
            value = value.lower()  # Convert to lowercase

        # Store in _data dict
        self._data[name] = value

    def __getattr__(self, name):
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")

    def __repr__(self):
        attrs = ', '.join(f"{k}={v!r}" for k, v in self._data.items())
        return f"ValidatedUser({attrs})"


# Test
user = ValidatedUser()
user.email = 'test@example.com'  # OK
user.age = 25  # OK
user.username = 'JohnDoe'  # Converted to 'johndoe'

print(user)

try:
    user.age = 200
except ValueError as e:
    print(f"Validation error: {e}")

try:
    user._id = 123
except AttributeError as e:
    print(f"Protection error: {e}")
```

## Solution 9: Memory-Efficient Data Class

```python
import sys
import time

class DataPointRegular:
    """Regular class with __dict__."""

    def __init__(self, timestamp, sensor_id, temperature, humidity):
        self.timestamp = timestamp
        self.sensor_id = sensor_id
        self.temperature = temperature
        self.humidity = humidity


class DataPoint:
    """Memory-efficient class with __slots__."""

    __slots__ = ('timestamp', 'sensor_id', 'temperature', 'humidity')

    def __init__(self, timestamp, sensor_id, temperature, humidity):
        self.timestamp = timestamp
        self.sensor_id = sensor_id
        self.temperature = temperature
        self.humidity = humidity

    def __repr__(self):
        return (f"DataPoint({self.sensor_id}: {self.temperature}°C, "
                f"{self.humidity}% at {int(self.timestamp)})")

    def __eq__(self, other):
        if not isinstance(other, DataPoint):
            return False
        return (self.timestamp == other.timestamp and
                self.sensor_id == other.sensor_id)

    def __lt__(self, other):
        if not isinstance(other, DataPoint):
            return NotImplemented
        return self.timestamp < other.timestamp


# Test and compare memory usage
print("Creating 10,000 instances...\n")

# Regular class
regular_points = [DataPointRegular(time.time(), f'sensor_{i % 100}',
                                   20 + (i % 20), 50 + (i % 30))
                 for i in range(10000)]

# Slotted class
slotted_points = [DataPoint(time.time(), f'sensor_{i % 100}',
                           20 + (i % 20), 50 + (i % 30))
                 for i in range(10000)]

# Measure memory
regular_size = sys.getsizeof(regular_points[0].__dict__) + sys.getsizeof(regular_points[0])
slotted_size = sys.getsizeof(slotted_points[0])

print(f"Regular class instance: ~{regular_size} bytes")
print(f"Slotted class instance: ~{slotted_size} bytes")
print(f"Memory saved per instance: ~{regular_size - slotted_size} bytes")
print(f"Total memory saved (10k instances): ~{(regular_size - slotted_size) * 10000 / 1024:.1f} KB")

# Test functionality
dp = DataPoint(time.time(), 'sensor_1', 22.5, 65.0)
print(f"\n{dp}")
```

## Solution 10: File Format Enum

```python
from enum import Enum, auto

class FileFormat(Enum):
    """File format enum with extensions and MIME types."""

    # Images
    JPEG = (auto(), '.jpg', 'image/jpeg', 'image')
    PNG = (auto(), '.png', 'image/png', 'image')
    GIF = (auto(), '.gif', 'image/gif', 'image')
    WEBP = (auto(), '.webp', 'image/webp', 'image')

    # Documents
    PDF = (auto(), '.pdf', 'application/pdf', 'document')
    DOCX = (auto(), '.docx', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'document')
    TXT = (auto(), '.txt', 'text/plain', 'document')

    def __init__(self, value, extension, mime_type, category):
        self._value_ = value
        self.extension = extension
        self.mime_type = mime_type
        self.category = category

    def is_image(self):
        """Check if format is an image."""
        return self.category == 'image'

    def is_document(self):
        """Check if format is a document."""
        return self.category == 'document'

    def get_extension(self):
        """Get file extension."""
        return self.extension

    @classmethod
    def from_extension(cls, ext):
        """Get format from file extension."""
        ext = ext.lower()
        if not ext.startswith('.'):
            ext = '.' + ext
        for fmt in cls:
            if fmt.extension == ext:
                return fmt
        return None


# Test
print("Image formats:")
for fmt in FileFormat:
    if fmt.is_image():
        print(f"  {fmt.name}: {fmt.get_extension()} ({fmt.mime_type})")

print("\nDocument formats:")
for fmt in FileFormat:
    if fmt.is_document():
        print(f"  {fmt.name}: {fmt.get_extension()} ({fmt.mime_type})")

# Lookup by extension
fmt = FileFormat.from_extension('.jpg')
print(f"\n.jpg format: {fmt.name}")
```

## Solution 11: Plugin System with Metadata

```python
class PluginBase:
    """Base class for plugins with auto-registration."""

    _plugins = {}
    _enabled = {}

    def __init_subclass__(cls, name=None, version='1.0', priority=50,
                         depends=None, **kwargs):
        super().__init_subclass__(**kwargs)

        if name is None:
            return  # Skip registration for intermediate base classes

        # Validate dependencies
        depends = depends or []
        for dep in depends:
            if dep not in cls._plugins:
                raise ValueError(f"Plugin '{name}' depends on undefined plugin '{dep}'")

        # Check for circular dependencies
        if cls._has_circular_dependency(name, depends):
            raise ValueError(f"Circular dependency detected for plugin '{name}'")

        # Register plugin
        cls._plugins[name] = {
            'class': cls,
            'version': version,
            'priority': priority,
            'depends': depends
        }
        cls._enabled[name] = True

        print(f"Registered plugin: {name} v{version} (priority: {priority})")

    @classmethod
    def _has_circular_dependency(cls, name, depends, visited=None):
        """Check for circular dependencies."""
        if visited is None:
            visited = set()

        if name in visited:
            return True

        visited.add(name)

        for dep in depends:
            if dep in cls._plugins:
                dep_info = cls._plugins[dep]
                if cls._has_circular_dependency(dep, dep_info['depends'], visited):
                    return True

        visited.remove(name)
        return False

    @classmethod
    def get_plugin(cls, name):
        """Get plugin class by name."""
        if name not in cls._plugins:
            return None
        if not cls._enabled[name]:
            return None
        return cls._plugins[name]['class']

    @classmethod
    def list_plugins(cls, enabled_only=True):
        """List all plugins sorted by priority."""
        plugins = []
        for name, info in cls._plugins.items():
            if enabled_only and not cls._enabled[name]:
                continue
            plugins.append({
                'name': name,
                'version': info['version'],
                'priority': info['priority'],
                'depends': info['depends'],
                'enabled': cls._enabled[name]
            })

        # Sort by priority (lower priority first)
        plugins.sort(key=lambda p: p['priority'])
        return plugins

    @classmethod
    def enable_plugin(cls, name):
        """Enable a plugin."""
        if name in cls._enabled:
            cls._enabled[name] = True

    @classmethod
    def disable_plugin(cls, name):
        """Disable a plugin."""
        if name in cls._enabled:
            cls._enabled[name] = False

    def initialize(self):
        """Initialize plugin (to be overridden)."""
        raise NotImplementedError


# Example plugins
class DatabasePlugin(PluginBase, name='database', version='1.0', priority=10):
    def initialize(self):
        return "Database initialized"


class CachePlugin(PluginBase, name='cache', version='2.0',
                  depends=['database'], priority=20):
    def initialize(self):
        return "Cache initialized"


class AuthPlugin(PluginBase, name='auth', version='1.5',
                 depends=['database', 'cache'], priority=30):
    def initialize(self):
        return "Auth initialized"


# Test
print("\nAll plugins:")
for plugin in PluginBase.list_plugins():
    print(f"  {plugin['name']} v{plugin['version']} - priority {plugin['priority']}")
    if plugin['depends']:
        print(f"    depends on: {', '.join(plugin['depends'])}")

# Get specific plugin
db_plugin_class = PluginBase.get_plugin('database')
db = db_plugin_class()
print(f"\n{db.initialize()}")
```

## Solution 12: Multi-Type Container

```python
class TypedContainer:
    """Container that organizes items by type."""

    def __init__(self):
        self._items = []  # All items in order
        self._by_type = {}  # Items grouped by type

    def __setitem__(self, key, value):
        """Add item to container."""
        if isinstance(key, type):
            # Adding by type: container[int] = 42
            self._items.append(value)
            if key not in self._by_type:
                self._by_type[key] = []
            self._by_type[key].append(value)
        elif isinstance(key, int):
            # Setting by index: container[0] = value
            if key < 0 or key >= len(self._items):
                raise IndexError("Index out of range")
            old_value = self._items[key]
            old_type = type(old_value)
            self._items[key] = value

            # Update type dictionary
            if old_type in self._by_type:
                self._by_type[old_type].remove(old_value)
            new_type = type(value)
            if new_type not in self._by_type:
                self._by_type[new_type] = []
            self._by_type[new_type].append(value)
        else:
            raise TypeError("Key must be a type or integer index")

    def __getitem__(self, key):
        """Get items from container."""
        if key is Ellipsis:
            # Get all items: container[...]
            return self._items[:]
        elif isinstance(key, type):
            # Get all of type: container[int]
            return self._by_type.get(key, [])[:]
        elif isinstance(key, int):
            # Get by index: container[0]
            return self._items[key]
        else:
            raise TypeError("Key must be Ellipsis, type, or integer index")

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"TypedContainer({self._items})"


# Test
container = TypedContainer()
container[int] = 42
container[str] = 'hello'
container[int] = 100
container[str] = 'world'
container[float] = 3.14

print(f"All integers: {container[int]}")  # [42, 100]
print(f"All strings: {container[str]}")   # ['hello', 'world']
print(f"All items: {container[...]}")     # [42, 'hello', 100, 'world', 3.14]
print(f"First item: {container[0]}")      # 42
print(f"Third item: {container[2]}")      # 100
```

## Solution 13: State Machine with Flags

```python
from enum import Flag, auto

class WorkflowState(Flag):
    """Workflow states that can be combined."""
    NONE = 0
    DRAFT = auto()       # 1
    REVIEW = auto()      # 2
    APPROVED = auto()    # 4
    PUBLISHED = auto()   # 8
    ARCHIVED = auto()    # 16


class Workflow:
    """State machine with flag-based states."""

    # Valid transitions
    TRANSITIONS = {
        WorkflowState.NONE: {WorkflowState.DRAFT},
        WorkflowState.DRAFT: {WorkflowState.REVIEW, WorkflowState.ARCHIVED},
        WorkflowState.REVIEW: {WorkflowState.DRAFT, WorkflowState.APPROVED, WorkflowState.ARCHIVED},
        WorkflowState.APPROVED: {WorkflowState.PUBLISHED, WorkflowState.ARCHIVED},
        WorkflowState.PUBLISHED: {WorkflowState.ARCHIVED},
        WorkflowState.ARCHIVED: set(),
    }

    def __init__(self):
        self.state = WorkflowState.NONE
        self.history = []

    def transition(self, new_state):
        """Transition to new state."""
        if not isinstance(new_state, WorkflowState):
            raise TypeError("State must be WorkflowState")

        # Check if transition is valid
        if not self.can_transition_to(new_state):
            valid = self.TRANSITIONS.get(self.state, set())
            raise ValueError(f"Cannot transition from {self.state} to {new_state}. "
                           f"Valid transitions: {valid}")

        # Record history
        self.history.append((self.state, new_state))

        # Update state (combine with existing if both are set)
        if new_state in {WorkflowState.REVIEW, WorkflowState.APPROVED}:
            self.state |= new_state
        else:
            self.state = new_state

    def can_transition_to(self, new_state):
        """Check if transition to new_state is allowed."""
        valid_transitions = self.TRANSITIONS.get(self.state, set())
        return new_state in valid_transitions

    @property
    def active_states(self):
        """Get list of currently active states."""
        if self.state == WorkflowState.NONE:
            return []
        return [s for s in WorkflowState if s != WorkflowState.NONE and s in self.state]

    def has_state(self, state):
        """Check if specific state is active."""
        return bool(self.state & state)

    def __repr__(self):
        states = ' | '.join(s.name for s in self.active_states) or 'NONE'
        return f"Workflow(state={states})"


# Test
workflow = Workflow()
print(workflow)

workflow.transition(WorkflowState.DRAFT)
print(workflow)

workflow.transition(WorkflowState.REVIEW)
print(workflow)
print(f"Active states: {[s.name for s in workflow.active_states]}")

print(f"Can publish? {workflow.can_transition_to(WorkflowState.PUBLISHED)}")
print(f"Can approve? {workflow.can_transition_to(WorkflowState.APPROVED)}")

try:
    workflow.transition(WorkflowState.PUBLISHED)
except ValueError as e:
    print(f"Error: {e}")
```

## Solution 14: Smart Descriptor with __set_name__

```python
import threading

class TypedProperty:
    """Descriptor with type validation and __set_name__."""

    def __init__(self, expected_type, default=None, validator=None):
        self.expected_type = expected_type
        self.default = default
        self.validator = validator
        self.name = None  # Will be set by __set_name__
        self._access_count = {}
        self._lock = threading.Lock()

    def __set_name__(self, owner, name):
        """Called when descriptor is assigned to class attribute."""
        self.name = name
        self.private_name = f'_{name}'

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        # Count access
        with self._lock:
            obj_id = id(obj)
            self._access_count[obj_id] = self._access_count.get(obj_id, 0) + 1

        # Get value or default
        value = getattr(obj, self.private_name, self.default)
        return value

    def __set__(self, obj, value):
        # Type validation
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"'{self.name}' must be {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )

        # Custom validation
        if self.validator is not None:
            if not self.validator(value):
                raise ValueError(f"Validation failed for '{self.name}' with value {value}")

        # Store value
        setattr(obj, self.private_name, value)

    def get_access_count(self, obj):
        """Get access count for specific object."""
        with self._lock:
            return self._access_count.get(id(obj), 0)


def validate_email(email):
    """Simple email validator."""
    return '@' in email and '.' in email.split('@')[1]


class User:
    """User class with typed properties."""
    name = TypedProperty(str)
    age = TypedProperty(int, default=0)
    email = TypedProperty(str, validator=validate_email)

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age}, email={self.email!r})"


# Test
user = User()
user.name = 'Alice'
user.age = 30
user.email = 'alice@example.com'

print(user)

# Access multiple times
for _ in range(5):
    _ = user.name

print(f"Name accessed {User.name.get_access_count(user)} times")

try:
    user.age = 'invalid'
except TypeError as e:
    print(f"Type error: {e}")

try:
    user.email = 'invalid-email'
except ValueError as e:
    print(f"Validation error: {e}")
```

## Solution 15: Custom Formatter System

```python
from math import floor

class Money:
    """Money with currency formatting."""

    SYMBOLS = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£',
        'JPY': '¥'
    }

    def __init__(self, amount, currency='USD'):
        self.amount = amount
        self.currency = currency

    def __format__(self, spec):
        symbol = self.SYMBOLS.get(self.currency, self.currency)

        if spec == '':
            # Default: 2 decimal places with thousands separator
            return f"{symbol}{self.amount:,.2f}"
        elif spec.endswith('f'):
            # Custom precision
            precision = int(spec[:-1]) if spec[:-1] else 2
            return f"{symbol}{self.amount:,.{precision}f}"
        else:
            return f"{symbol}{self.amount}"


class FileSize:
    """File size with unit conversion."""

    def __init__(self, bytes_count):
        self.bytes = bytes_count

    def __format__(self, spec):
        if spec == '' or spec == 'auto':
            # Auto-select appropriate unit
            for unit, divisor in [('GB', 1024**3), ('MB', 1024**2), ('KB', 1024)]:
                if self.bytes >= divisor:
                    value = self.bytes / divisor
                    return f"{value:.2f} {unit}"
            return f"{self.bytes} bytes"
        elif spec == 'KB':
            return f"{self.bytes / 1024:.2f} KB"
        elif spec == 'MB':
            return f"{self.bytes / (1024**2):.2f} MB"
        elif spec == 'GB':
            return f"{self.bytes / (1024**3):.2f} GB"
        elif spec == 'bytes':
            return f"{self.bytes} bytes"
        else:
            raise ValueError(f"Unknown format spec: {spec}")


class Duration:
    """Duration with human-readable formatting."""

    def __init__(self, seconds):
        self.seconds = int(seconds)

    def __format__(self, spec):
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        secs = self.seconds % 60

        if spec == '' or spec == 'long':
            # Long format: 1h 5m 30s
            parts = []
            if hours > 0:
                parts.append(f"{hours}h")
            if minutes > 0:
                parts.append(f"{minutes}m")
            if secs > 0 or not parts:
                parts.append(f"{secs}s")
            return ' '.join(parts)
        elif spec == 'short':
            # Short format: 1:05:30
            return f"{hours}:{minutes:02d}:{secs:02d}"
        elif spec == 'compact':
            # Compact: 1h5m30s (no spaces)
            parts = []
            if hours > 0:
                parts.append(f"{hours}h")
            if minutes > 0:
                parts.append(f"{minutes}m")
            if secs > 0 or not parts:
                parts.append(f"{secs}s")
            return ''.join(parts)
        else:
            raise ValueError(f"Unknown format spec: {spec}")


# Test Money
m = Money(1234.56, currency='USD')
print(f"Default: {m}")           # $1,234.56
print(f"No decimals: {m:.0f}")   # $1,235
print(f"3 decimals: {m:.3f}")    # $1,234.560

m_eur = Money(999.99, currency='EUR')
print(f"Euros: {m_eur}")         # €999.99

# Test FileSize
s = FileSize(1536000)
print(f"Auto: {s}")              # 1.46 MB
print(f"KB: {s:KB}")             # 1500.00 KB
print(f"MB: {s:MB}")             # 1.46 MB
print(f"Bytes: {s:bytes}")       # 1536000 bytes

# Test Duration
d = Duration(3665)
print(f"Long: {d}")              # 1h 1m 5s
print(f"Short: {d:short}")       # 1:01:05
print(f"Compact: {d:compact}")   # 1h1m5s

d2 = Duration(45)
print(f"Short duration: {d2}")   # 45s
```
