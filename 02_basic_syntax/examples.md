# Basic Syntax and Types: Code Examples

## Example 1: Variable Assignment and References

```python
# Simple assignment
x = 10
y = 20
print(f"x = {x}, y = {y}")

# Multiple assignment
a = b = c = 0
print(f"a = {a}, b = {b}, c = {c}")

# Tuple unpacking
p, q, r = 1, 2, 3
print(f"p = {p}, q = {q}, r = {r}")

# Swapping values
x, y = y, x
print(f"After swap: x = {x}, y = {y}")

# References demonstration
list1 = [1, 2, 3]
list2 = list1  # Both reference same list
list1.append(4)
print(f"list1: {list1}")  # [1, 2, 3, 4]
print(f"list2: {list2}")  # [1, 2, 3, 4] - same!

# To create a copy
list3 = list1.copy()  # or list1[:]
list1.append(5)
print(f"list1: {list1}")  # [1, 2, 3, 4, 5]
print(f"list3: {list3}")  # [1, 2, 3, 4] - unchanged
```

Output:
```
x = 10, y = 20
a = 0, b = 0, c = 0
p = 1, q = 2, r = 3
After swap: x = 20, y = 10
list1: [1, 2, 3, 4]
list2: [1, 2, 3, 4]
list1: [1, 2, 3, 4, 5]
list3: [1, 2, 3, 4]
```

---

## Example 2: Integer Operations

```python
# Basic arithmetic
a = 15
b = 4

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")  # Always returns float
print(f"Floor division: {a} // {b} = {a // b}")  # Integer result
print(f"Modulo: {a} % {b} = {a % b}")  # Remainder
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Large integers (unlimited precision)
huge = 123456789 ** 10
print(f"\nHuge number: {huge}")
print(f"Length: {len(str(huge))} digits")

# Different number bases
binary = 0b1010  # Binary
octal = 0o12     # Octal
hexadec = 0xFF   # Hexadecimal

print(f"\nBinary 0b1010 = {binary}")
print(f"Octal 0o12 = {octal}")
print(f"Hex 0xFF = {hexadec}")

# Convert to different bases
number = 42
print(f"\n{number} in binary: {bin(number)}")
print(f"{number} in octal: {oct(number)}")
print(f"{number} in hex: {hex(number)}")

# Readable numbers with underscores
million = 1_000_000
print(f"\nOne million: {million:,}")
```

---

## Example 3: Floating Point and Precision

```python
# Float basics
pi = 3.14159
scientific = 1.23e-4  # 0.000123

print(f"Pi: {pi}")
print(f"Scientific notation: {scientific}")

# Precision issues
result = 0.1 + 0.2
print(f"\n0.1 + 0.2 = {result}")  # 0.30000000000000004
print(f"Expected 0.3? {result == 0.3}")  # False!

# Solution 1: Round for comparison
print(f"Rounded: {round(result, 1) == 0.3}")  # True

# Solution 2: Use Decimal for exact arithmetic
from decimal import Decimal

d1 = Decimal('0.1')
d2 = Decimal('0.2')
d_result = d1 + d2
print(f"\nDecimal: {d_result}")  # Exactly 0.3
print(f"Equals 0.3? {d_result == Decimal('0.3')}")  # True

# Rounding
value = 3.14159
print(f"\nOriginal: {value}")
print(f"Round to 2 decimals: {round(value, 2)}")
print(f"Round to 0 decimals: {round(value)}")

import math
print(f"Floor: {math.floor(value)}")
print(f"Ceil: {math.ceil(value)}")
```

---

## Example 4: Complex Numbers

```python
# Creating complex numbers
z1 = 3 + 4j
z2 = complex(1, 2)

print(f"z1 = {z1}")
print(f"z2 = {z2}")

# Real and imaginary parts
print(f"\nz1 real part: {z1.real}")
print(f"z1 imaginary part: {z1.imag}")

# Magnitude (absolute value)
print(f"Magnitude of {z1}: {abs(z1)}")

# Conjugate
print(f"Conjugate of {z1}: {z1.conjugate()}")

# Arithmetic
print(f"\n{z1} + {z2} = {z1 + z2}")
print(f"{z1} - {z2} = {z1 - z2}")
print(f"{z1} * {z2} = {z1 * z2}")
print(f"{z1} / {z2} = {z1 / z2}")
```

---

## Example 5: Fractions for Exact Arithmetic

```python
from fractions import Fraction

# Create fractions
f1 = Fraction(3, 4)  # 3/4
f2 = Fraction(1, 2)  # 1/2
f3 = Fraction('0.25')  # From string

print(f"f1 = {f1}")
print(f"f2 = {f2}")
print(f"f3 = {f3}")

# Arithmetic
print(f"\n{f1} + {f2} = {f1 + f2}")
print(f"{f1} - {f2} = {f1 - f2}")
print(f"{f1} * {f2} = {f1 * f2}")
print(f"{f1} / {f2} = {f1 / f2}")

# Automatic simplification
f4 = Fraction(6, 8)
print(f"\nFraction(6, 8) simplified: {f4}")  # 3/4

# Convert to float
print(f"As float: {float(f1)}")

# Practical example: recipe scaling
recipe_flour = Fraction(2, 3)  # cups
scaling_factor = Fraction(3, 2)  # 1.5x recipe
new_flour = recipe_flour * scaling_factor
print(f"\nOriginal flour: {recipe_flour} cups")
print(f"Scaled (1.5x): {new_flour} cup = {float(new_flour)}")
```

---

## Example 6: String Operations

```python
# Creating strings
text = "Python Programming"
single = 'Single quotes'
triple = """
Multiple
lines
of text
"""

print(text)
print(single)
print(triple)

# Indexing and slicing
print(f"\nFirst character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"First 6 characters: {text[0:6]}")
print(f"Every 2nd character: {text[::2]}")
print(f"Reversed: {text[::-1]}")

# String methods
print(f"\nUppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")

# Searching
print(f"\nFind 'Pro': {text.find('Pro')}")
print(f"Count 'm': {text.count('m')}")
print(f"Starts with 'Python': {text.startswith('Python')}")
print(f"Ends with 'ing': {text.endswith('ing')}")

# Splitting and joining
words = text.split()
print(f"\nWords: {words}")
print(f"Joined with '-': {'-'.join(words)}")

# Stripping whitespace
messy = "  hello world  "
print(f"Original: '{messy}'")
print(f"Stripped: '{messy.strip()}'")

# Replacing
modified = text.replace("Python", "Java")
print(f"\nModified: {modified}")
```

---

## Example 7: String Formatting (f-strings)

```python
name = "Alice"
age = 30
pi = 3.14159
amount = 1234.56

# Basic formatting
print(f"Name: {name}")
print(f"Age: {age}")

# Expressions
print(f"Next year: {age + 1}")
print(f"Uppercase: {name.upper()}")

# Format specifiers
print(f"\n--- Number Formatting ---")
print(f"Pi (2 decimals): {pi:.2f}")
print(f"Pi (4 decimals): {pi:.4f}")
print(f"Amount with comma: ${amount:,.2f}")
print(f"Zero-padded: {age:05d}")
print(f"Percentage: {0.75:.1%}")
print(f"Scientific: {1234567:.2e}")

# Alignment
print(f"\n--- Alignment ---")
print(f"Left: '{name:<15}'")
print(f"Right: '{name:>15}'")
print(f"Center: '{name:^15}'")
print(f"Fill: '{name:*^15}'")

# Width from variable
width = 20
print(f"\nDynamic width: '{name:{width}}'")

# Debug syntax (Python 3.8+)
x = 42
y = 100
print(f"\n{x=}, {y=}")  # Shows variable names and values
print(f"{x + y=}")

# Nested formatting
value = 123.456
precision = 2
print(f"\nValue: {value:.{precision}f}")

# Datetime formatting
from datetime import datetime
now = datetime.now()
print(f"\nDate: {now:%Y-%m-%d}")
print(f"Time: {now:%H:%M:%S}")
print(f"Full: {now:%Y-%m-%d %H:%M:%S}")
```

---

## Example 8: Type Conversion

```python
# String to number
str_int = "42"
str_float = "3.14"

num_int = int(str_int)
num_float = float(str_float)

print(f"String '{str_int}' to int: {num_int}")
print(f"String '{str_float}' to float: {num_float}")

# Number to string
x = 100
y = 3.14
str_x = str(x)
str_y = str(y)

print(f"\nInt {x} to string: '{str_x}'")
print(f"Float {y} to string: '{str_y}'")

# Float to int (truncates)
f = 3.7
i = int(f)
print(f"\nFloat {f} to int: {i}")

# Int to float
num = 42
flt = float(num)
print(f"Int {num} to float: {flt}")

# Bool to int/string
true_val = True
false_val = False
print(f"\nTrue as int: {int(true_val)}")  # 1
print(f"False as int: {int(false_val)}")  # 0

# Checking types
print(f"\nType of {num_int}: {type(num_int)}")
print(f"Type of {num_float}: {type(num_float)}")
print(f"Is {num_int} an int? {isinstance(num_int, int)}")

# Error handling
try:
    bad = int("not a number")
except ValueError as e:
    print(f"\nError converting: {e}")
```

---

## Example 9: Boolean and Truthiness

```python
# Boolean values
is_valid = True
is_empty = False

print(f"is_valid: {is_valid}")
print(f"is_empty: {is_empty}")

# Boolean operations
print(f"\nTrue and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# Comparisons
x = 5
y = 10

print(f"\n{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} <= {y}: {x <= y}")
print(f"{x} >= {y}: {x >= y}")

# Truthiness - falsy values
print("\n--- Truthiness Tests ---")
values = [0, 0.0, "", [], {}, None, False]
for val in values:
    print(f"{repr(val):10} is {'truthy' if val else 'falsy'}")

# Truthiness - truthy values
print()
values = [1, -1, "text", [1], {"a": 1}, True]
for val in values:
    print(f"{repr(val):10} is {'truthy' if val else 'falsy'}")

# Practical usage
def process_data(data):
    if not data:  # Checks if falsy (None, empty, 0, etc.)
        return "No data to process"
    return f"Processing {len(data)} items"

print(f"\nEmpty list: {process_data([])}")
print(f"With data: {process_data([1, 2, 3])}")
```

---

## Example 10: None Type

```python
# None represents absence of value
result = None
name = None

print(f"result: {result}")
print(f"name: {name}")

# Checking for None (use 'is', not '==')
if result is None:
    print("Result is None")

if name is None:
    print("Name is None")

# Function returning None
def find_user(user_id):
    # Simulating database lookup
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # Returns None if not found

user = find_user(1)
if user is not None:
    print(f"\nFound user: {user}")

user = find_user(999)
if user is None:
    print("User not found")

# Default parameter with None
def greet(name=None):
    if name is None:
        return "Hello, stranger!"
    return f"Hello, {name}!"

print(f"\n{greet()}")
print(f"{greet('Alice')}")

# None vs empty
empty_list = []
none_list = None

print(f"\nEmpty list is None? {empty_list is None}")  # False
print(f"None list is None? {none_list is None}")      # True
print(f"Empty list is falsy? {not empty_list}")       # True
print(f"None is falsy? {not none_list}")              # True
```

---

## Example 11: Type Hints

```python
# Function with type hints
def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def divide(a: float, b: float) -> float | None:
    """Divide two numbers, return None if division by zero."""
    if b == 0:
        return None
    return a / b

# Using the functions
message = greet("Alice")
print(message)

sum_result = add(5, 3)
print(f"5 + 3 = {sum_result}")

div_result = divide(10.0, 2.0)
print(f"10 / 2 = {div_result}")

div_result = divide(10.0, 0.0)
print(f"10 / 0 = {div_result}")

# Variable annotations
age: int = 30
name: str = "Bob"
scores: list[int] = [95, 87, 92]
person: dict[str, str | int] = {"name": "Alice", "age": 30}

print(f"\nAge: {age}")
print(f"Name: {name}")
print(f"Scores: {scores}")
print(f"Person: {person}")

# Generic function (Python 3.14 syntax)
def first[T](items: list[T]) -> T:
    """Return first item from list."""
    return items[0]

print(f"\nFirst number: {first([1, 2, 3])}")
print(f"First word: {first(['apple', 'banana'])}")

# Generic class
class Box[T]:
    """A box that can hold any type."""
    def __init__(self, item: T):
        self.item = item

    def get(self) -> T:
        return self.item

    def __repr__(self) -> str:
        return f"Box({self.item!r})"

int_box = Box(42)
str_box = Box("hello")

print(f"\nInteger box: {int_box}")
print(f"String box: {str_box}")
print(f"Get from box: {int_box.get()}")
```

---

## Example 12: Practical Mini-Programs

### Temperature Converter

```python
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

# Test
temps_c = [0, 20, 37, 100]
for c in temps_c:
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C = {f:.1f}°F")

print()

temps_f = [32, 68, 98.6, 212]
for f in temps_f:
    c = fahrenheit_to_celsius(f)
    print(f"{f}°F = {c:.1f}°C")
```

### Calculator

```python
def calculate(a: float, b: float, operation: str) -> float | None:
    """Perform basic arithmetic operations."""
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b if b != 0 else None
        case "**":
            return a ** b
        case _:
            return None

# Test
operations = ["+", "-", "*", "/", "**"]
a, b = 10, 3

for op in operations:
    result = calculate(a, b, op)
    if result is not None:
        print(f"{a} {op} {b} = {result}")
    else:
        print(f"{a} {op} {b} = Error")
```

### String Analyzer

```python
def analyze_string(text: str) -> dict[str, int]:
    """Analyze a string and return statistics."""
    return {
        "length": len(text),
        "words": len(text.split()),
        "uppercase": sum(1 for c in text if c.isupper()),
        "lowercase": sum(1 for c in text if c.islower()),
        "digits": sum(1 for c in text if c.isdigit()),
        "spaces": sum(1 for c in text if c.isspace()),
    }

# Test
sample = "Hello World! Python 3.14 is Great!"
stats = analyze_string(sample)

print(f"Text: {sample}")
print("\nStatistics:")
for key, value in stats.items():
    print(f"  {key.capitalize()}: {value}")
```

---

## Key Takeaways from Examples

1. **Variables are flexible**: Dynamic typing allows reassignment to different types
2. **Numeric types have distinct uses**: int for whole numbers, float for decimals, Decimal for precision
3. **Strings are powerful**: Rich set of methods for manipulation
4. **f-strings are best**: Most readable and flexible formatting
5. **Truthiness is useful**: Simplifies conditional logic
6. **None is meaningful**: Represents intentional absence
7. **Type hints improve code**: Better documentation and tool support
8. **Python 3.14 generics**: Clean syntax with `[T]` for generic types

Try modifying these examples and experimenting with different values!
