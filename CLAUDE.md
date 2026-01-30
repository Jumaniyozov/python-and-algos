# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a comprehensive Python learning curriculum covering Python fundamentals (3.14+), standard library, and algorithms/data structures. The curriculum is organized as a book-like learning resource with 45 chapters.

## Curriculum Structure

The curriculum is divided into 5 parts:

### Part 1: Python Fundamentals (Chapters 1-8)
- Chapter 1: Getting Started
- Chapter 2: Basic Syntax and Types
- Chapter 3: Collections
- Chapter 4: Control Flow
- Chapter 5: Functions
- Chapter 6: Object-Oriented Programming
- Chapter 7: Modules and Packages
- Chapter 8: File I/O and Path Handling

### Part 2: Standard Library Deep Dive (Chapters 9-15)
- Chapter 9: Itertools and Functional Tools
- Chapter 10: String Processing
- Chapter 11: Date and Time
- Chapter 12: Concurrency
- Chapter 13: Networking and Web
- Chapter 14: Testing (unittest, doctest, mock)
- Chapter 15: Debugging and Profiling

### Part 3: Advanced Python (Chapters 16-22)
- Chapter 16: Metaclasses and Advanced OOP
- Chapter 17: Generators and Iterators
- Chapter 18: Context Managers
- Chapter 19: Type System and Static Analysis
- Chapter 20: Memory Management
- Chapter 21: Niche Features and Hidden Gems
- Chapter 22: Performance Optimization

### Part 4: Essential External Libraries & Developer Tools (Chapters 23-26)
- Chapter 23: pytest (Comprehensive testing framework)
- Chapter 24: Package Management & Environments (Poetry, pip, venv)
- Chapter 25: Code Quality & Linting (Black, Ruff, mypy, pre-commit)
- Chapter 26: Other Essential Tools (Rich, Click/Typer, Pydantic, Loguru)

### Part 5: Algorithms and Data Structures (Chapters 27-45)
- Chapter 27: Algorithms and Complexity Analysis (Algorithm design, mathematical induction, Big O, time/space complexity)
- Chapter 28: Problem-Solving Patterns (Two pointers, sliding window, fast/slow pointers, all 15 essential patterns)
- Chapter 29: Arrays and Strings (Fundamentals, manipulation techniques)
- Chapter 30: Linked Lists (Singly, doubly, circular linked lists)
- Chapter 31: Stacks and Queues (LIFO, FIFO, applications)
- Chapter 32: Hash Tables (Hash functions, collision handling)
- Chapter 33: Trees (Binary trees, BST, traversals)
- Chapter 34: Advanced Trees (AVL, Red-Black, B-Trees, Tries, Segment Trees)
- Chapter 35: Heaps (Priority queues, heap operations)
- Chapter 36: Graphs (DFS, BFS, topological sort, union find)
- Chapter 37: Advanced Graphs (Dijkstra, Bellman-Ford, MST, network flow)
- Chapter 38: Sorting Algorithms (Comparison and non-comparison based)
- Chapter 39: Searching Algorithms (Binary search and variations)
- Chapter 40: Dynamic Programming (1D, 2D, common patterns)
- Chapter 41: Greedy Algorithms (Interval scheduling, common patterns)
- Chapter 42: Backtracking (Permutations, combinations, N-Queens)
- Chapter 43: Bit Manipulation (Bitwise operations, tricks)
- Chapter 44: Advanced Algorithms (KMP, Rabin-Karp, LRU cache, advanced techniques)
- Chapter 45: Interview Strategy (Framework, communication, practice)

### Bonus Chapters (46-47)
- Chapter 46: Data Science Essentials (NumPy, Pandas, Matplotlib)
- Chapter 47: Web Development (Requests, Flask, FastAPI)

## File Structure Standard

Each chapter follows this structure:
- `README.md` - Chapter overview and learning objectives
- `theory.md` - Detailed explanations and concepts
- `examples.md` - Code examples with annotations
- `exercises.md` - Practice problems
- `solutions.md` - Detailed solutions with explanations
- `tips.md` - Tips, tricks, and gotchas
- Python files (`.py`) - Runnable code examples

## Content Guidelines

### Python Content (Chapters 1-26)
- Use Python 3.14 features and syntax
- Include niche features, tips, and tricks in relevant chapters
- Cover standard library comprehensively
- Explain with clear examples and use cases
- Include type hints and modern Python practices
- Reference PEPs where relevant (e.g., PEP 636 pattern matching, PEP 695 type parameters)
- For external tools (Part 4): provide comprehensive examples and real-world usage patterns

### Algorithms Content (Chapters 27-45)
- Start each algorithm with complexity analysis (time and space)
- Include common patterns and problem-solving templates
- Provide multiple solution approaches where applicable
- Add detailed explanations for each solution step
- Include edge cases and common mistakes
- Add practical tips and tricks for interviews
- Link related problems and patterns

## Development

### Running Examples
```bash
# Run any Python example
python <chapter_folder>/<example_file>.py

# Example:
python 01_getting_started/hello_world.py
```

### Navigation
- Start with `00_introduction/README.md` for curriculum overview
- Follow `INDEX.md` for complete table of contents
- Check `PROGRESS.md` to track completion status
- Use `LEARNING_PATHS.md` for suggested learning sequences

## Task Tracking

This project uses tasks to track curriculum creation progress. Use:
- `/tasks` - View all tasks and their status
- Task IDs #1-23 correspond to different sections of the curriculum
- Each task is self-contained and can be completed independently
- Progress persists across sessions

## Special Features to Include

### Python 3.14 Features
- Type parameter syntax (PEP 695)
- Improved error messages
- Per-interpreter GIL
- Other version-specific improvements

### Niche Python Tips
- Ellipsis (...) object uses
- Walrus operator (:=) patterns
- __missing__ in dicts
- Positional-only and keyword-only parameters
- Sentinel values and singleton patterns
- Module-level __getattr__ and __dir__
- Advanced descriptor patterns
- Metaclass applications

### Algorithm Patterns (Chapters 27-45)
- Two Pointers, Sliding Window
- Fast/Slow Pointers, Monotonic Stack
- Union Find, Topological Sort
- Binary Search variations
- DP patterns (1D, 2D, state machine)
- Backtracking templates
- Graph traversal patterns

### Part 4: External Tools - Comprehensive Coverage

**Chapter 23: pytest**
- Fixtures and dependency injection
- Parametrization and markers
- Plugins ecosystem (pytest-cov, pytest-mock, pytest-asyncio, pytest-xdist)
- Configuration and conftest.py
- Advanced testing patterns

**Chapter 24: Package Management**
- pip fundamentals (install, uninstall, freeze, requirements.txt)
- Virtual environments (venv, virtualenv)
- Poetry comprehensive guide (init, add, install, update, lock, publish)
- pyproject.toml and modern packaging (PEP 517/518/621)
- Dependency resolution and lockfiles (poetry.lock)
- Publishing to PyPI

**Chapter 25: Code Quality Tools**
- Black formatting rules and configuration
- Ruff comprehensive linting guide
- mypy type checking patterns
- Pre-commit hook setup and custom hooks

**Chapter 26: Essential Libraries**
- Rich: terminal formatting, progress bars, tables, syntax highlighting
- Click/Typer: building CLI applications
- Pydantic: data validation and settings management
- Loguru: advanced logging patterns
