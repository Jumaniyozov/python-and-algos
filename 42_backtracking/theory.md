# Chapter 42: Backtracking - Theory

## Table of Contents
1. [Introduction](#introduction)
2. [Backtracking Template](#backtracking-template)
3. [Permutations](#permutations)
4. [Combinations](#combinations)
5. [Subsets](#subsets)
6. [Constraint Satisfaction](#constraint-satisfaction)
7. [Pruning Techniques](#pruning-techniques)

---

## Introduction

**Backtracking** systematically explores all possible solutions by:
1. **Making a choice**
2. **Recursing** on remaining problem
3. **Undoing the choice** (backtracking)
4. **Trying next choice**

### When to Use Backtracking

✅ Use backtracking for:
- Generating all permutations/combinations/subsets
- Constraint satisfaction (N-Queens, Sudoku)
- Path finding with constraints
- Partition problems
- Word search, phone number combinations

---

## Backtracking Template

```python
def backtrack(path, choices):
    """
    Generic backtracking template.

    Args:
        path: Current partial solution
        choices: Remaining choices available
    """
    # Base case: valid complete solution
    if is_valid_solution(path):
        result.append(path.copy())  # Make copy!
        return

    # Try each choice
    for choice in get_choices(choices):
        # Skip invalid choices (pruning)
        if not is_valid(choice, path):
            continue

        # Make choice
        path.append(choice)

        # Recurse with updated choices
        backtrack(path, get_next_choices(choice, choices))

        # Undo choice (backtrack)
        path.pop()
```

---

## Permutations

**Problem**: Generate all arrangements of n elements.

### Approach

**Time**: O(n! × n) - n! permutations, O(n) to copy each
**Space**: O(n) - recursion depth

```python
def permute(nums):
    """
    All permutations of nums.

    Example: [1,2,3] → [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    """
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return

        for i in range(len(remaining)):
            backtrack(
                path + [remaining[i]],
                remaining[:i] + remaining[i+1:]
            )

    backtrack([], nums)
    return result
```

### Alternative: In-place with Used Array

```python
def permute_used(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            # Choose
            path.append(nums[i])
            used[i] = True

            # Recurse
            backtrack(path)

            # Unchoose
            path.pop()
            used[i] = False

    backtrack([])
    return result
```

---

## Combinations

**Problem**: Generate all k-element subsets.

### Approach

**Time**: O(C(n,k) × k) - C(n,k) combinations
**Space**: O(k) - recursion depth

```python
def combine(n, k):
    """
    All combinations of k numbers from 1..n.

    Example: n=4, k=2 → [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    """
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

### Key Insight

Use `start` index to avoid duplicates and maintain order.

---

## Subsets

**Problem**: Generate all possible subsets (power set).

### Approach

**Time**: O(2ⁿ × n) - 2ⁿ subsets
**Space**: O(n) - recursion depth

```python
def subsets(nums):
    """
    All subsets of nums.

    Example: [1,2,3] → [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    """
    result = []

    def backtrack(start, path):
        result.append(path[:])  # Every state is valid

        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return result
```

### Bit Manipulation Alternative

```python
def subsets_bits(nums):
    n = len(nums)
    result = []

    for mask in range(1 << n):  # 2^n possibilities
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)

    return result
```

---

## Constraint Satisfaction

### N-Queens Problem

**Problem**: Place n queens on n×n board with no attacks.

```python
def solve_n_queens(n):
    """
    Find all solutions to n-queens.

    Time: O(n!)
    Space: O(n^2)
    """
    result = []
    board = [['.'] * n for _ in range(n)]

    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check diagonal \
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check diagonal /
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            result.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)
    return result
```

### Sudoku Solver

```python
def solve_sudoku(board):
    """
    Solve Sudoku puzzle in-place.

    Time: O(9^m) where m = empty cells
    Space: O(1)
    """
    def is_valid(row, col, num):
        # Check row
        if num in board[row]:
            return False

        # Check column
        if num in [board[i][col] for i in range(9)]:
            return False

        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if is_valid(i, j, num):
                            board[i][j] = num

                            if backtrack():
                                return True

                            board[i][j] = '.'  # Backtrack

                    return False  # No valid number found

        return True  # All cells filled

    backtrack()
```

---

## Pruning Techniques

### 1. Early Termination

```python
def backtrack(path, remaining):
    # Prune: impossible to reach solution
    if len(path) + len(remaining) < target_length:
        return

    if is_solution(path):
        result.append(path[:])
        return

    for choice in remaining:
        backtrack(path + [choice], next_remaining)
```

### 2. Duplicate Avoidance

```python
def subsets_with_dup(nums):
    nums.sort()  # Sort first
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i-1]:
                continue

            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return result
```

### 3. Constraint Checking

```python
def backtrack(path):
    # Check constraints before recursing
    if not satisfies_constraints(path):
        return  # Prune this branch

    if is_complete(path):
        result.append(path[:])
        return

    for choice in get_choices():
        backtrack(path + [choice])
```

---

## Summary

**Backtracking Patterns:**

1. **Permutations**: Try each element, mark as used
2. **Combinations**: Use start index to maintain order
3. **Subsets**: Every state is valid, collect all
4. **Constraint Satisfaction**: Check validity before recursing

**Key Techniques:**

- Copy result before adding (`.copy()` or `[:]`)
- Use start index to avoid duplicates
- Sort first when dealing with duplicates
- Prune invalid branches early
- Visualize recursion tree

**Complexity:**
- Usually exponential: O(2ⁿ), O(n!), O(kⁿ)
- Space: O(depth of recursion)

Master the template and patterns - they apply to many problems!
