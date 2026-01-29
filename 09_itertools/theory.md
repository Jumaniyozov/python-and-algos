# Itertools and Functional Tools: Theory

## 1. Introduction to Itertools

The `itertools` module provides fast, memory-efficient tools for creating iterators. Instead of creating lists in memory, itertools functions return iterators that generate values on demand.

### Why Itertools?

```python
# Without itertools - creates entire list in memory
numbers = [i for i in range(1000000)]
result = [x * 2 for x in numbers if x % 2 == 0]

# With itertools - processes items one at a time
from itertools import islice, count
result = (x * 2 for x in count() if x % 2 == 0)
first_10 = list(islice(result, 10))
```

**Key Benefits**:
- Memory efficiency: O(1) space instead of O(n)
- Lazy evaluation: compute only what's needed
- Composability: chain multiple operations
- Speed: implemented in C

## 2. Combinatoric Iterators

### 2.1 product() - Cartesian Product

Equivalent to nested for-loops.

```python
from itertools import product

# product('AB', 'xy') → Ax Ay Bx By
list(product('AB', 'xy'))  # [('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y')]

# Repeat argument for multiple copies
list(product(range(2), repeat=3))  # [(0,0,0), (0,0,1), (0,1,0), ...]
```

**Use cases**: Generate all combinations of options, test cases, grid coordinates.

### 2.2 permutations() - All Orderings

Generate all possible orderings of elements.

```python
from itertools import permutations

# permutations('ABC', 2) → AB AC BA BC CA CB
list(permutations('ABC', 2))  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ...]

# Without length: all permutations of all elements
list(permutations('ABC'))  # [('A', 'B', 'C'), ('A', 'C', 'B'), ...]
```

**Formula**: n! / (n-r)! where n is elements, r is selection size

### 2.3 combinations() - Unique Selections

Generate all r-length combinations without repetition. Order doesn't matter.

```python
from itertools import combinations

# combinations('ABCD', 2) → AB AC AD BC BD CD
list(combinations('ABCD', 2))  # [('A', 'B'), ('A', 'C'), ('A', 'D'), ...]
```

**Formula**: n! / (r! * (n-r)!)

### 2.4 combinations_with_replacement()

Combinations where elements can repeat.

```python
from itertools import combinations_with_replacement

# combinations_with_replacement('ABC', 2) → AA AB AC BB BC CC
list(combinations_with_replacement('ABC', 2))
```

## 3. Infinite Iterators

These iterators never stop. Always use with something that limits them (like `islice()`, `takewhile()`, or break).

### 3.1 count(start=0, step=1)

Count from start infinitely.

```python
from itertools import count, islice

# Count from 10 by 2s
counter = count(10, 2)  # 10, 12, 14, 16, ...
list(islice(counter, 5))  # [10, 12, 14, 16, 18]

# Can count with floats or Decimals
from decimal import Decimal
counter = count(Decimal('0.1'), Decimal('0.1'))
```

### 3.2 cycle(iterable)

Repeat an iterable infinitely.

```python
from itertools import cycle

# cycle('ABC') → A B C A B C A B C ...
colors = cycle(['red', 'green', 'blue'])
```

**Use case**: Round-robin task assignment, alternating patterns.

### 3.3 repeat(object, times=None)

Repeat an object, either infinitely or n times.

```python
from itertools import repeat

list(repeat(10, 3))  # [10, 10, 10]
repeat(10)  # Infinite 10s

# Useful with map for constant arguments
list(map(pow, range(5), repeat(2)))  # [0^2, 1^2, 2^2, 3^2, 4^2]
```

## 4. Terminating Iterators

### 4.1 chain(*iterables)

Chain multiple iterables together.

```python
from itertools import chain

list(chain('ABC', 'DEF'))  # ['A', 'B', 'C', 'D', 'E', 'F']
list(chain.from_iterable(['ABC', 'DEF']))  # Same result

# Flattening nested lists
nested = [[1, 2], [3, 4], [5]]
flat = list(chain.from_iterable(nested))  # [1, 2, 3, 4, 5]
```

### 4.2 compress(data, selectors)

Filter data based on selectors (boolean mask).

```python
from itertools import compress

data = ['A', 'B', 'C', 'D']
selectors = [1, 0, 1, 0]
list(compress(data, selectors))  # ['A', 'C']
```

### 4.3 dropwhile(predicate, iterable)

Drop elements while predicate is true, then yield everything.

```python
from itertools import dropwhile

data = [1, 4, 6, 4, 1]
list(dropwhile(lambda x: x < 5, data))  # [6, 4, 1]
```

### 4.4 takewhile(predicate, iterable)

Yield elements while predicate is true.

```python
from itertools import takewhile

data = [1, 4, 6, 4, 1]
list(takewhile(lambda x: x < 5, data))  # [1, 4]
```

### 4.5 groupby(iterable, key=None)

Group consecutive elements by key function.

**Important**: Data must be sorted by the key first!

```python
from itertools import groupby

data = ['a', 'a', 'b', 'b', 'b', 'c']
for key, group in groupby(data):
    print(key, list(group))
# Output:
# a ['a', 'a']
# b ['b', 'b', 'b']
# c ['c']

# With key function
data = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
for key, group in groupby(sorted(data, key=len), key=len):
    print(f"Length {key}: {list(group)}")
```

### 4.6 islice(iterable, start, stop, step)

Slice an iterator.

```python
from itertools import islice, count

list(islice('ABCDEFG', 2))  # ['A', 'B']
list(islice('ABCDEFG', 2, 4))  # ['C', 'D']
list(islice('ABCDEFG', 2, None))  # ['C', 'D', 'E', 'F', 'G']
list(islice(count(), 5, 10))  # [5, 6, 7, 8, 9]
```

### 4.7 accumulate(iterable, func=operator.add)

Cumulative results of binary function.

```python
from itertools import accumulate
import operator

list(accumulate([1, 2, 3, 4, 5]))  # [1, 3, 6, 10, 15] (cumulative sum)
list(accumulate([1, 2, 3, 4, 5], operator.mul))  # [1, 2, 6, 24, 120] (factorial)

# Running maximum
data = [3, 4, 6, 2, 1, 9, 0, 7]
list(accumulate(data, max))  # [3, 4, 6, 6, 6, 9, 9, 9]
```

### 4.8 zip_longest(*iterables, fillvalue=None)

Zip iterables, filling missing values.

```python
from itertools import zip_longest

list(zip_longest('ABC', '12345', fillvalue='?'))
# [('A', '1'), ('B', '2'), ('C', '3'), ('?', '4'), ('?', '5')]
```

## 5. Functools Module

Functional programming tools for higher-order functions.

### 5.1 partial() - Partial Function Application

Create new function with some arguments pre-filled.

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

square(5)  # 25
cube(5)  # 125
```

**Use cases**:
- Creating specialized functions from general ones
- Passing to higher-order functions
- Configuration with default arguments

### 5.2 reduce() - Cumulative Computation

Apply function cumulatively to items.

```python
from functools import reduce

# Sum
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 15

# Product
reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])  # 120

# Maximum
reduce(max, [3, 7, 2, 9, 1])  # 9
```

**Note**: For sum, prefer built-in `sum()`. For product, use `math.prod()`.

### 5.3 cache() and lru_cache() - Memoization

Cache function results for faster repeated calls.

```python
from functools import cache, lru_cache

@cache  # Unbounded cache (Python 3.9+)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@lru_cache(maxsize=128)  # Bounded cache (LRU eviction)
def expensive_computation(x):
    return x ** 2

# Cache info
fibonacci.cache_info()  # CacheInfo(hits=..., misses=..., maxsize=None, currsize=...)
fibonacci.cache_clear()  # Clear cache
```

**When to use**:
- `@cache`: Pure functions with hashable arguments
- `@lru_cache`: When memory is a concern
- Not for functions with side effects

### 5.4 singledispatch() - Function Overloading

Create generic functions with type-specific implementations.

```python
from functools import singledispatch

@singledispatch
def process(data):
    raise NotImplementedError(f"Cannot process type {type(data)}")

@process.register(str)
def _(data):
    return data.upper()

@process.register(list)
def _(data):
    return [x * 2 for x in data]

@process.register(int)
@process.register(float)
def _(data):
    return data ** 2

process("hello")  # "HELLO"
process([1, 2, 3])  # [2, 4, 6]
process(5)  # 25
```

### 5.5 wraps() - Decorator Helper

Preserve function metadata in decorators.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves func's name, docstring, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Say hello."""
    return f"Hello, {name}!"

greet.__name__  # 'greet' (not 'wrapper')
greet.__doc__  # 'Say hello.'
```

### 5.6 total_ordering() - Comparison Methods

Generate comparison methods from `__eq__` and one other.

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

    # __le__, __gt__, __ge__ are automatically generated!

alice = Student("Alice", 85)
bob = Student("Bob", 90)
alice < bob  # True
alice >= bob  # False
```

## 6. Operator Module

Function equivalents of operators.

```python
import operator

# Arithmetic
operator.add(1, 2)  # 3
operator.mul(3, 4)  # 12

# Comparison
operator.lt(1, 2)  # True
operator.eq(1, 1)  # True

# Item and attribute access
operator.itemgetter(1)([1, 2, 3])  # 2
operator.itemgetter('name')({'name': 'Alice'})  # 'Alice'

# Sort by second element
data = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted(data, key=operator.itemgetter(1))

# Sort objects by attribute
from operator import attrgetter
users = [User('Bob', 30), User('Alice', 25)]
sorted(users, key=attrgetter('age'))

# Call methods
operator.methodcaller('upper')('hello')  # 'HELLO'
operator.methodcaller('split', ',')('a,b,c')  # ['a', 'b', 'c']
```

## 7. Efficient Iteration Patterns

### Pattern 1: Pairwise Iteration

```python
from itertools import islice

def pairwise(iterable):
    """s -> (s0, s1), (s1, s2), (s2, s3), ..."""
    a, b = iter(iterable), iter(iterable)
    next(b, None)
    return zip(a, b)

list(pairwise([1, 2, 3, 4]))  # [(1, 2), (2, 3), (3, 4)]

# Or in Python 3.10+
from itertools import pairwise
```

### Pattern 2: Sliding Window

```python
from itertools import islice
from collections import deque

def sliding_window(iterable, n):
    """Return sliding window of size n"""
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for item in it:
        window.append(item)
        yield tuple(window)

list(sliding_window([1, 2, 3, 4, 5], 3))
# [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
```

### Pattern 3: Chunking

```python
from itertools import islice

def chunked(iterable, n):
    """Break iterable into chunks of size n"""
    it = iter(iterable)
    while True:
        chunk = list(islice(it, n))
        if not chunk:
            return
        yield chunk

list(chunked(range(10), 3))  # [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
```

### Pattern 4: Flatten

```python
from itertools import chain

def flatten(nested_list):
    """Flatten one level"""
    return chain.from_iterable(nested_list)

list(flatten([[1, 2], [3, 4], [5]]))  # [1, 2, 3, 4, 5]

# Deep flatten
def deep_flatten(nested):
    """Recursively flatten any depth"""
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from deep_flatten(item)
        else:
            yield item
```

## 8. Performance Considerations

### Memory Usage

```python
# Bad: Creates entire list in memory
squares = [x**2 for x in range(1000000)]

# Good: Generator expression
squares = (x**2 for x in range(1000000))

# Even better with itertools
from itertools import count, islice
squares = (x**2 for x in count())
first_million = islice(squares, 1000000)
```

### When to Convert to List

Only convert to list when you need:
1. Multiple iterations over data
2. Length of the iterator
3. Random access
4. Reverse iteration

Otherwise, keep as iterator for memory efficiency.

## Summary

| Tool | Purpose | Returns |
|------|---------|---------|
| `product` | Cartesian product | Iterator of tuples |
| `permutations` | All orderings | Iterator of tuples |
| `combinations` | Unique selections | Iterator of tuples |
| `chain` | Concatenate iterables | Iterator |
| `groupby` | Group consecutive items | Iterator of (key, group) |
| `accumulate` | Running totals | Iterator |
| `@cache` | Memoization | Decorated function |
| `partial` | Partial application | Function |
| `reduce` | Cumulative computation | Single value |

## Key Takeaways

1. **Lazy evaluation** is memory-efficient and fast
2. **Combine tools** for complex operations
3. **Use caching** for expensive pure functions
4. **Operator module** for functional-style code
5. **Always limit** infinite iterators
6. **Sort before groupby** for correct grouping
7. **itertools is fast** - implemented in C
