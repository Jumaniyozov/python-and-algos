#!/usr/bin/env python3
"""
types_demo.py - Demonstration of Python's basic data types

This script showcases different numeric types, strings, booleans,
and type conversions with practical examples.
"""


def demo_integers():
    """Demonstrate integer operations."""
    print("=" * 50)
    print("INTEGER DEMONSTRATION")
    print("=" * 50)

    # Basic operations
    a, b = 15, 4
    print(f"\na = {a}, b = {b}")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor division: {a} // {b} = {a // b}")
    print(f"Modulo: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a**b}")

    # Large integers
    huge = 2**100
    print(f"\n2^100 = {huge}")
    print(f"Length: {len(str(huge))} digits")

    # Number bases
    binary = 0b1010
    octal = 0o12
    hexadec = 0xFF
    print(f"\nBinary 0b1010 = {binary}")
    print(f"Octal 0o12 = {octal}")
    print(f"Hexadecimal 0xFF = {hexadec}")


def demo_floats():
    """Demonstrate floating point operations."""
    print("\n" + "=" * 50)
    print("FLOAT DEMONSTRATION")
    print("=" * 50)

    pi = 3.14159
    e = 2.71828
    print(f"\nπ ≈ {pi}")
    print(f"e ≈ {e}")

    # Precision issues
    result = 0.1 + 0.2
    print(f"\n0.1 + 0.2 = {result}")
    print(f"Expected 0.3? {result == 0.3}")
    print(f"Rounded: {round(result, 1)}")

    # Using Decimal for precision
    from decimal import Decimal

    d1 = Decimal("0.1")
    d2 = Decimal("0.2")
    print(f"\nUsing Decimal: {d1} + {d2} = {d1 + d2}")
    print(f"Exact? {d1 + d2 == Decimal('0.3')}")


def demo_strings():
    """Demonstrate string operations."""
    print("\n" + "=" * 50)
    print("STRING DEMONSTRATION")
    print("=" * 50)

    text = "Python Programming"
    print(f"\nOriginal: {text}")
    print(f"Length: {len(text)}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    print(f"First 6 chars: {text[:6]}")
    print(f"Last 11 chars: {text[-11:]}")
    print(f"Reversed: {text[::-1]}")

    # String formatting
    name = "Alice"
    age = 30
    print(f"\n--- String Formatting ---")
    print(f"Hello, {name}! You are {age} years old.")
    print(f"Next year: {name} will be {age + 1}")

    # Advanced formatting
    value = 1234.5678
    print(f"\n--- Number Formatting ---")
    print(f"Original: {value}")
    print(f"2 decimals: {value:.2f}")
    print(f"With commas: {value:,.2f}")
    print(f"Percentage: {0.755:.1%}")


def demo_booleans():
    """Demonstrate boolean operations and truthiness."""
    print("\n" + "=" * 50)
    print("BOOLEAN DEMONSTRATION")
    print("=" * 50)

    # Boolean operations
    print(f"\nTrue and False = {True and False}")
    print(f"True or False = {True or False}")
    print(f"not True = {not True}")

    # Comparisons
    x, y = 5, 10
    print(f"\n{x} == {y} = {x == y}")
    print(f"{x} < {y} = {x < y}")
    print(f"{x} != {y} = {x != y}")

    # Truthiness
    print("\n--- Truthiness Tests ---")
    falsy_values = [0, 0.0, "", [], {}, None, False]
    for val in falsy_values:
        print(f"{repr(val):10} is falsy")

    print()
    truthy_values = [1, "text", [1], {"a": 1}, True]
    for val in truthy_values:
        print(f"{repr(val):10} is truthy")


def demo_type_conversion():
    """Demonstrate type conversions."""
    print("\n" + "=" * 50)
    print("TYPE CONVERSION DEMONSTRATION")
    print("=" * 50)

    # String to number
    str_int = "42"
    str_float = "3.14"
    print(f"\nString '{str_int}' to int: {int(str_int)}")
    print(f"String '{str_float}' to float: {float(str_float)}")

    # Number to string
    num = 100
    print(f"\nInt {num} to string: '{str(num)}'")

    # Float to int (truncates)
    f = 3.7
    print(f"\nFloat {f} to int: {int(f)} (truncates)")

    # Type checking
    print(f"\nType of {num}: {type(num)}")
    print(f"Is {num} an int? {isinstance(num, int)}")


def demo_generics():
    """Demonstrate Python 3.14 generic types."""
    print("\n" + "=" * 50)
    print("GENERIC TYPES DEMONSTRATION (Python 3.14)")
    print("=" * 50)

    # Generic function
    def first[T](items: list[T]) -> T:
        """Return first item from list."""
        return items[0]

    # Works with any type
    numbers = [1, 2, 3]
    words = ["hello", "world"]

    print(f"\nFirst number: {first(numbers)}")
    print(f"First word: {first(words)}")

    # Generic class
    class Box[T]:
        """A generic container."""

        def __init__(self, item: T):
            self.item = item

        def get(self) -> T:
            return self.item

        def __repr__(self) -> str:
            return f"Box({self.item!r})"

    int_box = Box(42)
    str_box = Box("Python")

    print(f"\nInteger box: {int_box}")
    print(f"String box: {str_box}")
    print(f"Get value: {int_box.get()}")


def main():
    """Run all demonstrations."""
    print("\n")
    print("╔" + "═" * 48 + "╗")
    print("║" + " " * 10 + "PYTHON TYPES DEMONSTRATION" + " " * 12 + "║")
    print("╚" + "═" * 48 + "╝")

    demo_integers()
    demo_floats()
    demo_strings()
    demo_booleans()
    demo_type_conversion()
    demo_generics()

    print("\n" + "=" * 50)
    print("DEMONSTRATION COMPLETE")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
