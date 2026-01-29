# Examples: Type System & Static Analysis

## Example 1: Basic Type Hints

```python
from typing import List, Dict, Tuple

def greet(name: str) -> str:
    """Simple function with type hints"""
    return f"Hello, {name}!"

def calculate_average(numbers: List[float]) -> float:
    """Calculate average of a list of numbers"""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def process_user_data(user_id: int, metadata: Dict[str, str]) -> Tuple[int, str]:
    """Process user data and return id with formatted info"""
    info = ", ".join(f"{k}={v}" for k, v in metadata.items())
    return user_id, info

# Usage
print(greet("Alice"))  # Hello, Alice!
print(calculate_average([1.5, 2.5, 3.5]))  # 2.5
print(process_user_data(42, {"role": "admin", "status": "active"}))
# Output: (42, 'role=admin, status=active')
```

## Example 2: Optional and Union Types

```python
from typing import Optional, Union

def find_user(user_id: int) -> Optional[str]:
    """Return username or None if not found"""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

def process_input(value: Union[int, str, float]) -> str:
    """Handle multiple input types"""
    if isinstance(value, int):
        return f"Integer: {value}"
    elif isinstance(value, str):
        return f"String: {value}"
    else:
        return f"Float: {value:.2f}"

# Modern syntax (Python 3.10+)
def get_config(key: str) -> str | None:
    """Get config value or None"""
    config = {"debug": "true", "port": "8080"}
    return config.get(key)

# Usage
print(find_user(1))  # Alice
print(find_user(5))  # None
print(process_input(42))  # Integer: 42
print(process_input("test"))  # String: test
print(process_input(3.14159))  # Float: 3.14
```

## Example 3: Generic Classes

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    """A generic stack implementation"""

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """Push item onto stack"""
        self._items.append(item)

    def pop(self) -> T:
        """Pop item from stack"""
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        """View top item without removing"""
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check if stack is empty"""
        return len(self._items) == 0

# Usage
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())  # 2

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")
print(str_stack.peek())  # world
```

## Example 4: Protocol (Structural Subtyping)

```python
from typing import Protocol, List

class Drawable(Protocol):
    """Protocol for objects that can be drawn"""

    def draw(self) -> str:
        """Return string representation of drawing"""
        ...

class Circle:
    """Circle class - implements Drawable implicitly"""

    def __init__(self, radius: float):
        self.radius = radius

    def draw(self) -> str:
        return f"Circle with radius {self.radius}"

class Rectangle:
    """Rectangle class - implements Drawable implicitly"""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def draw(self) -> str:
        return f"Rectangle {self.width}x{self.height}"

def render_shapes(shapes: List[Drawable]) -> None:
    """Render all drawable shapes"""
    for shape in shapes:
        print(shape.draw())

# Usage - works without explicit inheritance
shapes = [Circle(5), Rectangle(10, 20), Circle(3)]
render_shapes(shapes)
# Output:
# Circle with radius 5
# Rectangle 10x20
# Circle with radius 3
```

## Example 5: TypedDict

```python
from typing import TypedDict, List, NotRequired

class UserDict(TypedDict):
    """Structured dictionary for user data"""
    id: int
    name: str
    email: str
    active: bool

class ProductDict(TypedDict, total=False):
    """Product with optional fields (total=False)"""
    id: int
    name: str
    price: float
    description: str  # Optional

class ConfigDict(TypedDict):
    """Config with required and optional fields"""
    host: str
    port: int
    timeout: NotRequired[int]  # Python 3.11+

def create_user(user: UserDict) -> str:
    """Create user from typed dict"""
    return f"User {user['name']} ({user['email']}) created with ID {user['id']}"

def format_product(product: ProductDict) -> str:
    """Format product information"""
    desc = product.get('description', 'No description')
    return f"{product['name']}: ${product.get('price', 0):.2f} - {desc}"

# Usage
user: UserDict = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "active": True
}
print(create_user(user))

product: ProductDict = {"id": 1, "name": "Widget", "price": 29.99}
print(format_product(product))
```

## Example 6: Literal Types

```python
from typing import Literal, get_args

Mode = Literal["read", "write", "append"]
Status = Literal["pending", "approved", "rejected"]

def open_file(filename: str, mode: Mode) -> str:
    """Open file with specific mode"""
    return f"Opening {filename} in {mode} mode"

def update_status(item_id: int, status: Status) -> str:
    """Update item status"""
    valid_statuses = get_args(Status)
    if status not in valid_statuses:
        raise ValueError(f"Invalid status. Must be one of {valid_statuses}")
    return f"Item {item_id} status changed to {status}"

# Usage
print(open_file("data.txt", "read"))  # OK
print(update_status(42, "approved"))  # OK

# These would be caught by type checker:
# open_file("data.txt", "delete")  # Error: invalid mode
# update_status(42, "cancelled")  # Error: invalid status
```

## Example 7: Type Aliases

```python
from typing import List, Dict, Tuple, Union, Callable

# Simple aliases
UserId = int
Username = str
Email = str

# Complex aliases
Coordinate = Tuple[float, float]
Path = List[Coordinate]
UserMap = Dict[UserId, Username]

# Function type aliases
Validator = Callable[[str], bool]
Transformer = Callable[[str], str]

# Union aliases
Number = Union[int, float]
Result = Union[str, Exception]

def calculate_distance(start: Coordinate, end: Coordinate) -> float:
    """Calculate distance between two points"""
    import math
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    return math.sqrt(dx**2 + dy**2)

def get_user_info(user_map: UserMap, user_id: UserId) -> Username:
    """Get username from user map"""
    return user_map.get(user_id, "Unknown")

def validate_email(validator: Validator, email: Email) -> bool:
    """Validate email using provided validator"""
    return validator(email)

# Usage
point1: Coordinate = (0.0, 0.0)
point2: Coordinate = (3.0, 4.0)
print(f"Distance: {calculate_distance(point1, point2):.2f}")  # 5.00

users: UserMap = {1: "Alice", 2: "Bob"}
print(get_user_info(users, 1))  # Alice

email_validator: Validator = lambda e: "@" in e and "." in e
print(validate_email(email_validator, "test@example.com"))  # True
```

## Example 8: Callable Types

```python
from typing import Callable, List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def apply_function(func: Callable[[int], int], value: int) -> int:
    """Apply function to value"""
    return func(value)

def map_list(func: Callable[[T], U], items: List[T]) -> List[U]:
    """Map function over list"""
    return [func(item) for item in items]

def retry(func: Callable[[], T], max_attempts: int = 3) -> T:
    """Retry function up to max_attempts times"""
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            if attempt == max_attempts - 1:
                raise
            print(f"Attempt {attempt + 1} failed: {e}")
    raise RuntimeError("Should not reach here")

# Usage
result = apply_function(lambda x: x * 2, 5)
print(result)  # 10

numbers = [1, 2, 3, 4]
squared = map_list(lambda x: x ** 2, numbers)
print(squared)  # [1, 4, 9, 16]

strings = ["hello", "world"]
lengths = map_list(len, strings)
print(lengths)  # [5, 5]
```

## Example 9: Overload Decorator

```python
from typing import overload, Union, List

@overload
def process(data: int) -> str: ...

@overload
def process(data: str) -> int: ...

@overload
def process(data: List[int]) -> List[str]: ...

def process(data: Union[int, str, List[int]]) -> Union[str, int, List[str]]:
    """Process different types of input"""
    if isinstance(data, int):
        return str(data)
    elif isinstance(data, str):
        return len(data)
    elif isinstance(data, list):
        return [str(x) for x in data]
    raise TypeError(f"Unsupported type: {type(data)}")

# Usage - type checker knows exact return types
result1: str = process(42)  # Type checker knows this returns str
result2: int = process("hello")  # Type checker knows this returns int
result3: List[str] = process([1, 2, 3])  # Returns List[str]

print(result1)  # "42"
print(result2)  # 5
print(result3)  # ['1', '2', '3']
```

## Example 10: Generic Functions with Constraints

```python
from typing import TypeVar, List, Protocol

class Comparable(Protocol):
    """Protocol for comparable objects"""
    def __lt__(self, other: 'Comparable') -> bool: ...
    def __gt__(self, other: 'Comparable') -> bool: ...

T = TypeVar('T', bound=Comparable)

def find_max(items: List[T]) -> T:
    """Find maximum item in list"""
    if not items:
        raise ValueError("Cannot find max of empty list")
    max_item = items[0]
    for item in items[1:]:
        if item > max_item:
            max_item = item
    return max_item

def sort_items(items: List[T]) -> List[T]:
    """Sort items (must be comparable)"""
    return sorted(items)

# Usage - works with any comparable type
print(find_max([1, 5, 3, 2]))  # 5
print(find_max(["apple", "zebra", "banana"]))  # zebra
print(sort_items([3.14, 2.71, 1.41]))  # [1.41, 2.71, 3.14]
```

## Example 11: ParamSpec for Decorator Typing

```python
from typing import TypeVar, Callable, ParamSpec
import time
import functools

P = ParamSpec('P')
T = TypeVar('T')

def timer(func: Callable[P, T]) -> Callable[P, T]:
    """Decorator that times function execution"""
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

def logging(func: Callable[P, T]) -> Callable[P, T]:
    """Decorator that logs function calls"""
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Usage - preserves original function signature
@timer
@logging
def calculate(x: int, y: int, operation: str = "add") -> int:
    """Perform calculation"""
    if operation == "add":
        return x + y
    elif operation == "multiply":
        return x * y
    return 0

result = calculate(5, 3, operation="multiply")
# Output:
# Calling calculate with args=(5, 3), kwargs={'operation': 'multiply'}
# calculate returned 15
# calculate took 0.0001 seconds
```

## Example 12: NewType for Distinct Types

```python
from typing import NewType

# Create distinct types
UserId = NewType('UserId', int)
OrderId = NewType('OrderId', int)
Email = NewType('Email', str)

def get_user(user_id: UserId) -> str:
    """Get user by ID"""
    users = {UserId(1): "Alice", UserId(2): "Bob"}
    return users.get(user_id, "Unknown")

def get_order(order_id: OrderId) -> str:
    """Get order by ID"""
    orders = {OrderId(100): "Order A", OrderId(200): "Order B"}
    return orders.get(order_id, "Not found")

def send_email(email: Email, message: str) -> None:
    """Send email to address"""
    print(f"Sending to {email}: {message}")

# Usage - requires explicit type conversion
user_id = UserId(1)
order_id = OrderId(100)
email = Email("user@example.com")

print(get_user(user_id))  # Alice
print(get_order(order_id))  # Order A
send_email(email, "Hello!")

# Type checker catches this error:
# get_user(order_id)  # Error: OrderId is not UserId
# get_order(user_id)  # Error: UserId is not OrderId
```

## Example 13: TypeGuard for Runtime Type Checking

```python
from typing import TypeGuard, List, Union

def is_string_list(val: List[Union[str, int]]) -> TypeGuard[List[str]]:
    """Check if all elements are strings"""
    return all(isinstance(x, str) for x in val)

def is_int_list(val: List[Union[str, int]]) -> TypeGuard[List[int]]:
    """Check if all elements are integers"""
    return all(isinstance(x, int) for x in val)

def process_strings(items: List[str]) -> str:
    """Process list of strings"""
    return ", ".join(items)

def process_ints(items: List[int]) -> int:
    """Process list of integers"""
    return sum(items)

# Usage
data: List[Union[str, int]] = ["a", "b", "c"]

if is_string_list(data):
    # Type checker knows data is List[str] here
    result = process_strings(data)
    print(result)  # a, b, c

numbers: List[Union[str, int]] = [1, 2, 3]

if is_int_list(numbers):
    # Type checker knows numbers is List[int] here
    result = process_ints(numbers)
    print(result)  # 6
```

## Example 14: Self Type for Method Chaining

```python
from typing import Self  # Python 3.11+

class Builder:
    """Fluent builder with method chaining"""

    def __init__(self) -> None:
        self._name: str = ""
        self._age: int = 0
        self._email: str = ""

    def set_name(self, name: str) -> Self:
        """Set name and return self"""
        self._name = name
        return self

    def set_age(self, age: int) -> Self:
        """Set age and return self"""
        self._age = age
        return self

    def set_email(self, email: str) -> Self:
        """Set email and return self"""
        self._email = email
        return self

    def build(self) -> dict:
        """Build final object"""
        return {
            "name": self._name,
            "age": self._age,
            "email": self._email
        }

class ExtendedBuilder(Builder):
    """Extended builder with additional methods"""

    def set_phone(self, phone: str) -> Self:
        """Set phone and return self"""
        self._phone = phone
        return self

# Usage - method chaining works correctly
user = (Builder()
    .set_name("Alice")
    .set_age(30)
    .set_email("alice@example.com")
    .build())

print(user)
# {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}
```

## Example 15: Advanced mypy Configuration and Usage

```python
# mypy.ini configuration example:
"""
[mypy]
python_version = 3.11
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_any_generics = True
disallow_subclassing_any = True
disallow_untyped_calls = True
disallow_incomplete_defs = True
check_untyped_defs = True
disallow_untyped_decorators = True
no_implicit_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
warn_no_return = True
warn_unreachable = True
strict_equality = True
"""

from typing import Any, cast, TYPE_CHECKING
import sys

# Use TYPE_CHECKING for imports only needed by type checker
if TYPE_CHECKING:
    from collections.abc import Sequence

def strict_function(data: list[int]) -> int:
    """Strictly typed function"""
    return sum(data)

def handle_any(value: Any) -> str:
    """Function that needs to handle Any type"""
    # Use type: ignore when necessary with explanation
    return str(value)  # type: ignore[arg-type]  # Any can be converted to str

def safe_cast_demo(value: object) -> int:
    """Demonstrate safe casting"""
    if isinstance(value, int):
        return value
    # Use cast when you know the type but mypy doesn't
    return cast(int, value)

# Platform-specific typing
if sys.platform == "win32":
    PathType = str
else:
    PathType = bytes

def process_path(path: PathType) -> str:
    """Process platform-specific path"""
    if isinstance(path, bytes):
        return path.decode()
    return path

# Usage
print(strict_function([1, 2, 3]))  # 6
print(handle_any(42))  # "42"
print(safe_cast_demo(5))  # 5

# Run mypy to check types:
# $ mypy script.py --strict
# $ mypy script.py --disallow-untyped-defs
# $ mypy script.py --show-error-codes
```
