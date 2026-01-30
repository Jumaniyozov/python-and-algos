# Advanced Algorithms - Tips and Best Practices

## Quick Reference Guide

### Algorithm Selection Matrix

```
Problem Type              Algorithm           Time        When to Use
────────────────────────────────────────────────────────────────────────
Pattern matching         KMP                 O(n+m)      Exact string match
Multiple patterns        Rabin-Karp          O(n+m)      Rolling hash works
Palindrome substring     Manacher            O(n)        Need longest palindrome
Sliding window max       Monotonic Deque     O(n)        Range queries
Cache with recency       LRU Cache           O(1)        Recent access matters
Cache with frequency     LFU Cache           O(1)        Access count matters
Subset problems (n≤20)   Bitmask DP          O(n×2ⁿ)     Small sets
Range counting           Digit DP            O(log n×k)  Large number ranges
Next greater/smaller     Monotonic Stack     O(n)        Comparison with neighbors
```

---

## Pattern Recognition Guide

### Pattern 1: String Matching

**When to use**: Finding substring in text, pattern matching

**Algorithms**:
- KMP: Single pattern, need all occurrences
- Rabin-Karp: Multiple patterns, approximate matching
- Z-Algorithm: All prefix matches, simple implementation

**Key indicators**:
- "Find pattern in text"
- "Count occurrences"
- "Repeated substring"

```python
# Template: KMP
def kmp_search(text, pattern):
    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1
```

---

### Pattern 2: Palindrome Problems

**When to use**: Finding palindromic substrings, palindrome queries

**Algorithms**:
- Manacher: Longest palindromic substring in O(n)
- Expand around center: Simple, O(n²)
- DP: Multiple queries

**Key indicators**:
- "Longest palindrome"
- "Count palindromes"
- "Palindromic substring"

```python
# Template: Manacher's
def manacher(s):
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n
    center = right = 0

    for i in range(1, n - 1):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])

        while t[i + (1 + p[i])] == t[i - (1 + p[i])]:
            p[i] += 1

        if i + p[i] > right:
            center, right = i, i + p[i]

    max_len = max(p)
    max_center = p.index(max_len)
    start = (max_center - max_len) // 2
    return s[start:start + max_len]
```

---

### Pattern 3: Sliding Window Maximum/Minimum

**When to use**: Range queries on sliding window

**Algorithm**: Monotonic deque

**Key indicators**:
- "Maximum/minimum in window"
- "Sliding window of size k"
- "Range query"

```python
# Template: Sliding Window Maximum
from collections import deque

def max_sliding_window(nums, k):
    deq = deque()
    result = []

    for i in range(len(nums)):
        # Remove outside window
        while deq and deq[0] < i - k + 1:
            deq.popleft()

        # Remove smaller elements
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            result.append(nums[deq[0]])

    return result
```

---

### Pattern 4: Cache Design

**When to use**: Need O(1) get/put with eviction policy

**Structures**:
- LRU: HashMap + Doubly Linked List
- LFU: HashMap + Frequency Map + OrderedDict

**Key indicators**:
- "Design cache"
- "O(1) operations"
- "Eviction policy"

```python
# Template: LRU Cache
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

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
```

---

### Pattern 5: Bitmask DP

**When to use**: Subset enumeration, small n (≤ 20)

**Key indicators**:
- "All subsets"
- "Assignment problem"
- "n ≤ 20"
- "Distinct elements"

```python
# Template: TSP
def tsp(dist):
    n = len(dist)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue

            for j in range(n):
                if mask & (1 << j):
                    continue

                new_mask = mask | (1 << j)
                dp[new_mask][j] = min(dp[new_mask][j],
                                     dp[mask][i] + dist[i][j])

    final_mask = (1 << n) - 1
    return min(dp[final_mask][i] + dist[i][0] for i in range(1, n))
```

---

### Pattern 6: Digit DP

**When to use**: Count numbers in range with properties

**Key indicators**:
- "Count numbers from 1 to n"
- "Digit sum = k"
- "No repeated digits"
- "Number properties"

```python
# Template: Digit DP
def digit_dp(n, property_check):
    s = str(n)
    memo = {}

    def dp(pos, tight, state):
        if pos == len(s):
            return 1 if property_check(state) else 0

        if (pos, tight, state) in memo:
            return memo[(pos, tight, state)]

        limit = int(s[pos]) if tight else 9
        result = 0

        for digit in range(0, limit + 1):
            new_tight = tight and (digit == limit)
            new_state = update_state(state, digit)
            result += dp(pos + 1, new_tight, new_state)

        memo[(pos, tight, state)] = result
        return result

    return dp(0, True, initial_state)
```

---

### Pattern 7: Monotonic Stack

**When to use**: Next greater/smaller element

**Key indicators**:
- "Next greater element"
- "Previous smaller element"
- "Largest rectangle"
- "Stock span"

```python
# Template: Next Greater Element
def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result
```

---

## 50+ LeetCode Problems by Topic

### String Algorithms (KMP, Rabin-Karp, Z-Algorithm)

1. **[28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)** - Easy
   - Pattern: KMP basic implementation
   - Time: O(n + m)

2. **[214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)** - Hard
   - Pattern: KMP for palindrome
   - Time: O(n)

3. **[459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)** - Easy
   - Pattern: KMP LPS array
   - Time: O(n)

4. **[686. Repeated String Match](https://leetcode.com/problems/repeated-string-match/)** - Medium
   - Pattern: Rabin-Karp
   - Time: O(n)

5. **[1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)** - Hard
   - Pattern: Binary search + Rabin-Karp
   - Time: O(n log n)

6. **[1392. Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/)** - Hard
   - Pattern: KMP LPS
   - Time: O(n)

7. **[1397. Find All Good Strings](https://leetcode.com/problems/find-all-good-strings/)** - Hard
   - Pattern: KMP + Digit DP
   - Time: O(n × m)

---

### Palindrome Problems (Manacher's Algorithm)

8. **[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)** - Medium
   - Pattern: Manacher's algorithm
   - Time: O(n)

9. **[647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)** - Medium
   - Pattern: Manacher's to count
   - Time: O(n)

10. **[1147. Longest Chunked Palindrome Decomposition](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/)** - Hard
    - Pattern: Greedy + rolling hash
    - Time: O(n)

11. **[1312. Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)** - Hard
    - Pattern: LCS variant
    - Time: O(n²)

12. **[336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)** - Hard
    - Pattern: Trie or HashMap
    - Time: O(n × k²)

---

### Sliding Window Maximum

13. **[239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)** - Hard
    - Pattern: Monotonic deque
    - Time: O(n)

14. **[1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)** - Medium
    - Pattern: Two monotonic deques
    - Time: O(n)

15. **[1499. Max Value of Equation](https://leetcode.com/problems/max-value-of-equation/)** - Hard
    - Pattern: Monotonic deque with transformation
    - Time: O(n)

16. **[1696. Jump Game VI](https://leetcode.com/problems/jump-game-vi/)** - Medium
    - Pattern: DP + monotonic deque
    - Time: O(n)

17. **[862. Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)** - Hard
    - Pattern: Prefix sum + monotonic deque
    - Time: O(n)

---

### Cache Design

18. **[146. LRU Cache](https://leetcode.com/problems/lru-cache/)** - Medium
    - Pattern: HashMap + Doubly Linked List
    - Time: O(1)

19. **[460. LFU Cache](https://leetcode.com/problems/lfu-cache/)** - Hard
    - Pattern: HashMap + Frequency Map
    - Time: O(1)

20. **[981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)** - Medium
    - Pattern: HashMap + Binary Search
    - Time: O(log n)

21. **[1472. Design Browser History](https://leetcode.com/problems/design-browser-history/)** - Medium
    - Pattern: Doubly Linked List or Array
    - Time: O(1)

22. **[1206. Design Skiplist](https://leetcode.com/problems/design-skiplist/)** - Hard
    - Pattern: Multi-level linked list
    - Time: O(log n) average

---

### Bitmask DP

23. **[943. Find the Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/)** - Hard
    - Pattern: TSP variant
    - Time: O(n² × 2ⁿ)

24. **[1125. Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/)** - Hard
    - Pattern: Subset selection
    - Time: O(n × 2ᵐ)

25. **[1655. Distribute Repeating Integers](https://leetcode.com/problems/distribute-repeating-integers/)** - Hard
    - Pattern: Bitmask DP
    - Time: O(m × 3ᵐ)

26. **[1349. Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/)** - Hard
    - Pattern: Row bitmask DP
    - Time: O(m × 4ⁿ)

27. **[1434. Number of Ways to Wear Different Hats to Each Other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/)** - Hard
    - Pattern: Bitmask DP over people
    - Time: O(40 × 2¹⁰)

28. **[847. Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)** - Hard
    - Pattern: BFS + bitmask
    - Time: O(n × 2ⁿ)

---

### Digit DP

29. **[233. Number of Digit One](https://leetcode.com/problems/number-of-digit-one/)** - Hard
    - Pattern: Digit DP counting
    - Time: O(log n)

30. **[902. Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/)** - Hard
    - Pattern: Digit DP
    - Time: O(log n × d)

31. **[1012. Numbers With Repeated Digits](https://leetcode.com/problems/numbers-with-repeated-digits/)** - Hard
    - Pattern: Digit DP with bitmask
    - Time: O(log n × 2¹⁰)

32. **[1397. Find All Good Strings](https://leetcode.com/problems/find-all-good-strings/)** - Hard
    - Pattern: Digit DP + KMP
    - Time: O(n × m)

33. **[2376. Count Special Integers](https://leetcode.com/problems/count-special-integers/)** - Hard
    - Pattern: Digit DP distinct digits
    - Time: O(log n × 2¹⁰)

---

### Monotonic Stack

34. **[84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)** - Hard
    - Pattern: Monotonic stack
    - Time: O(n)

35. **[85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)** - Hard
    - Pattern: Histogram + monotonic stack
    - Time: O(m × n)

36. **[496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)** - Easy
    - Pattern: Basic monotonic stack
    - Time: O(n)

37. **[503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)** - Medium
    - Pattern: Circular array
    - Time: O(n)

38. **[739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)** - Medium
    - Pattern: Monotonic stack
    - Time: O(n)

39. **[901. Online Stock Span](https://leetcode.com/problems/online-stock-span/)** - Medium
    - Pattern: Monotonic stack online
    - Time: O(1) amortized

40. **[907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/)** - Medium
    - Pattern: Contribution technique
    - Time: O(n)

41. **[1019. Next Greater Node In Linked List](https://leetcode.com/problems/next-greater-node-in-linked-list/)** - Medium
    - Pattern: Monotonic stack on list
    - Time: O(n)

42. **[1124. Longest Well-Performing Interval](https://leetcode.com/problems/longest-well-performing-interval/)** - Medium
    - Pattern: Prefix sum + monotonic stack
    - Time: O(n)

43. **[1475. Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)** - Easy
    - Pattern: Next smaller element
    - Time: O(n)

---

### Mixed Advanced Topics

44. **[1923. Longest Common Subpath](https://leetcode.com/problems/longest-common-subpath/)** - Hard
    - Pattern: Binary search + Rabin-Karp
    - Time: O(n log n)

45. **[1316. Distinct Echo Substrings](https://leetcode.com/problems/distinct-echo-substrings/)** - Hard
    - Pattern: Rolling hash
    - Time: O(n²)

46. **[1687. Delivering Boxes from Storage to Ports](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/)** - Hard
    - Pattern: DP + monotonic deque
    - Time: O(n)

47. **[1368. Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)** - Hard
    - Pattern: 0-1 BFS + deque
    - Time: O(m × n)

48. **[995. Minimum Number of K Consecutive Bit Flips](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/)** - Hard
    - Pattern: Greedy + sliding window
    - Time: O(n)

49. **[1335. Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/)** - Hard
    - Pattern: DP + monotonic stack
    - Time: O(n × d)

50. **[1420. Build Array Where You Can Find The Maximum Exactly K Comparisons](https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)** - Hard
    - Pattern: DP with multiple states
    - Time: O(n × m² × k)

---

## Common Mistakes to Avoid

### Mistake 1: Not Preprocessing for KMP

```python
# WRONG: Recompute LPS every time
def search_all(text, pattern):
    positions = []
    for i in range(len(text)):
        lps = build_lps(pattern)  # Wasteful!
        if kmp_search(text[i:], pattern) != -1:
            positions.append(i)

# CORRECT: Build LPS once
def search_all(text, pattern):
    lps = build_lps(pattern)
    positions = []
    # Use lps for all searches
```

---

### Mistake 2: Forgetting to Handle Even/Odd in Manacher's

```python
# WRONG: Doesn't handle even-length palindromes
def manacher_wrong(s):
    # Process string directly
    p = [0] * len(s)
    # Will miss "abba" type palindromes

# CORRECT: Preprocess with separators
def manacher_correct(s):
    t = '#'.join('^{}$'.format(s))
    # Now handles both even and odd lengths
```

---

### Mistake 3: Not Maintaining Deque Invariant

```python
# WRONG: Doesn't remove outside window
def sliding_max_wrong(nums, k):
    deq = deque()
    for i in range(len(nums)):
        # Missing: Remove elements outside window!
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        deq.append(i)

# CORRECT: Remove outside window first
def sliding_max_correct(nums, k):
    deq = deque()
    for i in range(len(nums)):
        while deq and deq[0] < i - k + 1:  # Remove old
            deq.popleft()
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        deq.append(i)
```

---

### Mistake 4: Incorrect Bitmask Operations

```python
# WRONG: Using wrong bit operations
if mask & i:  # Should use (1 << i)

# CORRECT: Proper bit manipulation
if mask & (1 << i):  # Check if i-th bit is set
mask |= (1 << i)     # Set i-th bit
mask &= ~(1 << i)    # Clear i-th bit
```

---

## Interview Tips

### String Algorithm Questions

**How to approach**:
1. Identify if exact match or approximate
2. Single pattern vs multiple patterns
3. All occurrences vs first occurrence
4. Consider time constraints (KMP O(n+m) vs naive O(nm))

**Common follow-ups**:
- "What if we have multiple patterns?"
- "How to handle wildcards?"
- "Can you optimize space?"

---

### Cache Design Questions

**Key points to discuss**:
1. Eviction policy (LRU, LFU, MRU)
2. Time complexity requirement (O(1) expected)
3. Thread safety considerations
4. Memory constraints

**Common variations**:
- "Add time-to-live"
- "Add priority levels"
- "Support concurrent access"

---

### DP Optimization Questions

**When interviewer says "optimize"**:
1. Check if monotonic deque can optimize window DP
2. Look for bitmask DP if n ≤ 20
3. Consider digit DP for counting in ranges
4. Think about state compression

---

## Study Schedule Recommendations

### Week 1: String Algorithms
- Days 1-2: KMP algorithm (theory + practice)
- Days 3-4: Rabin-Karp (single + multiple patterns)
- Days 5-6: Z-algorithm
- Day 7: Manacher's algorithm

**Practice**: 10-15 problems

---

### Week 2: Sliding Window & Monotonic Structures
- Days 1-2: Sliding window maximum
- Days 3-4: Monotonic stack patterns
- Days 5-6: Monotonic queue applications
- Day 7: Mixed problems

**Practice**: 10-15 problems

---

### Week 3: Cache Design & Advanced DP
- Days 1-2: LRU and LFU cache
- Days 3-4: Bitmask DP
- Days 5-6: Digit DP
- Day 7: Review and practice

**Practice**: 10-15 problems

---

## Performance Optimization Tips

### Tip 1: Choose Right Hash Function

```python
# For Rabin-Karp, use:
d = 256  # Base (alphabet size)
q = 10**9 + 7  # Large prime

# Avoid small primes (more collisions)
# Avoid non-primes (poor distribution)
```

---

### Tip 2: Optimize Manacher's with Early Exit

```python
def manacher_optimized(s):
    t = '#'.join('^{}$'.format(s))
    # If only need length, can exit early
    max_len = 0
    for i in range(1, len(t) - 1):
        # ... expand ...
        if p[i] > max_len:
            max_len = p[i]
            # Can exit if max_len > remaining positions
            if max_len > len(t) - i:
                break
```

---

### Tip 3: Reuse Bitmask DP States

```python
# Store intermediate results
memo = {}  # (mask, state) → result

# Iterate masks in order to build up
for mask in range(1 << n):
    # Can use results from smaller masks
    pass
```

---

## Mastery Checklist

```
□ Can implement KMP from scratch in < 10 minutes
□ Understand why KMP is O(n + m)
□ Can explain Manacher's algorithm intuitively
□ Can design LRU cache with O(1) operations
□ Comfortable with bitmask DP for n ≤ 20
□ Can recognize digit DP problems
□ Master monotonic stack/queue patterns
□ Solve hard problems in 30-40 minutes
```

---

Remember: **Pattern recognition > memorization**. Focus on understanding when and why each algorithm works!
