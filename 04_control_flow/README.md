# Chapter 4: Control Flow

## Learning Objectives

By the end of this chapter, you will:
- Master conditional statements (if, elif, else)
- Use pattern matching (match-case) effectively
- Write efficient loops (for, while)
- Understand the else clause in loops
- Handle exceptions properly
- Use context managers with the 'with' statement
- Apply Python 3.10+ pattern matching

## Chapter Contents

1. **theory.md** - Core concepts
   - Conditional statements
   - Loops and iteration
   - Exception handling
   - Context managers
   - Pattern matching (PEP 636)

2. **examples.md** - Practical code examples
   - Real-world conditionals
   - Loop patterns
   - Exception handling strategies
   - Context manager usage
   - Pattern matching examples

3. **exercises.md** - Practice problems
4. **solutions.md** - Detailed solutions
5. **tips.md** - Best practices and gotchas

## Quick Reference

```python
# Conditionals
if condition:
    pass
elif other_condition:
    pass
else:
    pass

# Pattern matching (Python 3.10+)
match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")

# Loops
for item in iterable:
    pass

while condition:
    pass

# Exception handling
try:
    risky_operation()
except ValueError as e:
    handle_error(e)
finally:
    cleanup()

# Context manager
with open('file.txt') as f:
    data = f.read()
```

## Prerequisites

- Chapters 1-3
- Understanding of Python basics

## Estimated Time

- Reading: 2-3 hours
- Practice: 2-3 hours
- Total: 4-6 hours

## Next Chapter

**Chapter 5: Functions** - Learn about function definitions, arguments, decorators, and generators.
