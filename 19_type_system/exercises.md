# Exercises: Type System & Static Analysis

## Exercise 1: Type a Data Processing Function (Easy)

Write a function that takes a list of integers and returns a dictionary mapping each number to its square. Add complete type hints.

**Requirements**:
- Function signature with type hints
- Handle empty lists
- Return type must be Dict[int, int]

**Example**:
```python
# Input: [1, 2, 3]
# Output: {1: 1, 2: 4, 3: 9}
```

## Exercise 2: Create a Generic Container (Easy)

Implement a generic `Box` class that can hold a single value of any type with methods to get and set the value.

**Requirements**:
- Use Generic[T]
- Implement get() -> T
- Implement set(value: T) -> None
- Type hints for all methods

**Example**:
```python
box: Box[str] = Box("hello")
print(box.get())  # "hello"
```

## Exercise 3: Write a Protocol for Serializable Objects (Easy)

Create a Protocol that defines objects that can be serialized to a dictionary, then write a function that uses it.

**Requirements**:
- Protocol with to_dict() method
- Function accepting List[Serializable]
- Return combined dictionary

**Example**:
```python
def serialize_all(items: List[Serializable]) -> Dict[str, Any]: ...
```

## Exercise 4: Use TypedDict for API Response (Easy)

Define a TypedDict for a user API response with id, name, email (required) and phone (optional).

**Requirements**:
- Required fields: id, name, email
- Optional field: phone
- Function to validate and process response

**Example**:
```python
response: UserResponse = {"id": 1, "name": "Alice", "email": "a@test.com"}
```

## Exercise 5: Type Hint a Decorator (Medium)

Create a decorator that logs function calls. Use proper type hints including ParamSpec and TypeVar.

**Requirements**:
- Preserve function signature
- Use ParamSpec and TypeVar
- Log arguments and return value

**Example**:
```python
@log_calls
def add(x: int, y: int) -> int:
    return x + y
```

## Exercise 6: Implement Overloaded Function (Medium)

Create a function `parse_data` that accepts int (returns str), str (returns int), or list (returns tuple). Use @overload.

**Requirements**:
- Three overload signatures
- Type checker knows exact return type
- Runtime implementation

**Example**:
```python
result: str = parse_data(42)  # Type checker knows it's str
```

## Exercise 7: Generic Function with Constraints (Medium)

Write a generic function that finds the minimum of a list, but only works with comparable types.

**Requirements**:
- Use TypeVar with bound parameter
- Create Comparable Protocol
- Works with int, str, float

**Example**:
```python
print(find_min([3, 1, 4]))  # 1
print(find_min(["c", "a", "b"]))  # "a"
```

## Exercise 8: Create NewType for Domain Types (Medium)

Create distinct types for UserId, ProductId, and OrderId (all based on int), and functions that use them.

**Requirements**:
- Three NewType definitions
- Functions enforcing type distinctions
- Type checker prevents mixing

**Example**:
```python
user = get_user(UserId(1))  # OK
user = get_user(ProductId(1))  # Type error
```

## Exercise 9: TypeGuard for Validation (Medium)

Write a type guard function that checks if a value is a valid email string and use it to narrow types.

**Requirements**:
- TypeGuard return type
- Runtime validation (@ and . check)
- Usage example showing type narrowing

**Example**:
```python
if is_email(value):
    # Type checker knows value is str here
    send_email(value)
```

## Exercise 10: Builder Pattern with Self Type (Medium)

Create a QueryBuilder class with method chaining using Self type. Should support select, where, and limit.

**Requirements**:
- All builder methods return Self
- Works with inheritance
- Type-safe method chaining

**Example**:
```python
query = QueryBuilder().select("name").where("age > 18").limit(10)
```

## Exercise 11: Advanced Generic Class (Hard)

Implement a `Cache` class that uses two type parameters: one for keys and one for values. Include get, set, and has methods.

**Requirements**:
- Generic[K, V] where K is hashable
- Type hints for all methods
- Optional default value in get

**Example**:
```python
cache: Cache[str, int] = Cache()
cache.set("count", 42)
```

## Exercise 12: Complex Protocol with Multiple Methods (Hard)

Create a Protocol for database-like objects with connect, execute, and close methods. Write functions using this protocol.

**Requirements**:
- Protocol with 3+ methods
- Different return types
- Function accepting the protocol

**Example**:
```python
def run_query(db: DatabaseProtocol, sql: str) -> List[Dict[str, Any]]: ...
```

## Exercise 13: Literal Types for State Machine (Hard)

Design a state machine using Literal types for states and create a transition function that's type-safe.

**Requirements**:
- State = Literal["idle", "running", "paused", "stopped"]
- Type-safe transitions
- Invalid transitions caught by type checker

**Example**:
```python
def transition(from_state: State, action: Action) -> State: ...
```

## Exercise 14: Variadic Generic Function (Hard)

Create a function that takes multiple arguments of different types and returns a tuple with all types preserved.

**Requirements**:
- Use TypeVarTuple or overloads
- Return type matches input types
- Works with 1-5 arguments

**Example**:
```python
result: Tuple[int, str, float] = pack(1, "hello", 3.14)
```

## Exercise 15: Full Type Coverage with mypy Strict Mode (Hard)

Take an existing untyped module and add complete type hints to pass mypy --strict. Include at least:
- 5 functions with various signatures
- 1 class with generic type
- 1 Protocol
- 1 TypedDict

**Requirements**:
- Zero mypy errors in strict mode
- No use of Any except where necessary
- Complete inline documentation

**Example**:
```python
# Module must pass:
# mypy module.py --strict
```
