# Itertools and Functional Tools: Exercise Solutions

## Solution 1: Test Case Generator

```python
from itertools import product

def generate_test_cases():
    """Generate all test case combinations."""
    sizes = ['small', 'medium', 'large']
    colors = ['red', 'blue', 'green']
    enabled = [True, False]

    test_cases = [
        {'size': s, 'color': c, 'enabled': e}
        for s, c, e in product(sizes, colors, enabled)
    ]

    return test_cases

# Test
cases = generate_test_cases()
print(f"Total test cases: {len(cases)}")  # 18
for case in cases[:3]:
    print(case)
# {'size': 'small', 'color': 'red', 'enabled': True}
# {'size': 'small', 'color': 'red', 'enabled': False}
# {'size': 'small', 'color': 'blue', 'enabled': True}
```

## Solution 2: Find Anagrams

```python
from itertools import permutations

def find_anagrams(word, word_list):
    """Find all anagrams of word in word_list."""
    # Generate all permutations
    anagram_set = {''.join(p) for p in permutations(word)}

    # Find matches in word_list
    return [w for w in word_list if w in anagram_set]

# Better solution without generating all permutations
def find_anagrams_efficient(word, word_list):
    """More efficient: compare sorted characters."""
    word_sorted = sorted(word)
    return [w for w in word_list if sorted(w) == word_sorted]

# Test
word_list = ['cat', 'dog', 'act', 'tac', 'god', 'hello']
print(find_anagrams_efficient('cat', word_list))  # ['cat', 'act', 'tac']
```

## Solution 3: Team Generator

```python
from itertools import combinations
from math import comb

def generate_teams(people, team_size):
    """Generate all possible teams."""
    teams = list(combinations(people, team_size))
    count = comb(len(people), team_size)

    return {
        'count': count,
        'teams': teams
    }

# Test
people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
result = generate_teams(people, 3)
print(f"Possible teams: {result['count']}")
for i, team in enumerate(result['teams'], 1):
    print(f"Team {i}: {team}")
```

## Solution 4: Flatten Nested Structure

```python
from itertools import chain

def flatten_nested(nested_list):
    """Recursively flatten nested list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_nested(item))
        else:
            result.append(item)
    return result

# Alternative with generator
def flatten_nested_gen(nested_list):
    """Generator version."""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_nested_gen(item)
        else:
            yield item

# Test
nested = [[1, 2], [3, [4, 5]], [6, 7, [8, 9]]]
print(flatten_nested(nested))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(flatten_nested_gen(nested)))  # Same result
```

## Solution 5: Sales Report

```python
from itertools import groupby
from operator import itemgetter

def monthly_revenue_report(sales):
    """Calculate monthly revenue."""
    # Sort by date first
    sales_sorted = sorted(sales, key=itemgetter('date'))

    # Group by date and calculate revenue
    report = {}
    for date, group in groupby(sales_sorted, key=itemgetter('date')):
        total_revenue = sum(
            item['quantity'] * item['price']
            for item in group
        )
        report[date] = total_revenue

    return report

# Test
sales = [
    {'date': '2024-01', 'product': 'A', 'quantity': 10, 'price': 100},
    {'date': '2024-01', 'product': 'B', 'quantity': 5, 'price': 200},
    {'date': '2024-02', 'product': 'A', 'quantity': 15, 'price': 100},
    {'date': '2024-02', 'product': 'B', 'quantity': 8, 'price': 200},
]

report = monthly_revenue_report(sales)
for month, revenue in report.items():
    print(f"{month}: ${revenue:,}")
# 2024-01: $2,000
# 2024-02: $3,100
```

## Solution 6: Stock Prices

```python
from itertools import accumulate
import operator

def stock_analysis(prices):
    """Analyze stock prices."""
    return {
        'running_max': list(accumulate(prices, max)),
        'running_min': list(accumulate(prices, min)),
        'running_avg': [
            sum(prices[:i+1]) / (i+1)
            for i in range(len(prices))
        ]
    }

# Test
prices = [100, 105, 98, 110, 95, 115, 108]
analysis = stock_analysis(prices)

print("Day | Price | Max   | Min  | Avg")
print("-" * 40)
for i, price in enumerate(prices):
    print(f"{i+1:3} | ${price:3} | ${analysis['running_max'][i]:3} | "
          f"${analysis['running_min'][i]:3} | ${analysis['running_avg'][i]:.2f}")
```

## Solution 7: Fibonacci Generator

```python
from itertools import count, islice

def fibonacci():
    """Infinite Fibonacci generator."""
    a, b = 0, 1
    for _ in count():
        yield a
        a, b = b, a + b

# Test
fib = fibonacci()
print(list(islice(fib, 10)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Alternative using accumulate
from itertools import accumulate

def fibonacci_accumulate():
    """Fibonacci using accumulate."""
    def fib_step(state, _):
        a, b = state
        return b, a + b

    # Start with (0, 1), apply fib_step infinitely
    from itertools import repeat
    fib_states = accumulate(repeat(None), fib_step, initial=(0, 1))
    return (a for a, _ in fib_states)
```

## Solution 8: Password Generator

```python
from itertools import product, islice, chain

def generate_passwords(charset, min_length, max_length, count):
    """Generate passwords of varying lengths."""
    # Generate passwords for each length
    all_passwords = chain.from_iterable(
        (''.join(p) for p in product(charset, repeat=length))
        for length in range(min_length, max_length + 1)
    )

    # Take first count passwords
    return list(islice(all_passwords, count))

# Test
charset = 'ab12'
passwords = generate_passwords(charset, 2, 3, 20)
print(f"Generated {len(passwords)} passwords:")
for i, pwd in enumerate(passwords, 1):
    print(f"{i:2}. {pwd}")
```

## Solution 9: Logger Factory

```python
from functools import partial
from datetime import datetime

def log(level, message, timestamp=True):
    """Base logging function."""
    if timestamp:
        time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{time_str}] [{level}] {message}")
    else:
        print(f"[{level}] {message}")

# Create specialized loggers
info = partial(log, 'INFO')
warning = partial(log, 'WARNING')
error = partial(log, 'ERROR')
debug = partial(log, 'DEBUG', timestamp=False)

# Test
info("Application started")
warning("Low disk space")
error("Connection failed")
debug("Debug message without timestamp")
```

## Solution 10: LRU Cache - API Call

```python
from functools import lru_cache
import time
import random

# Simulate database
_user_database = {
    i: {'id': i, 'name': f'User{i}', 'email': f'user{i}@example.com'}
    for i in range(1000)
}

def get_user_slow(user_id):
    """Slow API call without cache."""
    time.sleep(0.1)  # Simulate network delay
    return _user_database.get(user_id)

@lru_cache(maxsize=100)
def get_user_cached(user_id):
    """Fast API call with cache."""
    time.sleep(0.1)  # Simulate network delay
    return _user_database.get(user_id)

# Test
def benchmark():
    user_ids = [random.randint(1, 50) for _ in range(200)]

    # Without cache
    start = time.time()
    for uid in user_ids:
        get_user_slow(uid)
    slow_time = time.time() - start

    # With cache
    start = time.time()
    for uid in user_ids:
        get_user_cached(uid)
    fast_time = time.time() - start

    print(f"Without cache: {slow_time:.2f}s")
    print(f"With cache: {fast_time:.2f}s")
    print(f"Speedup: {slow_time/fast_time:.2f}x")
    print(f"Cache info: {get_user_cached.cache_info()}")

# benchmark()
```

## Solution 11: Single Dispatch - Type Formatter

```python
from functools import singledispatch

@singledispatch
def format_value(value):
    """Default formatter."""
    return str(value)

@format_value.register(int)
def _(value):
    """Format integer with commas."""
    return f"{value:,}"

@format_value.register(float)
def _(value):
    """Format float to 2 decimal places."""
    return f"{value:.2f}"

@format_value.register(list)
def _(value):
    """Format list as comma-separated string."""
    return ", ".join(str(v) for v in value)

@format_value.register(dict)
def _(value):
    """Format dict as JSON-like string."""
    items = [f'"{k}": {format_value(v)}' for k, v in value.items()]
    return "{" + ", ".join(items) + "}"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@format_value.register(Person)
def _(value):
    """Format Person as 'Name (Age)'."""
    return f"{value.name} ({value.age})"

# Test
print(format_value(1000000))  # "1,000,000"
print(format_value(3.14159))  # "3.14"
print(format_value([1, 2, 3]))  # "1, 2, 3"
print(format_value({'name': 'Alice', 'age': 30}))
print(format_value(Person('Bob', 25)))  # "Bob (25)"
```

## Solution 12: Operator Module - Data Transformation

```python
import operator
from itertools import groupby

data = [
    {'name': 'Alice', 'age': 30, 'salary': 75000, 'dept': 'IT'},
    {'name': 'Bob', 'age': 25, 'salary': 60000, 'dept': 'HR'},
    {'name': 'Charlie', 'age': 35, 'salary': 85000, 'dept': 'IT'},
    {'name': 'David', 'age': 28, 'salary': 70000, 'dept': 'HR'},
]

# Sort by salary (descending) then age
sorted_data = sorted(
    data,
    key=operator.itemgetter('salary', 'age'),
    reverse=True
)

# Extract just names
names = list(map(operator.itemgetter('name'), data))
print(names)  # ['Alice', 'Bob', 'Charlie', 'David']

# Extract multiple fields
name_salary = list(map(
    operator.itemgetter('name', 'salary'),
    data
))
print(name_salary)  # [('Alice', 75000), ...]

# Group by department and calculate average salary
data_sorted = sorted(data, key=operator.itemgetter('dept'))
for dept, group in groupby(data_sorted, key=operator.itemgetter('dept')):
    salaries = list(map(operator.itemgetter('salary'), group))
    avg_salary = sum(salaries) / len(salaries)
    print(f"{dept}: ${avg_salary:,.2f}")
```

## Solution 13: Compress - Apply Mask

```python
from itertools import compress

def apply_mask(data, mask):
    """Apply boolean mask to data."""
    return list(compress(data, mask))

# Test
data = [1, 2, 3, 4, 5]
mask = [True, False, True, False, True]
print(apply_mask(data, mask))  # [1, 3, 5]

# Use case: filter by condition from another list
scores = [85, 92, 78, 95, 88]
passing = [s >= 80 for s in scores]
passing_scores = apply_mask(scores, passing)
print(passing_scores)  # [85, 92, 95, 88]
```

## Solution 14: Log Processing

```python
from itertools import takewhile, dropwhile

logs = [
    {'time': '08:00', 'message': 'Start'},
    {'time': '09:00', 'message': 'Process'},
    {'time': '10:00', 'message': 'Process'},
    {'time': '12:00', 'message': 'Error'},
    {'time': '13:00', 'message': 'Restart'},
    {'time': '14:00', 'message': 'Process'},
]

def is_not_error(log):
    return 'Error' not in log['message']

# Logs before error
before_error = list(takewhile(is_not_error, logs))
print("Before error:")
for log in before_error:
    print(f"  {log['time']}: {log['message']}")

# Logs after error (including error)
after_error = list(dropwhile(is_not_error, logs))
print("\nAfter error:")
for log in after_error:
    print(f"  {log['time']}: {log['message']}")
```

## Solution 15: Zip Longest - Fill Missing Data

```python
from itertools import zip_longest

names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25]
cities = ['NYC']

# Combine with fill value
combined = list(zip_longest(names, ages, cities, fillvalue='Unknown'))
print(combined)
# [('Alice', 30, 'NYC'), ('Bob', 25, 'Unknown'), ('Charlie', 'Unknown', 'Unknown')]

# As list of dictionaries
people = [
    {'name': name, 'age': age, 'city': city}
    for name, age, city in zip_longest(names, ages, cities, fillvalue='Unknown')
]

for person in people:
    print(person)
```

## Challenge 1: Efficient Data Pipeline

```python
from itertools import groupby, islice
from operator import itemgetter
import csv

def process_large_csv(filename):
    """Process large CSV efficiently without loading all data."""
    with open(filename) as f:
        # Read header
        reader = csv.DictReader(f)

        # Filter rows (only active users)
        filtered = (row for row in reader if row.get('status') == 'active')

        # Convert types
        typed = (
            {
                'user_id': row['user_id'],
                'amount': float(row['amount']),
                'date': row['date']
            }
            for row in filtered
        )

        # Group by date (requires materialization for sorting)
        # For truly large files, use external sorting or database
        data_list = list(typed)
        data_sorted = sorted(data_list, key=itemgetter('date'))

        # Calculate daily totals
        result = {}
        for date, group in groupby(data_sorted, key=itemgetter('date')):
            total = sum(item['amount'] for item in group)
            result[date] = total

        return result

# For demonstration
def create_sample_csv():
    """Create sample CSV for testing."""
    with open('sample.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['user_id', 'amount', 'date', 'status'])
        writer.writeheader()
        writer.writerows([
            {'user_id': '1', 'amount': '100.50', 'date': '2024-01-01', 'status': 'active'},
            {'user_id': '2', 'amount': '200.75', 'date': '2024-01-01', 'status': 'active'},
            {'user_id': '3', 'amount': '150.00', 'date': '2024-01-01', 'status': 'inactive'},
            {'user_id': '4', 'amount': '300.25', 'date': '2024-01-02', 'status': 'active'},
        ])
```

## Challenge 2: Pairwise with Overlap

```python
from collections import deque
from itertools import islice

def pairwise_overlap(iterable, n):
    """Create overlapping windows of size n."""
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)

    if len(window) == n:
        yield tuple(window)

    for item in it:
        window.append(item)
        yield tuple(window)

# Test
print(list(pairwise_overlap([1, 2, 3, 4, 5], 2)))
# [(1, 2), (2, 3), (3, 4), (4, 5)]

print(list(pairwise_overlap([1, 2, 3, 4, 5], 3)))
# [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
```

## Challenge 3: Memoization Decorator

```python
from collections import OrderedDict
from functools import wraps

def lru_cache_custom(maxsize=128):
    """Custom LRU cache decorator."""
    def decorator(func):
        cache = OrderedDict()
        hits = misses = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal hits, misses

            # Create cache key
            key = (args, tuple(sorted(kwargs.items())))

            if key in cache:
                # Cache hit - move to end (most recent)
                cache.move_to_end(key)
                hits += 1
                return cache[key]

            # Cache miss
            misses += 1
            result = func(*args, **kwargs)

            # Add to cache
            cache[key] = result

            # Evict oldest if over maxsize
            if len(cache) > maxsize:
                cache.popitem(last=False)

            return result

        def cache_info():
            return f"CacheInfo(hits={hits}, misses={misses}, " \
                   f"maxsize={maxsize}, currsize={len(cache)})"

        def cache_clear():
            nonlocal hits, misses
            cache.clear()
            hits = misses = 0

        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear

        return wrapper
    return decorator

# Test
@lru_cache_custom(maxsize=3)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))
print(fib.cache_info())
```

## Challenge 4: Cartesian Product Filter

```python
from itertools import product

def filtered_product(*iterables, filter_func):
    """Generate Cartesian product with filtering."""
    return (
        item for item in product(*iterables)
        if filter_func(item)
    )

# Test
result = filtered_product(
    [1, 2, 3],
    [1, 2, 3],
    filter_func=lambda t: sum(t) % 2 == 0
)

print(list(result))
# [(1, 1), (1, 3), (2, 2), (3, 1), (3, 3)]
```

## Challenge 5: Advanced GroupBy

```python
from itertools import groupby
from operator import itemgetter
from collections import defaultdict

def group_by_multiple_keys(data, keys):
    """Group by multiple keys, creating nested structure."""
    if not keys:
        return data

    # Sort by all keys
    data_sorted = sorted(data, key=lambda x: [x[k] for k in keys])

    # Group by first key
    first_key = keys[0]
    result = {}

    for key_value, group in groupby(data_sorted, key=itemgetter(first_key)):
        group_list = list(group)

        if len(keys) == 1:
            result[key_value] = group_list
        else:
            # Recursively group by remaining keys
            result[key_value] = group_by_multiple_keys(group_list, keys[1:])

    return result

# Test
data = [
    {'category': 'Electronics', 'region': 'North', 'sales': 100},
    {'category': 'Electronics', 'region': 'South', 'sales': 150},
    {'category': 'Clothing', 'region': 'North', 'sales': 200},
    {'category': 'Clothing', 'region': 'South', 'sales': 175},
    {'category': 'Electronics', 'region': 'North', 'sales': 120},
]

grouped = group_by_multiple_keys(data, ['category', 'region'])

for category, regions in grouped.items():
    print(f"{category}:")
    for region, items in regions.items():
        total = sum(item['sales'] for item in items)
        print(f"  {region}: {len(items)} items, ${total} total")
```

Great work completing these exercises! Check `tips.md` for more patterns and best practices.
