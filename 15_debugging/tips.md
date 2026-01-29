# Debugging and Profiling - Tips and Best Practices

## Debugging Best Practices

### 1. Read the Error Message Carefully

**Error messages tell you**:
- Type of error
- Where it occurred (file and line number)
- What went wrong
- Stack trace (call hierarchy)

**Example**:
```python
Traceback (most recent call last):
  File "script.py", line 15, in <module>
    result = divide(10, 0)
  File "script.py", line 8, in divide
    return a / b
ZeroDivisionError: division by zero
```

Read from bottom to top: Error type → What happened → Where it happened

### 2. Use print() Strategically

**Bad** (too much noise):
```python
def process(data):
    print("Starting")
    print(f"Data: {data}")
    for item in data:
        print(f"Processing {item}")
        result = item * 2
        print(f"Result: {result}")
    print("Done")
```

**Good** (focused):
```python
def process(data):
    print(f"Processing {len(data)} items")
    results = [item * 2 for item in data]
    print(f"First result: {results[0]}, Last result: {results[-1]}")
    return results
```

### 3. Use pdb Effectively

**Quick reference**:
```python
breakpoint()  # Python 3.7+

# Common commands:
# l (list) - show code
# n (next) - next line
# s (step) - step into function
# c (continue) - continue execution
# p var - print variable
# pp var - pretty print
# w (where) - stack trace
# u (up) - move up stack
# d (down) - move down stack
# q (quit) - exit debugger
```

**Conditional breakpoints**:
```python
for i in range(100):
    if i == 50:  # Only break when i is 50
        breakpoint()
    process(i)
```

### 4. Log, Don't Print

**Print statements**:
- Hard to disable
- No context
- Not production-ready

**Logging**:
- Can be enabled/disabled by level
- Includes timestamps, module names
- Can log to files
- Production-ready

```python
import logging

# Instead of prints
# print("Processing data")
# print(f"Error: {error}")

# Use logging
logging.info("Processing data")
logging.error(f"Error: {error}")
```

### 5. Use Assertions for Assumptions

```python
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers"

    return sum(numbers) / len(numbers)
```

## Profiling Best Practices

### 1. Profile Before Optimizing

**Wrong approach**:
1. Guess what's slow
2. Optimize it
3. Hope it's faster

**Right approach**:
1. **Profile** to find bottleneck
2. Optimize bottleneck
3. **Profile again** to verify improvement

### 2. Use the Right Tool

**timeit**: Micro-benchmarks
```python
import timeit
timeit.timeit('x = sum(range(100))', number=10000)
```

**cProfile**: Function-level profiling
```python
import cProfile
cProfile.run('my_function()')
```

**tracemalloc**: Memory profiling
```python
import tracemalloc
tracemalloc.start()
# ... code ...
current, peak = tracemalloc.get_traced_memory()
```

### 3. Focus on Hot Paths

- 80/20 rule: 80% of time spent in 20% of code
- Find and optimize the hot paths
- Don't optimize code that rarely runs

### 4. Compare Performance

```python
import timeit

# Always compare implementations
time_old = timeit.timeit(old_implementation, number=1000)
time_new = timeit.timeit(new_implementation, number=1000)

print(f"Old: {time_old:.4f}s")
print(f"New: {time_new:.4f}s")
print(f"Speedup: {time_old/time_new:.2f}x")
```

## Common Pitfalls

### 1. Debugging in Production Code

**Bad**:
```python
def important_function():
    print("Debug: entering function")  # Left in production!
    breakpoint()  # NEVER do this in production!
    # ... code ...
```

**Good**:
```python
import logging

def important_function():
    logger.debug("Entering function")  # Can be disabled
    # ... code ...
```

### 2. Not Removing Debug Code

- Use version control
- Search for `print(`, `breakpoint()`, `pdb.set_trace()` before committing
- Use logging instead of print

### 3. Over-Optimizing

**Premature optimization is the root of all evil**:
- Write clear code first
- Profile to find real bottlenecks
- Only optimize what matters

### 4. Profiling in Debug Mode

- Always profile in production-like environment
- Debug mode is slower
- Use optimizations (-O flag)

## Quick Debugging Checklist

When you hit a bug:

1. **Can you reproduce it?**
   - If not, add logging to understand when it happens

2. **What's the error message?**
   - Read it carefully
   - Google it if unclear

3. **Where does it happen?**
   - Check stack trace
   - Add breakpoint or prints

4. **What are the values?**
   - Print/inspect relevant variables
   - Check for None, empty strings, etc.

5. **What did you expect?**
   - Write it down
   - Compare with actual behavior

6. **What changed recently?**
   - Check version control
   - Revert if necessary

## Logging Best Practices

### Log Levels

```python
logger.debug("Detailed diagnostic info")     # Development
logger.info("General informational messages") # Production events
logger.warning("Something unexpected")        # Potential problems
logger.error("Serious problem occurred")      # Errors
logger.critical("System unstable")            # Critical failures
```

### Log Format

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Output:
# 2024-03-15 14:30:45 - mymodule - INFO - Processing started
```

### Don't Log Sensitive Data

```python
# BAD
logger.info(f"User login: {username} with password {password}")

# GOOD
logger.info(f"User login attempt: {username}")
```

## Memory Profiling Tips

### Find Memory Leaks

```python
import tracemalloc

tracemalloc.start()

# Snapshot before
snapshot1 = tracemalloc.take_snapshot()

# Run code
suspicious_function()

# Snapshot after
snapshot2 = tracemalloc.take_snapshot()

# Compare
stats = snapshot2.compare_to(snapshot1, 'lineno')
for stat in stats[:10]:
    print(stat)
```

### Check Object Count

```python
import gc
import sys

# Count objects of specific type
def count_objects(obj_type):
    return len([obj for obj in gc.get_objects() if isinstance(obj, obj_type)])

# Before
before = count_objects(MyClass)

# Do something
# ...

# After
after = count_objects(MyClass)
print(f"Created {after - before} objects")
```

## Quick Reference Card

**Debugging**:
```bash
# Run with debugger
python -m pdb script.py

# Post-mortem debugging
python -i script.py  # Opens interpreter on error
```

**Profiling**:
```bash
# Profile script
python -m cProfile -s cumtime script.py

# Time one-liner
python -m timeit 'sum(range(100))'

# Memory profile (needs memory_profiler)
python -m memory_profiler script.py
```

**Logging**:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

**Common Issues**:
- `NameError`: Variable not defined
- `AttributeError`: Object doesn't have attribute
- `TypeError`: Wrong type
- `IndexError`: List index out of range
- `KeyError`: Dict key doesn't exist
- `ZeroDivisionError`: Division by zero
- `FileNotFoundError`: File doesn't exist
- `ImportError`: Module not found

## Tools and Resources

**Debugging**:
- pdb (built-in)
- ipdb (improved pdb)
- pudb (visual debugger)
- IDE debuggers (VS Code, PyCharm)

**Profiling**:
- cProfile (built-in)
- timeit (built-in)
- line_profiler (pip install)
- memory_profiler (pip install)
- py-spy (sampling profiler)

**Logging**:
- logging (built-in)
- loguru (pip install - simpler API)
- structlog (structured logging)
