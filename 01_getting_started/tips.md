# Getting Started: Tips, Tricks, and Gotchas

## Installation Tips

### ✅ Always Add Python to PATH

**Windows**: Check "Add Python to PATH" during installation. If you forgot:
1. Search for "Environment Variables" in Windows
2. Edit PATH variable
3. Add Python installation directory

**Verify**:
```bash
python --version  # Should work from any directory
```

### ✅ Use `python3` on Unix Systems

On macOS/Linux, `python` might still point to Python 2:

```bash
# Check what python points to
which python
python --version

# Use python3 for Python 3.x
which python3
python3 --version

# Create an alias in ~/.bashrc or ~/.zshrc
alias python=python3
alias pip=pip3
```

### ✅ Keep Python Updated

```bash
# Check current version
python --version

# Update on macOS with Homebrew
brew upgrade python

# On Linux
sudo apt update && sudo apt upgrade python3.14
```

---

## REPL Productivity Tips

### Tip 1: Use Arrow Keys

- **Up/Down arrows**: Navigate command history
- **Left/Right arrows**: Edit current line
- **Ctrl+A**: Jump to beginning of line
- **Ctrl+E**: Jump to end of line
- **Ctrl+K**: Delete from cursor to end of line

### Tip 2: Multi-line Editing

For functions and loops:

```python
>>> def greet(name):  # Press Enter
...     return f"Hello, {name}"  # Press Enter
...     # Press Enter again to execute
>>> greet("World")
'Hello, World!'
```

### Tip 3: Quick Exit

Multiple ways to exit REPL:

```python
>>> exit()        # Function call
>>> quit()        # Also works
>>> # Ctrl+D (Unix/macOS)
>>> # Ctrl+Z then Enter (Windows)
```

### Tip 4: Suppress Output with Semicolon

```python
>>> x = 42  # No output
>>> x
42
>>> x = 43;  # Semicolon suppresses output
>>>
```

### Tip 5: Use `_` for Last Result

```python
>>> 100 * 5
500
>>> _ + 50
550
>>> result = _
>>> result
550
```

**Gotcha**: `_` only works in interactive mode, not in scripts!

### Tip 6: Quick Documentation

```python
>>> help(str.upper)  # Detailed help
>>> str.upper.__doc__  # Quick docstring
'Return a copy of the string converted to uppercase.'
```

### Tip 7: Explore Objects with `dir()`

```python
>>> dir(str)  # All string methods
>>> [x for x in dir(str) if not x.startswith('_')]  # Hide private methods
['capitalize', 'casefold', 'center', 'count', ...]
```

### Tip 8: Use IPython for Enhanced REPL

Install IPython for better interactive experience:

```bash
pip install ipython
ipython
```

Features:
- Syntax highlighting
- Better tab completion
- Magic commands (`%timeit`, `%run`, etc.)
- Enhanced help with `?`

---

## Script Writing Tips

### Tip 1: Always Use `if __name__ == "__main__"`

**Good**:
```python
# script.py

def main():
    print("Running main")

if __name__ == "__main__":
    main()
```

**Why**:
- Makes code reusable
- Can import functions without running script
- Follows Python conventions

### Tip 2: Use Descriptive File Names

**Good**: `temperature_converter.py`, `data_analyzer.py`
**Bad**: `script.py`, `test.py`, `new.py`

### Tip 3: Add Shebang for Unix Systems

```python
#!/usr/bin/env python3
# your_script.py

print("Hello")
```

Make executable:
```bash
chmod +x your_script.py
./your_script.py
```

### Tip 4: Use `.py` Extension

Always save Python files with `.py` extension:
- Enables syntax highlighting
- Makes clear it's Python code
- Required for imports

### Tip 5: One Script, One Purpose

Keep scripts focused:

**Good**: `download_data.py`, `process_data.py`, `visualize_data.py`
**Bad**: `do_everything.py`

---

## Common Gotchas and Mistakes

### Gotcha 1: Indentation Matters

**Wrong**:
```python
def greet():
print("Hello")  # IndentationError!
```

**Right**:
```python
def greet():
    print("Hello")  # 4 spaces or 1 tab
```

**Tip**: Use spaces (4 spaces is standard), not tabs. Configure your editor to insert spaces when you press Tab.

### Gotcha 2: Case Sensitivity

```python
name = "Alice"
print(Name)  # NameError: name 'Name' is not defined

# Python is case-sensitive!
# name ≠ Name ≠ NAME
```

### Gotcha 3: Reserved Keywords

Can't use keywords as variable names:

```python
class = "Math"  # SyntaxError: invalid syntax
for = 10  # SyntaxError: invalid syntax

# Reserved words: and, as, assert, break, class, continue, def, del,
# elif, else, except, False, finally, for, from, global, if, import,
# in, is, lambda, None, nonlocal, not, or, pass, raise, return, True,
# try, while, with, yield
```

**Check keywords**:
```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', ...]
>>> keyword.iskeyword('class')
True
```

### Gotcha 4: Division Behavior

```python
# Integer division in Python 2 vs Python 3
>>> 7 / 2
3.5  # Python 3: always returns float

>>> 7 // 2  # Floor division
3  # Returns integer

>>> 7.0 // 2.0
3.0  # Floor division with floats returns float
```

### Gotcha 5: Mutable Default Arguments

**Dangerous**:
```python
def add_item(item, items=[]):  # Bad!
    items.append(item)
    return items

>>> add_item(1)
[1]
>>> add_item(2)  # Expects [2], but...
[1, 2]  # The list persists!
```

**Safe**:
```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

(More on this in Chapter 5: Functions)

### Gotcha 6: Comparison vs Assignment

```python
# Assignment (single =)
x = 5  # Sets x to 5

# Comparison (double ==)
x == 5  # Checks if x equals 5, returns True/False

# Common mistake
if x = 5:  # SyntaxError!
    print("Wrong")

# Correct
if x == 5:
    print("Correct")
```

### Gotcha 7: String Immutability

```python
>>> text = "hello"
>>> text[0] = "H"  # TypeError: 'str' object does not support item assignment

# Strings are immutable - create new string instead
>>> text = "H" + text[1:]
>>> text
'Hello'
```

---

## Development Environment Tips

### Tip 1: Configure Your Editor

**VS Code**:
1. Install Python extension
2. Select Python interpreter (Ctrl+Shift+P → "Python: Select Interpreter")
3. Enable linting and formatting

**Settings to enable**:
- Auto-indentation
- Spaces instead of tabs (4 spaces)
- Show whitespace characters
- Auto-save

### Tip 2: Use Virtual Environments Early

Even for learning, use virtual environments:

```bash
# Create
python -m venv venv

# Activate
source venv/bin/activate  # Unix
venv\Scripts\activate  # Windows

# Install packages
pip install package_name

# Deactivate
deactivate
```

**Why**:
- Keeps system Python clean
- Each project has its own dependencies
- Easy to delete and recreate

### Tip 3: Learn Keyboard Shortcuts

**Terminal**:
- `Ctrl+C`: Interrupt current command
- `Ctrl+D`: Exit Python REPL (Unix)
- `Ctrl+L`: Clear screen
- Tab: Auto-complete

**Editor** (VS Code):
- `Ctrl+\``: Open terminal
- `F5`: Run with debugger
- `Ctrl+/`: Comment/uncomment line
- `Shift+Alt+F`: Format code

### Tip 4: Use Version Control from Day One

```bash
git init
git add .
git commit -m "Initial commit"
```

Even for learning projects!

---

## Python 3.14 Specific Tips

### Tip 1: Use New Type Parameter Syntax

**Old way** (still works):
```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Container(Generic[T]):
    pass
```

**New way** (Python 3.14+):
```python
class Container[T]:
    pass
```

Cleaner and more intuitive!

### Tip 2: Take Advantage of Better Error Messages

Python 3.14's errors are incredibly helpful:

```python
>>> name = "Alice"
>>> print(nam)
NameError: name 'nam' is not defined. Did you mean: 'name'?
```

Don't ignore these suggestions!

### Tip 3: Use `match-case` for Complex Conditions

Pattern matching (since 3.10, refined in 3.14):

```python
def handle_command(command):
    match command:
        case "start":
            print("Starting...")
        case "stop":
            print("Stopping...")
        case _:
            print("Unknown command")
```

More on this in Chapter 4: Control Flow.

---

## Performance Tips (Preview)

### Tip 1: Use Built-in Functions

Built-ins are optimized in C:

```python
# Slower
total = 0
for x in range(1000):
    total += x

# Faster
total = sum(range(1000))
```

### Tip 2: List Comprehensions are Fast

```python
# Slower
squares = []
for x in range(1000):
    squares.append(x ** 2)

# Faster
squares = [x ** 2 for x in range(1000)]
```

More in Chapter 22: Performance Optimization.

---

## Debugging Tips

### Tip 1: Use `print()` Debugging

Quick and effective:

```python
def calculate(x):
    print(f"DEBUG: x = {x}")  # Debug print
    result = x * 2
    print(f"DEBUG: result = {result}")
    return result
```

Remove debug prints before committing code!

### Tip 2: Use `type()` to Check Types

```python
>>> x = 42
>>> type(x)
<class 'int'>

>>> y = "42"
>>> type(y)
<class 'str'>
```

### Tip 3: Use `repr()` for Debugging

```python
>>> text = "hello\nworld"
>>> print(text)
hello
world
>>> print(repr(text))
'hello\nworld'  # Shows escape characters
```

---

## Learning Tips

### Tip 1: Type Code, Don't Copy-Paste

Muscle memory helps learning:
- Type examples yourself
- Make intentional mistakes to see errors
- Experiment with variations

### Tip 2: Use the REPL Constantly

Before writing a script:
- Test snippets in REPL
- Verify behavior
- Then write script

### Tip 3: Read Error Messages Carefully

Python's error messages are helpful:
- Read the whole message
- Look at the line number
- Understand the error type

### Tip 4: Experiment Fearlessly

You can't break Python:
- Try things in REPL
- See what happens
- Learn from errors

### Tip 5: Build Small Projects

After each chapter:
- Build a tiny project using what you learned
- Examples: calculator, todo list, word counter
- Learning by doing is most effective

---

## Quick Reference

### Run Python Code
```bash
python                    # Start REPL
python script.py          # Run script
python -c "code"          # Run one-liner
python -m module          # Run module
```

### Get Help
```bash
python --help             # Command-line help
help()                    # REPL help system
help(object)              # Help on object
object.__doc__            # Quick docstring
dir(object)               # List attributes
```

### Check Version
```bash
python --version          # Version string
python -c "import sys; print(sys.version_info)"  # Detailed info
```

---

## Common Error Messages

| Error | Meaning | Common Cause |
|-------|---------|--------------|
| `SyntaxError` | Invalid Python syntax | Missing colon, wrong indentation |
| `NameError` | Name not defined | Typo, forgot to assign variable |
| `TypeError` | Wrong type for operation | Adding str + int |
| `IndentationError` | Incorrect indentation | Mixed tabs/spaces |
| `AttributeError` | Object has no attribute | Typo in method name |
| `IndexError` | Index out of range | Accessing list[10] when len is 5 |
| `KeyError` | Key not in dictionary | Accessing non-existent dict key |
| `ValueError` | Inappropriate value | int("hello") |
| `ImportError` | Can't import module | Module not installed |

---

## Next Steps

1. Practice everything in this chapter
2. Get comfortable with REPL and scripts
3. Experiment with Python 3.14 features
4. Set up your development environment
5. Move on to Chapter 2: Basic Syntax and Types

Happy coding!
