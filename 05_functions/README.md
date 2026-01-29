# Chapter 5: Functions

## Learning Objectives

By the end of this chapter, you will:
- Define and call functions with various parameter types
- Use *args and **kwargs effectively
- Create and use lambda functions
- Understand and apply decorators
- Master closures and nonlocal variables
- Write generator functions with yield
- Use async functions and coroutines

## Chapter Contents

1. **theory.md** - Comprehensive coverage of:
   - Function basics and parameters
   - Args, kwargs, and parameter types
   - Lambda functions
   - Decorators and functools
   - Closures and scope
   - Generators and yield
   - Async functions

2. **examples.md** - Practical implementations
3. **exercises.md** - Practice problems
4. **solutions.md** - Detailed solutions
5. **tips.md** - Best practices and gotchas

## Quick Reference

```python
# Basic function
def greet(name):
    return f"Hello, {name}"

# Default parameters
def power(base, exponent=2):
    return base ** exponent

# *args and **kwargs
def func(*args, **kwargs):
    pass

# Lambda
square = lambda x: x ** 2

# Decorator
@decorator
def function():
    pass

# Generator
def count(n):
    for i in range(n):
        yield i

# Async function
async def fetch_data():
    await asyncio.sleep(1)
    return "data"
```

## Prerequisites

- Chapters 1-4
- Understanding of Python basics

## Estimated Time

- Reading: 3-4 hours
- Practice: 3-4 hours
- Total: 6-8 hours

## Next Chapter

**Chapter 6: Object-Oriented Programming**
