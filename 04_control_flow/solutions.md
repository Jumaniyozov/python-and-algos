# Control Flow: Exercise Solutions

## Solution 1: Number Classifier

```python
def classify_number(n: int) -> str:
    """Classify a number as positive/negative and even/odd."""
    if n == 0:
        return "zero"

    sign = "positive" if n > 0 else "negative"
    parity = "even" if n % 2 == 0 else "odd"
    return f"{sign} {parity}"

# Tests
print(classify_number(4))   # "positive even"
print(classify_number(-3))  # "negative odd"
print(classify_number(0))   # "zero"
```

## Solution 2: Leap Year

```python
def is_leap_year(year: int) -> bool:
    """Check if year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Tests
print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2024))  # True
```

## Solution 3: Find Duplicates

```python
def find_duplicates(items: list) -> list:
    """Find items appearing more than once."""
    seen = set()
    duplicates = []

    for item in items:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.add(item)

    return duplicates

# Test
print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))  # [2, 3]
```

## Solution 4: Safe Division Calculator

```python
def calculator(a: float, b: float, op: str) -> float | None:
    """Perform arithmetic operations safely."""
    try:
        match op:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                if b == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                return a / b
            case _:
                return None
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None

# Tests
print(calculator(10, 5, "+"))   # 15.0
print(calculator(10, 0, "/"))   # None (with error message)
print(calculator(10, 5, "%"))   # None (invalid operator)
```

## Solution 5: File Line Counter

```python
def count_lines(filename: str) -> int:
    """Count lines in a file."""
    try:
        with open(filename) as f:
            return sum(1 for line in f)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0

# Test
print(count_lines("test.txt"))
```

## Solution 6: Password Validator

```python
def validate_password(password: str) -> tuple[bool, list[str]]:
    """Validate password against security rules."""
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    if not any(c.isupper() for c in password):
        errors.append("Password must contain uppercase letter")

    if not any(c.isdigit() for c in password):
        errors.append("Password must contain digit")

    special_chars = "!@#$%^&*"
    if not any(c in special_chars for c in password):
        errors.append("Password must contain special character")

    return (len(errors) == 0, errors)

# Tests
print(validate_password("Weak"))
# (False, ['Password must be at least 8 characters', ...])
print(validate_password("Strong123!"))
# (True, [])
```

## Solution 7: Pattern Matching Command Parser

```python
def parse_command(command: str) -> str:
    """Parse and execute commands using pattern matching."""
    parts = command.split()

    match parts:
        case ["help"]:
            return "Available commands: help, list, add, remove, clear"
        case ["list"]:
            return "Listing all items..."
        case ["add", item]:
            return f"Adding: {item}"
        case ["add", *items]:
            return f"Adding {len(items)} items"
        case ["remove", item]:
            return f"Removing: {item}"
        case ["clear"]:
            return "Clearing all items"
        case _:
            return "Unknown command. Type 'help' for available commands"

# Tests
commands = ["help", "list", "add book", "add item1 item2", "remove book", "invalid"]
for cmd in commands:
    print(f"{cmd} -> {parse_command(cmd)}")
```

## Solution 8: Fibonacci Generator

```python
def fibonacci(n: int):
    """Generate first n Fibonacci numbers."""
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Test
print(list(fibonacci(10)))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Solution 9: Retry Decorator

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    """Decorator to retry function on failure."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

# Test
@retry(max_attempts=3, delay=0.1)
def unreliable_function(fail_count=[0]):
    fail_count[0] += 1
    if fail_count[0] < 3:
        raise ValueError("Temporary failure")
    return "Success!"

print(unreliable_function())  # Eventually succeeds
```

## Solution 10: Nested Data Navigator

```python
def get_nested(data: dict, path: str, default=None):
    """Safely navigate nested dictionaries."""
    keys = path.split(".")
    current = data

    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default

# Test
data = {
    "user": {
        "profile": {
            "name": "Alice",
            "age": 30
        }
    }
}

print(get_nested(data, "user.profile.name"))    # "Alice"
print(get_nested(data, "user.settings.theme"))  # None
print(get_nested(data, "user.profile.age"))     # 30
```

## Challenge 1: Expression Evaluator

```python
def evaluate_expression(expr: str) -> float:
    """Evaluate simple mathematical expressions."""
    # Remove spaces
    expr = expr.replace(" ", "")

    # Simple recursive descent parser
    def parse_number(s, pos):
        start = pos
        while pos < len(s) and (s[pos].isdigit() or s[pos] == '.'):
            pos += 1
        return float(s[start:pos]), pos

    def parse_term(s, pos):
        left, pos = parse_factor(s, pos)
        while pos < len(s) and s[pos] in "*/":
            op = s[pos]
            pos += 1
            right, pos = parse_factor(s, pos)
            if op == '*':
                left *= right
            else:
                left /= right
        return left, pos

    def parse_factor(s, pos):
        if s[pos] == '(':
            pos += 1
            result, pos = parse_expr(s, pos)
            pos += 1  # Skip ')'
            return result, pos
        return parse_number(s, pos)

    def parse_expr(s, pos):
        left, pos = parse_term(s, pos)
        while pos < len(s) and s[pos] in "+-":
            op = s[pos]
            pos += 1
            right, pos = parse_term(s, pos)
            if op == '+':
                left += right
            else:
                left -= right
        return left, pos

    result, _ = parse_expr(expr, 0)
    return result

# Test
print(evaluate_expression("2 + 3 * 4"))    # 14.0
print(evaluate_expression("(2 + 3) * 4"))  # 20.0
```

## Challenge 2: State Machine

```python
class TrafficLight:
    """Traffic light state machine."""

    def __init__(self):
        self.state = "red"

    def next_state(self):
        """Transition to next state."""
        match self.state:
            case "red":
                self.state = "green"
                return "Go!"
            case "green":
                self.state = "yellow"
                return "Caution!"
            case "yellow":
                self.state = "red"
                return "Stop!"

    def handle_event(self, event):
        """Handle traffic light events."""
        match (self.state, event):
            case ("red", "timer"):
                return self.next_state()
            case ("green", "timer"):
                return self.next_state()
            case ("yellow", "timer"):
                return self.next_state()
            case (_, "emergency"):
                self.state = "red"
                return "Emergency! All stop!"
            case _:
                return f"Invalid event in {self.state} state"

# Test
light = TrafficLight()
print(f"Start: {light.state}")
for _ in range(4):
    msg = light.handle_event("timer")
    print(f"{msg} (now {light.state})")
```

## Challenge 3: Context Manager for Timing

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name="Code block", format="seconds"):
    """Time code execution with different formats."""
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        match format:
            case "seconds":
                print(f"{name}: {elapsed:.4f} seconds")
            case "milliseconds":
                print(f"{name}: {elapsed * 1000:.2f} ms")
            case "formatted":
                if elapsed < 1:
                    print(f"{name}: {elapsed * 1000:.2f} ms")
                elif elapsed < 60:
                    print(f"{name}: {elapsed:.2f} seconds")
                else:
                    mins = int(elapsed // 60)
                    secs = elapsed % 60
                    print(f"{name}: {mins}m {secs:.2f}s")

# Test
with timer("Sum calculation", "milliseconds"):
    total = sum(range(1000000))

with timer("Large sum", "formatted"):
    total = sum(range(10000000))
```

Excellent work! Check examples.md for more patterns.
