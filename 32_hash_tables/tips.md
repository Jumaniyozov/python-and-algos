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

---

## LeetCode Practice Problems

### 📊 Problem Statistics
- **Total Problems:** 70+
- **Easy:** 22 problems
- **Medium:** 33 problems
- **Hard:** 15 problems
- **Estimated Time:** 50-65 hours

---

## Easy Problems (22)

### 1. Two Sum
**Link:** https://leetcode.com/problems/two-sum/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table  
**Description:** Find two numbers that sum to target  
**Why Practice:** Most asked interview question, hash map basics

### 2. Contains Duplicate
**Link:** https://leetcode.com/problems/contains-duplicate/  
**Pattern:** Hash Set  
**Topics:** Array, Hash Table, Sorting  
**Description:** Check if array has duplicates  
**Why Practice:** Basic hash set usage

### 3. Valid Anagram
**Link:** https://leetcode.com/problems/valid-anagram/  
**Pattern:** Hash Map  
**Topics:** Hash Table, String, Sorting  
**Description:** Check if two strings are anagrams  
**Why Practice:** Character frequency counting

### 4. Intersection of Two Arrays
**Link:** https://leetcode.com/problems/intersection-of-two-arrays/  
**Pattern:** Hash Set  
**Topics:** Array, Hash Table, Two Pointers, Binary Search, Sorting  
**Description:** Find intersection (unique elements)  
**Why Practice:** Set operations

### 5. Happy Number
**Link:** https://leetcode.com/problems/happy-number/  
**Pattern:** Hash Set  
**Topics:** Hash Table, Math, Two Pointers  
**Description:** Determine if number is happy  
**Why Practice:** Cycle detection with hash set

### 6. First Unique Character in a String
**Link:** https://leetcode.com/problems/first-unique-character-in-a-string/  
**Pattern:** Hash Map  
**Topics:** Hash Table, String, Queue, Counting  
**Description:** Find first non-repeating character  
**Why Practice:** Frequency counting

### 7. Ransom Note
**Link:** https://leetcode.com/problems/ransom-note/  
**Pattern:** Hash Map  
**Topics:** Hash Table, String, Counting  
**Description:** Check if can construct ransom note  
**Why Practice:** Character counting validation

### 8. Isomorphic Strings
**Link:** https://leetcode.com/problems/isomorphic-strings/  
**Pattern:** Hash Map  
**Topics:** Hash Table, String  
**Description:** Check if strings are isomorphic  
**Why Practice:** Bijective mapping

### 9. Word Pattern
**Link:** https://leetcode.com/problems/word-pattern/  
**Pattern:** Hash Map  
**Topics:** Hash Table, String  
**Description:** Check if string follows pattern  
**Why Practice:** Pattern matching with hash map

### 10. Missing Number
**Link:** https://leetcode.com/problems/missing-number/  
**Pattern:** Hash Set / Math  
**Topics:** Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting  
**Description:** Find missing number in array  
**Why Practice:** Multiple solution approaches

### 11. Single Number
**Link:** https://leetcode.com/problems/single-number/  
**Pattern:** Hash Set / XOR  
**Topics:** Array, Bit Manipulation  
**Description:** Find element appearing once  
**Why Practice:** Hash set or XOR technique

### 12. Intersection of Two Arrays II
**Link:** https://leetcode.com/problems/intersection-of-two-arrays-ii/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table, Two Pointers, Binary Search, Sorting  
**Description:** Find intersection with duplicates  
**Why Practice:** Frequency tracking

### 13. Majority Element
**Link:** https://leetcode.com/problems/majority-element/  
**Pattern:** Hash Map / Boyer-Moore  
**Topics:** Array, Hash Table, Divide and Conquer, Sorting, Counting  
**Description:** Find element appearing > n/2 times  
**Why Practice:** Multiple approaches

### 14. Contains Duplicate II
**Link:** https://leetcode.com/problems/contains-duplicate-ii/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table, Sliding Window  
**Description:** Check duplicates within k distance  
**Why Practice:** Hash map with sliding window

### 15. Logger Rate Limiter
**Link:** https://leetcode.com/problems/logger-rate-limiter/  
**Pattern:** Hash Map  
**Topics:** Hash Table, Design  
**Description:** Rate limiting with hash map  
**Why Practice:** Practical hash map application (Premium)

### 16. Group Anagrams (Can be Medium)
**Link:** https://leetcode.com/problems/group-anagrams/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table, String, Sorting  
**Description:** Group strings that are anagrams  
**Why Practice:** Using sorted string as key

### 17. Find All Numbers Disappeared in Array
**Link:** https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/  
**Pattern:** Hash Set / Index Marking  
**Topics:** Array, Hash Table  
**Description:** Find missing numbers  
**Why Practice:** Space vs time trade-off

### 18. Jewels and Stones
**Link:** https://leetcode.com/problems/jewels-and-stones/  
**Pattern:** Hash Set  
**Topics:** Hash Table, String  
**Description:** Count jewels in stones  
**Why Practice:** Simple hash set lookup

### 19. Unique Email Addresses
**Link:** https://leetcode.com/problems/unique-email-addresses/  
**Pattern:** Hash Set  
**Topics:** Array, Hash Table, String  
**Description:** Count unique emails  
**Why Practice:** String normalization

### 20. Valid Sudoku
**Link:** https://leetcode.com/problems/valid-sudoku/  
**Pattern:** Hash Set  
**Topics:** Array, Hash Table, Matrix  
**Description:** Check if Sudoku is valid  
**Why Practice:** Multiple hash set tracking

### 21. Unique Morse Code Words
**Link:** https://leetcode.com/problems/unique-morse-code-words/  
**Pattern:** Hash Set  
**Topics:** Array, Hash Table, String  
**Description:** Count unique transformations  
**Why Practice:** Hash set for uniqueness

### 22. Uncommon Words from Two Sentences
**Link:** https://leetcode.com/problems/uncommon-words-from-two-sentences/  
**Pattern:** Hash Map  
**Topics:** Hash Table, String, Counting  
**Description:** Find words appearing once total  
**Why Practice:** Frequency counting across sources

---

## Medium Problems (33)

### 23. Group Anagrams
**Link:** https://leetcode.com/problems/group-anagrams/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table, String, Sorting  
**Description:** Group anagram strings  
**Why Practice:** Classic hash map with key transformation

### 24. Top K Frequent Elements
**Link:** https://leetcode.com/problems/top-k-frequent-elements/  
**Pattern:** Hash Map + Heap  
**Topics:** Array, Hash Table, Divide and Conquer, Sorting, Heap, Bucket Sort, Counting, Quickselect  
**Description:** Find k most frequent elements  
**Why Practice:** Multiple solution approaches

### 25. Sort Characters By Frequency
**Link:** https://leetcode.com/problems/sort-characters-by-frequency/  
**Pattern:** Hash Map + Sorting  
**Topics:** Hash Table, String, Sorting, Heap, Bucket Sort, Counting  
**Description:** Sort by character frequency  
**Why Practice:** Frequency-based sorting

### 26. Subarray Sum Equals K
**Link:** https://leetcode.com/problems/subarray-sum-equals-k/  
**Pattern:** Hash Map + Prefix Sum  
**Topics:** Array, Hash Table, Prefix Sum  
**Description:** Count subarrays with sum K  
**Why Practice:** VERY IMPORTANT - prefix sum technique

### 27. Longest Consecutive Sequence
**Link:** https://leetcode.com/problems/longest-consecutive-sequence/  
**Pattern:** Hash Set  
**Topics:** Array, Hash Table, Union Find  
**Description:** Find longest consecutive sequence  
**Why Practice:** O(n) solution with hash set

### 28. Find All Anagrams in a String
**Link:** https://leetcode.com/problems/find-all-anagrams-in-a-string/  
**Pattern:** Hash Map + Sliding Window  
**Topics:** Hash Table, String, Sliding Window  
**Description:** Find all anagram start indices  
**Why Practice:** Sliding window with hash map

### 29. 4Sum II
**Link:** https://leetcode.com/problems/4sum-ii/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table  
**Description:** Count quadruplets with sum 0  
**Why Practice:** Reducing complexity with hash map

### 30. Longest Substring Without Repeating Characters
**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/  
**Pattern:** Hash Map + Sliding Window  
**Topics:** Hash Table, String, Sliding Window  
**Description:** Longest substring with unique characters  
**Why Practice:** Classic sliding window problem

### 31. Minimum Window Substring
**Link:** https://leetcode.com/problems/minimum-window-substring/  
**Pattern:** Hash Map + Sliding Window  
**Topics:** Hash Table, String, Sliding Window  
**Description:** Minimum window containing all characters  
**Why Practice:** VERY IMPORTANT - advanced sliding window

### 32. Contiguous Array
**Link:** https://leetcode.com/problems/contiguous-array/  
**Pattern:** Hash Map + Prefix Sum  
**Topics:** Array, Hash Table, Prefix Sum  
**Description:** Longest subarray with equal 0s and 1s  
**Why Practice:** Prefix sum variant

### 33. Longest Palindrome
**Link:** https://leetcode.com/problems/longest-palindrome/  
**Pattern:** Hash Map  
**Topics:** Hash Table, String, Greedy  
**Description:** Length of longest palindrome  
**Why Practice:** Character frequency analysis

### 34. Bulls and Cows
**Link:** https://leetcode.com/problems/bulls-and-cows/  
**Pattern:** Hash Map  
**Topics:** Hash Table, String, Counting  
**Description:** Calculate bulls and cows  
**Why Practice:** Frequency matching

### 35. Design HashMap
**Link:** https://leetcode.com/problems/design-hashmap/  
**Pattern:** Design  
**Topics:** Array, Hash Table, Linked List, Design, Hash Function  
**Description:** Implement HashMap from scratch  
**Why Practice:** Understanding hash table internals

### 36. Design HashSet
**Link:** https://leetcode.com/problems/design-hashset/  
**Pattern:** Design  
**Topics:** Array, Hash Table, Linked List, Design, Hash Function  
**Description:** Implement HashSet from scratch  
**Why Practice:** Hash set fundamentals

### 37. Brick Wall
**Link:** https://leetcode.com/problems/brick-wall/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table  
**Description:** Find position with most gaps  
**Why Practice:** Creative hash map usage

### 38. Custom Sort String
**Link:** https://leetcode.com/problems/custom-sort-string/  
**Pattern:** Hash Map  
**Topics:** Hash Table, String, Sorting  
**Description:** Sort string by custom order  
**Why Practice:** Frequency + ordering

### 39. Valid Anagram (Extended)
**Link:** https://leetcode.com/problems/find-all-anagrams-in-a-string/  
**Pattern:** Hash Map + Sliding Window  
**Topics:** Hash Table, String, Sliding Window  
**Description:** All anagram positions  
**Why Practice:** Fixed-size sliding window

### 40. Find Duplicate File in System
**Link:** https://leetcode.com/problems/find-duplicate-file-in-system/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table, String  
**Description:** Group files by content  
**Why Practice:** Real-world hash map application

### 41. Encode and Decode TinyURL
**Link:** https://leetcode.com/problems/encode-and-decode-tinyurl/  
**Pattern:** Hash Map  
**Topics:** Hash Table, String, Design, Hash Function  
**Description:** Design URL shortener  
**Why Practice:** Bidirectional hash map

### 42. Maximum Size Subarray Sum Equals k
**Link:** https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/  
**Pattern:** Hash Map + Prefix Sum  
**Topics:** Array, Hash Table, Prefix Sum  
**Description:** Longest subarray with sum k  
**Why Practice:** Extension of subarray sum (Premium)

### 43. Longest Substring with At Most K Distinct Characters
**Link:** https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/  
**Pattern:** Hash Map + Sliding Window  
**Topics:** Hash Table, String, Sliding Window  
**Description:** Longest with <= K distinct chars  
**Why Practice:** Variable sliding window (Premium)

### 44. 3Sum with Multiplicity
**Link:** https://leetcode.com/problems/3sum-with-multiplicity/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table, Two Pointers, Counting  
**Description:** Count triplets with sum  
**Why Practice:** Hash map for counting

### 45. Most Common Word
**Link:** https://leetcode.com/problems/most-common-word/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table, String, Counting  
**Description:** Find most common non-banned word  
**Why Practice:** String processing + frequency

### 46. Longest Word in Dictionary
**Link:** https://leetcode.com/problems/longest-word-in-dictionary/  
**Pattern:** Hash Set / Trie  
**Topics:** Array, Hash Table, String, Trie, Sorting  
**Description:** Find longest buildable word  
**Why Practice:** Hash set for lookups

### 47. Keyboard Row
**Link:** https://leetcode.com/problems/keyboard-row/  
**Pattern:** Hash Set  
**Topics:** Array, Hash Table, String  
**Description:** Find words in one keyboard row  
**Why Practice:** Simple hash set filtering

### 48. Subdomain Visit Count
**Link:** https://leetcode.com/problems/subdomain-visit-count/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table, String, Counting  
**Description:** Count subdomain visits  
**Why Practice:** Hierarchical counting

### 49. Repeated DNA Sequences
**Link:** https://leetcode.com/problems/repeated-dna-sequences/  
**Pattern:** Hash Set  
**Topics:** Hash Table, String, Bit Manipulation, Sliding Window, Rolling Hash  
**Description:** Find repeated 10-letter sequences  
**Why Practice:** Sliding window with hash set

### 50. Insert Delete GetRandom O(1)
**Link:** https://leetcode.com/problems/insert-delete-getrandom-o1/  
**Pattern:** Hash Map + Array  
**Topics:** Array, Hash Table, Math, Design, Randomized  
**Description:** Design data structure with O(1) operations  
**Why Practice:** Combining hash map with array

### 51. Find and Replace Pattern
**Link:** https://leetcode.com/problems/find-and-replace-pattern/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table, String  
**Description:** Find words matching pattern  
**Why Practice:** Isomorphic matching

### 52. Longest Harmonious Subsequence
**Link:** https://leetcode.com/problems/longest-harmonious-subsequence/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table, Sorting  
**Description:** Longest with max-min = 1  
**Why Practice:** Frequency + constraint

### 53. Friend Circles (can use hash)
**Link:** https://leetcode.com/problems/number-of-provinces/  
**Pattern:** Union Find / DFS  
**Topics:** Depth-First Search, Breadth-First Search, Union Find, Graph  
**Description:** Count connected components  
**Why Practice:** Hash map for grouping

### 54. Contains Duplicate III
**Link:** https://leetcode.com/problems/contains-duplicate-iii/  
**Pattern:** Hash Table / BST  
**Topics:** Array, Hash Table, Sliding Window, Sorting, Bucket Sort, Ordered Set  
**Description:** Check duplicates with value/index constraints  
**Why Practice:** Bucket/window technique

### 55. Fraction to Recurring Decimal
**Link:** https://leetcode.com/problems/fraction-to-recurring-decimal/  
**Pattern:** Hash Map  
**Topics:** Hash Table, Math, String  
**Description:** Convert fraction to decimal string  
**Why Practice:** Detecting cycles with hash map

---

## Hard Problems (15)

### 56. LRU Cache
**Link:** https://leetcode.com/problems/lru-cache/  
**Pattern:** Hash Map + Doubly Linked List  
**Topics:** Hash Table, Linked List, Design, Doubly-Linked List  
**Description:** Implement LRU cache  
**Why Practice:** MUST KNOW - very common interview question

### 57. LFU Cache
**Link:** https://leetcode.com/problems/lfu-cache/  
**Pattern:** Hash Map + Doubly Linked List  
**Topics:** Hash Table, Linked List, Design, Doubly-Linked List  
**Description:** Implement LFU cache  
**Why Practice:** More complex than LRU

### 58. All O`one Data Structure
**Link:** https://leetcode.com/problems/all-oone-data-structure/  
**Pattern:** Hash Map + Doubly Linked List  
**Topics:** Hash Table, Linked List, Design, Doubly-Linked List  
**Description:** Inc, dec, getMax, getMin in O(1)  
**Why Practice:** Complex data structure design

### 59. Substring with Concatenation of All Words
**Link:** https://leetcode.com/problems/substring-with-concatenation-of-all-words/  
**Pattern:** Hash Map + Sliding Window  
**Topics:** Hash Table, String, Sliding Window  
**Description:** Find all concatenation start indices  
**Why Practice:** Complex sliding window with hash map

### 60. First Missing Positive (can use hash)
**Link:** https://leetcode.com/problems/first-missing-positive/  
**Pattern:** Hash Set / Index Marking  
**Topics:** Array, Hash Table  
**Description:** Find smallest missing positive  
**Why Practice:** O(1) space challenge

### 61. Longest Substring with At Most Two Distinct Characters
**Link:** https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/  
**Pattern:** Hash Map + Sliding Window  
**Topics:** Hash Table, String, Sliding Window  
**Description:** Longest with <= 2 distinct  
**Why Practice:** Sliding window constraint (Premium)

### 62. Max Points on a Line
**Link:** https://leetcode.com/problems/max-points-on-a-line/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table, Math, Geometry  
**Description:** Find max points on same line  
**Why Practice:** Hash map for slope counting

### 63. Shortest Distance from All Buildings
**Link:** https://leetcode.com/problems/shortest-distance-from-all-buildings/  
**Pattern:** BFS + Hash Map  
**Topics:** Array, Breadth-First Search, Matrix  
**Description:** Find optimal meeting point  
**Why Practice:** Complex BFS with tracking (Premium)

### 64. Insert Delete GetRandom O(1) - Duplicates allowed
**Link:** https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/  
**Pattern:** Hash Map + Array  
**Topics:** Array, Hash Table, Math, Design, Randomized  
**Description:** Same as 50 but allow duplicates  
**Why Practice:** More complex than basic version

### 65. Count of Smaller Numbers After Self (can use hash)
**Link:** https://leetcode.com/problems/count-of-smaller-numbers-after-self/  
**Pattern:** Multiple approaches  
**Topics:** Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set  
**Description:** Count smaller to the right  
**Why Practice:** Multiple advanced techniques

### 66. Shortest Subarray with Sum at Least K
**Link:** https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/  
**Pattern:** Hash Map + Prefix Sum + Monotonic Queue  
**Topics:** Array, Binary Search, Queue, Sliding Window, Heap, Prefix Sum, Monotonic Queue  
**Description:** Shortest subarray with sum >= K  
**Why Practice:** Combining multiple techniques

### 67. Alien Dictionary
**Link:** https://leetcode.com/problems/alien-dictionary/  
**Pattern:** Graph + Hash Map  
**Topics:** Array, String, Depth-First Search, Breadth-First Search, Graph, Topological Sort  
**Description:** Derive alien language order  
**Why Practice:** Topological sort application (Premium)

### 68. Count Unique Characters of All Substrings
**Link:** https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/  
**Pattern:** Hash Map  
**Topics:** Hash Table, String, Dynamic Programming  
**Description:** Count unique chars across all substrings  
**Why Practice:** Advanced counting technique

### 69. Subarrays with K Different Integers
**Link:** https://leetcode.com/problems/subarrays-with-k-different-integers/  
**Pattern:** Hash Map + Sliding Window  
**Topics:** Array, Hash Table, Sliding Window, Counting  
**Description:** Count subarrays with exactly K distinct  
**Why Practice:** AtMost(K) - AtMost(K-1) technique

### 70. Palindrome Pairs
**Link:** https://leetcode.com/problems/palindrome-pairs/  
**Pattern:** Hash Map + Trie  
**Topics:** Array, Hash Table, String, Trie  
**Description:** Find palindrome word pairs  
**Why Practice:** Complex string matching

---

## Practice Progression

### Week 1-2: Basics (Easy 1-15)
Master fundamentals:
- Two Sum (1) - MUST master first
- Hash set basics (2, 4, 5, 11)
- Frequency counting (3, 6, 7, 12)
- Pattern matching (8, 9)

### Week 3: Advanced Easy (Easy 16-22)
Complete easy problems:
- Group anagrams basics (16)
- Validation with hash (20)
- Set uniqueness (18, 19, 21)

### Week 4-5: Core Medium (Medium 23-35)
Essential medium patterns:
- **Subarray Sum Equals K (26)** - CRITICAL
- **Longest Consecutive (27)** - IMPORTANT
- **Sliding window with hash (28, 30, 31)** - ESSENTIAL
- Design problems (35, 36)

### Week 6-7: Advanced Medium (Medium 36-50)
Complex applications:
- **Insert Delete GetRandom (50)** - IMPORTANT
- Prefix sum variations (32, 42)
- Real-world applications (40, 41, 48)

### Week 8-9: More Medium (Medium 51-55)
Complete medium section:
- Pattern matching (51)
- Constraint problems (54, 55)
- Complex counting (53)

### Week 10-11: Hard Problems (Hard 56-70)
Master hard concepts:
- **LRU Cache (56)** - MUST KNOW, very common
- **LFU Cache (57)** - Shows mastery
- All O'one (58) - Complex design
- Advanced sliding window (59, 61, 69)
- Complex applications (62, 67, 70)

---

## Pattern Mastery Guide

### Hash Map + Prefix Sum
**Key Problems:** 26, 32, 42, 66
**Template:**
```python
def subarray_sum(nums, k):
    prefix_sum = {0: 1}
    current_sum = count = 0
    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sum:
            count += prefix_sum[current_sum - k]
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
    return count
```
**Why Important:** O(n) solution for subarray problems

### Hash Map + Sliding Window
**Key Problems:** 28, 30, 31, 43, 59, 61, 69
**When to Use:** Variable-size window with constraints
**Key Insight:** Track window state with hash map

### Design with Hash Map
**Key Problems:** 35, 36, 50, 56, 57, 58, 64
**Patterns:**
- Hash map + array for O(1) random access
- Hash map + doubly linked list for ordering
- Multiple hash maps for complex state

### Frequency Counting
**Key Problems:** 3, 6, 23, 24, 25, 45, 52
**Template:**
```python
from collections import Counter
freq = Counter(items)
# or
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1
```

---

## Must-Know Problems (Top 15)

1. **Two Sum (1)** - MUST KNOW, most asked
2. **Group Anagrams (23)** - Very common
3. **Subarray Sum Equals K (26)** - CRITICAL pattern
4. **Longest Consecutive Sequence (27)** - Shows hash set mastery
5. **Longest Substring Without Repeating (30)** - Classic
6. **Minimum Window Substring (31)** - Advanced sliding window
7. **4Sum II (29)** - Optimization technique
8. **Top K Frequent Elements (24)** - Multiple approaches
9. **Design HashMap (35)** - Understanding internals
10. **Insert Delete GetRandom (50)** - Creative design
11. **LRU Cache (56)** - MUST KNOW, extremely common
12. **LFU Cache (57)** - Shows advanced design
13. **Substring with Concatenation (59)** - Complex sliding window
14. **All O'one Data Structure (58)** - Advanced design
15. **Subarrays with K Different (69)** - Advanced counting

---

## Common Mistakes

1. **Not handling hash collisions:** Design problems need collision handling
2. **Wrong hash function:** Use appropriate keys (sorted string, tuple, etc.)
3. **Forgetting edge cases:** Empty input, single element, all same
4. **Memory leaks in design:** Not removing old entries
5. **Not optimizing space:** Sometimes need to use indices instead of values
6. **Ignoring time complexity:** Some operations might be O(n) in worst case

---

## Interview Tips

### Hash Map Recognition
**Keywords:** "count", "frequency", "unique", "anagram", "sum equals", "longest/shortest"
**Pattern:** When you need O(1) lookup/insert

### Time Allocation
- Easy: 10-15 minutes
- Medium: 20-35 minutes
- Hard: 40-55 minutes

### Strategy
1. **Clarify constraints:** Can values be negative? Duplicates allowed?
2. **Start simple:** Brute force first, then optimize with hash
3. **Discuss trade-offs:** Time vs space, hash map vs other structures
4. **Handle collisions:** For design problems, explain collision resolution
5. **Test edge cases:** Empty, single element, all duplicates

### For Design Problems (LRU/LFU)
1. **Draw the structure:** Show how hash map connects to list
2. **Walk through operations:** Demonstrate get/put step by step
3. **Discuss complexity:** Prove O(1) for all operations
4. **Handle edge cases:** Capacity 0, eviction when full

---

**Total Practice Time:** 50-65 hours  
**Recommended Pace:** 6-8 problems per week  
**Mastery Timeline:** 10-12 weeks

Remember: Hash tables are the Swiss Army knife of data structures. Master them and you'll solve problems much faster!

---

## Additional Resources

### Related Topics
- **Trie problems:** Often combine with hash map
- **Union Find:** Alternative for grouping problems
- **Bit manipulation:** Can replace hash set for small ranges

### Python-Specific Tips
```python
# defaultdict for cleaner code
from collections import defaultdict
freq = defaultdict(int)  # No need for get()

# Counter for frequency
from collections import Counter
freq = Counter(items)
most_common = freq.most_common(k)

# OrderedDict for ordered hash map
from collections import OrderedDict
ordered = OrderedDict()  # Maintains insertion order
```

