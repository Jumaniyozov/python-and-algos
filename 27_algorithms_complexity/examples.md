# Algorithms and Complexity Analysis - Examples

## Mathematical Induction Examples

### Example 1: Proving Sum Formula

**Claim**: 1 + 2 + 3 + ... + n = n(n+1)/2

```python
def sum_formula(n):
    """Formula approach: n(n+1)/2"""
    return n * (n + 1) // 2

def sum_iterative(n):
    """Iterative approach"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Proof by induction already shown in theory.md
# Let's verify it works:

for n in [1, 5, 10, 100, 1000]:
    formula_result = sum_formula(n)
    iterative_result = sum_iterative(n)
    print(f"n={n}: Formula={formula_result}, Iterative={iterative_result}, Match={formula_result == iterative_result}")

# Output:
# n=1: Formula=1, Iterative=1, Match=True
# n=5: Formula=15, Iterative=15, Match=True
# n=10: Formula=55, Iterative=55, Match=True
# n=100: Formula=5050, Iterative=5050, Match=True
# n=1000: Formula=500500, Iterative=500500, Match=True
```

### Example 2: Loop Invariant for Array Reversal

```python
def reverse_array(arr):
    """
    Reverse array in-place using two pointers.

    Loop Invariant:
    - Elements before left pointer are reversed
    - Elements after right pointer are reversed
    - Elements between pointers are not yet processed

    Proof:
    - Initialization: left=0, right=n-1, no elements reversed yet ✓
    - Maintenance: Swap arr[left] and arr[right], increment left, decrement right ✓
    - Termination: When left >= right, all elements are reversed ✓
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        # Invariant holds here: [reversed | unprocessed | reversed]
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        # Invariant still holds after swap

    return arr

# Test
original = [1, 2, 3, 4, 5]
reversed_arr = reverse_array(original[:])
print(f"Original: [1, 2, 3, 4, 5]")
print(f"Reversed: {reversed_arr}")
print(f"Correct: {reversed_arr == [5, 4, 3, 2, 1]}")
```

### Example 3: Proving Algorithm Correctness for Selection Sort

```python
def selection_sort(arr):
    """
    Sort array using selection sort.

    Loop Invariant:
    - After i iterations, first i elements are sorted
    - First i elements contain the i smallest values
    - Elements after index i are unsorted

    Proof by Induction:

    Base Case (i=0):
      - Zero elements are sorted (trivially true) ✓

    Inductive Hypothesis:
      - Assume after k iterations, first k elements are sorted
      - and contain the k smallest values

    Inductive Step (i=k+1):
      - Find minimum in arr[k+1:]
      - Swap with arr[k]
      - Now first k+1 elements are sorted
      - and contain the k+1 smallest values ✓

    Termination (i=n):
      - First n elements are sorted
      - This is the entire array ✓

    Time: O(n²), Space: O(1)
    """
    n = len(arr)

    for i in range(n):
        # Invariant: arr[0:i] is sorted and contains i smallest elements
        min_idx = i

        # Find minimum in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap minimum to position i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # Invariant holds: arr[0:i+1] is now sorted

    return arr

# Test
test_arr = [64, 25, 12, 22, 11]
print(f"Original: {test_arr}")
sorted_arr = selection_sort(test_arr[:])
print(f"Sorted: {sorted_arr}")
print(f"Correct: {sorted_arr == [11, 12, 22, 25, 64]}")
```

### Example 4: Geometric Series Sum

**Claim**: 1 + 2 + 4 + 8 + ... + 2^n = 2^(n+1) - 1

```python
def geometric_sum_formula(n):
    """Sum of powers of 2 from 2^0 to 2^n using formula"""
    return 2**(n + 1) - 1

def geometric_sum_iterative(n):
    """Sum of powers of 2 iteratively"""
    total = 0
    for i in range(n + 1):
        total += 2**i
    return total

# Induction Proof:
# Base Case (n=0): 2^0 = 1, Formula = 2^1 - 1 = 1 ✓
# Assume true for n=k: sum = 2^(k+1) - 1
# Prove for n=k+1:
#   sum = (2^(k+1) - 1) + 2^(k+1)  [by hypothesis + new term]
#       = 2*2^(k+1) - 1
#       = 2^(k+2) - 1
#       = 2^((k+1)+1) - 1  ✓

for n in [0, 1, 2, 3, 4, 10]:
    formula = geometric_sum_formula(n)
    iterative = geometric_sum_iterative(n)
    print(f"n={n}: Formula={formula}, Iterative={iterative}, Match={formula == iterative}")
```

---

## Complexity Analysis Examples

### O(1) - Constant Time Examples

#### Example 1: Dictionary Lookup

```python
def find_student_grade(grades_dict, student_name):
    """
    Retrieve a student's grade by name.

    Time: O(1) - Dictionary lookup is constant
    Space: O(1) - Only store one value
    """
    return grades_dict[student_name]

# Usage
grades = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
print(find_student_grade(grades, 'Bob'))  # O(1)
```

#### Example 2: Direct Array Access

```python
def get_first_last(arr):
    """
    Get first and last elements of array.

    Time: O(1) - Direct index access
    Space: O(1) - Constant memory
    """
    first = arr[0]
    last = arr[-1]
    return first, last

# Usage
numbers = [1, 2, 3, 4, 5]
print(get_first_last(numbers))  # O(1)
```

---

### O(log n) - Logarithmic Examples

#### Example 3: Binary Search

```python
def binary_search(arr, target):
    """
    Find target in sorted array.

    Time: O(log n) - Halves search space each iteration
    Space: O(1) - Constant extra space

    For n=1000000:
      - Linear search: ~500,000 comparisons
      - Binary search: ~20 comparisons
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

# Usage
numbers = list(range(1000000))
print(binary_search(numbers, 999999))  # ~20 iterations
```

#### Example 4: Find in Power of 2

```python
def find_highest_power(n):
    """
    Find highest power of 2 less than n.

    Time: O(log n) - Divides by 2 each iteration
    Space: O(1)

    n=1000000 → ~20 iterations
    """
    power = 1
    while power * 2 <= n:
        power *= 2
    return power

print(find_highest_power(1000))  # 512 (2^9)
```

---

### O(n) - Linear Examples

#### Example 5: Sum of Array

```python
def sum_array(arr):
    """
    Sum all elements in array.

    Time: O(n) - Must check each element once
    Space: O(1) - Only store running total
    """
    total = 0
    for num in arr:
        total += num
    return total

# Time comparison:
# n=100: 100 operations
# n=1000000: 1000000 operations
```

#### Example 6: Linear Search

```python
def linear_search(arr, target):
    """
    Find target in unsorted array.

    Time: O(n) in worst case
      - Best: O(1) if first element
      - Average: O(n/2) = O(n)
      - Worst: O(n) if not found
    Space: O(1)
    """
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

# vs Binary Search:
# Linear: 500,000 comparisons
# Binary: 20 comparisons
```

---

### O(n log n) - Linearithmic Examples

#### Example 7: Merge Sort

```python
def merge_sort(arr):
    """
    Sort array using merge sort.

    Time: O(n log n) - Always
      - Divide: O(log n) levels
      - Merge: O(n) per level
      - Total: O(n) × O(log n) = O(n log n)
    Space: O(n) - Extra space for merging

    For n=1000000:
      - ~20 million operations
      - Merge sort: Very fast
      - Bubble sort: 1 trillion operations (slow!)
    """
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
```

#### Example 8: For Each, Binary Search

```python
def count_occurrences_efficient(arr, targets):
    """
    Count occurrences of each target in sorted array.

    Time: O(n log n)
      - For each target: O(log n) binary search
      - m targets: O(m log n)
      - Here m = n, so O(n log n)
    Space: O(n) for results dictionary
    """
    sorted_arr = sorted(arr)  # O(n log n)
    counts = {}

    for target in targets:  # O(n)
        count = binary_search_count(sorted_arr, target)  # O(log n)
        counts[target] = count

    return counts

def binary_search_count(arr, target):
    # Find leftmost and rightmost positions
    left = binary_search_left(arr, target)
    right = binary_search_right(arr, target)
    return right - left + 1 if left != -1 else 0
```

---

### O(n²) - Quadratic Examples

#### Example 9: Bubble Sort

```python
def bubble_sort(arr):
    """
    Sort array using bubble sort.

    Time: O(n²) - Always
      - Outer loop: n iterations
      - Inner loop: n-1 iterations each
      - Total: n × (n-1) ≈ n²
    Space: O(1) - In-place sorting

    AVOID for large datasets!
    n=1000: ~1,000,000 operations
    n=10000: ~100,000,000 operations
    """
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

#### Example 10: All Pairs

```python
def find_pairs_with_sum(arr, target_sum):
    """
    Find all pairs that sum to target.

    Time: O(n²) - Check all pairs
      - Outer loop: n iterations
      - Inner loop: n iterations
      - Total: n × n = n²
    Space: O(n) for results

    Better solution exists: O(n) with hash set
    """
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs

# O(n) solution:
def find_pairs_fast(arr, target_sum):
    """
    Find all pairs using hash set.

    Time: O(n) - Single pass with hash table
    Space: O(n) for hash set
    """
    seen = set()
    pairs = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)

    return list(pairs)
```

---

### O(2ⁿ) - Exponential Examples

#### Example 11: Fibonacci (Naive)

```python
def fibonacci_bad(n):
    """
    Calculate fibonacci number (VERY SLOW).

    Time: O(2ⁿ) - Exponential!
    Space: O(n) - Call stack depth

    fib(10): 177 calls
    fib(20): 21,891 calls
    fib(30): 2,178,309 calls
    fib(40): 267,914,296 calls

    NEVER use for n > 35!
    """
    if n <= 1:
        return n
    return fibonacci_bad(n - 1) + fibonacci_bad(n - 2)

# Time it
import time
start = time.time()
print(fibonacci_bad(30))  # Takes 1 second
print(f"Time: {time.time() - start:.2f}s")

# Better solution: O(n)
def fibonacci_good(n):
    """
    Calculate fibonacci number (FAST).

    Time: O(n) - Single pass
    Space: O(1) - Constant extra space
    """
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

# Time it
start = time.time()
print(fibonacci_good(30))  # Instant
print(f"Time: {time.time() - start:.6f}s")
```

---

### Space Complexity Examples

#### Example 12: Inplace vs Extra Space

```python
def reverse_inplace(arr):
    """
    Reverse array in-place.

    Time: O(n)
    Space: O(1) - No extra space
    """
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def reverse_with_space(arr):
    """
    Reverse array using extra space.

    Time: O(n)
    Space: O(n) - Creates new array
    """
    return arr[::-1]

# For n=1,000,000:
# In-place: 4 bytes temporary storage
# With space: 4,000,000 bytes (4 MB) for new array
```

---

### Comparison Examples

#### Example 13: Finding Maximum

```python
# O(n) - Must check all elements
def find_max_linear(arr):
    return max(arr)

# O(n log n) - Sort then return last
def find_max_overkill(arr):
    return sorted(arr)[-1]

# Performance for n=1,000,000:
# Linear: 1 million comparisons
# Sorting: 20 million comparisons
# Linear is 20x faster!

# Time it
import time
import random

data = [random.randint(1, 1000000) for _ in range(1000000)]

start = time.time()
max1 = find_max_linear(data)
time1 = time.time() - start

start = time.time()
max2 = find_max_overkill(data)
time2 = time.time() - start

print(f"Linear: {time1:.4f}s")
print(f"Sorting: {time2:.4f}s")
print(f"Sorting is {time2/time1:.1f}x slower")
```

---

### Amortized Analysis Example

#### Example 14: Dynamic Array Growth

```python
import time

def measure_appends(n):
    """
    Measure time to append n items.

    Each append:
    - Usually O(1)
    - Occasionally O(n) when resizing

    Total: O(n) for all appends
    Amortized: O(1) per append
    """
    lst = []
    start = time.time()

    for i in range(n):
        lst.append(i)

    elapsed = time.time() - start
    return elapsed

# Test
for n in [100000, 1000000, 10000000]:
    elapsed = measure_appends(n)
    per_append = elapsed * 1e6 / n  # microseconds per append
    print(f"n={n}: {per_append:.2f} µs per append")

# Output:
# n=100000: ~0.05 µs per append
# n=1000000: ~0.05 µs per append
# n=10000000: ~0.05 µs per append
# Average is constant despite occasional O(n) resizes!
```

---

### Real-World Complexity Analysis

#### Example 15: Web Search Algorithm

```python
def search_database(query, database):
    """
    Search database for query terms.

    Complexity depends on approach:

    Approach 1: Linear scan
    - Read all records: O(n)
    - Check each record: O(m) where m is record size
    - Time: O(n × m)

    Approach 2: Indexed search
    - Index lookup: O(log n)
    - Time: O(log n)

    For 1 billion records:
    - Linear: ~1 billion operations
    - Indexed: ~30 operations

    Indexed is 33 million times faster!
    """
    # Linear approach (BAD)
    results = []
    for record in database:
        if query.lower() in record['text'].lower():
            results.append(record)
    return results

def search_indexed(query, index):
    """
    Search using pre-built index.

    Time: O(log n) to find index entry
    Then O(k) to retrieve k results

    Total: O(log n + k) - Much better!
    """
    if query in index:
        return index[query]  # O(log n) for dictionary lookup
    return []
```

---

## Visualization of Growth

```
Iterations Required by Algorithm Type

Input Size: 10
O(1):  1 operation
O(logn): 3 operations
O(n): 10 operations
O(nlogn): 30 operations
O(n²): 100 operations
O(2ⁿ): 1,024 operations
O(n!): 3,628,800 operations

Input Size: 100
O(1):  1
O(logn): 7
O(n): 100
O(nlogn): 700
O(n²): 10,000
O(2ⁿ): Impossible (10³⁰ operations)
O(n!): Impossible

Input Size: 1000
O(1):  1
O(logn): 10
O(n): 1,000
O(nlogn): 10,000
O(n²): 1,000,000
O(2ⁿ): Impossible
O(n!): Impossible

Input Size: 1,000,000
O(1):  1 (instant)
O(logn): 20 (instant)
O(n): 1,000,000 (1ms)
O(nlogn): 20,000,000 (20ms)
O(n²): Impossible for practical use
O(2ⁿ): Impossible
O(n!): Impossible
```

---

## Key Takeaways

1. **Always analyze complexity** before writing code
2. **Avoid exponential** algorithms whenever possible
3. **Know common patterns**: loops, recursion, divide-and-conquer
4. **Trade space for time** when beneficial
5. **Use right data structure**: arrays, hash tables, trees
6. **Test with large datasets** to see real complexity
7. **Profile code** to identify bottlenecks
8. **Algorithm choice matters** more than language optimizations
