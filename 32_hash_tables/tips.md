# Hash Tables: Tips and Patterns

## Table of Contents
1. [When to Use Hash Tables](#when-to-use-hash-tables)
2. [Common Patterns](#common-patterns)
3. [Python Dict Best Practices](#python-dict-best-practices)
4. [Optimization Techniques](#optimization-techniques)
5. [Common Pitfalls](#common-pitfalls)
6. [Interview Tips](#interview-tips)

---

## When to Use Hash Tables

### Use Hash Table When:

**Pattern Recognition:**
- Need **O(1) lookup** by key
- **Counting frequencies**
- **Detecting duplicates**
- **Grouping** related items
- **Caching** or **memoization**
- **Two Sum** and pairing problems

**Examples:**
```python
# Frequency counting
from collections import Counter
counts = Counter(['a', 'b', 'a', 'c', 'b', 'a'])

# Grouping
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    groups[item.category].append(item)

# Caching
cache = {}
def expensive_function(n):
    if n in cache:
        return cache[n]
    result = ... # expensive computation
    cache[n] = result
    return result

# Two Sum pattern
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

---

## Common Patterns

### Pattern 1: Complement Pattern

**When:** Find pair that sums to target

```python
def two_sum(nums, target):
    """
    Store complements as you go.
    Time: O(n), Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

**Variations:**
- Three Sum: Fix one, two sum on rest
- Four Sum: Fix two, two sum on rest
- Subarray sum = k: Use prefix sums

### Pattern 2: Frequency Counting

**When:** Count occurrences of elements

```python
from collections import Counter

# Basic counting
def top_k_frequent(nums, k):
    """Most frequent k elements."""
    count = Counter(nums)
    return count.most_common(k)

# Character frequency
def is_anagram(s, t):
    """Check if anagram using counts."""
    return Counter(s) == Counter(t)

# Sliding window with counts
def find_anagrams(s, p):
    """Find all anagram substrings."""
    p_count = Counter(p)
    window = Counter()
    result = []
    
    for i in range(len(s)):
        window[s[i]] += 1
        if i >= len(p):
            if window[s[i-len(p)]] == 1:
                del window[s[i-len(p)]]
            else:
                window[s[i-len(p)]] -= 1
        
        if i >= len(p) - 1 and window == p_count:
            result.append(i - len(p) + 1)
    
    return result
```

### Pattern 3: Grouping

**When:** Group items by common property

```python
from collections import defaultdict

def group_anagrams(strs):
    """
    Group strings that are anagrams.
    Time: O(n * k log k), Space: O(n * k)
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Use sorted string as key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())


def group_anagrams_optimized(strs):
    """
    Optimized using character counts.
    Time: O(n * k), Space: O(n * k)
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Count characters
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        # Use tuple as key (hashable)
        key = tuple(count)
        groups[key].append(s)
    
    return list(groups.values())
```

### Pattern 4: Prefix Sum + Hash Table

**When:** Find subarray with sum = k

```python
def subarray_sum(nums, k):
    """
    Count subarrays with sum = k.
    
    Key insight: If prefix[i] - prefix[j] = k,
    then subarray[j+1:i+1] has sum k.
    
    Time: O(n), Space: O(n)
    """
    count = 0
    prefix = 0
    freq = {0: 1}  # prefix_sum -> frequency
    
    for num in nums:
        prefix += num
        
        # Check if (prefix - k) exists
        if prefix - k in freq:
            count += freq[prefix - k]
        
        # Record current prefix
        freq[prefix] = freq.get(prefix, 0) + 1
    
    return count


def continuous_subarray_sum(nums, k):
    """
    Check if subarray sum is multiple of k.
    Use modulo as key!
    
    Time: O(n), Space: O(min(n, k))
    """
    prefix = 0
    mod_seen = {0: -1}  # mod -> index
    
    for i, num in enumerate(nums):
        prefix += num
        
        if k != 0:
            prefix %= k
        
        if prefix in mod_seen:
            # Found subarray
            if i - mod_seen[prefix] >= 2:
                return True
        else:
            mod_seen[prefix] = i
    
    return False
```

### Pattern 5: Sliding Window + Hash Table

**When:** Track elements in current window

```python
def length_of_longest_substring(s):
    """
    Longest substring without repeating characters.
    
    Time: O(n), Space: O(min(n, m))
    """
    char_index = {}  # char -> last seen index
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If char in current window, move start
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length


def min_window(s, t):
    """
    Minimum window substring containing all chars of t.
    
    Time: O(n + m), Space: O(m)
    """
    from collections import Counter
    
    if not s or not t:
        return ""
    
    t_count = Counter(t)
    window = Counter()
    
    required = len(t_count)
    formed = 0
    
    left = 0
    min_len = float('inf')
    result = (0, 0)
    
    for right in range(len(s)):
        # Expand window
        char = s[right]
        window[char] += 1
        
        if char in t_count and window[char] == t_count[char]:
            formed += 1
        
        # Contract window
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = (left, right)
            
            char = s[left]
            window[char] -= 1
            if char in t_count and window[char] < t_count[char]:
                formed -= 1
            
            left += 1
    
    return "" if min_len == float('inf') else s[result[0]:result[1]+1]
```

### Pattern 6: Bidirectional Mapping

**When:** Need one-to-one correspondence

```python
def is_isomorphic(s, t):
    """
    Check if strings are isomorphic.
    Need bijection: s -> t AND t -> s
    
    Time: O(n), Space: O(1) - at most 256 chars
    """
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for cs, ct in zip(s, t):
        # Check s -> t mapping
        if cs in s_to_t:
            if s_to_t[cs] != ct:
                return False
        else:
            s_to_t[cs] = ct
        
        # Check t -> s mapping
        if ct in t_to_s:
            if t_to_s[ct] != cs:
                return False
        else:
            t_to_s[ct] = cs
    
    return True


def word_pattern(pattern, s):
    """
    Check if string follows pattern.
    Similar to isomorphic strings.
    
    Time: O(n), Space: O(n)
    """
    words = s.split()
    
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for c, w in zip(pattern, words):
        if c in char_to_word:
            if char_to_word[c] != w:
                return False
        else:
            char_to_word[c] = w
        
        if w in word_to_char:
            if word_to_char[w] != c:
                return False
        else:
            word_to_char[w] = c
    
    return True
```

---

## Python Dict Best Practices

### Choosing Right Collection

```python
# Basic dict - general purpose
d = {'a': 1, 'b': 2}

# defaultdict - auto-initialize
from collections import defaultdict
counts = defaultdict(int)
groups = defaultdict(list)
unique = defaultdict(set)

# Counter - frequency counting
from collections import Counter
freq = Counter(['a', 'b', 'a'])
freq.most_common(2)  # [('a', 2), ('b', 1)]

# OrderedDict - maintain order + move_to_end
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od.move_to_end('a')  # Move to end

# set - membership testing
seen = set()
seen.add(1)
1 in seen  # O(1)
```

### Common Idioms

```python
# Get with default
value = d.get(key, default)

# Set if not exists
d.setdefault(key, []).append(item)

# Update multiple
d.update({'a': 1, 'b': 2})

# Merge dicts (Python 3.9+)
merged = d1 | d2

# Iterate items
for key, value in d.items():
    pass

# Dict comprehension
squares = {x: x**2 for x in range(10)}

# Invert dict
inverted = {v: k for k, v in d.items()}
```

### Performance Tips

```python
# Check existence
if key in d:  # O(1)
    pass

# Avoid KeyError
value = d.get(key)  # Returns None if missing
value = d.get(key, 0)  # Custom default

# Conditional update
if key not in d:
    d[key] = value
# OR
d.setdefault(key, value)

# Delete safely
d.pop(key, None)  # No KeyError if missing

# Clear efficiently
d.clear()  # Better than d = {}
```

---

## Optimization Techniques

### 1. Use Set for Membership

```python
# BAD - O(n) per check
def contains_duplicate(nums):
    for i in range(len(nums)):
        if nums[i] in nums[:i]:  # O(n) check
            return True
    return False

# GOOD - O(1) per check
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:  # O(1) check
            return True
        seen.add(num)
    return False
```

### 2. Counter for Frequencies

```python
# BAD - manual counting
def top_k_frequent(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    # ... more code

# GOOD - use Counter
from collections import Counter
def top_k_frequent(nums, k):
    count = Counter(nums)
    return count.most_common(k)
```

### 3. Tuple Keys for Composite

```python
# Multiple values as key
visited = set()
visited.add((x, y))  # Tuple is hashable

# Character counts as key
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)  # Tuple is hashable
        groups[key].append(s)
    return list(groups.values())
```

### 4. Early Termination

```python
def is_anagram(s, t):
    # Quick checks first
    if len(s) != len(t):
        return False  # Early exit
    
    from collections import Counter
    return Counter(s) == Counter(t)
```

---

## Common Pitfalls

### Pitfall 1: Using Mutable Keys

```python
# BAD - list is not hashable
d = {[1, 2]: 'value'}  # TypeError

# GOOD - use tuple
d = {(1, 2): 'value'}  # OK

# BAD - dict as key
d = {{1: 2}: 'value'}  # TypeError

# GOOD - use frozenset or tuple
d = {frozenset({1, 2}): 'value'}  # OK
```

### Pitfall 2: Not Handling Missing Keys

```python
# BAD - KeyError if key missing
value = d[key]

# GOOD - handle missing key
value = d.get(key)  # Returns None
value = d.get(key, default)  # Custom default

# OR use defaultdict
from collections import defaultdict
d = defaultdict(int)
d['missing']  # Returns 0, no error
```

### Pitfall 3: Modifying While Iterating

```python
# BAD - RuntimeError
for key in d:
    if condition:
        del d[key]  # Can't modify during iteration

# GOOD - iterate over copy
for key in list(d.keys()):
    if condition:
        del d[key]

# OR collect keys to delete
to_delete = [k for k in d if condition]
for k in to_delete:
    del d[k]
```

### Pitfall 4: Shallow Copy Issues

```python
# BAD - shallow copy
d1 = {'a': [1, 2]}
d2 = d1.copy()
d2['a'].append(3)  # Affects d1!

# GOOD - deep copy
import copy
d2 = copy.deepcopy(d1)
d2['a'].append(3)  # d1 unchanged
```

### Pitfall 5: Hash Collisions

```python
# Even with good hash function, collisions happen
# Python handles this, but be aware:

# Custom __hash__ must match __eq__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

---

## Interview Tips

### 1. Problem Recognition

**Ask yourself:**
- Need fast lookup? → Hash table
- Counting frequencies? → Counter
- Detecting duplicates? → Set
- Grouping items? → defaultdict
- Finding pairs? → Complement pattern

### 2. Clarify Constraints

**Important questions:**
- Are keys unique?
- Can values be None?
- What's the range of keys?
- Hash function provided or custom?
- Order matter?

### 3. Start with Brute Force

```python
# Brute force Two Sum
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # O(n²)

# Then optimize with hash table
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []  # O(n)
```

### 4. Consider Space-Time Tradeoffs

```python
# More space, less time
def group_anagrams_fast(strs):
    # O(n*k) time, O(n*k) space
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())

# Less space, more time
def group_anagrams_slow(strs):
    # O(n²*k) time, O(1) extra space
    result = []
    used = set()
    for i, s1 in enumerate(strs):
        if i in used:
            continue
        group = [s1]
        for j in range(i + 1, len(strs)):
            if j not in used and is_anagram(s1, strs[j]):
                group.append(strs[j])
                used.add(j)
        result.append(group)
    return result
```

### 5. Test Edge Cases

```python
# Always test:
test_cases = [
    [],              # Empty
    [1],             # Single element
    [1, 1, 1],       # All duplicates
    [1, 2, 3],       # All unique
    [1, 2, 1, 3],    # Mixed
]
```

### 6. Complexity Analysis

**State clearly:**
- Time: O(n) for hash table lookups
- Space: O(n) for storing n elements
- Average vs worst case

```python
def solution():
    """
    Time: O(n) average, O(n²) worst (all collisions)
    Space: O(n) for hash table
    """
    pass
```

---

## Quick Reference

```python
# Basic operations
d = {}
d[key] = value      # Insert/Update - O(1)
value = d[key]      # Get - O(1), KeyError if missing
del d[key]          # Delete - O(1)
key in d            # Check - O(1)

# Safe operations
d.get(key, default) # Get with default
d.pop(key, default) # Remove with default
d.setdefault(key, default)  # Set if not exists

# Collections
from collections import Counter, defaultdict, OrderedDict
Counter(iterable)   # Frequency counting
defaultdict(type)   # Auto-initialize
OrderedDict()       # Ordered dict

# Set operations
s = set()
s.add(x)            # Add - O(1)
s.remove(x)         # Remove - O(1), KeyError
s.discard(x)        # Remove - O(1), no error
x in s              # Check - O(1)

# Set algebra
a | b               # Union
a & b               # Intersection
a - b               # Difference
a ^ b               # Symmetric difference
```

---

## Summary

**Key Takeaways:**
1. Hash tables provide O(1) average time operations
2. Use appropriate collection: dict, Counter, defaultdict, set
3. Master common patterns: complement, frequency, grouping
4. Handle edge cases: missing keys, empty input
5. Consider space-time tradeoffs
6. Use tuple for composite hashable keys
7. Understand average vs worst case complexity

Practice these patterns until they become second nature!
