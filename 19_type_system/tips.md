# Tips & Best Practices: Type System & Static Analysis

## Best Practices

### Tip 1: Start with Function Signatures

Always type your function signatures first. This provides the most value with minimal effort.

```python
# Good - clear types from the start
def process_data(items: list[int], threshold: float) -> dict[str, int]:
    return {"count": len([x for x in items if x > threshold])}

# Bad - no type information
def process_data(items, threshold):
    return {"count": len([x for x in items if x > threshold])}
```

### Tip 2: Use Modern Syntax (Python 3.10+)

Prefer the new syntax over typing module when possible:

```python
# Modern (Python 3.10+)
def greet(name: str) -> str | None:
    return f"Hello, {name}" if name else None

def process(data: list[int | str]) -> dict[str, list[int]]:
    pass

# Older style
from typing import Optional, Union, List, Dict
def greet(name: str) -> Optional[str]:
    return f"Hello, {name}" if name else None
```

### Tip 3: Use TypedDict for Dictionary Shapes

When working with structured dictionaries, use TypedDict for clarity:

```python
from typing import TypedDict

class UserData(TypedDict):
    id: int
    name: str
    email: str

def create_user(data: UserData) -> None:
    # Type checker knows exact keys and types
    print(data["name"])  # OK
    # print(data["age"])  # Error: 'age' not in UserData
```

### Tip 4: Leverage Protocol for Structural Typing

Use Protocol instead of inheritance when you only care about behavior:

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:
        return "Circle"

class Square:
    def draw(self) -> str:
        return "Square"

# Both work without inheriting from Drawable
def render(obj: Drawable) -> None:
    print(obj.draw())
```

### Tip 5: Use Generic for Reusable Data Structures

Make containers generic when they work with multiple types:

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# Type-safe usage
int_stack: Stack[int] = Stack()
str_stack: Stack[str] = Stack()
```

### Tip 6: Configure mypy Properly

Use a mypy.ini file for consistent checking:

```ini
[mypy]
python_version = 3.11
warn_return_any = True
warn_unused_configs = True
warn_redundant_casts = True
warn_unused_ignores = True
disallow_untyped_defs = True
check_untyped_defs = True
no_implicit_optional = True
strict_equality = True
```

### Tip 7: Use NewType for Domain-Specific Types

Create distinct types for better type safety:

```python
from typing import NewType

UserId = NewType('UserId', int)
ProductId = NewType('ProductId', int)

def get_user(user_id: UserId) -> str: ...
def get_product(product_id: ProductId) -> str: ...

# Type checker catches mixing these up
user = get_user(UserId(1))  # OK
# user = get_user(ProductId(1))  # Error!
```

### Tip 8: Use ParamSpec for Decorator Typing

Preserve function signatures in decorators:

```python
from typing import TypeVar, ParamSpec, Callable
import functools

P = ParamSpec('P')
T = TypeVar('T')

def logged(func: Callable[P, T]) -> Callable[P, T]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

## Common Pitfalls

### Pitfall 1: Overusing Any

Avoid `Any` type as it defeats the purpose of type checking:

```python
from typing import Any

# Bad - loses all type information
def process(data: Any) -> Any:
    return data.upper()

# Good - specific types
def process(data: str) -> str:
    return data.upper()

# Better - generic when needed
from typing import TypeVar
T = TypeVar('T')
def process(data: T) -> T:
    return data
```

### Pitfall 2: Forgetting Optional

None values must be explicitly typed:

```python
# Bad - mypy error with strict mode
def find_user(user_id: int) -> str:
    users = {1: "Alice"}
    return users.get(user_id)  # Could return None!

# Good - explicit optional
from typing import Optional
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice"}
    return users.get(user_id)
```

### Pitfall 3: Mutable Default Arguments

Type hints don't solve mutable default issues:

```python
from typing import List

# Still problematic
def add_item(item: int, items: List[int] = []) -> List[int]:
    items.append(item)
    return items

# Better
def add_item(item: int, items: List[int] | None = None) -> List[int]:
    if items is None:
        items = []
    items.append(item)
    return items
```

### Pitfall 4: Incorrect Generic Bounds

Be careful with TypeVar bounds:

```python
from typing import TypeVar

# Bad - too restrictive
T = TypeVar('T', int, str)  # Only int or str

# Good - for comparable types
from typing import Protocol
class Comparable(Protocol):
    def __lt__(self, other) -> bool: ...

T = TypeVar('T', bound=Comparable)  # Any comparable type
```

### Pitfall 5: Not Using TYPE_CHECKING

Avoid circular imports in type hints:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from my_module import SomeClass  # Only imported for type checking

def process(obj: 'SomeClass') -> None:  # Use string annotation
    pass
```

## Performance Considerations

### Performance Tip 1: Type Hints Have Zero Runtime Cost

Type hints are discarded at runtime in standard Python:

```python
# These have identical performance
def add_slow(x, y):
    return x + y

def add_fast(x: int, y: int) -> int:
    return x + y

# Type checking happens before runtime
```

### Performance Tip 2: Use Literal for Constants

Literal types help optimize constant values:

```python
from typing import Literal

Mode = Literal["read", "write"]

def open_file(mode: Mode) -> None:
    # Type checker ensures only valid modes
    if mode == "read":  # Can optimize this check
        pass
```

### Performance Tip 3: Protocol vs ABC

Protocols are checked statically, ABCs at runtime:

```python
from typing import Protocol
from abc import ABC, abstractmethod

# Static checking only (faster)
class Drawable(Protocol):
    def draw(self) -> str: ...

# Runtime checking (slower)
class DrawableABC(ABC):
    @abstractmethod
    def draw(self) -> str: ...
```

## Real-World Patterns

### Pattern 1: Builder Pattern with Self

```python
from typing import Self

class QueryBuilder:
    def select(self, field: str) -> Self:
        self._fields.append(field)
        return self

    def where(self, condition: str) -> Self:
        self._conditions.append(condition)
        return self

    def build(self) -> str:
        return f"SELECT {','.join(self._fields)} WHERE {' AND '.join(self._conditions)}"

# Chain calls
query = QueryBuilder().select("name").where("age > 18").build()
```

### Pattern 2: Result Type for Error Handling

```python
from typing import TypeVar, Generic

T = TypeVar('T')
E = TypeVar('E')

class Result(Generic[T, E]):
    def __init__(self, value: T | None = None, error: E | None = None):
        self._value = value
        self._error = error

    def is_ok(self) -> bool:
        return self._error is None

    def unwrap(self) -> T:
        if self._error:
            raise ValueError(f"Called unwrap on error: {self._error}")
        return self._value  # type: ignore

def divide(a: int, b: int) -> Result[float, str]:
    if b == 0:
        return Result(error="Division by zero")
    return Result(value=a / b)
```

### Pattern 3: Type-Safe State Machine

```python
from typing import Literal

State = Literal["idle", "running", "stopped"]
Event = Literal["start", "stop"]

def transition(state: State, event: Event) -> State:
    if state == "idle" and event == "start":
        return "running"
    elif state == "running" and event == "stop":
        return "stopped"
    return state
```

### Pattern 4: Generic Factory

```python
from typing import TypeVar, Type, Generic

T = TypeVar('T')

class Factory(Generic[T]):
    def __init__(self, cls: Type[T]):
        self._cls = cls

    def create(self, *args, **kwargs) -> T:
        return self._cls(*args, **kwargs)

class User:
    def __init__(self, name: str):
        self.name = name

user_factory: Factory[User] = Factory(User)
user = user_factory.create("Alice")  # Type is User
```

## Debugging Tips

### Debug Tip 1: Use reveal_type

Find out what mypy thinks a type is:

```python
from typing import reveal_type

def process(data):
    reveal_type(data)  # mypy will show the inferred type
    return data.upper()
```

### Debug Tip 2: Check with --show-error-codes

Get specific error codes for targeted ignores:

```bash
mypy script.py --show-error-codes
# error: Incompatible return value type [return-value]
```

```python
# Then use specific ignores
return value  # type: ignore[return-value]
```

### Debug Tip 3: Use assert_type for Testing

Verify types in tests:

```python
from typing import assert_type

def test_process():
    result = process([1, 2, 3])
    assert_type(result, list[int])  # Fails if wrong type
```

### Debug Tip 4: Enable Incremental Mode

Speed up mypy with caching:

```bash
mypy --incremental script.py
```

Or in mypy.ini:
```ini
[mypy]
incremental = True
cache_dir = .mypy_cache
```

## Key Takeaways

1. **Start Simple**: Begin with function signatures, gradually add more complex types
2. **Use Modern Syntax**: Prefer `list[int]` over `List[int]` in Python 3.9+
3. **Protocol Over Inheritance**: Use structural typing when possible
4. **TypedDict for Dicts**: Make dictionary shapes explicit
5. **Generic for Reusability**: Create type-safe, reusable components
6. **Configure mypy**: Use mypy.ini for consistent team standards
7. **Avoid Any**: Be specific with types or use generics
8. **Document Decisions**: Add comments explaining complex type choices
9. **Incremental Adoption**: Type critical paths first, expand gradually
10. **Test Type Coverage**: Use mypy in CI/CD pipelines

## Quick Reference

### Common Type Constructs

```python
from typing import (
    List, Dict, Set, Tuple,  # Collections
    Optional, Union,          # Nullability and alternatives
    Callable, TypeVar,        # Functions and generics
    Protocol, TypedDict,      # Structural types
    Literal, Final,           # Constants
    overload,                 # Function overloading
    Generic,                  # Generic classes
    ParamSpec,                # Decorator typing
)

# Modern syntax (3.10+)
x: int | str | None          # Union with None
y: list[int]                 # Generic list
z: dict[str, list[int]]      # Nested generics
```

### mypy Commands

```bash
# Basic check
mypy script.py

# Strict mode
mypy script.py --strict

# Show error codes
mypy script.py --show-error-codes

# Check specific module
mypy -m mymodule

# Generate coverage report
mypy script.py --html-report ./mypy-report
```
