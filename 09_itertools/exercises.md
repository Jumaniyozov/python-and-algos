# Itertools and Functional Tools: Practice Exercises

## Exercise 1: Product - Test Case Generator
Create a function that generates all test cases for a function with multiple parameters:
- Parameters: `size` (small, medium, large), `color` (red, blue, green), `enabled` (True, False)
- Return list of all combinations as dictionaries

## Exercise 2: Permutations - Find Anagrams
Write a function that:
- Takes a word and a list of words
- Returns all words from the list that are anagrams of the input word
- Use permutations to check

## Exercise 3: Combinations - Team Generator
Create a function that:
- Takes a list of n people
- Generates all possible teams of k people
- Returns the number of possible teams and lists them

## Exercise 4: Chain - Flatten Nested Structure
Write a function that flattens a nested list structure:
- Input: `[[1, 2], [3, [4, 5]], [6, 7, [8, 9]]]`
- Output: `[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- Handle arbitrary nesting depth

## Exercise 5: GroupBy - Sales Report
Given sales data:
```python
sales = [
    {'date': '2024-01', 'product': 'A', 'quantity': 10, 'price': 100},
    {'date': '2024-01', 'product': 'B', 'quantity': 5, 'price': 200},
    {'date': '2024-02', 'product': 'A', 'quantity': 15, 'price': 100},
    # ... more data
]
```
Create a function that groups by date and calculates total revenue per month.

## Exercise 6: Accumulate - Stock Prices
Given daily stock prices, create functions that calculate:
- Running maximum price (highest price seen so far)
- Running minimum price (lowest price seen so far)
- Running average price

## Exercise 7: Infinite Iterators - Fibonacci Generator
Create an infinite Fibonacci sequence generator using `count()` and other itertools functions.

## Exercise 8: Multiple Itertools - Password Generator
Create a password generator that:
- Takes charset (letters, digits, special chars)
- Takes minimum length
- Generates all possible passwords up to that length
- Returns first N passwords

## Exercise 9: Partial - Logger Factory
Create a logger factory using `partial()`:
- Base function: `log(level, message, timestamp=True)`
- Create specialized functions: `info()`, `warning()`, `error()`
- Each should have the appropriate level preset

## Exercise 10: LRU Cache - Expensive API Call
Simulate an expensive API call:
- Function takes user_id and returns user data
- Add LRU cache with size 100
- Measure performance improvement

## Exercise 11: Single Dispatch - Type Formatter
Create a `format_value()` function using singledispatch:
- Format `int`: add commas (1000 -> "1,000")
- Format `float`: two decimal places (3.14159 -> "3.14")
- Format `list`: join with ", "
- Format `dict`: JSON-like format
- Format custom `Person` class: "Name (Age)"

## Exercise 12: Operator Module - Data Transformation
Given a list of dictionaries, use operator module to:
- Sort by multiple fields
- Extract specific fields
- Apply transformations

## Exercise 13: Compress - Apply Mask
Write a function that applies a boolean mask to data:
- Input: `data = [1, 2, 3, 4, 5]`, `mask = [True, False, True, False, True]`
- Output: `[1, 3, 5]`
- Use `compress()`

## Exercise 14: Takewhile/Dropwhile - Log Processing
Given log entries with timestamps:
```python
logs = [
    {'time': '08:00', 'message': 'Start'},
    {'time': '09:00', 'message': 'Process'},
    {'time': '12:00', 'message': 'Error'},
    {'time': '13:00', 'message': 'Restart'},
]
```
- Extract logs before first error (takewhile)
- Extract logs after first error (dropwhile)

## Exercise 15: Zip Longest - Fill Missing Data
You have incomplete data across multiple lists:
```python
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25]
cities = ['NYC']
```
Use `zip_longest()` to combine them, filling missing values with "Unknown".

## Challenge 1: Efficient Data Pipeline
Create a data processing pipeline that:
- Reads a large CSV file (don't load all at once)
- Filters rows based on criteria
- Groups by a field
- Calculates aggregates
- All using iterators for memory efficiency

## Challenge 2: Custom Iterator - Pairwise with Overlap
Create a function `pairwise_overlap(iterable, n)`:
- Returns overlapping pairs of n elements
- Example: `pairwise_overlap([1,2,3,4,5], 2)` -> `[(1,2), (2,3), (3,4), (4,5)]`
- Example: `pairwise_overlap([1,2,3,4,5], 3)` -> `[(1,2,3), (2,3,4), (3,4,5)]`

## Challenge 3: Memoization Decorator
Create your own memoization decorator without using functools:
- Implement LRU cache with a maximum size
- Track cache hits and misses
- Provide cache_clear() and cache_info() methods

## Challenge 4: Cartesian Product Filter
Generate Cartesian product but with filtering:
- Input: `product([1, 2, 3], [1, 2, 3])`
- Filter: sum of tuple must be even
- Should be memory efficient (don't generate all then filter)

## Challenge 5: Advanced GroupBy
Create a function that groups by multiple keys:
- Input: list of dictionaries
- Group by `['category', 'region']`
- Return nested dictionary: `{category: {region: [items]}}`
- Use itertools and functools

See `solutions.md` for answers!
