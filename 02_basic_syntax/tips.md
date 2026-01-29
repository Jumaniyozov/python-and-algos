# Basic Syntax and Types: Tips, Tricks, and Gotchas

## Variable Assignment Tips

### Tip 1: Use Meaningful Names

**Bad**:
```python
x = 100
y = 0.08
z = x * y
```

**Good**:
```python
principal = 100
interest_rate = 0.08
interest = principal * interest_rate
```

### Tip 2: Multiple Assignment for Related Values

```python
# Good for initialization
x = y = z = 0

# Good for swapping
a, b = b, a

# Good for unpacking
name, age, city = get_user_data()

# But don't overuse
x = y = z = []  # Dangerous! All reference same list
```

### Tip 3: Use _ for Throwaway Variables

```python
# When you don't need all values
first, _, last = "John Middle Doe".split()
# first = "John", last = "Doe", ignore middle

# In loops when you don't use the value
for _ in range(10):
    print("Hello")

# Multiple throwaway values with *_
first, *_, last = [1, 2, 3, 4, 5]
# first = 1, last = 5, ignore middle values
```

---

## Numeric Type Tips

### Tip 1: Integer Division Gotcha

```python
# Python 3: / always returns float
5 / 2  # 2.5

# Use // for integer division
5 // 2  # 2

# This changed from Python 2!
# Python 2: 5 / 2 was 2 (int)
```

### Tip 2: Use Underscores in Large Numbers

```python
# Hard to read
population = 7900000000

# Easy to read
population = 7_900_000_000

# Also works with binary, hex, etc.
flags = 0b_1111_0000
address = 0xFF_FF_00_00
```

### Tip 3: Float Comparison Issues

**Wrong**:
```python
0.1 + 0.2 == 0.3  # False! (floating point precision)
```

**Right**:
```python
import math

# Use isclose for float comparison
math.isclose(0.1 + 0.2, 0.3)  # True

# Or round for comparison
round(0.1 + 0.2, 10) == round(0.3, 10)  # True

# Or use Decimal for exact arithmetic
from decimal import Decimal
Decimal('0.1') + Decimal('0.2') == Decimal('0.3')  # True
```

### Tip 4: When to Use Which Numeric Type

| Type | Use Case | Example |
|------|----------|---------|
| `int` | Counting, indexing, whole numbers | `count = 42` |
| `float` | Measurements, scientific calculations | `temperature = 98.6` |
| `Decimal` | Financial calculations, exact decimals | `price = Decimal('19.99')` |
| `Fraction` | Mathematical ratios, teaching | `ratio = Fraction(2, 3)` |
| `complex` | Engineering, physics calculations | `z = 3 + 4j` |

### Tip 5: Division by Zero

```python
# int/float division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    result = None

# Better: check before dividing
denominator = 0
result = numerator / denominator if denominator != 0 else None

# Or use exception handling for clearer intent
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

---

## String Tips

### Tip 1: Use f-strings (Python 3.6+)

**Avoid** (old % formatting):
```python
name = "Alice"
age = 30
msg = "Hello, %s! You are %d years old." % (name, age)
```

**Avoid** (.format() is okay but verbose):
```python
msg = "Hello, {}! You are {} years old.".format(name, age)
```

**Prefer** (f-strings):
```python
msg = f"Hello, {name}! You are {age} years old."
```

### Tip 2: String Immutability

Strings can't be modified in place:

**Wrong**:
```python
text = "hello"
text[0] = "H"  # TypeError!
```

**Right**:
```python
text = "hello"
text = "H" + text[1:]  # Create new string
# or
text = text.capitalize()
```

### Tip 3: Use join() for Concatenation in Loops

**Slow** (creates new string each iteration):
```python
result = ""
for word in words:
    result += word + " "
```

**Fast** (single join operation):
```python
result = " ".join(words)
```

### Tip 4: Raw Strings for File Paths and Regex

```python
# Regular string (need to escape backslashes)
path = "C:\\Users\\name\\Documents"

# Raw string (no escaping needed)
path = r"C:\Users\name\Documents"

# Regex patterns
import re
pattern = r"\d{3}-\d{2}-\d{4}"  # SSN pattern
```

### Tip 5: Multiline Strings

```python
# Triple quotes preserve formatting
text = """
Line 1
Line 2
Line 3
"""

# For code readability, use parentheses
long_string = (
    "This is a very long string that "
    "spans multiple lines but will be "
    "concatenated into a single line"
)
```

### Tip 6: String Methods Don't Modify Original

```python
text = "hello"
text.upper()  # Returns "HELLO" but doesn't change text
print(text)   # Still "hello"

# Must assign result
text = text.upper()  # Now text is "HELLO"
```

---

## Type Hint Tips

### Tip 1: Use Type Hints for Documentation

Even if not using static type checkers, type hints document your code:

```python
def calculate_tax(amount: float, rate: float) -> float:
    """Much clearer than no hints!"""
    return amount * rate
```

### Tip 2: Optional Values

```python
from typing import Optional

# Python 3.9 and earlier
def find_user(user_id: int) -> Optional[str]:
    # Returns str or None
    pass

# Python 3.10+: Use | None
def find_user(user_id: int) -> str | None:
    pass
```

### Tip 3: Union Types

```python
# Multiple possible types
def process(value: int | float | str) -> str:
    return str(value)

# Note: Union is from typing module in older Python
from typing import Union
def process(value: Union[int, float, str]) -> str:
    pass
```

### Tip 4: Use TypeAlias for Complex Types

```python
# Without alias
def process_data(data: dict[str, list[tuple[int, str]]]) -> dict[str, list[tuple[int, str]]]:
    pass

# With alias (cleaner)
DataType = dict[str, list[tuple[int, str]]]

def process_data(data: DataType) -> DataType:
    pass

# Python 3.12+ type alias syntax
type DataType = dict[str, list[tuple[int, str]]]
```

### Tip 5: Type Hints Don't Enforce Types

```python
def add(a: int, b: int) -> int:
    return a + b

# This still works at runtime!
result = add("hello", "world")  # Returns "helloworld"

# Type hints are for static analysis tools
# Use mypy, pyright, etc. to catch these issues
```

### Tip 6: When to Skip Type Hints

Don't over-type:

**Overkill**:
```python
x: int = 5  # Obvious from value
name: str = "Alice"  # Obvious from value
```

**Better**:
```python
x = 5
name = "Alice"
```

**Use hints when not obvious**:
```python
result = process_data(input_file)  # What type is result?

# Better:
result: ProcessedData = process_data(input_file)
```

---

## Common Gotchas

### Gotcha 1: Mutable vs Immutable

**Immutable** (can't be changed):
- int, float, str, tuple, frozenset

**Mutable** (can be changed):
- list, dict, set

```python
# Immutable
x = 5
y = x
x = 10
# y is still 5

# Mutable
list1 = [1, 2, 3]
list2 = list1  # Both reference SAME list
list1.append(4)
# list2 is now [1, 2, 3, 4]!

# To copy:
list2 = list1.copy()  # or list1[:]
```

### Gotcha 2: String Multiplication Edge Cases

```python
"hello" * 0  # "" (empty string)
"hello" * -1  # "" (empty string, not error!)

# Useful for creating separator lines
print("=" * 50)
```

### Gotcha 3: Boolean Truthiness Surprises

```python
# Empty string is falsy
if "":
    print("Won't print")

# But string "False" is truthy!
if "False":
    print("Will print!")

# Be explicit when needed
value = "False"
if value == "True":  # Better than if value
    pass
```

### Gotcha 4: is vs ==

```python
# == compares values
a = [1, 2, 3]
b = [1, 2, 3]
a == b  # True (same values)

# is compares identity (same object)
a is b  # False (different objects)

# For None, always use 'is'
value = None
if value is None:  # Correct
    pass

if value == None:  # Works but not idiomatic
    pass
```

### Gotcha 5: String Interning

Python "interns" small strings and integers for efficiency:

```python
a = "hello"
b = "hello"
a is b  # True (same object due to interning)

# But not always!
a = "hello world"
b = "hello world"
a is b  # Might be False!

# Never rely on this for logic
# Always use == for string comparison
```

### Gotcha 6: Integer Division and Negative Numbers

```python
7 // 2   # 3 (floor division)
-7 // 2  # -4 (floors toward negative infinity, not zero!)

# If you want truncation toward zero, use int()
int(-7 / 2)  # -3
```

### Gotcha 7: Floating Point Representation

```python
# Not all decimals can be represented exactly
0.1 + 0.1 + 0.1 == 0.3  # False!
0.1 + 0.1 + 0.1  # 0.30000000000000004

# Use Decimal for exactness
from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') == Decimal('0.3')  # True
```

---

## Python 3.14 Specific Tips

### Tip 1: Use New Type Parameter Syntax

**Old** (still works):
```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Container(Generic[T]):
    pass

def first(items: list[T]) -> T:
    pass
```

**New** (Python 3.14):
```python
class Container[T]:
    pass

def first[T](items: list[T]) -> T:
    pass
```

Cleaner and more intuitive!

### Tip 2: Leverage Better Error Messages

Python 3.14 has excellent error suggestions:

```python
name = "Alice"
print(nam)  # Error suggests: Did you mean: 'name'?

my_dict = {"key": "value"}
my_dict["kye"]  # Error suggests: Did you mean: 'key'?
```

Pay attention to these suggestions!

---

## Performance Tips

### Tip 1: Use Built-in Functions

Built-ins are implemented in C and are fast:

```python
# Slow
total = 0
for num in numbers:
    total += num

# Fast
total = sum(numbers)
```

### Tip 2: String Concatenation Performance

```python
# Slow (O(n²) - creates new string each time)
result = ""
for s in strings:
    result += s

# Fast (O(n))
result = "".join(strings)
```

### Tip 3: Use Appropriate Data Types

```python
# For membership testing
# List (slow): O(n)
if item in my_list:
    pass

# Set (fast): O(1)
if item in my_set:
    pass
```

More in Chapter 22: Performance Optimization!

---

## Quick Reference

### Type Conversion
```python
int("42")      # String to int
float("3.14")  # String to float
str(42)        # Number to string
bool(1)        # Anything to bool (truthiness)
list("abc")    # Iterable to list: ['a', 'b', 'c']
tuple([1,2])   # Iterable to tuple: (1, 2)
```

### String Methods (Most Common)
```python
s.upper()      # UPPERCASE
s.lower()      # lowercase
s.strip()      # Remove whitespace
s.split()      # Split into list
s.replace(old, new)  # Replace substring
s.startswith(prefix)  # Check prefix
s.endswith(suffix)    # Check suffix
s.find(sub)    # Find substring (returns index or -1)
s.count(sub)   # Count occurrences
```

### F-String Formatting
```python
f"{value}"           # Basic
f"{value:10}"        # Width 10
f"{value:<10}"       # Left align
f"{value:>10}"       # Right align
f"{value:^10}"       # Center
f"{value:05d}"       # Zero-padded integer
f"{value:.2f}"       # 2 decimal places
f"{value:,.2f}"      # Thousands separator
f"{value:.2%}"       # Percentage
f"{value:.2e}"       # Scientific notation
```

---

## Summary

**Do**:
- ✅ Use f-strings for string formatting
- ✅ Add type hints to functions
- ✅ Use meaningful variable names
- ✅ Use `is None` instead of `== None`
- ✅ Use Decimal for financial calculations
- ✅ Use `join()` for string concatenation in loops

**Don't**:
- ❌ Compare floats with `==`
- ❌ Use mutable default arguments
- ❌ Rely on string interning
- ❌ Use `==` for None
- ❌ Concatenate strings in loops with `+=`
- ❌ Forget that strings are immutable

Master these tips and you'll write cleaner, more Pythonic code!
