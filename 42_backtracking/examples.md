# Chapter 42: Backtracking - Examples

## Permutations and Combinations

### Example 1: Permutations (LeetCode 46)
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

### Example 2: Combinations (LeetCode 77)
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

### Example 3: Subsets (LeetCode 78)
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

---

## Constraint Satisfaction

### Example 4: N-Queens (LeetCode 51)
```python
def solve_n_queens(n):
    result = []
    board = [['.'] * n for _ in range(n)]

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1; j -= 1
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1; j += 1
        return True

    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)
    return result
```

### Example 5: Word Search (LeetCode 79)
```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(row, col, index):
        if index == len(word):
            return True
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        if board[row][col] != word[index]:
            return False

        temp = board[row][col]
        board[row][col] = '#'  # Mark visited

        found = (backtrack(row+1, col, index+1) or
                backtrack(row-1, col, index+1) or
                backtrack(row, col+1, index+1) or
                backtrack(row, col-1, index+1))

        board[row][col] = temp  # Unmark
        return found

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    return False
```

---

## String Backtracking

### Example 6: Letter Combinations (LeetCode 17)
```python
def letter_combinations(digits):
    if not digits:
        return []

    phone = {'2':'abc','3':'def','4':'ghi','5':'jkl',
             '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    result = []

    def backtrack(index, path):
        if index == len(digits):
            result.append(path)
            return
        for letter in phone[digits[index]]:
            backtrack(index + 1, path + letter)

    backtrack(0, '')
    return result
```

### Example 7: Palindrome Partitioning (LeetCode 131)
```python
def partition(s):
    result = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                backtrack(end, path + [substring])

    backtrack(0, [])
    return result
```

---

## Advanced Backtracking

### Example 8: Combination Sum (LeetCode 39)
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
            backtrack(i, path + [candidates[i]],
                     total + candidates[i])

    backtrack(0, [], 0)
    return result
```

### Example 9: Generate Parentheses (LeetCode 22)
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

---

Practice these patterns until backtracking becomes intuitive!
