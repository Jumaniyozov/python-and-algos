# Basic Syntax and Types: Theory and Concepts

## 2.1 Variables and Assignment

### What is a Variable?

A variable is a name that refers to a value stored in memory. In Python, variables are:
- **Dynamically typed**: Type is determined at runtime
- **Strongly typed**: Cannot perform operations between incompatible types without explicit conversion
- **References**: Variables are references to objects, not containers

### Variable Assignment

```python
x = 42  # Assigns the integer 42 to variable x
```

The `=` operator is the **assignment operator** (not equality!).

### Assignment Semantics

In Python, assignment creates a **reference** to an object:

```python
x = 100
y = x  # y now references the same object as x

# For immutable types (int, str, tuple), this seems like copying
x = 200  # x now references a different object
# y still references 100
```

For mutable types (lists, dicts), this has implications:

```python
list1 = [1, 2, 3]
list2 = list1  # Both reference the SAME list
list1.append(4)
# list2 is now [1, 2, 3, 4] too!
```

### Multiple Assignment

```python
# Assign same value to multiple variables
x = y = z = 0

# Unpack multiple values
a, b, c = 1, 2, 3
# a=1, b=2, c=3

# Swap values
x, y = y, x
```

### Naming Rules

**Valid variable names**:
- Start with letter or underscore: `name`, `_private`, `result2`
- Contain letters, digits, underscores: `my_var_1`
- Case-sensitive: `name` ≠ `Name` ≠ `NAME`

**Invalid**:
```python
2fast = 10  # SyntaxError: can't start with digit
my-var = 5  # SyntaxError: hyphens not allowed
class = "Math"  # SyntaxError: reserved keyword
```

**Conventions** (PEP 8):
- Variables/functions: `snake_case`
- Constants: `UPPER_CASE`
- Classes: `PascalCase`
- Private: `_leading_underscore`

---

## 2.2 Numbers

Python has several numeric types.

### Integers (int)

Arbitrary precision integers - can be as large as memory allows:

```python
small = 42
large = 123456789012345678901234567890
negative = -100

# Underscores for readability (Python 3.6+)
million = 1_000_000
binary = 0b1010  # Binary: 10
octal = 0o12     # Octal: 10
hex_num = 0xFF   # Hexadecimal: 255
```

**Operations**:
```python
a + b      # Addition
a - b      # Subtraction
a * b      # Multiplication
a / b      # Division (always returns float)
a // b     # Floor division (integer division)
a % b      # Modulo (remainder)
a ** b     # Exponentiation
abs(a)     # Absolute value
pow(a, b)  # Same as a ** b
```

### Floating Point (float)

Double-precision floating point numbers:

```python
pi = 3.14159
scientific = 1.23e-4  # 0.000123
negative = -0.001
```

**Precision Issues**:
```python
>>> 0.1 + 0.2
0.30000000000000004  # Floating point representation issue
```

This is not a Python bug - it's how computers represent decimals in binary!

**Operations**: Same as integers, plus:
```python
round(x, n)      # Round to n decimal places
math.floor(x)    # Round down
math.ceil(x)     # Round up
math.trunc(x)    # Truncate to integer
```

### Complex Numbers (complex)

Built-in support for complex numbers:

```python
z = 3 + 4j  # or complex(3, 4)
# j or J represents imaginary unit (√-1)

z.real  # 3.0
z.imag  # 4.0
abs(z)  # Magnitude: 5.0
```

**Operations**:
```python
z1 = 1 + 2j
z2 = 3 + 4j
z1 + z2  # (4+6j)
z1 * z2  # (-5+10j)
z1.conjugate()  # (1-2j)
```

### Decimal (from decimal module)

For precise decimal arithmetic:

```python
from decimal import Decimal

# Avoiding float precision issues
price = Decimal('0.1')
quantity = Decimal('0.2')
total = price + quantity  # Decimal('0.3') - exact!

# vs float
0.1 + 0.2  # 0.30000000000000004
```

**When to use**:
- Financial calculations
- When exact decimal representation is required
- Scientific calculations needing specific precision

**Configuration**:
```python
from decimal import Decimal, getcontext

getcontext().prec = 50  # Set precision to 50 digits
Decimal(1) / Decimal(7)  # Very precise result
```

### Fraction (from fractions module)

For rational number arithmetic:

```python
from fractions import Fraction

# Create from integers
f1 = Fraction(3, 4)  # 3/4

# Create from decimal
f2 = Fraction('0.25')  # 1/4

# Arithmetic
f1 + f2  # Fraction(1, 1) = 1
f1 * 2   # Fraction(3, 2) = 1.5

# Automatic simplification
Fraction(6, 8)  # Fraction(3, 4)
```

**When to use**:
- Mathematical proofs
- Educational purposes
- When you need exact rational representation

### Type Conversion

```python
int(3.7)       # 3 (truncates)
int("42")      # 42
float(42)      # 42.0
float("3.14")  # 3.14
complex(2)     # (2+0j)
str(42)        # "42"

# Be careful!
int("3.14")    # ValueError: invalid literal for int()
int(float("3.14"))  # 3 (works)
```

---

## 2.3 Strings and String Formatting

### String Basics

Strings are **immutable** sequences of Unicode characters:

```python
# Single or double quotes (equivalent)
single = 'Hello'
double = "World"

# Triple quotes for multiline
multiline = """This is
a multiline
string"""

# Raw strings (no escape sequences)
path = r"C:\Users\name"  # r prefix

# Unicode
emoji = "😀"
chinese = "你好"
```

### String Operations

```python
# Concatenation
"Hello" + " " + "World"  # "Hello World"

# Repetition
"Ha" * 3  # "HaHaHa"

# Indexing (0-based)
text = "Python"
text[0]   # 'P'
text[-1]  # 'n' (last character)

# Slicing
text[0:2]   # 'Py'
text[2:]    # 'thon'
text[:4]    # 'Pyth'
text[::2]   # 'Pto' (every 2nd character)
text[::-1]  # 'nohtyP' (reverse)

# Length
len(text)  # 6

# Membership
'th' in text  # True
'x' in text   # False
```

### String Methods

Strings have many useful methods (all return new strings - strings are immutable!):

```python
text = "  Hello, World!  "

# Case conversion
text.upper()      # "  HELLO, WORLD!  "
text.lower()      # "  hello, world!  "
text.capitalize() # "  hello, world!  "
text.title()      # "  Hello, World!  "
text.swapcase()   # "  hELLO, wORLD!  "

# Whitespace
text.strip()      # "Hello, World!" (remove leading/trailing)
text.lstrip()     # "Hello, World!  " (left strip)
text.rstrip()     # "  Hello, World!" (right strip)

# Searching
text.find("World")      # 9 (index of first occurrence)
text.find("xyz")        # -1 (not found)
text.index("World")     # 9 (like find, but raises ValueError if not found)
text.count("l")         # 3
text.startswith("  H")  # True
text.endswith("!  ")    # True

# Replacement
text.replace("World", "Python")  # "  Hello, Python!  "

# Splitting and joining
words = "a,b,c".split(",")  # ['a', 'b', 'c']
"-".join(words)             # "a-b-c"

# Checking
"123".isdigit()    # True
"abc".isalpha()    # True
"abc123".isalnum() # True
"   ".isspace()    # True
```

### String Formatting

#### 1. f-strings (Python 3.6+, Recommended)

```python
name = "Alice"
age = 30

# Basic
f"Hello, {name}!"  # "Hello, Alice!"

# Expressions
f"{name} is {age} years old"  # "Alice is 30 years old"
f"Next year: {age + 1}"       # "Next year: 31"

# Format specifiers
pi = 3.14159
f"{pi:.2f}"      # "3.14" (2 decimal places)
f"{pi:.4f}"      # "3.1416"
f"{1000:,}"      # "1,000" (thousands separator)
f"{42:05d}"      # "00042" (zero-padded to 5 digits)
f"{0.5:.1%}"     # "50.0%" (percentage)

# Alignment
f"{name:<10}"    # "Alice     " (left-align in 10 chars)
f"{name:>10}"    # "     Alice" (right-align)
f"{name:^10}"    # "  Alice   " (center)

# Debug (Python 3.8+)
x = 42
f"{x=}"  # "x=42" (shows variable name and value)
```

#### 2. str.format() (Older style)

```python
"Hello, {}!".format(name)
"Hello, {0}! Age: {1}".format(name, age)
"Hello, {name}! Age: {age}".format(name=name, age=age)

# Format specifiers work similarly
"{:.2f}".format(pi)
```

#### 3. %-formatting (Legacy, avoid)

```python
"Hello, %s! Age: %d" % (name, age)
# Works but outdated - use f-strings instead
```

### String Escape Sequences

```python
"\n"   # Newline
"\t"   # Tab
"\\"   # Backslash
"\'"   # Single quote
"\""   # Double quote
"\uXXXX"  # Unicode character

print("Line 1\nLine 2")
# Line 1
# Line 2

# Raw strings ignore escapes
print(r"C:\new\test")  # C:\new\test (not C:<newline>ew	est)
```

---

## 2.4 Booleans and None

### Boolean Type (bool)

Only two values: `True` and `False` (capitalized!)

```python
is_valid = True
is_empty = False

# Boolean operators
True and False   # False
True or False    # True
not True         # False

# Comparison operators return bool
5 > 3           # True
5 == 5          # True
5 != 3          # True
"a" < "b"       # True (lexicographic)
```

### Truthiness

In Python, every value has a truth value:

**Falsy values** (evaluate to False):
- `False`
- `None`
- `0`, `0.0`, `0j`
- Empty sequences: `""`, `[]`, `()`, `{}`
- Empty collections: `set()`, `dict()`

**Everything else is truthy** (evaluates to True):
- `True`
- Non-zero numbers: `1`, `-1`, `3.14`
- Non-empty sequences: `"text"`, `[1, 2]`, `(1,)`
- Non-empty collections: `{1, 2}`, `{'a': 1}`

```python
if "":
    print("This won't print")  # Empty string is falsy

if "text":
    print("This will print")   # Non-empty string is truthy

# Practical use
def process_data(data):
    if not data:  # Checks if data is falsy (None, empty, etc.)
        return "No data"
    # Process data...
```

### None Type

`None` is Python's null value - represents absence of value:

```python
result = None

# Check for None
if result is None:
    print("No result")

# DON'T use ==
if result == None:  # Works but not idiomatic
    print("No result")

# Use 'is'
if result is None:  # Correct
    print("No result")
```

**When to use None**:
- Default function return value
- Sentinel value for "no data"
- Default parameter values

```python
def find_item(items, target):
    for item in items:
        if item == target:
            return item
    return None  # Not found

result = find_item([1, 2, 3], 5)
if result is None:
    print("Not found")
```

---

## 2.5 Type Hints and Annotations

Type hints are optional type information for variables and functions. They don't affect runtime behavior but help with:
- Code documentation
- IDE autocompletion
- Static type checking (mypy, pyright)
- Catching bugs before runtime

### Basic Type Hints

```python
# Variable annotations
name: str = "Alice"
age: int = 30
height: float = 5.6
is_student: bool = True

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def process() -> None:  # Returns nothing
    print("Processing...")
```

### Built-in Generic Types (Python 3.9+)

Before Python 3.9, you needed `from typing import List, Dict, etc.`

**Python 3.9+ (preferred)**:
```python
# Lists
numbers: list[int] = [1, 2, 3]
names: list[str] = ["Alice", "Bob"]

# Dictionaries
scores: dict[str, int] = {"Alice": 95, "Bob": 87}

# Tuples
point: tuple[int, int] = (10, 20)
person: tuple[str, int, float] = ("Alice", 30, 5.6)

# Sets
tags: set[str] = {"python", "coding"}

# Optional (can be value or None)
from typing import Optional
result: Optional[int] = None  # Can be int or None
# Or in Python 3.10+:
result: int | None = None
```

### Union Types

**Python 3.10+** (PEP 604):
```python
# Old way (still works)
from typing import Union
value: Union[int, str] = 42

# New way (Python 3.10+)
value: int | str = 42  # Can be int OR str
value = "text"  # Also valid

def process(data: int | str | None) -> str:
    if isinstance(data, int):
        return f"Number: {data}"
    elif isinstance(data, str):
        return f"Text: {data}"
    else:
        return "No data"
```

### Type Parameters (Python 3.12+, Enhanced in 3.14)

**PEP 695 - New syntax**:

```python
# Generic function
def first[T](items: list[T]) -> T:
    return items[0]

# Works with any type
first([1, 2, 3])          # Returns int
first(["a", "b", "c"])    # Returns str

# Generic class
class Box[T]:
    def __init__(self, item: T):
        self.item = item

    def get(self) -> T:
        return self.item

int_box = Box(42)
str_box = Box("hello")

# Multiple type parameters
def pair[T, U](first: T, second: U) -> tuple[T, U]:
    return (first, second)

pair(1, "one")  # tuple[int, str]
```

### Common Type Hints

```python
from typing import Any, Callable, Sequence

# Any - any type (avoid when possible)
def process(data: Any) -> Any:
    return data

# Callable - function type
def apply(func: Callable[[int], int], x: int) -> int:
    return func(x)

# Sequence - list, tuple, etc.
def sum_all(items: Sequence[int]) -> int:
    return sum(items)

sum_all([1, 2, 3])   # OK
sum_all((1, 2, 3))   # OK
```

### Type Aliases

```python
# Simple alias
UserId = int
UserName = str

def get_user(user_id: UserId) -> UserName:
    return f"user_{user_id}"

# Complex alias
Point = tuple[int, int]
Line = list[Point]

def draw_line(line: Line) -> None:
    for point in line:
        print(point)

# Python 3.12+ type alias syntax
type Point = tuple[int, int]
type Line = list[Point]
```

### TypedDict (for dictionary structure)

```python
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

person: Person = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}

# Type checker will catch missing or wrong keys
```

### Literal Types

```python
from typing import Literal

def set_mode(mode: Literal["read", "write", "append"]) -> None:
    print(f"Mode: {mode}")

set_mode("read")   # OK
set_mode("delete") # Type error!
```

### When to Use Type Hints

**Use type hints when**:
- Writing libraries or APIs
- Working in large codebases
- Want IDE autocompletion
- Using static type checkers (mypy)

**Skip type hints when**:
- Quick scripts or prototypes
- Types are obvious from context
- Over-typing makes code harder to read

---

## Key Concepts Summary

1. **Variables are references**: Assignment creates references to objects
2. **Dynamic typing**: Type determined at runtime
3. **Strong typing**: No implicit type coercion (can't add int + str)
4. **Multiple numeric types**: int, float, complex, Decimal, Fraction
5. **Strings are immutable**: Operations create new strings
6. **f-strings are preferred**: Modern, readable string formatting
7. **Truthiness matters**: Every value has a truth value
8. **None is special**: Use `is None`, not `== None`
9. **Type hints are optional**: But very useful for documentation and tooling
10. **Python 3.14**: Enhanced type parameter syntax with `[T]`

---

## Next Steps

1. Practice variable assignment and manipulation
2. Experiment with different numeric types
3. Master string formatting with f-strings
4. Add type hints to your functions
5. Move on to examples.md for hands-on practice
