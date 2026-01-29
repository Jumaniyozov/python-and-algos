# Basic Syntax and Types: Exercise Solutions

## Solution 1: Variable Manipulation

```python
# Create variables
x, y, z = 10, 20, 30

print(f"Before: x={x}, y={y}, z={z}")

# Swap values using tuple unpacking
# x gets y (20), y gets z (30), z gets x (10)
x, y, z = y, z, x

print(f"After: x={x}, y={y}, z={z}")
```

**Explanation**: Python's tuple unpacking allows simultaneous assignment. The right side is evaluated first, creating a tuple `(20, 30, 10)`, then unpacked into `x, y, z`.

---

## Solution 2: Number Operations

```python
def calculate_stats(numbers: list[float]) -> dict[str, float]:
    """Calculate statistics for a list of numbers."""
    if not numbers:
        return {}

    total = sum(numbers)
    count = len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)

    return {
        "sum": total,
        "average": total / count,
        "min": minimum,
        "max": maximum,
        "range": maximum - minimum
    }

# Test
test_numbers = [10, 25, 3, 47, 19, 33]
stats = calculate_stats(test_numbers)

for key, value in stats.items():
    print(f"{key}: {value}")
```

**Output**:
```
sum: 137.0
average: 22.833333333333332
min: 3.0
max: 47.0
range: 44.0
```

---

## Solution 3: Temperature Converter (Enhanced)

```python
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float | None:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    # Normalize units to uppercase
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # If same unit, return value
    if from_unit == to_unit:
        return value

    # Convert to Celsius first
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5/9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        return None  # Invalid from_unit

    # Check for absolute zero violation
    if celsius < -273.15:
        return None

    # Convert from Celsius to target unit
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius * 9/5 + 32
    elif to_unit == "K":
        kelvin = celsius + 273.15
        return kelvin if kelvin >= 0 else None
    else:
        return None  # Invalid to_unit

# Tests
print(convert_temperature(0, "C", "F"))      # 32.0
print(convert_temperature(100, "C", "K"))    # 373.15
print(convert_temperature(32, "F", "C"))     # 0.0
print(convert_temperature(-300, "C", "K"))   # None
```

---

## Solution 4: String Manipulation

```python
def process_name(full_name: str) -> dict[str, str]:
    """Process a full name and return formatted components."""
    # Clean up whitespace
    full_name = " ".join(full_name.split())

    # Split into parts
    parts = full_name.split()

    if not parts:
        return {
            "first": "",
            "last": "",
            "initials": "",
            "reversed": ""
        }

    # Extract first and last
    first = parts[0].capitalize()
    last = parts[-1].capitalize() if len(parts) > 1 else ""

    # Create initials
    if last:
        initials = f"{first[0].upper()}.{last[0].upper()}."
    else:
        initials = f"{first[0].upper()}."

    # Create reversed format
    reversed_name = f"{last}, {first}" if last else first

    return {
        "first": first,
        "last": last,
        "initials": initials,
        "reversed": reversed_name
    }

# Tests
print(process_name("john doe"))
print(process_name("Mary Jane Watson"))  # Uses first and last only
print(process_name("Madonna"))  # Single name
print(process_name("  john   doe  "))  # Extra whitespace
```

**Output**:
```
{'first': 'John', 'last': 'Doe', 'initials': 'J.D.', 'reversed': 'Doe, John'}
{'first': 'Mary', 'last': 'Watson', 'initials': 'M.W.', 'reversed': 'Watson, Mary'}
{'first': 'Madonna', 'last': '', 'initials': 'M.', 'reversed': 'Madonna'}
{'first': 'John', 'last': 'Doe', 'initials': 'J.D.', 'reversed': 'Doe, John'}
```

---

## Solution 5: String Formatting Practice

```python
def format_invoice(item: str, quantity: int, price: float, tax_rate: float) -> str:
    """Format an invoice with item details and calculations."""
    subtotal = quantity * price
    tax = subtotal * tax_rate
    total = subtotal + tax

    invoice = f"""Item: {item:<20} Qty: {quantity:>5}
Price: ${price:.2f} each
Subtotal: ${subtotal:.2f}
Tax ({tax_rate:.1%}): ${tax:.2f}
Total: ${total:.2f}"""

    return invoice

# Test
print(format_invoice("Python Book", 3, 29.99, 0.085))
```

**Output**:
```
Item: Python Book         Qty:     3
Price: $29.99 each
Subtotal: $89.97
Tax (8.5%): $7.65
Total: $97.62
```

---

## Solution 6: Type Conversion Challenge

```python
def safe_convert(value: str, target_type: str) -> int | float | bool | None:
    """Safely convert a string to the specified type."""
    try:
        if target_type == "int":
            return int(value)
        elif target_type == "float":
            return float(value)
        elif target_type == "bool":
            # Handle boolean conversion
            value_lower = value.lower().strip()
            if value_lower in ("true", "yes", "1"):
                return True
            elif value_lower in ("false", "no", "0"):
                return False
            else:
                return None
        else:
            return None
    except (ValueError, AttributeError):
        return None

# Tests
print(safe_convert("42", "int"))        # 42
print(safe_convert("3.14", "float"))    # 3.14
print(safe_convert("true", "bool"))     # True
print(safe_convert("yes", "bool"))      # True
print(safe_convert("0", "bool"))        # False
print(safe_convert("invalid", "int"))   # None
print(safe_convert("3.14", "int"))      # None (can't convert float string directly)
```

---

## Solution 7: Boolean Logic

```python
def validate_password(password: str) -> tuple[bool, list[str]]:
    """Validate password against security rules."""
    errors = []

    # Check length
    if len(password) < 8:
        errors.append("Too short (minimum 8 characters)")

    # Check for uppercase
    if not any(c.isupper() for c in password):
        errors.append("No uppercase letter")

    # Check for lowercase
    if not any(c.islower() for c in password):
        errors.append("No lowercase letter")

    # Check for digit
    if not any(c.isdigit() for c in password):
        errors.append("No digit")

    # Check for special character
    special_chars = "!@#$%^&*"
    if not any(c in special_chars for c in password):
        errors.append("No special character")

    is_valid = len(errors) == 0
    return (is_valid, errors)

# Tests
print(validate_password("Abc123!@"))
# (True, [])

print(validate_password("short"))
# (False, ['Too short (minimum 8 characters)', 'No uppercase letter', 'No digit', 'No special character'])

print(validate_password("NoDigitsOrSpecial"))
# (False, ['No digit', 'No special character'])
```

---

## Solution 8: Decimal Precision

```python
from decimal import Decimal, getcontext

def calculate_compound_interest(principal: float, rate: float, years: int) -> float:
    """Calculate compound interest using Decimal for precision."""
    # Set precision
    getcontext().prec = 10

    # Convert to Decimal
    p = Decimal(str(principal))
    r = Decimal(str(rate))
    t = Decimal(str(years))

    # Calculate: A = P(1 + r)^t
    amount = p * (Decimal('1') + r) ** t

    # Round to 2 decimal places and return as float
    return float(round(amount, 2))

# Test
result = calculate_compound_interest(1000, 0.05, 10)
print(f"${result:.2f}")  # $1628.89
```

---

## Solution 9: Fraction Operations

```python
from fractions import Fraction

class FractionCalculator:
    def _parse_fraction(self, frac_str: str) -> Fraction:
        """Parse a fraction string like "1/2" into Fraction object."""
        parts = frac_str.split('/')
        return Fraction(int(parts[0]), int(parts[1]))

    def add(self, frac1: str, frac2: str) -> str:
        """Add two fractions."""
        f1 = self._parse_fraction(frac1)
        f2 = self._parse_fraction(frac2)
        result = f1 + f2
        return f"{result.numerator}/{result.denominator}"

    def subtract(self, frac1: str, frac2: str) -> str:
        """Subtract two fractions."""
        f1 = self._parse_fraction(frac1)
        f2 = self._parse_fraction(frac2)
        result = f1 - f2
        return f"{result.numerator}/{result.denominator}"

    def multiply(self, frac1: str, frac2: str) -> str:
        """Multiply two fractions."""
        f1 = self._parse_fraction(frac1)
        f2 = self._parse_fraction(frac2)
        result = f1 * f2
        return f"{result.numerator}/{result.denominator}"

    def divide(self, frac1: str, frac2: str) -> str | None:
        """Divide two fractions. Return None if dividing by zero."""
        f1 = self._parse_fraction(frac1)
        f2 = self._parse_fraction(frac2)

        if f2 == 0:
            return None

        result = f1 / f2
        return f"{result.numerator}/{result.denominator}"

# Tests
calc = FractionCalculator()
print(calc.add("1/2", "1/3"))      # 5/6
print(calc.subtract("3/4", "1/4")) # 1/2
print(calc.multiply("2/3", "3/4")) # 1/2
print(calc.divide("1/2", "1/4"))   # 2/1
print(calc.divide("1/2", "0/1"))   # None
```

---

## Solution 10: Type Hints Practice

```python
def process_data[T: (int, float)](
    data: list[T],
    multiplier: T = 2,  # type: ignore
    include_negative: bool = True
) -> list[T]:
    """
    Process a list of numbers by multiplying each by a multiplier.

    Args:
        data: List of numbers to process
        multiplier: Value to multiply each item by (default: 2)
        include_negative: Whether to include negative results (default: True)

    Returns:
        List of processed values
    """
    result: list[T] = []
    for item in data:
        value = item * multiplier
        if include_negative or value >= 0:
            result.append(value)  # type: ignore
    return result

# Alternative without type parameter:
def process_data_alt(
    data: list[int] | list[float],
    multiplier: int | float = 2,
    include_negative: bool = True
) -> list[int] | list[float]:
    """Process a list of numbers."""
    result = []
    for item in data:
        value = item * multiplier
        if include_negative or value >= 0:
            result.append(value)
    return result
```

---

## Solution 11: String Analyzer (Advanced)

```python
from collections import Counter

def analyze_text(text: str) -> dict[str, int | float | dict]:
    """Analyze text and return comprehensive statistics."""
    # Count characters (excluding spaces for some metrics)
    characters = len(text)

    # Count words
    words = text.split()
    word_count = len(words)

    # Count sentences (. ! ?)
    sentence_count = text.count('.') + text.count('!') + text.count('?')

    # Calculate average word length
    if word_count > 0:
        total_chars = sum(len(word) for word in words)
        avg_word_length = total_chars / word_count
    else:
        avg_word_length = 0.0

    # Count letter frequency (case-insensitive)
    letters_only = ''.join(c.lower() for c in text if c.isalpha())
    letter_freq = dict(Counter(letters_only))

    return {
        "characters": characters,
        "words": word_count,
        "sentences": sentence_count,
        "average_word_length": round(avg_word_length, 2),
        "letter_frequency": letter_freq
    }

# Test
result = analyze_text("Hello world! How are you?")
print(result)
```

---

## Solution 12: Generic Container (Python 3.14)

```python
class Stack[T]:
    """A generic stack (LIFO) data structure."""

    def __init__(self):
        """Initialize empty stack."""
        self._items: list[T] = []

    def push(self, item: T) -> None:
        """Add item to top of stack."""
        self._items.append(item)

    def pop(self) -> T | None:
        """Remove and return top item, or None if empty."""
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self) -> T | None:
        """Return top item without removing, or None if empty."""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return number of items in stack."""
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items})"

# Test
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)
print(int_stack)         # Stack([1, 2, 3])
print(int_stack.pop())   # 3
print(int_stack.peek())  # 2
print(int_stack.size())  # 2

str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
print(str_stack.pop())   # world
```

---

## Challenge Solutions

### Challenge 1: Number Formatter

```python
def format_number(num: int | float, style: str) -> str:
    """Format number in different styles."""
    match style.lower():
        case "currency":
            return f"${num:,.2f}"
        case "scientific":
            return f"{num:.2e}"
        case "percentage":
            return f"{num:.1%}"
        case "binary":
            if isinstance(num, int):
                return bin(num)
            return bin(int(num))
        case "hex":
            if isinstance(num, int):
                return hex(num)
            return hex(int(num))
        case _:
            return str(num)

# Tests
print(format_number(1234.56, "currency"))      # $1,234.56
print(format_number(1234, "scientific"))       # 1.23e+03
print(format_number(0.123, "percentage"))      # 12.3%
print(format_number(1234, "binary"))           # 0b10011010010
print(format_number(1234, "hex"))              # 0x4d2
```

### Challenge 2: Roman Numerals

```python
def int_to_roman(num: int) -> str:
    """Convert integer to Roman numerals."""
    if num < 1 or num > 3999:
        raise ValueError("Number must be between 1 and 3999")

    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result = ""
    for value, symbol in zip(values, symbols):
        count = num // value
        if count:
            result += symbol * count
            num -= value * count
    return result

def roman_to_int(roman: str) -> int:
    """Convert Roman numerals to integer."""
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    result = 0
    prev_value = 0

    for char in reversed(roman.upper()):
        value = values.get(char, 0)
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result

# Tests
print(int_to_roman(1234))  # MCCXXXIV
print(int_to_roman(49))    # XLIX
print(roman_to_int("MCMXC"))  # 1990
print(roman_to_int("XLIX"))   # 49
```

### Challenge 3: Expression Evaluator

```python
import re

def evaluate(expression: str) -> float | None:
    """Safely evaluate simple mathematical expressions."""
    # Remove whitespace
    expression = expression.replace(" ", "")

    # Check if expression contains only allowed characters
    # Allow: digits, operators (+, -, *, /, **, ()), decimal point
    if not re.match(r'^[\d+\-*/().]+$', expression):
        return None

    # Check for dangerous patterns
    if any(word in expression for word in ['__', 'import', 'eval', 'exec']):
        return None

    try:
        # Evaluate in restricted namespace
        result = eval(expression, {"__builtins__": {}}, {})
        return float(result)
    except (SyntaxError, ZeroDivisionError, NameError, TypeError):
        return None

# Tests
print(evaluate("2 + 3 * 4"))      # 14.0
print(evaluate("(10 + 5) / 3"))   # 5.0
print(evaluate("2 ** 3"))         # 8.0
print(evaluate("invalid"))        # None
print(evaluate("import os"))      # None (blocked)
```

---

## Key Learning Points

1. **Multiple assignment**: Use tuple unpacking for elegant swaps
2. **Built-in functions**: `min`, `max`, `sum`, `len` are efficient
3. **Type checking**: Use `isinstance()` for runtime type checks
4. **String methods**: Master `split()`, `join()`, `strip()`, etc.
5. **F-strings**: Most flexible and readable formatting
6. **Decimal/Fraction**: Use for precision when needed
7. **Type hints**: Document expected types and improve tooling
8. **Error handling**: Use `try/except` for risky conversions
9. **List comprehensions**: Concise and Pythonic
10. **Generic types**: Python 3.14's `[T]` syntax is clean and powerful

Practice these solutions and try to understand each line of code!
