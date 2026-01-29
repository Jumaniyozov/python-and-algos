#!/usr/bin/env python3
"""
string_formatting.py - Comprehensive guide to string formatting in Python

Demonstrates various string formatting techniques with f-strings,
showing practical examples and common use cases.
"""

from datetime import datetime
from decimal import Decimal

def basic_formatting():
    """Basic f-string formatting examples."""
    print("=" * 60)
    print("BASIC F-STRING FORMATTING")
    print("=" * 60)

    name = "Alice"
    age = 30
    city = "New York"

    print(f"\nName: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Full info: {name} is {age} years old and lives in {city}")

    # Expressions in f-strings
    print(f"\nNext year {name} will be {age + 1}")
    print(f"Uppercase name: {name.upper()}")
    print(f"Name length: {len(name)}")

def number_formatting():
    """Demonstrate number formatting."""
    print("\n" + "=" * 60)
    print("NUMBER FORMATTING")
    print("=" * 60)

    pi = 3.14159265359
    large_num = 1234567.89
    percentage = 0.755

    print("\n--- Decimal Places ---")
    print(f"Pi (original): {pi}")
    print(f"Pi (2 decimals): {pi:.2f}")
    print(f"Pi (4 decimals): {pi:.4f}")
    print(f"Pi (6 decimals): {pi:.6f}")

    print("\n--- Thousands Separator ---")
    print(f"Large number: {large_num:,.2f}")
    print(f"As integer: {int(large_num):,}")

    print("\n--- Percentage ---")
    print(f"Percentage: {percentage:.1%}")
    print(f"Percentage (2 decimals): {percentage:.2%}")

    print("\n--- Scientific Notation ---")
    print(f"Scientific (2 decimals): {large_num:.2e}")
    print(f"Scientific (4 decimals): {large_num:.4e}")

    print("\n--- Zero Padding ---")
    num = 42
    print(f"Zero-padded (5 digits): {num:05d}")
    print(f"Zero-padded (8 digits): {num:08d}")

    print("\n--- Sign Display ---")
    positive = 42
    negative = -42
    print(f"Always show sign: {positive:+d}")
    print(f"Always show sign: {negative:+d}")
    print(f"Space for positive: {positive: d}")
    print(f"Space for positive: {negative: d}")

def alignment_formatting():
    """Demonstrate text alignment."""
    print("\n" + "=" * 60)
    print("TEXT ALIGNMENT")
    print("=" * 60)

    text = "Python"
    width = 20

    print("\n--- Basic Alignment ---")
    print(f"Left:   '{text:<{width}}'")
    print(f"Right:  '{text:>{width}}'")
    print(f"Center: '{text:^{width}}'")

    print("\n--- Alignment with Fill Character ---")
    print(f"Fill with dots:   '{text:.<{width}}'")
    print(f"Fill with dashes: '{text:->{width}}'")
    print(f"Fill with stars:  '{text:*^{width}}'")

    print("\n--- Table-like Formatting ---")
    items = [
        ("Apple", 10, 1.50),
        ("Banana", 25, 0.75),
        ("Orange", 15, 1.25),
    ]

    print(f"{'Item':<12} {'Qty':>6} {'Price':>8}")
    print("-" * 28)
    for item, qty, price in items:
        print(f"{item:<12} {qty:>6} ${price:>7.2f}")

def advanced_formatting():
    """Advanced formatting techniques."""
    print("\n" + "=" * 60)
    print("ADVANCED FORMATTING")
    print("=" * 60)

    # Debug formatting (Python 3.8+)
    x = 42
    y = 100
    print("\n--- Debug Formatting (shows variable name) ---")
    print(f"{x=}")
    print(f"{y=}")
    print(f"{x + y=}")

    # Nested formatting
    value = 123.456789
    precision = 2
    print("\n--- Nested Formatting ---")
    print(f"Value with {precision} decimals: {value:.{precision}f}")

    precision = 4
    print(f"Value with {precision} decimals: {value:.{precision}f}")

    # Datetime formatting
    now = datetime.now()
    print("\n--- Datetime Formatting ---")
    print(f"Full: {now:%Y-%m-%d %H:%M:%S}")
    print(f"Date only: {now:%Y-%m-%d}")
    print(f"Time only: {now:%H:%M:%S}")
    print(f"Custom: {now:%B %d, %Y}")
    print(f"Weekday: {now:%A}")

    # Binary, octal, hex
    num = 42
    print("\n--- Number Base Formatting ---")
    print(f"Decimal: {num}")
    print(f"Binary: {num:b} (or {bin(num)})")
    print(f"Octal: {num:o} (or {oct(num)})")
    print(f"Hex (lowercase): {num:x} (or {hex(num)})")
    print(f"Hex (uppercase): {num:X}")

def practical_examples():
    """Practical real-world formatting examples."""
    print("\n" + "=" * 60)
    print("PRACTICAL EXAMPLES")
    print("=" * 60)

    # Invoice formatting
    print("\n--- Invoice ---")
    items = [
        ("Python Programming Book", 2, 29.99),
        ("Code Editor License", 1, 49.99),
        ("Online Course", 1, 89.99),
    ]

    print(f"{'Item':<25} {'Qty':>5} {'Price':>10} {'Total':>10}")
    print("-" * 52)

    subtotal = 0
    for item, qty, price in items:
        total = qty * price
        subtotal += total
        print(f"{item:<25} {qty:>5} ${price:>9.2f} ${total:>9.2f}")

    tax = subtotal * 0.085
    total = subtotal + tax

    print("-" * 52)
    print(f"{'Subtotal:':<42} ${subtotal:>9.2f}")
    print(f"{'Tax (8.5%):':<42} ${tax:>9.2f}")
    print(f"{'Total:':<42} ${total:>9.2f}")

    # Progress bar
    print("\n--- Progress Bar ---")
    for i in range(0, 101, 10):
        filled = i // 2
        bar = "█" * filled + "░" * (50 - filled)
        print(f"\r[{bar}] {i:>3}%", end="")
    print()  # Newline after progress bar

    # Financial data
    print("\n--- Stock Prices ---")
    stocks = [
        ("AAPL", 150.25, 2.5),
        ("GOOGL", 2800.50, -1.3),
        ("TSLA", 725.75, 5.8),
    ]

    print(f"{'Symbol':<8} {'Price':>10} {'Change':>10}")
    print("-" * 30)

    for symbol, price, change in stocks:
        sign = "+" if change > 0 else ""
        print(f"{symbol:<8} ${price:>9.2f} {sign}{change:>8.2f}%")

def comparison_example():
    """Compare different formatting methods."""
    print("\n" + "=" * 60)
    print("FORMATTING METHOD COMPARISON")
    print("=" * 60)

    name = "Alice"
    age = 30

    print("\n--- Old % formatting (avoid) ---")
    print("Hello, %s! You are %d years old." % (name, age))

    print("\n--- .format() method (okay but verbose) ---")
    print("Hello, {}! You are {} years old.".format(name, age))
    print("Hello, {0}! You are {1} years old.".format(name, age))
    print("Hello, {name}! You are {age} years old.".format(name=name, age=age))

    print("\n--- f-strings (preferred, Python 3.6+) ---")
    print(f"Hello, {name}! You are {age} years old.")

    print("\n✓ f-strings are:")
    print("  - More readable")
    print("  - Faster")
    print("  - Support expressions")
    print("  - Modern Python standard")

def main():
    """Run all formatting examples."""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 12 + "PYTHON STRING FORMATTING GUIDE" + " " * 16 + "║")
    print("╚" + "═" * 58 + "╝")

    basic_formatting()
    number_formatting()
    alignment_formatting()
    advanced_formatting()
    practical_examples()
    comparison_example()

    print("\n" + "=" * 60)
    print("FORMATTING GUIDE COMPLETE")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
