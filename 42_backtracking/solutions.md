# Chapter 42: Backtracking - Solutions

## Easy Problems

### E1: Subsets
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
**Time**: O(2ⁿ × n), **Space**: O(n)

### E2: Permutations
```python
def permute(nums):
    result = []
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
    backtrack([], nums)
    return result
```
**Time**: O(n! × n), **Space**: O(n)

### E3: Combinations
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
**Time**: O(C(n,k) × k), **Space**: O(k)

---

## Medium Problems

### M2: Subsets II
```python
def subsets_with_dup(nums):
    nums.sort()
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            backtrack(i + 1, path + [nums[i]])
    backtrack(0, [])
    return result
```
**Time**: O(2ⁿ × n), **Space**: O(n)

### M3: Combination Sum
```python
def combination_sum(candidates, target):
    result = []
    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            backtrack(i, path + [candidates[i]], total + candidates[i])
    backtrack(0, [], 0)
    return result
```
**Time**: O(2^target), **Space**: O(target)

### M5: Generate Parentheses
```python
def generate_parenthesis(n):
    result = []
    def backtrack(path, open_count, close_count):
        if len(path) == 2 * n:
            result.append(path)
            return
        if open_count < n:
            backtrack(path + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(path + ')', open_count, close_count + 1)
    backtrack('', 0, 0)
    return result
```
**Time**: O(4ⁿ / √n), **Space**: O(n)

---

## Hard Problems

### H1: N-Queens
```python
def solve_n_queens(n):
    result = []
    board = [['.'] * n for _ in range(n)]
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board[row][col] = 'Q'

            backtrack(row + 1)

            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return result
```
**Time**: O(n!), **Space**: O(n²)

### H2: Sudoku Solver
```python
def solve_sudoku(board):
    def is_valid(row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
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
                            board[i][j] = '.'
                    return False
        return True

    backtrack()
```
**Time**: O(9^m) where m = empty cells, **Space**: O(1)

---

Master these solutions - they're essential backtracking patterns!
