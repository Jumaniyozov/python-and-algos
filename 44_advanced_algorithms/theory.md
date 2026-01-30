# Advanced Algorithms - Theory

## Table of Contents

1. [String Algorithms](#string-algorithms)
2. [KMP Algorithm](#kmp-algorithm)
3. [Rabin-Karp Algorithm](#rabin-karp-algorithm)
4. [Z-Algorithm](#z-algorithm)
5. [Manacher's Algorithm](#manachers-algorithm)
6. [Sliding Window Maximum](#sliding-window-maximum)
7. [LRU Cache](#lru-cache)
8. [LFU Cache](#lfu-cache)
9. [Advanced DP - Bitmask DP](#bitmask-dp)
10. [Advanced DP - Digit DP](#digit-dp)
11. [Monotonic Stack Advanced](#monotonic-stack-advanced)
12. [Monotonic Queue Advanced](#monotonic-queue-advanced)

---

## String Algorithms

### Why String Algorithms Matter

String processing is fundamental to:
- Text editors and word processors
- Search engines (Google, Bing)
- Bioinformatics (DNA sequencing)
- Compilers and interpreters
- Network security (pattern detection)
- Data compression

### Naive String Matching

```python
def naive_search(text, pattern):
    """
    Brute force pattern matching.
    Time: O(n × m) where n = len(text), m = len(pattern)
    Space: O(1)
    """
    n, m = len(text), len(pattern)

    for i in range(n - m + 1):
        # Check if pattern matches at position i
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            return i  # Found match

    return -1  # No match

# Example:
# text = "ABABDABACDABABCABAB"
# pattern = "ABABC"
#
# Checks:
# Position 0: ABABD != ABABC (fail at index 4)
# Position 1: BABDA != ABABC (fail at index 0)
# ...
# Position 10: ABABC == ABABC (success!)
#
# Total comparisons: Many wasteful comparisons
```

**Problem**: Naive approach doesn't use information from previous comparisons.

---

## KMP Algorithm

### Knuth-Morris-Pratt Algorithm

KMP avoids redundant comparisons by preprocessing the pattern to find overlapping prefixes and suffixes.

### Core Idea

```
When mismatch occurs, don't restart from scratch.
Use previous matches to skip ahead intelligently.

Example:
text    = "ABABABABC"
pattern = "ABABC"

Position 0:
ABABABABC
ABABC
    ↑ Mismatch at index 4

Instead of starting over at position 1,
we know "ABAB" matched, and "AB" prefix = "AB" suffix.
So jump to position 2 (skip 2 characters).

ABABABABC
  ABABC
    ↑ Continue from here
```

### LPS Array (Longest Proper Prefix which is also Suffix)

```
For pattern = "ABABC"

Index: 0  1  2  3  4
Char:  A  B  A  B  C
LPS:   0  0  1  2  0

Explanation:
- Index 0: "" has no proper prefix/suffix → 0
- Index 1: "A" has no matching prefix/suffix → 0
- Index 2: "AB" vs "A" → prefix "A" = suffix "A" → 1
- Index 3: "ABA" vs "AB" → prefix "AB" = suffix "AB" → 2
- Index 4: "ABAB" vs "C" → no match → 0
```

### KMP Implementation

```python
def kmp_search(text, pattern):
    """
    KMP string matching algorithm.

    Time Complexity: O(n + m)
    - Building LPS: O(m)
    - Searching: O(n)

    Space Complexity: O(m) for LPS array
    """
    n, m = len(text), len(pattern)

    if m == 0:
        return 0
    if m > n:
        return -1

    # Build LPS (Longest Proper Prefix Suffix) array
    lps = build_lps(pattern)

    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            return i - j  # Found match at index i-j

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                # Don't match lps[0..lps[j-1]] characters
                # They will match anyway
                j = lps[j - 1]
            else:
                i += 1

    return -1


def build_lps(pattern):
    """
    Build Longest Proper Prefix Suffix array.

    LPS[i] = length of longest proper prefix of pattern[0..i]
             which is also a suffix of pattern[0..i]
    """
    m = len(pattern)
    lps = [0] * m

    length = 0  # Length of previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Try shorter prefix
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


# Step-by-step example:
text = "ABABDABACDABABCABAB"
pattern = "ABABC"

# LPS array for "ABABC": [0, 0, 1, 2, 0]

# Matching process:
# i=0, j=0: A=A, match → i=1, j=1
# i=1, j=1: B=B, match → i=2, j=2
# i=2, j=2: A=A, match → i=3, j=3
# i=3, j=3: B=B, match → i=4, j=4
# i=4, j=4: D≠C, mismatch → j=lps[3]=2 (jump back)
# i=4, j=2: D≠A, mismatch → j=lps[1]=0
# i=4, j=0: D≠A, mismatch → i=5
# ...continue until match found
```

### Why KMP is O(n + m)

```
Analysis:
1. Building LPS array: O(m)
   - Each character processed once
   - Backtracking uses previously computed values

2. Searching text: O(n)
   - i always increases (never decreases)
   - j can decrease but total decrements ≤ total increments
   - Each character visited at most twice

Total: O(m) + O(n) = O(n + m)
```

---

## Rabin-Karp Algorithm

### Rolling Hash Concept

Instead of comparing characters, compare hash values.

```
Idea: Hash pattern and each text window.
If hashes match, verify with character comparison.

text = "ABCDEF"
pattern = "CDE"

Hash("ABC") = ?
Hash("BCD") = ? ← Can compute from Hash("ABC") efficiently!
Hash("CDE") = ?
```

### Polynomial Rolling Hash

```
For string S = s₀s₁s₂...sₙ₋₁

Hash(S) = (s₀ × dⁿ⁻¹ + s₁ × dⁿ⁻² + ... + sₙ₋₁) mod q

Where:
- d = base (usually 256 for ASCII)
- q = large prime number (to avoid overflow)

Example:
For "ABC" with d=256, q=101:
Hash = (65×256² + 66×256¹ + 67×256⁰) mod 101
     = (4259840 + 16896 + 67) mod 101
     = 4276803 mod 101
     = 68
```

### Rolling Hash Update

```
Given Hash(S[i..i+m-1]), compute Hash(S[i+1..i+m]) efficiently:

Remove first character: hash = hash - S[i] × d^(m-1)
Shift remaining: hash = hash × d
Add new character: hash = hash + S[i+m]
Take modulo: hash = hash mod q

Time: O(1) instead of O(m)!
```

### Rabin-Karp Implementation

```python
def rabin_karp(text, pattern):
    """
    Rabin-Karp string matching using rolling hash.

    Time Complexity:
    - Average: O(n + m)
    - Worst: O(n × m) if many hash collisions

    Space Complexity: O(1)
    """
    n, m = len(text), len(pattern)
    if m > n:
        return -1

    d = 256  # Number of characters in alphabet
    q = 101  # A prime number

    # Calculate hash value of pattern and first window
    pattern_hash = 0
    window_hash = 0
    h = 1  # d^(m-1) mod q

    # Calculate h = d^(m-1) mod q
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate initial hash values
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        window_hash = (d * window_hash + ord(text[i])) % q

    # Slide pattern over text
    for i in range(n - m + 1):
        # Check if hash values match
        if pattern_hash == window_hash:
            # Verify character by character (avoid false positives)
            if text[i:i+m] == pattern:
                return i

        # Calculate hash for next window
        if i < n - m:
            window_hash = (d * (window_hash - ord(text[i]) * h) +
                          ord(text[i + m])) % q

            # Convert negative hash to positive
            if window_hash < 0:
                window_hash += q

    return -1
```

### Multiple Pattern Matching

```python
def rabin_karp_multiple(text, patterns):
    """
    Find multiple patterns in text efficiently.

    Time: O(n + m₁ + m₂ + ... + mₖ) where k = number of patterns
    """
    d = 256
    q = 101
    results = {}

    # Build hash map of all pattern hashes
    pattern_hashes = {}
    for pattern in patterns:
        h = 0
        for char in pattern:
            h = (d * h + ord(char)) % q
        if h not in pattern_hashes:
            pattern_hashes[h] = []
        pattern_hashes[h].append(pattern)

    # Slide through text with all pattern lengths
    for pattern_length in set(len(p) for p in patterns):
        # Similar to single pattern search
        # Check if window hash matches any pattern hash
        pass

    return results
```

---

## Z-Algorithm

### Z-Array Definition

```
For string S, Z[i] = length of longest substring starting from S[i]
                     which is also a prefix of S

Example: S = "aabcaabxaaaz"

Index: 0  1  2  3  4  5  6  7  8  9 10 11
Char:  a  a  b  c  a  a  b  x  a  a  a  z
Z:     -  1  0  0  3  1  0  0  2  2  1  0

Explanation:
- Z[1] = 1: "a" matches prefix "a"
- Z[2] = 0: "b" doesn't match prefix "a"
- Z[4] = 3: "aab" matches prefix "aab"
- Z[8] = 2: "aa" matches prefix "aa"
```

### Z-Algorithm for Pattern Matching

```
Concatenate: S = pattern + "$" + text
where $ is a character not in pattern or text

Then find all i where Z[i] == len(pattern)

Example:
pattern = "aab"
text = "baabaa"
S = "aab$baabaa"

Z array: [-, 1, 0, 0, 0, 3, 1, 0, 3, 1]
                        ↑           ↑
                   Match at 5   Match at 8

Actual positions in text: 5-4 = 1, 8-4 = 4
```

### Z-Algorithm Implementation

```python
def z_algorithm(s):
    """
    Compute Z array for string s.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Z[i] = length of longest substring starting from s[i]
           which is also prefix of s
    """
    n = len(s)
    z = [0] * n
    z[0] = n  # Entire string matches itself

    l, r = 0, 0  # [l, r] is Z-box: substring matching prefix

    for i in range(1, n):
        if i > r:
            # Outside Z-box, compute naively
            l, r = i, i
            while r < n and s[r] == s[r - l]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            # Inside Z-box, use previously computed values
            k = i - l  # Corresponding position in prefix

            if z[k] < r - i + 1:
                # Fits completely within Z-box
                z[i] = z[k]
            else:
                # Extends beyond Z-box, compute extension
                l = i
                while r < n and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1

    return z


def z_search(text, pattern):
    """
    Find all occurrences of pattern in text using Z-algorithm.

    Time: O(n + m)
    Space: O(n + m)
    """
    # Create combined string
    s = pattern + "$" + text
    z = z_algorithm(s)

    pattern_len = len(pattern)
    matches = []

    # Find positions where Z[i] == pattern length
    for i in range(len(z)):
        if z[i] == pattern_len:
            # Position in original text
            matches.append(i - pattern_len - 1)

    return matches
```

---

## Manacher's Algorithm

### Longest Palindromic Substring Problem

```
Given string s, find longest palindromic substring.

Naive approach: O(n²) or O(n³)
Manacher's algorithm: O(n)
```

### Key Insight

```
Use previously computed palindrome information to avoid redundant checks.

If we know a palindrome centered at position c with radius r:
[.....|....c....|.....]
      l           r

Then for position i inside this palindrome:
- Mirror position i' = c - (i - c)
- Palindrome at i is at least min(palindrome[i'], r - i)
```

### String Preprocessing

```
Add special characters to handle even/odd length palindromes uniformly:

Original: "abba"
Modified: "#a#b#b#a#"

Original: "aba"
Modified: "#a#b#a#"

Now all palindromes have odd length in modified string!
```

### Manacher's Implementation

```python
def manacher(s):
    """
    Find longest palindromic substring using Manacher's algorithm.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Returns: (start_index, length)
    """
    # Preprocess string
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n  # p[i] = radius of palindrome centered at i

    center = 0  # Center of rightmost palindrome
    right = 0   # Right boundary of rightmost palindrome

    max_len = 0
    max_center = 0

    for i in range(1, n - 1):
        # Mirror of i with respect to center
        mirror = 2 * center - i

        if i < right:
            # Use previously computed values
            p[i] = min(right - i, p[mirror])

        # Attempt to expand palindrome centered at i
        while t[i + (1 + p[i])] == t[i - (1 + p[i])]:
            p[i] += 1

        # Update rightmost palindrome if we expanded past it
        if i + p[i] > right:
            center = i
            right = i + p[i]

        # Track longest palindrome
        if p[i] > max_len:
            max_len = p[i]
            max_center = i

    # Convert back to original string indices
    start = (max_center - max_len) // 2
    return s[start:start + max_len]


# Example walkthrough:
s = "babad"
# Preprocessed: "^#b#a#b#a#d#$"
#
# Index:  0 1 2 3 4 5 6 7 8 9 10 11 12
# Char:   ^ # b # a # b # a # d  #  $
# p:      0 0 1 0 3 0 1 4 1 0 1  0  0
#                     ↑
#              Max palindrome at index 7
#              Radius = 4
#              Original: "bab" or "aba"
```

### Why Manacher's is O(n)

```
Key observation: right boundary only moves forward

Proof:
- Each iteration either:
  1. Expands right boundary (increases right)
  2. Doesn't expand (uses precomputed value)

- right can increase at most n times
- Total expansions across all iterations ≤ n

Therefore: O(n) total time
```

---

## Sliding Window Maximum

### Problem Statement

```
Given array and window size k, find maximum in each window.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation:
Window [1  3  -1] → max = 3
Window [3  -1  -3] → max = 3
Window [-1  -3  5] → max = 5
Window [-3  5  3] → max = 5
Window [5  3  6] → max = 6
Window [3  6  7] → max = 7
```

### Naive Approach: O(n × k)

```python
def max_sliding_window_naive(nums, k):
    """
    Time: O(n × k) - For each window, find max in O(k)
    Space: O(1)
    """
    result = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        result.append(max(window))
    return result

# For n=1,000,000 and k=10,000: Too slow!
```

### Optimized: Monotonic Deque O(n)

```python
from collections import deque

def max_sliding_window(nums, k):
    """
    Use monotonic decreasing deque.

    Time Complexity: O(n)
    - Each element added once: O(n)
    - Each element removed once: O(n)
    Total: O(2n) = O(n)

    Space Complexity: O(k) for deque
    """
    deq = deque()  # Store indices
    result = []

    for i in range(len(nums)):
        # Remove indices outside current window
        while deq and deq[0] < i - k + 1:
            deq.popleft()

        # Remove smaller elements (they'll never be max)
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        # Add to result when window is full
        if i >= k - 1:
            result.append(nums[deq[0]])

    return result


# Example walkthrough:
nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3

# i=0: deq=[0], window not full
# i=1: deq=[1] (removed 0 as 1<3), window not full
# i=2: deq=[1,2], window full, max=nums[1]=3
# i=3: deq=[1,2,3], window full, max=nums[1]=3
# i=4: deq=[4] (removed all as 5 is largest), max=5
# i=5: deq=[4,5], max=5
# i=6: deq=[6] (removed all as 6 is largest), max=6
# i=7: deq=[7] (removed all as 7 is largest), max=7
```

### Monotonic Deque Properties

```
Invariant: Deque contains indices in decreasing order of values

Why it works:
1. Front of deque = maximum in current window
2. When new element arrives:
   - If larger than back elements, they'll never be max
   - Remove them to maintain monotonic property
3. Remove elements outside window from front

Deque always contains potential maximums for future windows
```

---

## LRU Cache

### Least Recently Used Cache

```
Cache with fixed capacity. When full:
- Evict least recently used item
- O(1) for both get and put

Operations:
- get(key): Return value, mark as recently used
- put(key, value): Add/update, evict LRU if needed
```

### Data Structure Design

```
Need:
1. O(1) lookup → HashMap
2. O(1) update order → Doubly Linked List
3. O(1) eviction → Remove from tail of list

Combination: HashMap + Doubly Linked List
```

### LRU Implementation

```python
class Node:
    """Doubly linked list node."""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache with O(1) get and put operations.

    Data Structures:
    - HashMap: key → node (O(1) lookup)
    - Doubly Linked List: maintain access order

    Most recent: head.next
    Least recent: tail.prev
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key → node

        # Dummy head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node):
        """Add node right after head (most recent)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove node from list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        """Move existing node to head (mark as recently used)."""
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self):
        """Remove and return least recently used node."""
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key):
        """
        Get value for key.
        Time: O(1)
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_head(node)  # Mark as recently used
        return node.value

    def put(self, key, value):
        """
        Put key-value pair.
        Time: O(1)
        """
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # Add new key
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)

            if len(self.cache) > self.capacity:
                # Evict LRU
                lru = self._remove_tail()
                del self.cache[lru.key]


# Usage:
cache = LRUCache(2)
cache.put(1, 1)  # cache: {1=1}
cache.put(2, 2)  # cache: {1=1, 2=2}
cache.get(1)     # returns 1, cache: {2=2, 1=1}
cache.put(3, 3)  # evicts key 2, cache: {1=1, 3=3}
cache.get(2)     # returns -1 (not found)
```

### Why O(1)?

```
get(key):
1. HashMap lookup: O(1)
2. Move to head: O(1) (pointer manipulation)
Total: O(1)

put(key, value):
1. HashMap lookup/insert: O(1)
2. Add to head or move to head: O(1)
3. Remove tail if needed: O(1)
Total: O(1)

All operations are O(1)!
```

---

## LFU Cache

### Least Frequently Used Cache

```
Evict least frequently used item.
If tie, evict least recently used.

Example:
put(1, 1) → freq[1]=1
put(2, 2) → freq[2]=1
get(1)    → freq[1]=2
put(3, 3) → evict 2 (freq=1, LRU among freq=1)
```

### LFU Implementation

```python
from collections import defaultdict, OrderedDict

class LFUCache:
    """
    LFU Cache with O(1) operations.

    Data Structures:
    - cache: key → (value, frequency)
    - freq_map: frequency → OrderedDict of keys
    - min_freq: track minimum frequency
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key → (value, freq)
        self.freq_map = defaultdict(OrderedDict)  # freq → {key: None}
        self.min_freq = 0

    def _update_freq(self, key):
        """Update frequency of key."""
        value, freq = self.cache[key]

        # Remove from current frequency list
        del self.freq_map[freq][key]

        # If this was the only key with min_freq, increment min_freq
        if not self.freq_map[freq] and freq == self.min_freq:
            self.min_freq += 1

        # Add to new frequency list
        freq += 1
        self.cache[key] = (value, freq)
        self.freq_map[freq][key] = None

    def get(self, key):
        """
        Get value and update frequency.
        Time: O(1)
        """
        if key not in self.cache:
            return -1

        self._update_freq(key)
        return self.cache[key][0]

    def put(self, key, value):
        """
        Put key-value and update frequency.
        Time: O(1)
        """
        if self.capacity == 0:
            return

        if key in self.cache:
            # Update existing key
            self.cache[key] = (value, self.cache[key][1])
            self._update_freq(key)
        else:
            # Add new key
            if len(self.cache) >= self.capacity:
                # Evict LFU (and LRU among LFU)
                evict_key = next(iter(self.freq_map[self.min_freq]))
                del self.freq_map[self.min_freq][evict_key]
                del self.cache[evict_key]

            # Add new key with frequency 1
            self.cache[key] = (value, 1)
            self.freq_map[1][key] = None
            self.min_freq = 1


# Usage:
cache = LFUCache(2)
cache.put(1, 1)  # cache: {1=1}, freq: {1: 1}
cache.put(2, 2)  # cache: {1=1, 2=2}, freq: {1: 2}
cache.get(1)     # cache: {1=1, 2=2}, freq: {1: 1, 2: 1}
cache.put(3, 3)  # evict key 2, cache: {1=1, 3=3}
cache.get(2)     # returns -1
cache.get(3)     # returns 3, freq: {1: 1, 2: 1}
```

---

## Bitmask DP

### Introduction to Bitmask DP

```
Use bitmask to represent subsets efficiently.

Example: Set {0, 1, 2, 3}
Subset {0, 2}: bitmask = 0101 = 5
Subset {1, 3}: bitmask = 1010 = 10

Operations:
- Check if i-th element in set: mask & (1 << i)
- Add i-th element: mask | (1 << i)
- Remove i-th element: mask & ~(1 << i)
- Iterate all subsets: for mask in range(1 << n)
```

### Classic Problem: Traveling Salesman

```python
def tsp(dist):
    """
    Traveling Salesman Problem using bitmask DP.

    dp[mask][i] = minimum cost to visit all cities in mask,
                  ending at city i

    Time: O(n² × 2ⁿ)
    Space: O(n × 2ⁿ)
    """
    n = len(dist)
    # dp[mask][i] = min cost to visit cities in mask, ending at i
    dp = [[float('inf')] * n for _ in range(1 << n)]

    # Start at city 0
    dp[1][0] = 0

    # Iterate all subsets
    for mask in range(1 << n):
        for i in range(n):
            # If i not in mask, skip
            if not (mask & (1 << i)):
                continue

            # Try adding city j
            for j in range(n):
                # If j already in mask, skip
                if mask & (1 << j):
                    continue

                # New mask with j added
                new_mask = mask | (1 << j)
                dp[new_mask][j] = min(dp[new_mask][j],
                                     dp[mask][i] + dist[i][j])

    # Return to starting city
    final_mask = (1 << n) - 1  # All cities visited
    return min(dp[final_mask][i] + dist[i][0] for i in range(1, n))
```

### Subset Sum with Bitmask

```python
def subset_sum_bitmask(nums, target):
    """
    Count subsets that sum to target using bitmask.

    Time: O(2ⁿ × n)
    Space: O(1)
    """
    n = len(nums)
    count = 0

    # Try all 2^n subsets
    for mask in range(1 << n):
        subset_sum = 0

        # Calculate sum of current subset
        for i in range(n):
            if mask & (1 << i):
                subset_sum += nums[i]

        if subset_sum == target:
            count += 1

    return count


# Optimized with DP:
def subset_sum_dp(nums, target):
    """
    DP approach for subset sum.

    dp[i][j] = can we achieve sum j using first i elements

    Time: O(n × target)
    Space: O(target)
    """
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        # Iterate backwards to avoid using same element twice
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]
```

---

## Digit DP

### Introduction

```
Digit DP solves counting problems on integers.

Example problems:
- Count numbers ≤ N with digit sum = K
- Count numbers in [L, R] without digit 4
- Count palindromic numbers in range
```

### Template

```python
def digit_dp(num_str):
    """
    Template for digit DP problems.

    State: (position, tight, state_specific_params)

    - position: current digit position
    - tight: whether we're still bounded by input
    - state_specific: depends on problem
    """
    memo = {}

    def dp(pos, tight, state):
        # Base case: processed all digits
        if pos == len(num_str):
            return 1 if check_condition(state) else 0

        # Memoization
        if (pos, tight, state) in memo:
            return memo[(pos, tight, state)]

        # Determine max digit we can use
        limit = int(num_str[pos]) if tight else 9

        result = 0
        for digit in range(0, limit + 1):
            new_tight = tight and (digit == limit)
            new_state = update_state(state, digit)
            result += dp(pos + 1, new_tight, new_state)

        memo[(pos, tight, state)] = result
        return result

    return dp(0, True, initial_state)
```

### Example: Count Numbers with Digit Sum

```python
def count_with_digit_sum(n, target_sum):
    """
    Count numbers from 1 to n with digit sum = target_sum.

    Time: O(log n × target_sum × 2)
    Space: O(log n × target_sum × 2)
    """
    s = str(n)
    memo = {}

    def dp(pos, tight, digit_sum):
        # Base case
        if pos == len(s):
            return 1 if digit_sum == target_sum else 0

        # Memoization
        if (pos, tight, digit_sum) in memo:
            return memo[(pos, tight, digit_sum)]

        limit = int(s[pos]) if tight else 9
        result = 0

        for digit in range(0, limit + 1):
            if digit_sum + digit <= target_sum:
                new_tight = tight and (digit == limit)
                result += dp(pos + 1, new_tight, digit_sum + digit)

        memo[(pos, tight, digit_sum)] = result
        return result

    return dp(0, True, 0)


# Example:
print(count_with_digit_sum(20, 5))
# Count: 5, 14 → 2 numbers
```

---

## Monotonic Stack Advanced

### Applications

```
1. Next Greater Element
2. Largest Rectangle in Histogram
3. Maximal Rectangle
4. Sum of Subarray Minimums
```

### Largest Rectangle in Histogram

```python
def largest_rectangle_area(heights):
    """
    Find largest rectangle in histogram.

    Time: O(n)
    Space: O(n)

    Key idea: For each bar, find:
    - Left boundary: first bar shorter than current
    - Right boundary: first bar shorter than current
    - Area = height[i] × (right - left - 1)
    """
    stack = []  # Store indices
    max_area = 0
    heights.append(0)  # Sentinel to pop all elements

    for i in range(len(heights)):
        # Pop while current height < stack top height
        while stack and heights[stack[-1]] > heights[i]:
            h_idx = stack.pop()
            h = heights[h_idx]

            # Width: from right after previous element to before current
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)

        stack.append(i)

    return max_area


# Example:
heights = [2, 1, 5, 6, 2, 3]
# Answer: 10 (5×2 rectangle)
```

---

## Monotonic Queue Advanced

### Applications

```
1. Sliding Window Maximum
2. Shortest Subarray with Sum ≥ K
3. Jump Game VI
```

### Shortest Subarray with Sum ≥ K

```python
from collections import deque

def shortest_subarray(nums, k):
    """
    Find shortest subarray with sum ≥ k.

    Time: O(n)
    Space: O(n)

    Use monotonic deque with prefix sums.
    """
    n = len(nums)
    prefix = [0] * (n + 1)

    # Build prefix sum
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    deq = deque()  # Store indices
    result = float('inf')

    for i in range(n + 1):
        # Check if we can form valid subarray
        while deq and prefix[i] - prefix[deq[0]] >= k:
            result = min(result, i - deq.popleft())

        # Maintain monotonic increasing deque
        while deq and prefix[i] <= prefix[deq[-1]]:
            deq.pop()

        deq.append(i)

    return result if result != float('inf') else -1
```

---

## Summary

### Algorithm Complexity Summary

```
Algorithm               Time        Space       When to Use
─────────────────────────────────────────────────────────────────
KMP                    O(n+m)      O(m)        Pattern matching
Rabin-Karp             O(n+m)avg   O(1)        Multiple patterns
Z-Algorithm            O(n+m)      O(n+m)      All occurrences
Manacher               O(n)        O(n)        Longest palindrome
Sliding Window Max     O(n)        O(k)        Window queries
LRU Cache              O(1)        O(n)        Cache with recency
LFU Cache              O(1)        O(n)        Cache with frequency
Bitmask DP             O(n×2ⁿ)     O(2ⁿ)       Small n, subsets
Digit DP               O(log n×k)  O(log n×k)  Count in range
Monotonic Stack        O(n)        O(n)        Next greater/smaller
```

### Key Takeaways

```
1. String algorithms eliminate redundant comparisons
2. Manacher's algorithm achieves O(n) for palindromes
3. Monotonic structures maintain useful invariants
4. Cache designs require careful data structure choice
5. Bitmask DP efficient for small sets (n ≤ 20)
6. Digit DP handles large range counting
7. Understanding time-space tradeoffs is crucial
```
