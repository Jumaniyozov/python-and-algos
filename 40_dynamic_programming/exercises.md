# Chapter 40: Dynamic Programming - Exercises

## Table of Contents
1. [Easy Problems (1-8)](#easy-problems)
2. [Medium Problems (9-20)](#medium-problems)
3. [Hard Problems (21-25)](#hard-problems)
4. [Problem Categories](#problem-categories)

---

## Easy Problems

### Problem 1: Climbing Stairs (Fibonacci Variant)

**Difficulty**: Easy
**Pattern**: 1D DP

You are climbing a staircase with `n` steps. You can climb 1 or 2 steps at a time. How many distinct ways can you climb to the top?

**Example**:
```
Input: n = 3
Output: 3
Explanation: Three ways: 1+1+1, 1+2, 2+1
```

**Constraints**:
- 1 ≤ n ≤ 45

**Hints**:
- Think about how you can reach step n
- The answer is similar to Fibonacci sequence
- Can you optimize space to O(1)?

---

### Problem 2: Min Cost Climbing Stairs

**Difficulty**: Easy
**Pattern**: 1D DP

You are given an array `cost` where `cost[i]` is the cost of stepping on the ith stair. You can start from index 0 or 1. Find minimum cost to reach the top (past the last stair).

**Example**:
```
Input: cost = [10,15,20]
Output: 15
Explanation: Start at index 1, pay 15, and step to the top.
```

**Constraints**:
- 2 ≤ cost.length ≤ 1000
- 0 ≤ cost[i] ≤ 999

**Hints**:
- dp[i] = minimum cost to reach step i
- You can reach step i from step i-1 or i-2
- What are the base cases?

---

### Problem 3: Tribonacci Number

**Difficulty**: Easy
**Pattern**: 1D DP

The Tribonacci sequence is defined as:
- T₀ = 0, T₁ = 1, T₂ = 1
- Tₙ₊₃ = Tₙ + Tₙ₊₁ + Tₙ₊₂ for n ≥ 0

Given `n`, return the value of Tₙ.

**Example**:
```
Input: n = 4
Output: 4
Explanation: T₄ = 0 + 1 + 1 = 2, T₃ = 0 + 1 + 1 = 2, T₄ = 1 + 1 + 2 = 4
```

**Constraints**:
- 0 ≤ n ≤ 37

**Hints**:
- Similar to Fibonacci but with 3 previous values
- Can be done in O(1) space

---

### Problem 4: Divisor Game

**Difficulty**: Easy
**Pattern**: Game Theory DP

Alice and Bob take turns playing a game on a chalkboard with number `n`. On each turn, a player chooses `x` where `0 < x < n` and `n % x == 0`, then replaces `n` with `n - x`. The player who cannot make a move loses.

Return `true` if Alice wins assuming both play optimally.

**Example**:
```
Input: n = 2
Output: true
Explanation: Alice chooses 1, n becomes 1. Bob cannot make a move.
```

**Constraints**:
- 1 ≤ n ≤ 1000

**Hints**:
- dp[i] = can current player win with number i?
- For each valid move x, check if opponent loses
- Base case: dp[1] = false (no valid moves)

---

### Problem 5: Is Subsequence

**Difficulty**: Easy
**Pattern**: String DP (Two Pointers also works)

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`.

**Example**:
```
Input: s = "abc", t = "ahbgdc"
Output: true
```

**Constraints**:
- 0 ≤ s.length ≤ 100
- 0 ≤ t.length ≤ 10⁴

**Hints**:
- Can be solved with two pointers (easier)
- DP approach: dp[i][j] = is s[:i] subsequence of t[:j]?
- This is a simplified LCS problem

---

### Problem 6: N-th Tribonacci Number

**Difficulty**: Easy
**Pattern**: 1D DP with Matrix Exponentiation (Optional)

Same as Problem 3, but solve it using matrix exponentiation for O(log n) time.

**Hints**:
- Represent recurrence as matrix multiplication
- Use fast exponentiation for O(log n)

---

### Problem 7: Count Bits

**Difficulty**: Easy
**Pattern**: Bit DP

Given an integer `n`, return an array `ans` of length `n + 1` where `ans[i]` is the number of 1's in the binary representation of `i`.

**Example**:
```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 -> 0b0 (0 ones)
1 -> 0b1 (1 one)
2 -> 0b10 (1 one)
3 -> 0b11 (2 ones)
4 -> 0b100 (1 one)
5 -> 0b101 (2 ones)
```

**Constraints**:
- 0 ≤ n ≤ 10⁵

**Hints**:
- dp[i] = dp[i >> 1] + (i & 1)
- Or: dp[i] = dp[i & (i-1)] + 1

---

### Problem 8: Pascal's Triangle

**Difficulty**: Easy
**Pattern**: 2D DP (Generation)

Generate the first `numRows` of Pascal's triangle. Each number is the sum of the two numbers directly above it.

**Example**:
```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**Constraints**:
- 1 ≤ numRows ≤ 30

**Hints**:
- row[i][j] = row[i-1][j-1] + row[i-1][j]
- Handle boundary elements (always 1)

---

## Medium Problems

### Problem 9: House Robber

**Difficulty**: Medium
**Pattern**: 1D DP

You are a robber planning to rob houses along a street. Each house has a certain amount of money. Adjacent houses have security systems connected. Cannot rob adjacent houses.

**Example**:
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and house 3 (money = 3).
```

**Constraints**:
- 1 ≤ nums.length ≤ 100
- 0 ≤ nums[i] ≤ 400

**Hints**:
- dp[i] = max money robbing first i houses
- dp[i] = max(dp[i-1], dp[i-2] + nums[i])

---

### Problem 10: House Robber II

**Difficulty**: Medium
**Pattern**: 1D DP with Constraint

Same as House Robber, but houses are arranged in a circle. First and last houses are adjacent.

**Example**:
```
Input: nums = [2,3,2]
Output: 3
Explanation: Cannot rob house 1 and house 3 together.
```

**Constraints**:
- 1 ≤ nums.length ≤ 100
- 0 ≤ nums[i] ≤ 1000

**Hints**:
- Cannot rob both first and last house
- Solve twice: rob houses [0...n-2] and [1...n-1]
- Return max of two results

---

### Problem 11: Coin Change

**Difficulty**: Medium
**Pattern**: Unbounded Knapsack

Given coins of different denominations and total amount, find the fewest number of coins to make up that amount. Return -1 if impossible.

**Example**:
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Constraints**:
- 1 ≤ coins.length ≤ 12
- 1 ≤ coins[i] ≤ 2³¹ - 1
- 0 ≤ amount ≤ 10⁴

**Hints**:
- dp[i] = minimum coins to make amount i
- dp[i] = min(dp[i-coin] + 1) for all coins
- Initialize with infinity except dp[0] = 0

---

### Problem 12: Coin Change 2

**Difficulty**: Medium
**Pattern**: Unbounded Knapsack

Given coins and amount, compute number of combinations that make up that amount.

**Example**:
```
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1
```

**Constraints**:
- 1 ≤ coins.length ≤ 300
- 1 ≤ coins[i] ≤ 5000
- 0 ≤ amount ≤ 5000

**Hints**:
- dp[i] = number of ways to make amount i
- Order matters: iterate coins in outer loop
- dp[i] += dp[i-coin]

---

### Problem 13: Longest Increasing Subsequence

**Difficulty**: Medium
**Pattern**: Sequence DP

Find the length of the longest strictly increasing subsequence.

**Example**:
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: LIS is [2,3,7,101] (or [2,3,7,18])
```

**Constraints**:
- 1 ≤ nums.length ≤ 2500
- -10⁴ ≤ nums[i] ≤ 10⁴

**Hints**:
- O(n²): dp[i] = LIS length ending at i
- O(n log n): Use binary search with patience sorting

---

### Problem 14: Longest Common Subsequence

**Difficulty**: Medium
**Pattern**: 2D DP, Two Sequences

Find the length of longest common subsequence of two strings.

**Example**:
```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: LCS is "ace"
```

**Constraints**:
- 1 ≤ text1.length, text2.length ≤ 1000

**Hints**:
- dp[i][j] = LCS for text1[:i] and text2[:j]
- If text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
- Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

---

### Problem 15: Unique Paths

**Difficulty**: Medium
**Pattern**: 2D Grid DP

Robot in m×n grid, starts at top-left, wants to reach bottom-right. Can only move right or down. Count unique paths.

**Example**:
```
Input: m = 3, n = 7
Output: 28
```

**Constraints**:
- 1 ≤ m, n ≤ 100

**Hints**:
- dp[i][j] = dp[i-1][j] + dp[i][j-1]
- Base cases: dp[0][j] = 1, dp[i][0] = 1
- Space optimization: O(n) array

---

### Problem 16: Unique Paths II

**Difficulty**: Medium
**Pattern**: 2D Grid DP with Obstacles

Same as Unique Paths, but grid has obstacles (marked as 1).

**Example**:
```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: One obstacle in the middle.
```

**Constraints**:
- m, n ≤ 100

**Hints**:
- If obstacle at (i,j): dp[i][j] = 0
- Check first row/column carefully

---

### Problem 17: Minimum Path Sum

**Difficulty**: Medium
**Pattern**: 2D Grid DP

Find path from top-left to bottom-right minimizing sum of numbers along the path.

**Example**:
```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Path 1→3→1→1→1
```

**Constraints**:
- m, n ≤ 200

**Hints**:
- dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
- Can modify grid in place

---

### Problem 18: Triangle

**Difficulty**: Medium
**Pattern**: 2D DP, Top-Down Path

Given triangle array, find minimum path sum from top to bottom. Each step can move to adjacent numbers.

**Example**:
```
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: 2→3→5→1
```

**Constraints**:
- 1 ≤ triangle.length ≤ 200

**Hints**:
- Work bottom-up: dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
- Space optimization: O(n)

---

### Problem 19: Partition Equal Subset Sum

**Difficulty**: Medium
**Pattern**: 0/1 Knapsack, Subset Sum

Can you partition array into two subsets with equal sum?

**Example**:
```
Input: nums = [1,5,11,5]
Output: true
Explanation: [1,5,5] and [11]
```

**Constraints**:
- 1 ≤ nums.length ≤ 200
- 1 ≤ nums[i] ≤ 100

**Hints**:
- If total sum is odd, return false
- Find subset with sum = total/2
- This is subset sum problem

---

### Problem 20: Target Sum

**Difficulty**: Medium
**Pattern**: 0/1 Knapsack, Subset Sum

Assign + or - before each number to reach target. Count ways.

**Example**:
```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: -1+1+1+1+1, 1-1+1+1+1, 1+1-1+1+1, 1+1+1-1+1, 1+1+1+1-1
```

**Constraints**:
- 1 ≤ nums.length ≤ 20
- 0 ≤ nums[i] ≤ 1000
- -1000 ≤ target ≤ 1000

**Hints**:
- Partition into positive (P) and negative (N)
- sum(P) - sum(N) = target
- sum(P) = (target + sum(nums)) / 2

---

## Hard Problems

### Problem 21: Edit Distance

**Difficulty**: Hard
**Pattern**: 2D DP, String Edit

Minimum operations (insert, delete, replace) to convert word1 to word2.

**Example**:
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: horse → rorse → rose → ros
```

**Constraints**:
- 0 ≤ word1.length, word2.length ≤ 500

**Hints**:
- dp[i][j] = min edits for word1[:i] → word2[:j]
- Three operations: insert, delete, replace
- If chars match: no operation needed

---

### Problem 22: Longest Palindromic Subsequence

**Difficulty**: Hard
**Pattern**: Interval DP, Palindrome

Find length of longest palindromic subsequence.

**Example**:
```
Input: s = "bbbab"
Output: 4
Explanation: "bbbb"
```

**Constraints**:
- 1 ≤ s.length ≤ 1000

**Hints**:
- dp[i][j] = LPS length in s[i:j+1]
- If s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
- Iterate by increasing substring length

---

### Problem 23: Regular Expression Matching

**Difficulty**: Hard
**Pattern**: 2D DP, String Matching

Implement regex with '.' (matches any char) and '*' (matches 0+ of previous element).

**Example**:
```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more 'a'
```

**Constraints**:
- 1 ≤ s.length ≤ 20
- 1 ≤ p.length ≤ 30

**Hints**:
- dp[i][j] = does s[:i] match p[:j]?
- Handle '*' carefully: can match 0 or more
- If p[j-1] is '*': dp[i][j] = dp[i][j-2] or (match and dp[i-1][j])

---

### Problem 24: Burst Balloons

**Difficulty**: Hard
**Pattern**: Interval DP

Burst balloons to maximize coins. Bursting balloon i gives `nums[left]*nums[i]*nums[right]` coins.

**Example**:
```
Input: nums = [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
             coins = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167
```

**Constraints**:
- n ≤ 500
- 0 ≤ nums[i] ≤ 100

**Hints**:
- Think about which balloon to burst LAST
- Add 1s to boundaries
- dp[i][j] = max coins for range (i,j)

---

### Problem 25: Maximum Profit in Job Scheduling

**Difficulty**: Hard
**Pattern**: DP with Binary Search, Interval Scheduling

Given jobs with start time, end time, and profit. Jobs don't overlap. Maximize profit.

**Example**:
```
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: Jobs 1 and 4 (profit = 50 + 70 = 120)
```

**Constraints**:
- 1 ≤ n ≤ 5×10⁴
- 1 ≤ startTime[i] < endTime[i] ≤ 10⁹
- 1 ≤ profit[i] ≤ 10⁴

**Hints**:
- Sort jobs by end time
- dp[i] = max profit considering first i jobs
- Use binary search to find latest non-overlapping job

---

## Problem Categories

### By Pattern

**1D Linear DP**:
- Problems 1, 2, 3, 4, 9, 10

**2D Grid DP**:
- Problems 8, 15, 16, 17, 18

**2D Two-Sequence DP**:
- Problems 5, 14, 21, 23

**Knapsack Variants**:
- Problems 11, 12, 19, 20

**Sequence DP**:
- Problems 13, 22

**Interval DP**:
- Problems 22, 24

**DP with Binary Search**:
- Problem 25

**Bit DP**:
- Problem 7

### By Difficulty Distribution

- **Easy (1-8)**: 8 problems - Master fundamentals
- **Medium (9-20)**: 12 problems - Core interview questions
- **Hard (21-25)**: 5 problems - Advanced techniques

### Recommended Order

**Week 1: Easy Problems**
- Day 1: Problems 1, 2, 3
- Day 2: Problems 4, 5
- Day 3: Problems 6, 7, 8

**Week 2: Medium - Linear DP**
- Day 1: Problems 9, 10
- Day 2: Problems 11, 12
- Day 3: Problem 13

**Week 3: Medium - 2D DP**
- Day 1: Problems 14, 15
- Day 2: Problems 16, 17
- Day 3: Problem 18

**Week 4: Medium - Knapsack**
- Day 1: Problems 19, 20
- Day 2: Review and optimize

**Week 5-6: Hard Problems**
- Problems 21-25 (one per day, with thorough understanding)

---

## Practice Tips

1. **Start Simple**: Always implement brute force recursion first
2. **Add Memoization**: Convert to top-down DP
3. **Build Table**: Try bottom-up tabulation
4. **Optimize Space**: Reduce space complexity
5. **Verify**: Test with examples and edge cases

## Common Mistakes to Avoid

1. ❌ Not handling base cases properly
2. ❌ Off-by-one errors in array indices
3. ❌ Not considering empty input
4. ❌ Iterating in wrong order (tabulation)
5. ❌ Using wrong initial values for DP table

## Next Steps

After completing these exercises:
1. Review [Solutions](./solutions.md) for each problem
2. Study [Tips](./tips.md) for optimization techniques
3. Practice 80+ LeetCode problems in tips.md
4. Focus on recognizing patterns quickly

---

**Remember**: The goal isn't to memorize solutions, but to recognize patterns and build problem-solving intuition. Take your time with each problem and understand the state transitions thoroughly.

Good luck with your practice!
