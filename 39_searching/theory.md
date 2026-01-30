# Chapter 39: Searching - Theory

## Table of Contents
1. [Introduction to Searching](#introduction-to-searching)
2. [Linear Search](#linear-search)
3. [Binary Search](#binary-search)
4. [Binary Search Variations](#binary-search-variations)
5. [Binary Search Templates](#binary-search-templates)
6. [Binary Search on Answer](#binary-search-on-answer)
7. [Other Search Algorithms](#other-search-algorithms)
8. [Advanced Search Patterns](#advanced-search-patterns)

---

## Introduction to Searching

**Searching** is the process of finding a particular element in a collection of elements. It's one of the most common operations in computer science.

### Why Searching Matters

1. **Fundamental Operation**: Core to many algorithms and data structures
2. **Efficiency**: Can make the difference between O(n) and O(log n)
3. **Interview Frequency**: 20-25% of coding interview problems
4. **Real-World Use**: Powers search engines, databases, file systems
5. **Problem-Solving Tool**: Enables "binary search on answer" pattern

### Classification

**By Data Structure:**
- Arrays/Lists
- Trees (covered in Chapter 33)
- Graphs (Chapter 40)
- Hash Tables (Chapter 32)

**By Approach:**
- **Sequential**: Linear search
- **Divide and Conquer**: Binary search
- **Heuristic**: Jump search, interpolation search

---

## Linear Search

### Concept

**Linear search** (or sequential search) checks each element one by one until finding the target or reaching the end.

### Algorithm

```
For each element in array:
    If element equals target:
        Return index
    Return -1 (not found)
```

### Implementation

```python
def linear_search(arr, target):
    """
    Search for target in unsorted array.
    Time: O(n), Space: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

### Characteristics

**Time Complexity:**
- Best Case: O(1) - Target is first element
- Average Case: O(n) - Target is somewhere in middle
- Worst Case: O(n) - Target is last or not present

**Space Complexity:** O(1) - No extra space needed

**Advantages:**
- Works on unsorted data
- Simple to implement
- No preprocessing needed
- Works on any data structure (arrays, linked lists, etc.)

**Disadvantages:**
- Slow for large datasets
- Not efficient compared to binary search for sorted data

**When to Use:**
- Small datasets (n < 100)
- Unsorted data
- Single search operation
- Linked lists (can't use binary search)

---

## Binary Search

### Concept

**Binary search** repeatedly divides a sorted array in half, comparing the middle element with the target. If the middle element is the target, we're done. Otherwise, eliminate half of the array and repeat.

### Requirements

1. **Data must be sorted**
2. **Random access** (O(1) access to any element)

### Algorithm

```
1. Set left = 0, right = n-1
2. While left <= right:
   a. Calculate mid = left + (right - left) / 2
   b. If arr[mid] == target: return mid
   c. If arr[mid] < target: search right half (left = mid + 1)
   d. If arr[mid] > target: search left half (right = mid - 1)
3. Return -1 (not found)
```

### Visualization

```
Array: [1, 3, 5, 7, 9, 11, 13, 15, 17]
Target: 7

Step 1: left=0, right=8, mid=4
[1, 3, 5, 7, 9, 11, 13, 15, 17]
             ^
arr[4]=9 > 7, search left half

Step 2: left=0, right=3, mid=1
[1, 3, 5, 7]
    ^
arr[1]=3 < 7, search right half

Step 3: left=2, right=3, mid=2
[5, 7]
 ^
arr[2]=5 < 7, search right half

Step 4: left=3, right=3, mid=3
[7]
 ^
arr[3]=7 == 7, found at index 3!
```

### Implementation

```python
def binary_search(arr, target):
    """
    Binary search on sorted array.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        # Avoid integer overflow
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Not found
```

### Recursive Implementation

```python
def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive binary search.
    Time: O(log n), Space: O(log n) for recursion stack
    """
    if right is None:
        right = len(arr) - 1

    # Base case: search space exhausted
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

### Complexity Analysis

**Time Complexity:**
- Best Case: O(1) - Target is middle element
- Average Case: O(log n)
- Worst Case: O(log n) - Keep halving until 1 element

**Derivation:**
```
n → n/2 → n/4 → n/8 → ... → 1
After k steps: n / 2^k = 1
Therefore: 2^k = n
Taking log: k = log₂(n)
```

**Space Complexity:**
- Iterative: O(1)
- Recursive: O(log n) for call stack

**Comparison with Linear Search:**
```
n = 100:     Linear: 100 ops,    Binary: 7 ops
n = 1,000:   Linear: 1,000 ops,  Binary: 10 ops
n = 1M:      Linear: 1M ops,     Binary: 20 ops
n = 1B:      Linear: 1B ops,     Binary: 30 ops
```

### When Binary Search Fails

```python
# ❌ Unsorted array
arr = [5, 2, 8, 1, 9]
binary_search(arr, 8)  # May not work!

# ❌ Linked list (no random access)
# Binary search requires O(1) access, linked list is O(n)

# ✅ Must sort first
arr.sort()  # O(n log n)
binary_search(arr, 8)  # Now works
```

---

## Binary Search Variations

### 1. Find Leftmost/First Occurrence

Find the first (leftmost) occurrence of target in array with duplicates.

```python
def find_first(arr, target):
    """
    Find first occurrence of target.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

**Example:**
```
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
Result: 1 (first occurrence at index 1)
```

### 2. Find Rightmost/Last Occurrence

Find the last (rightmost) occurrence of target.

```python
def find_last(arr, target):
    """
    Find last occurrence of target.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

### 3. Search Insert Position

Find index where target should be inserted to maintain sorted order.

```python
def search_insert(arr, target):
    """
    Find insertion position for target.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Insertion position
```

**Example:**
```
arr = [1, 3, 5, 6]
target = 2 → return 1 (insert at index 1)
target = 7 → return 4 (insert at end)
target = 0 → return 0 (insert at start)
```

### 4. Find Lower Bound

Find first element >= target.

```python
def lower_bound(arr, target):
    """
    Find first element >= target.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

### 5. Find Upper Bound

Find first element > target.

```python
def upper_bound(arr, target):
    """
    Find first element > target.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left
```

### 6. Count Occurrences

Count how many times target appears.

```python
def count_occurrences(arr, target):
    """
    Count occurrences of target using binary search.
    Time: O(log n), Space: O(1)
    """
    first = find_first(arr, target)
    if first == -1:
        return 0

    last = find_last(arr, target)
    return last - first + 1
```

---

## Binary Search Templates

### Template 1: Standard (left <= right)

**Use when:** Finding exact target, can check mid directly.

```python
def template1(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

**Characteristics:**
- Search space: `[left, right]` (inclusive)
- Termination: `left > right`
- Used for: Exact match

### Template 2: Find Boundary (left < right)

**Use when:** Finding boundary, need to preserve elements.

```python
def template2(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid  # Don't discard mid

    return left
```

**Characteristics:**
- Search space: `[left, right)` (left inclusive, right exclusive)
- Termination: `left == right`
- Used for: Lower bound, upper bound, insert position

### Template 3: Avoid Adjacent Elements

**Use when:** Need to check mid with neighbors.

```python
def template3(arr, target):
    left, right = 0, len(arr) - 1

    while left + 1 < right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing: check left and right
    if arr[left] == target:
        return left
    if arr[right] == target:
        return right
    return -1
```

**Characteristics:**
- Search space: `[left, right]`
- Termination: `left + 1 >= right`
- Used for: Peak finding, rotated arrays

---

## Binary Search on Answer

A powerful pattern where we binary search on the **answer space** rather than array indices.

### Concept

Instead of searching for a value in an array, we search for the answer in a range `[min_answer, max_answer]`.

**Key insight:** If answer X works, all answers ≥ X (or ≤ X) also work. This creates a monotonic property we can binary search on.

### Template

```python
def binary_search_on_answer(condition_func, low, high):
    """
    Binary search on answer space.
    Find minimum/maximum value satisfying condition.
    """
    result = -1

    while low <= high:
        mid = low + (high - low) // 2

        if condition_func(mid):
            result = mid
            # Depending on problem:
            # For minimum: high = mid - 1
            # For maximum: low = mid + 1
        else:
            # Adjust search space
            pass

    return result
```

### Example: Minimum Days to Make Bouquets

**Problem:** Given `m` bouquets needed, `k` flowers per bouquet, and array of bloom days, find minimum days to wait.

```python
def min_days(bloom_day, m, k):
    """
    Binary search on answer (days).
    """
    def can_make_bouquets(days):
        """Check if we can make m bouquets in 'days'."""
        bouquets = 0
        flowers = 0

        for bloom in bloom_day:
            if bloom <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0

        return bouquets >= m

    if m * k > len(bloom_day):
        return -1

    left, right = min(bloom_day), max(bloom_day)
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if can_make_bouquets(mid):
            result = mid
            right = mid - 1  # Try smaller days
        else:
            left = mid + 1

    return result
```

**Pattern Recognition:**
- Can define a range for answer: `[min_days, max_days]`
- If X days work, X+1 days also work (monotonic)
- Binary search to find minimum working days

### Common Applications

1. **Capacity Problems**: Minimum capacity needed
2. **Speed Problems**: Minimum/maximum speed
3. **Resource Allocation**: Minimum resources to satisfy condition
4. **Distance Problems**: Maximum minimum distance

---

## Other Search Algorithms

### Jump Search

**Idea:** Jump ahead by fixed steps, then linear search within block.

```python
def jump_search(arr, target):
    """
    Jump search on sorted array.
    Time: O(√n), Space: O(1)
    """
    import math

    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jump to find block
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search in block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev

    return -1
```

**Best step size:** √n
**Time:** O(√n)
**Use case:** Better than linear, worse than binary; useful when backward jumps are expensive

### Interpolation Search

**Idea:** Estimate position based on value distribution (like looking up a phone book).

```python
def interpolation_search(arr, target):
    """
    Interpolation search for uniformly distributed data.
    Time: O(log log n) average, O(n) worst
    """
    left, right = 0, len(arr) - 1

    while left <= right and arr[left] <= target <= arr[right]:
        if left == right:
            if arr[left] == target:
                return left
            return -1

        # Estimate position
        pos = left + ((target - arr[left]) * (right - left) //
                      (arr[right] - arr[left]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1

    return -1
```

**Time:** O(log log n) for uniformly distributed data, O(n) worst case
**Use case:** Large sorted arrays with uniform distribution

### Exponential Search

**Idea:** Find range by exponentially increasing index, then binary search.

```python
def exponential_search(arr, target):
    """
    Exponential search for unbounded/infinite arrays.
    Time: O(log n), Space: O(1)
    """
    if arr[0] == target:
        return 0

    # Find range for binary search
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2

    # Binary search in range [i/2, min(i, n-1)]
    return binary_search_range(arr, target, i // 2, min(i, len(arr) - 1))

def binary_search_range(arr, target, left, right):
    """Binary search in specified range."""
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**Time:** O(log n)
**Use case:** Infinite or unbounded arrays, when you don't know the size

---

## Advanced Search Patterns

### 1. Search in Rotated Sorted Array

```python
def search_rotated(nums, target):
    """
    Search in rotated sorted array.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

### 2. Find Peak Element

```python
def find_peak(nums):
    """
    Find any peak element in array.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1  # Peak is on right
        else:
            right = mid  # Peak is on left or at mid

    return left
```

### 3. Search 2D Matrix

```python
def search_matrix(matrix, target):
    """
    Search in sorted 2D matrix.
    Time: O(log(m*n)), Space: O(1)
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        # Convert 1D index to 2D
        row, col = mid // n, mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
```

### 4. Ternary Search

Find maximum/minimum of unimodal function.

```python
def ternary_search(f, left, right, epsilon=1e-9):
    """
    Find maximum of unimodal function.
    Time: O(log₃ n), Space: O(1)
    """
    while right - left > epsilon:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3

        if f(mid1) < f(mid2):
            left = mid1
        else:
            right = mid2

    return (left + right) / 2
```

---

## Summary

**Key Concepts:**

1. **Linear Search**: O(n), works on unsorted data
2. **Binary Search**: O(log n), requires sorted data
3. **Binary Search Variations**: Handle duplicates, find boundaries
4. **Binary Search Templates**: Three main templates for different scenarios
5. **Binary Search on Answer**: Search solution space, not just arrays
6. **Other Searches**: Jump, interpolation, exponential for specific cases

**When to Use Binary Search:**
- Data is sorted (or can be viewed as sorted)
- Need O(log n) performance
- Can define monotonic property
- Random access available

**Binary Search Checklist:**
- [ ] Is data sorted?
- [ ] Can eliminate half each iteration?
- [ ] Using correct template?
- [ ] Handling overflow (mid calculation)?
- [ ] Avoiding infinite loops?
- [ ] Post-processing if needed?

**Most Important:**
- Master standard binary search
- Learn the three templates
- Practice "binary search on answer"
- Recognize when to use binary search

Binary search is fundamental - practice until it becomes second nature!
