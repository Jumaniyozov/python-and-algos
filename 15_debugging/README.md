# Chapter 15: Debugging and Profiling

Master debugging techniques and performance profiling in Python.

## What You'll Learn

- pdb debugger usage
- logging module
- Profiling with cProfile and timeit
- Memory profiling with tracemalloc
- Debugging techniques and strategies
- Common debugging patterns

## Files

- [theory.md](theory.md) - Debugging fundamentals
- [examples.md](examples.md) - Practical examples
- [exercises.md](exercises.md) - Practice problems
- [solutions.md](solutions.md) - Solutions
- [tips.md](tips.md) - Best practices

## Quick Reference

### pdb Debugger
```python
import pdb; pdb.set_trace()  # Breakpoint

# Or Python 3.7+
breakpoint()  # Easier syntax
```

### Logging
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
```

### Profiling
```python
import cProfile
cProfile.run('my_function()')

# Or
python -m cProfile script.py
```

### Timing Code
```python
import timeit
time = timeit.timeit('x = sum(range(100))', number=10000)
print(f"Time: {time}s")
```

## Prerequisites

- Basic Python syntax
- Understanding of functions
- Command line familiarity

## Next Steps

- Chapter 22: Performance Optimization
- Advanced profiling techniques
- Production debugging
