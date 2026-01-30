# Chapter 40: Dynamic Programming - Tips and Tricks

## Table of Contents
1. [Common Pitfalls](#common-pitfalls)
2. [Pattern Recognition](#pattern-recognition)
3. [Interview Tips](#interview-tips)
4. [Performance Optimization](#performance-optimization)
5. [LeetCode Practice Problems (80+)](#leetcode-practice-problems)

---

## Common Pitfalls

### 1. Wrong Base Case Initialization

```python
# ❌ WRONG: Coin Change with wrong initialization
def coin_change(coins, amount):
    dp = [0] * (amount + 1)  # Wrong! 0 means 0 coins needed
    for i in range(1, amount + 1):
        dp[i] = min(dp[i-coin] + 1 for coin in coins if i >= coin)
    # This will give wrong results!

# ✅ CORRECT: Initialize with infinity
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins for amount 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

### 2. Space Optimization Gone Wrong

```python
# ❌ WRONG: Using updated values in 0/1 knapsack
def knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(weights[i], capacity + 1):  # Forward iteration!
            dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
    # This becomes unbounded knapsack (wrong!)

# ✅ CORRECT: Iterate backwards
def knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):  # Backwards!
            dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
    return dp[capacity]
```

### 3. Coin Change 2: Order Matters

```python
# ❌ WRONG: Counts permutations, not combinations
def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] += dp[i-coin]
    # This counts [1,2] and [2,1] as different!

# ✅ CORRECT: Coins in outer loop
def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:  # Outer loop!
        for i in range(coin, amount + 1):
            dp[i] += dp[i-coin]
    return dp[amount]
```

### 4. LCS: Off-By-One Errors

```python
# ❌ WRONG: Indices don't match DP table
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i] == text2[j]:  # Wrong! Should be i-1, j-1
                dp[i][j] = dp[i-1][j-1] + 1

# ✅ CORRECT: Account for 0-indexing
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:  # i-1 and j-1!
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

### 5. Forgetting to Check Feasibility

```python
# ❌ WRONG: Target Sum without feasibility check
def find_target_sum_ways(nums, target):
    total = sum(nums)
    subset_sum = (target + total) // 2  # May be invalid!
    # Proceed with DP...

# ✅ CORRECT: Check feasibility first
def find_target_sum_ways(nums, target):
    total = sum(nums)

    # Feasibility checks
    if total < abs(target):  # Impossible to reach
        return 0
    if (target + total) % 2:  # Must be even
        return 0

    subset_sum = (target + total) // 2
    # Now proceed with DP
```

### 6. House Robber II: Wrong Split

```python
# ❌ WRONG: Missing edge case
def rob(nums):
    if len(nums) == 1:  # Missing this check!
        return nums[0]

    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# ✅ CORRECT: Handle all edge cases
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
```

---

## Pattern Recognition

### How to Identify DP Problems

#### Checklist
1. ✅ **Optimization** (max/min) or **Counting** (number of ways)?
2. ✅ **Overlapping subproblems** (same calculation repeated)?
3. ✅ **Optimal substructure** (optimal solution contains optimal sub-solutions)?
4. ✅ Can define **state** and **transitions**?

#### Keywords That Suggest DP
- "Maximum/Minimum"
- "Longest/Shortest"
- "Count number of ways"
- "Is it possible to..."
- "Optimal"
- "Fewest/Most"

### Pattern Classification

#### Pattern 1: Linear DP (1D)
**When to use**: Single sequence, decision at each element

**State**: `dp[i]` = answer for first i elements

**Examples**:
- Climbing Stairs
- House Robber
- Decode Ways
- Jump Game

**Template**:
```python
dp = [base] * n
for i in range(n):
    for prev_state in relevant_previous_states:
        dp[i] = combine(dp[i], dp[prev_state])
```

#### Pattern 2: Grid DP (2D)
**When to use**: 2D grid, path finding

**State**: `dp[i][j]` = answer for cell (i,j)

**Examples**:
- Unique Paths
- Minimum Path Sum
- Dungeon Game

**Template**:
```python
dp = [[base] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        dp[i][j] = combine(dp[i-1][j], dp[i][j-1], ...)
```

#### Pattern 3: Two Sequences (2D)
**When to use**: Two strings/arrays, find relationship

**State**: `dp[i][j]` = answer for seq1[:i] and seq2[:j]

**Examples**:
- LCS
- Edit Distance
- Distinct Subsequences

**Template**:
```python
dp = [[base] * (n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if condition(seq1[i-1], seq2[j-1]):
            dp[i][j] = compute_from_diagonal(dp[i-1][j-1])
        else:
            dp[i][j] = combine(dp[i-1][j], dp[i][j-1])
```

#### Pattern 4: Knapsack
**When to use**: Items with weights/costs, capacity constraint

**State**: `dp[i][w]` = optimal value with first i items, capacity w

**Examples**:
- 0/1 Knapsack
- Partition Equal Subset Sum
- Target Sum

**0/1 Knapsack Template**:
```python
dp = [0] * (capacity + 1)
for item in items:
    for w in range(capacity, weight[item] - 1, -1):  # Backwards!
        dp[w] = max(dp[w], dp[w-weight[item]] + value[item])
```

**Unbounded Knapsack Template**:
```python
dp = [0] * (capacity + 1)
for item in items:
    for w in range(weight[item], capacity + 1):  # Forward!
        dp[w] = max(dp[w], dp[w-weight[item]] + value[item])
```

#### Pattern 5: Interval DP
**When to use**: Subarray/substring problems, range queries

**State**: `dp[i][j]` = answer for range [i,j]

**Examples**:
- Burst Balloons
- Palindrome Partitioning
- Matrix Chain Multiplication

**Template**:
```python
n = len(arr)
dp = [[base] * n for _ in range(n)]

# Base case: length 1
for i in range(n):
    dp[i][i] = base_value

# Fill by increasing length
for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        for k in range(i, j+1):  # Split point
            dp[i][j] = optimize(dp[i][j], dp[i][k], dp[k+1][j])
```

#### Pattern 6: State Machine
**When to use**: Multiple states with transitions

**State**: `dp[i][state]` = answer at position i in state

**Examples**:
- Best Time to Buy and Sell Stock
- Paint House
- House Robber with Cooldown

**Template**:
```python
states = ['state1', 'state2', ...]
dp = {state: initial_value for state in states}

for i in range(n):
    new_dp = {}
    for state in states:
        for next_state in valid_transitions[state]:
            new_dp[next_state] = optimize(
                new_dp.get(next_state, default),
                dp[state] + transition_cost(state, next_state)
            )
    dp = new_dp
```

---

## Interview Tips

### Step-by-Step Approach

#### Step 1: Recognize DP (1 minute)
- Check for optimization/counting
- Look for overlapping subproblems
- Verify optimal substructure

#### Step 2: Define State (2-3 minutes)
Ask yourself:
- What changes between subproblems?
- What information do I need to make a decision?
- 1D state? 2D state? Multi-dimensional?

#### Step 3: Write Recurrence (3-5 minutes)
- What are the base cases?
- How to compute dp[current] from previous states?
- What are the choices/transitions?

#### Step 4: Implement (5-10 minutes)
- Start with memoization (easier to code)
- Use dictionary for memo (handles any state)
- Add base cases first, then recursion

#### Step 5: Optimize (2-5 minutes)
- Can space be reduced?
- Can time be optimized?
- Are there unnecessary computations?

### Communication During Interview

**Good Framework**:
```
1. "This looks like a DP problem because..."
   - Explain overlapping subproblems
   - Mention optimal substructure

2. "Let me define the state..."
   - Clearly state what dp[i] or dp[i][j] represents
   - Give concrete example

3. "The recurrence relation is..."
   - Explain the choices/transitions
   - Show how to combine subproblems

4. "Let me trace through an example..."
   - Walk through small input
   - Show DP table evolution

5. "I can optimize this by..."
   - Space optimization
   - Early termination
```

### Time Management

**Target Times** (for 45-minute interview):
- Easy DP: 10-15 minutes
- Medium DP: 20-30 minutes
- Hard DP: 35-45 minutes (may not finish optimization)

**If stuck**:
1. Start with brute force recursion (5 min)
2. Add memoization (2 min)
3. Discuss time/space complexity
4. Mention tabulation as optimization

---

## Performance Optimization

### Space Optimization Techniques

#### Technique 1: 1D → O(1)
When `dp[i]` only depends on constant previous states:

```python
# Before: O(n) space
dp = [0] * n
for i in range(n):
    dp[i] = f(dp[i-1], dp[i-2])

# After: O(1) space
prev2, prev1 = base1, base2
for i in range(n):
    curr = f(prev1, prev2)
    prev2, prev1 = prev1, curr
```

#### Technique 2: 2D → 1D
When `dp[i][j]` only depends on previous row:

```python
# Before: O(m*n) space
dp = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        dp[i][j] = f(dp[i-1][j], dp[i][j-1])

# After: O(n) space
dp = [0] * n
for i in range(m):
    for j in range(n):
        dp[j] = f(dp[j], dp[j-1])  # dp[j] is "previous row"
```

#### Technique 3: In-Place Modification
When input can be modified:

```python
# Before: O(m*n) extra space
def min_path_sum(grid):
    dp = [[0] * len(grid[0]) for _ in range(len(grid))]
    # ...

# After: O(1) extra space
def min_path_sum(grid):
    # Modify grid in place
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i > 0 and j > 0:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
```

### Time Optimization Techniques

#### Technique 1: Binary Search
In LIS, reduce O(n²) to O(n log n):

```python
# O(n²) approach
def length_of_lis(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# O(n log n) approach with binary search
def length_of_lis(nums):
    import bisect
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```

#### Technique 2: Early Termination
Stop when answer found:

```python
def can_partition(nums):
    target = sum(nums) // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]
            if dp[target]:  # Early termination!
                return True

    return dp[target]
```

#### Technique 3: Pruning
Skip impossible states:

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        if dp[i-1] == float('inf'):  # Pruning: can't reach i-1
            continue
        for coin in coins:
            if i + coin <= amount:
                dp[i + coin] = min(dp[i + coin], dp[i] + 1)
```

---

## LeetCode Practice Problems

### Study Plan Overview

**Total**: 85+ problems organized by pattern and difficulty
**Estimated Time**: 80-100 hours for complete mastery
**Recommended Pace**: 10-12 problems per week

### Difficulty Distribution
- ⭐ Easy: 20 problems
- ⭐⭐ Medium: 50 problems
- ⭐⭐⭐ Hard: 15 problems

---

### Phase 1: Foundations (Week 1-2) - 20 Problems

#### 1.1 Linear DP - Fibonacci Variants
1. ⭐ [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
   - **Pattern**: 1D DP, Fibonacci
   - **Time**: 10 min
   - **Key**: dp[i] = dp[i-1] + dp[i-2]

2. ⭐ [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)
   - **Pattern**: 1D DP with cost
   - **Time**: 10 min
   - **Key**: Can start at index 0 or 1

3. ⭐ [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)
   - **Pattern**: 1D DP, three previous
   - **Time**: 10 min
   - **Key**: T(n) = T(n-1) + T(n-2) + T(n-3)

#### 1.2 Simple Decision DP
4. ⭐ [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
   - **Pattern**: Basic DP
   - **Time**: 5 min
   - **Key**: Classic problem

5. ⭐⭐ [198. House Robber](https://leetcode.com/problems/house-robber/)
   - **Pattern**: 1D DP, skip or take
   - **Time**: 15 min
   - **Key**: dp[i] = max(dp[i-1], dp[i-2] + nums[i])

6. ⭐⭐ [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)
   - **Pattern**: 1D DP, circular constraint
   - **Time**: 20 min
   - **Key**: Rob [0,n-2] or [1,n-1]

7. ⭐⭐ [740. Delete and Earn](https://leetcode.com/problems/delete-and-earn/)
   - **Pattern**: Transform to House Robber
   - **Time**: 20 min
   - **Key**: Count frequencies, then house robber

#### 1.3 Grid DP Basics
8. ⭐⭐ [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
   - **Pattern**: 2D grid DP
   - **Time**: 15 min
   - **Key**: dp[i][j] = dp[i-1][j] + dp[i][j-1]

9. ⭐⭐ [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)
   - **Pattern**: 2D grid with obstacles
   - **Time**: 15 min
   - **Key**: If obstacle, dp[i][j] = 0

10. ⭐⭐ [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
    - **Pattern**: 2D grid DP
    - **Time**: 15 min
    - **Key**: Can modify in place

11. ⭐⭐ [120. Triangle](https://leetcode.com/problems/triangle/)
    - **Pattern**: Top-down path
    - **Time**: 15 min
    - **Key**: Work bottom-up

#### 1.4 Simple String DP
12. ⭐ [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)
    - **Pattern**: Two pointers (DP for learning)
    - **Time**: 10 min
    - **Key**: Simple LCS variant

13. ⭐⭐ [91. Decode Ways](https://leetcode.com/problems/decode-ways/)
    - **Pattern**: 1D DP, decode decisions
    - **Time**: 20 min
    - **Key**: Check 1-digit and 2-digit decodings

14. ⭐⭐ [139. Word Break](https://leetcode.com/problems/word-break/)
    - **Pattern**: String DP
    - **Time**: 20 min
    - **Key**: dp[i] = any dp[j] and s[j:i] in dict

#### 1.5 Bit DP
15. ⭐ [338. Counting Bits](https://leetcode.com/problems/counting-bits/)
    - **Pattern**: Bit DP
    - **Time**: 10 min
    - **Key**: dp[i] = dp[i>>1] + (i&1)

16. ⭐ [1025. Divisor Game](https://leetcode.com/problems/divisor-game/)
    - **Pattern**: Game theory DP
    - **Time**: 15 min
    - **Key**: n%2==0 always wins

#### 1.6 Array DP
17. ⭐⭐ [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
    - **Pattern**: Kadane's algorithm
    - **Time**: 10 min
    - **Key**: dp[i] = max(dp[i-1] + nums[i], nums[i])

18. ⭐⭐ [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
    - **Pattern**: Track max and min
    - **Time**: 20 min
    - **Key**: Negative flips max/min

19. ⭐⭐ [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)
    - **Pattern**: Kadane's with wrap
    - **Time**: 25 min
    - **Key**: Max(normal, total - min_subarray)

20. ⭐ [1646. Get Maximum in Generated Array](https://leetcode.com/problems/get-maximum-in-generated-array/)
    - **Pattern**: Array generation DP
    - **Time**: 10 min
    - **Key**: Follow generation rules

---

### Phase 2: Core Patterns (Week 3-4) - 25 Problems

#### 2.1 Knapsack - Unbounded
21. ⭐⭐ [322. Coin Change](https://leetcode.com/problems/coin-change/)
    - **Pattern**: Unbounded knapsack
    - **Time**: 20 min
    - **Key**: Fewest coins, initialize with inf

22. ⭐⭐ [518. Coin Change 2](https://leetcode.com/problems/coin-change-2/)
    - **Pattern**: Unbounded knapsack, counting
    - **Time**: 20 min
    - **Key**: Coins in outer loop!

23. ⭐⭐ [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)
    - **Pattern**: Unbounded knapsack
    - **Time**: 20 min
    - **Key**: Coins are perfect squares

24. ⭐⭐ [983. Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/)
    - **Pattern**: Unbounded knapsack variant
    - **Time**: 25 min
    - **Key**: Choose 1-day, 7-day, or 30-day pass

#### 2.2 Knapsack - 0/1
25. ⭐⭐ [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
    - **Pattern**: 0/1 knapsack, subset sum
    - **Time**: 20 min
    - **Key**: Find subset with sum = total/2

26. ⭐⭐ [494. Target Sum](https://leetcode.com/problems/target-sum/)
    - **Pattern**: 0/1 knapsack transformation
    - **Time**: 25 min
    - **Key**: Transform to subset sum

27. ⭐⭐ [1049. Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/)
    - **Pattern**: 0/1 knapsack
    - **Time**: 25 min
    - **Key**: Partition into two groups

28. ⭐⭐ [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)
    - **Pattern**: Backtracking + DP
    - **Time**: 30 min
    - **Key**: More complex than simple knapsack

#### 2.3 Sequence DP - LIS Variants
29. ⭐⭐ [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
    - **Pattern**: Sequence DP
    - **Time**: 20 min (O(n²)), 30 min (O(n log n))
    - **Key**: dp[i] = LIS ending at i

30. ⭐⭐ [673. Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)
    - **Pattern**: LIS with counting
    - **Time**: 30 min
    - **Key**: Track both length and count

31. ⭐⭐ [646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/)
    - **Pattern**: LIS variant
    - **Time**: 20 min
    - **Key**: Sort + LIS or greedy

32. ⭐⭐ [354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)
    - **Pattern**: 2D LIS
    - **Time**: 30 min
    - **Key**: Sort + LIS on one dimension

33. ⭐⭐ [368. Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/)
    - **Pattern**: LIS with divisibility
    - **Time**: 25 min
    - **Key**: Similar structure to LIS

#### 2.4 Two Sequences - LCS Variants
34. ⭐⭐ [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
    - **Pattern**: 2D DP, two sequences
    - **Time**: 20 min
    - **Key**: Classic LCS

35. ⭐⭐ [583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)
    - **Pattern**: LCS variant
    - **Time**: 20 min
    - **Key**: Delete = length - LCS

36. ⭐⭐ [712. Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)
    - **Pattern**: LCS with cost
    - **Time**: 25 min
    - **Key**: Track ASCII sums

37. ⭐⭐ [1035. Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/)
    - **Pattern**: LCS in disguise
    - **Time**: 15 min
    - **Key**: Exactly LCS problem

38. ⭐⭐ [1458. Max Dot Product of Two Subsequences](https://leetcode.com/problems/max-dot-product-of-two-subsequences/)
    - **Pattern**: 2D DP
    - **Time**: 30 min
    - **Key**: Include/exclude decisions

#### 2.5 Jump Game Variants
39. ⭐⭐ [55. Jump Game](https://leetcode.com/problems/jump-game/)
    - **Pattern**: DP or greedy
    - **Time**: 15 min
    - **Key**: Track farthest reachable

40. ⭐⭐ [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)
    - **Pattern**: BFS or DP
    - **Time**: 20 min
    - **Key**: Minimum jumps

41. ⭐⭐ [1306. Jump Game III](https://leetcode.com/problems/jump-game-iii/)
    - **Pattern**: DFS/BFS
    - **Time**: 15 min
    - **Key**: Can jump left or right

42. ⭐⭐ [1345. Jump Game IV](https://leetcode.com/problems/jump-game-iv/)
    - **Pattern**: BFS with hash map
    - **Time**: 25 min
    - **Key**: Jump to same values

#### 2.6 Matrix DP
43. ⭐⭐ [221. Maximal Square](https://leetcode.com/problems/maximal-square/)
    - **Pattern**: 2D DP
    - **Time**: 25 min
    - **Key**: dp[i][j] = side length of square

44. ⭐⭐ [304. Range Sum Query 2D](https://leetcode.com/problems/range-sum-query-2d-immutable/)
    - **Pattern**: Prefix sum 2D
    - **Time**: 20 min
    - **Key**: Build prefix sum matrix

45. ⭐⭐⭐ [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
    - **Pattern**: DP + monotonic stack
    - **Time**: 35 min
    - **Key**: Each row as histogram

---

### Phase 3: Advanced Patterns (Week 5-6) - 25 Problems

#### 3.1 String DP
46. ⭐⭐⭐ [72. Edit Distance](https://leetcode.com/problems/edit-distance/)
    - **Pattern**: 2D string DP
    - **Time**: 25 min
    - **Key**: Insert/delete/replace operations

47. ⭐⭐ [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)
    - **Pattern**: 2D string DP, counting
    - **Time**: 25 min
    - **Key**: Count ways to match

48. ⭐⭐ [97. Interleaving String](https://leetcode.com/problems/interleaving-string/)
    - **Pattern**: 2D string DP
    - **Time**: 25 min
    - **Key**: Track positions in both strings

49. ⭐⭐⭐ [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
    - **Pattern**: 2D string DP, complex
    - **Time**: 35 min
    - **Key**: Handle '.' and '*' carefully

50. ⭐⭐⭐ [44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)
    - **Pattern**: 2D string DP
    - **Time**: 30 min
    - **Key**: Similar to regex but simpler '*'

51. ⭐⭐ [140. Word Break II](https://leetcode.com/problems/word-break-ii/)
    - **Pattern**: String DP + backtracking
    - **Time**: 30 min
    - **Key**: Find all segmentations

#### 3.2 Palindrome DP
52. ⭐⭐ [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
    - **Pattern**: Interval DP
    - **Time**: 20 min
    - **Key**: Expand from center or DP

53. ⭐⭐ [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
    - **Pattern**: Interval DP
    - **Time**: 25 min
    - **Key**: dp[i][j] for range [i,j]

54. ⭐⭐ [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
    - **Pattern**: Expand from center or DP
    - **Time**: 20 min
    - **Key**: Count all palindromes

55. ⭐⭐⭐ [132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)
    - **Pattern**: String DP + palindrome table
    - **Time**: 30 min
    - **Key**: Precompute palindromes

56. ⭐⭐ [1312. Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)
    - **Pattern**: LCS with reverse
    - **Time**: 20 min
    - **Key**: length - LCS(s, reverse(s))

#### 3.3 State Machine DP - Stock Problems
57. ⭐ [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
    - **Pattern**: Simple tracking
    - **Time**: 10 min
    - **Key**: Track min price

58. ⭐⭐ [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
    - **Pattern**: State machine, unlimited transactions
    - **Time**: 15 min
    - **Key**: Sum all positive differences

59. ⭐⭐⭐ [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
    - **Pattern**: State machine, 2 transactions
    - **Time**: 30 min
    - **Key**: Track 4 states

60. ⭐⭐⭐ [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
    - **Pattern**: State machine, k transactions
    - **Time**: 35 min
    - **Key**: Generalize to k

61. ⭐⭐ [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
    - **Pattern**: State machine
    - **Time**: 25 min
    - **Key**: 3 states: hold, sold, rest

62. ⭐⭐ [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
    - **Pattern**: State machine
    - **Time**: 20 min
    - **Key**: Deduct fee on sell

#### 3.4 State Machine DP - Other
63. ⭐⭐ [256. Paint House](https://leetcode.com/problems/paint-house/) 🔒
    - **Pattern**: State machine, 3 colors
    - **Time**: 15 min
    - **Key**: Can't use same color as previous

64. ⭐⭐ [265. Paint House II](https://leetcode.com/problems/paint-house-ii/) 🔒
    - **Pattern**: State machine, k colors
    - **Time**: 25 min
    - **Key**: Track min and second min

65. ⭐⭐ [276. Paint Fence](https://leetcode.com/problems/paint-fence/) 🔒
    - **Pattern**: State machine
    - **Time**: 20 min
    - **Key**: Track same/different from previous

#### 3.5 Interval DP
66. ⭐⭐⭐ [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/)
    - **Pattern**: Interval DP
    - **Time**: 35 min
    - **Key**: Think about which to burst LAST

67. ⭐⭐⭐ [1039. Minimum Score Triangulation of Polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/)
    - **Pattern**: Interval DP
    - **Time**: 30 min
    - **Key**: Similar to burst balloons

68. ⭐⭐⭐ [1000. Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/)
    - **Pattern**: Interval DP with constraint
    - **Time**: 40 min
    - **Key**: Must merge k piles at a time

69. ⭐⭐⭐ [1547. Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)
    - **Pattern**: Interval DP
    - **Time**: 30 min
    - **Key**: Try all cut positions

70. ⭐⭐⭐ [546. Remove Boxes](https://leetcode.com/problems/remove-boxes/)
    - **Pattern**: Interval DP, 3D state
    - **Time**: 45 min
    - **Key**: Track consecutive boxes

---

### Phase 4: Mastery (Week 7-8) - 15 Problems

#### 4.1 Tree DP
71. ⭐⭐ [337. House Robber III](https://leetcode.com/problems/house-robber-iii/)
    - **Pattern**: Tree DP
    - **Time**: 25 min
    - **Key**: Return (rob_root, not_rob_root)

72. ⭐⭐⭐ [968. Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/)
    - **Pattern**: Tree DP, greedy
    - **Time**: 35 min
    - **Key**: 3 states: has camera, monitored, not monitored

73. ⭐⭐ [1130. Minimum Cost Tree From Leaf Values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/)
    - **Pattern**: Interval DP on array
    - **Time**: 30 min
    - **Key**: Choose root of subtree

#### 4.2 Bitmask DP
74. ⭐⭐⭐ [847. Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)
    - **Pattern**: Bitmask DP, BFS
    - **Time**: 35 min
    - **Key**: State (node, visited_mask)

75. ⭐⭐⭐ [943. Find the Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/)
    - **Pattern**: Bitmask DP, TSP variant
    - **Time**: 45 min
    - **Key**: dp[mask][i] = min superstring

76. ⭐⭐⭐ [1349. Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/)
    - **Pattern**: Bitmask DP
    - **Time**: 40 min
    - **Key**: State = row mask

#### 4.3 Digit DP
77. ⭐⭐⭐ [233. Number of Digit One](https://leetcode.com/problems/number-of-digit-one/)
    - **Pattern**: Digit DP
    - **Time**: 35 min
    - **Key**: Count 1s in each position

78. ⭐⭐⭐ [902. Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/)
    - **Pattern**: Digit DP
    - **Time**: 30 min
    - **Key**: Build numbers digit by digit

#### 4.4 Probability DP
79. ⭐⭐ [688. Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/)
    - **Pattern**: Probability DP
    - **Time**: 25 min
    - **Key**: dp[k][r][c] = probability

80. ⭐⭐ [837. New 21 Game](https://leetcode.com/problems/new-21-game/)
    - **Pattern**: Probability DP, sliding window
    - **Time**: 30 min
    - **Key**: Use sliding window for sum

#### 4.5 Hard Interview Favorites
81. ⭐⭐⭐ [1220. Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation/)
    - **Pattern**: State machine DP
    - **Time**: 25 min
    - **Key**: Transition rules for vowels

82. ⭐⭐⭐ [1187. Make Array Strictly Increasing](https://leetcode.com/problems/make-array-strictly-increasing/)
    - **Pattern**: DP with binary search
    - **Time**: 40 min
    - **Key**: dp[i][j] = min ops for arr1[:i] with j replacements

83. ⭐⭐⭐ [1125. Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/)
    - **Pattern**: Bitmask DP, set cover
    - **Time**: 40 min
    - **Key**: dp[mask] = smallest team

84. ⭐⭐⭐ [1478. Allocate Mailboxes](https://leetcode.com/problems/allocate-mailboxes/)
    - **Pattern**: 2D DP + precomputation
    - **Time**: 35 min
    - **Key**: dp[i][k] = cost for first i houses with k mailboxes

85. ⭐⭐⭐ [1639. Number of Ways to Form a Target String Given a Dictionary](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/)
    - **Pattern**: 2D DP with counting
    - **Time**: 35 min
    - **Key**: Count characters at each position

---

## Study Schedule

### 8-Week Intensive Plan

**Week 1**: Problems 1-10 (Foundations)
- Day 1: Problems 1-3 (Fibonacci variants)
- Day 2: Problems 4-7 (Decision DP)
- Day 3: Problems 8-10 (Grid DP basics)

**Week 2**: Problems 11-20 (More Foundations)
- Day 1: Problems 11-14 (String DP)
- Day 2: Problems 15-17 (Bit & Array DP)
- Day 3: Problems 18-20 (Advanced array DP)

**Week 3**: Problems 21-33 (Core Patterns Part 1)
- Day 1: Problems 21-24 (Unbounded Knapsack)
- Day 2: Problems 25-28 (0/1 Knapsack)
- Day 3: Problems 29-33 (LIS variants)

**Week 4**: Problems 34-45 (Core Patterns Part 2)
- Day 1: Problems 34-38 (LCS variants)
- Day 2: Problems 39-42 (Jump games)
- Day 3: Problems 43-45 (Matrix DP)

**Week 5**: Problems 46-56 (Advanced Part 1)
- Day 1: Problems 46-51 (String DP)
- Day 2: Problems 52-56 (Palindrome DP)

**Week 6**: Problems 57-70 (Advanced Part 2)
- Day 1: Problems 57-62 (Stock problems)
- Day 2: Problems 63-65 (State machine)
- Day 3: Problems 66-70 (Interval DP)

**Week 7**: Problems 71-80 (Mastery Part 1)
- Day 1: Problems 71-73 (Tree DP)
- Day 2: Problems 74-76 (Bitmask DP)
- Day 3: Problems 77-80 (Digit & Probability DP)

**Week 8**: Problems 81-85 + Review
- Day 1: Problems 81-85 (Hard favorites)
- Day 2: Review weak patterns
- Day 3: Timed practice

---

## Final Tips

### Before Interview
1. ✅ Review pattern templates
2. ✅ Practice 2-3 medium problems
3. ✅ Know time/space complexity formulas
4. ✅ Review common pitfalls

### During Interview
1. ✅ Communicate your thought process
2. ✅ Start with brute force, optimize to DP
3. ✅ Draw DP table for small example
4. ✅ Code memoization first (easier)
5. ✅ Discuss space optimization

### After Interview
1. ✅ Review what went well
2. ✅ Identify patterns you struggled with
3. ✅ Practice similar problems
4. ✅ Track your progress

---

## Resources

### Online Platforms
- [LeetCode DP Tag](https://leetcode.com/tag/dynamic-programming/)
- [LeetCode DP Explore Card](https://leetcode.com/explore/featured/card/dynamic-programming/)
- [NeetCode DP Roadmap](https://neetcode.io/roadmap)

### Visualizations
- [VisuAlgo DP](https://visualgo.net/en/recursion)
- [Algorithm Visualizer](https://algorithm-visualizer.org/)

### Articles
- [DP Patterns for Coding Interviews](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)
- [Comprehensive DP Tutorial](https://leetcode.com/discuss/general-discussion/651719/how-to-solve-dp-string-template-and-4-steps-to-be-followed)

---

**Remember**: Dynamic Programming mastery comes through practice and pattern recognition. Don't get discouraged by difficult problems. Focus on understanding the patterns, and gradually increase difficulty. With consistent practice of these 85+ problems, you'll develop strong DP intuition for technical interviews.

Good luck! 🚀
