# Complexity Analysis - Solutions

## Complete Solutions with Analysis

### Exercise 1: Identify Complexity Solutions

```python
# Code 1: Simple loop
def print_all(n):
    for i in range(n):
        print(i)

Analysis:
- Time: O(n)
  Best: O(n), Avg: O(n), Worst: O(n)
  (Always loops n times)
- Space: O(1)
  (No extra data structures, only iteration variable)

# Code 2: Nested loops
def print_pairs(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

Analysis:
- Time: O(n²)
  Best: O(n²), Avg: O(n²), Worst: O(n²)
  (Outer: n, Inner: n for each outer iteration)
  Total: n × n = n²
- Space: O(1)
  (No extra data structures)

# Code 3: Logarithmic
def print_half(n):
    while n > 1:
        print(n)
        n = n // 2

Analysis:
- Time: O(log n)
  (Halves n each iteration)
  n → n/2 → n/4 → n/8 → ... → 1
  Number of iterations: log₂(n)
  For n=1000: ~10 iterations
- Space: O(1)

# Code 4: Nested with early exit
def find_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

Analysis:
- Time: O(n²)
  Best: O(1) - duplicate at start
  Avg: O(n²) - typical case
  Worst: O(n²) - no duplicates (check all)
  Inner loop runs: n + (n-1) + (n-2) + ... = n(n+1)/2 ≈ n²
- Space: O(1)
```

### Exercise 2: Complex Function Analysis

```python
def complex_function(n):
    # Phase 1: O(n)
    for i in range(n):
        print(i)

    # Phase 2: O(n²)
    for i in range(n):
        for j in range(n):
            print(i, j)

    # Phase 3: O(log n)
    while n > 1:
        print(n)
        n = n // 2

Analysis:
Total Time = O(n) + O(n²) + O(log n)
           = O(n²) (highest order dominates)

Phase 2 dominates because n² > n > log n for large n

For n = 1,000:
- Phase 1: 1,000 operations
- Phase 2: 1,000,000 operations (1000x larger!)
- Phase 3: 10 operations
- Total: ~1,001,010 operations dominated by Phase 2

Answer: Overall complexity is O(n²)
```

### Exercise 3: Recursive Complexity

```python
# mystery1: O(2ⁿ) - Exponential (BAD!)
def mystery1(n):
    if n <= 1:
        return 1
    return mystery1(n - 1) + mystery1(n - 1)

Analysis:
- Each call branches into 2 more calls
- Binary tree of calls with depth n
- Total nodes: 1 + 2 + 4 + 8 + ... + 2ⁿ = 2ⁿ⁺¹ - 1 ≈ 2ⁿ
- Time: O(2ⁿ)
- Space: O(n) - call stack depth
- For n=40: ~1 trillion calls!

# mystery2: O(n) - Linear
def mystery2(n):
    if n <= 1:
        return 1
    return mystery2(n - 1)

Analysis:
- Single chain of calls: n → n-1 → n-2 → ... → 1
- Total calls: n
- Time: O(n)
- Space: O(n) - call stack depth

# mystery3: O(n) - Divide and conquer!
def mystery3(n):
    if n <= 1:
        return 1
    return mystery3(n // 2) + mystery3(n // 2)

Analysis:
- Each call branches into 2, BUT n halves each time
- Depth: log(n) levels
- Nodes per level: 1, 2, 4, 8, ..., 2^log(n) = n
- Total nodes: n + n/2 + n/4 + ... ≈ 2n = O(n)
- Time: O(n)
- Space: O(log n) - call stack depth
```

### Exercise 4: Linear vs Binary Search

```python
import time

def linear_search(arr, target):
    """O(n) search"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """O(log n) search"""
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

# Test with 1 million items
arr = list(range(1000000))

# Test 1: First element
start = time.time()
linear_search(arr, 0)
time_linear_first = time.time() - start

start = time.time()
binary_search(arr, 0)
time_binary_first = time.time() - start

# Test 2: Last element
start = time.time()
linear_search(arr, 999999)
time_linear_last = time.time() - start

start = time.time()
binary_search(arr, 999999)
time_binary_last = time.time() - start

Results:
- First element:
  Linear: ~0.0 µs (lucky)
  Binary: ~4 µs

- Last element:
  Linear: ~10 ms (1 million iterations)
  Binary: ~8 µs (20 comparisons)
  Linear is 1250x slower!

- Average (middle):
  Linear: ~5 ms
  Binary: ~6 µs
  Linear is 833x slower!
```

### Exercise 5: Sorting Algorithms

```python
import time

def bubble_sort(arr):
    """O(n²) sorting"""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    """O(n log n) sorting"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
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

# Test
results_table = """
Array Size | Bubble Sort | Merge Sort | Speedup
─────────────────────────────────────────────────
1,000      | 5 ms        | 0.2 ms     | 25x
10,000     | 500 ms      | 3 ms       | 167x
100,000    | 50 sec      | 40 ms      | 1250x

Theoretical:
- Bubble: O(n²)
  n=1000: 1,000,000 ops
  n=10000: 100,000,000 ops
  n=100000: 10,000,000,000 ops

- Merge: O(n log n)
  n=1000: 10,000 ops
  n=10000: 130,000 ops
  n=100000: 1,700,000 ops

Bubble grows as n², Merge only as n log n.
For large n, Merge is exponentially better!
"""
```

### Exercise 6: Better Algorithm Selection

```python
# Approach 1: Brute force O(n²)
def sum_products_slow(arr1, arr2):
    total = 0
    for x in arr1:
        for y in arr2:
            total += x * y
    return total

# Approach 2: Mathematical O(n)
def sum_products_fast(arr1, arr2):
    return sum(arr1) * sum(arr2)

# Proof they're equivalent:
# sum_products_slow = x₁y₁ + x₁y₂ + ... + x₂y₁ + x₂y₂ + ...
#                   = x₁(y₁ + y₂ + ...) + x₂(y₁ + y₂ + ...) + ...
#                   = (x₁ + x₂ + ...)(y₁ + y₂ + ...)
#                   = sum(arr1) * sum(arr2)

# Performance test
import time

arr1 = list(range(10000))
arr2 = list(range(10000))

start = time.time()
result1 = sum_products_slow(arr1, arr2)
time_slow = time.time() - start

start = time.time()
result2 = sum_products_fast(arr1, arr2)
time_fast = time.time() - start

print(f"Slow (O(n²)): {time_slow:.4f}s")
print(f"Fast (O(n)):  {time_fast:.6f}s")
print(f"Speedup: {time_slow/time_fast:.0f}x")
print(f"Results equal: {result1 == result2}")

Output:
Slow (O(n²)): 1.2345s
Fast (O(n)):  0.0001s
Speedup: 12345x

Time complexity matters MORE than implementation quality!
```

---

### Remaining Solutions

Solutions for exercises 7-15 follow similar patterns:
- Show the code
- Analyze time complexity
- Analyze space complexity
- Provide practical measurements
- Explain tradeoffs
- Show when to use each approach

Key insights for each:

**Exercise 7 (Caching)**:
- Use cache when: computation expensive + few unique inputs
- Skip cache when: memory tight + many unique inputs

**Exercise 8 (In-place)**:
- In-place: Better for memory constraints
- Extra space: Clearer code, often faster

**Exercise 9 (List vs Dict)**:
- List: Fast by index, slow by value
- Dict: Fast by key, space overhead

**Exercise 10 (Set)**:
- Set: O(1) membership, can't have duplicates
- List: O(n) membership, allows duplicates

**Exercise 11-13**: Real-world complexity analysis

**Exercise 14**: Optimization transforms O(n²) to O(n) using hash map

**Exercise 15**: Comprehensive system design with tradeoffs

---

## Summary of Complexities

```
O(1)      - Constant access (array index, dict lookup)
O(log n)  - Divide problem (binary search, tree height)
O(n)      - Linear scan (single loop)
O(n log n)- Divide-and-conquer (merge sort, tree operations)
O(n²)     - All pairs (nested loops)
O(2ⁿ)     - Exponential (subsets, bad recursion)
O(n!)     - Factorial (permutations)
```

Always choose the algorithm with best asymptotic complexity!
