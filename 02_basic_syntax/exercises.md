# Basic Syntax and Types: Practice Exercises

## Exercise 1: Variable Manipulation

Write a program that:
1. Creates three variables: `x = 10`, `y = 20`, `z = 30`
2. Swaps their values so that `x` gets `y`'s value, `y` gets `z`'s value, and `z` gets `x`'s original value
3. Prints the result

Expected output:
```
Before: x=10, y=20, z=30
After: x=20, y=30, z=10
```

---

## Exercise 2: Number Operations

Create a function `calculate_stats(numbers: list[float]) -> dict[str, float]` that takes a list of numbers and returns a dictionary containing:
- `"sum"`: Sum of all numbers
- `"average"`: Average of the numbers
- `"min"`: Minimum value
- `"max"`: Maximum value
- `"range"`: Difference between max and min

Test with `[10, 25, 3, 47, 19, 33]`

---

## Exercise 3: Temperature Converter (Enhanced)

Create a function `convert_temperature(value: float, from_unit: str, to_unit: str) -> float | None` that converts between Celsius (C), Fahrenheit (F), and Kelvin (K).

Formulas:
- C to F: `F = C * 9/5 + 32`
- F to C: `C = (F - 32) * 5/9`
- C to K: `K = C + 273.15`
- K to C: `C = K - 273.15`

Return `None` for invalid conversions or if Kelvin goes below 0 (absolute zero).

Test cases:
```python
convert_temperature(0, "C", "F")      # 32.0
convert_temperature(100, "C", "K")    # 373.15
convert_temperature(32, "F", "C")     # 0.0
convert_temperature(-300, "C", "K")   # None (below absolute zero)
```

---

## Exercise 4: String Manipulation

Write a function `process_name(full_name: str) -> dict[str, str]` that takes a full name and returns:
- `"first"`: First name
- `"last"`: Last name
- `"initials"`: Initials (uppercase)
- `"reversed"`: Name in "Last, First" format

Example:
```python
process_name("john doe")
# Returns: {
#     "first": "John",
#     "last": "Doe",
#     "initials": "J.D.",
#     "reversed": "Doe, John"
# }
```

Handle edge cases:
- Names with more than 2 parts (use first and last only)
- Single names (last name is empty)
- Extra whitespace

---

## Exercise 5: String Formatting Practice

Create a function `format_invoice(item: str, quantity: int, price: float, tax_rate: float) -> str` that returns a formatted invoice string.

Requirements:
- Item name left-aligned in 20 characters
- Quantity right-aligned in 5 characters
- Price formatted as currency with 2 decimals
- Calculate and show subtotal, tax, and total
- Use f-strings for all formatting

Example output:
```
Item: Python Book        Qty:     3
Price: $29.99 each
Subtotal: $89.97
Tax (8.5%): $7.65
Total: $97.62
```

---

## Exercise 6: Type Conversion Challenge

Write a function `safe_convert(value: str, target_type: str) -> int | float | bool | None` that safely converts a string to the specified type.

- `target_type` can be: `"int"`, `"float"`, `"bool"`
- Return `None` if conversion fails
- For bool: `"true"`, `"yes"`, `"1"` → `True`; `"false"`, `"no"`, `"0"` → `False`

Test cases:
```python
safe_convert("42", "int")        # 42
safe_convert("3.14", "float")    # 3.14
safe_convert("true", "bool")     # True
safe_convert("invalid", "int")   # None
```

---

## Exercise 7: Boolean Logic

Write a function `validate_password(password: str) -> tuple[bool, list[str]]` that validates a password and returns:
- Boolean: Whether password is valid
- List of strings: Error messages (empty if valid)

Rules:
- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character (!@#$%^&*)

Example:
```python
validate_password("Abc123!@")
# (True, [])

validate_password("short")
# (False, ['Too short', 'No uppercase', 'No digit', 'No special character'])
```

---

## Exercise 8: Decimal Precision

Write a function `calculate_compound_interest(principal: float, rate: float, years: int) -> float` that calculates compound interest using the `Decimal` type for precision.

Formula: `A = P(1 + r)^t`
- P = principal
- r = annual interest rate (as decimal, e.g., 0.05 for 5%)
- t = time in years

Return the final amount rounded to 2 decimal places.

Test:
```python
calculate_compound_interest(1000, 0.05, 10)
# Should return: 1628.89 (using Decimal for precision)
```

---

## Exercise 9: Fraction Operations

Create a `FractionCalculator` class that performs arithmetic with fractions:

```python
class FractionCalculator:
    def add(self, frac1: str, frac2: str) -> str:
        """Add two fractions given as strings like "1/2"."""
        pass

    def subtract(self, frac1: str, frac2: str) -> str:
        pass

    def multiply(self, frac1: str, frac2: str) -> str:
        pass

    def divide(self, frac1: str, frac2: str) -> str | None:
        """Return None if dividing by zero."""
        pass
```

Use the `fractions.Fraction` class internally.

Test:
```python
calc = FractionCalculator()
calc.add("1/2", "1/3")      # "5/6"
calc.multiply("2/3", "3/4") # "1/2"
calc.divide("1/2", "0/1")   # None
```

---

## Exercise 10: Type Hints Practice

Add proper type hints to this function and fix any type-related issues:

```python
def process_data(data, multiplier=2, include_negative=True):
    result = []
    for item in data:
        value = item * multiplier
        if include_negative or value >= 0:
            result.append(value)
    return result
```

Requirements:
- Add parameter and return type hints
- Use Python 3.14 generic syntax if applicable
- Ensure the function is properly typed

---

## Exercise 11: String Analyzer (Advanced)

Create a function `analyze_text(text: str) -> dict[str, int | float | dict]` that returns comprehensive text statistics:

```python
{
    "characters": int,              # Total characters
    "words": int,                   # Total words
    "sentences": int,               # Number of sentences (. ! ?)
    "average_word_length": float,   # Average characters per word
    "letter_frequency": dict        # Count of each letter (case-insensitive)
}
```

Example:
```python
analyze_text("Hello world! How are you?")
# Returns:
# {
#     "characters": 25,
#     "words": 5,
#     "sentences": 2,
#     "average_word_length": 4.0,
#     "letter_frequency": {'h': 2, 'e': 2, 'l': 3, ...}
# }
```

---

## Exercise 12: Generic Container (Python 3.14)

Implement a generic `Stack` class using Python 3.14's type parameter syntax:

```python
class Stack[T]:
    def __init__(self):
        """Initialize empty stack."""
        pass

    def push(self, item: T) -> None:
        """Add item to top of stack."""
        pass

    def pop(self) -> T | None:
        """Remove and return top item, or None if empty."""
        pass

    def peek(self) -> T | None:
        """Return top item without removing, or None if empty."""
        pass

    def is_empty(self) -> bool:
        """Check if stack is empty."""
        pass

    def size(self) -> int:
        """Return number of items in stack."""
        pass
```

Test:
```python
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)
print(int_stack.pop())  # 3
print(int_stack.peek())  # 2
print(int_stack.size())  # 2
```

---

## Challenge Exercises

### Challenge 1: Number Formatter

Create a function `format_number(num: int | float, style: str) -> str` that formats numbers in different styles:

Styles:
- `"currency"`: $1,234.56
- `"scientific"`: 1.23e+03
- `"percentage"`: 12.3%
- `"binary"`: 0b10011010010
- `"hex"`: 0x4D2
- `"words"`: "one thousand two hundred thirty-four" (bonus!)

### Challenge 2: Roman Numerals

Write two functions:
- `int_to_roman(num: int) -> str`: Convert integer (1-3999) to Roman numerals
- `roman_to_int(roman: str) -> int`: Convert Roman numerals to integer

Rules:
- I=1, V=5, X=10, L=50, C=100, D=500, M=1000
- Subtractive notation: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900

### Challenge 3: Expression Evaluator

Create a function `evaluate(expression: str) -> float | None` that evaluates simple mathematical expressions:

```python
evaluate("2 + 3 * 4")      # 14.0
evaluate("(10 + 5) / 3")   # 5.0
evaluate("2 ** 3")         # 8.0
evaluate("invalid")        # None
```

Use Python's built-in `eval()` with safety checks (only allow numbers and basic operators).

---

## Hints

- For Exercise 4: Use `split()` and `join()` methods
- For Exercise 7: Use string methods like `any()` with generator expressions
- For Exercise 8: `from decimal import Decimal` and convert inputs to Decimal
- For Exercise 11: Use `collections.Counter` for letter frequency
- For Exercise 12: Use a list internally to store stack items

---

## Submission

Test your solutions with different inputs to ensure they handle edge cases:
- Empty strings
- Zero and negative numbers
- None values
- Type mismatches

Check solutions.md after attempting these exercises!
