# Chapter 40: Dynamic Programming - Theory

## Table of Contents
1. [What is Dynamic Programming?](#what-is-dynamic-programming)
2. [When to Use DP](#when-to-use-dp)
3. [DP Fundamentals](#dp-fundamentals)
4. [Memoization vs Tabulation](#memoization-vs-tabulation)
5. [1D DP Patterns](#1d-dp-patterns)
6. [2D DP Patterns](#2d-dp-patterns)
7. [Knapsack Problems](#knapsack-problems)
8. [Sequence DP](#sequence-dp)
9. [String DP](#string-dp)
10. [State Machine DP](#state-machine-dp)
11. [Interval DP](#interval-dp)
12. [Space Optimization](#space-optimization)
13. [DP vs Other Approaches](#dp-vs-other-approaches)

---

## What is Dynamic Programming?

Dynamic Programming is an algorithmic paradigm that solves complex problems by:
1. Breaking them into simpler **overlapping subproblems**
2. Solving each subproblem only once
3. Storing solutions to avoid redundant computation
4. Building up solutions to larger problems from smaller ones

### The Name "Dynamic Programming"

Despite its name, DP has little to do with "programming" in the coding sense. Richard Bellman coined the term in the 1950s to make his optimization research sound impressive to funders. "Dynamic" refers to time-dependent optimization, and "Programming" meant planning/scheduling in military/operations research contexts.

### Key Insight

**DP = Recursion + Memoization**

Instead of recalculating the same subproblems repeatedly, we store (cache) results and reuse them.

---

## When to Use DP

### Three Conditions for DP

A problem is suitable for DP if it satisfies:

#### 1. Overlapping Subproblems
The problem can be broken down into subproblems that are reused multiple times.

**Example: Fibonacci**
```
fib(5) calls fib(4) and fib(3)
fib(4) calls fib(3) and fib(2)
        ↑ fib(3) is computed twice!
```

#### 2. Optimal Substructure
An optimal solution to the problem contains optimal solutions to subproblems.

**Example: Shortest Path**
- If path A→C is shortest, and it goes through B
- Then A→B must be shortest path from A to B
- And B→C must be shortest path from B to C

#### 3. Can Define State and Transitions
You can define:
- **State**: What information uniquely describes a subproblem
- **Transitions**: How to compute a state from previous states

### Problem Types That Use DP

1. **Optimization Problems**
   - Minimize/maximize some value
   - "Find minimum cost", "Find maximum profit"

2. **Counting Problems**
   - Count number of ways to do something
   - "How many ways to...", "Count distinct paths"

3. **Yes/No Problems**
   - Determine if something is possible
   - "Can you partition...", "Is there a subset..."

4. **Sequence Problems**
   - Find longest/shortest sequence with property
   - "Longest increasing subsequence", "Shortest common supersequence"

---

## DP Fundamentals

### Overlapping Subproblems in Detail

Consider computing Fibonacci(5) recursively:

```
                    fib(5)
                   /      \
              fib(4)        fib(3)
             /     \        /     \
        fib(3)   fib(2)  fib(2)  fib(1)
        /   \     /  \    /  \
    fib(2) fib(1) 1   0  1   0
    /  \
   1    0
```

**Observations**:
- fib(3) computed **2 times**
- fib(2) computed **3 times**
- fib(1) computed **3 times**
- fib(0) computed **2 times**

Total function calls: **15** for just fib(5)!

With DP (memoization), we compute each unique value only once: **6 calls** total.

### Optimal Substructure in Detail

**Example: Minimum Cost Path**

```
Grid:
1  3  1
1  5  1
4  2  1

Minimum cost to reach (2,2):
  = value[2][2] + min(cost to reach (1,2), cost to reach (2,1))
  = 1 + min(cost to (1,2), cost to (2,1))
```

The optimal path to (2,2) must use optimal paths to its predecessors.

**Counter-Example: Longest Path** (without cycle constraint)
Longest simple path doesn't have optimal substructure because:
- Longest path from A to C might not use longest path from A to B
- (The longest A→B path might eliminate nodes needed for B→C)

---

## Memoization vs Tabulation

### Memoization (Top-Down)

**Approach**: Start with the original problem and recursively break it down, caching results.

**Characteristics**:
- ✅ Natural recursive structure
- ✅ Only computes needed subproblems
- ✅ Easier to implement initially
- ❌ Recursion overhead (stack space)
- ❌ May hit recursion limit

**Template**:
```python
def memoization_dp(n):
    memo = {}

    def dp(state):
        # Base case
        if base_condition:
            return base_value

        # Check cache
        if state in memo:
            return memo[state]

        # Recurrence relation
        result = compute_from_subproblems(dp(substate1), dp(substate2), ...)

        # Cache and return
        memo[state] = result
        return result

    return dp(n)
```

**Example: Fibonacci**
```python
def fib(n):
    memo = {}

    def helper(k):
        if k <= 1:
            return k
        if k in memo:
            return memo[k]

        memo[k] = helper(k-1) + helper(k-2)
        return memo[k]

    return helper(n)
```

### Tabulation (Bottom-Up)

**Approach**: Start with base cases and iteratively build up to the solution.

**Characteristics**:
- ✅ No recursion overhead
- ✅ Better cache locality
- ✅ Easier to optimize space
- ✅ Guaranteed order of computation
- ❌ Must compute all subproblems
- ❌ May be less intuitive

**Template**:
```python
def tabulation_dp(n):
    # Initialize table
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = base_value_0
    dp[1] = base_value_1

    # Fill table bottom-up
    for i in range(2, n + 1):
        dp[i] = compute_from_previous(dp[i-1], dp[i-2], ...)

    return dp[n]
```

**Example: Fibonacci**
```python
def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

### When to Use Which?

| Criterion | Memoization | Tabulation |
|-----------|-------------|------------|
| Ease of implementation | ✅ Easier | Harder initially |
| Space efficiency | May waste space | Can optimize easily |
| Time constant factor | Slower (recursion) | ✅ Faster |
| Natural fit | Complex transitions | Simple iterations |
| Debugging | Harder | ✅ Easier to trace |
| Sparse problems | ✅ Better | May waste computation |

**Rule of Thumb**: Start with memoization to understand the problem, then convert to tabulation for optimization if needed.

---

## 1D DP Patterns

### Pattern: Single Sequence

**State Definition**: `dp[i]` = answer for the first `i` elements (or for element at index `i`)

**Common Variants**:
1. `dp[i]` depends on `dp[i-1]` (previous one)
2. `dp[i]` depends on `dp[i-1]` and `dp[i-2]` (previous two)
3. `dp[i]` depends on all previous `dp[j]` where `j < i`

### Example 1: Climbing Stairs

**Problem**: Climb stairs with 1 or 2 steps at a time. How many ways to reach step `n`?

**Recurrence**:
- `dp[i]` = ways to reach step `i`
- `dp[i] = dp[i-1] + dp[i-2]`
  - From step `i-1`, take 1 step
  - From step `i-2`, take 2 steps

**Base Cases**: `dp[0] = 1`, `dp[1] = 1`

```python
def climb_stairs(n):
    if n <= 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

**Time**: O(n), **Space**: O(n) → can optimize to O(1)

### Example 2: House Robber

**Problem**: Rob houses in a line. Can't rob adjacent houses. Maximize loot.

**Recurrence**:
- `dp[i]` = max money robbing first `i` houses
- `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
  - Option 1: Don't rob house `i`, keep `dp[i-1]`
  - Option 2: Rob house `i`, add to `dp[i-2]`

**Base Cases**: `dp[0] = nums[0]`, `dp[1] = max(nums[0], nums[1])`

```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[-1]
```

**Time**: O(n), **Space**: O(n) → can optimize to O(1)

### Example 3: Longest Increasing Subsequence (LIS)

**Problem**: Find length of longest strictly increasing subsequence.

**Recurrence**:
- `dp[i]` = length of LIS ending at index `i`
- `dp[i] = max(dp[j] + 1)` for all `j < i` where `nums[j] < nums[i]`

**Base Cases**: `dp[i] = 1` for all `i` (each element is a subsequence of length 1)

```python
def length_of_lis(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
```

**Time**: O(n²), **Space**: O(n)

**Note**: There's an O(n log n) solution using binary search + patience sorting.

---

## 2D DP Patterns

### Pattern: Grid DP

**State Definition**: `dp[i][j]` = answer for cell `(i, j)` or subgrid `[0..i][0..j]`

**Transitions**: Usually from `dp[i-1][j]`, `dp[i][j-1]`, or `dp[i-1][j-1]`

### Example 1: Unique Paths

**Problem**: Robot in grid, can only move right or down. Count paths from top-left to bottom-right.

**Recurrence**:
- `dp[i][j]` = number of paths to reach `(i, j)`
- `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
  - Paths from above + paths from left

**Base Cases**: `dp[0][j] = 1` (one way along top row), `dp[i][0] = 1` (one way along left column)

```python
def unique_paths(m, n):
    dp = [[0] * n for _ in range(m)]

    # Base cases
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # Fill table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]
```

**Time**: O(m×n), **Space**: O(m×n) → can optimize to O(n)

### Example 2: Minimum Path Sum

**Problem**: Grid with values. Find path from top-left to bottom-right minimizing sum.

**Recurrence**:
- `dp[i][j]` = minimum sum to reach `(i, j)`
- `dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`

**Base Cases**:
- `dp[0][0] = grid[0][0]`
- `dp[i][0] = dp[i-1][0] + grid[i][0]`
- `dp[0][j] = dp[0][j-1] + grid[0][j]`

```python
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = grid[0][0]

    # First column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # First row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Rest of grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[m-1][n-1]
```

**Time**: O(m×n), **Space**: O(m×n)

### Pattern: Two Sequences

**State Definition**: `dp[i][j]` = answer for first sequence up to index `i` and second sequence up to index `j`

### Example: Longest Common Subsequence (LCS)

**Problem**: Find length of longest subsequence common to two strings.

**Recurrence**:
- `dp[i][j]` = LCS length for `text1[0..i-1]` and `text2[0..j-1]`
- If `text1[i-1] == text2[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1`
- Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

**Base Cases**: `dp[i][0] = 0`, `dp[0][j] = 0`

```python
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

**Time**: O(m×n), **Space**: O(m×n) → can optimize to O(min(m,n))

---

## Knapsack Problems

### 0/1 Knapsack (Classic)

**Problem**: Given items with weights and values, and a knapsack capacity, maximize value without exceeding capacity. Each item can be used 0 or 1 time.

**State**:
- `dp[i][w]` = max value using first `i` items with capacity `w`

**Recurrence**:
- If `weight[i-1] > w`: `dp[i][w] = dp[i-1][w]` (can't take item)
- Else: `dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i-1]] + value[i-1])`
  - Option 1: Don't take item `i`
  - Option 2: Take item `i`

```python
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w],
                               dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
```

**Time**: O(n×W), **Space**: O(n×W) → can optimize to O(W)

### Unbounded Knapsack

**Problem**: Same as 0/1, but each item can be used unlimited times.

**Recurrence**:
- `dp[i][w] = max(dp[i-1][w], dp[i][w-weight[i-1]] + value[i-1])`
  - Note: `dp[i][...]` instead of `dp[i-1][...]` when taking item (can reuse)

```python
def knapsack_unbounded(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w],
                               dp[i][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
```

### Subset Sum

**Problem**: Can we select a subset with sum equal to target?

**State**: `dp[i][s]` = can we get sum `s` using first `i` numbers?

**Recurrence**:
- `dp[i][s] = dp[i-1][s] or dp[i-1][s-nums[i-1]]`

```python
def can_partition(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base case: sum 0 is always possible
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for s in range(1, target + 1):
            dp[i][s] = dp[i-1][s]  # Don't take nums[i-1]
            if s >= nums[i-1]:
                dp[i][s] = dp[i][s] or dp[i-1][s-nums[i-1]]  # Take it

    return dp[n][target]
```

---

## Sequence DP

### Pattern: Subsequence Problems

Problems involving finding subsequences with certain properties.

**Common Types**:
1. Longest Increasing Subsequence (LIS)
2. Longest Common Subsequence (LCS)
3. Longest Palindromic Subsequence
4. Maximum Sum Increasing Subsequence

### Longest Palindromic Subsequence

**Problem**: Find length of longest palindromic subsequence.

**State**: `dp[i][j]` = LPS length in substring `s[i..j]`

**Recurrence**:
- If `s[i] == s[j]`: `dp[i][j] = dp[i+1][j-1] + 2`
- Else: `dp[i][j] = max(dp[i+1][j], dp[i][j-1])`

```python
def longest_palindrome_subseq(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters
    for i in range(n):
        dp[i][i] = 1

    # Fill table: length 2, 3, ..., n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]
```

---

## String DP

### Edit Distance (Levenshtein Distance)

**Problem**: Minimum operations to convert string1 to string2. Operations: insert, delete, replace.

**State**: `dp[i][j]` = min operations to convert `word1[0..i-1]` to `word2[0..j-1]`

**Recurrence**:
- If `word1[i-1] == word2[j-1]`: `dp[i][j] = dp[i-1][j-1]`
- Else: `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`
  - `dp[i-1][j] + 1`: delete from word1
  - `dp[i][j-1] + 1`: insert into word1
  - `dp[i-1][j-1] + 1`: replace

```python
def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # delete
                                   dp[i][j-1],    # insert
                                   dp[i-1][j-1])  # replace

    return dp[m][n]
```

**Time**: O(m×n), **Space**: O(m×n)

---

## State Machine DP

### Pattern: State Transitions

Problems where you're in different "states" and transition between them.

**Example**: Best Time to Buy and Sell Stock II (unlimited transactions)

**States**:
- Hold: Currently holding stock
- Sold: Just sold stock (or never bought)

**State**: `dp[i][state]` = max profit on day `i` in `state`

```python
def max_profit(prices):
    if not prices:
        return 0

    n = len(prices)
    # dp[i][0] = max profit on day i, not holding stock
    # dp[i][1] = max profit on day i, holding stock

    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])  # sell
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])  # buy

    return dp[n-1][0]
```

---

## Interval DP

### Pattern: Range Problems

**State**: `dp[i][j]` = answer for subarray/substring from index `i` to `j`

**Iteration Order**: Usually by increasing length

### Example: Burst Balloons

**Problem**: Burst balloons to maximize coins. Bursting balloon `i` gives `nums[left] * nums[i] * nums[right]` coins.

**Key Insight**: Think about which balloon to burst **last** in range `[i, j]`

**State**: `dp[i][j]` = max coins from bursting balloons in range `[i, j]`

**Recurrence**: `dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j+1])` for all `k` in `[i, j]`

```python
def max_coins(nums):
    nums = [1] + nums + [1]  # Add boundaries
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    # Length of subarray
    for length in range(1, n - 1):
        for i in range(1, n - length):
            j = i + length - 1
            for k in range(i, j + 1):
                coins = nums[i-1] * nums[k] * nums[j+1]
                coins += dp[i][k-1] + dp[k+1][j]
                dp[i][j] = max(dp[i][j], coins)

    return dp[1][n-2]
```

---

## Space Optimization

### Technique 1: Rolling Array (1D to Constant Space)

When `dp[i]` only depends on `dp[i-1]` and `dp[i-2]`:

```python
# Before: O(n) space
dp = [0] * n
for i in range(n):
    dp[i] = dp[i-1] + dp[i-2]

# After: O(1) space
prev2, prev1 = base_case_0, base_case_1
for i in range(2, n):
    curr = prev1 + prev2
    prev2, prev1 = prev1, curr
```

### Technique 2: 2D to 1D

When `dp[i][j]` only depends on `dp[i-1][...]`:

```python
# Before: O(m×n) space
dp = [[0] * n for _ in range(m)]

# After: O(n) space
prev = [0] * n
curr = [0] * n
for i in range(m):
    for j in range(n):
        curr[j] = compute_from(prev[j], prev[j-1], ...)
    prev, curr = curr, prev
```

### Technique 3: In-Place DP

Modify input array if allowed:

```python
# Minimum path sum - modify grid in place
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])

    for i in range(1, m):
        grid[i][0] += grid[i-1][0]

    for j in range(1, n):
        grid[0][j] += grid[0][j-1]

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[m-1][n-1]
```

---

## DP vs Other Approaches

### DP vs Divide and Conquer

| Aspect | DP | Divide & Conquer |
|--------|----|--------------------|
| Subproblems | Overlapping | Independent |
| Examples | Fibonacci, LCS | Merge Sort, Quick Sort |
| Technique | Memoization/Tabulation | Recursion |

### DP vs Greedy

| Aspect | DP | Greedy |
|--------|----|--------------------|
| Approach | Try all options | Choose locally optimal |
| Guarantee | Optimal solution | Optimal only if greedy choice property holds |
| Time | Usually polynomial | Usually linear |
| Examples | 0/1 Knapsack | Activity Selection |

**When Greedy Works**: Problem has **greedy choice property** (local optimum leads to global optimum)

### DP vs Backtracking

| Aspect | DP | Backtracking |
|--------|----|--------------------|
| Use Case | Optimization, counting | Finding all solutions |
| Pruning | Memoization | Branch pruning |
| Examples | Subset Sum (count) | All subsets |

---

## Summary

### DP Problem-Solving Steps

1. **Identify DP Opportunity**
   - Optimization/counting/yes-no problem?
   - Overlapping subproblems?
   - Optimal substructure?

2. **Define State**
   - What information uniquely describes a subproblem?
   - 1D state? 2D state? Multi-dimensional?

3. **Write Recurrence Relation**
   - How to compute `dp[state]` from previous states?
   - What are the base cases?

4. **Implement**
   - Start with memoization (top-down)
   - Convert to tabulation if needed
   - Optimize space if possible

5. **Verify**
   - Test with examples
   - Check edge cases
   - Analyze complexity

### Key Takeaways

1. **DP = Recursion + Memoization**
2. **Start Top-Down, Optimize Bottom-Up**
3. **State Definition is Critical**
4. **Draw the DP Table for Understanding**
5. **Practice Pattern Recognition**

Dynamic Programming is challenging but incredibly powerful. With practice, you'll develop strong intuition for recognizing DP problems and choosing the right approach.

---

Next: [Examples](./examples.md) - See 20+ detailed DP implementations!
