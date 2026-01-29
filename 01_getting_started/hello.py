#!/usr/bin/env python3
"""
hello.py - Your first Python program

This script demonstrates basic Python concepts:
- Print statements
- Variables
- String formatting
- Functions
"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def main():
    """Main function - entry point of the program."""
    # Print a simple message
    print("Hello, World!")
    print("Welcome to Python 3.14!")

    # Use variables
    name = "Python Learner"
    message = greet(name)
    print(message)

    # Do some math
    result = 2 + 2
    print(f"2 + 2 = {result}")

    # Show Python version
    import sys
    print(f"\nYou are using Python {sys.version_info.major}.{sys.version_info.minor}")

if __name__ == "__main__":
    main()
