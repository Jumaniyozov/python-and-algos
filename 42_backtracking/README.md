# Chapter 42: Backtracking

## Overview

Backtracking is a systematic way to explore all possible solutions by building candidates incrementally and abandoning them ("backtracking") when they fail to satisfy constraints. It's essential for permutations, combinations, subsets, and constraint satisfaction problems.

## Learning Objectives

1. Understand backtracking template and when to use it
2. Implement permutations, combinations, and subsets
3. Solve constraint satisfaction problems (N-Queens, Sudoku)
4. Apply pruning to optimize backtracking
5. Recognize backtracking patterns in problems
6. Master recursion tree visualization
7. Combine backtracking with other techniques

## Chapter Structure

- **theory.md** - Backtracking fundamentals, template, when to use
- **examples.md** - Classic backtracking problems with detailed walkthroughs
- **exercises.md** - 15-20 practice problems
- **solutions.md** - Complete solutions with complexity analysis
- **tips.md** - Tips, tricks, and 50+ LeetCode problems

## Prerequisites

- Recursion (Chapter 5)
- Arrays and Strings (Chapter 29)
- Complexity Analysis (Chapter 27)
- Tree DFS (Chapter 33)

## Key Concepts

### Backtracking Fundamentals

- **Incremental Building**: Build solution step by step
- **Constraint Checking**: Validate at each step
- **Backtracking**: Undo choice and try next option
- **Pruning**: Skip branches that can't lead to solution

### Classic Patterns

**1. Permutations**: All arrangements of elements
**2. Combinations**: All k-element subsets
**3. Subsets**: All possible subsets (power set)
**4. Partition**: Split into valid groups
**5. Constraint Satisfaction**: N-Queens, Sudoku, etc.

## Time Complexity Summary

| Problem | Time Complexity | Notes |
|---------|----------------|-------|
| Permutations | O(n! × n) | n! permutations, O(n) to copy each |
| Combinations | O(C(n,k) × k) | C(n,k) combinations |
| Subsets | O(2ⁿ × n) | 2ⁿ subsets |
| N-Queens | O(n!) | With pruning |
| Sudoku | O(9^m) | m = empty cells |

## Navigation

- **Previous**: [Chapter 41: Greedy](../41_greedy/README.md)
- **Next**: [Chapter 43: Bit Manipulation](../43_bit_manipulation/README.md)
- **Home**: [Main README](../README.md)

---

## Quick Reference

### Backtracking Template

```python
def backtrack(path, choices):
    if is_valid_solution(path):
        result.append(path.copy())
        return

    for choice in choices:
        # Make choice
        path.append(choice)

        # Recurse
        backtrack(path, next_choices)

        # Undo choice (backtrack)
        path.pop()
```

### Common Patterns

**Permutations Template**:
```python
def permute(nums):
    result = []
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]],
                     remaining[:i] + remaining[i+1:])
    backtrack([], nums)
    return result
```

**Combinations Template**:
```python
def combine(n, k):
    result = []
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            backtrack(i + 1, path + [i])
    backtrack(1, [])
    return result
```

**Subsets Template**:
```python
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])
    backtrack(0, [])
    return result
```

## Study Time

- Theory: 3-4 hours
- Examples: 5-6 hours
- Exercises: 10-12 hours
- LeetCode (50+ problems): 50-70 hours

**Total**: 68-92 hours for mastery

Happy learning! Backtracking unlocks a whole class of problems!
