# Chapter 40: Dynamic Programming - Solutions

## Table of Contents
1. [Easy Solutions (1-8)](#easy-solutions)
2. [Medium Solutions (9-20)](#medium-solutions)
3. [Hard Solutions (21-25)](#hard-solutions)

---

## Easy Solutions

### Solution 1: Climbing Stairs

#### Approach 1: Memoization (Top-Down)
```python
def climb_stairs_memo(n):
    """
    Time: O(n)
    Space: O(n) - recursion stack + memo
    """
    memo = {}

    def dp(i):
        if i <= 1:
            return 1
        if i in memo:
            return memo[i]

        memo[i] = dp(i-1) + dp(i-2)
        return memo[i]

    return dp(n)
```

#### Approach 2: Tabulation (Bottom-Up)
```python
def climb_stairs_tab(n):
    """
    Time: O(n)
    Space: O(n)
    """
    if n <= 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

#### Approach 3: Space-Optimized
```python
def climb_stairs(n):
    """
    Time: O(n)
    Space: O(1)
    """
    if n <= 1:
        return 1

    prev2, prev1 = 1, 1

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1
```

**Explanation**:
- At each step, you can either come from step i-1 or i-2
- This is exactly Fibonacci: dp[i] = dp[i-1] + dp[i-2]
- Space can be optimized to O(1) since we only need 2 previous values

---

### Solution 2: Min Cost Climbing Stairs

```python
def min_cost_climbing_stairs(cost):
    """
    State: dp[i] = min cost to reach step i
    Recurrence: dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    Time: O(n)
    Space: O(1)
    """
    n = len(cost)

    # Can start from index 0 or 1
    prev2, prev1 = cost[0], cost[1]

    for i in range(2, n):
        curr = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, curr

    # To reach top (past last stair), take min of last two
    return min(prev1, prev2)
```

**Explanation**:
- dp[i] represents minimum cost to reach step i
- To reach step i, we must come from i-1 or i-2, then pay cost[i]
- Final answer is min of reaching last two steps (can step past either)

**Alternative (More Clear)**:
```python
def min_cost_climbing_stairs(cost):
    """Include extra step for 'top'."""
    n = len(cost)
    dp = [0] * (n + 1)

    # Base cases (can start at 0 or 1 for free)
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    # Top is past last stair
    dp[n] = min(dp[n-1], dp[n-2])

    return dp[n]
```

---

### Solution 3: Tribonacci Number

```python
def tribonacci(n):
    """
    Recurrence: T(n) = T(n-1) + T(n-2) + T(n-3)
    Base: T(0)=0, T(1)=1, T(2)=1

    Time: O(n)
    Space: O(1)
    """
    if n == 0:
        return 0
    if n <= 2:
        return 1

    t0, t1, t2 = 0, 1, 1

    for _ in range(3, n + 1):
        t0, t1, t2 = t1, t2, t0 + t1 + t2

    return t2
```

**Explanation**:
- Similar to Fibonacci but sum three previous values
- Only need to track 3 previous values

---

### Solution 4: Divisor Game

```python
def divisor_game(n):
    """
    State: dp[i] = can current player win with number i?
    Transition: Try all valid moves x, if opponent loses, we win

    Time: O(n²)
    Space: O(n)
    """
    dp = [False] * (n + 1)
    dp[1] = False  # Base case: no moves available

    for i in range(2, n + 1):
        # Try all possible divisors
        for x in range(1, i):
            if i % x == 0:  # x is valid divisor
                # If opponent loses with n-x, we win
                if not dp[i - x]:
                    dp[i] = True
                    break

    return dp[n]
```

**Mathematical Solution (O(1))**:
```python
def divisor_game(n):
    """
    Insight: Player with even number always wins!
    - Even: choose 1 (always divisor), give opponent odd
    - Odd: any divisor is odd, so odd-odd = even, give opponent even

    Time: O(1)
    Space: O(1)
    """
    return n % 2 == 0
```

---

### Solution 5: Is Subsequence

#### Two Pointers (Optimal)
```python
def is_subsequence(s, t):
    """
    Time: O(n) where n = len(t)
    Space: O(1)
    """
    i = 0  # pointer for s

    for char in t:
        if i < len(s) and char == s[i]:
            i += 1

    return i == len(s)
```

#### DP Approach (For Learning)
```python
def is_subsequence_dp(s, t):
    """
    State: dp[i][j] = is s[:i] subsequence of t[:j]?

    Time: O(m*n)
    Space: O(m*n) → can optimize to O(n)
    """
    m, n = len(s), len(t)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty string is subsequence of anything
    for j in range(n + 1):
        dp[0][j] = True

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]

    return dp[m][n]
```

---

### Solution 6: N-th Tribonacci (Matrix Exponentiation)

```python
def tribonacci_fast(n):
    """
    Use matrix exponentiation for O(log n)

    [T(n+1)]   [1 1 1]   [T(n)  ]
    [T(n)  ] = [1 0 0] * [T(n-1)]
    [T(n-1)]   [0 1 0]   [T(n-2)]

    Time: O(log n)
    Space: O(1)
    """
    if n == 0:
        return 0
    if n <= 2:
        return 1

    def matrix_mult(A, B):
        """3x3 matrix multiplication."""
        return [
            [sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)
        ]

    def matrix_pow(M, exp):
        """Fast exponentiation."""
        result = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # Identity
        base = [row[:] for row in M]

        while exp:
            if exp & 1:
                result = matrix_mult(result, base)
            base = matrix_mult(base, base)
            exp >>= 1

        return result

    transition = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    result = matrix_pow(transition, n - 2)

    # T(n) = result * [T(2), T(1), T(0)]
    return result[0][0] * 1 + result[0][1] * 1 + result[0][2] * 0
```

---

### Solution 7: Count Bits

#### Approach 1: Using Right Shift
```python
def count_bits(n):
    """
    dp[i] = dp[i >> 1] + (i & 1)

    Explanation:
    - i >> 1 is i with rightmost bit removed
    - i & 1 is rightmost bit (0 or 1)
    - Number of 1s in i = number in (i >> 1) + rightmost bit

    Time: O(n)
    Space: O(n) for output (O(1) auxiliary)
    """
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)

    return ans
```

#### Approach 2: Using Last Set Bit
```python
def count_bits(n):
    """
    dp[i] = dp[i & (i-1)] + 1

    Explanation:
    - i & (i-1) removes the rightmost set bit
    - Number of 1s in i = number in (i with one 1 removed) + 1

    Time: O(n)
    Space: O(n)
    """
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        ans[i] = ans[i & (i - 1)] + 1

    return ans
```

**Examples**:
```
i=5 (0b101):
- i >> 1 = 2 (0b10), count = 1
- i & 1 = 1
- ans[5] = ans[2] + 1 = 1 + 1 = 2

i=6 (0b110):
- i & (i-1) = 6 & 5 = 0b110 & 0b101 = 0b100 = 4
- ans[6] = ans[4] + 1 = 1 + 1 = 2
```

---

### Solution 8: Pascal's Triangle

```python
def generate_pascals_triangle(numRows):
    """
    Generate Pascal's triangle.
    row[i][j] = row[i-1][j-1] + row[i-1][j]

    Time: O(n²) - n rows, row i has i+1 elements
    Space: O(n²) for output
    """
    triangle = []

    for i in range(numRows):
        # Start each row with 1
        row = [1] * (i + 1)

        # Fill middle elements
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)

    return triangle
```

**Space-Optimized (In-Place Row Generation)**:
```python
def generate_pascals_triangle(numRows):
    """Generate row by row, modifying in place."""
    triangle = [[1]]

    for i in range(1, numRows):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
```

---

## Medium Solutions

### Solution 9: House Robber

```python
def rob(nums):
    """
    State: dp[i] = max money robbing first i houses
    Recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    - Skip house i: take dp[i-1]
    - Rob house i: can't rob i-1, so take dp[i-2] + nums[i]

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
```

**Tabulation (For Clarity)**:
```python
def rob_tab(nums):
    """
    Time: O(n)
    Space: O(n)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[n-1]
```

---

### Solution 10: House Robber II

```python
def rob_circular(nums):
    """
    Houses in circle: can't rob both first and last.

    Solution: Solve twice:
    1. Rob houses [0, n-2] (exclude last)
    2. Rob houses [1, n-1] (exclude first)
    Return max of two.

    Time: O(n)
    Space: O(1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    def rob_linear(houses):
        """Helper: rob houses in a line."""
        prev2, prev1 = houses[0], max(houses[0], houses[1])

        for i in range(2, len(houses)):
            curr = max(prev1, prev2 + houses[i])
            prev2, prev1 = prev1, curr

        return prev1

    # Case 1: Rob houses [0, n-2]
    case1 = rob_linear(nums[:-1])

    # Case 2: Rob houses [1, n-1]
    case2 = rob_linear(nums[1:])

    return max(case1, case2)
```

---

### Solution 11: Coin Change

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
            if i >= coin and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

**Alternative (Cleaner)**:
```python
def coin_change(coins, amount):
    """Time: O(amount * n), Space: O(amount)"""
    dp = [amount + 1] * (amount + 1)  # Use amount+1 as "infinity"
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1
```

---

### Solution 12: Coin Change 2

```python
def change(amount, coins):
    """
    State: dp[i] = number of ways to make amount i
    Recurrence: dp[i] += dp[i-coin]

    IMPORTANT: Iterate coins in outer loop to avoid counting duplicates.

    Time: O(amount * n)
    Space: O(amount)
    """
    dp = [0] * (amount + 1)
    dp[0] = 1  # One way to make 0: use no coins

    # Iterate coins in outer loop (order matters!)
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]
```

**Why Order Matters**:
```python
# WRONG: Counts [1,2] and [2,1] as different
for i in range(amount + 1):
    for coin in coins:
        dp[i] += dp[i-coin]

# CORRECT: Coins in outer loop ensures [1,2] counted once
for coin in coins:
    for i in range(amount + 1):
        dp[i] += dp[i-coin]
```

---

### Solution 13: Longest Increasing Subsequence

#### Approach 1: O(n²) DP
```python
def length_of_lis(nums):
    """
    State: dp[i] = LIS length ending at index i
    Recurrence: dp[i] = max(dp[j] + 1) for j<i where nums[j]<nums[i]

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
```

#### Approach 2: O(n log n) with Binary Search
```python
def length_of_lis_optimized(nums):
    """
    Use patience sorting with binary search.
    tails[i] = smallest tail of all increasing subsequences of length i+1

    Time: O(n log n)
    Space: O(n)
    """
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

**Explanation of Binary Search Approach**:
```
nums = [10,9,2,5,3,7,101,18]

Process:
10:  tails = [10]
9:   tails = [9]     (replace 10, same length but better tail)
2:   tails = [2]     (replace 9)
5:   tails = [2,5]   (extend)
3:   tails = [2,3]   (replace 5, length stays 2 but better tail)
7:   tails = [2,3,7] (extend)
101: tails = [2,3,7,101] (extend)
18:  tails = [2,3,7,18]  (replace 101)

Length = 4
```

---

### Solution 14: Longest Common Subsequence

```python
def longest_common_subsequence(text1, text2):
    """
    State: dp[i][j] = LCS length for text1[:i] and text2[:j]
    Recurrence:
    - If text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
    - Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    Time: O(m*n)
    Space: O(m*n) → can optimize to O(min(m,n))
    """
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

**Space-Optimized O(n)**:
```python
def longest_common_subsequence_optimized(text1, text2):
    """
    Space: O(min(m,n))
    """
    # Ensure text2 is shorter for space optimization
    if len(text1) < len(text2):
        text1, text2 = text2, text1

    m, n = len(text1), len(text2)
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
```

---

### Solution 15: Unique Paths

```python
def unique_paths(m, n):
    """
    State: dp[i][j] = paths to reach (i,j)
    Recurrence: dp[i][j] = dp[i-1][j] + dp[i][j-1]

    Time: O(m*n)
    Space: O(n)
    """
    dp = [1] * n  # First row all 1s

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]

    return dp[n-1]
```

**Mathematical Solution (Combinatorics)**:
```python
def unique_paths_math(m, n):
    """
    Need (m-1) downs and (n-1) rights = (m+n-2) total moves
    Choose (m-1) positions for downs: C(m+n-2, m-1)

    Time: O(min(m,n))
    Space: O(1)
    """
    from math import comb
    return comb(m + n - 2, m - 1)
```

---

### Solution 16: Unique Paths II

```python
def unique_paths_with_obstacles(obstacleGrid):
    """
    State: dp[i][j] = paths to (i,j)
    If obstacle at (i,j): dp[i][j] = 0

    Time: O(m*n)
    Space: O(n)
    """
    if not obstacleGrid or obstacleGrid[0][0] == 1:
        return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * n
    dp[0] = 1

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j-1]

    return dp[n-1]
```

---

### Solution 17: Minimum Path Sum

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
```

---

### Solution 18: Triangle

```python
def minimum_total(triangle):
    """
    Work bottom-up.
    dp[j] = min path sum from bottom to position j in current row

    Time: O(n²) where n is number of rows
    Space: O(n)
    """
    n = len(triangle)
    dp = triangle[-1][:]  # Start with last row

    # Work upwards
    for i in range(n-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

    return dp[0]
```

**In-Place Solution**:
```python
def minimum_total_inplace(triangle):
    """Modify triangle in place."""
    n = len(triangle)

    for i in range(n-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

    return triangle[0][0]
```

---

### Solution 19: Partition Equal Subset Sum

```python
def can_partition(nums):
    """
    Find subset with sum = total_sum / 2

    State: dp[s] = can we make sum s?
    Recurrence: dp[s] = dp[s] or dp[s-num]

    Time: O(n * sum)
    Space: O(sum)
    """
    total = sum(nums)

    if total % 2:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        # Iterate backwards to avoid using updated values
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    return dp[target]
```

---

### Solution 20: Target Sum

```python
def find_target_sum_ways(nums, target):
    """
    Transform to subset sum problem.
    Let P = sum of positive nums, N = sum of negative nums
    P - N = target
    P + N = sum(nums)
    => P = (target + sum(nums)) / 2

    Count subsets with sum = (target + sum(nums)) / 2

    Time: O(n * sum)
    Space: O(sum)
    """
    total = sum(nums)

    if total < abs(target) or (target + total) % 2:
        return 0

    subset_sum = (target + total) // 2
    dp = [0] * (subset_sum + 1)
    dp[0] = 1

    for num in nums:
        for s in range(subset_sum, num - 1, -1):
            dp[s] += dp[s - num]

    return dp[subset_sum]
```

---

## Hard Solutions

### Solution 21: Edit Distance

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
    Space: O(m*n) → can optimize to O(min(m,n))
    """
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
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # delete
                    dp[i][j-1],    # insert
                    dp[i-1][j-1]   # replace
                )

    return dp[m][n]
```

**Space-Optimized O(n)**:
```python
def min_distance_optimized(word1, word2):
    """Space: O(min(m,n))"""
    if len(word1) < len(word2):
        word1, word2 = word2, word1

    m, n = len(word1), len(word2)
    prev = list(range(n + 1))

    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
        prev = curr

    return prev[n]
```

---

### Solution 22: Longest Palindromic Subsequence

```python
def longest_palindrome_subseq(s):
    """
    State: dp[i][j] = LPS length in s[i:j+1]
    Recurrence:
    - If s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
    - Else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    Time: O(n²)
    Space: O(n²)
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters
    for i in range(n):
        dp[i][i] = 1

    # Fill by increasing substring length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]
```

**Alternative: LCS with Reverse**:
```python
def longest_palindrome_subseq_lcs(s):
    """
    Insight: LPS of s = LCS of s and reverse(s)

    Time: O(n²)
    Space: O(n²)
    """
    return longest_common_subsequence(s, s[::-1])
```

---

### Solution 23: Regular Expression Matching

```python
def is_match(s, p):
    """
    State: dp[i][j] = does s[:i] match p[:j]?
    Recurrence:
    - If p[j-1] is letter/dot:
        dp[i][j] = dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='.')
    - If p[j-1] is '*':
        dp[i][j] = dp[i][j-2] (match 0)
                or dp[i-1][j] and char_match (match 1+)

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
                # Match 0 occurrences of previous char
                dp[i][j] = dp[i][j-2]

                # Match 1+ occurrences if chars match
                if p[j-2] == s[i-1] or p[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]
            elif p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]

    return dp[m][n]
```

---

### Solution 24: Burst Balloons

```python
def max_coins(nums):
    """
    Think about which balloon to burst LAST in range [i,j].

    State: dp[i][j] = max coins from bursting balloons in (i,j)
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
```

---

### Solution 25: Maximum Profit in Job Scheduling

```python
def job_scheduling(startTime, endTime, profit):
    """
    Sort jobs by end time.
    dp[i] = max profit considering first i jobs

    For each job, either take it or skip:
    - Skip: dp[i] = dp[i-1]
    - Take: dp[i] = profit[i] + dp[j] where j is latest non-overlapping job

    Use binary search to find j efficiently.

    Time: O(n log n)
    Space: O(n)
    """
    import bisect

    # Combine and sort by end time
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    n = len(jobs)

    # Extract sorted arrays
    start = [job[0] for job in jobs]
    end = [job[1] for job in jobs]
    profit = [job[2] for job in jobs]

    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # Option 1: Skip job i-1
        skip = dp[i-1]

        # Option 2: Take job i-1
        # Find latest job that doesn't overlap
        j = bisect.bisect_right(end, start[i-1])
        take = profit[i-1] + dp[j]

        dp[i] = max(skip, take)

    return dp[n]
```

**Alternative with Dictionary (Cleaner)**:
```python
def job_scheduling(startTime, endTime, profit):
    """Use dictionary for DP."""
    import bisect

    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    end_times = [job[1] for job in jobs]

    dp = {}
    dp[0] = 0  # Base: no jobs, 0 profit

    for i, (start, end, prof) in enumerate(jobs, 1):
        # Find latest non-overlapping job
        j = bisect.bisect_right(end_times, start)

        # Take current job or skip
        dp[end] = max(dp.get(end_times[i-2] if i > 1 else 0, 0),
                      dp[end_times[j-1] if j > 0 else 0] + prof)

    return max(dp.values())
```

---

## Summary

### Key Patterns Covered

1. **1D Linear DP**: Problems 1-4, 9-10
2. **2D Grid DP**: Problems 8, 15-18
3. **2D Two-Sequence DP**: Problems 5, 14, 21, 23
4. **Knapsack Variants**: Problems 11-12, 19-20
5. **Sequence DP**: Problems 13, 22
6. **Interval DP**: Problems 22, 24
7. **DP with Binary Search**: Problem 25
8. **Bit DP**: Problem 7

### Optimization Techniques Used

1. **Space Optimization**: Rolling arrays (1D → O(1), 2D → O(n))
2. **In-Place DP**: Modifying input when allowed
3. **Binary Search**: Reducing O(n) to O(log n) for lookups
4. **Matrix Exponentiation**: O(n) to O(log n) for linear recurrences
5. **Mathematical Solutions**: Combinatorics instead of DP

### Common Mistakes to Avoid

1. ❌ Wrong base case initialization
2. ❌ Off-by-one errors in indices
3. ❌ Iterating in wrong order (especially with space optimization)
4. ❌ Not handling edge cases (empty input, single element)
5. ❌ Using updated values when should use previous (iterate backwards)

---

**Next Steps**:
1. Implement all solutions from scratch without looking
2. Time yourself on medium problems (aim for 15-20 minutes)
3. Review [Tips](./tips.md) for LeetCode problem list
4. Practice pattern recognition on new problems

Keep practicing! Dynamic Programming mastery comes with recognizing patterns quickly.
