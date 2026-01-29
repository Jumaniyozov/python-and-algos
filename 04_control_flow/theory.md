# Control Flow: Theory and Concepts

## 4.1 Conditionals (if, elif, else)

### Basic if Statement

```python
if condition:
    # Execute if condition is True
    pass
```

**Example**:
```python
age = 18

if age >= 18:
    print("Adult")
```

### if-else

```python
if condition:
    # Execute if True
    pass
else:
    # Execute if False
    pass
```

**Example**:
```python
temperature = 25

if temperature > 30:
    print("Hot")
else:
    print("Not hot")
```

### if-elif-else

```python
if condition1:
    pass
elif condition2:
    pass
elif condition3:
    pass
else:
    pass
```

**Example**:
```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
```

### Ternary Operator (Conditional Expression)

**Syntax**: `value_if_true if condition else value_if_false`

```python
# Traditional
if x > 0:
    result = "positive"
else:
    result = "non-positive"

# Ternary (one line)
result = "positive" if x > 0 else "non-positive"

# Nested ternary (less readable, use sparingly)
result = "positive" if x > 0 else "zero" if x == 0 else "negative"
```

### Truthy and Falsy Values

Conditions can be any expression. Falsy values:
- `False`, `None`
- `0`, `0.0`, `0j`
- `""`, `[]`, `()`, `{}`, `set()`

Everything else is truthy.

```python
items = []

if items:
    print("Has items")
else:
    print("Empty")  # This executes

# Explicit is better
if len(items) > 0:
    print("Has items")
```

---

## 4.2 Loops (for, while, else clause)

### for Loop

Iterate over sequences:

```python
# List
for item in [1, 2, 3]:
    print(item)

# String
for char in "hello":
    print(char)

# Range
for i in range(5):  # 0 to 4
    print(i)

# Dictionary
person = {"name": "Alice", "age": 30}
for key in person:
    print(key, person[key])

# Better: items()
for key, value in person.items():
    print(f"{key}: {value}")

# Enumerate (index and value)
for index, value in enumerate(["a", "b", "c"]):
    print(f"{index}: {value}")

# Zip (parallel iteration)
names = ["Alice", "Bob"]
ages = [30, 25]
for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

### while Loop

Execute while condition is true:

```python
count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop (break to exit)
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")
```

### Loop Control: break, continue, pass

**break**: Exit loop entirely

```python
for i in range(10):
    if i == 5:
        break  # Stop loop
    print(i)  # Prints 0, 1, 2, 3, 4
```

**continue**: Skip rest of current iteration

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Prints 1, 3, 5, 7, 9
```

**pass**: Do nothing (placeholder)

```python
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print(i)
```

### else Clause in Loops

The `else` block executes if loop completes normally (not broken):

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed normally")  # Executes

for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed normally")  # Doesn't execute
```

**Use case**: Searching

```python
def find_item(items, target):
    for item in items:
        if item == target:
            print(f"Found: {target}")
            break
    else:
        print(f"Not found: {target}")

find_item([1, 2, 3, 4], 3)  # Found: 3
find_item([1, 2, 3, 4], 10)  # Not found: 10
```

---

## 4.3 Exception Handling

### try-except

Handle errors gracefully:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Multiple Exceptions

```python
try:
    value = int(input("Enter number: "))
    result = 100 / value
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

**Or combine**:
```python
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
```

### try-except-else-finally

```python
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found")
else:
    # Executes if no exception
    print(f"Read {len(data)} characters")
finally:
    # Always executes (cleanup)
    if 'file' in locals():
        file.close()
```

### Catching All Exceptions

```python
try:
    risky_operation()
except Exception as e:
    print(f"Error: {e}")

# Catching everything (not recommended)
except:
    print("Something went wrong")
```

### Raising Exceptions

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b

# Re-raising
try:
    process_data()
except ValueError:
    log_error()
    raise  # Re-raise same exception
```

### Custom Exceptions

```python
class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    return age
```

### Exception Groups (Python 3.11+)

```python
try:
    raise ExceptionGroup("multiple errors", [
        ValueError("bad value"),
        TypeError("bad type")
    ])
except* ValueError as eg:
    print(f"Value errors: {eg}")
except* TypeError as eg:
    print(f"Type errors: {eg}")
```

---

## 4.4 Context Managers and 'with' Statement

### The Problem

```python
# Manual resource management (error-prone)
file = open("data.txt")
data = file.read()
file.close()  # What if error before this?
```

### The Solution: with Statement

```python
with open("data.txt") as file:
    data = file.read()
# File automatically closed, even if error occurs
```

### How It Works

Context managers implement:
- `__enter__()`: Setup (returns resource)
- `__exit__()`: Cleanup (always called)

### Multiple Context Managers

```python
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    data = infile.read()
    outfile.write(data.upper())
```

### Common Uses

```python
# File operations
with open("file.txt") as f:
    data = f.read()

# Locks (threading)
import threading
lock = threading.Lock()
with lock:
    # Critical section
    pass

# Database connections
with db.connection() as conn:
    conn.execute("SELECT * FROM users")

# Suppress exceptions
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove("file.txt")  # No error if file doesn't exist
```

### Creating Context Managers

**Class-based**:
```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False  # Don't suppress exceptions

with FileManager("data.txt") as f:
    data = f.read()
```

**Function-based** (using `contextlib`):
```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename):
    file = open(filename)
    try:
        yield file
    finally:
        file.close()

with file_manager("data.txt") as f:
    data = f.read()
```

---

## 4.5 Pattern Matching (PEP 636 - Python 3.10+)

### Basic match-case

```python
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:  # Default (like 'else')
            return "Unknown"

print(http_status(404))  # "Not Found"
```

### Matching Multiple Values

```python
match status:
    case 200 | 201 | 204:
        return "Success"
    case 400 | 401 | 403:
        return "Client Error"
    case 500 | 502 | 503:
        return "Server Error"
```

### Matching with Conditions (Guards)

```python
match point:
    case (x, y) if x == y:
        print(f"On diagonal: {x}")
    case (x, y):
        print(f"Not on diagonal: ({x}, {y})")
```

### Matching Sequences

```python
match data:
    case []:
        print("Empty list")
    case [x]:
        print(f"Single item: {x}")
    case [x, y]:
        print(f"Two items: {x}, {y}")
    case [first, *rest]:
        print(f"First: {first}, Rest: {rest}")
```

### Matching Dictionaries

```python
match user:
    case {"name": name, "age": age}:
        print(f"{name} is {age} years old")
    case {"name": name}:
        print(f"Name: {name}, age unknown")
```

### Matching Objects/Classes

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

match point:
    case Point(x=0, y=0):
        print("Origin")
    case Point(x=0, y=y):
        print(f"On Y axis at {y}")
    case Point(x=x, y=0):
        print(f"On X axis at {x}")
    case Point(x=x, y=y):
        print(f"At ({x}, {y})")
```

### Capturing Values

```python
match command:
    case ["load", filename]:
        load_file(filename)
    case ["save", filename]:
        save_file(filename)
    case ["delete", *filenames]:
        delete_files(filenames)
    case _:
        print("Unknown command")
```

### Complex Patterns

```python
match event:
    case {"type": "click", "button": "left", "pos": (x, y)}:
        handle_left_click(x, y)
    case {"type": "click", "button": "right", "pos": (x, y)}:
        handle_right_click(x, y)
    case {"type": "keypress", "key": key} if key in ["enter", "return"]:
        handle_enter()
    case {"type": "scroll", "delta": delta}:
        handle_scroll(delta)
```

---

## Key Concepts Summary

1. **Conditionals**: Use `if/elif/else` for decision making
2. **Loops**: `for` for iteration, `while` for condition-based loops
3. **Loop control**: `break`, `continue`, `pass`
4. **else in loops**: Executes if loop completes without break
5. **Exceptions**: Handle errors gracefully with try/except
6. **Context managers**: Use `with` for resource management
7. **Pattern matching**: Modern, powerful alternative to if/elif chains
8. **Truthy/falsy**: Every value has a boolean context
9. **Always cleanup**: Use `finally` or context managers

---

## Best Practices

1. **Use truthy/falsy wisely**: `if items:` vs `if len(items) > 0:`
2. **Prefer pattern matching**: For complex conditionals (Python 3.10+)
3. **Always use context managers**: For files, locks, connections
4. **Be specific with exceptions**: Catch only what you expect
5. **Avoid bare except**: Always specify exception type
6. **Use else in loops**: For search patterns
7. **Keep conditionals simple**: Extract complex logic to functions
8. **Don't suppress errors**: Unless you have good reason

---

## Next Steps

1. Practice all control flow patterns
2. Write error-handling code
3. Use pattern matching for complex logic
4. Master context managers
5. Move on to examples.md
