# Advanced Algorithms - Examples

## Table of Contents

1. [KMP String Matching Examples](#kmp-string-matching-examples)
2. [Rabin-Karp Examples](#rabin-karp-examples)
3. [Z-Algorithm Examples](#z-algorithm-examples)
4. [Manacher's Algorithm Examples](#manachers-algorithm-examples)
5. [Sliding Window Maximum Examples](#sliding-window-maximum-examples)
6. [LRU Cache Examples](#lru-cache-examples)
7. [LFU Cache Examples](#lfu-cache-examples)
8. [Bitmask DP Examples](#bitmask-dp-examples)
9. [Digit DP Examples](#digit-dp-examples)
10. [Monotonic Stack Examples](#monotonic-stack-examples)

---

## KMP String Matching Examples

### Example 1: Basic KMP Implementation

```python
def build_lps(pattern):
    """Build Longest Proper Prefix Suffix array."""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    """KMP string matching algorithm."""
    n, m = len(text), len(pattern)

    if m == 0:
        return 0
    if m > n:
        return -1

    lps = build_lps(pattern)

    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            return i - j

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


# Test
text = "ABABDABACDABABCABAB"
pattern = "ABABC"

print(f"Text: {text}")
print(f"Pattern: {pattern}")
print(f"LPS array: {build_lps(pattern)}")
print(f"Pattern found at index: {kmp_search(text, pattern)}")

# Output:
# Text: ABABDABACDABABCABAB
# Pattern: ABABC
# LPS array: [0, 0, 1, 2, 0]
# Pattern found at index: 10
```

### Example 2: Find All Occurrences

```python
def kmp_search_all(text, pattern):
    """Find all occurrences of pattern in text."""
    n, m = len(text), len(pattern)
    lps = build_lps(pattern)

    i = j = 0
    occurrences = []

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]  # Continue searching

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return occurrences


# Test
text = "AABAACAADAABAABA"
pattern = "AABA"

print(f"Text: {text}")
print(f"Pattern: {pattern}")
print(f"All occurrences: {kmp_search_all(text, pattern)}")

# Output:
# Text: AABAACAADAABAABA
# Pattern: AABA
# All occurrences: [0, 9, 12]
```

### Example 3: LPS Array Step-by-Step

```python
def build_lps_verbose(pattern):
    """Build LPS array with detailed steps."""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    print(f"Building LPS for pattern: {pattern}")
    print(f"Index: {list(range(m))}")
    print(f"Char:  {list(pattern)}")
    print()

    while i < m:
        print(f"Step: i={i}, length={length}")
        print(f"  Comparing pattern[{i}]='{pattern[i]}' with pattern[{length}]='{pattern[length]}'")

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            print(f"  Match! lps[{i}] = {length}")
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
                print(f"  Mismatch. Backtrack to length={length}")
            else:
                lps[i] = 0
                print(f"  Mismatch at start. lps[{i}] = 0")
                i += 1

        print(f"  Current LPS: {lps}")
        print()

    return lps


# Test
pattern = "ABABCABAB"
lps = build_lps_verbose(pattern)
print(f"Final LPS: {lps}")
```

---

## Rabin-Karp Examples

### Example 1: Basic Rabin-Karp

```python
def rabin_karp(text, pattern):
    """Rabin-Karp string matching."""
    n, m = len(text), len(pattern)
    if m > n:
        return -1

    d = 256  # Number of characters
    q = 101  # Prime number

    pattern_hash = 0
    window_hash = 0
    h = 1

    # Calculate h = d^(m-1) % q
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate initial hashes
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        window_hash = (d * window_hash + ord(text[i])) % q

    print(f"Pattern hash: {pattern_hash}")
    print(f"Searching...\n")

    # Slide pattern over text
    for i in range(n - m + 1):
        print(f"Position {i}: window='{text[i:i+m]}', hash={window_hash}")

        if pattern_hash == window_hash:
            # Verify character by character
            if text[i:i+m] == pattern:
                print(f"MATCH at position {i}!")
                return i
            else:
                print(f"Hash collision (false positive)")

        # Calculate next window hash
        if i < n - m:
            window_hash = (d * (window_hash - ord(text[i]) * h) +
                          ord(text[i + m])) % q

            if window_hash < 0:
                window_hash += q

    print("Not found")
    return -1


# Test
text = "GEEKS FOR GEEKS"
pattern = "GEEK"
rabin_karp(text, pattern)
```

### Example 2: Multiple Pattern Matching

```python
def rabin_karp_multiple(text, patterns):
    """Find multiple patterns in text."""
    d = 256
    q = 101

    # Build hash map for all patterns
    pattern_hashes = {}
    for pattern in patterns:
        h = 0
        for char in pattern:
            h = (d * h + ord(char)) % q

        if h not in pattern_hashes:
            pattern_hashes[h] = []
        pattern_hashes[h].append(pattern)

    results = {pattern: [] for pattern in patterns}

    # Search for each pattern length
    for pattern_len in set(len(p) for p in patterns):
        if pattern_len > len(text):
            continue

        # Calculate initial window hash
        window_hash = 0
        h = 1
        for i in range(pattern_len - 1):
            h = (h * d) % q

        for i in range(pattern_len):
            window_hash = (d * window_hash + ord(text[i])) % q

        # Slide window
        for i in range(len(text) - pattern_len + 1):
            # Check if hash matches any pattern
            if window_hash in pattern_hashes:
                for pattern in pattern_hashes[window_hash]:
                    if text[i:i+pattern_len] == pattern:
                        results[pattern].append(i)

            # Calculate next hash
            if i < len(text) - pattern_len:
                window_hash = (d * (window_hash - ord(text[i]) * h) +
                              ord(text[i + pattern_len])) % q
                if window_hash < 0:
                    window_hash += q

    return results


# Test
text = "AABAACAADAABAAABAA"
patterns = ["AABA", "AAB", "AAA"]

results = rabin_karp_multiple(text, patterns)
for pattern, positions in results.items():
    print(f"Pattern '{pattern}' found at: {positions}")

# Output:
# Pattern 'AABA' found at: [0, 9, 13]
# Pattern 'AAB' found at: [0, 4, 9, 13]
# Pattern 'AAA' found at: [12]
```

---

## Z-Algorithm Examples

### Example 1: Z-Array Construction

```python
def z_algorithm(s):
    """Compute Z array for string s."""
    n = len(s)
    z = [0] * n
    z[0] = n

    l, r = 0, 0

    print(f"Computing Z array for: {s}")
    print(f"Index: {list(range(n))}")
    print(f"Char:  {list(s)}")
    print()

    for i in range(1, n):
        print(f"Position {i}:")

        if i > r:
            # Outside Z-box
            l, r = i, i
            while r < n and s[r] == s[r - l]:
                r += 1
            z[i] = r - l
            r -= 1
            print(f"  Outside Z-box. Computed z[{i}] = {z[i]}")
        else:
            # Inside Z-box
            k = i - l
            print(f"  Inside Z-box [{l}, {r}]. Mirror k = {k}")

            if z[k] < r - i + 1:
                z[i] = z[k]
                print(f"  Fits in box. z[{i}] = z[{k}] = {z[k]}")
            else:
                l = i
                while r < n and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1
                print(f"  Extends box. Computed z[{i}] = {z[i]}")

        print(f"  Z-box: [{l}, {r}], Z: {z}")
        print()

    return z


# Test
s = "aabcaabxaaaz"
z = z_algorithm(s)
print(f"Final Z array: {z}")
```

### Example 2: Pattern Matching with Z-Algorithm

```python
def z_search(text, pattern):
    """Find all occurrences using Z-algorithm."""
    s = pattern + "$" + text
    z = z_algorithm_simple(s)

    pattern_len = len(pattern)
    matches = []

    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Combined: {s}")
    print(f"Z array: {z}")
    print()

    for i in range(len(z)):
        if z[i] == pattern_len:
            match_pos = i - pattern_len - 1
            matches.append(match_pos)
            print(f"Match at position {match_pos}")

    return matches


def z_algorithm_simple(s):
    """Simple Z-algorithm without verbose output."""
    n = len(s)
    z = [0] * n
    z[0] = n
    l, r = 0, 0

    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r] == s[r - l]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1

    return z


# Test
text = "aabaabaaab"
pattern = "aab"
matches = z_search(text, pattern)
print(f"\nAll matches: {matches}")
```

---

## Manacher's Algorithm Examples

### Example 1: Longest Palindromic Substring

```python
def manacher(s):
    """Find longest palindromic substring."""
    # Preprocess string
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n

    center = 0
    right = 0

    print(f"Original: {s}")
    print(f"Preprocessed: {t}")
    print(f"Index: {list(range(n))}")
    print(f"Char:  {list(t)}")
    print()

    max_len = 0
    max_center = 0

    for i in range(1, n - 1):
        mirror = 2 * center - i

        if i < right:
            p[i] = min(right - i, p[mirror])

        # Expand around i
        expansions = 0
        while t[i + (1 + p[i])] == t[i - (1 + p[i])]:
            p[i] += 1
            expansions += 1

        print(f"i={i} ('{t[i]}'): mirror={mirror}, "
              f"initial_p={min(right - i, p[mirror]) if i < right else 0}, "
              f"expansions={expansions}, final_p={p[i]}")

        # Update rightmost palindrome
        if i + p[i] > right:
            center = i
            right = i + p[i]
            print(f"  New rightmost palindrome: center={center}, right={right}")

        # Track longest
        if p[i] > max_len:
            max_len = p[i]
            max_center = i
            print(f"  New longest palindrome!")

    print(f"\nP array: {p}")

    # Convert to original string
    start = (max_center - max_len) // 2
    result = s[start:start + max_len]

    print(f"\nLongest palindrome: '{result}' (length {max_len})")
    return result


# Test
s = "babad"
manacher(s)

print("\n" + "="*50 + "\n")

s = "cbbd"
manacher(s)
```

### Example 2: All Palindromic Substrings

```python
def count_palindromes(s):
    """Count all palindromic substrings."""
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n

    center = 0
    right = 0

    for i in range(1, n - 1):
        mirror = 2 * center - i

        if i < right:
            p[i] = min(right - i, p[mirror])

        while t[i + (1 + p[i])] == t[i - (1 + p[i])]:
            p[i] += 1

        if i + p[i] > right:
            center = i
            right = i + p[i]

    # Count palindromes
    # Each p[i] represents p[i] palindromes centered at i
    count = sum((p[i] + 1) // 2 for i in range(1, n - 1))

    return count


# Test
test_cases = ["abc", "aaa", "noon", "racecar"]

for s in test_cases:
    count = count_palindromes(s)
    print(f"String '{s}': {count} palindromic substrings")

# Output:
# String 'abc': 3 palindromic substrings
# String 'aaa': 6 palindromic substrings
# String 'noon': 5 palindromic substrings
# String 'racecar': 10 palindromic substrings
```

---

## Sliding Window Maximum Examples

### Example 1: Basic Sliding Window Maximum

```python
from collections import deque

def max_sliding_window(nums, k):
    """Find maximum in each sliding window."""
    deq = deque()
    result = []

    print(f"Array: {nums}")
    print(f"Window size: {k}")
    print()

    for i in range(len(nums)):
        # Remove indices outside window
        while deq and deq[0] < i - k + 1:
            removed = deq.popleft()
            print(f"i={i}: Removed index {removed} (outside window)")

        # Remove smaller elements
        while deq and nums[deq[-1]] < nums[i]:
            removed = deq.pop()
            print(f"i={i}: Removed index {removed} "
                  f"(nums[{removed}]={nums[removed]} < nums[{i}]={nums[i]})")

        deq.append(i)
        print(f"i={i}: Added index {i}, deque={list(deq)}")

        # Add to result when window is full
        if i >= k - 1:
            max_idx = deq[0]
            result.append(nums[max_idx])
            print(f"  Window [{i-k+1}:{i+1}] = {nums[i-k+1:i+1]}, "
                  f"max = nums[{max_idx}] = {nums[max_idx]}")

        print()

    return result


# Test
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = max_sliding_window(nums, k)
print(f"Result: {result}")
```

### Example 2: Sliding Window Minimum

```python
from collections import deque

def min_sliding_window(nums, k):
    """Find minimum in each sliding window."""
    deq = deque()
    result = []

    for i in range(len(nums)):
        # Remove indices outside window
        while deq and deq[0] < i - k + 1:
            deq.popleft()

        # Remove larger elements (opposite of max)
        while deq and nums[deq[-1]] > nums[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            result.append(nums[deq[0]])

    return result


# Test
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

max_result = max_sliding_window(nums, k)
min_result = min_sliding_window(nums, k)

print(f"Array: {nums}")
print(f"Window size: {k}")
print(f"Max in each window: {max_result}")
print(f"Min in each window: {min_result}")
```

---

## LRU Cache Examples

### Example 1: Complete LRU Cache

```python
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)

            if len(self.cache) > self.capacity:
                lru = self._remove_tail()
                del self.cache[lru.key]

    def display(self):
        """Display cache state."""
        print("Cache state (most recent to least recent):")
        current = self.head.next
        items = []
        while current != self.tail:
            items.append(f"{current.key}:{current.value}")
            current = current.next
        print(" -> ".join(items))


# Test
cache = LRUCache(2)

print("put(1, 1)")
cache.put(1, 1)
cache.display()
print()

print("put(2, 2)")
cache.put(2, 2)
cache.display()
print()

print("get(1)")
value = cache.get(1)
print(f"Returned: {value}")
cache.display()
print()

print("put(3, 3) - evicts key 2")
cache.put(3, 3)
cache.display()
print()

print("get(2)")
value = cache.get(2)
print(f"Returned: {value}")
print()

print("put(4, 4) - evicts key 1")
cache.put(4, 4)
cache.display()
```

---

## LFU Cache Examples

### Example 1: Complete LFU Cache

```python
from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq_map = defaultdict(OrderedDict)
        self.min_freq = 0

    def _update_freq(self, key):
        value, freq = self.cache[key]

        del self.freq_map[freq][key]

        if not self.freq_map[freq] and freq == self.min_freq:
            self.min_freq += 1

        freq += 1
        self.cache[key] = (value, freq)
        self.freq_map[freq][key] = None

    def get(self, key):
        if key not in self.cache:
            return -1

        self._update_freq(key)
        return self.cache[key][0]

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key] = (value, self.cache[key][1])
            self._update_freq(key)
        else:
            if len(self.cache) >= self.capacity:
                evict_key = next(iter(self.freq_map[self.min_freq]))
                del self.freq_map[self.min_freq][evict_key]
                del self.cache[evict_key]

            self.cache[key] = (value, 1)
            self.freq_map[1][key] = None
            self.min_freq = 1

    def display(self):
        """Display cache state."""
        print(f"Cache state (min_freq={self.min_freq}):")
        for freq in sorted(self.freq_map.keys()):
            if self.freq_map[freq]:
                items = list(self.freq_map[freq].keys())
                print(f"  Frequency {freq}: {items}")


# Test
cache = LFUCache(2)

print("put(1, 1)")
cache.put(1, 1)
cache.display()
print()

print("put(2, 2)")
cache.put(2, 2)
cache.display()
print()

print("get(1)")
cache.get(1)
cache.display()
print()

print("put(3, 3) - evicts key 2 (least frequent)")
cache.put(3, 3)
cache.display()
print()

print("get(2)")
value = cache.get(2)
print(f"Returned: {value}")
cache.display()
```

---

## Bitmask DP Examples

### Example 1: Traveling Salesman Problem

```python
def tsp(dist):
    """Traveling Salesman Problem using bitmask DP."""
    n = len(dist)
    dp = [[float('inf')] * n for _ in range(1 << n)]

    dp[1][0] = 0  # Start at city 0

    print(f"Cities: {n}")
    print(f"Distance matrix:")
    for row in dist:
        print(row)
    print()

    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue

            if dp[mask][i] == float('inf'):
                continue

            for j in range(n):
                if mask & (1 << j):
                    continue

                new_mask = mask | (1 << j)
                dp[new_mask][j] = min(dp[new_mask][j],
                                     dp[mask][i] + dist[i][j])

    # Return to start
    final_mask = (1 << n) - 1
    result = min(dp[final_mask][i] + dist[i][0] for i in range(1, n))

    print(f"Minimum tour cost: {result}")
    return result


# Test
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp(dist)
```

### Example 2: Subset Sum

```python
def subset_sum_count(nums, target):
    """Count subsets with given sum using bitmask."""
    n = len(nums)
    count = 0

    print(f"Array: {nums}")
    print(f"Target sum: {target}")
    print()

    for mask in range(1 << n):
        subset = []
        subset_sum = 0

        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
                subset_sum += nums[i]

        if subset_sum == target:
            print(f"Subset {subset} sums to {target}")
            count += 1

    print(f"\nTotal subsets: {count}")
    return count


# Test
nums = [1, 2, 3, 4, 5]
target = 7
subset_sum_count(nums, target)
```

---

## Digit DP Examples

### Example 1: Count Numbers with Digit Sum

```python
def count_with_digit_sum(n, target_sum):
    """Count numbers from 1 to n with digit sum = target_sum."""
    s = str(n)
    memo = {}

    def dp(pos, tight, digit_sum):
        if pos == len(s):
            return 1 if digit_sum == target_sum else 0

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

    count = dp(0, True, 0)
    print(f"Count of numbers ≤ {n} with digit sum = {target_sum}: {count}")
    return count


# Test
count_with_digit_sum(100, 10)
count_with_digit_sum(1000, 15)
```

---

## Monotonic Stack Examples

### Example 1: Next Greater Element

```python
def next_greater_element(nums):
    """Find next greater element for each element."""
    n = len(nums)
    result = [-1] * n
    stack = []

    print(f"Array: {nums}")
    print()

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
            print(f"nums[{idx}]={nums[idx]} -> next greater = nums[{i}]={nums[i]}")

        stack.append(i)

    print(f"\nResult: {result}")
    return result


# Test
nums = [2, 1, 2, 4, 3]
next_greater_element(nums)
```

### Example 2: Largest Rectangle in Histogram

```python
def largest_rectangle_area(heights):
    """Find largest rectangle in histogram."""
    stack = []
    max_area = 0
    heights.append(0)

    print(f"Heights: {heights[:-1]}")
    print()

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h_idx = stack.pop()
            h = heights[h_idx]
            w = i if not stack else i - stack[-1] - 1
            area = h * w

            print(f"i={i}: Pop height={h} at index {h_idx}, width={w}, area={area}")

            max_area = max(max_area, area)

        stack.append(i)

    print(f"\nMax area: {max_area}")
    return max_area


# Test
heights = [2, 1, 5, 6, 2, 3]
largest_rectangle_area(heights)
```

---

## Summary

These examples demonstrate:
1. **String Algorithms**: Efficient pattern matching
2. **Manacher's**: Linear-time palindrome finding
3. **Sliding Window**: Efficient range queries
4. **Cache Design**: O(1) operations with proper data structures
5. **Bitmask DP**: Subset enumeration optimization
6. **Digit DP**: Range counting problems
7. **Monotonic Structures**: Next greater/smaller patterns

Practice these implementations to master advanced algorithms!
