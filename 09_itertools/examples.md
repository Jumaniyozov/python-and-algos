# Itertools and Functional Tools: Examples

## Example 1: Product - Grid Coordinates

```python
from itertools import product

# Generate all coordinates in a 3x3 grid
grid = list(product(range(3), range(3)))
print(grid)
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Chess board coordinates
board = list(product('abcdefgh', '12345678'))
print(board[:5])  # [('a', '1'), ('a', '2'), ('a', '3'), ('a', '4'), ('a', '5')]

# All possible dice rolls (two dice)
dice_rolls = list(product(range(1, 7), repeat=2))
print(len(dice_rolls))  # 36
```

## Example 2: Permutations - Anagram Generator

```python
from itertools import permutations

def all_anagrams(word):
    """Generate all anagrams of a word."""
    return [''.join(p) for p in permutations(word)]

print(all_anagrams('cat'))
# ['cat', 'cta', 'act', 'atc', 'tca', 'tac']

# Partial permutations
def generate_passwords(chars, length):
    """Generate all passwords of given length from chars."""
    return [''.join(p) for p in permutations(chars, length)]

print(generate_passwords('ABC', 2))
# ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']
```

## Example 3: Combinations - Lottery Numbers

```python
from itertools import combinations

def lottery_combinations(n=49, k=6):
    """Generate all possible lottery number combinations."""
    return list(combinations(range(1, n+1), k))

# How many combinations?
from math import comb
print(f"Total combinations: {comb(49, 6):,}")  # 13,983,816

# Generate team pairings
def generate_teams(players, team_size):
    """Generate all possible teams."""
    return list(combinations(players, team_size))

players = ['Alice', 'Bob', 'Charlie', 'David']
teams = generate_teams(players, 2)
print(teams)
# [('Alice', 'Bob'), ('Alice', 'Charlie'), ('Alice', 'David'),
#  ('Bob', 'Charlie'), ('Bob', 'David'), ('Charlie', 'David')]
```

## Example 4: Chain - Flattening Lists

```python
from itertools import chain

# Combine multiple lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

combined = list(chain(list1, list2, list3))
print(combined)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Flatten nested lists
nested = [[1, 2], [3, 4, 5], [6]]
flat = list(chain.from_iterable(nested))
print(flat)  # [1, 2, 3, 4, 5, 6]

# Read from multiple files
def read_multiple_files(filenames):
    """Read lines from multiple files as single stream."""
    from pathlib import Path
    return chain.from_iterable(
        Path(f).read_text().splitlines()
        for f in filenames
    )
```

## Example 5: GroupBy - Data Grouping

```python
from itertools import groupby

# Group by first letter
words = ['apple', 'apricot', 'banana', 'cherry', 'coconut']
words_sorted = sorted(words)  # MUST be sorted first!

for letter, group in groupby(words_sorted, key=lambda x: x[0]):
    print(f"{letter}: {list(group)}")
# a: ['apple', 'apricot']
# b: ['banana']
# c: ['cherry', 'coconut']

# Group students by grade
students = [
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'},
    {'name': 'Charlie', 'grade': 'A'},
    {'name': 'David', 'grade': 'B'},
]

students_sorted = sorted(students, key=lambda s: s['grade'])
for grade, group in groupby(students_sorted, key=lambda s: s['grade']):
    names = [s['name'] for s in group]
    print(f"Grade {grade}: {names}")
# Grade A: ['Alice', 'Charlie']
# Grade B: ['Bob', 'David']

# Count consecutive duplicates
data = [1, 1, 2, 2, 2, 3, 1, 1]
counts = [(key, len(list(group))) for key, group in groupby(data)]
print(counts)  # [(1, 2), (2, 3), (3, 1), (1, 2)]
```

## Example 6: Accumulate - Running Calculations

```python
from itertools import accumulate
import operator

# Running sum
data = [1, 2, 3, 4, 5]
print(list(accumulate(data)))  # [1, 3, 6, 10, 15]

# Running product (factorial sequence)
print(list(accumulate(data, operator.mul)))  # [1, 2, 6, 24, 120]

# Running maximum
prices = [100, 105, 98, 110, 95, 115]
print(list(accumulate(prices, max)))  # [100, 105, 105, 110, 110, 115]

# Compound interest calculator
def compound_interest(principal, rate, years):
    """Calculate compound interest over time."""
    multiplier = 1 + rate
    return list(accumulate([principal] + [multiplier] * years, operator.mul))

balance = compound_interest(1000, 0.05, 10)
for year, amount in enumerate(balance):
    print(f"Year {year}: ${amount:.2f}")
```

## Example 7: Infinite Iterators - Cyclic Patterns

```python
from itertools import cycle, count, repeat, islice

# Round-robin task assignment
tasks = ['Task A', 'Task B', 'Task C', 'Task D', 'Task E']
workers = cycle(['Alice', 'Bob', 'Charlie'])

assignments = [(task, next(workers)) for task in tasks]
print(assignments)
# [('Task A', 'Alice'), ('Task B', 'Bob'), ('Task C', 'Charlie'),
#  ('Task D', 'Alice'), ('Task E', 'Bob')]

# Alternating colors
colors = cycle(['red', 'blue', 'green'])
rows = [{'id': i, 'color': next(colors)} for i in range(10)]

# Countdown
countdown = count(10, -1)
print(list(islice(countdown, 11)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Create fixed-length iterator
default_values = list(islice(repeat('N/A'), 5))
print(default_values)  # ['N/A', 'N/A', 'N/A', 'N/A', 'N/A']
```

## Example 8: Combining Itertools - Complex Queries

```python
from itertools import chain, combinations, permutations

def generate_subsets(items):
    """Generate all subsets (power set)."""
    return chain.from_iterable(
        combinations(items, r) for r in range(len(items) + 1)
    )

subsets = list(generate_subsets([1, 2, 3]))
print(subsets)
# [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

# Generate all possible strings from pattern
def expand_pattern(pattern):
    """
    Expand pattern with alternatives.
    'a{1,2}b' -> ['a1b', 'a2b']
    """
    # Simplified example
    options = [['a', 'b'], ['1', '2', '3'], ['x', 'y']]
    return [''.join(combo) for combo in product(*options)]
```

## Example 9: Functools - Partial Application

```python
from functools import partial

# Create specialized sorting functions
def sort_by_field(data, field, reverse=False):
    return sorted(data, key=lambda x: x[field], reverse=reverse)

users = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# Create specialized functions
sort_by_age = partial(sort_by_field, field='age')
sort_by_name = partial(sort_by_field, field='name')
sort_by_age_desc = partial(sort_by_field, field='age', reverse=True)

print(sort_by_age(users))
print(sort_by_name(users))
print(sort_by_age_desc(users))

# Configuration functions
def connect_db(host, port, user, password):
    return f"Connected to {user}@{host}:{port}"

# Development database
dev_db = partial(connect_db, host='localhost', port=5432)
prod_db = partial(connect_db, host='prod.example.com', port=5432)

print(dev_db(user='admin', password='secret'))
print(prod_db(user='admin', password='secret'))
```

## Example 10: Functools - Caching

```python
from functools import cache, lru_cache
import time

# Fibonacci with caching
@cache
def fib(n):
    """Fibonacci with unbounded cache."""
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

start = time.time()
print(fib(100))
print(f"Time: {time.time() - start:.4f}s")  # Fast!

# LRU cache with size limit
@lru_cache(maxsize=100)
def expensive_computation(x, y):
    """Simulate expensive computation."""
    time.sleep(0.1)  # Simulate work
    return x ** y

# First call is slow
print(expensive_computation(2, 10))  # Takes 0.1s

# Cached call is instant
print(expensive_computation(2, 10))  # Instant!

# Check cache statistics
print(expensive_computation.cache_info())
# CacheInfo(hits=1, misses=1, maxsize=100, currsize=1)

# Clear cache when needed
expensive_computation.cache_clear()
```

## Example 11: Functools - Single Dispatch

```python
from functools import singledispatch
import json

@singledispatch
def serialize(data):
    """Serialize data to JSON string."""
    return json.dumps(data)

@serialize.register(list)
def _(data):
    """Serialize list with custom formatting."""
    return json.dumps(data, indent=2)

@serialize.register(dict)
def _(data):
    """Serialize dict with sorted keys."""
    return json.dumps(data, sort_keys=True, indent=2)

@serialize.register(set)
def _(data):
    """Serialize set as sorted list."""
    return json.dumps(sorted(data))

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@serialize.register(User)
def _(data):
    """Serialize User object."""
    return json.dumps({'name': data.name, 'age': data.age})

# Usage
print(serialize([1, 2, 3]))
print(serialize({'name': 'Alice', 'age': 30}))
print(serialize({1, 2, 3}))
print(serialize(User('Bob', 25)))
```

## Example 12: Operator Module

```python
import operator
from itertools import groupby

# Sorting with itemgetter
students = [
    ('Alice', 85, 'A'),
    ('Bob', 75, 'B'),
    ('Charlie', 90, 'A'),
    ('David', 75, 'B')
]

# Sort by grade (index 1)
by_grade = sorted(students, key=operator.itemgetter(1))
print(by_grade)

# Sort by multiple fields (grade, then name)
by_grade_name = sorted(students, key=operator.itemgetter(1, 0))
print(by_grade_name)

# Sorting objects by attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Person({self.name}, {self.age})"

people = [Person('Alice', 30), Person('Bob', 25), Person('Charlie', 35)]
by_age = sorted(people, key=operator.attrgetter('age'))
print(by_age)

# Method caller
words = ['hello', 'WORLD', 'Python']
upper_words = list(map(operator.methodcaller('upper'), words))
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# Split with arguments
texts = ['a,b,c', 'd,e,f']
split_texts = list(map(operator.methodcaller('split', ','), texts))
print(split_texts)  # [['a', 'b', 'c'], ['d', 'e', 'f']]
```

## Example 13: Efficient Data Processing Pipeline

```python
from itertools import islice, takewhile, dropwhile, chain
from functools import reduce
import operator

# Process large dataset efficiently
def process_data(filename):
    """Process data file without loading entire file."""
    with open(filename) as f:
        # Skip header
        lines = islice(f, 1, None)

        # Parse and filter
        data = (line.strip().split(',') for line in lines)
        data = ((int(row[0]), float(row[1])) for row in data)

        # Take while condition is met
        valid_data = takewhile(lambda x: x[0] < 1000, data)

        # Process
        total = sum(value for _, value in valid_data)
        return total

# Chaining operations
numbers = range(100)

result = (
    n for n in numbers
    if n % 2 == 0  # Filter evens
)
result = (n ** 2 for n in result)  # Square
result = (n for n in result if n > 100)  # Filter > 100

print(list(islice(result, 10)))
```

## Example 14: Real-World Use Case - Data Analysis

```python
from itertools import groupby, chain
from functools import reduce
from operator import itemgetter
import statistics

# Sales data
sales = [
    {'date': '2024-01-01', 'product': 'A', 'amount': 100},
    {'date': '2024-01-01', 'product': 'B', 'amount': 150},
    {'date': '2024-01-02', 'product': 'A', 'amount': 120},
    {'date': '2024-01-02', 'product': 'B', 'amount': 130},
    {'date': '2024-01-03', 'product': 'A', 'amount': 110},
]

# Group by date and calculate daily totals
sales_by_date = sorted(sales, key=itemgetter('date'))
daily_totals = {
    date: sum(s['amount'] for s in group)
    for date, group in groupby(sales_by_date, key=itemgetter('date'))
}
print(daily_totals)

# Group by product and calculate stats
sales_by_product = sorted(sales, key=itemgetter('product'))
product_stats = {
    product: {
        'total': sum(s['amount'] for s in group_list),
        'average': statistics.mean(s['amount'] for s in group_list),
        'count': len(group_list)
    }
    for product, group in groupby(sales_by_product, key=itemgetter('product'))
    for group_list in [list(group)]  # Consume group once
}
print(product_stats)
```

## Example 15: Custom Iterator Patterns

```python
from itertools import islice, count, takewhile

def batched(iterable, n):
    """Batch iterable into chunks of size n."""
    it = iter(iterable)
    while batch := list(islice(it, n)):
        yield batch

# Usage
for batch in batched(range(10), 3):
    print(batch)
# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]
# [9]

def windowed(iterable, n):
    """Create sliding window of size n."""
    from collections import deque
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for item in it:
        window.append(item)
        yield tuple(window)

# Usage
for window in windowed([1, 2, 3, 4, 5], 3):
    print(window)
# (1, 2, 3)
# (2, 3, 4)
# (3, 4, 5)

def take(n, iterable):
    """Return first n items of iterable."""
    return list(islice(iterable, n))

def nth(iterable, n, default=None):
    """Return nth item of iterable or default."""
    return next(islice(iterable, n, None), default)

# Usage
print(take(5, count()))  # [0, 1, 2, 3, 4]
print(nth(count(), 10))  # 10
```

See `exercises.md` for practice problems!
