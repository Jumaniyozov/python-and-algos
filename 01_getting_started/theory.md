# Getting Started: Theory and Concepts

## 1.1 Python Installation and Setup

### What is Python?

Python is a high-level, interpreted, general-purpose programming language created by Guido van Rossum in 1991. It emphasizes code readability and allows programmers to express concepts in fewer lines of code compared to languages like C++ or Java.

### Installing Python 3.14

#### Download and Install

**Official Source**: https://python.org

**Platform-Specific Instructions**:

**Windows**:
1. Download installer from python.org
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Click "Install Now"
5. Verify: `python --version` in Command Prompt

**macOS**:
```bash
# Using Homebrew (recommended)
brew install python@3.14

# Or download from python.org
# Verify
python3 --version
```

**Linux (Ubuntu/Debian)**:
```bash
# Update package list
sudo apt update

# Install Python 3.14
sudo apt install python3.14 python3.14-venv

# Verify
python3.14 --version
```

### Verification

After installation, verify:

```bash
# Check version
python --version
# or
python3 --version

# Should output: Python 3.14.x

# Check pip (package manager)
pip --version
# or
pip3 --version
```

---

## 1.2 The Python Interpreter and Execution Model

### How Python Works

Python is an **interpreted language**, meaning:

1. **Source Code** (.py files) → human-readable Python code
2. **Bytecode** (.pyc files) → intermediate representation
3. **Python Virtual Machine (PVM)** → executes bytecode

```
Your Code (.py)  →  [Python Interpreter]  →  Bytecode (.pyc)  →  [PVM]  →  Execution
```

### The Python Interpreter

The interpreter is the program that reads and executes Python code. When you run:

```bash
python script.py
```

The interpreter:
1. Reads `script.py`
2. Compiles it to bytecode (cached in `__pycache__/`)
3. Executes the bytecode

### Execution Models

Python code can be executed in several ways:

#### 1. Interactive Mode (REPL)
```bash
python
>>> print("Hello")
Hello
```

#### 2. Script Mode
```bash
python script.py
```

#### 3. Module Mode
```bash
python -m module_name
```

#### 4. One-liner Mode
```bash
python -c "print('Hello')"
```

---

## 1.3 REPL and Interactive Development

### What is the REPL?

**REPL** = Read-Eval-Print Loop

A way to:
- **R**ead user input
- **E**valuate the expression
- **P**rint the result
- **L**oop back for more input

### Starting the REPL

```bash
python
# or
python3
```

You'll see:

```
Python 3.14.0 (main, Jan 2026...)
[GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` is the **primary prompt**, waiting for your input.

### Basic REPL Usage

```python
>>> 2 + 2
4

>>> name = "Alice"
>>> name
'Alice'

>>> def greet(name):
...     return f"Hello, {name}!"
...
>>> greet("Bob")
'Hello, Bob!'
```

Notice:
- Single expressions show their value
- The `...` is the **secondary prompt** for multi-line statements
- Functions and variables persist in the session

### Special REPL Variables

```python
>>> 10 + 5
15
>>> _  # Last result
15
>>> _ * 2
30
```

`_` holds the last returned value (in interactive mode only).

### Useful REPL Commands

```python
>>> help()  # Interactive help system
>>> help(str)  # Help on a specific object
>>> dir()  # List names in current scope
>>> dir(str)  # List attributes of an object
>>> exit()  # Exit REPL (or Ctrl+D on Unix, Ctrl+Z on Windows)
```

### Multiline Input

For blocks (functions, loops, classes), use Enter to create newlines:

```python
>>> for i in range(3):
...     print(i)
...     # Press Enter twice to execute
0
1
2
```

---

## 1.4 First Programs and Execution Models

### Hello World

The traditional first program:

```python
# hello.py
print("Hello, World!")
```

Run it:

```bash
python hello.py
```

Output:
```
Hello, World!
```

### Script Structure

A basic Python script:

```python
# Comments start with #

# Statements execute top-to-bottom
x = 10
y = 20
print(x + y)

# Functions must be defined before use
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

### The `if __name__ == "__main__"` Pattern

```python
# my_module.py

def greet(name):
    return f"Hello, {name}"

# This block only runs when script is executed directly
# Not when imported as a module
if __name__ == "__main__":
    print(greet("World"))
```

**Why use it?**
- Allows file to be both imported and executed
- Code in the `if` block runs only when script is main program
- Code outside runs even when imported

Usage:

```bash
# Direct execution
python my_module.py
# Output: Hello, World

# Import in another script
# import my_module  # greet() function available, but no print output
```

### Shebang (Unix/Linux/macOS)

Make scripts executable:

```python
#!/usr/bin/env python3
# hello.py

print("Hello, World!")
```

```bash
chmod +x hello.py
./hello.py
```

---

## 1.5 Python 3.14 Overview and New Features

Python 3.14 (released January 2026) includes several improvements and new features.

### Key Features

#### 1. Type Parameter Syntax (PEP 695)

**Before (3.11 and earlier)**:
```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, item: T):
        self.item = item
```

**Python 3.14+**:
```python
class Box[T]:
    def __init__(self, item: T):
        self.item = item

def first[T](items: list[T]) -> T:
    return items[0]
```

Much cleaner syntax for generic types!

#### 2. Improved Error Messages

Python 3.14 has even better error messages:

```python
# Typo in variable name
name = "Alice"
print(nam)

# Python 3.14 suggests:
# NameError: name 'nam' is not defined. Did you mean: 'name'?
```

#### 3. Per-Interpreter GIL (Subinterpreters)

Experimental support for true parallelism with subinterpreters, each with their own GIL (Global Interpreter Lock).

```python
import _xxsubinterpreters as interpreters

# Create isolated interpreter
interp_id = interpreters.create()
interpreters.run_string(interp_id, "print('Hello from subinterpreter')")
```

#### 4. Performance Improvements

- Faster dictionary operations
- Improved bytecode optimization
- Better memory management

#### 5. Standard Library Updates

- Enhanced `pathlib` features
- New `tomllib` for TOML parsing (read-only)
- Improved `asyncio` performance

### Checking Python Features

```python
import sys

print(f"Python version: {sys.version}")
print(f"Version info: {sys.version_info}")

# Check feature availability
if sys.version_info >= (3, 14):
    print("Type parameter syntax available!")
```

---

## Development Environment Setup

### Choosing an Editor

**For Beginners**:
- **VS Code**: Free, excellent Python support, many extensions
- **PyCharm Community**: Powerful IDE, Python-focused

**For Advanced Users**:
- **Vim/Neovim**: Fast, customizable
- **Emacs**: Highly extensible
- **Sublime Text**: Fast, lightweight

### Essential Editor Features

1. **Syntax highlighting**: Makes code readable
2. **Auto-indentation**: Python requires proper indentation
3. **Linting**: Catches errors as you type
4. **Code completion**: Suggests completions

### Virtual Environments (Preview)

We'll cover this in depth in Chapter 24, but briefly:

```bash
# Create virtual environment
python -m venv myenv

# Activate
source myenv/bin/activate  # Unix/macOS
myenv\Scripts\activate  # Windows

# Deactivate
deactivate
```

**Why use them?**
- Isolate project dependencies
- Avoid conflicts between projects
- Easy to recreate environment

---

## Key Concepts Summary

1. **Python is interpreted**: Code is executed line-by-line
2. **REPL is your friend**: Test code quickly, experiment, learn
3. **Scripts are files**: Save code in `.py` files and run with `python script.py`
4. **`if __name__ == "__main__"`**: Distinguishes script execution from imports
5. **Python 3.14**: Latest features include cleaner type syntax and better errors
6. **Environment matters**: Set up a good editor and use virtual environments

---

## Common Questions

**Q: Python or python3?**
A: Depends on your system. `python` might be Python 2 on older systems. Use `python3` or check `python --version`.

**Q: When to use REPL vs scripts?**
A: REPL for quick tests and learning. Scripts for programs you want to save and run repeatedly.

**Q: Do I need to know about bytecode?**
A: Not initially. Python handles it automatically. Understanding helps with performance tuning later.

**Q: Why so many Python versions?**
A: Python evolves. Newer versions have better features, but some old code may only work with older versions.

---

## Next Steps

1. Practice in the REPL
2. Write and run simple scripts
3. Explore Python 3.14 features
4. Set up your development environment
5. Move on to examples.md for hands-on practice
