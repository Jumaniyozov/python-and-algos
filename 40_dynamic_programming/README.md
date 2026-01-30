# Chapter 40: Dynamic Programming

## Overview

Dynamic Programming (DP) is one of the most powerful and important algorithm paradigms in computer science. It solves complex problems by breaking them down into simpler overlapping subproblems and storing their solutions to avoid redundant computation. DP is essential for technical interviews at top tech companies and appears in 20-30% of coding interviews.

## Learning Objectives

By the end of this chapter, you will be able to:

1. Understand the fundamental principles of dynamic programming
2. Identify when a problem can be solved using DP
3. Recognize overlapping subproblems and optimal substructure
4. Implement both memoization (top-down) and tabulation (bottom-up) approaches
5. Master common DP patterns (1D, 2D, knapsack, strings, sequences)
6. Optimize space complexity in DP solutions
7. Solve 80+ LeetCode DP problems efficiently
8. Recognize DP patterns in interview settings

## Chapter Structure

- **theory.md** - Comprehensive explanations of DP concepts and patterns
- **examples.md** - 20+ annotated DP examples with detailed state transitions
- **exercises.md** - 25 practice problems organized by pattern and difficulty
- **solutions.md** - Detailed solutions with both memoization and tabulation approaches
- **tips.md** - Tips, tricks, common pitfalls, and 80+ LeetCode DP problems

## Prerequisites

Before starting this chapter, you should be comfortable with:

- Recursion (Chapter 5)
- Complexity Analysis (Chapter 27)
- Problem-Solving Patterns (Chapter 28)
- Arrays and Strings (Chapter 29)
- Hash Tables (Chapter 32)

## Key Concepts

### DP Fundamentals
- Overlapping subproblems
- Optimal substructure
- State and state transitions
- Decision trees and recurrence relations

### DP Approaches
- **Memoization (Top-Down)**: Recursion + caching
- **Tabulation (Bottom-Up)**: Iterative table filling
- Space optimization techniques
- Choosing the right approach

### Common DP Patterns

#### 1. Linear DP (1D)
- Fibonacci sequence
- Climbing Stairs
- House Robber
- Decode Ways
- Jump Game

#### 2. Grid DP (2D)
- Unique Paths
- Minimum Path Sum
- Dungeon Game
- Edit Distance

#### 3. Sequence DP
- Longest Increasing Subsequence (LIS)
- Longest Common Subsequence (LCS)
- Longest Palindromic Subsequence
- Maximum Subarray (Kadane's Algorithm)

#### 4. Knapsack Problems
- 0/1 Knapsack
- Unbounded Knapsack
- Subset Sum
- Partition Equal Subset Sum
- Target Sum

#### 5. String DP
- Edit Distance
- Distinct Subsequences
- Word Break
- Palindrome problems
- Interleaving String

#### 6. State Machine DP
- Best Time to Buy and Sell Stock (all variants)
- Paint House
- State-based transitions

#### 7. Interval DP
- Burst Balloons
- Minimum Cost Tree From Leaf Values
- Matrix Chain Multiplication

## Time Complexity Summary

| Pattern | Typical Time | Typical Space | Example Problem |
|---------|--------------|---------------|-----------------|
| 1D DP | O(n) | O(n) → O(1) | Climbing Stairs |
| 2D DP | O(n*m) | O(n*m) → O(m) | Unique Paths |
| Knapsack | O(n*W) | O(W) | 0/1 Knapsack |
| LCS | O(n*m) | O(n*m) → O(min(n,m)) | Edit Distance |
| LIS | O(n²) or O(n log n) | O(n) | Longest Increasing Subsequence |

## Real-World Applications

- **Optimization Problems**: Resource allocation, scheduling
- **Bioinformatics**: DNA sequence alignment, protein folding
- **Finance**: Portfolio optimization, option pricing
- **Natural Language Processing**: Text comparison, spell checking
- **Computer Graphics**: Image processing, compression algorithms
- **Operations Research**: Inventory management, supply chain

## Study Approach

1. **Master the Theory** (3-4 hours)
   - Understand overlapping subproblems and optimal substructure
   - Learn to identify DP problems
   - Study memoization vs tabulation

2. **Learn Pattern by Pattern** (12-15 hours)
   - Start with 1D DP (Fibonacci, Climbing Stairs)
   - Progress to 2D DP (Grid problems)
   - Master Knapsack patterns
   - Study sequence and string DP
   - Practice state machine DP

3. **Practice Examples** (8-10 hours)
   - Implement both memoization and tabulation
   - Practice space optimization
   - Understand state transitions

4. **Solve Exercises** (15-20 hours)
   - Work through problems by pattern
   - Focus on state definition
   - Practice identifying DP opportunities

5. **LeetCode Marathon** (60-80 hours)
   - Work through 80+ curated problems in tips.md
   - Follow the structured learning path
   - Review patterns regularly

6. **Review and Consolidate** (5-7 hours)
   - Review common pitfalls
   - Practice pattern recognition
   - Time yourself on medium problems

## Estimated Study Time

- Theory and concepts: 3-4 hours
- Examples and implementation: 8-10 hours
- Exercises: 15-20 hours
- LeetCode practice (80+ problems in tips.md): 60-80 hours

**Total**: 90-120 hours for mastery

**Note**: Dynamic Programming is the most time-intensive chapter but also the most valuable for interviews. Companies like Google, Facebook, Amazon, and Microsoft heavily test DP skills.

## Navigation

- **Previous**: [Chapter 39: Searching](../39_searching/README.md)
- **Next**: [Chapter 41: Greedy Algorithms](../41_greedy/README.md)
- **Home**: [Main README](../README.md)

---

## Quick Reference

### DP Problem Checklist

Ask yourself these questions to identify DP problems:

1. **Can the problem be broken into subproblems?**
   - Are subproblems overlapping?
   - Can solutions to subproblems be combined?

2. **Does the problem ask for optimization?**
   - Maximum/minimum value?
   - Count of ways?
   - Yes/no possibility?

3. **Can you define a recurrence relation?**
   - What's the base case?
   - What's the recursive case?

4. **Is there optimal substructure?**
   - Does optimal solution contain optimal solutions to subproblems?

### DP Implementation Template

```python
# Memoization (Top-Down)
def dp_memoization(n):
    memo = {}

    def helper(state):
        # Base case
        if base_condition:
            return base_value

        # Check cache
        if state in memo:
            return memo[state]

        # Compute result
        result = # ... recursive calls to helper

        # Store and return
        memo[state] = result
        return result

    return helper(n)

# Tabulation (Bottom-Up)
def dp_tabulation(n):
    # Initialize DP table
    dp = [0] * (n + 1)

    # Base case
    dp[0] = base_value

    # Fill table
    for i in range(1, n + 1):
        dp[i] = # ... use previous dp values

    return dp[n]
```

### Common State Definitions

| Problem Type | State | Example |
|--------------|-------|---------|
| 1D Sequence | `dp[i]` = answer for first i elements | Climbing Stairs |
| 2D Grid | `dp[i][j]` = answer for cell (i,j) | Unique Paths |
| Two Sequences | `dp[i][j]` = answer for seq1[:i] and seq2[:j] | Edit Distance |
| Knapsack | `dp[i][w]` = max value with first i items, weight w | 0/1 Knapsack |
| Interval | `dp[i][j]` = answer for range [i,j] | Burst Balloons |

## Why DP is Critical for Interviews

1. **High Frequency**: 20-30% of medium/hard interview problems
2. **Differentiator**: Separates strong candidates from average ones
3. **Tests Multiple Skills**: Problem-solving, recursion, optimization
4. **Scalable Thinking**: Shows ability to optimize brute force solutions
5. **Pattern Recognition**: Demonstrates systematic approach to problems

## Study Schedule Recommendation

### Week 1-2: Foundations
- Study theory and fundamentals
- Master Fibonacci, Climbing Stairs, House Robber
- Practice memoization vs tabulation
- Complete first 20 LeetCode problems

### Week 3-4: Core Patterns
- 2D DP and Grid problems
- Knapsack variants
- Complete 30 more LeetCode problems

### Week 5-6: Advanced Patterns
- Sequence DP (LIS, LCS)
- String DP
- State machine DP
- Complete 30 more LeetCode problems

### Week 7-8: Mastery
- Interval DP
- Mixed pattern problems
- Timed practice
- Review and consolidate

---

## Additional Resources

- [LeetCode DP Problems](https://leetcode.com/tag/dynamic-programming/)
- [DP Patterns for Coding Interviews](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)
- [Visualgo DP Visualization](https://visualgo.net/en/recursion)
- [MIT OpenCourseWare: Dynamic Programming](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/)

---

**Important**: Dynamic Programming is challenging but incredibly rewarding. Don't get discouraged if problems seem difficult at first. With consistent practice following the patterns in this chapter, you'll develop strong DP intuition. The 80+ LeetCode problems in tips.md are carefully curated to build your skills systematically.

Good luck, and happy optimizing!
