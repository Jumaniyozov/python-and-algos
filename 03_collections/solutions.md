# Collections: Exercise Solutions

## Solution 1: List Rotation
```python
def rotate_list(lst: list, k: int) -> list:
    """Rotate list k positions to the right."""
    if not lst:
        return lst
    k = k % len(lst)  # Handle k > len(lst)
    return lst[-k:] + lst[:-k]

# Test
print(rotate_list([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
```

## Solution 2: Merge Dictionaries
```python
def merge_dicts(*dicts) -> dict:
    """Merge multiple dictionaries."""
    result = {}
    for d in dicts:
        result.update(d)
    return result

# Python 3.9+ alternative
def merge_dicts_modern(*dicts) -> dict:
    result = {}
    for d in dicts:
        result |= d
    return result
```

## Solution 3: Common Elements
```python
def find_common_elements(*lists) -> set:
    """Find elements common to all lists."""
    if not lists:
        return set()
    result = set(lists[0])
    for lst in lists[1:]:
        result &= set(lst)
    return result

# Test
print(find_common_elements([1, 2, 3], [2, 3, 4], [2, 3, 5]))  # {2, 3}
```

## Solution 4: Most Common Words
```python
from collections import Counter
import re

def most_common_words(text: str, n: int = 10) -> list:
    """Find n most common words in text."""
    # Remove punctuation, lowercase, split
    words = re.findall(r'\b\w+\b', text.lower())
    counts = Counter(words)
    return counts.most_common(n)
```

## Solution 5: Group by First Element
```python
from collections import defaultdict

def group_tuples(tuples_list: list) -> dict:
    """Group tuples by first element."""
    groups = defaultdict(list)
    for tup in tuples_list:
        groups[tup[0]].append(tup)
    return dict(groups)

# Test
data = [(1, 'a'), (2, 'b'), (1, 'c'), (2, 'd')]
print(group_tuples(data))
# {1: [(1, 'a'), (1, 'c')], 2: [(2, 'b'), (2, 'd')]}
```

## Solution 6: Prime Numbers
```python
def primes_up_to(n: int) -> list:
    """Generate prime numbers up to n using comprehension."""
    def is_prime(num):
        if num < 2:
            return False
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

    return [x for x in range(2, n + 1) if is_prime(x)]

print(primes_up_to(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

## Solution 7: Named Tuple Person
```python
from collections import namedtuple
from datetime import datetime

Person = namedtuple('Person', ['name', 'birthdate'])

def calculate_age(person: Person) -> int:
    """Calculate age from birthdate."""
    today = datetime.now()
    age = today.year - person.birthdate.year
    if (today.month, today.day) < (person.birthdate.month, person.birthdate.day):
        age -= 1
    return age

# Test
p = Person('Alice', datetime(1990, 5, 15))
print(calculate_age(p))
```

## Solution 8: Circular Buffer
```python
from collections import deque

class CircularBuffer:
    def __init__(self, max_size: int):
        self.buffer = deque(maxlen=max_size)

    def add(self, item):
        self.buffer.append(item)

    def get_all(self) -> list:
        return list(self.buffer)

# Test
cb = CircularBuffer(3)
for i in range(5):
    cb.add(i)
print(cb.get_all())  # [2, 3, 4] - only last 3
```

## Solution 9: Flatten Nested List
```python
def flatten(nested_list):
    """Flatten nested list of arbitrary depth."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Test
print(flatten([1, [2, [3, 4], 5], 6]))  # [1, 2, 3, 4, 5, 6]
```

## Solution 10: Performance Comparison
```python
import time

# Create test data
test_list = list(range(10000))
test_set = set(range(10000))
search_value = 9999

# Test list
start = time.time()
for _ in range(10000):
    _ = search_value in test_list
list_time = time.time() - start

# Test set
start = time.time()
for _ in range(10000):
    _ = search_value in test_set
set_time = time.time() - start

print(f"List time: {list_time:.4f}s")
print(f"Set time: {set_time:.4f}s")
print(f"Set is {list_time/set_time:.1f}x faster")
```

See examples.md for more practical examples.
