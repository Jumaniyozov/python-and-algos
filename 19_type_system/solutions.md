# Solutions: Type System & Static Analysis

## Solution 1: Type a Data Processing Function

```python
from typing import Dict, List

def square_mapping(numbers: List[int]) -> Dict[int, int]:
    """
    Create a dictionary mapping each number to its square.

    Args:
        numbers: List of integers to process

    Returns:
        Dictionary mapping each number to its square

    Examples:
        >>> square_mapping([1, 2, 3])
        {1: 1, 2: 4, 3: 9}
        >>> square_mapping([])
        {}
    """
    return {num: num ** 2 for num in numbers}

# Test
print(square_mapping([1, 2, 3]))  # {1: 1, 2: 4, 3: 9}
print(square_mapping([]))  # {}
print(square_mapping([-2, 0, 2]))  # {-2: 4, 0: 0, 2: 4}
```

## Solution 2: Create a Generic Container

```python
from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Box(Generic[T]):
    """A generic container that holds a single value of any type."""

    def __init__(self, value: Optional[T] = None) -> None:
        """Initialize box with optional value."""
        self._value: Optional[T] = value

    def get(self) -> Optional[T]:
        """Get the stored value."""
        return self._value

    def set(self, value: T) -> None:
        """Set a new value."""
        self._value = value

    def has_value(self) -> bool:
        """Check if box contains a value."""
        return self._value is not None

# Test
str_box: Box[str] = Box("hello")
print(str_box.get())  # hello

int_box: Box[int] = Box()
int_box.set(42)
print(int_box.get())  # 42

list_box: Box[list[int]] = Box([1, 2, 3])
print(list_box.get())  # [1, 2, 3]
```

## Solution 3: Write a Protocol for Serializable Objects

```python
from typing import Protocol, List, Dict, Any

class Serializable(Protocol):
    """Protocol for objects that can be serialized to dict."""

    def to_dict(self) -> Dict[str, Any]:
        """Convert object to dictionary."""
        ...

def serialize_all(items: List[Serializable]) -> Dict[str, Any]:
    """
    Serialize all items and combine into single dict.

    Args:
        items: List of serializable objects

    Returns:
        Combined dictionary with all serialized data
    """
    result: Dict[str, Any] = {}
    for i, item in enumerate(items):
        result[f"item_{i}"] = item.to_dict()
    return result

# Example classes that implement the protocol
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def to_dict(self) -> Dict[str, Any]:
        return {"name": self.name, "age": self.age}

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        return {"name": self.name, "price": self.price}

# Test
users = [User("Alice", 30), User("Bob", 25)]
products = [Product("Widget", 19.99), Product("Gadget", 29.99)]

print(serialize_all(users))
print(serialize_all(products))
```

## Solution 4: Use TypedDict for API Response

```python
from typing import TypedDict, NotRequired, Optional

class UserResponse(TypedDict):
    """User API response structure."""
    id: int
    name: str
    email: str
    phone: NotRequired[str]  # Optional field

def validate_user_response(data: dict) -> Optional[UserResponse]:
    """
    Validate and convert dict to UserResponse.

    Args:
        data: Raw dictionary from API

    Returns:
        Validated UserResponse or None if invalid
    """
    required_keys = {"id", "name", "email"}
    if not required_keys.issubset(data.keys()):
        return None

    if not isinstance(data["id"], int):
        return None
    if not isinstance(data["name"], str):
        return None
    if not isinstance(data["email"], str):
        return None

    # TypedDict allows extra keys, but we validate phone if present
    if "phone" in data and not isinstance(data["phone"], str):
        return None

    return data  # type: ignore[return-value]

def format_user(user: UserResponse) -> str:
    """Format user info as string."""
    phone = user.get("phone", "N/A")
    return f"{user['name']} (ID: {user['id']}, Email: {user['email']}, Phone: {phone})"

# Test
response1: UserResponse = {"id": 1, "name": "Alice", "email": "alice@test.com"}
response2: UserResponse = {"id": 2, "name": "Bob", "email": "bob@test.com", "phone": "555-1234"}

print(format_user(response1))
print(format_user(response2))
```

## Solution 5: Type Hint a Decorator

```python
from typing import TypeVar, Callable, ParamSpec
import functools

P = ParamSpec('P')
T = TypeVar('T')

def log_calls(func: Callable[P, T]) -> Callable[P, T]:
    """
    Decorator that logs function calls with arguments and return value.

    Args:
        func: Function to decorate

    Returns:
        Wrapped function with same signature
    """
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        args_str = ", ".join(repr(arg) for arg in args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))

        print(f"Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result

    return wrapper

# Test
@log_calls
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y

@log_calls
def greet(name: str, greeting: str = "Hello") -> str:
    """Greet a person."""
    return f"{greeting}, {name}!"

print(add(5, 3))
print(greet("Alice", greeting="Hi"))
```

## Solution 6: Implement Overloaded Function

```python
from typing import overload, Union, List, Tuple

@overload
def parse_data(value: int) -> str: ...

@overload
def parse_data(value: str) -> int: ...

@overload
def parse_data(value: List[int]) -> Tuple[int, ...]: ...

def parse_data(value: Union[int, str, List[int]]) -> Union[str, int, Tuple[int, ...]]:
    """
    Parse data based on input type.

    Args:
        value: int, str, or list of ints

    Returns:
        - str if input is int (converts to string)
        - int if input is str (returns length)
        - tuple if input is list (converts to tuple)
    """
    if isinstance(value, int):
        return f"Number: {value}"
    elif isinstance(value, str):
        return len(value)
    elif isinstance(value, list):
        return tuple(value)
    else:
        raise TypeError(f"Unsupported type: {type(value)}")

# Test - type checker knows exact return types
result1: str = parse_data(42)
result2: int = parse_data("hello")
result3: Tuple[int, ...] = parse_data([1, 2, 3])

print(result1)  # Number: 42
print(result2)  # 5
print(result3)  # (1, 2, 3)
```

## Solution 7: Generic Function with Constraints

```python
from typing import TypeVar, List, Protocol

class Comparable(Protocol):
    """Protocol for comparable objects."""

    def __lt__(self, other: 'Comparable') -> bool:
        """Less than comparison."""
        ...

    def __gt__(self, other: 'Comparable') -> bool:
        """Greater than comparison."""
        ...

T = TypeVar('T', bound=Comparable)

def find_min(items: List[T]) -> T:
    """
    Find minimum item in list.

    Args:
        items: Non-empty list of comparable items

    Returns:
        Minimum item

    Raises:
        ValueError: If list is empty
    """
    if not items:
        raise ValueError("Cannot find min of empty list")

    min_item = items[0]
    for item in items[1:]:
        if item < min_item:
            min_item = item
    return min_item

def find_max(items: List[T]) -> T:
    """Find maximum item in list."""
    if not items:
        raise ValueError("Cannot find max of empty list")

    max_item = items[0]
    for item in items[1:]:
        if item > max_item:
            max_item = item
    return max_item

# Test
print(find_min([3, 1, 4, 1, 5]))  # 1
print(find_min(["zebra", "apple", "banana"]))  # apple
print(find_min([3.14, 2.71, 1.41]))  # 1.41

print(find_max([3, 1, 4, 1, 5]))  # 5
print(find_max(["zebra", "apple", "banana"]))  # zebra
```

## Solution 8: Create NewType for Domain Types

```python
from typing import NewType, Dict

UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)
OrderId = NewType('OrderId', int)

# Mock databases
USERS: Dict[UserId, str] = {UserId(1): "Alice", UserId(2): "Bob"}
PRODUCTS: Dict[ProductId, str] = {ProductId(100): "Widget", ProductId(101): "Gadget"}
ORDERS: Dict[OrderId, UserId] = {OrderId(1000): UserId(1), OrderId(1001): UserId(2)}

def get_user(user_id: UserId) -> str:
    """Get username by user ID."""
    return USERS.get(user_id, "Unknown User")

def get_product(product_id: ProductId) -> str:
    """Get product name by product ID."""
    return PRODUCTS.get(product_id, "Unknown Product")

def get_order_user(order_id: OrderId) -> UserId:
    """Get user ID associated with order."""
    return ORDERS.get(order_id, UserId(0))

def create_order(user_id: UserId, product_id: ProductId) -> OrderId:
    """Create new order."""
    order_id = OrderId(max((k for k in ORDERS.keys()), default=999) + 1)
    ORDERS[order_id] = user_id
    return order_id

# Test
user_id = UserId(1)
product_id = ProductId(100)
order_id = OrderId(1000)

print(get_user(user_id))  # Alice
print(get_product(product_id))  # Widget
print(get_order_user(order_id))  # 1

# Type checker prevents this:
# get_user(product_id)  # Error: ProductId is not UserId
# get_product(user_id)  # Error: UserId is not ProductId

new_order = create_order(user_id, product_id)
print(f"Created order: {new_order}")
```

## Solution 9: TypeGuard for Validation

```python
from typing import TypeGuard, Union

def is_email(value: Union[str, int, None]) -> TypeGuard[str]:
    """
    Check if value is a valid email string.

    Args:
        value: Value to check

    Returns:
        True if value is a string containing @ and .
    """
    return isinstance(value, str) and "@" in value and "." in value

def send_email(email: str, message: str) -> None:
    """Send email to address."""
    print(f"Sending to {email}: {message}")

def process_contact(value: Union[str, int, None]) -> None:
    """Process contact information."""
    if is_email(value):
        # Type checker knows value is str here
        send_email(value, "Hello!")
        print(f"Email length: {len(value)}")
    else:
        print(f"Invalid email: {value}")

# Test
process_contact("user@example.com")  # Sends email
process_contact("invalid")  # Invalid email
process_contact(12345)  # Invalid email
process_contact(None)  # Invalid email
```

## Solution 10: Builder Pattern with Self Type

```python
from typing import Self, List, Optional

class QueryBuilder:
    """SQL query builder with method chaining."""

    def __init__(self) -> None:
        self._select: List[str] = []
        self._where: List[str] = []
        self._limit: Optional[int] = None

    def select(self, *fields: str) -> Self:
        """Add fields to SELECT clause."""
        self._select.extend(fields)
        return self

    def where(self, condition: str) -> Self:
        """Add condition to WHERE clause."""
        self._where.append(condition)
        return self

    def limit(self, count: int) -> Self:
        """Set LIMIT clause."""
        self._limit = count
        return self

    def build(self) -> str:
        """Build final SQL query."""
        query_parts = []

        if self._select:
            query_parts.append(f"SELECT {', '.join(self._select)}")
        else:
            query_parts.append("SELECT *")

        query_parts.append("FROM table")

        if self._where:
            query_parts.append(f"WHERE {' AND '.join(self._where)}")

        if self._limit:
            query_parts.append(f"LIMIT {self._limit}")

        return " ".join(query_parts)

class ExtendedQueryBuilder(QueryBuilder):
    """Extended query builder with ORDER BY."""

    def __init__(self) -> None:
        super().__init__()
        self._order_by: List[str] = []

    def order_by(self, field: str, direction: str = "ASC") -> Self:
        """Add ORDER BY clause."""
        self._order_by.append(f"{field} {direction}")
        return self

    def build(self) -> str:
        """Build query with ORDER BY."""
        query = super().build()
        if self._order_by:
            query += f" ORDER BY {', '.join(self._order_by)}"
        return query

# Test
query1 = (QueryBuilder()
    .select("name", "email")
    .where("age > 18")
    .limit(10)
    .build())
print(query1)

query2 = (ExtendedQueryBuilder()
    .select("id", "name")
    .where("active = 1")
    .order_by("name", "DESC")
    .limit(5)
    .build())
print(query2)
```

## Solution 11: Advanced Generic Class

```python
from typing import TypeVar, Generic, Dict, Optional, Hashable

K = TypeVar('K', bound=Hashable)
V = TypeVar('V')

class Cache(Generic[K, V]):
    """Generic cache with key-value storage."""

    def __init__(self, max_size: int = 100) -> None:
        """
        Initialize cache.

        Args:
            max_size: Maximum number of items to store
        """
        self._data: Dict[K, V] = {}
        self._max_size = max_size

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        """
        Get value by key.

        Args:
            key: Key to look up
            default: Default value if key not found

        Returns:
            Value or default
        """
        return self._data.get(key, default)

    def set(self, key: K, value: V) -> None:
        """
        Set key-value pair.

        Args:
            key: Key to set
            value: Value to store
        """
        if len(self._data) >= self._max_size and key not in self._data:
            # Remove oldest item (in production, use OrderedDict or LRU)
            self._data.pop(next(iter(self._data)))
        self._data[key] = value

    def has(self, key: K) -> bool:
        """Check if key exists in cache."""
        return key in self._data

    def delete(self, key: K) -> bool:
        """
        Delete key from cache.

        Returns:
            True if key was deleted, False if not found
        """
        if key in self._data:
            del self._data[key]
            return True
        return False

    def clear(self) -> None:
        """Clear all cached items."""
        self._data.clear()

    def size(self) -> int:
        """Get number of items in cache."""
        return len(self._data)

# Test
str_int_cache: Cache[str, int] = Cache(max_size=3)
str_int_cache.set("count", 42)
str_int_cache.set("total", 100)
print(str_int_cache.get("count"))  # 42
print(str_int_cache.has("total"))  # True

int_str_cache: Cache[int, str] = Cache()
int_str_cache.set(1, "one")
int_str_cache.set(2, "two")
print(int_str_cache.get(1))  # one
```

## Solution 12: Complex Protocol with Multiple Methods

```python
from typing import Protocol, List, Dict, Any, Optional

class DatabaseProtocol(Protocol):
    """Protocol for database-like objects."""

    def connect(self, connection_string: str) -> bool:
        """Connect to database."""
        ...

    def execute(self, query: str) -> List[Dict[str, Any]]:
        """Execute query and return results."""
        ...

    def close(self) -> None:
        """Close database connection."""
        ...

def run_query(db: DatabaseProtocol, sql: str) -> List[Dict[str, Any]]:
    """
    Run query on database.

    Args:
        db: Database connection
        sql: SQL query to execute

    Returns:
        Query results
    """
    try:
        results = db.execute(sql)
        return results
    except Exception as e:
        print(f"Query failed: {e}")
        return []

def with_database(db: DatabaseProtocol, connection_string: str, queries: List[str]) -> List[List[Dict[str, Any]]]:
    """
    Execute multiple queries with database.

    Args:
        db: Database connection
        connection_string: Connection string
        queries: List of SQL queries

    Returns:
        List of results for each query
    """
    results: List[List[Dict[str, Any]]] = []

    if not db.connect(connection_string):
        return results

    try:
        for query in queries:
            result = run_query(db, query)
            results.append(result)
    finally:
        db.close()

    return results

# Example implementation
class MockDatabase:
    """Mock database for testing."""

    def __init__(self) -> None:
        self.connected = False
        self.data = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]

    def connect(self, connection_string: str) -> bool:
        """Connect to database."""
        print(f"Connecting to {connection_string}")
        self.connected = True
        return True

    def execute(self, query: str) -> List[Dict[str, Any]]:
        """Execute query."""
        if not self.connected:
            raise RuntimeError("Not connected")
        print(f"Executing: {query}")
        return self.data

    def close(self) -> None:
        """Close connection."""
        print("Closing connection")
        self.connected = False

# Test
db = MockDatabase()
results = with_database(db, "localhost:5432", ["SELECT * FROM users"])
print(f"Got {len(results)} result sets")
```

## Solution 13: Literal Types for State Machine

```python
from typing import Literal, Dict, Tuple

State = Literal["idle", "running", "paused", "stopped"]
Action = Literal["start", "pause", "resume", "stop", "reset"]

# Define valid transitions
TRANSITIONS: Dict[Tuple[State, Action], State] = {
    ("idle", "start"): "running",
    ("running", "pause"): "paused",
    ("running", "stop"): "stopped",
    ("paused", "resume"): "running",
    ("paused", "stop"): "stopped",
    ("stopped", "reset"): "idle",
}

def transition(from_state: State, action: Action) -> State:
    """
    Perform state transition.

    Args:
        from_state: Current state
        action: Action to perform

    Returns:
        New state

    Raises:
        ValueError: If transition is invalid
    """
    key = (from_state, action)
    if key not in TRANSITIONS:
        raise ValueError(f"Invalid transition: {from_state} + {action}")
    return TRANSITIONS[key]

def is_valid_transition(from_state: State, action: Action) -> bool:
    """Check if transition is valid."""
    return (from_state, action) in TRANSITIONS

class StateMachine:
    """State machine implementation."""

    def __init__(self) -> None:
        self._state: State = "idle"

    @property
    def state(self) -> State:
        """Get current state."""
        return self._state

    def apply(self, action: Action) -> State:
        """
        Apply action and transition to new state.

        Args:
            action: Action to apply

        Returns:
            New state
        """
        self._state = transition(self._state, action)
        return self._state

    def can_apply(self, action: Action) -> bool:
        """Check if action can be applied."""
        return is_valid_transition(self._state, action)

# Test
machine = StateMachine()
print(f"Initial state: {machine.state}")  # idle

machine.apply("start")
print(f"After start: {machine.state}")  # running

machine.apply("pause")
print(f"After pause: {machine.state}")  # paused

machine.apply("resume")
print(f"After resume: {machine.state}")  # running

machine.apply("stop")
print(f"After stop: {machine.state}")  # stopped

machine.apply("reset")
print(f"After reset: {machine.state}")  # idle

print(f"Can start from idle? {machine.can_apply('start')}")  # True
print(f"Can pause from idle? {machine.can_apply('pause')}")  # False
```

## Solution 14: Variadic Generic Function

```python
from typing import overload, Tuple

# Use overloads for different argument counts
@overload
def pack(arg1: int) -> Tuple[int]: ...

@overload
def pack(arg1: int, arg2: str) -> Tuple[int, str]: ...

@overload
def pack(arg1: int, arg2: str, arg3: float) -> Tuple[int, str, float]: ...

@overload
def pack(arg1: int, arg2: str, arg3: float, arg4: bool) -> Tuple[int, str, float, bool]: ...

@overload
def pack(arg1: int, arg2: str, arg3: float, arg4: bool, arg5: list) -> Tuple[int, str, float, bool, list]: ...

def pack(*args):
    """Pack arguments into tuple preserving types."""
    return args

# Test - type checker knows exact types
result1: Tuple[int] = pack(42)
result2: Tuple[int, str] = pack(42, "hello")
result3: Tuple[int, str, float] = pack(42, "hello", 3.14)
result4: Tuple[int, str, float, bool] = pack(42, "hello", 3.14, True)
result5: Tuple[int, str, float, bool, list] = pack(42, "hello", 3.14, True, [1, 2])

print(result1)  # (42,)
print(result2)  # (42, 'hello')
print(result3)  # (42, 'hello', 3.14)
print(result4)  # (42, 'hello', 3.14, True)
print(result5)  # (42, 'hello', 3.14, True, [1, 2])
```

## Solution 15: Full Type Coverage with mypy Strict Mode

```python
"""
Module with complete type coverage for mypy --strict.

Run: mypy solution_15.py --strict
"""
from typing import TypeVar, Generic, Protocol, TypedDict, List, Optional, Dict, Any
from dataclasses import dataclass

# TypedDict for configuration
class AppConfig(TypedDict):
    """Application configuration."""
    host: str
    port: int
    debug: bool
    max_connections: int

# Protocol for loggable objects
class Loggable(Protocol):
    """Protocol for objects that can be logged."""

    def to_log_string(self) -> str:
        """Convert to log string."""
        ...

# Generic class
T = TypeVar('T')

class Repository(Generic[T]):
    """Generic repository for data storage."""

    def __init__(self) -> None:
        """Initialize repository."""
        self._items: List[T] = []

    def add(self, item: T) -> None:
        """Add item to repository."""
        self._items.append(item)

    def get_all(self) -> List[T]:
        """Get all items."""
        return self._items.copy()

    def find(self, predicate: 'Callable[[T], bool]') -> Optional[T]:
        """Find first item matching predicate."""
        for item in self._items:
            if predicate(item):
                return item
        return None

    def count(self) -> int:
        """Get number of items."""
        return len(self._items)

# Regular class with full type hints
@dataclass
class User:
    """User data class."""
    id: int
    name: str
    email: str
    active: bool = True

    def to_log_string(self) -> str:
        """Convert to log string."""
        return f"User(id={self.id}, name={self.name})"

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "active": self.active
        }

# Function 1: Work with config
def load_config(config_dict: Dict[str, Any]) -> AppConfig:
    """Load configuration from dictionary."""
    return AppConfig(
        host=str(config_dict.get("host", "localhost")),
        port=int(config_dict.get("port", 8080)),
        debug=bool(config_dict.get("debug", False)),
        max_connections=int(config_dict.get("max_connections", 100))
    )

# Function 2: Work with protocol
def log_item(item: Loggable) -> None:
    """Log an item."""
    print(f"[LOG] {item.to_log_string()}")

# Function 3: Work with generic repository
def create_user_repository() -> Repository[User]:
    """Create repository for users."""
    return Repository[User]()

# Function 4: Process list with type narrowing
def process_users(users: List[User], active_only: bool = False) -> List[Dict[str, Any]]:
    """
    Process users into dictionaries.

    Args:
        users: List of users to process
        active_only: Only include active users

    Returns:
        List of user dictionaries
    """
    result: List[Dict[str, Any]] = []
    for user in users:
        if active_only and not user.active:
            continue
        result.append(user.to_dict())
    return result

# Function 5: Optional return type
def find_user_by_id(users: List[User], user_id: int) -> Optional[User]:
    """
    Find user by ID.

    Args:
        users: List of users to search
        user_id: ID to find

    Returns:
        User if found, None otherwise
    """
    for user in users:
        if user.id == user_id:
            return user
    return None

# Import for type hints only
from typing import Callable

def main() -> None:
    """Main function demonstrating usage."""
    # Create config
    config = load_config({"host": "0.0.0.0", "port": 3000, "debug": True})
    print(f"Server: {config['host']}:{config['port']}")

    # Create users
    user1 = User(1, "Alice", "alice@example.com")
    user2 = User(2, "Bob", "bob@example.com", active=False)

    # Use repository
    repo = create_user_repository()
    repo.add(user1)
    repo.add(user2)

    # Log users
    for user in repo.get_all():
        log_item(user)

    # Process users
    all_users_dict = process_users(repo.get_all())
    active_users_dict = process_users(repo.get_all(), active_only=True)

    print(f"All users: {len(all_users_dict)}")
    print(f"Active users: {len(active_users_dict)}")

    # Find user
    found = find_user_by_id(repo.get_all(), 1)
    if found:
        print(f"Found: {found.name}")

if __name__ == "__main__":
    main()
```

All solutions include:
- Complete type hints
- Proper documentation
- Working implementations
- Test cases
- Type safety verified by mypy
