# Chapter 21: Niche Features - Exercises

## Exercise 1: Ellipsis-Based Configuration (Easy)

Create a `Config` class that uses ellipsis (`...`) to indicate "inherit from parent config". The class should support nested configuration with inheritance.

**Requirements**:
- Accept parent config in constructor
- Use `...` to indicate inherited values
- Support nested dictionaries
- Provide method to resolve all values

**Example**:
```python
parent = Config({'timeout': 30, 'retries': 3, 'debug': False})
child = Config({'timeout': ..., 'retries': 5, 'debug': ...}, parent=parent)
# child.resolve() should return {'timeout': 30, 'retries': 5, 'debug': False}
```

## Exercise 2: Walrus Operator File Parser (Easy)

Write a function `parse_log_file(filename)` that uses the walrus operator to read and parse a log file line by line, extracting only lines that contain "ERROR" or "WARNING".

**Requirements**:
- Use walrus operator in while loop
- Extract timestamp and message
- Return list of parsed entries
- Handle file not found gracefully

**Example**:
```python
# Sample log:
# 2024-01-15 10:30:00 INFO System started
# 2024-01-15 10:30:15 ERROR Connection failed
# 2024-01-15 10:30:20 WARNING Low memory

result = parse_log_file('app.log')
# Returns: [{'time': '10:30:15', 'level': 'ERROR', 'msg': 'Connection failed'}, ...]
```

## Exercise 3: Smart Function Parameters (Easy)

Create a function `create_report(data, /, *, format='pdf', include_charts=True, template=None)` that generates reports with proper parameter restrictions.

**Requirements**:
- `data` must be positional-only
- `format`, `include_charts`, `template` must be keyword-only
- Validate format is one of: 'pdf', 'html', 'markdown'
- Return dictionary with report metadata

**Example**:
```python
report = create_report([1, 2, 3], format='html', include_charts=False)
```

## Exercise 4: Auto-Counting Dict (Easy)

Implement `CountingDict` that uses `__missing__` to automatically initialize counters for new keys and increment them.

**Requirements**:
- Start count at 0 for new keys
- Support increment() method
- Support += operator
- Track total accesses to missing keys

**Example**:
```python
counter = CountingDict()
counter['apple'] += 1
counter['banana'] += 1
counter['apple'] += 1
# counter = {'apple': 2, 'banana': 1}
```

## Exercise 5: HTTP Status Enum (Easy)

Create an `HTTPStatus` enum with common status codes (200, 404, 500, etc.) that includes:
- Numeric value
- Descriptive name
- Method to check if status is error (>= 400)
- Method to get status category (2xx, 4xx, 5xx)

**Requirements**:
- At least 8 different status codes
- `is_error()` method
- `category()` method returning string like "2xx"
- `description()` method with human-readable text

## Exercise 6: Sentinel-Based Cache (Medium)

Implement a `Cache` class using sentinel values to distinguish between:
- Cached `None` values
- Cache miss (key never set)
- Expired cache entries

**Requirements**:
- Use different sentinels for "miss" and "expired"
- Support TTL (time-to-live)
- `get()` method that takes default parameter
- `set()` method with optional TTL
- Clear expired entries automatically

**Example**:
```python
cache = Cache()
cache.set('key1', None)  # Explicitly cache None
cache.get('key1')  # Returns None (cached)
cache.get('key2')  # Returns sentinel CACHE_MISS
cache.get('key2', 'default')  # Returns 'default'
```

## Exercise 7: Dynamic API Client (Medium)

Create an `APIClient` class using `__getattr__` that converts attribute access into API endpoint calls.

**Requirements**:
- `client.users.list()` → GET /users/list
- `client.posts.create(data)` → POST /posts/create
- Chain attributes for nested endpoints
- Return mock response (don't make real HTTP calls)

**Example**:
```python
api = APIClient('https://api.example.com')
response = api.users.profile.get(user_id=123)
# Simulates: GET https://api.example.com/users/profile?user_id=123
```

## Exercise 8: Validated Attributes (Medium)

Implement a `ValidatedUser` class using `__setattr__` that:
- Validates email format
- Ensures age is between 0-150
- Converts username to lowercase
- Prevents setting protected attributes (_id, _created_at)

**Requirements**:
- Type validation
- Range validation for age
- Regex validation for email
- Raise appropriate errors with clear messages

**Example**:
```python
user = ValidatedUser()
user.email = 'test@example.com'  # OK
user.age = 25  # OK
user.age = 200  # Raises ValueError
user._id = 123  # Raises AttributeError
```

## Exercise 9: Memory-Efficient Data Class (Medium)

Create a `DataPoint` class using `__slots__` for storing sensor data with:
- timestamp
- sensor_id
- temperature
- humidity
- Compare memory usage vs regular class

**Requirements**:
- Use `__slots__`
- Implement `__repr__`
- Implement comparison methods
- Create 10,000 instances and measure memory

**Example**:
```python
dp = DataPoint(time.time(), 'sensor_1', 22.5, 65.0)
print(dp)  # DataPoint(sensor_1: 22.5°C, 65.0% at 1234567890)
```

## Exercise 10: File Format Enum (Medium)

Create a `FileFormat` enum with auto-generated extensions and MIME types:
- Image formats (JPEG, PNG, GIF, WebP)
- Document formats (PDF, DOCX, TXT)
- Methods to check if format is image/document
- Method to get file extension

**Requirements**:
- Use `auto()` for values
- Store extension and MIME type per format
- `is_image()` and `is_document()` methods
- `get_extension()` method

## Exercise 11: Plugin System with Metadata (Hard)

Create a plugin system using `__init_subclass__` where plugins:
- Auto-register with name and version
- Declare dependencies on other plugins
- Have priority levels
- Can be enabled/disabled

**Requirements**:
- Validate dependencies exist
- Sort plugins by priority
- Check circular dependencies
- Provide `get_plugin()` and `list_plugins()` methods

**Example**:
```python
class PluginBase:
    ...

class DatabasePlugin(PluginBase, name='database', version='1.0', priority=10):
    def initialize(self):
        return "Database initialized"

class CachePlugin(PluginBase, name='cache', version='2.0',
                  depends=['database'], priority=20):
    def initialize(self):
        return "Cache initialized"
```

## Exercise 12: Multi-Type Container (Hard)

Implement a `TypedContainer` using `__getitem__` and `__setitem__` that:
- Stores different types in separate internal containers
- Accepts ellipsis to get all items
- Accepts type as key to get all items of that type
- Accepts integer index for positional access

**Requirements**:
- `container[int]` returns all integers
- `container[...]` returns all items
- `container[0]` returns first item
- `container[str] = 'hello'` adds string

**Example**:
```python
container = TypedContainer()
container[int] = 42
container[str] = 'hello'
container[int] = 100
print(container[int])  # [42, 100]
print(container[...])  # [42, 'hello', 100]
```

## Exercise 13: State Machine with Flags (Hard)

Create a state machine using Flag enum for workflow states:
- Multiple states can be active simultaneously
- Valid state transitions defined
- Check if transition is allowed
- Get active states

**Requirements**:
- Use Flag enum for states
- States: DRAFT, REVIEW, APPROVED, PUBLISHED, ARCHIVED
- Allow combinations like REVIEW | APPROVED
- Validate transitions
- Track state history

**Example**:
```python
workflow = Workflow()
workflow.transition(WorkflowState.DRAFT)
workflow.transition(WorkflowState.REVIEW)
print(workflow.can_transition_to(WorkflowState.PUBLISHED))  # False
print(workflow.active_states)  # [DRAFT, REVIEW]
```

## Exercise 14: Smart Descriptor with __set_name__ (Hard)

Create a `TypedProperty` descriptor that:
- Uses `__set_name__` to know its attribute name
- Validates type at assignment
- Supports optional default value
- Logs access if in debug mode
- Caches validation results

**Requirements**:
- Type checking with isinstance()
- Optional conversion (e.g., str to int)
- Thread-safe access counting
- Clear error messages with attribute name

**Example**:
```python
class User:
    name = TypedProperty(str)
    age = TypedProperty(int, default=0)
    email = TypedProperty(str, validator=validate_email)

user = User()
user.name = 'Alice'  # OK
user.age = 'invalid'  # Raises TypeError
```

## Exercise 15: Custom Formatter System (Hard)

Build a formatting system using `__format__` for different data types:
- `Money`: formats as currency with symbol
- `FileSize`: formats bytes as KB/MB/GB
- `Duration`: formats seconds as human-readable
- Support custom format specs

**Requirements**:
- Default format for each type
- Precision control (e.g., `{money:.2f}`)
- Unit control (e.g., `{size:MB}`)
- Locale support for Money (optional)

**Example**:
```python
m = Money(1234.56, currency='USD')
print(f"{m}")  # $1,234.56
print(f"{m:.0f}")  # $1,235

s = FileSize(1536000)
print(f"{s}")  # 1.46 MB
print(f"{s:KB}")  # 1500.00 KB

d = Duration(3665)
print(f"{d}")  # 1h 1m 5s
print(f"{d:short}")  # 1:01:05
```
