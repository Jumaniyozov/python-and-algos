# Hash Tables: Theory and Fundamentals

## Table of Contents
1. [Hash Table Fundamentals](#hash-table-fundamentals)
2. [Hash Functions](#hash-functions)
3. [Collision Resolution](#collision-resolution)
4. [Load Factor and Resizing](#load-factor-and-resizing)
5. [Python dict Implementation](#python-dict-implementation)
6. [Python Collections](#python-collections)
7. [Set Operations](#set-operations)
8. [Complexity Analysis](#complexity-analysis)

---

## Hash Table Fundamentals

### What is a Hash Table?

A **hash table** (also called hash map or dictionary) is a data structure that implements an associative array abstract data type, mapping keys to values.

**Core Components:**
1. **Array**: Underlying storage (buckets)
2. **Hash Function**: Maps keys to array indices
3. **Collision Resolution**: Handles when multiple keys hash to same index

### Visual Representation

```
Key-Value Pairs:
("apple", 5)
("banana", 3)
("orange", 7)

Hash Function:
hash("apple") % 10 = 3
hash("banana") % 10 = 7
hash("orange") % 10 = 3  <- Collision!

Hash Table (size 10):
[0] -> None
[1] -> None
[2] -> None
[3] -> ("apple", 5) -> ("orange", 7)  <- Chaining
[4] -> None
[5] -> None
[6] -> None
[7] -> ("banana", 3)
[8] -> None
[9] -> None
```

### Basic Operations

**Insert:**
```
1. Compute hash(key)
2. Find index = hash(key) % table_size
3. Handle collision if needed
4. Store (key, value) at index
```

**Lookup:**
```
1. Compute hash(key)
2. Find index = hash(key) % table_size
3. Check bucket at index
4. If collision resolution used, search in bucket
5. Return value if found, else KeyError
```

**Delete:**
```
1. Compute hash(key)
2. Find index = hash(key) % table_size
3. Search bucket for key
4. Remove (key, value) pair
```

---

## Hash Functions

A **hash function** maps data of arbitrary size to fixed-size values (hash codes).

### Properties of Good Hash Functions

1. **Deterministic**: Same input always produces same output
2. **Uniform Distribution**: Spreads keys evenly across buckets
3. **Fast to Compute**: O(1) or O(k) where k is key length
4. **Minimize Collisions**: Different keys rarely hash to same value

### Common Hash Functions

#### 1. Division Method

```python
def hash_division(key, table_size):
    """
    Simple: hash = key % table_size

    Pros: Fast, simple
    Cons: Table size should be prime to avoid patterns
    """
    return hash(key) % table_size
```

**Example:**
```
key = 12345, table_size = 10
hash = 12345 % 10 = 5

key = 67890, table_size = 10
hash = 67890 % 10 = 0
```

#### 2. Multiplication Method

```python
def hash_multiplication(key, table_size):
    """
    hash = floor(table_size * ((key * A) % 1))
    where A ≈ 0.6180339887 (golden ratio)

    Pros: Table size doesn't need to be prime
    Cons: Slightly slower than division
    """
    A = 0.6180339887
    return int(table_size * ((key * A) % 1))
```

**Example:**
```
key = 123, table_size = 1000, A = 0.618...
hash = floor(1000 * ((123 * 0.618) % 1))
     = floor(1000 * 0.014)
     = 14
```

#### 3. Universal Hashing

```python
import random

class UniversalHash:
    """
    hash = ((a * key + b) % p) % table_size

    where p is prime > max_key, a and b are random
    """
    def __init__(self, table_size):
        self.table_size = table_size
        self.p = 2**31 - 1  # Large prime
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def hash(self, key):
        return ((self.a * key + self.b) % self.p) % self.table_size
```

### String Hashing

**Polynomial Rolling Hash:**
```python
def hash_string(s, base=31, mod=10**9 + 9):
    """
    hash = (s[0]*base^(n-1) + s[1]*base^(n-2) + ... + s[n-1]) % mod

    Common bases: 31 (lowercase), 53 (case-sensitive)
    """
    hash_value = 0
    power = 1

    for char in s:
        hash_value = (hash_value + ord(char) * power) % mod
        power = (power * base) % mod

    return hash_value
```

**Example:**
```
s = "abc", base = 31, mod = 10^9 + 9

hash = (a*31^0 + b*31^1 + c*31^2) % mod
     = (97*1 + 98*31 + 99*961) % mod
     = (97 + 3038 + 95139) % mod
     = 98274 % mod
     = 98274
```

### Python's hash() Function

```python
# Built-in hash function
hash(42)           # Integer: returns itself (usually)
hash("hello")      # String: polynomial hash
hash((1, 2, 3))    # Tuple: combines element hashes
hash([1, 2, 3])    # ERROR: lists are not hashable

# Custom hash
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

**Important:** Objects that compare equal must have the same hash value!

---

## Collision Resolution

When two keys hash to the same index, we have a **collision**. Several strategies exist to handle this.

### 1. Chaining (Separate Chaining)

Each bucket contains a linked list (or other structure) of all (key, value) pairs that hash to that index.

```
Hash Table with Chaining:

[0] -> None
[1] -> ("cat", 3) -> ("dog", 4)
[2] -> ("bird", 2)
[3] -> ("fish", 1) -> ("hamster", 5) -> ("rabbit", 6)
[4] -> None
```

**Implementation:**
```python
class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)

        # Update if key exists
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return

        # Add new entry
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        raise KeyError(key)

    def delete(self, key):
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

        raise KeyError(key)
```

**Complexity:**
- Average case: O(1 + α) where α = n/m (load factor)
- Worst case: O(n) if all keys hash to same bucket

### 2. Open Addressing

All elements stored in the hash table itself. When collision occurs, probe for next available slot.

#### Linear Probing

```
Probe sequence: h(k), h(k)+1, h(k)+2, ..., h(k)+i

index = (hash(key) + i) % table_size
```

**Example:**
```
Insert 23, 43, 13, 27 into table of size 10
hash(x) = x % 10

hash(23) = 3 -> table[3] = 23
hash(43) = 3 (collision!) -> try table[4] = 43
hash(13) = 3 (collision!) -> try table[4] (occupied)
                          -> try table[5] = 13
hash(27) = 7 -> table[7] = 27

Table:
[0] [1] [2] [23] [43] [13] [6] [27] [8] [9]
            3    4    5         7
```

**Implementation:**
```python
class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)

        # Linear probing
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size

        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size

        raise KeyError(key)

    def delete(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                # Rehash subsequent entries
                self._rehash(index)
                return
            index = (index + 1) % self.size

        raise KeyError(key)

    def _rehash(self, start):
        """Rehash entries after deletion to maintain probing chain."""
        index = (start + 1) % self.size

        while self.keys[index] is not None:
            key, value = self.keys[index], self.values[index]
            self.keys[index] = None
            self.values[index] = None
            self.insert(key, value)
            index = (index + 1) % self.size
```

**Problems with Linear Probing:**
- **Primary Clustering**: Long runs of occupied slots form

#### Quadratic Probing

```
Probe sequence: h(k), h(k)+1^2, h(k)+2^2, h(k)+3^2, ...

index = (hash(key) + i^2) % table_size
```

**Reduces clustering but:**
- May not probe all positions
- Table size should be prime

#### Double Hashing

```
Probe sequence uses second hash function:
index = (hash1(key) + i * hash2(key)) % table_size

hash2 should never return 0
```

**Example:**
```python
def hash1(key, size):
    return key % size

def hash2(key, size):
    return 1 + (key % (size - 1))

# Probe: (hash1(k) + i * hash2(k)) % size
```

### Comparison of Collision Resolution

| Method | Pros | Cons |
|--------|------|------|
| Chaining | Simple, no clustering | Extra memory for pointers |
| Linear Probing | Cache-friendly, simple | Primary clustering |
| Quadratic Probing | Less clustering | May not find empty slot |
| Double Hashing | Best distribution | Two hash functions needed |

---

## Load Factor and Resizing

### Load Factor (α)

```
α = n / m

where:
  n = number of elements
  m = table size
```

**Impact on Performance:**
- α < 0.5: Sparse, fast lookups, wasted space
- α ≈ 0.75: Good balance (Python's default)
- α > 1.0: Many collisions, slower lookups

### Dynamic Resizing

When load factor exceeds threshold, **resize** the hash table:

```python
def resize(self):
    """
    1. Create new table (usually 2x size)
    2. Rehash all existing entries
    3. Replace old table
    """
    old_table = self.table
    self.size *= 2
    self.table = [[] for _ in range(self.size)]

    for bucket in old_table:
        for key, value in bucket:
            self.insert(key, value)  # Rehash
```

**Complexity:**
- Single resize: O(n)
- Amortized over n insertions: O(1) per insertion

**Proof of Amortized O(1):**
```
Insertions: 1, 2, 4, 8, 16, ...
Cost:       1, 2, 4, 8, 16, ...  (resize cost)

Total cost for n insertions:
= n + (1 + 2 + 4 + 8 + ... + n/2)
= n + (2n - 1)
= 3n - 1
= O(n)

Average per insertion = O(n)/n = O(1)
```

---

## Python dict Implementation

Python's dict uses **open addressing** with **random probing** (not linear).

### Key Features

1. **Hash Function**: Uses object's `__hash__()` method
2. **Collision Resolution**: Pseudo-random probing
3. **Load Factor**: Resize at 2/3 full
4. **Size**: Powers of 2 for fast modulo (bitwise AND)

### Internal Structure (Simplified)

```python
# Actual implementation is in C
class PyDict:
    def __init__(self):
        self.size = 8  # Initial size
        self.used = 0  # Number of entries
        # Actual storage
        self.entries = [None] * self.size

    def _hash(self, key):
        h = hash(key)
        # Use all bits of hash
        return h & (self.size - 1)  # Fast modulo for power of 2

    def _probe(self, hash_value):
        """Pseudo-random probing."""
        index = hash_value & (self.size - 1)
        perturb = hash_value

        while True:
            yield index
            perturb >>= 5  # Shift right
            index = (5 * index + perturb + 1) & (self.size - 1)
```

### Key Ordering

**Python 3.7+:** Dictionaries maintain insertion order!

```python
d = {}
d['c'] = 3
d['a'] = 1
d['b'] = 2

list(d.keys())  # ['c', 'a', 'b'] - insertion order
```

This is implemented using a compact array + hash table:

```
Entries Array (insertion order):
[0] = ('c', 3)
[1] = ('a', 1)
[2] = ('b', 2)

Hash Table (indices into entries):
[hash('c') % size] = 0
[hash('a') % size] = 1
[hash('b') % size] = 2
```

---

## Python Collections

### dict - Basic Hash Table

```python
# Creation
d = {'a': 1, 'b': 2}
d = dict(a=1, b=2)
d = dict([('a', 1), ('b', 2)])

# Operations
d['c'] = 3           # Insert/Update
value = d['a']       # Get (KeyError if missing)
value = d.get('x', 0)  # Get with default
del d['b']           # Delete
'a' in d             # Membership (O(1))

# Methods
d.keys()             # dict_keys(['a', 'b'])
d.values()           # dict_values([1, 2])
d.items()            # dict_items([('a', 1), ('b', 2)])
d.pop('a')           # Remove and return
d.clear()            # Remove all
d.update({'x': 10})  # Merge another dict
```

### defaultdict - Auto-initialize

```python
from collections import defaultdict

# With int (default 0)
counts = defaultdict(int)
counts['a'] += 1  # No KeyError, starts at 0

# With list (default [])
groups = defaultdict(list)
groups['fruits'].append('apple')

# With set (default set())
unique = defaultdict(set)
unique['vowels'].add('a')

# With lambda
d = defaultdict(lambda: 'N/A')
print(d['missing'])  # 'N/A'
```

### Counter - Frequency Counting

```python
from collections import Counter

# Creation
c = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
# Counter({'a': 3, 'b': 2, 'c': 1})

# Methods
c.most_common(2)     # [('a', 3), ('b', 2)]
c['a']               # 3
c['d']               # 0 (default for missing)

# Arithmetic
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
c1 + c2              # Counter({'a': 4, 'b': 3})
c1 - c2              # Counter({'a': 2})
c1 & c2              # Counter({'a': 1, 'b': 1}) - min
c1 | c2              # Counter({'a': 3, 'b': 2}) - max
```

### OrderedDict - Ordered Dictionary

```python
from collections import OrderedDict

# Maintains insertion order (dict does too in Python 3.7+)
od = OrderedDict()
od['c'] = 3
od['a'] = 1
od['b'] = 2

# Additional methods
od.move_to_end('a')      # Move to end
od.move_to_end('b', last=False)  # Move to beginning
od.popitem(last=True)    # Pop from end
od.popitem(last=False)   # Pop from beginning

# Use for LRU cache
class LRU:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

---

## Set Operations

A **set** is a hash table without values (only keys).

### Basic Set Operations

```python
# Creation
s = {1, 2, 3}
s = set([1, 2, 3])

# Operations
s.add(4)             # Add element
s.remove(2)          # Remove (KeyError if missing)
s.discard(2)         # Remove (no error if missing)
2 in s               # Membership O(1)
len(s)               # Size

# Set algebra
a = {1, 2, 3}
b = {2, 3, 4}

a | b                # Union: {1, 2, 3, 4}
a & b                # Intersection: {2, 3}
a - b                # Difference: {1}
a ^ b                # Symmetric difference: {1, 4}

# Subset/superset
a <= b               # Is subset
a < b                # Is proper subset
a >= b               # Is superset
```

### frozenset - Immutable Set

```python
# Hashable, can be dict key or set element
fs = frozenset([1, 2, 3])
d = {fs: 'value'}    # OK
s = {fs}             # OK

fs.add(4)            # ERROR: immutable
```

---

## Complexity Analysis

### Average Case (Good Hash Function)

| Operation | Time | Notes |
|-----------|------|-------|
| Insert | O(1) | Amortized with resizing |
| Delete | O(1) | |
| Lookup | O(1) | |
| Iteration | O(n) | |
| Space | O(n) | Plus overhead |

### Worst Case (All Collisions)

| Operation | Chaining | Open Addressing |
|-----------|----------|-----------------|
| Insert | O(n) | O(n) |
| Delete | O(n) | O(n) |
| Lookup | O(n) | O(n) |

**When Worst Case Occurs:**
- Poor hash function (all keys → same bucket)
- Adversarial input (hash collision attack)
- Very high load factor

### Space Complexity

```
Hash Table: O(m) where m ≥ n
- m = table size
- n = number of elements
- Overhead: α = n/m ≈ 0.75 in Python

Actual memory:
- Chaining: O(n + m) for pointers
- Open Addressing: O(m) fixed
```

### Amortized Analysis for Resizing

```
Sequence of n insertions:
- Most insertions: O(1)
- Resize operations: O(n), but rare

Total cost = n * O(1) + log(n) * O(n)
           = O(n)

Average per insertion = O(n) / n = O(1)
```

---

## Key Insights

1. **Hash Function Quality:** Critical for performance
   - Good distribution → O(1) average case
   - Poor distribution → O(n) worst case

2. **Load Factor:** Trade-off between space and time
   - Low α: Fast but wasteful
   - High α: Compact but slow

3. **Collision Resolution:** Depends on use case
   - Chaining: Simple, no clustering
   - Open addressing: Cache-friendly, less memory

4. **Python dict:** Highly optimized
   - Use built-in dict for production
   - Implement custom only for learning

5. **Hashability:** Keys must be immutable
   - OK: int, str, tuple, frozenset
   - NOT OK: list, dict, set

6. **Order:** Python 3.7+ dicts are ordered
   - Insertion order preserved
   - Use OrderedDict for move_to_end()

---

## Summary

**When to Use:**
- Fast lookup by key: dict
- Unique elements: set
- Frequency counting: Counter
- Auto-initialize: defaultdict
- LRU cache: OrderedDict

**Key Properties:**
- Average O(1) operations
- Requires hashable keys
- Load factor affects performance
- Python's implementation is excellent

**Common Pitfalls:**
- Using mutable keys (list, dict)
- Not handling KeyError
- Ignoring worst-case O(n) complexity
- Over-engineering custom hash functions
