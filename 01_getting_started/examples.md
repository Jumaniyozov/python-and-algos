# Getting Started: Code Examples

## Example 1: First REPL Session

Open your terminal and start Python:

```bash
$ python
Python 3.14.0 (main, Jan 2026...)
>>>
```

Now try these commands:

```python
>>> # This is a comment - Python ignores it
>>> print("Hello, Python!")
Hello, Python!

>>> # Math operations
>>> 2 + 2
4

>>> 10 * 5
50

>>> 7 / 2  # Division always returns float
3.5

>>> 7 // 2  # Floor division
3

>>> 2 ** 10  # Exponentiation
1024

>>> # Variables
>>> name = "Alice"
>>> age = 30
>>> print(f"{name} is {age} years old")
Alice is 30 years old

>>> # The special _ variable
>>> 100 + 200
300
>>> _  # Last result
300
>>> _ * 2
600

>>> # Getting help
>>> help(print)
# Shows documentation for print()

>>> # Listing available names
>>> dir()
['__builtins__', '__doc__', '__name__', ..., 'age', 'name']

>>> # Exit
>>> exit()
```

---

## Example 2: Hello World Script

Create a file `hello.py`:

```python
# hello.py - My first Python program

print("Hello, World!")
print("Welcome to Python 3.14!")

# Let's do some math
result = 2 + 2
print(f"2 + 2 = {result}")

# Let's use a variable
name = "Python Learner"
print(f"Hello, {name}!")
```

Run it:

```bash
$ python hello.py
Hello, World!
Welcome to Python 3.14!
2 + 2 = 4
Hello, Python Learner!
```

---

## Example 3: Interactive Calculation

```python
# calculator.py

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined"

# Display results
print(f"\n{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
```

Run it:

```bash
$ python calculator.py
Enter first number: 10
Enter second number: 3
10.0 + 3.0 = 13.0
10.0 - 3.0 = 7.0
10.0 * 3.0 = 30.0
10.0 / 3.0 = 3.3333333333333335
```

---

## Example 4: Using Functions

```python
# greet.py

def greet(name):
    """
    Greet someone by name.
    """
    return f"Hello, {name}!"

def greet_multiple(names):
    """
    Greet multiple people.
    """
    for name in names:
        print(greet(name))

# This code only runs when script is executed directly
if __name__ == "__main__":
    # Single greeting
    message = greet("Alice")
    print(message)

    # Multiple greetings
    people = ["Bob", "Charlie", "Diana"]
    greet_multiple(people)
```

Run it:

```bash
$ python greet.py
Hello, Alice!
Hello, Bob!
Hello, Charlie!
Hello, Diana!
```

Import it in REPL:

```python
>>> import greet
>>> greet.greet("Python")
'Hello, Python!'
>>> # Notice: the if __name__ == "__main__" block didn't run
```

---

## Example 5: Python 3.14 Type Parameter Syntax

```python
# generics.py - Demonstrating Python 3.14 type parameters

def first[T](items: list[T]) -> T:
    """
    Return the first item from a list.
    T is a type parameter - can be any type.
    """
    if not items:
        raise ValueError("List is empty")
    return items[0]

def last[T](items: list[T]) -> T:
    """
    Return the last item from a list.
    """
    if not items:
        raise ValueError("List is empty")
    return items[-1]

class Box[T]:
    """
    A generic box that can hold any type.
    """
    def __init__(self, item: T):
        self.item = item

    def get(self) -> T:
        return self.item

    def set(self, item: T) -> None:
        self.item = item

    def __repr__(self) -> str:
        return f"Box({self.item!r})"

if __name__ == "__main__":
    # Using generic functions
    numbers = [1, 2, 3, 4, 5]
    print(f"First: {first(numbers)}")  # 1
    print(f"Last: {last(numbers)}")    # 5

    words = ["hello", "world"]
    print(f"First: {first(words)}")    # hello

    # Using generic class
    int_box = Box(42)
    print(int_box)  # Box(42)
    print(int_box.get())  # 42

    str_box = Box("Python")
    print(str_box)  # Box('Python')
    print(str_box.get())  # Python
```

Output:

```bash
$ python generics.py
First: 1
Last: 5
First: hello
Box(42)
42
Box('Python')
Python
```

---

## Example 6: Command Line Arguments

```python
# args.py - Working with command line arguments

import sys

def main():
    # sys.argv is a list of command line arguments
    # sys.argv[0] is the script name
    # sys.argv[1:] are the arguments

    print(f"Script name: {sys.argv[0]}")
    print(f"Number of arguments: {len(sys.argv) - 1}")

    if len(sys.argv) > 1:
        print("Arguments:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"  {i}. {arg}")
    else:
        print("No arguments provided")
        print("Usage: python args.py arg1 arg2 arg3")

if __name__ == "__main__":
    main()
```

Usage:

```bash
$ python args.py
Script name: args.py
Number of arguments: 0
No arguments provided
Usage: python args.py arg1 arg2 arg3

$ python args.py hello world
Script name: args.py
Number of arguments: 2
Arguments:
  1. hello
  2. world
```

---

## Example 7: One-Liner Execution

```bash
# Print Python version
$ python -c "import sys; print(sys.version)"

# Quick calculation
$ python -c "print(sum(range(101)))"
5050

# Generate random number
$ python -c "import random; print(random.randint(1, 100))"
42

# Current date and time
$ python -c "from datetime import datetime; print(datetime.now())"
2026-01-28 14:30:00.123456
```

---

## Example 8: Module Execution

Python can execute modules directly with `-m`:

```bash
# Run the built-in HTTP server
$ python -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 ...

# Run the built-in calendar module
$ python -m calendar 2026 1
    January 2026
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31

# Check if a module is available
$ python -m pip --version
pip 24.0 from ...

# Create a virtual environment
$ python -m venv myenv
```

---

## Example 9: Interactive Help System

```python
>>> # Start help system
>>> help()

Welcome to Python 3.14's help utility!
...
help> str
# Shows documentation for str class

help> print
# Shows documentation for print function

help> keywords
# Shows Python keywords

help> quit
# Exit help system
>>>

>>> # Quick help on specific object
>>> help(len)
# Shows help for len() function

>>> help([].append)
# Shows help for list.append() method
```

---

## Example 10: Checking Version and Features

```python
# version_check.py

import sys

def check_python_version():
    """
    Display Python version information.
    """
    print(f"Python version: {sys.version}")
    print(f"Version info: {sys.version_info}")

    # Check specific version
    if sys.version_info >= (3, 14):
        print("✓ Python 3.14+ detected")
        print("✓ Type parameter syntax available")
        print("✓ Enhanced error messages available")
    elif sys.version_info >= (3, 10):
        print("⚠ Python 3.10+ detected")
        print("⚠ Consider upgrading to Python 3.14")
    else:
        print("✗ Python version too old")
        print("✗ Please upgrade to Python 3.14+")

    # Platform information
    print(f"\nPlatform: {sys.platform}")
    print(f"Implementation: {sys.implementation.name}")

if __name__ == "__main__":
    check_python_version()
```

Output:

```bash
$ python version_check.py
Python version: 3.14.0 (main, Jan 28 2026, ...)
Version info: sys.version_info(major=3, minor=14, micro=0, releaselevel='final', serial=0)
✓ Python 3.14+ detected
✓ Type parameter syntax available
✓ Enhanced error messages available

Platform: linux
Implementation: cpython
```

---

## Example 11: Error Messages in Python 3.14

```python
# errors.py - Demonstrating improved error messages

def demonstrate_errors():
    # 1. Name error with suggestion
    name = "Alice"
    # print(nam)  # Uncomment to see: NameError: name 'nam' is not defined. Did you mean: 'name'?

    # 2. Attribute error with suggestion
    text = "hello"
    # text.upcase()  # Uncomment to see: AttributeError: 'str' has no attribute 'upcase'. Did you mean: 'upper'?

    # 3. Type error with clear message
    # result = "5" + 5  # Uncomment to see detailed type error

    # 4. Index error with context
    numbers = [1, 2, 3]
    # print(numbers[5])  # Uncomment to see: IndexError: list index out of range

    print("All errors demonstrated (commented out)")

if __name__ == "__main__":
    demonstrate_errors()
```

---

## Practice Exercises

Try creating these programs yourself:

### Exercise 1: Personal Info
Create a script that asks for your name and age, then prints a greeting.

### Exercise 2: Temperature Converter
Convert Celsius to Fahrenheit: F = C * 9/5 + 32

### Exercise 3: Area Calculator
Calculate area of circle, rectangle, and triangle based on user input.

### Exercise 4: Countdown
Create a countdown from 10 to 1 using a loop.

Solutions in `solutions.md` (when available).

---

## Key Takeaways

1. **REPL is great for experimentation**: Quick feedback, no need to save files
2. **Scripts are for reusable code**: Save your work, run it multiple times
3. **`if __name__ == "__main__"`**: Makes code both importable and executable
4. **Python 3.14 features**: Type parameters, better errors, performance improvements
5. **Help is always available**: `help()`, `dir()`, and documentation

Next, check out `tips.md` for best practices and common mistakes to avoid!
