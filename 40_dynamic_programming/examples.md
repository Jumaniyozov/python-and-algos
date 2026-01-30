# Chapter 40: Dynamic Programming - Examples

## Table of Contents
1. [1D DP Examples](#1d-dp-examples)
2. [2D DP Examples](#2d-dp-examples)
3. [Knapsack Examples](#knapsack-examples)
4. [Sequence DP Examples](#sequence-dp-examples)
5. [String DP Examples](#string-dp-examples)
6. [State Machine DP Examples](#state-machine-dp-examples)
7. [Advanced DP Examples](#advanced-dp-examples)

---

## 1D DP Examples

### Example 1: Fibonacci Sequence

**Problem**: Calculate the nth Fibonacci number.

**Pattern**: Linear DP with two previous states

#### Approach 1: Memoization (Top-Down)

```python
def fibonacci_memo(n):
    """
    Time: O(n) - each fib(k) computed once
    Space: O(n) - recursion stack + memo
    """
    memo = {}

    def fib(k):
        if k <= 1:
            return k

        if k in memo:
            return memo[k]

        memo[k] = fib(k-1) + fib(k-2)
        return memo[k]

    return fib(n)

# Trace for n=5:
# fib(5) -> fib(4) + fib(3)
# fib(4) -> fib(3) + fib(2)
# fib(3) -> fib(2) + fib(1)
# fib(2) -> fib(1) + fib(0)
# fib(3) retrieved from memo (computed once!)
```

#### Approach 2: Tabulation (Bottom-Up)

```python
def fibonacci_tab(n):
    """
    Time: O(n)
    Space: O(n)
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# DP table for n=5:
# dp = [0, 1, 1, 2, 3, 5]
#       0  1  2  3  4  5
```

#### Approach 3: Space-Optimized

```python
def fibonacci_optimized(n):
    """
    Time: O(n)
    Space: O(1)
    """
    if n <= 1:
        return n

    prev2, prev1 = 0, 1

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1

# Evolution for n=5:
# i=2: prev2=0, prev1=1 -> curr=1 -> prev2=1, prev1=1
# i=3: prev2=1, prev1=1 -> curr=2 -> prev2=1, prev1=2
# i=4: prev2=1, prev1=2 -> curr=3 -> prev2=2, prev1=3
# i=5: prev2=2, prev1=3 -> curr=5 -> prev2=3, prev1=5
```

---

### Example 2: Climbing Stairs

**Problem**: You can climb 1 or 2 steps at a time. How many ways to reach step n?

**Pattern**: Same as Fibonacci (each step can be reached from previous 1 or 2 steps)

```python
def climb_stairs(n):
    """
    Recurrence: dp[i] = dp[i-1] + dp[i-2]
    - Reach step i from step i-1 (take 1 step)
    - Reach step i from step i-2 (take 2 steps)

    Time: O(n)
    Space: O(1)
    """
    if n <= 2:
        return n

    prev2, prev1 = 1, 2

    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1

# Example: n=5
# Step 0: 1 way (base)
# Step 1: 1 way (base)
# Step 2: 2 ways (1+1, 2)
# Step 3: 3 ways (1+1+1, 1+2, 2+1)
# Step 4: 5 ways (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)
# Step 5: 8 ways
```

---

### Example 3: House Robber

**Problem**: Rob houses in a line. Can't rob adjacent houses. Maximize loot.

**Pattern**: At each house, decide to rob or skip

```python
def rob(nums):
    """
    State: dp[i] = max money robbing first i houses
    Recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    - Option 1: Skip house i, take dp[i-1]
    - Option 2: Rob house i, add to dp[i-2]

    Time: O(n)
    Space: O(1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, curr

    return prev1

# Example: nums = [2, 7, 9, 3, 1]
# i=0: rob=2
# i=1: rob=max(7, 2)=7
# i=2: rob=max(7, 2+9)=11 (rob houses 0,2)
# i=3: rob=max(11, 7+3)=11
# i=4: rob=max(11, 11+1)=12 (rob houses 0,2,4)
```

---

### Example 4: Decode Ways

**Problem**: '1'-'26' map to 'A'-'Z'. Count ways to decode a digit string.

**Pattern**: Decision at each position - decode 1 digit or 2 digits

```python
def num_decodings(s):
    """
    State: dp[i] = number of ways to decode s[:i]
    Recurrence:
    - If s[i-1] is valid (1-9): add dp[i-1]
    - If s[i-2:i] is valid (10-26): add dp[i-2]

    Time: O(n)
    Space: O(1)
    """
    if not s or s[0] == '0':
        return 0

    n = len(s)
    prev2, prev1 = 1, 1  # dp[0]=1, dp[1]=1

    for i in range(2, n + 1):
        curr = 0

        # Single digit decode
        if s[i-1] != '0':
            curr += prev1

        # Two digit decode
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            curr += prev2

        prev2, prev1 = prev1, curr

    return prev1

# Example: s = "226"
# i=0: "2" -> 1 way (B)
# i=1: "22" -> 2 ways (BB, V)
# i=2: "226" -> 3 ways (BBF, VF, BZ)
#   - "6" is valid: add ways from "22" (2 ways)
#   - "26" is valid: add ways from "2" (1 way)
```

---

### Example 5: Coin Change

**Problem**: Fewest coins to make amount (unlimited coins).

**Pattern**: Unbounded knapsack (can use each coin unlimited times)

```python
def coin_change(coins, amount):
    """
    State: dp[i] = fewest coins to make amount i
    Recurrence: dp[i] = min(dp[i-coin] + 1) for all coins

    Time: O(amount * len(coins))
    Space: O(amount)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example: coins = [1,2,5], amount = 11
# dp[0] = 0
# dp[1] = 1 (1)
# dp[2] = 1 (2)
# dp[3] = 2 (1+2)
# dp[4] = 2 (2+2)
# dp[5] = 1 (5)
# dp[6] = 2 (5+1)
# ...
# dp[11] = 3 (5+5+1)
```

---

### Example 6: Maximum Product Subarray

**Problem**: Find contiguous subarray with largest product.

**Pattern**: Track both max and min (negative can become positive)

```python
def max_product(nums):
    """
    State: max_prod, min_prod = max/min product ending at i
    Key insight: negative number can flip max/min

    Time: O(n)
    Space: O(1)
    """
    if not nums:
        return 0

    result = max_prod = min_prod = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        # Store current max before updating
        temp_max = max_prod

        # Update max_prod (could come from min_prod * negative)
        max_prod = max(num, max_prod * num, min_prod * num)

        # Update min_prod
        min_prod = min(num, temp_max * num, min_prod * num)

        result = max(result, max_prod)

    return result

# Example: nums = [2, 3, -2, 4]
# i=0: max=2, min=2, result=2
# i=1: max=6, min=2, result=6
# i=2: max=-2, min=-12, result=6 (negative flips max/min)
# i=3: max=4, min=-48, result=6
```

---

## 2D DP Examples

### Example 7: Unique Paths

**Problem**: Grid m×n, robot starts at top-left, moves right/down only. Count paths to bottom-right.

```python
def unique_paths(m, n):
    """
    State: dp[i][j] = paths to reach (i,j)
    Recurrence: dp[i][j] = dp[i-1][j] + dp[i][j-1]

    Time: O(m*n)
    Space: O(n) - optimized
    """
    # Space-optimized: only need previous row
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]

    return dp[n-1]

# Example: m=3, n=3
# Initial: dp = [1, 1, 1]
# i=1:     dp = [1, 2, 3]
# i=2:     dp = [1, 3, 6]
# Answer: 6 paths
```

**Visualization** (m=3, n=3):
```
Start   1  →  1  →  1
  ↓              ↓
  1  →  2  →  3  →  3
  ↓              ↓
  1  →  3  →  6  →  6 End
```

---

### Example 8: Minimum Path Sum

**Problem**: Grid with values, find path from top-left to bottom-right minimizing sum.

```python
def min_path_sum(grid):
    """
    State: dp[i][j] = min sum to reach (i,j)
    Recurrence: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    Time: O(m*n)
    Space: O(1) - modify in place
    """
    m, n = len(grid), len(grid[0])

    # Initialize first row and column
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]

    for j in range(1, n):
        grid[0][j] += grid[0][j-1]

    # Fill rest of grid
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[m-1][n-1]

# Example: grid = [[1,3,1],
#                  [1,5,1],
#                  [4,2,1]]
#
# After DP:       [[1,4,5],
#                  [2,7,6],
#                  [6,8,7]]
# Min path: 1→3→1→1→1 = 7
```

---

### Example 9: Longest Common Subsequence (LCS)

**Problem**: Find length of longest subsequence present in both strings.

```python
def longest_common_subsequence(text1, text2):
    """
    State: dp[i][j] = LCS length for text1[:i] and text2[:j]
    Recurrence:
    - If text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
    - Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    Time: O(m*n)
    Space: O(n) - optimized
    """
    m, n = len(text1), len(text2)

    # Space optimization: only need previous row
    prev = [0] * (n + 1)

    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev = curr

    return prev[n]

# Example: text1 = "abcde", text2 = "ace"
# DP table:
#     ""  a  c  e
# ""   0  0  0  0
# a    0  1  1  1
# b    0  1  1  1
# c    0  1  2  2
# d    0  1  2  2
# e    0  1  2  3
# LCS = "ace", length = 3
```

**How to reconstruct LCS**:
```python
def lcs_with_string(text1, text2):
    """Return actual LCS string."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Reconstruct LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))
```

---

### Example 10: Edit Distance

**Problem**: Minimum operations (insert, delete, replace) to convert word1 to word2.

```python
def min_distance(word1, word2):
    """
    State: dp[i][j] = min edits for word1[:i] -> word2[:j]
    Recurrence:
    - If word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
    - Else: dp[i][j] = 1 + min(
        dp[i-1][j],    # delete from word1
        dp[i][j-1],    # insert to word1
        dp[i-1][j-1]   # replace
      )

    Time: O(m*n)
    Space: O(n) - optimized
    """
    m, n = len(word1), len(word2)

    # Space optimization
    prev = list(range(n + 1))

    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(prev[j],      # delete
                                  curr[j-1],    # insert
                                  prev[j-1])    # replace
        prev = curr

    return prev[n]

# Example: word1 = "horse", word2 = "ros"
# DP table:
#       ""  r  o  s
#   ""   0  1  2  3
#   h    1  1  2  3
#   o    2  2  1  2
#   r    3  2  2  2
#   s    4  3  3  2
#   e    5  4  4  3
#
# Operations: horse -> rorse -> rose -> ros (3 operations)
```

---

## Knapsack Examples

### Example 11: 0/1 Knapsack

**Problem**: Items with weights and values. Maximize value without exceeding capacity. Each item used 0 or 1 time.

```python
def knapsack_01(weights, values, capacity):
    """
    State: dp[i][w] = max value with first i items, capacity w
    Recurrence:
    - If weight[i-1] > w: dp[i][w] = dp[i-1][w]
    - Else: dp[i][w] = max(dp[i-1][w],                    # don't take
                            dp[i-1][w-weight[i-1]] + value[i-1])  # take

    Time: O(n*W)
    Space: O(W) - optimized
    """
    n = len(weights)

    # Space optimization: 1D array, iterate backwards
    dp = [0] * (capacity + 1)

    for i in range(n):
        # Iterate backwards to avoid using updated values
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

# Example: weights = [1,3,4,5], values = [1,4,5,7], capacity = 7
# i=0 (w=1,v=1): dp = [0,1,1,1,1,1,1,1]
# i=1 (w=3,v=4): dp = [0,1,1,4,5,5,5,5]
# i=2 (w=4,v=5): dp = [0,1,1,4,5,5,6,9]
# i=3 (w=5,v=7): dp = [0,1,1,4,5,7,8,9]
# Max value = 9 (items 1 and 2: weights 3+4=7, values 4+5=9)
```

**With item tracking**:
```python
def knapsack_with_items(weights, values, capacity):
    """Return max value and items selected."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w],
                               dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    # Reconstruct items
    items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items.append(i-1)
            w -= weights[i-1]

    return dp[n][capacity], items[::-1]
```

---

### Example 12: Partition Equal Subset Sum

**Problem**: Can array be partitioned into two subsets with equal sum?

```python
def can_partition(nums):
    """
    Insight: Partition is possible iff we can find subset with sum = total_sum/2
    This is subset sum problem (variant of 0/1 knapsack)

    State: dp[s] = can we make sum s?
    Recurrence: dp[s] = dp[s] or dp[s-num]

    Time: O(n * sum)
    Space: O(sum)
    """
    total = sum(nums)

    # If odd sum, can't partition equally
    if total % 2:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True  # Sum 0 always possible (empty subset)

    for num in nums:
        # Iterate backwards to avoid using updated values
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    return dp[target]

# Example: nums = [1,5,11,5]
# total = 22, target = 11
# After num=1:  dp[1] = True
# After num=5:  dp[5], dp[6] = True
# After num=11: dp[11], dp[12], dp[16], dp[17] = True
# After num=5:  dp[11] already True
# Result: True (subsets: [1,5,5] and [11])
```

---

### Example 13: Target Sum

**Problem**: Add + or - before each number to reach target sum. Count ways.

```python
def find_target_sum_ways(nums, target):
    """
    Insight: Partition nums into P (positive) and N (negative)
    sum(P) - sum(N) = target
    sum(P) + sum(N) = sum(nums)
    => sum(P) = (target + sum(nums)) / 2

    This becomes: count subsets with sum = (target + sum(nums)) / 2

    State: dp[s] = number of ways to make sum s
    Recurrence: dp[s] += dp[s - num]

    Time: O(n * sum)
    Space: O(sum)
    """
    total = sum(nums)

    # Check feasibility
    if total < abs(target) or (target + total) % 2:
        return 0

    subset_sum = (target + total) // 2

    dp = [0] * (subset_sum + 1)
    dp[0] = 1  # One way to make 0: select nothing

    for num in nums:
        for s in range(subset_sum, num - 1, -1):
            dp[s] += dp[s - num]

    return dp[subset_sum]

# Example: nums = [1,1,1,1,1], target = 3
# total = 5, subset_sum = (3+5)/2 = 4
# Find subsets with sum = 4 (there are 5 ways)
# Each way corresponds to a +/- assignment
```

---

## Sequence DP Examples

### Example 14: Longest Increasing Subsequence (LIS)

**Problem**: Find length of longest strictly increasing subsequence.

#### Approach 1: O(n²) DP

```python
def length_of_lis(nums):
    """
    State: dp[i] = length of LIS ending at index i
    Recurrence: dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]

    Time: O(n²)
    Space: O(n)
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example: nums = [10,9,2,5,3,7,101,18]
# dp = [1,1,1,2,2,3,4,4]
# LIS: [2,5,7,101] or [2,3,7,101], length = 4
```

#### Approach 2: O(n log n) with Binary Search

```python
def length_of_lis_optimized(nums):
    """
    Use patience sorting algorithm with binary search.
    tails[i] = smallest tail of all increasing subsequences of length i+1

    Time: O(n log n)
    Space: O(n)
    """
    import bisect

    tails = []

    for num in nums:
        # Find position to insert/replace
        pos = bisect.bisect_left(tails, num)

        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)

# Example: nums = [10,9,2,5,3,7,101,18]
# Process:
# 10: tails = [10]
# 9:  tails = [9]     (replace 10)
# 2:  tails = [2]     (replace 9)
# 5:  tails = [2,5]
# 3:  tails = [2,3]   (replace 5)
# 7:  tails = [2,3,7]
# 101: tails = [2,3,7,101]
# 18: tails = [2,3,7,18] (replace 101)
# Length = 4
```

---

### Example 15: Longest Palindromic Subsequence

**Problem**: Find length of longest palindromic subsequence.

```python
def longest_palindrome_subseq(s):
    """
    State: dp[i][j] = LPS length in s[i:j+1]
    Recurrence:
    - If s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
    - Else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    Time: O(n²)
    Space: O(n²) or O(n) optimized
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base case: single character palindromes
    for i in range(n):
        dp[i][i] = 1

    # Fill table by increasing substring length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]

# Example: s = "bbbab"
# DP table:
#     b  b  b  a  b
# b   1  2  3  3  4
# b      1  2  2  3
# b         1  1  3
# a            1  1
# b               1
#
# LPS = "bbbb", length = 4
```

---

## String DP Examples

### Example 16: Word Break

**Problem**: Given string s and dictionary, determine if s can be segmented into dictionary words.

```python
def word_break(s, word_dict):
    """
    State: dp[i] = can we segment s[:i]?
    Recurrence: dp[i] = True if any dp[j] and s[j:i] in dict

    Time: O(n² * m) where m = avg word length
    Space: O(n)
    """
    n = len(s)
    word_set = set(word_dict)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string can be segmented

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]

# Example: s = "leetcode", wordDict = ["leet","code"]
# dp[0] = True
# dp[4] = True (s[0:4] = "leet" in dict)
# dp[8] = True (dp[4] True and s[4:8] = "code" in dict)
```

**Count all ways to segment**:
```python
def word_break_count(s, word_dict):
    """Count number of ways to segment."""
    n = len(s)
    word_set = set(word_dict)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] += dp[j]

    return dp[n]
```

---

### Example 17: Palindrome Partitioning II

**Problem**: Minimum cuts to partition string into palindromes.

```python
def min_cut(s):
    """
    State: dp[i] = min cuts for s[:i]
    Recurrence: dp[i] = min(dp[j] + 1) if s[j:i] is palindrome

    Optimization: precompute palindrome table

    Time: O(n²)
    Space: O(n²)
    """
    n = len(s)

    # Precompute palindrome table
    is_palindrome = [[False] * n for _ in range(n)]

    for i in range(n):
        is_palindrome[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                is_palindrome[i][j] = (length == 2 or is_palindrome[i+1][j-1])

    # DP for min cuts
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(i):
            if is_palindrome[j][i-1]:
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[n] - 1  # Subtract 1 (count cuts, not pieces)

# Example: s = "aab"
# Palindromes: "a", "a", "b", "aa", "aab"
# dp = [0, 1, 1, 1]
# Min cuts = 1 (cut after "aa": "aa|b")
```

---

## State Machine DP Examples

### Example 18: Best Time to Buy and Sell Stock with Cooldown

**Problem**: Buy/sell stock with cooldown (can't buy next day after sell).

```python
def max_profit_with_cooldown(prices):
    """
    States:
    - hold: currently holding stock
    - sold: just sold (cooldown tomorrow)
    - rest: not holding, can buy

    Transitions:
    - hold: max(prev_hold, prev_rest - price) (keep holding or buy)
    - sold: prev_hold + price (sell)
    - rest: max(prev_rest, prev_sold) (rest or cooldown over)

    Time: O(n)
    Space: O(1)
    """
    if not prices:
        return 0

    hold = -prices[0]  # Bought first stock
    sold = 0           # Haven't sold yet
    rest = 0           # Haven't bought yet

    for price in prices[1:]:
        prev_hold, prev_sold = hold, sold

        hold = max(prev_hold, rest - price)
        sold = prev_hold + price
        rest = max(rest, prev_sold)

    return max(sold, rest)

# Example: prices = [1,2,3,0,2]
# Day 0: hold=-1, sold=0, rest=0
# Day 1: hold=-1, sold=1, rest=0 (buy day 0, sell day 1)
# Day 2: hold=-1, sold=2, rest=1 (sell day 2)
# Day 3: hold=1, sold=-1, rest=2 (rest, then buy day 3)
# Day 4: hold=1, sold=3, rest=2 (sell day 4)
# Max profit = 3
```

---

### Example 19: Paint House

**Problem**: n houses, 3 colors (R,G,B). Adjacent houses can't have same color. Minimize cost.

```python
def min_cost(costs):
    """
    States: dp[i][color] = min cost to paint first i houses,
            with house i having color

    Transitions: dp[i][c] = costs[i][c] + min(dp[i-1][other_colors])

    Time: O(n)
    Space: O(1)
    """
    if not costs:
        return 0

    # Previous row: min cost for each color
    prev = costs[0][:]

    for i in range(1, len(costs)):
        curr = [0] * 3
        curr[0] = costs[i][0] + min(prev[1], prev[2])  # Red
        curr[1] = costs[i][1] + min(prev[0], prev[2])  # Green
        curr[2] = costs[i][2] + min(prev[0], prev[1])  # Blue
        prev = curr

    return min(prev)

# Example: costs = [[17,2,17],[16,16,5],[14,3,19]]
# House 0: [17, 2, 17]
# House 1: [17+16, 2+16, 17+5] = [33, 18, 22]
# House 2: [33+14, 18+3, 22+19] = [47, 21, 41]
# Min = 21 (Green, Blue, Green)
```

---

## Advanced DP Examples

### Example 20: Burst Balloons

**Problem**: Burst balloons to maximize coins. Bursting i gives `nums[left]*nums[i]*nums[right]` coins.

```python
def max_coins(nums):
    """
    Key insight: Think about which balloon to burst LAST in range [i,j]

    State: dp[i][j] = max coins from bursting balloons in range (i,j)
           (not including i and j)

    Recurrence: For each k in (i,j):
      dp[i][j] = max(dp[i][k] + nums[i]*nums[k]*nums[j] + dp[k][j])

    Time: O(n³)
    Space: O(n²)
    """
    # Add 1s to boundaries
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    # Iterate by range length
    for length in range(2, n):
        for i in range(n - length):
            j = i + length

            # Try bursting each balloon k last in range (i,j)
            for k in range(i + 1, j):
                coins = nums[i] * nums[k] * nums[j]
                coins += dp[i][k] + dp[k][j]
                dp[i][j] = max(dp[i][j], coins)

    return dp[0][n-1]

# Example: nums = [3,1,5,8]
# With boundaries: [1,3,1,5,8,1]
#
# Length 2 (adjacent): dp[0][2]=3, dp[1][3]=15, dp[2][4]=40, dp[3][5]=40
# Length 3: ...
# Final: dp[0][5] = 167
```

---

### Example 21: Regular Expression Matching

**Problem**: Implement regex matching with `.` (any char) and `*` (0+ of previous).

```python
def is_match(s, p):
    """
    State: dp[i][j] = does s[:i] match p[:j]?

    Recurrence:
    - If p[j-1] is letter/dot:
        dp[i][j] = dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='.')
    - If p[j-1] is '*':
        dp[i][j] = dp[i][j-2] (match 0 of prev char)
                or dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.') (match 1+)

    Time: O(m*n)
    Space: O(m*n)
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Handle patterns like a*, a*b*, etc. matching empty string
    for j in range(2, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                # Match 0 of previous char
                dp[i][j] = dp[i][j-2]

                # Match 1+ of previous char
                if p[j-2] == s[i-1] or p[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]
            elif p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]

    return dp[m][n]

# Example: s = "aab", p = "c*a*b"
# DP table shows True at dp[3][6]
```

---

### Example 22: Maximal Rectangle

**Problem**: Find largest rectangle containing only 1s in binary matrix.

```python
def maximal_rectangle(matrix):
    """
    Insight: For each row, compute histogram heights and find max rectangle.

    Use DP to build heights array, then use histogram algorithm.

    Time: O(m*n)
    Space: O(n)
    """
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix[0])
    heights = [0] * n
    max_area = 0

    for row in matrix:
        # Update heights (DP for histogram)
        for i in range(n):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0

        # Find max rectangle in histogram
        max_area = max(max_area, largest_rectangle_in_histogram(heights))

    return max_area


def largest_rectangle_in_histogram(heights):
    """Helper: max rectangle area in histogram."""
    stack = []
    max_area = 0
    heights = heights + [0]  # Sentinel

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area

# Example: matrix = [["1","0","1","0","0"],
#                    ["1","0","1","1","1"],
#                    ["1","1","1","1","1"],
#                    ["1","0","0","1","0"]]
#
# Row 0: heights = [1,0,1,0,0], max = 1
# Row 1: heights = [2,0,2,1,1], max = 3
# Row 2: heights = [3,1,3,2,2], max = 6 ← answer
# Row 3: heights = [4,0,0,3,0], max = 6
```

---

## Summary

These 22 examples cover the most important DP patterns:

1. **1D DP**: Fibonacci, Climbing Stairs, House Robber, Decode Ways, Coin Change, Max Product
2. **2D DP**: Unique Paths, Min Path Sum, LCS, Edit Distance
3. **Knapsack**: 0/1 Knapsack, Partition Equal Subset, Target Sum
4. **Sequence**: LIS, Longest Palindromic Subsequence
5. **String**: Word Break, Palindrome Partitioning
6. **State Machine**: Stock with Cooldown, Paint House
7. **Advanced**: Burst Balloons, Regex Matching, Maximal Rectangle

### Key Takeaways

1. **Always define state clearly**
2. **Draw DP table for small examples**
3. **Identify base cases first**
4. **Optimize space after correctness**
5. **Practice pattern recognition**

Next: [Exercises](./exercises.md) - Test your understanding with 25 practice problems!
