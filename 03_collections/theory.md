# Collections: Theory and Concepts

## 3.1 Lists and List Comprehensions

### What is a List?

A **list** is a mutable, ordered collection of items. Lists can contain items of different types.

```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]
```

**Key characteristics**:
- **Mutable**: Can be modified after creation
- **Ordered**: Items maintain insertion order
- **Indexed**: Access items by position (0-based)
- **Dynamic**: Can grow and shrink
- **Allows duplicates**: Same value can appear multiple times

### Creating Lists

```python
# Empty list
empty = []
empty = list()

# From iterable
chars = list("abc")  # ['a', 'b', 'c']
nums = list(range(5))  # [0, 1, 2, 3, 4]

# Literal syntax
numbers = [1, 2, 3, 4, 5]
```

### List Operations

**Indexing and Slicing**:
```python
items = [10, 20, 30, 40, 50]

# Indexing
items[0]    # 10 (first item)
items[-1]   # 50 (last item)
items[2]    # 30

# Slicing [start:stop:step]
items[1:3]   # [20, 30]
items[:2]    # [10, 20] (first 2)
items[2:]    # [30, 40, 50] (from index 2)
items[::2]   # [10, 30, 50] (every 2nd)
items[::-1]  # [50, 40, 30, 20, 10] (reversed)
```

**Modifying Lists**:
```python
items = [1, 2, 3]

# Append (add to end)
items.append(4)  # [1, 2, 3, 4]

# Insert (add at position)
items.insert(0, 0)  # [0, 1, 2, 3, 4]

# Extend (add multiple items)
items.extend([5, 6])  # [0, 1, 2, 3, 4, 5, 6]

# Remove (by value)
items.remove(0)  # [1, 2, 3, 4, 5, 6]

# Pop (remove by index, returns item)
last = items.pop()  # 6, items is now [1, 2, 3, 4, 5]
first = items.pop(0)  # 1, items is now [2, 3, 4, 5]

# Clear (remove all)
items.clear()  # []
```

**Other Operations**:
```python
items = [3, 1, 4, 1, 5]

# Length
len(items)  # 5

# Count occurrences
items.count(1)  # 2

# Find index
items.index(4)  # 2 (first occurrence)

# Sort (in-place)
items.sort()  # [1, 1, 3, 4, 5]

# Reverse (in-place)
items.reverse()  # [5, 4, 3, 1, 1]

# Sorted (returns new list)
sorted_items = sorted([3, 1, 4])  # [1, 3, 4]

# Concatenation
[1, 2] + [3, 4]  # [1, 2, 3, 4]

# Repetition
[1, 2] * 3  # [1, 2, 1, 2, 1, 2]

# Membership
1 in items  # True
10 in items  # False
```

### List Comprehensions

**Syntax**: `[expression for item in iterable if condition]`

```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension (more Pythonic)
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# With transformation
words = ["hello", "world"]
upper = [word.upper() for word in words]
# ['HELLO', 'WORLD']

# Nested loops
pairs = [(x, y) for x in range(3) for y in range(3)]
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

# Nested comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 3.2 Tuples and Named Tuples

### What is a Tuple?

A **tuple** is an immutable, ordered collection of items.

```python
point = (10, 20)
person = ("Alice", 30, "NYC")
```

**Key characteristics**:
- **Immutable**: Cannot be modified after creation
- **Ordered**: Items maintain order
- **Indexed**: Access by position
- **Allows duplicates**: Same value can appear multiple times
- **Hashable**: Can be used as dict keys (if all items are hashable)

### Creating Tuples

```python
# Parentheses (optional but recommended)
point = (10, 20)

# Without parentheses (tuple packing)
coords = 10, 20, 30

# Single item tuple (comma required!)
single = (42,)  # Tuple with one item
not_tuple = (42)  # This is just int 42!

# Empty tuple
empty = ()
empty = tuple()

# From iterable
tuple_from_list = tuple([1, 2, 3])
```

### Tuple Operations

```python
items = (1, 2, 3, 4, 5)

# Indexing (same as lists)
items[0]    # 1
items[-1]   # 5

# Slicing
items[1:3]  # (2, 3)

# Length
len(items)  # 5

# Count and index
(1, 2, 1, 3).count(1)  # 2
(1, 2, 3).index(2)     # 1

# Concatenation
(1, 2) + (3, 4)  # (1, 2, 3, 4)

# Repetition
(1, 2) * 3  # (1, 2, 1, 2, 1, 2)

# Membership
2 in items  # True

# Unpacking
x, y, z = (1, 2, 3)
# x=1, y=2, z=3

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
# first=1, middle=[2,3,4], last=5
```

### Why Use Tuples?

1. **Immutability**: Data that shouldn't change
2. **Performance**: Tuples are faster than lists
3. **Dict keys**: Can be used as dictionary keys
4. **Return multiple values**: Functions can return tuples
5. **Unpacking**: Clean syntax for multiple assignment

```python
# Function returning multiple values
def get_user():
    return "Alice", 30, "NYC"

name, age, city = get_user()

# Tuple as dict key
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}
```

### Named Tuples

Named tuples provide field names for better readability:

```python
from collections import namedtuple

# Define named tuple type
Point = namedtuple('Point', ['x', 'y'])

# Create instance
p = Point(10, 20)

# Access by name
print(p.x)  # 10
print(p.y)  # 20

# Access by index (still works)
print(p[0])  # 10

# Convert to dict
p._asdict()  # {'x': 10, 'y': 20}

# Replace fields (creates new tuple)
p2 = p._replace(x=30)  # Point(x=30, y=20)
```

---

## 3.3 Dictionaries and Dict Comprehensions

### What is a Dictionary?

A **dictionary** is a mutable collection of key-value pairs.

```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "NYC"
}
```

**Key characteristics**:
- **Mutable**: Can be modified
- **Unordered** (Python 3.6-): Order not guaranteed
- **Ordered** (Python 3.7+): Maintains insertion order
- **Keys must be unique**: Duplicate keys not allowed
- **Keys must be hashable**: Immutable types (str, int, tuple)
- **Values can be anything**: Any type

### Creating Dictionaries

```python
# Empty dict
empty = {}
empty = dict()

# Literal syntax
person = {"name": "Alice", "age": 30}

# From pairs
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)  # {'a': 1, 'b': 2}

# Using dict constructor with kwargs
d = dict(name="Alice", age=30)

# From keys with default value
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)  # {'a': 0, 'b': 0, 'c': 0}
```

### Dictionary Operations

**Accessing Values**:
```python
person = {"name": "Alice", "age": 30}

# Access by key
person["name"]  # "Alice"
person["age"]   # 30

# KeyError if key doesn't exist
person["city"]  # KeyError!

# get() method (safer, returns None or default)
person.get("name")  # "Alice"
person.get("city")  # None
person.get("city", "Unknown")  # "Unknown"
```

**Modifying Dictionaries**:
```python
d = {"a": 1, "b": 2}

# Add/update item
d["c"] = 3  # {'a': 1, 'b': 2, 'c': 3}
d["a"] = 10  # {'a': 10, 'b': 2, 'c': 3}

# Update with another dict
d.update({"d": 4, "e": 5})

# Remove item (returns value)
value = d.pop("a")  # 10, d is now {'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Remove and return arbitrary item (Python 3.7+: last inserted)
item = d.popitem()  # ('e', 5)

# Delete item
del d["b"]

# Clear all items
d.clear()  # {}
```

**Dictionary Methods**:
```python
d = {"a": 1, "b": 2, "c": 3}

# Keys, values, items
d.keys()    # dict_keys(['a', 'b', 'c'])
d.values()  # dict_values([1, 2, 3])
d.items()   # dict_items([('a', 1), ('b', 2), ('c', 3)])

# Convert to lists
list(d.keys())    # ['a', 'b', 'c']
list(d.values())  # [1, 2, 3]
list(d.items())   # [('a', 1), ('b', 2), ('c', 3)]

# Check membership (checks keys)
"a" in d     # True
1 in d       # False (checks keys, not values)

# Length
len(d)  # 3

# setdefault (get with default, also sets if missing)
d.setdefault("d", 4)  # 4, and d now has 'd': 4
```

### Dictionary Comprehensions

**Syntax**: `{key_expr: value_expr for item in iterable if condition}`

```python
# Square numbers
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Invert dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Filter items
data = {"a": 1, "b": 2, "c": 3, "d": 4}
evens = {k: v for k, v in data.items() if v % 2 == 0}
# {'b': 2, 'd': 4}

# Transform values
words = {"apple": 5, "banana": 6}
upper_words = {k.upper(): v for k, v in words.items()}
# {'APPLE': 5, 'BANANA': 6}
```

### Dictionary Merge (Python 3.9+)

```python
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

# Merge operator |
merged = d1 | d2  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Update operator |=
d1 |= d2  # d1 is now merged
```

---

## 3.4 Sets and Set Operations

### What is a Set?

A **set** is a mutable, unordered collection of unique items.

```python
numbers = {1, 2, 3, 4, 5}
```

**Key characteristics**:
- **Mutable**: Can be modified
- **Unordered**: No guaranteed order
- **Unique items**: No duplicates
- **Items must be hashable**: Immutable types only
- **No indexing**: Can't access by position

### Creating Sets

```python
# Literal syntax (Python 3.x)
numbers = {1, 2, 3, 4, 5}

# From iterable
chars = set("hello")  # {'h', 'e', 'l', 'o'}

# Empty set (must use set(), not {})
empty = set()  # {}  would be empty dict!

# Remove duplicates
unique = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}
```

### Set Operations

**Modifying Sets**:
```python
s = {1, 2, 3}

# Add item
s.add(4)  # {1, 2, 3, 4}

# Add multiple items
s.update([5, 6, 7])  # {1, 2, 3, 4, 5, 6, 7}

# Remove item (raises KeyError if not found)
s.remove(1)  # {2, 3, 4, 5, 6, 7}

# Discard item (no error if not found)
s.discard(10)  # No error

# Pop random item
item = s.pop()

# Clear all
s.clear()
```

**Set Mathematics**:
```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union (all items from both)
a | b  # {1, 2, 3, 4, 5, 6, 7, 8}
a.union(b)

# Intersection (items in both)
a & b  # {4, 5}
a.intersection(b)

# Difference (in a but not in b)
a - b  # {1, 2, 3}
a.difference(b)

# Symmetric difference (in either but not both)
a ^ b  # {1, 2, 3, 6, 7, 8}
a.symmetric_difference(b)

# Subset
{1, 2} <= {1, 2, 3}  # True
{1, 2}.issubset({1, 2, 3})

# Superset
{1, 2, 3} >= {1, 2}  # True
{1, 2, 3}.issuperset({1, 2})

# Disjoint (no common items)
{1, 2}.isdisjoint({3, 4})  # True
```

### Frozenset (Immutable Set)

```python
# Create frozenset
fs = frozenset([1, 2, 3])

# Can't be modified
# fs.add(4)  # AttributeError!

# Can be used as dict key or set item
d = {fs: "value"}
s = {frozenset([1, 2]), frozenset([3, 4])}
```

### Set Comprehensions

```python
# Squares
squares = {x**2 for x in range(10)}

# Unique characters (case-insensitive)
text = "Hello World"
unique_chars = {char.lower() for char in text if char.isalpha()}
# {'h', 'e', 'l', 'o', 'w', 'r', 'd'}
```

---

## 3.5 Collections Module

The `collections` module provides specialized container datatypes.

### Counter

Count occurrences of items:

```python
from collections import Counter

# Count items in iterable
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Count characters
text = "hello world"
char_counts = Counter(text)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Most common
counts.most_common(2)  # [('apple', 3), ('banana', 2)]

# Arithmetic operations
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
c1 + c2  # Counter({'a': 4, 'b': 3})
c1 - c2  # Counter({'a': 2})
```

### defaultdict

Dictionary with default value for missing keys:

```python
from collections import defaultdict

# With list
groups = defaultdict(list)
groups["fruits"].append("apple")  # No KeyError!
# defaultdict(<class 'list'>, {'fruits': ['apple']})

# With int (useful for counting)
counts = defaultdict(int)
for word in ["a", "b", "a", "c", "b", "a"]:
    counts[word] += 1  # Starts at 0
# defaultdict(<class 'int'>, {'a': 3, 'b': 2, 'c': 1})

# With custom default
def default_value():
    return "N/A"

d = defaultdict(default_value)
d["missing"]  # "N/A"
```

### deque (Double-Ended Queue)

Fast appends and pops from both ends:

```python
from collections import deque

# Create deque
dq = deque([1, 2, 3])

# Append to right
dq.append(4)  # deque([1, 2, 3, 4])

# Append to left
dq.appendleft(0)  # deque([0, 1, 2, 3, 4])

# Pop from right
dq.pop()  # 4, deque([0, 1, 2, 3])

# Pop from left
dq.popleft()  # 0, deque([1, 2, 3])

# Rotate
dq.rotate(1)  # deque([3, 1, 2])
dq.rotate(-1)  # deque([1, 2, 3])

# Maximum length (circular buffer)
dq = deque([1, 2, 3], maxlen=3)
dq.append(4)  # deque([2, 3, 4]) - 1 was removed
```

### ChainMap

Combine multiple dictionaries:

```python
from collections import ChainMap

# Combine dicts
defaults = {"theme": "light", "lang": "en"}
user_prefs = {"theme": "dark"}

config = ChainMap(user_prefs, defaults)
config["theme"]  # "dark" (from user_prefs)
config["lang"]   # "en" (from defaults)

# Modifications affect first dict only
config["new_key"] = "value"  # Added to user_prefs

# Search order: user_prefs, then defaults
```

---

## 3.6 Array Module and Memory-Efficient Collections

### Array Module

For homogeneous numeric data (more memory-efficient than lists):

```python
from array import array

# Create array (type code 'i' = signed int)
numbers = array('i', [1, 2, 3, 4, 5])

# Use like list
numbers.append(6)
numbers[0]  # 1

# Type codes:
# 'b' - signed char (1 byte)
# 'i' - signed int (2+ bytes)
# 'f' - float (4 bytes)
# 'd' - double (8 bytes)

# Memory efficient
import sys
list_size = sys.getsizeof([1, 2, 3, 4, 5])
array_size = sys.getsizeof(array('i', [1, 2, 3, 4, 5]))
# array is smaller!
```

---

## Key Concepts Summary

### When to Use Which Collection?

| Collection | Use When | Key Feature |
|------------|----------|-------------|
| **list** | Order matters, need modification | Mutable, ordered |
| **tuple** | Immutable sequence, dict keys | Immutable, ordered |
| **dict** | Key-value pairs, fast lookup | Key-value mapping |
| **set** | Unique items, set operations | Unique, unordered |
| **Counter** | Count occurrences | Specialized dict |
| **defaultdict** | Dict with default values | No KeyError |
| **deque** | Queue/stack operations | Fast ends |
| **ChainMap** | Multiple dict layers | Dict hierarchy |
| **array** | Numeric data, memory efficiency | Typed, compact |

### Mutability Summary

**Mutable** (can change):
- list, dict, set, bytearray
- collections: Counter, defaultdict, deque

**Immutable** (cannot change):
- tuple, frozenset, str, bytes
- collections: namedtuple

### Performance Characteristics

| Operation | list | tuple | dict | set |
|-----------|------|-------|------|-----|
| Index access | O(1) | O(1) | N/A | N/A |
| Search | O(n) | O(n) | O(1) | O(1) |
| Insert/Delete | O(n) | N/A | O(1) | O(1) |
| Append | O(1) | N/A | O(1) | O(1) |

---

## Next Steps

1. Practice with each collection type
2. Master list and dict comprehensions
3. Experiment with collections module
4. Understand performance trade-offs
5. Move on to examples.md for hands-on practice
