# Exercises: Generators & Iterators

## Exercise 1: Range Iterator (Easy)
Implement a custom `Range` iterator class that mimics Python's built-in `range()`.

**Requirements:**
- Support `start`, `stop`, and `step` parameters
- Implement `__iter__` and `__next__`
- Handle negative steps
- Raise `StopIteration` appropriately

## Exercise 2: Prime Number Generator (Easy)
Create a generator function that yields prime numbers up to a given limit.

**Example:**
```python
for prime in primes(20):
    print(prime)  # 2, 3, 5, 7, 11, 13, 17, 19
```

## Exercise 3: File Line Counter (Easy)
Write a generator that yields line numbers and content for non-empty lines in a file.

**Output format:** `(line_number, line_content)`

## Exercise 4: Moving Average (Medium)
Implement a generator that calculates moving average over a sliding window.

**Example:**
```python
data = [1, 2, 3, 4, 5, 6, 7, 8]
for avg in moving_average(data, window=3):
    print(avg)  # 2.0, 3.0, 4.0, 5.0, 6.0, 7.0
```

## Exercise 5: Permutations Generator (Medium)
Create a generator that yields all permutations of a list without using `itertools`.

## Exercise 6: Merge Sorted Iterables (Medium)
Write a generator that merges multiple sorted iterables into a single sorted sequence.

**Example:**
```python
a = [1, 4, 7]
b = [2, 5, 8]
c = [3, 6, 9]
list(merge(a, b, c))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Exercise 7: Coroutine Log Processor (Medium)
Build a coroutine that processes log entries and categorizes them by level (INFO, WARNING, ERROR).

**Use send() to send log entries.**

## Exercise 8: Flatten Nested Structure (Medium)
Create a generator that flattens arbitrarily nested lists, tuples, and sets.

**Example:**
```python
nested = [1, [2, (3, 4)], {5, 6}, [[7]]]
list(flatten(nested))  # [1, 2, 3, 4, 5, 6, 7]
```

## Exercise 9: Lazy JSON Parser (Hard)
Implement a generator-based JSON array parser that yields objects one at a time without loading the entire file.

**For a JSON array like:** `[{...}, {...}, ...]`

## Exercise 10: Generator Pipeline Framework (Hard)
Build a framework for creating data processing pipelines using decorators.

**Requirements:**
- `@source` decorator for data sources
- `@filter` decorator for filtering
- `@transform` decorator for transformations
- `@sink` decorator for output
- Composable pipeline

## Exercise 11: Paginated API Client (Medium)
Create a generator that fetches all pages from a paginated API.

**Requirements:**
- Yield individual items, not pages
- Handle rate limiting
- Support different pagination styles (page number, cursor)

## Exercise 12: Generator-based Lexer (Hard)
Implement a simple lexer/tokenizer as a generator that yields tokens from source code.

**Token types:** Identifier, Number, Operator, Keyword, Whitespace

## Exercise 13: Circular Buffer Generator (Medium)
Implement a circular buffer as a generator that maintains a fixed-size window.

**Use send() to add items and yield oldest when buffer is full.**

## Exercise 14: Tree Walker with Control (Hard)
Create a tree walker generator that allows controlling traversal (skip subtree, stop traversal).

**Use send() for control signals:**
- `'skip'`: Skip current subtree
- `'stop'`: Stop traversal
- `None`: Continue normally

## Exercise 15: Async Web Scraper (Hard)
Build an async generator that scrapes multiple URLs concurrently and yields results as they complete.

**Requirements:**
- Use aiohttp for async HTTP requests
- Handle errors gracefully
- Limit concurrent requests
- Yield results in completion order

## Bonus: Generator-based State Machine

Implement a complex state machine (e.g., traffic light controller) using generators with `send()` for state transitions.

## Testing Guidelines

For each solution:
1. Test with edge cases (empty input, single item, large datasets)
2. Verify memory efficiency using `sys.getsizeof()` or memory profilers
3. Check that generators are lazy (don't compute all at once)
4. Test exception handling
5. Measure performance against non-generator alternatives

## Hints

- **Exercise 1**: Remember to handle all three range() formats
- **Exercise 2**: Use a sieve or trial division algorithm
- **Exercise 4**: Use `collections.deque` with `maxlen`
- **Exercise 5**: Think recursively
- **Exercise 6**: Use a heap for efficiency
- **Exercise 9**: Parse streaming JSON, handle nested structures
- **Exercise 10**: Study how decorators can wrap generators
- **Exercise 12**: Use regular expressions or character-by-character parsing
- **Exercise 13**: Circular buffer naturally fits generator patterns
- **Exercise 14**: Use tuples to communicate both value and control signals
