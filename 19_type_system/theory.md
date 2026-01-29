# Theory: Type System & Static Analysis

## Introduction

Python's type system provides optional static type checking that helps catch bugs early, improves code documentation, and enables better IDE support. This chapter covers type hints, generics, protocols, and type checking tools.

## Core Concepts

### 1. Type Hints

**Overview**: Type hints (PEP 484) allow you to annotate variables, function parameters, and return types without affecting runtime behavior.

**Key Points**:
- Type hints are optional and ignored at runtime
- They help catch bugs with static analysis tools like mypy
- Improve code readability and IDE autocomplete
- No performance overhead

**Basic Syntax**:
```python
from typing import List, Dict, Optional, Union

# Variable annotations
name: str = "Alice"
age: int = 30
scores: List[int] = [95, 87, 92]

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

def process_data(
    data: List[int],
    multiplier: float = 1.0
) -> Dict[str, float]:
    return {
        "sum": sum(data) * multiplier,
        "avg": sum(data) / len(data) * multiplier
    }

# Optional and Union types
def find_user(user_id: int) -> Optional[str]:
    # Returns str or None
    return users.get(user_id)

def parse_value(val: Union[int, str]) -> int:
    # Accepts int or str
    return int(val)
```

**Common Type Annotations**:
```python
from typing import List, Dict, Set, Tuple, Optional, Union, Any, Callable

# Built-in types
x: int = 5
y: float = 3.14
name: str = "Alice"
is_valid: bool = True

# Collections
numbers: List[int] = [1, 2, 3]
mapping: Dict[str, int] = {"a": 1, "b": 2}
unique: Set[str] = {"x", "y", "z"}
coord: Tuple[int, int] = (10, 20)

# Optional (can be None)
maybe_value: Optional[int] = None

# Union (multiple types)
id_value: Union[int, str] = 123

# Any (any type)
data: Any = {"key": "value"}

# Callable
transformer: Callable[[int], str] = str
```

### 2. Generics (TypeVar and Generic)

**Overview**: Generics allow you to write reusable code that works with multiple types while maintaining type safety.

**Key Points**:
- TypeVar creates type variables
- Generic[T] creates generic classes
- Preserves type information through operations
- Enables type-safe containers

**Example**:
```python
from typing import TypeVar, Generic, List

# Define a type variable
T = TypeVar('T')

class Stack(Generic[T]):
    """Generic stack that works with any type"""
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

# Usage - type checker knows the types
int_stack: Stack[int] = Stack()
int_stack.push(5)
value: int = int_stack.pop()  # Type checker knows this is int

str_stack: Stack[str] = Stack()
str_stack.push("hello")
text: str = str_stack.pop()  # Type checker knows this is str
```

**Generic Functions**:
```python
from typing import TypeVar, List, Sequence

T = TypeVar('T')

def first(items: Sequence[T]) -> T:
    """Get first item - type is preserved"""
    return items[0]

def last(items: List[T]) -> T:
    """Get last item - type is preserved"""
    return items[-1]

# Type checker understands return types
x: int = first([1, 2, 3])  # x is int
y: str = last(["a", "b"])  # y is str
```

### 3. Protocols (Structural Subtyping)

**Overview**: Protocols (PEP 544) enable structural subtyping - types are compatible if they have the required methods, regardless of inheritance.

**Key Points**:
- Duck typing with type checking
- No need for explicit inheritance
- Define interfaces without ABC
- More flexible than nominal typing

**Example**:
```python
from typing import Protocol

class Drawable(Protocol):
    """Protocol for drawable objects"""
    def draw(self) -> None:
        ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

class Square:
    def draw(self) -> None:
        print("Drawing square")

def render(shape: Drawable) -> None:
    """Accepts anything with draw() method"""
    shape.draw()

# Both work without inheriting from Drawable
render(Circle())  # OK
render(Square())  # OK
```

**Runtime Checkable Protocols**:
```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Comparable(Protocol):
    def __lt__(self, other: 'Comparable') -> bool:
        ...

def sort_items(items: List[Comparable]) -> List[Comparable]:
    return sorted(items)

# Can use isinstance at runtime
if isinstance(obj, Comparable):
    print("Object is comparable")
```

### 4. TypedDict

**Overview**: TypedDict allows you to specify the structure of dictionaries with specific keys and value types.

**Key Points**:
- Type-safe dictionaries
- Specify required and optional keys
- Better than Dict[str, Any]
- Useful for API responses, config

**Example**:
```python
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
    email: str
    age: int

# Type checker validates structure
user: User = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "age": 30
}

def get_user_info(user: User) -> str:
    # Type checker knows these keys exist
    return f"{user['name']} ({user['email']})"
```

**Optional Keys**:
```python
from typing import TypedDict, NotRequired

class Config(TypedDict):
    host: str
    port: int
    debug: NotRequired[bool]  # Optional key

config: Config = {
    "host": "localhost",
    "port": 8080
    # debug is optional
}
```

### 5. mypy - Static Type Checker

**Overview**: mypy is the most popular static type checker for Python that analyzes code and reports type errors.

**Key Points**:
- Catches type errors before runtime
- Configurable strictness levels
- Integrates with IDEs and CI/CD
- Can check legacy code incrementally

**Installation and Usage**:
```bash
# Install mypy
pip install mypy

# Check a file
mypy script.py

# Check a package
mypy package/

# With strict mode
mypy --strict script.py
```

**Configuration (mypy.ini)**:
```ini
[mypy]
python_version = 3.11
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_incomplete_defs = True

[mypy-thirdparty.*]
ignore_missing_imports = True
```

**Example with mypy**:
```python
def add(a: int, b: int) -> int:
    return a + b

# mypy will catch this error
result: str = add(5, 3)  # Error: int cannot be assigned to str

# mypy will catch this error
add("5", "3")  # Error: str cannot be passed where int is expected
```

## Advanced Type Features

### Literal Types
```python
from typing import Literal

def set_mode(mode: Literal["read", "write", "append"]) -> None:
    """Only accepts specific string values"""
    pass

set_mode("read")  # OK
set_mode("delete")  # Error: invalid literal
```

### Type Aliases
```python
from typing import List, Dict, Tuple

# Simple alias
UserId = int
Username = str

# Complex alias
Point = Tuple[float, float]
Matrix = List[List[float]]
UserMap = Dict[UserId, Username]

def get_distance(p1: Point, p2: Point) -> float:
    """Type alias makes intent clear"""
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
```

### Forward References
```python
from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, value: int):
        self.value: int = value
        self.left: Optional[TreeNode] = None  # Forward reference
        self.right: Optional[TreeNode] = None
```

## Summary

Python's type system provides powerful static analysis capabilities while maintaining the language's dynamic nature. Type hints improve code quality, documentation, and tooling support without runtime overhead.

## Key Takeaways

1. **Type hints are optional**: They don't affect runtime behavior
2. **Use mypy for checking**: Static analysis catches bugs early
3. **Generics for reusability**: Write type-safe generic code
4. **Protocols for flexibility**: Duck typing with type safety
5. **TypedDict for structures**: Type-safe dictionaries
6. **Progressive typing**: Add types incrementally to existing code
7. **IDE benefits**: Better autocomplete and refactoring
8. **Documentation**: Types serve as inline documentation
