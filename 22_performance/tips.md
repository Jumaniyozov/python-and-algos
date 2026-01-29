# Tips & Best Practices: Performance Optimization

## Best Practices

### Tip 1: Profile Before Optimizing

Never guess where the bottleneck is. Always profile first.

```python
import cProfile
import pstats
from pstats import SortKey

def my_function():
    # Your code here
    pass

# Profile the code
profiler = cProfile.Profile()
profiler.enable()
my_function()
profiler.disable()

# Print results
stats = pstats.Stats(profiler)
stats.sort_stats(SortKey.CUMULATIVE)
stats.print_stats(10)  # Top 10 slowest functions
```

**Why**: 90% of execution time is spent in 10% of the code. Find that 10% first.

### Tip 2: Use the Right Data Structure

Choose data structures based on operations you'll perform most.

```python
# BAD: List for membership testing
def check_membership_slow(items, search_terms):
    seen = []
    for item in items:
        if item not in seen:  # O(n) lookup!
            seen.append(item)
    return seen

# GOOD: Set for membership testing
def check_membership_fast(items, search_terms):
    return set(items)  # O(1) lookup

# Data structure comparison:
# Operation       List      Set       Dict
# Lookup          O(n)      O(1)      O(1)
# Insert          O(1)*     O(1)      O(1)
# Delete          O(n)      O(1)      O(1)
# Iteration       O(n)      O(n)      O(n)
# *Append is O(1), insert at position is O(n)
```

### Tip 3: Avoid Premature Optimization

Write clear code first, optimize only when needed.

```python
# FIRST: Write clear, correct code
def calculate_total(items):
    """Clear and readable."""
    return sum(item.price * item.quantity for item in items)

# ONLY OPTIMIZE IF profiling shows this is a bottleneck
def calculate_total_optimized(items):
    """Optimized after profiling showed bottleneck."""
    total = 0
    for item in items:
        total += item.price * item.quantity  # Avoid generator overhead
    return total
```

**Rule**: Make it work, make it right, make it fast (in that order).

### Tip 4: Cache Expensive Operations

Use memoization for expensive, repeated calculations.

```python
from functools import lru_cache
import time

# Without cache - slow
def fibonacci_slow(n):
    if n < 2:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)

# With cache - fast
@lru_cache(maxsize=None)
def fibonacci_fast(n):
    if n < 2:
        return n
    return fibonacci_fast(n-1) + fibonacci_fast(n-2)

# fibonacci_slow(35) takes ~5 seconds
# fibonacci_fast(35) takes ~0.0001 seconds

# Clear cache when needed
fibonacci_fast.cache_clear()

# Check cache statistics
print(fibonacci_fast.cache_info())
# CacheInfo(hits=33, misses=36, maxsize=None, currsize=36)
```

**When to cache**:
- Function is pure (same input = same output)
- Function is expensive
- Function is called repeatedly
- Limited number of unique inputs

### Tip 5: Use Generators for Large Data

Generators process data lazily, saving memory.

```python
# BAD: Loads all data into memory
def process_large_file_bad(filename):
    with open(filename) as f:
        lines = f.readlines()  # Loads entire file!
    return [line.strip().upper() for line in lines]

# GOOD: Processes line by line
def process_large_file_good(filename):
    with open(filename) as f:
        for line in f:  # Iterates one line at a time
            yield line.strip().upper()

# Use it
for processed_line in process_large_file_good('huge_file.txt'):
    print(processed_line)

# Generator expressions for pipelines
data = range(1000000)
pipeline = (
    x for x in data
    if x % 2 == 0  # Filter
)
pipeline = (x ** 2 for x in pipeline)  # Transform
result = sum(pipeline)  # Aggregate
```

### Tip 6: Batch Operations

Group operations to reduce overhead.

```python
import time

# BAD: Individual database commits
def save_items_slow(items, db):
    for item in items:
        db.insert(item)
        db.commit()  # Expensive!
    # 100 items = 100 commits

# GOOD: Batch commit
def save_items_fast(items, db):
    for item in items:
        db.insert(item)
    db.commit()  # Once!
    # 100 items = 1 commit

# BAD: Individual API calls
def fetch_users_slow(user_ids, api):
    users = []
    for user_id in user_ids:
        users.append(api.get_user(user_id))  # 100 API calls
    return users

# GOOD: Batch API call
def fetch_users_fast(user_ids, api):
    return api.get_users_batch(user_ids)  # 1 API call
```

### Tip 7: Use Local Variables

Local variable lookups are faster than global or attribute lookups.

```python
import math

# SLOWER: Global lookup
def calculate_slow(values):
    return [math.sqrt(x) for x in values]

# FASTER: Local variable
def calculate_fast(values):
    sqrt = math.sqrt  # Cache in local variable
    return [sqrt(x) for x in values]

# SLOWER: Attribute lookup in loop
class Calculator:
    def process_slow(self, values):
        result = []
        for x in values:
            result.append(self.helper(x))  # Attribute lookup each time
        return result

    def helper(self, x):
        return x ** 2

# FASTER: Cache method reference
class Calculator:
    def process_fast(self, values):
        helper = self.helper  # Cache method
        result = []
        for x in values:
            result.append(helper(x))
        return result

    def helper(self, x):
        return x ** 2
```

### Tip 8: Avoid Global Lookups

Global variable access is slower than local.

```python
# Global variable
MULTIPLIER = 10

# SLOWER
def process_slow(values):
    return [x * MULTIPLIER for x in values]  # Global lookup

# FASTER
def process_fast(values, multiplier=MULTIPLIER):
    return [x * multiplier for x in values]  # Local lookup

# Even better for large datasets
def process_fastest(values):
    mult = MULTIPLIER  # Cache as local
    return [x * mult for x in values]
```

### Tip 9: Pre-compile Regular Expressions

Compile regex patterns once, use many times.

```python
import re

# BAD: Compile in loop
def validate_emails_slow(emails):
    valid = []
    for email in emails:
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):  # Compiles each time!
            valid.append(email)
    return valid

# GOOD: Compile once
EMAIL_PATTERN = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

def validate_emails_fast(emails):
    valid = []
    for email in emails:
        if EMAIL_PATTERN.match(email):  # Uses pre-compiled pattern
            valid.append(email)
    return valid

# Even better with filter
def validate_emails_fastest(emails):
    return list(filter(EMAIL_PATTERN.match, emails))
```

### Tip 10: Use __slots__ for Classes

Reduce memory usage for classes with fixed attributes.

```python
# Without __slots__: Uses __dict__ (more memory)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# With __slots__: Fixed attributes (less memory)
class PointOptimized:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Memory comparison for 1 million points:
# Point: ~240 MB
# PointOptimized: ~160 MB (33% less!)

# Trade-off: Can't add new attributes dynamically
p = PointOptimized(1, 2)
# p.z = 3  # AttributeError!
```

### Tip 11: Use Built-in Functions

Built-in functions are implemented in C and are very fast.

```python
# SLOWER: Manual implementation
def sum_slow(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# FASTER: Built-in function
def sum_fast(numbers):
    return sum(numbers)

# More examples:
# Bad                          Good
# -------------------------    -------------------------
# manual max/min               max(items), min(items)
# manual any/all               any(items), all(items)
# manual sorting               sorted(items)
# manual reversal              reversed(items)
# loop with enumerate counter  enumerate(items)
# manual zip                   zip(list1, list2)
```

### Tip 12: List Comprehensions Over Loops

List comprehensions are faster than equivalent for loops.

```python
import timeit

# SLOWER: For loop
def squares_loop(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# FASTER: List comprehension (15-30% faster)
def squares_comprehension(n):
    return [i ** 2 for i in range(n)]

# FASTEST: map with lambda (only if function already exists)
def squares_map(n):
    return list(map(lambda x: x ** 2, range(n)))

# When to use what:
# - List comprehension: Most readable, fast enough
# - map(): When function already exists, no lambda needed
# - Loop: When logic is complex or has side effects
```

### Tip 13: Use Collections Module

Specialized data structures from collections are optimized.

```python
from collections import Counter, defaultdict, deque

# SLOWER: Manual counting
def count_words_slow(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

# FASTER: Counter
def count_words_fast(words):
    return Counter(words)

# defaultdict for grouping
from collections import defaultdict

def group_by_length_slow(words):
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups

def group_by_length_fast(words):
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return groups

# deque for queue operations (O(1) appendleft/popleft)
from collections import deque

queue = deque([1, 2, 3])
queue.appendleft(0)  # O(1) - list would be O(n)
queue.popleft()      # O(1) - list would be O(n)
```

### Tip 14: Avoid Repeated Attribute Access

Cache object attributes accessed in loops.

```python
# SLOWER: Repeated attribute access
def process_slow(obj, values):
    result = []
    for value in values:
        result.append(obj.expensive_method(value))  # Lookup each time
    return result

# FASTER: Cache attribute
def process_fast(obj, values):
    method = obj.expensive_method  # Cache once
    result = []
    for value in values:
        result.append(method(value))
    return result

# Also applies to methods and modules
import math

def calculate_slow(values):
    return [math.sqrt(x) for x in values]  # Lookup math.sqrt each time

def calculate_fast(values):
    sqrt = math.sqrt
    return [sqrt(x) for x in values]  # Cached lookup
```

### Tip 15: Use itertools for Efficient Iteration

itertools provides memory-efficient iteration tools.

```python
import itertools

# Chunking data efficiently
def chunk_data(data, chunk_size):
    """Split data into chunks without loading all in memory."""
    it = iter(data)
    return iter(lambda: list(itertools.islice(it, chunk_size)), [])

# Chain iterables without creating intermediate list
# SLOWER
combined = list1 + list2 + list3  # Creates new list

# FASTER
combined = itertools.chain(list1, list2, list3)  # No intermediate list

# Infinite sequences
counter = itertools.count(start=0, step=1)
# next(counter) returns 0, 1, 2, 3, ...

# Efficient permutations and combinations
itertools.permutations([1, 2, 3])
itertools.combinations([1, 2, 3], 2)

# Grouping consecutive items
data = [1, 1, 1, 2, 2, 3, 3, 3, 3]
for key, group in itertools.groupby(data):
    print(f"{key}: {len(list(group))}")
# 1: 3, 2: 2, 3: 4
```

---

## Common Pitfalls

### Pitfall 1: String Concatenation in Loops

**Problem**: String concatenation with += is O(n²).

```python
# BAD: O(n²) complexity
def build_string_bad(words):
    result = ""
    for word in words:
        result += word + " "  # Creates new string each time!
    return result

# Time for 10,000 words: ~0.025s

# GOOD: O(n) complexity
def build_string_good(words):
    return " ".join(words)

# Time for 10,000 words: ~0.0002s (125x faster!)
```

**Why it happens**: Strings are immutable. Each += creates a new string object.

**Solution**: Use join(), or use a list and append(), then join at the end.

### Pitfall 2: Repeated Function Calls

**Problem**: Calling same function repeatedly with same arguments.

```python
# BAD: Repeated calculation
def calculate_total_bad(items):
    total = 0
    for item in items:
        total += item.price * get_tax_rate(item.category)  # Called many times
    return total

# GOOD: Cache the result
def calculate_total_good(items):
    tax_cache = {}
    total = 0
    for item in items:
        if item.category not in tax_cache:
            tax_cache[item.category] = get_tax_rate(item.category)
        total += item.price * tax_cache[item.category]
    return total

# BEST: Use lru_cache on the function
from functools import lru_cache

@lru_cache(maxsize=128)
def get_tax_rate(category):
    # Expensive calculation
    return calculate_tax(category)
```

### Pitfall 3: Using Wrong Data Structure

**Problem**: Using list when set/dict would be better.

```python
# BAD: O(n) membership testing
def find_duplicates_bad(items):
    seen = []  # Wrong choice!
    duplicates = []
    for item in items:
        if item in seen:  # O(n) lookup
            duplicates.append(item)
        else:
            seen.append(item)
    return duplicates

# Time for 10,000 items: ~1.2s

# GOOD: O(1) membership testing
def find_duplicates_good(items):
    seen = set()  # Right choice!
    duplicates = set()
    for item in items:
        if item in seen:  # O(1) lookup
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Time for 10,000 items: ~0.0014s (850x faster!)
```

**When to use what**:
- **List**: Ordered collection, need indexing, duplicates allowed
- **Set**: Membership testing, unique items, no order needed
- **Dict**: Key-value pairs, fast lookups, unique keys
- **Tuple**: Immutable list, hashable, can use as dict key

### Pitfall 4: Not Using Built-ins

**Problem**: Reimplementing functionality that exists in standard library.

```python
# BAD: Manual implementation
def find_max_bad(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

# GOOD: Built-in function
def find_max_good(numbers):
    return max(numbers)

# More examples:
# Instead of manual:         Use built-in:
# ----------------------     ----------------------
# Manual sum                 sum(items)
# Manual min/max             min(items), max(items)
# Manual sorting             sorted(items)
# Manual reversal            reversed(items)
# Manual filtering           filter(func, items)
# Manual mapping             map(func, items)
# Manual counting            collections.Counter(items)
```

### Pitfall 5: Deep Nesting and Complex Logic

**Problem**: Nested loops and conditions are hard to optimize.

```python
# BAD: O(n³) nested loops
def find_triplets_bad(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
    return result

# Time for 1000 items: Several seconds

# GOOD: O(n²) with two pointers
def find_triplets_good(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return result

# Time for 1000 items: ~0.01s (100x faster!)
```

**Solution**: Look for algorithmic improvements, use better data structures.

---

## Performance Quick Wins

### 1. List Comprehensions vs Loops

List comprehensions are 15-30% faster than equivalent for loops.

```python
# Slower
result = []
for i in range(1000):
    result.append(i ** 2)

# Faster
result = [i ** 2 for i in range(1000)]
```

### 2. Set for Membership Testing

Sets provide O(1) membership testing vs O(n) for lists.

```python
# Slow: O(n) lookup
if item in my_list:
    ...

# Fast: O(1) lookup
if item in my_set:
    ...
```

### 3. dict.get() vs try/except

Use dict.get() for simple defaults, try/except when exception is rare.

```python
# For simple defaults: dict.get() is faster
value = my_dict.get(key, default_value)

# When key usually exists: try/except is faster
try:
    value = my_dict[key]
except KeyError:
    value = default_value

# Why: try/except is optimized for the common path (no exception)
# When exception is rare, try/except is 2x faster than if/else
```

### 4. Local vs Global Variables

Local variables are 20-30% faster to access than globals.

```python
# Slower: global lookup
import math
def calculate():
    return math.sqrt(100)

# Faster: local variable
import math
def calculate():
    sqrt = math.sqrt
    return sqrt(100)
```

### 5. Import Optimization

Import at module level, not inside functions (unless needed for lazy loading).

```python
# SLOWER: Import in function
def process_data(data):
    import json  # Imported every call
    return json.loads(data)

# FASTER: Import at module level
import json

def process_data(data):
    return json.loads(data)

# EXCEPTION: Lazy loading for rarely used, heavy modules
def rarely_used_function():
    import heavy_module  # Only imported when actually called
    return heavy_module.do_something()
```

### 6. Use += for Lists

Use += instead of append() in tight loops for single items.

```python
# Slower
result = []
for i in range(1000):
    result.append(i)

# Slightly faster (but less readable)
result = []
for i in range(1000):
    result += [i]

# Best: Use list comprehension
result = [i for i in range(1000)]

# But for multiple items, += is good:
result = []
for batch in batches:
    result += batch  # Better than extend() sometimes
```

### 7. Multiple Assignments

Use multiple assignment for swapping and unpacking.

```python
# Slower: Temporary variable
temp = a
a = b
b = temp

# Faster: Multiple assignment
a, b = b, a

# Also works for unpacking
x, y, z = get_coordinates()  # Faster than indexing
```

### 8. Use 'in' for String/List Checks

Use 'in' operator instead of find() or index() when you just need to check existence.

```python
# Slower
if text.find('substring') != -1:
    ...

# Faster
if 'substring' in text:
    ...

# Slower
try:
    items.index(value)
    found = True
except ValueError:
    found = False

# Faster
found = value in items
```

### 9. Use Generators for Large Sequences

Generators use constant memory regardless of sequence size.

```python
# Memory intensive
def get_squares(n):
    return [i ** 2 for i in range(n)]

# Memory efficient
def get_squares(n):
    return (i ** 2 for i in range(n))

# Or use yield
def get_squares(n):
    for i in range(n):
        yield i ** 2
```

### 10. Cache Property Lookups in Loops

Cache object properties accessed multiple times in loops.

```python
# Slower: Repeated attribute lookup
for item in items:
    result.append(obj.method(item))

# Faster: Cache the method
method = obj.method
for item in items:
    result.append(method(item))
```

### 11. Use Set Operations

Use set operations instead of loops for set-like operations.

```python
# Slower: Loop to find common elements
common = []
for item in list1:
    if item in list2:
        common.append(item)

# Faster: Set intersection
common = list(set(list1) & set(list2))

# Other set operations:
union = set(list1) | set(list2)
difference = set(list1) - set(list2)
symmetric_diff = set(list1) ^ set(list2)
```

### 12. Use enumerate() Instead of range(len())

enumerate() is more Pythonic and slightly faster.

```python
# Slower and less readable
for i in range(len(items)):
    print(i, items[i])

# Faster and more readable
for i, item in enumerate(items):
    print(i, item)
```

### 13. Use zip() for Parallel Iteration

zip() is optimized for iterating multiple sequences together.

```python
# Slower: Manual indexing
for i in range(len(list1)):
    process(list1[i], list2[i])

# Faster: zip
for item1, item2 in zip(list1, list2):
    process(item1, item2)
```

### 14. Use 'while True' Instead of 'while 1'

In Python 3, both are equally fast, but 'while True' is more readable.

```python
# Both equally fast in Python 3
while True:
    if condition:
        break

while 1:
    if condition:
        break

# Prefer 'while True' for readability
```

### 15. Use f-strings for String Formatting

f-strings are fastest string formatting method in Python 3.6+.

```python
name = "Alice"
age = 30

# Slowest: % formatting
s = "Name: %s, Age: %d" % (name, age)

# Slow: str.format()
s = "Name: {}, Age: {}".format(name, age)

# Fastest: f-strings
s = f"Name: {name}, Age: {age}"
```

---

## Profiling Workflow

### Step 1: Identify Performance Goals

Before optimizing, define what "fast enough" means:
- Response time requirements
- Throughput targets
- Memory constraints
- Acceptable latency

### Step 2: Profile with cProfile

Find the hotspots in your code.

```python
import cProfile
import pstats
from pstats import SortKey

def profile_function(func, *args, **kwargs):
    """Profile a function and print statistics."""
    profiler = cProfile.Profile()
    profiler.enable()

    result = func(*args, **kwargs)

    profiler.disable()

    # Print statistics
    stats = pstats.Stats(profiler)
    stats.sort_stats(SortKey.CUMULATIVE)
    stats.print_stats(20)  # Top 20 functions

    return result

# Usage
result = profile_function(my_slow_function, arg1, arg2)
```

### Step 3: Use line_profiler for Line-by-Line Analysis

Install: `pip install line_profiler`

```python
# Add @profile decorator
@profile
def slow_function():
    x = [i ** 2 for i in range(1000)]
    y = [i ** 3 for i in range(1000)]
    return sum(x) + sum(y)

# Run with:
# kernprof -l -v script.py
```

### Step 4: Memory Profiling

Install: `pip install memory_profiler`

```python
from memory_profiler import profile

@profile
def memory_intensive():
    big_list = [i for i in range(1000000)]
    return sum(big_list)

# Run with:
# python -m memory_profiler script.py
```

### Step 5: Benchmark with timeit

Measure small code snippets accurately.

```python
import timeit

# Time a function
def my_function():
    return sum(range(1000))

# Run 10000 times and get average
time = timeit.timeit(my_function, number=10000)
print(f"Average time: {time/10000:.6f} seconds")

# Compare two approaches
time1 = timeit.timeit('[i**2 for i in range(100)]', number=10000)
time2 = timeit.timeit('list(map(lambda x: x**2, range(100)))', number=10000)
print(f"Comprehension: {time1:.6f}")
print(f"Map: {time2:.6f}")
```

### Step 6: Analyze Results

Look for:
1. **Functions with high cumulative time**: Total time including callees
2. **Functions with high total time**: Time spent in function itself
3. **Functions called many times**: May benefit from caching
4. **Unexpected function calls**: Dead code or inefficient logic

### Step 7: Optimize One Thing at a Time

1. Pick the biggest bottleneck
2. Implement optimization
3. Profile again to verify improvement
4. Repeat until performance goal is met

### Step 8: Verify Correctness

Always ensure optimized code produces same results:

```python
import unittest

class TestOptimization(unittest.TestCase):
    def test_same_results(self):
        """Verify optimized version produces same results."""
        input_data = generate_test_data()

        result_slow = slow_version(input_data)
        result_fast = fast_version(input_data)

        self.assertEqual(result_slow, result_fast)

    def test_performance(self):
        """Verify performance improvement."""
        import timeit

        input_data = generate_test_data()

        time_slow = timeit.timeit(lambda: slow_version(input_data), number=10)
        time_fast = timeit.timeit(lambda: fast_version(input_data), number=10)

        # Expect at least 2x speedup
        self.assertLess(time_fast, time_slow / 2)
```

---

## Key Takeaways

1. **Profile before optimizing** - Don't guess, measure. Use cProfile to find real bottlenecks.

2. **Algorithm matters most** - O(n²) → O(n) beats any micro-optimization. Choose right algorithm first.

3. **Use appropriate data structures** - Sets for membership, dicts for counting, deque for queues, lists for sequences.

4. **Built-ins are your friends** - sum(), max(), sorted(), etc. are optimized in C and very fast.

5. **Cache expensive computations** - Use @lru_cache for repeated calculations with same inputs.

6. **Avoid premature optimization** - Write clear code first. Optimize only proven bottlenecks.

7. **String concatenation kills** - Never use += in loops. Use join() instead. 132x faster.

8. **Generators save memory** - Use generators for large datasets. Process data lazily when possible.

9. **Batch operations** - Group database commits, API calls, I/O operations. Massive performance gains.

10. **List comprehensions** - 15-30% faster than equivalent for loops. Use them.

11. **Local > Global** - Local variables 20-30% faster. Cache globals as locals in tight loops.

12. **Parallelize CPU-bound work** - Use multiprocessing for CPU-intensive tasks. Respects core count.

13. **Profile memory too** - Memory usage matters. Use generators, del unused objects, avoid copies.

14. **Test correctness** - Always verify optimized code produces same results as original.

15. **Measure improvement** - Use timeit to measure actual speedup. Compare before/after.

16. **One optimization at a time** - Profile after each change to isolate impact.

17. **Know your complexity** - Understand Big O of your operations. O(1) > O(log n) > O(n) > O(n log n) > O(n²).

18. **Use right tool** - cProfile for function-level, line_profiler for line-level, memory_profiler for memory.

19. **Cache property lookups** - Accessing obj.method repeatedly in loop? Cache it first.

20. **Don't reinvent the wheel** - Check if standard library or third-party package already solves your problem efficiently.

---

## Additional Resources

### Tools
- **cProfile**: Built-in profiler, good for finding slow functions
- **line_profiler**: Line-by-line profiling
- **memory_profiler**: Memory usage profiling
- **py-spy**: Sampling profiler, no code changes needed
- **timeit**: Accurate timing for small code snippets
- **snakeviz**: Visualize cProfile results

### When to Optimize
- **Do optimize**: Proven bottleneck, impacts user experience, clear improvement path
- **Don't optimize**: Premature, unclear benefit, hurts readability, no measurements

### Performance Mindset
1. Make it work
2. Make it right
3. Make it fast (only if needed)

### Remember
> "Premature optimization is the root of all evil" - Donald Knuth

But also:

> "No amount of micro-optimization will fix a bad algorithm" - Unknown

The best optimization is choosing the right algorithm from the start!
