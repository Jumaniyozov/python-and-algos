# Control Flow: Code Examples

## Example 1: Grade Calculator

```python
def get_grade(score):
    """Calculate letter grade from numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test
for score in [95, 82, 74, 65, 50]:
    print(f"Score {score}: Grade {get_grade(score)}")
```

## Example 2: FizzBuzz with Loops

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

## Example 3: Search with Loop Else

```python
def find_prime(n):
    """Find first prime >= n."""
    current = n
    while True:
        for divisor in range(2, int(current ** 0.5) + 1):
            if current % divisor == 0:
                break
        else:
            return current  # Found prime (loop completed)
        current += 1

print(find_prime(100))  # 101
```

## Example 4: Exception Handling

```python
def safe_divide(a, b):
    """Safely divide two numbers."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid types for division")
        return None
    else:
        print(f"Division successful: {result}")
        return result
    finally:
        print("Division attempt completed")

safe_divide(10, 2)   # Success
safe_divide(10, 0)   # ZeroDivisionError
safe_divide(10, "2") # TypeError
```

## Example 5: File Operations with Context Manager

```python
# Safe file writing
def write_data(filename, data):
    try:
        with open(filename, 'w') as f:
            f.write(data)
        print(f"Data written to {filename}")
    except IOError as e:
        print(f"Error writing file: {e}")

# Multiple files
def copy_file(source, dest):
    with open(source) as infile, open(dest, 'w') as outfile:
        outfile.write(infile.read())
```

## Example 6: Pattern Matching (Python 3.10+)

```python
def process_command(command):
    """Process user commands using pattern matching."""
    match command.split():
        case ["quit"] | ["exit"]:
            return "Goodbye!"
        case ["help"]:
            return "Available commands: quit, help, load, save"
        case ["load", filename]:
            return f"Loading {filename}"
        case ["save", filename]:
            return f"Saving to {filename}"
        case ["delete", *filenames]:
            return f"Deleting {len(filenames)} files"
        case _:
            return "Unknown command"

# Test
commands = ["quit", "help", "load test.txt", "delete a.txt b.txt"]
for cmd in commands:
    print(f"{cmd} -> {process_command(cmd)}")
```

## Example 7: Advanced Pattern Matching

```python
def describe_point(point):
    """Describe a point using pattern matching."""
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"On Y-axis at y={y}"
        case (x, 0):
            return f"On X-axis at x={x}"
        case (x, y) if x == y:
            return f"On diagonal y=x at ({x}, {y})"
        case (x, y) if x == -y:
            return f"On diagonal y=-x at ({x}, {y})"
        case (x, y):
            return f"Point at ({x}, {y})"

# Test
points = [(0, 0), (0, 5), (5, 0), (3, 3), (3, -3), (4, 7)]
for p in points:
    print(f"{p}: {describe_point(p)}")
```

## Example 8: List Comprehension with Conditionals

```python
# Filter with if
evens = [x for x in range(20) if x % 2 == 0]

# Transform with if-else
signs = ["positive" if x > 0 else "negative" if x < 0 else "zero"
         for x in [-5, -2, 0, 3, 7]]

# Nested with conditions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_evens = [num for row in matrix for num in row if num % 2 == 0]
print(flattened_evens)  # [2, 4, 6, 8]
```

## Example 9: Custom Context Manager

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name):
    """Context manager to time code execution."""
    start = time.time()
    print(f"Starting {name}...")
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name} took {elapsed:.2f} seconds")

# Usage
with timer("Data processing"):
    total = sum(range(1000000))
    print(f"Sum: {total}")
```

## Example 10: Real-World Validation

```python
def validate_user_input(data):
    """Validate user registration data."""
    errors = []

    # Check required fields
    required = ["username", "email", "password"]
    for field in required:
        if field not in data or not data[field]:
            errors.append(f"Missing {field}")

    if errors:
        return False, errors

    # Validate username
    username = data["username"]
    if len(username) < 3:
        errors.append("Username too short")
    elif len(username) > 20:
        errors.append("Username too long")

    # Validate email
    email = data["email"]
    if "@" not in email or "." not in email:
        errors.append("Invalid email format")

    # Validate password
    password = data["password"]
    if len(password) < 8:
        errors.append("Password too short")
    elif not any(c.isupper() for c in password):
        errors.append("Password needs uppercase letter")
    elif not any(c.isdigit() for c in password):
        errors.append("Password needs digit")

    if errors:
        return False, errors
    return True, []

# Test
test_data = {
    "username": "alice",
    "email": "alice@example.com",
    "password": "Secret123"
}

valid, errors = validate_user_input(test_data)
if valid:
    print("Valid user data")
else:
    print("Errors:", errors)
```

See solutions.md for more practical examples and exercises.
