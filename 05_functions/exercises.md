# Functions: Practice Exercises

## Exercise 1: Function Basics
Write a function `calculate_average(*numbers)` that accepts any number of arguments and returns their average. Return 0 if no arguments provided.

## Exercise 2: Keyword Arguments
Create `create_profile(name, age, *, city, country="USA", **interests)` that returns a dictionary with all the information.

## Exercise 3: Lambda and Sorting
Given a list of tuples `[(name, age, salary), ...]`, write lambda functions to sort by:
- Age (ascending)
- Salary (descending)
- Name (alphabetically)

## Exercise 4: Simple Decorator
Create a `@log_calls` decorator that prints the function name and arguments each time it's called.

## Exercise 5: Timing Decorator
Write a `@timer` decorator that measures and prints execution time of a function.

## Exercise 6: Closure-Based Counter
Create a function `make_counter()` that returns three functions: `increment()`, `decrement()`, and `get_count()`.

## Exercise 7: Generator for Primes
Write a generator `primes()` that yields prime numbers infinitely. Use it to get first 10 primes.

## Exercise 8: Memoization
Implement a `@memoize` decorator that caches function results based on arguments.

## Exercise 9: Retry Decorator
Create `@retry(max_attempts=3, delay=1)` that retries a function if it raises an exception.

## Exercise 10: Async Data Fetcher
Write an async function `fetch_all(urls)` that fetches from multiple URLs concurrently using `asyncio.gather`.

## Exercise 11: Function Composition
Write a `compose(*funcs)` function that composes multiple functions: `compose(f, g, h)(x)` = `f(g(h(x)))`.

## Exercise 12: Partial Application
Using `functools.partial`, create specialized versions of a `greet(greeting, name, punctuation)` function.

## Challenge 1: Decorator with Optional Arguments
Create a decorator that can be used both as `@debug` and `@debug(prefix="DEBUG")`.

## Challenge 2: Context Manager Generator
Write a generator-based context manager using `@contextmanager` that times code execution.

## Challenge 3: Async Rate Limiter
Implement an async decorator that limits function calls to N per second.

See solutions.md for answers.
