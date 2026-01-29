# Chapter 12: Concurrency

Master Python's concurrency models: threading, multiprocessing, and asyncio.

## What You'll Learn

- Threading basics and the Global Interpreter Lock (GIL)
- Multiprocessing for CPU-bound tasks
- asyncio for I/O-bound operations
- concurrent.futures for simplified concurrent execution
- When to use each concurrency model
- Common patterns and pitfalls

## Files

- [theory.md](theory.md) - Core concepts and models
- [examples.md](examples.md) - Practical examples
- [exercises.md](exercises.md) - Practice problems
- [solutions.md](solutions.md) - Exercise solutions
- [tips.md](tips.md) - Best practices and gotchas

## Quick Reference

### When to Use What

**Threading**: I/O-bound tasks (network, file operations)
```python
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(download_file, urls)
```

**Multiprocessing**: CPU-bound tasks (computation, data processing)
```python
from concurrent.futures import ProcessPoolExecutor
with ProcessPoolExecutor(max_workers=4) as executor:
    results = executor.map(process_data, datasets)
```

**Asyncio**: Many I/O operations, network servers
```python
import asyncio
async def main():
    results = await asyncio.gather(*[fetch(url) for url in urls])
```

## Key Concepts

1. **GIL**: Global Interpreter Lock limits one thread executing Python bytecode
2. **Thread Safety**: Managing shared state between threads
3. **Race Conditions**: Concurrent access leading to bugs
4. **Deadlocks**: Threads waiting for each other indefinitely
5. **Event Loop**: Core of asyncio's cooperative multitasking

## Prerequisites

- Understanding of functions and generators
- Basic exception handling
- Familiarity with file I/O and networking concepts

## Next Steps

After mastering concurrency, explore:
- Chapter 13: Networking and Web
- Chapter 22: Performance Optimization
- Advanced async patterns
