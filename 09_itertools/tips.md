# Itertools and Functional Tools: Tips and Best Practices

## General Tips

### 1. Always Limit Infinite Iterators

```python
from itertools import count, cycle, islice

# BAD - This will run forever!
# for i in count():
#     print(i)

# GOOD - Use islice or break condition
for i in islice(count(), 10):
    print(i)

# GOOD - Use with zip (stops at shortest)
for i, letter in zip(count(), 'abc'):
    print(f"{i}: {letter}")  # 0: a, 1: b, 2: c
```

### 2. Sort Before groupby()

```python
from itertools import groupby

# WRONG - Won't group correctly!
data = ['apple', 'banana', 'apricot', 'cherry']
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# a ['apple']
# b ['banana']
# a ['apricot']  # Separate group!
# c ['cherry']

# CORRECT - Sort first
data_sorted = sorted(data, key=lambda x: x[0])
for key, group in groupby(data_sorted, key=lambda x: x[0]):
    print(key, list(group))
# a ['apple', 'apricot']
# b ['banana']
# c ['cherry']
```

### 3. Consume Groups Immediately or Convert to List

```python
from itertools import groupby

data = [1, 1, 2, 2, 2, 3]

# WRONG - Group iterator is exhausted after first iteration
groups = {k: g for k, g in groupby(data)}
for key, group in groups.items():
    print(key, list(group))  # Empty lists!

# CORRECT - Convert to list immediately
groups = {k: list(g) for k, g in groupby(data)}
for key, group in groups.items():
    print(key, group)  # Works!
```

### 4. Use Generator Expressions with Itertools

```python
from itertools import islice

# Memory efficient - only generates what's needed
squares = (x**2 for x in range(1000000))
first_ten = list(islice(squares, 10))

# Don't create unnecessary lists
# BAD
numbers = [x for x in range(1000000)]
squares = [x**2 for x in numbers]

# GOOD
numbers = range(1000000)
squares = (x**2 for x in numbers)
```

## Performance Tips

### 5. Use Built-ins When Available

```python
from functools import reduce
import operator

# For sum, use built-in
# BAD
total = reduce(operator.add, numbers)

# GOOD
total = sum(numbers)

# For product, use math.prod (Python 3.8+)
import math
# BAD
product = reduce(operator.mul, numbers)

# GOOD
product = math.prod(numbers)

# For max/min, use built-ins
# BAD
maximum = reduce(max, numbers)

# GOOD
maximum = max(numbers)
```

### 6. Prefer itertools Over Manual Loops

```python
from itertools import chain, product

# BAD - Nested loops
result = []
for i in range(3):
    for j in range(3):
        result.append((i, j))

# GOOD - product
result = list(product(range(3), range(3)))

# BAD - Manual flattening
result = []
for sublist in nested_lists:
    for item in sublist:
        result.append(item)

# GOOD - chain
result = list(chain.from_iterable(nested_lists))
```

### 7. Use accumulate for Running Calculations

```python
from itertools import accumulate
import operator

data = [1, 2, 3, 4, 5]

# BAD - Manual calculation
running_sum = []
total = 0
for x in data:
    total += x
    running_sum.append(total)

# GOOD - accumulate
running_sum = list(accumulate(data))

# BAD - Manual running maximum
running_max = []
max_val = float('-inf')
for x in data:
    max_val = max(max_val, x)
    running_max.append(max_val)

# GOOD - accumulate with max
running_max = list(accumulate(data, max))
```

## Caching Tips

### 8. Know When to Use @cache vs @lru_cache

```python
from functools import cache, lru_cache

# Use @cache for:
# - Small to medium input spaces
# - When you want unlimited caching
# - Pure functions with hashable arguments

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Use @lru_cache when:
# - Large input space (prevents memory issues)
# - Need control over cache size
# - Want cache statistics

@lru_cache(maxsize=128)
def expensive_api_call(user_id):
    # ...
    pass
```

### 9. Don't Cache Functions with Side Effects

```python
from functools import cache

# BAD - Side effects shouldn't be cached
@cache
def log_and_compute(x):
    print(f"Computing {x}")  # Side effect!
    return x ** 2

log_and_compute(5)  # Prints "Computing 5"
log_and_compute(5)  # Doesn't print (cached)

# GOOD - Separate side effects from pure computation
def compute(x):
    return x ** 2

@cache
def cached_compute(x):
    return compute(x)

def log_and_compute(x):
    print(f"Computing {x}")
    return cached_compute(x)
```

### 10. Clear Caches When Needed

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_config(key):
    # Read from config file
    pass

# When config file changes:
get_config.cache_clear()

# Check cache statistics
info = get_config.cache_info()
print(f"Hits: {info.hits}, Misses: {info.misses}")
print(f"Hit rate: {info.hits / (info.hits + info.misses):.2%}")
```

## Common Patterns

### 11. Pairwise Iteration

```python
from itertools import pairwise  # Python 3.10+

# For adjacent pairs
data = [1, 2, 3, 4, 5]
for a, b in pairwise(data):
    print(f"{a} -> {b}")
# 1 -> 2
# 2 -> 3
# 3 -> 4
# 4 -> 5

# Python < 3.10
def pairwise_old(iterable):
    a, b = iter(iterable), iter(iterable)
    next(b, None)
    return zip(a, b)
```

### 12. Chunking Data

```python
from itertools import islice

def chunked(iterable, n):
    """Break iterable into chunks of size n."""
    it = iter(iterable)
    while chunk := list(islice(it, n)):
        yield chunk

# Usage
for chunk in chunked(range(10), 3):
    process(chunk)
```

### 13. Flatten with Different Depths

```python
from itertools import chain

# Flatten one level
nested = [[1, 2], [3, 4], [5]]
flat = list(chain.from_iterable(nested))

# Flatten any depth recursively
def deep_flatten(nested):
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from deep_flatten(item)
        else:
            yield item
```

### 14. Round-Robin from Multiple Iterables

```python
from itertools import cycle, islice

def roundrobin(*iterables):
    """roundrobin('ABC', 'D', 'EF') → A D E B F C"""
    num_active = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next_func in nexts:
                yield next_func()
        except StopIteration:
            num_active -= 1
            nexts = cycle(islice(nexts, num_active))
```

### 15. Take While and Drop While

```python
from itertools import takewhile, dropwhile

data = [1, 4, 6, 4, 1]

# Take until condition fails
small = list(takewhile(lambda x: x < 5, data))  # [1, 4]

# Drop until condition fails, then take all
rest = list(dropwhile(lambda x: x < 5, data))  # [6, 4, 1]

# Combined: split at first element where condition fails
def split_at(iterable, predicate):
    it = iter(iterable)
    before = list(takewhile(predicate, it))
    after = list(it)  # Remaining elements
    return before, after
```

## Operator Module Tips

### 16. Use itemgetter for Sorting

```python
import operator

data = [
    ('Alice', 30, 'NYC'),
    ('Bob', 25, 'LA'),
    ('Charlie', 30, 'NYC'),
]

# Sort by second element (age)
by_age = sorted(data, key=operator.itemgetter(1))

# Sort by multiple fields (age, then name)
by_age_name = sorted(data, key=operator.itemgetter(1, 0))

# More efficient than lambda
# LESS EFFICIENT
sorted(data, key=lambda x: x[1])

# MORE EFFICIENT
sorted(data, key=operator.itemgetter(1))
```

### 17. Use attrgetter for Object Attributes

```python
import operator

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person('Alice', 30), Person('Bob', 25)]

# Sort by attribute
by_age = sorted(people, key=operator.attrgetter('age'))

# Multiple attributes
by_age_name = sorted(people, key=operator.attrgetter('age', 'name'))
```

### 18. Use methodcaller to Call Methods

```python
import operator

# Apply method to all items
words = ['hello', 'world', 'python']
upper_words = list(map(operator.methodcaller('upper'), words))

# Method with arguments
texts = ['a,b,c', 'd,e,f']
split_texts = list(map(operator.methodcaller('split', ','), texts))

# More efficient than lambda
# LESS EFFICIENT
list(map(lambda x: x.upper(), words))

# MORE EFFICIENT
list(map(operator.methodcaller('upper'), words))
```

## Gotchas and Common Mistakes

### 19. Don't Reuse Iterators

```python
from itertools import product

# WRONG - Iterator is exhausted after first use
prod = product([1, 2], [3, 4])
print(list(prod))  # [(1, 3), (1, 4), (2, 3), (2, 4)]
print(list(prod))  # [] - Empty!

# CORRECT - Create new iterator or convert to list
prod = list(product([1, 2], [3, 4]))
print(prod)  # Works multiple times
print(prod)  # Still works
```

### 20. Watch Out for Memory with Large Combinations

```python
from itertools import combinations, islice

# BAD - Tries to create huge list
# large_list = list(combinations(range(1000), 500))  # Out of memory!

# GOOD - Take only what you need
first_few = list(islice(combinations(range(1000), 500), 10))

# Or process one at a time
for combo in islice(combinations(range(1000), 500), 100):
    process(combo)
```

### 21. Be Careful with Mutable Default Arguments

```python
from functools import partial

# BAD - Mutable default is shared!
def append_to(item, list_arg=[]):
    list_arg.append(item)
    return list_arg

# GOOD - Use None and create new list
def append_to(item, list_arg=None):
    if list_arg is None:
        list_arg = []
    list_arg.append(item)
    return list_arg
```

## Advanced Patterns

### 22. Efficient Windowing

```python
from collections import deque
from itertools import islice

def sliding_window(iterable, n):
    """Memory-efficient sliding window."""
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for item in it:
        window.append(item)
        yield tuple(window)

# Usage: process data in windows
data = range(1000000)  # Large dataset
for window in sliding_window(data, 3):
    # Process window
    pass
```

### 23. Efficient Grouping Without Sorting

```python
from collections import defaultdict

# When you can't sort (streaming data or too large):
def group_without_sort(iterable, key_func):
    """Group items without sorting."""
    groups = defaultdict(list)
    for item in iterable:
        groups[key_func(item)].append(item)
    return dict(groups)

# Usage
data = [{'name': 'Alice', 'dept': 'IT'}, ...]
grouped = group_without_sort(data, lambda x: x['dept'])
```

### 24. Infinite Retry with Backoff

```python
from itertools import count
import time

def retry_with_backoff(func, max_retries=5, base_delay=1):
    """Retry function with exponential backoff."""
    for attempt in count():
        try:
            return func()
        except Exception as e:
            if attempt >= max_retries:
                raise
            delay = base_delay * (2 ** attempt)
            print(f"Retry {attempt + 1} after {delay}s")
            time.sleep(delay)
```

### 25. Efficient Data Pipeline

```python
from itertools import islice, chain

def process_pipeline(data):
    """Chain multiple processing steps efficiently."""
    # Step 1: Filter
    filtered = (x for x in data if x > 0)

    # Step 2: Transform
    transformed = (x ** 2 for x in filtered)

    # Step 3: Take top N
    top_n = islice(transformed, 100)

    # All done lazily - no intermediate lists!
    return list(top_n)
```

## Summary of Best Practices

1. **Always limit infinite iterators** with `islice()` or loop conditions
2. **Sort before `groupby()`** for correct grouping
3. **Consume groups immediately** or convert to list
4. **Use generator expressions** for memory efficiency
5. **Prefer built-in functions** over `reduce()` when available
6. **Use `@cache` for unlimited caching**, `@lru_cache` for bounded
7. **Don't cache functions with side effects**
8. **Use `operator` module** instead of lambdas for better performance
9. **Don't reuse iterators** - they're one-time use
10. **Watch memory** with large combinatorics
11. **Use `itemgetter/attrgetter/methodcaller`** for efficiency
12. **Clear caches** when underlying data changes
13. **Process data lazily** when possible
14. **Chain operations** for efficient pipelines
15. **Use `partial()` for configuration** and specialized functions

## Performance Comparison

```python
import time
from itertools import product, chain
import operator

def benchmark():
    data = range(1000)

    # List comprehension vs generator
    start = time.time()
    list_comp = [x**2 for x in data]
    list_time = time.time() - start

    start = time.time()
    gen_exp = (x**2 for x in data)
    list(gen_exp)  # Consume it
    gen_time = time.time() - start

    # Lambda vs operator
    pairs = [(1, 2), (3, 4), (5, 6)]

    start = time.time()
    for _ in range(10000):
        sorted(pairs, key=lambda x: x[1])
    lambda_time = time.time() - start

    start = time.time()
    for _ in range(10000):
        sorted(pairs, key=operator.itemgetter(1))
    operator_time = time.time() - start

    print(f"List comprehension: {list_time:.4f}s")
    print(f"Generator expression: {gen_time:.4f}s")
    print(f"Lambda sorting: {lambda_time:.4f}s")
    print(f"Operator sorting: {operator_time:.4f}s")
```

Remember: **Measure, don't guess!** Always profile your code to see what actually matters for performance.
