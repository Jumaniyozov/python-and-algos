# Complexity Analysis - Tips and Best Practices

## Quick Reference Guide

### Common Complexity Times

```
O(1)       < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)

For n = 1,000,000:

O(1):      1 operation
O(log n):  20 operations
O(n):      1 million operations
O(n log n):20 million operations
O(n²):     1 trillion operations (NEVER FINISH)
O(2ⁿ):     Impossible
O(n!):     Impossible
```

---

## Analysis Techniques

### Technique 1: Identify Dominant Term

```python
def example(n):
    # 100 constant operations
    x = 0
    for i in range(100):
        x += 1

    # 5n linear operations
    for i in range(n):
        print(i)

    # n² quadratic operations
    for i in range(n):
        for j in range(n):
            print(i, j)

# Total time:
# 100 + 5n + n²

# As n grows:
# n=10:     100 + 50 + 100 = 250
# n=100:    100 + 500 + 10,000 = 10,600
# n=1000:   100 + 5000 + 1,000,000 = 1,005,100

# Dominant term: n²
# Final answer: O(n²)

# Rule: Keep only highest-order term
```

### Technique 2: Count Loop Iterations

```python
# Simple loop: n iterations
for i in range(n):
    print(i)
# Result: O(n)

# Nested loop: n × n iterations
for i in range(n):
    for j in range(n):
        print(i, j)
# Result: O(n²)

# Loop halving: log(n) iterations
x = n
while x > 1:
    print(x)
    x = x // 2
# Result: O(log n)

# Loop doubling: log(n) iterations
x = 1
while x < n:
    print(x)
    x = x * 2
# Result: O(log n)

# Partial loop: n/2 iterations (still O(n))
for i in range(n // 2):
    print(i)
# Result: O(n) not O(n/2)
# (Constants dropped)

# Three nested loops: n × n × n
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
# Result: O(n³)
```

### Technique 3: Sequential Operations Add

```python
def example(n):
    # Phase 1: O(n)
    for i in range(n):
        print(i)

    # Phase 2: O(n log n)
    sorted_arr = sorted(list(range(n)))

    # Phase 3: O(n²)
    for i in range(n):
        for j in range(n):
            print(i, j)

# Total: O(n) + O(n log n) + O(n²)

# When adding complexities:
# Keep only the HIGHEST
# O(n) + O(n log n) + O(n²) = O(n²)

# Why?
# For large n:
# n² >> n log n >> n
# n² dominates everything else
```

### Technique 4: Understand Common Patterns

```
Loop Pattern                    Complexity
─────────────────────────────────────────────
for i in range(n):             O(n)
    statement

for i in range(n):             O(n²)
    for j in range(n):
        statement

for i in range(n):             O(n log n)
    for j in range(i):
        statement

while n > 1:                    O(log n)
    n = n // 2

while n < limit:               O(log n)
    n = n * 2

for i in range(n):             O(n log n)
    binary_search(arr, i)

sorted(arr)                     O(n log n)

arr.append()                    O(1) amortized

x in arr                        O(n)

x in set                        O(1)

dict[key]                       O(1)
```

---

## Optimization Strategies

### Strategy 1: Use Better Data Structures

```python
# SLOW: List search O(n)
def find_student(students, name):
    for student in students:
        if student['name'] == name:
            return student
    return None

# FAST: Dictionary lookup O(1)
def find_student_fast(student_dict, name):
    return student_dict.get(name)

# Performance:
# List of 1 million students: ~500,000 comparisons
# Dictionary of 1 million students: ~1 lookup
# Dictionary is 500,000x faster!
```

### Strategy 2: Use Better Algorithm

```python
# SLOW: Bubble sort O(n²)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# FAST: Merge sort O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # Conquer
    return merge(left, right)

# For 10,000 items:
# Bubble sort: ~100 million operations
# Merge sort: ~130,000 operations
# Merge sort is ~1000x faster!
```

### Strategy 3: Memoization for Repeated Calculations

```python
# SLOW: Exponential O(2ⁿ)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# FAST: With memoization O(n)
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# For n=40:
# Without memo: ~1 billion calls
# With memo: ~40 calls
# 25 million times faster!
```

### Strategy 4: Early Exit/Pruning

```python
# SLOW: Check all pairs O(n²)
def find_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

# FAST: Use set O(n)
def find_duplicate_fast(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

# Even better for small arrays: O(n) with early exit
# Return as soon as duplicate found!
```

---

## Common Mistakes to Avoid

### Mistake 1: Ignoring Hidden Loops

```python
# Looks like O(n), but:
def process(arr):
    for item in arr:              # O(n)
        print(item.upper())       # O(m) where m = length of string
    return

# Actually O(n × m) where m = average string length
# If m is large, this could be slow!
```

### Mistake 2: Underestimating Recursion

```python
# Looks harmless, but O(2ⁿ)!
def count_subsets(arr):
    if not arr:
        return 1
    head, *tail = arr
    # Recursively count: with head, without head
    return count_subsets(tail) + count_subsets(tail)

# Each call branches into 2
# For n=30: ~1 billion calls!
```

### Mistake 3: Forgetting String Operations

```python
# Each concatenation: O(n)
result = ""
for item in items:
    result += item  # This is O(n) each time!

# Total: O(n²) not O(n)!

# Fix: Use list and join O(n)
result_list = []
for item in items:
    result_list.append(item)  # O(1)
result = "".join(result_list)  # O(n)

# Total: O(n)
```

### Mistake 4: Underestimating Collection Size

```python
# For n = 1,000,000:
# This seems reasonable but is VERY slow

for i in range(len(arr)):          # O(n)
    for j in range(len(arr)):      # O(n)
        if arr[i] * arr[j] == target:  # O(n²)
            results.append((i, j))

# 1,000,000 × 1,000,000 = 1 trillion operations
# Will take hours to run!
```

---

## Best Practices

### Practice 1: Always Analyze Before Coding

```python
# GOOD: Think about complexity first
# Problem: Find if two arrays have common elements
#
# Analysis:
# - Brute force: O(n²) nested loops
# - Better: O(n) with set
# - Best for this problem: O(n)
#
# Implementation:
def has_common(arr1, arr2):
    set1 = set(arr1)  # O(n)
    for item in arr2:  # O(m)
        if item in set1:  # O(1)
            return True
    return False
# Total: O(n + m)

# BAD: Code first, optimize later
# Often results in poor algorithmic choice
```

### Practice 2: Measure Performance

```python
import time

def algorithm1(n):
    # O(n) implementation
    total = 0
    for i in range(n):
        total += i
    return total

def algorithm2(n):
    # O(1) implementation
    return n * (n - 1) // 2

# Measure
for n in [1000, 10000, 100000, 1000000]:
    start = time.time()
    result1 = algorithm1(n)
    time1 = time.time() - start

    start = time.time()
    result2 = algorithm2(n)
    time2 = time.time() - start

    print(f"n={n}: algo1={time1:.6f}s, algo2={time2:.6f}s")

# As n increases:
# - algo1 time increases linearly
# - algo2 time stays constant
# Proves O(n) vs O(1)
```

### Practice 3: Use Appropriate Data Structures

```
Use:                    When:
─────────────────────────────────────────
List                    Need order, frequent indexing
Dictionary              Need fast key lookup
Set                     Need membership testing, uniqueness
Tuple                   Need immutable sequence
Deque                   Need fast append/pop both ends
Heap                    Need min/max operations
Tree                    Need sorted data, range queries
```

### Practice 4: Document Complexity

```python
def binary_search(arr, target):
    """
    Search for target in sorted array.

    Time Complexity:  O(log n)
    Space Complexity: O(1)

    Reasoning:
    - Halves search space each iteration
    - log₂(n) iterations needed
    - Constant extra space

    Best case: O(1) - target is middle element
    Worst case: O(log n) - target not found
    """
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

---

## Practical Decision Framework

When choosing an algorithm, consider:

### 1. What is Expected Data Size?

```
n < 100:
  Any algorithm works
  Readability > performance

100 < n < 10,000:
  O(n²) is acceptable
  O(n log n) is better

n > 10,000:
  O(n) is minimum
  O(n log n) is good
  O(n²) is unacceptable

n > 1,000,000:
  O(n) must be optimized
  O(log n) is ideal
  Any O(n²) will timeout
```

### 2. What are Resource Constraints?

```
Time constraint (must complete in 1 second):
  n = 1,000,000 → need O(1) or O(log n)
  n = 10,000 → need O(n log n) or better
  n = 100 → any algorithm OK

Space constraint (limited memory):
  Can't use O(n) extra space
  → Use O(1) or O(log n) algorithms
  → Avoid creating copies

Both constraints:
  → Choose most efficient algorithm
  → Usually sacrifice space for time
  → Use memoization sparingly
```

### 3. Real-World Tradeoff Matrix

```
Scenario              Algorithm        Time      Space    Reason
─────────────────────────────────────────────────────────────────
Sorting millions      Merge sort       O(nlogn)  O(n)    Best time
  of items
Finding in dict      Hash table       O(1) avg  O(n)    Best lookup
Sorting with         Heap sort        O(nlogn)  O(1)    Save space
  no extra space
Many queries         Build index      O(n)      O(n)    Save query time
  on same data
Limited memory       Bubble sort      O(n²)     O(1)    Only option
  small data
Real-time system    Binary search    O(logn)   O(1)    Predictable
```

---

## Debugging Complexity Issues

### Problem: Code Runs Slow

```
Checklist:
- [ ] What is current complexity?
- [ ] What is expected complexity?
- [ ] Identify the slow part (profile code)
- [ ] Can you use better algorithm?
- [ ] Can you use better data structure?
- [ ] Are there unnecessary operations?
- [ ] Is there redundant computation?
- [ ] Can you cache results?

Example fix:
# SLOW
for i in range(n):
    if i in list_of_items:  # O(n) per iteration

# FAST
items_set = set(list_of_items)
for i in range(n):
    if i in items_set:  # O(1) per iteration
```

### Problem: Code Uses Too Much Memory

```
Checklist:
- [ ] What is current space complexity?
- [ ] Where is memory used?
- [ ] Can you use in-place algorithm?
- [ ] Can you process in chunks?
- [ ] Can you stream instead of loading all?

Example fix:
# MEMORY HEAVY: Load all data
data = [process(line) for line in open('huge_file.txt')]

# MEMORY LIGHT: Process line by line
for line in open('huge_file.txt'):
    process(line)
```

---

## Interview Tips

When analyzing code in an interview:

1. **State assumption clearly**
   - "Assuming n is the input size..."
   - "For the worst case..."

2. **Walk through example**
   - Use small input like n=4
   - Count actual operations
   - Show pattern

3. **Express Big O clearly**
   - "This is O(n) linear time"
   - "O(1) constant space"
   - "Not O(2^n) exponential"

4. **Explain reasoning**
   - "The loop runs n times..."
   - "Nested loops multiply..."
   - "Sorting is O(n log n)..."

5. **Optimize step by step**
   - Start with correct solution
   - Identify bottleneck
   - Propose better approach
   - Verify correctness

---

## Cheat Sheet

```
Common Complexities Quick Lookup:

array[i]                    O(1)
list.append()               O(1) amortized
list.insert(0, x)           O(n)
list.pop()                  O(1)
list.pop(0)                 O(n)
x in list                   O(n)
x in set                    O(1)
dict[key]                   O(1)
sorted()                    O(n log n)
sum(list)                   O(n)
len(list)                   O(1)
list.index(x)               O(n)
set.add()                   O(1)
set.remove()                O(1)
dict.update()               O(n)

Two sum problem:
- Brute force: O(n²)
- Hash map: O(n)

Three sum problem:
- Brute force: O(n³)
- Sort + two pointers: O(n²)

Merge arrays:
- Naive: O(n log n) with sorting
- Two pointers: O(n)
```

Remember: **Algorithm choice matters far more than code optimization!**
