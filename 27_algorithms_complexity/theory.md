# Algorithms and Complexity Analysis - Theory

## Table of Contents

1. [Introduction to Algorithm Design](#introduction-to-algorithm-design)
2. [Mathematical Induction](#mathematical-induction)
3. [Algorithm Design Strategies](#algorithm-design-strategies)
4. [Problem-Solving Framework](#problem-solving-framework)
5. [Big O Notation](#big-o-notation)
6. [Time Complexity](#time-complexity)
7. [Space Complexity](#space-complexity)
8. [Best, Average, Worst Case](#best-average-worst-case)
9. [Common Complexities](#common-complexities)
10. [Amortized Analysis](#amortized-analysis)
11. [Complexity Comparison](#complexity-comparison)

---

## Introduction to Algorithm Design

### What is an Algorithm?

An algorithm is a step-by-step procedure for solving a problem or performing a computation. It's a finite sequence of well-defined instructions that transforms input into output.

```
Algorithm = Input → Process → Output

Example: Making a sandwich
Input: Bread, peanut butter, jelly
Process: 1. Take two slices of bread
         2. Spread peanut butter on one slice
         3. Spread jelly on the other slice
         4. Put slices together
Output: Sandwich
```

### Properties of Good Algorithms

A good algorithm must have these essential properties:

#### 1. Correctness

The algorithm produces the correct output for all valid inputs.

```python
# Correct algorithm to find maximum
def find_max(arr):
    """Always returns the maximum element."""
    if not arr:
        raise ValueError("Empty array")
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Incorrect algorithm (fails for negative numbers)
def find_max_wrong(arr):
    """Bug: Assumes all numbers are positive."""
    max_val = 0  # Wrong initialization!
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

print(find_max_wrong([-5, -2, -10]))  # Returns 0, should return -2
```

#### 2. Efficiency

The algorithm uses minimal time and space resources.

```python
# Efficient: O(n)
def sum_array_efficient(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Inefficient: O(n²)
def sum_array_inefficient(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(i + 1):  # Unnecessary nested loop!
            if i == j:
                total += arr[i]
    return total

# Both produce same result, but first is much faster
```

#### 3. Clarity

The algorithm is easy to understand and implement.

```python
# Clear algorithm
def is_palindrome_clear(s):
    """Check if string reads same forwards and backwards."""
    return s == s[::-1]

# Unclear algorithm (same logic, harder to understand)
def is_palindrome_unclear(s):
    """Same as above but unnecessarily complex."""
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
```

#### 4. Finiteness

The algorithm must terminate after a finite number of steps.

```python
# Finite: Always terminates
def countdown(n):
    while n > 0:
        print(n)
        n -= 1  # Guaranteed to reach 0
    print("Done!")

# Infinite: Never terminates (BUG!)
def countdown_infinite(n):
    while n > 0:
        print(n)
        # Forgot to decrement n!
    print("Never printed")
```

#### 5. Generality

The algorithm works for a class of problems, not just one specific instance.

```python
# General: Works for any array size
def find_min(arr):
    if not arr:
        raise ValueError("Empty array")
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

# Not general: Only works for array of size 3
def find_min_of_three(a, b, c):
    if a < b and a < c:
        return a
    elif b < c:
        return b
    else:
        return c
```

### Algorithm Design Process

Follow these steps when designing algorithms:

```
1. Understand the Problem
   - What are the inputs?
   - What are the outputs?
   - What are the constraints?
   - What are edge cases?

2. Design the Algorithm
   - Choose appropriate strategy
   - Write pseudocode
   - Consider tradeoffs

3. Analyze the Algorithm
   - Prove correctness
   - Calculate time complexity
   - Calculate space complexity

4. Implement the Algorithm
   - Write clean, clear code
   - Add comments and documentation
   - Handle edge cases

5. Test the Algorithm
   - Test with small inputs
   - Test edge cases
   - Test with large inputs
   - Verify correctness

6. Optimize if Needed
   - Profile for bottlenecks
   - Improve time/space complexity
   - Consider alternative approaches
```

---

## Mathematical Induction

### Principle of Induction

Mathematical induction is a powerful proof technique for establishing the correctness of algorithms, especially those involving loops or recursion.

**Analogy**: Dominoes falling
- If the first domino falls (base case)
- And each domino knocks over the next one (inductive step)
- Then all dominoes will fall (conclusion)

### Structure of Induction Proof

Every induction proof has two parts:

```
1. Base Case
   - Prove the statement is true for the smallest value (usually n=0 or n=1)

2. Inductive Step
   - Assume the statement is true for n=k (inductive hypothesis)
   - Prove the statement is true for n=k+1
   - If both steps succeed, the statement is true for all n
```

### Example 1: Sum of First n Natural Numbers

**Claim**: The sum of first n natural numbers is n(n+1)/2

```
Proof by Induction:

Base Case (n=1):
  Sum = 1
  Formula = 1(1+1)/2 = 1
  ✓ Base case holds

Inductive Hypothesis:
  Assume for n=k: 1 + 2 + ... + k = k(k+1)/2

Inductive Step (prove for n=k+1):
  1 + 2 + ... + k + (k+1)
  = [1 + 2 + ... + k] + (k+1)
  = k(k+1)/2 + (k+1)           [by hypothesis]
  = k(k+1)/2 + 2(k+1)/2
  = (k(k+1) + 2(k+1))/2
  = (k+1)(k+2)/2
  = (k+1)((k+1)+1)/2
  ✓ This matches the formula for n=k+1

Conclusion: Formula holds for all n ≥ 1
```

Python verification:

```python
def sum_formula(n):
    """Formula: n(n+1)/2"""
    return n * (n + 1) // 2

def sum_loop(n):
    """Direct summation"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Verify formula matches loop for various n
for n in [1, 10, 100, 1000]:
    assert sum_formula(n) == sum_loop(n)
    print(f"n={n}: {sum_formula(n)}")
```

### Example 2: Power of 2

**Claim**: For all n ≥ 0, 2^n ≥ n + 1

```
Proof by Induction:

Base Case (n=0):
  2^0 = 1
  n + 1 = 0 + 1 = 1
  1 ≥ 1 ✓

Inductive Hypothesis:
  Assume for n=k: 2^k ≥ k + 1

Inductive Step (prove for n=k+1):
  2^(k+1) = 2 × 2^k
          ≥ 2 × (k + 1)        [by hypothesis]
          = 2k + 2
          = (k + 1) + (k + 1)
          ≥ (k + 1) + 1        [since k ≥ 0]
          = k + 2
          = (k + 1) + 1
  ✓ Formula holds for k+1

Conclusion: 2^n ≥ n + 1 for all n ≥ 0
```

### Using Induction to Prove Algorithm Correctness

#### Example: Array Sum Algorithm

```python
def array_sum(arr):
    """Sum all elements in array."""
    total = 0
    for num in arr:
        total += num
    return total
```

**Claim**: This algorithm correctly computes the sum of all elements

**Proof using Loop Invariant**:

A loop invariant is a property that holds before and after each iteration.

```
Loop Invariant: After processing k elements,
                total = sum of first k elements

Initialization (k=0):
  - Before loop, total = 0
  - Sum of first 0 elements = 0
  - ✓ Invariant holds initially

Maintenance (assume true for k, prove for k+1):
  - Before iteration k+1: total = sum of first k elements
  - During iteration k+1: total += arr[k]
  - After iteration k+1: total = sum of first k+1 elements
  - ✓ Invariant maintained

Termination:
  - Loop ends when k = n (all elements processed)
  - By invariant: total = sum of first n elements
  - ✓ Algorithm is correct
```

#### Example: Binary Search Correctness

```python
def binary_search(arr, target):
    """Find target in sorted array."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

**Loop Invariant**: If target exists in arr, it's in range [left, right]

```
Initialization:
  - left = 0, right = len(arr) - 1
  - If target exists, it's somewhere in [0, len(arr)-1]
  - ✓ Invariant holds

Maintenance:
  - If arr[mid] < target: target must be in [mid+1, right]
  - If arr[mid] > target: target must be in [left, mid-1]
  - If arr[mid] == target: found it!
  - ✓ Invariant maintained

Termination:
  - Loop ends when left > right
  - If target existed, we would have found it
  - If not found, target doesn't exist
  - ✓ Algorithm is correct
```

### Strong Induction

Sometimes we need to assume the statement holds for all values up to k, not just k.

**Example: Fibonacci Correctness**

```python
def fib(n):
    """Calculate nth Fibonacci number."""
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

**Claim**: This correctly computes the nth Fibonacci number

```
Proof by Strong Induction:

Base Cases (n=0, n=1):
  - fib(0) = 0 ✓
  - fib(1) = 1 ✓

Inductive Hypothesis:
  - Assume fib(i) is correct for all i ≤ k

Inductive Step (prove for n=k+1):
  - fib(k+1) = fib(k) + fib(k-1)
  - By hypothesis, fib(k) and fib(k-1) are correct
  - Therefore fib(k+1) is correct
  - ✓ Correctness proven
```

---

## Algorithm Design Strategies

Understanding major algorithm design strategies helps you choose the right approach for a problem. These strategies are covered in depth in later chapters.

### 1. Brute Force

**Idea**: Try all possible solutions and pick the best one

```python
# Find pair that sums to target
def find_pair_brute_force(arr, target):
    """Time: O(n²), Space: O(1)"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None

# Advantages: Simple, always correct
# Disadvantages: Usually slow (exponential or polynomial time)
# When to use: Small inputs, no better solution exists
```

### 2. Divide and Conquer

**Idea**: Break problem into smaller subproblems, solve recursively, combine results

```python
# Merge sort example
def merge_sort(arr):
    """Time: O(n log n), Space: O(n)"""
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer (merge)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Pattern: Divide → Solve subproblems → Combine
# Examples: Binary search, merge sort, quick sort
# Time: Often O(n log n) or O(log n)
```

### 3. Greedy Algorithms

**Idea**: Make locally optimal choice at each step, hope for global optimum

```python
# Coin change (with standard US coins)
def coin_change_greedy(amount):
    """Time: O(1), Space: O(1)"""
    coins = [25, 10, 5, 1]  # Quarters, dimes, nickels, pennies
    result = []

    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin

    return result

# Works for US coins: coin_change_greedy(41) → [25, 10, 5, 1]
# Doesn't always work: Different coin systems may need different approach

# Advantages: Fast, simple
# Disadvantages: Doesn't always give optimal solution
# When to use: Problem has greedy-choice property
```

### 4. Dynamic Programming

**Idea**: Break into overlapping subproblems, store results to avoid recomputation

```python
# Fibonacci with memoization
def fib_dp(n, memo=None):
    """Time: O(n), Space: O(n)"""
    if memo is None:
        memo = {}

    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fib_dp(n-1, memo) + fib_dp(n-2, memo)
    return memo[n]

# Compare to naive recursion:
# fib(40) → Naive: ~1 second, DP: instant
# fib(100) → Naive: centuries, DP: instant

# Pattern: Optimal substructure + overlapping subproblems
# Examples: Fibonacci, longest common subsequence, knapsack
# Time: Often O(n²) or O(n×m)
```

### 5. Backtracking

**Idea**: Build solution incrementally, abandon paths that won't work

```python
# Generate all permutations
def permutations(arr):
    """Time: O(n!), Space: O(n)"""
    def backtrack(start):
        if start == len(arr):
            result.append(arr[:])
            return

        for i in range(start, len(arr)):
            # Choose
            arr[start], arr[i] = arr[i], arr[start]
            # Explore
            backtrack(start + 1)
            # Unchoose (backtrack)
            arr[start], arr[i] = arr[i], arr[start]

    result = []
    backtrack(0)
    return result

# Pattern: Choose → Explore → Unchoose
# Examples: N-Queens, Sudoku solver, subset sum
# Time: Often exponential, but prunes invalid paths
```

### Strategy Comparison

```
Strategy          Time          Space         When to Use
─────────────────────────────────────────────────────────────
Brute Force       High          Low           Small inputs
Divide/Conquer    O(n log n)    O(log n)      Divide naturally
Greedy            Low           Low           Greedy property
Dynamic Prog      O(n²)         O(n)          Overlapping subproblems
Backtracking      Exponential   O(n)          Constraint satisfaction
```

---

## Problem-Solving Framework

A systematic approach to solving algorithmic problems:

### Step 1: Understand the Problem

```
Ask yourself:
1. What is the input? (Type, size, constraints)
2. What is the output? (Type, format)
3. What are the edge cases? (Empty input, single element, duplicates)
4. Are there constraints? (Time limit, space limit)
5. Can I solve a simpler version first?

Example: "Find two numbers that sum to target"
- Input: Array of integers, target integer
- Output: Pair of numbers or indices
- Edge cases: Empty array, no solution, multiple solutions
- Constraints: Array sorted? Duplicates allowed?
```

### Step 2: Devise a Plan

```
Choose a strategy:
1. Brute force first (establish correctness)
2. Can I use a better strategy?
   - Does divide and conquer apply?
   - Is there a greedy approach?
   - Can I use dynamic programming?
   - Should I try backtracking?
3. What data structures help?
   - Hash table for O(1) lookup?
   - Heap for min/max?
   - Stack for LIFO?
   - Queue for BFS?

Example: Two sum problem
- Brute force: Check all pairs O(n²)
- Better: Use hash table O(n)
```

### Step 3: Execute the Plan

```
1. Write pseudocode first
2. Consider edge cases
3. Think about loop invariants
4. Write clean, documented code

Example pseudocode:
```
```
function twoSum(arr, target):
    create empty hash map
    for each number in arr:
        complement = target - number
        if complement in hash map:
            return [complement, number]
        add number to hash map
    return null
```
```

### Step 4: Review and Optimize

```
1. Does it work for all test cases?
2. What is the time complexity?
3. What is the space complexity?
4. Can I optimize further?
5. Is the code clear and maintainable?

Example analysis:
- Time: O(n) - single pass
- Space: O(n) - hash map
- Optimization: If sorted, could use two pointers for O(1) space
```

### Complete Example: Longest Substring Without Repeating Characters

```python
def longest_unique_substring(s):
    """
    Find length of longest substring without repeating characters.

    Example: "abcabcbb" → 3 (substring "abc")

    1. UNDERSTAND
       - Input: String
       - Output: Integer length
       - Edge: Empty string → 0, single char → 1

    2. PLAN
       - Sliding window with hash set
       - Expand window while unique
       - Shrink when duplicate found

    3. EXECUTE
    """
    max_length = 0
    left = 0
    char_set = set()

    for right in range(len(s)):
        # Shrink window while duplicate exists
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add current character
        char_set.add(s[right])

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length

# 4. REVIEW
# Time: O(n) - each character visited at most twice
# Space: O(min(n, m)) where m is character set size
# Correctness: Sliding window maintains invariant of unique characters

# Test
print(longest_unique_substring("abcabcbb"))  # 3
print(longest_unique_substring("bbbbb"))     # 1
print(longest_unique_substring("pwwkew"))    # 3
```

---

## Big O Notation

### What is Big O?

Big O notation describes how an algorithm's performance scales with input size. It answers: "As input size grows, how much slower does my code get?"

```
               Time
               ↑
               │     O(2ⁿ) - Exponential
               │    /
               │   /
               │  O(n²) - Quadratic
               │ /
               │O(n log n)
               │|
               │| O(n) - Linear
               │|
               │| O(log n)
               │|
               │_____ O(1) - Constant
               ├───────────────────────→ Input Size
               0                         n
```

### Formal Definition

Big O describes the upper bound of an algorithm's growth rate.

```
f(n) = O(g(n))

if there exist positive constants c and n₀ such that
f(n) ≤ c·g(n) for all n ≥ n₀
```

Example:
```
f(n) = 2n² + 3n + 5

f(n) is O(n²) because:
  For large n, 2n² dominates
  We can drop lower terms (3n + 5)
  We can drop constants (2)
```

### Why Ignore Constants and Lower Terms?

```
f(n) = n + 5

n = 10:   f(n) = 15
n = 100:  f(n) = 105
n = 1000: f(n) = 1005

Ratio: 105/15 ≈ 7 (small difference)

But for f(n) = n²:

n = 10:   f(n) = 100
n = 100:  f(n) = 10,000
n = 1000: f(n) = 1,000,000

Ratio: 10,000/100 = 100 (huge difference!)

Constants and lower terms become irrelevant as n grows.
```

---

## Time Complexity

### How to Analyze Time Complexity

#### Step 1: Count Operations

```python
def example1(n):
    x = 5              # 1 operation
    y = 10             # 1 operation
    print(x + y)       # 1 operation
    return x + y       # 1 operation

# Total: 4 operations (constant, independent of n)
# Time Complexity: O(1)
```

#### Step 2: Simple Loop

```python
def example2(n):
    for i in range(n):  # Runs n times
        print(i)        # 1 operation each time
    return

# Operations: n
# Time Complexity: O(n)
```

#### Step 3: Nested Loops

```python
def example3(n):
    for i in range(n):      # Runs n times
        for j in range(n):  # Runs n times for each i
            print(i, j)     # 1 operation each time

# Operations: n × n = n²
# Time Complexity: O(n²)
```

#### Step 4: Logarithmic

```python
def example4(n):
    while n > 1:        # Halves n each time
        print(n)        # 1 operation
        n = n // 2

# Operations: log₂(n)
# For n=1000: ~10 iterations
# Time Complexity: O(log n)
```

#### Step 5: Linear + Logarithmic

```python
def example5(n):
    for i in range(n):       # Runs n times
        j = n
        while j > 1:         # Runs log(n) times
            print(i, j)
            j = j // 2

# Operations: n × log(n)
# Time Complexity: O(n log n)
```

### Common Patterns

```
Pattern                                      Complexity
────────────────────────────────────────────────────────────
Simple statements                            O(1)
Single loop 0 to n                          O(n)
Nested loops 0 to n                         O(n²)
Triple nested loops                         O(n³)
Loop that halves n each time               O(log n)
Loop that multiplies n each time           O(log n)
For each item, binary search                O(n log n)
Dividing and conquering                     O(n log n)
Each pair of items                          O(n²)
Generating all subsets                      O(2ⁿ)
Generating all permutations                 O(n!)
```

### Example: Sequential vs Nested

```python
def sequential(n):
    for i in range(n):      # O(n)
        print(i)
    for j in range(n):      # O(n)
        print(j)
    return

# Total: O(n) + O(n) = O(2n) = O(n)
# Constants are dropped!

def nested(n):
    for i in range(n):      # O(n)
        for j in range(n):  # O(n) for each i
            print(i, j)
    return

# Total: O(n²)
```

---

## Space Complexity

### What is Space Complexity?

Space complexity measures how much memory an algorithm uses as a function of input size.

```python
def space_example1():
    x = 5              # O(1) - Fixed memory
    y = 10
    return x + y

# Space: O(1) - Constant space

def space_example2(n):
    lst = []
    for i in range(n):  # Add n items to list
        lst.append(i)
    return lst

# Space: O(n) - Linear space

def space_example3(n):
    matrix = []
    for i in range(n):              # O(n²) items
        row = []
        for j in range(n):
            row.append(i*j)
        matrix.append(row)
    return matrix

# Space: O(n²) - Quadratic space
```

### Time vs Space Tradeoff

Many algorithms trade space for time:

```python
# Time: O(n), Space: O(1)
def find_max_inplace(arr):
    max_val = arr[0]
    for item in arr:
        if item > max_val:
            max_val = item
    return max_val

# Time: O(n), Space: O(n)
# But faster if checking from cache
def find_max_cached(arr):
    # Create dictionary of max values
    seen = {}
    for item in arr:
        seen[item] = True
    return max(seen.keys())
```

---

## Best, Average, Worst Case

### Definitions

```
Worst Case:   Maximum time for any input of size n
Average Case: Expected time for random input
Best Case:    Minimum time for any input of size n
```

### Example: Linear Search

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Best Case:    O(1) - Target is first element
# Average Case: O(n) - Target is in middle
# Worst Case:   O(n) - Target not found or is last
```

### Example: Insertion

```python
def insert_into_sorted_list(arr, value):
    # Find position
    for i in range(len(arr)):
        if arr[i] > value:
            arr.insert(i, value)
            return

# Best Case:    O(1) - Insert at end
# Average Case: O(n) - Insert in middle (shift elements)
# Worst Case:   O(n) - Insert at beginning (shift all)
```

### Typically Report Worst Case

```
Why?
- Worst case is guaranteed performance
- Average case is often close to worst case
- Best case is rarely useful in practice
```

---

## Common Complexities

### O(1) - Constant

```python
# Dictionary lookup
value = my_dict['key']  # O(1)

# List access by index
item = my_list[5]  # O(1)

# Arithmetic operation
result = 5 + 3 * 2  # O(1)
```

### O(log n) - Logarithmic

```python
# Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Time: O(log n) - halves search space each time
```

### O(n) - Linear

```python
# Simple loop
total = 0
for item in items:
    total += item  # O(n)

# List operation
max_value = max(items)  # O(n)

# String search
found = 'target' in long_string  # O(n)
```

### O(n log n) - Linearithmic

```python
# Good sorting algorithms
sorted_list = sorted(items)  # Merge sort, O(n log n)

# Divide and conquer
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# O(log n) levels, O(n) merge per level
# Total: O(n log n)
```

### O(n²) - Quadratic

```python
# Nested loops
total = 0
for i in range(n):
    for j in range(n):
        total += i * j  # O(n²)

# Bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # O(n²)
```

### O(2ⁿ) - Exponential

```python
# Recursive without memoization
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Each call branches into 2 more calls
# Tree has 2ⁿ nodes
# Time: O(2ⁿ) - TERRIBLE for large n!

# fib(40) requires ~1 million calls
# fib(50) requires ~1 billion calls
```

### O(n!) - Factorial

```python
# Generate all permutations
def permutations(arr):
    if len(arr) <= 1:
        return [arr]

    result = []
    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[:i] + arr[i+1:]
        for perm in permutations(remaining):
            result.append([current] + perm)
    return result

# For n items: n! permutations
# 5 items: 120 permutations
# 10 items: 3,628,800 permutations
# 13 items: 6,227,020,800 permutations
# IMPOSSIBLY slow!
```

---

## Amortized Analysis

### What is Amortized Analysis?

Amortized analysis averages cost over a sequence of operations, even if individual operations vary in cost.

```
Example: Appending to Python list

First:           1 2 3 4 5 6 7 8 [10 slots]
Append "9":      1 2 3 4 5 6 7 8 9 [10 slots]
Append "10":     1 2 3 4 5 6 7 8 9 10 [10 slots]
Append "11":     Need to resize! [15 slots]
                 1 2 3 4 5 6 7 8 9 10 11 [15 slots]

Resize is O(n) but happens rarely.
Amortized: O(1) per append.
```

### Python List Append Analysis

```python
# Create list and append n items
lst = []
for i in range(n):
    lst.append(i)  # Sometimes O(n), usually O(1)

# Total time:
# - Most appends: O(1)
# - Few resizes: O(n) total across all resizes
# - Pattern: doubling strategy
#
# Total time for n appends: O(n)
# Amortized per append: O(n)/n = O(1)
```

### Dictionary Hashing

```python
# Similar strategy for dictionaries
# Occasional resize when load factor high
# Most operations: O(1)
# Amortized over many operations: O(1) on average
```

---

## Complexity Comparison

### Visual Comparison

```
     Time
      ↑
 10⁶ │                                        O(2ⁿ)
 10⁵ │                                      /
 10⁴ │                                    /
 10³ │                             O(n!)
 10² │                         /
 10¹ │                       O(n²)
 10⁰ │                    O(n log n)
     │                  /
     │               O(n)
     │            /
     │         /
     │    O(log n)
     │ /
     │ O(1)
     └─────────────────────────────────→
       1   10   100  1000  10000  n
```

### Growth Rate Table

```
n      O(1)  O(logn)  O(n)    O(nlogn)  O(n²)    O(2ⁿ)
────────────────────────────────────────────────────────
10     1     3        10      33        100      1,024
100    1     7        100     664       10,000   ~10³⁰
1000   1     10       1000    9,965     1,000,000 ~10³⁰⁰
10000  1     13       10,000  132,877   100M     Impossible
```

### Practical Limits

```
For typical computer (1 billion operations/sec):

O(1)       - Any size instantly
O(log n)   - 1 billion items: 30 operations
O(n)       - 1 billion items: 1 second
O(n log n) - 1 billion items: 30 seconds
O(n²)      - 1 million items: 12 days
O(2ⁿ)      - 30 items: Millions of years
O(n!)      - 15 items: Millions of years
```

---

## How to Analyze Code: Step-by-Step Process

### Process

1. **Identify loops and recursion**
2. **Count iterations**
3. **Apply multiplication rule for nested loops**
4. **Apply addition rule for sequential operations**
5. **Drop constants and lower terms**
6. **Identify final complexity**

### Example 1: Simple Loop

```python
def print_items(n):
    for i in range(n):
        print(i)

Step 1: One loop, runs n times
Step 2: n iterations
Step 3: Not nested
Step 4: O(n)
Step 5: Already simplified
Step 6: O(n)
```

### Example 2: Nested Loops

```python
def print_pairs(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

Step 1: Two nested loops
Step 2: Outer: n, Inner: n
Step 3: n × n = n²
Step 4: O(n²)
Step 5: Already simplified
Step 6: O(n²)
```

### Example 3: Mixed Operations

```python
def complex_algorithm(n):
    # Phase 1: O(n)
    for i in range(n):
        print(i)

    # Phase 2: O(n²)
    for i in range(n):
        for j in range(n):
            print(i, j)

    # Phase 3: O(1)
    x = 5
    y = 10

Step 1-4: O(n) + O(n²) + O(1)
Step 5: O(n) + O(n²) is dominated by O(n²)
Step 6: O(n²)
```

### Example 4: Recursive

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

Step 1: Recursion, calls itself once per value
Step 2: Called n times (n, n-1, ..., 1)
Step 3: Linear chain, O(n)
Step 4: O(n)
Step 5: Already simplified
Step 6: O(n) time, O(n) space (call stack)
```

---

## Summary

### Big O Classes (Fastest to Slowest)

```
O(1)        Constant        Instant, independent of n
O(log n)    Logarithmic     Binary search
O(n)        Linear          Single loop
O(n log n)  Linearithmic    Good sorting
O(n²)       Quadratic       Nested loops
O(n³)       Cubic           Triple nested loops
O(2ⁿ)       Exponential     Subset generation (avoid!)
O(n!)       Factorial       Permutations (avoid!)
```

### Key Rules

```
1. Drop constants: O(2n) → O(n)
2. Drop lower terms: O(n² + n) → O(n²)
3. Nested loops multiply: O(n) × O(n) = O(n²)
4. Sequential operations add: O(n) + O(n) = O(n)
5. Worst case usually reported
```

### Always Analyze

```
1. What is the time complexity?
2. What is the space complexity?
3. Is there a better algorithm?
4. What are tradeoffs?
5. Does it scale for real-world data?
```

### Algorithm Design Checklist

```
✓ Understand the problem thoroughly
✓ Consider multiple approaches
✓ Prove correctness (induction/invariants)
✓ Analyze time and space complexity
✓ Implement with clear, documented code
✓ Test with edge cases
✓ Optimize if needed
```
