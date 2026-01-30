# Chapter 38: Sorting - Theory

## Table of Contents
1. [Introduction to Sorting](#introduction-to-sorting)
2. [Sorting Properties](#sorting-properties)
3. [Simple Sorting Algorithms](#simple-sorting-algorithms)
4. [Efficient Sorting Algorithms](#efficient-sorting-algorithms)
5. [Non-Comparison Sorting](#non-comparison-sorting)
6. [Python's Timsort](#pythons-timsort)
7. [Comparison Table](#comparison-table)
8. [When to Use Each Algorithm](#when-to-use-each-algorithm)

---

## Introduction to Sorting

**Sorting** is the process of arranging elements in a specific order (usually ascending or descending). It's one of the most studied problems in computer science.

### Why Sorting Matters

1. **Enables Binary Search**: Sorted data allows O(log n) search
2. **Data Organization**: Makes data more readable and analyzable
3. **Algorithm Building Block**: Many algorithms require sorted input
4. **Database Operations**: Essential for query optimization
5. **Interview Staple**: Frequently tested in coding interviews

### Classification of Sorting Algorithms

**By Time Complexity:**
- **O(n²)**: Bubble, Selection, Insertion
- **O(n log n)**: Merge, Quick, Heap
- **O(n)**: Counting, Radix, Bucket (under specific conditions)

**By Space Complexity:**
- **O(1)** - In-place: Bubble, Selection, Insertion, Quick, Heap
- **O(n)** - Not in-place: Merge, Counting, Radix, Bucket

**By Stability:**
- **Stable**: Bubble, Insertion, Merge, Counting, Radix, Bucket, Timsort
- **Unstable**: Selection, Quick, Heap

---

## Sorting Properties

### 1. Stability

A sorting algorithm is **stable** if it preserves the relative order of equal elements.

**Example:**
```
Input: [(Alice, 25), (Bob, 20), (Charlie, 25)]
Sort by age (stable):   [(Bob, 20), (Alice, 25), (Charlie, 25)]
Sort by age (unstable): [(Bob, 20), (Charlie, 25), (Alice, 25)]
```

**Why it matters:**
- Multi-key sorting (sort by age, then by name)
- Preserving original order for equal keys
- Required in many real-world applications

### 2. In-Place Sorting

An algorithm is **in-place** if it uses O(1) extra space (excluding input).

**In-place:** Quick Sort, Heap Sort, Insertion Sort
**Not in-place:** Merge Sort (uses O(n) extra space)

### 3. Adaptive

An algorithm is **adaptive** if it performs better on partially sorted data.

**Adaptive:** Insertion Sort, Bubble Sort, Timsort
**Non-adaptive:** Selection Sort, Heap Sort, Merge Sort

### 4. Online

An algorithm is **online** if it can sort data as it arrives.

**Online:** Insertion Sort
**Offline:** Most others (need all data upfront)

---

## Simple Sorting Algorithms

### 1. Bubble Sort

**Idea:** Repeatedly swap adjacent elements if they're in wrong order.

**Algorithm:**
1. Compare adjacent elements
2. Swap if they're in wrong order
3. After each pass, largest element "bubbles" to the end
4. Repeat for n-1 passes

**Visualization:**
```
Pass 1: [5, 2, 8, 1, 9]
        [2, 5, 8, 1, 9]  (swap 5,2)
        [2, 5, 1, 8, 9]  (swap 8,1)
        [2, 5, 1, 8, 9]  (9 in place)

Pass 2: [2, 1, 5, 8, 9]  (swap 5,1)
        [2, 1, 5, 8, 9]  (8 in place)

Pass 3: [1, 2, 5, 8, 9]  (swap 2,1)
        [1, 2, 5, 8, 9]  (sorted!)
```

**Implementation:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Optimization: stop if already sorted
            break
    return arr
```

**Complexity:**
- **Time:** O(n²) worst/average, O(n) best (with optimization)
- **Space:** O(1)
- **Stable:** Yes
- **Adaptive:** Yes (with early termination)

**When to use:**
- Educational purposes only
- Very small datasets (n < 10)
- Nearly sorted data with early termination

### 2. Selection Sort

**Idea:** Repeatedly find minimum element and place it at the beginning.

**Algorithm:**
1. Find minimum in unsorted portion
2. Swap with first element of unsorted portion
3. Move boundary of sorted portion
4. Repeat until array is sorted

**Visualization:**
```
[5, 2, 8, 1, 9]
 ^           ^  min=1, swap with 5
[1, 2, 8, 5, 9]
    ^     ^     min=2, already in place
[1, 2, 8, 5, 9]
       ^  ^     min=5, swap with 8
[1, 2, 5, 8, 9]
          ^  ^  min=8, already in place
[1, 2, 5, 8, 9] sorted!
```

**Implementation:**
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

**Complexity:**
- **Time:** O(n²) all cases
- **Space:** O(1)
- **Stable:** No (can be made stable with extra space)
- **Adaptive:** No

**When to use:**
- Small datasets
- When memory writes are expensive (fewer swaps than bubble sort)
- When you need to minimize number of swaps

### 3. Insertion Sort

**Idea:** Build sorted array one element at a time by inserting each element into its correct position.

**Algorithm:**
1. Start with first element (considered sorted)
2. Take next element
3. Compare with elements in sorted portion (right to left)
4. Shift larger elements to the right
5. Insert element at correct position
6. Repeat for all elements

**Visualization:**
```
[5, 2, 8, 1, 9]
[5] 2, 8, 1, 9     (5 is sorted)
[2, 5] 8, 1, 9     (insert 2 before 5)
[2, 5, 8] 1, 9     (8 already in place)
[1, 2, 5, 8] 9     (insert 1 at start)
[1, 2, 5, 8, 9]    (9 already in place)
```

**Implementation:**
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

**Complexity:**
- **Time:** O(n²) worst/average, O(n) best
- **Space:** O(1)
- **Stable:** Yes
- **Adaptive:** Yes

**When to use:**
- Small datasets (n < 50)
- Nearly sorted data (very efficient!)
- Online sorting (data arrives one at a time)
- As subroutine in hybrid algorithms (Timsort uses it)

---

## Efficient Sorting Algorithms

### 4. Merge Sort

**Idea:** Divide array into halves, recursively sort them, then merge sorted halves.

**Algorithm (Divide and Conquer):**
1. **Divide:** Split array into two halves
2. **Conquer:** Recursively sort each half
3. **Combine:** Merge two sorted halves

**Visualization:**
```
[5, 2, 8, 1, 9, 3]
      /        \
[5, 2, 8]   [1, 9, 3]     Divide
  /   \       /   \
[5] [2, 8]  [1] [9, 3]    Divide
     / \         / \
    [2] [8]     [9] [3]   Base case

Merge back:
[2, 8]          [3, 9]    Merge
[2, 5, 8]       [1, 3, 9] Merge
[1, 2, 3, 5, 8, 9]        Final merge
```

**Implementation:**
```python
def merge_sort(arr):
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

    # Merge two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Complexity:**
- **Time:** O(n log n) all cases
- **Space:** O(n)
- **Stable:** Yes
- **Adaptive:** No

**When to use:**
- Need guaranteed O(n log n) performance
- Stability is required
- Sorting linked lists (no random access needed)
- External sorting (sorting data that doesn't fit in memory)

### 5. Quick Sort

**Idea:** Pick a pivot, partition array so elements smaller than pivot are on left, larger on right, then recursively sort partitions.

**Algorithm:**
1. Choose a pivot element
2. Partition: rearrange so all smaller elements are before pivot, larger after
3. Recursively sort left and right partitions

**Visualization:**
```
[5, 2, 8, 1, 9, 3]  pivot=3
[2, 1] 3 [5, 8, 9]  partition around 3

[2, 1]  pivot=1
[1] 2               left sorted

[5, 8, 9]  pivot=9
[5, 8] 9            right sorted

[1, 2, 3, 5, 8, 9]  final result
```

**Implementation:**
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# In-place version (more efficient)
def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

**Complexity:**
- **Time:** O(n log n) average, O(n²) worst
- **Space:** O(log n) for recursion stack
- **Stable:** No (standard version)
- **Adaptive:** No

**Pivot Selection Strategies:**
- **First/Last element:** Simple but bad for sorted data
- **Random:** Good average case
- **Median-of-three:** Pick median of first, middle, last
- **Median-of-medians:** Guarantees O(n log n) but slower in practice

**When to use:**
- General-purpose sorting (fast average case)
- In-place sorting needed
- Cache-friendly (good locality of reference)
- Not when worst-case O(n log n) is required

### 6. Heap Sort

**Idea:** Build a max heap, then repeatedly extract maximum element.

**Algorithm:**
1. Build max heap from array
2. Swap root (maximum) with last element
3. Reduce heap size by 1
4. Heapify root
5. Repeat until heap size is 1

**Visualization:**
```
[5, 2, 8, 1, 9, 3]

Build max heap:
        9
      /   \
     5     8
    / \   /
   1   2 3

Extract max (9):
[8, 5, 3, 1, 2] | 9

Extract max (8):
[5, 2, 3, 1] | 8, 9

Continue until sorted:
[1, 2, 3, 5, 8, 9]
```

**Implementation:**
```python
def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)

    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

**Complexity:**
- **Time:** O(n log n) all cases
- **Space:** O(1)
- **Stable:** No
- **Adaptive:** No

**When to use:**
- Guaranteed O(n log n) with O(1) space
- When you need in-place sorting
- Embedded systems with limited memory
- Not when stability is required

---

## Non-Comparison Sorting

These algorithms don't compare elements; instead, they exploit properties of the data.

### 7. Counting Sort

**Idea:** Count occurrences of each value, then reconstruct sorted array.

**Requirements:**
- Elements are non-negative integers
- Range of values (k) is not too large

**Algorithm:**
1. Find min and max values
2. Create count array of size (max - min + 1)
3. Count occurrences of each value
4. Calculate cumulative counts
5. Place elements in sorted order

**Visualization:**
```
Input: [2, 5, 2, 8, 1, 2]
Range: 1 to 8

Count array:
Index: 1  2  3  4  5  6  7  8
Count: 1  3  0  0  1  0  0  1

Cumulative:
Index: 1  2  3  4  5  6  7  8
Count: 1  4  4  4  5  5  5  6

Output: [1, 2, 2, 2, 5, 8]
```

**Implementation:**
```python
def counting_sort(arr):
    if not arr:
        return arr

    # Find range
    min_val, max_val = min(arr), max(arr)
    range_size = max_val - min_val + 1

    # Count occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1

    # Reconstruct sorted array
    result = []
    for i in range(range_size):
        result.extend([i + min_val] * count[i])

    return result
```

**Complexity:**
- **Time:** O(n + k) where k is range
- **Space:** O(k)
- **Stable:** Yes (with careful implementation)
- **Adaptive:** No

**When to use:**
- Small range of integers (k = O(n))
- Need linear time sorting
- Stability is required
- Not when range is too large

### 8. Radix Sort

**Idea:** Sort numbers digit by digit, starting from least significant digit.

**Algorithm:**
1. Find maximum number to know number of digits
2. For each digit position (LSD to MSD):
   - Use counting sort on that digit
3. Array becomes sorted after processing all digits

**Visualization:**
```
[170, 45, 75, 90, 802, 24, 2, 66]

Sort by 1s place:
[170, 90, 802, 2, 24, 45, 75, 66]

Sort by 10s place:
[802, 2, 24, 45, 66, 170, 75, 90]

Sort by 100s place:
[2, 24, 45, 66, 75, 90, 170, 802]
```

**Implementation:**
```python
def radix_sort(arr):
    if not arr:
        return arr

    # Find maximum number to know number of digits
    max_num = max(arr)

    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of digits
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # Copy to original array
    for i in range(n):
        arr[i] = output[i]
```

**Complexity:**
- **Time:** O(d · (n + k)) where d is digits, k is base (usually 10)
- **Space:** O(n + k)
- **Stable:** Yes
- **Adaptive:** No

**When to use:**
- Fixed-length integers
- Large number of elements
- Need linear time complexity
- Not for floating-point numbers or variable-length strings

### 9. Bucket Sort

**Idea:** Distribute elements into buckets, sort buckets individually, then concatenate.

**Algorithm:**
1. Create n empty buckets
2. Distribute elements into buckets based on range
3. Sort each bucket individually (using insertion sort)
4. Concatenate all buckets

**Visualization:**
```
Input: [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
Range: [0, 1)

Bucket 0 [0.0-0.2): []
Bucket 1 [0.2-0.4): [0.23, 0.25, 0.32]
Bucket 2 [0.4-0.6): [0.42, 0.47, 0.51, 0.52]
Bucket 3 [0.6-0.8): []
Bucket 4 [0.8-1.0): []

After sorting buckets:
[0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]
```

**Implementation:**
```python
def bucket_sort(arr):
    if not arr:
        return arr

    # Create buckets
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Distribute elements into buckets
    min_val, max_val = min(arr), max(arr)
    range_size = max_val - min_val

    for num in arr:
        if range_size == 0:
            idx = 0
        else:
            idx = int((num - min_val) / range_size * (n - 1))
        buckets[idx].append(num)

    # Sort each bucket and concatenate
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))  # Or use insertion sort

    return result
```

**Complexity:**
- **Time:** O(n + k) average, O(n²) worst
- **Space:** O(n + k)
- **Stable:** Yes
- **Adaptive:** Yes

**When to use:**
- Uniformly distributed data
- Floating-point numbers
- Data can be partitioned into ranges
- Not when data has many duplicates or is non-uniform

---

## Python's Timsort

**Timsort** is Python's built-in sorting algorithm (used by `sorted()` and `.sort()`).

### What is Timsort?

A **hybrid** sorting algorithm combining:
- **Merge Sort**: For divide and conquer
- **Insertion Sort**: For small runs and nearly sorted data

Designed by Tim Peters in 2002 for Python.

### Key Ideas

1. **Identify runs**: Find sequences that are already sorted
2. **Merge runs**: Use merge sort to combine runs
3. **Galloping mode**: Optimize merging when one array has many consecutive elements
4. **Minimum run size**: Use insertion sort for runs smaller than minrun (32-64)

### Why Timsort is Amazing

**Advantages:**
- O(n) best case for sorted data
- O(n log n) worst case
- Stable
- Adaptive (exploits existing order)
- Very fast in practice

**Performance:**
```python
# Near-sorted data: O(n)
arr = list(range(1000000))
sorted(arr)  # Very fast!

# Random data: O(n log n)
arr = [random.randint(1, 1000) for _ in range(1000000)]
sorted(arr)  # Still fast!

# Reverse sorted: O(n)
arr = list(range(1000000, 0, -1))
sorted(arr)  # Fast (recognizes reverse runs)!
```

### Using Python's Sort

```python
# sorted() - returns new list
nums = [3, 1, 4, 1, 5]
result = sorted(nums)  # [1, 1, 3, 4, 5]

# list.sort() - sorts in-place
nums.sort()  # nums is now [1, 1, 3, 4, 5]

# Custom key function
words = ['banana', 'apple', 'cherry']
sorted(words, key=len)  # ['apple', 'banana', 'cherry']

# Reverse
sorted(nums, reverse=True)

# Multi-key sorting
students = [('Alice', 25), ('Bob', 20), ('Charlie', 25)]
sorted(students, key=lambda x: (x[1], x[0]))  # Sort by age, then name

# Using itemgetter (faster)
from operator import itemgetter
sorted(students, key=itemgetter(1, 0))
```

---

## Comparison Table

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Stable | In-Place |
|-----------|-------------|------------|--------------|-------|--------|----------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes | No |
| Radix | O(d·n) | O(d·n) | O(d·n) | O(n+k) | Yes | No |
| Bucket | O(n+k) | O(n+k) | O(n²) | O(n) | Yes | No |
| Timsort | O(n) | O(n log n) | O(n log n) | O(n) | Yes | No |

---

## When to Use Each Algorithm

### Decision Tree

```
Is data small (n < 50)?
├─ Yes → Insertion Sort
└─ No → Continue

Is data nearly sorted?
├─ Yes → Insertion Sort or Timsort
└─ No → Continue

Are elements small non-negative integers with small range?
├─ Yes → Counting Sort
└─ No → Continue

Are elements fixed-length integers?
├─ Yes → Radix Sort
└─ No → Continue

Is stability required?
├─ Yes → Merge Sort or Timsort
└─ No → Continue

Is space limited (need in-place)?
├─ Yes → Quick Sort or Heap Sort
└─ No → Continue

General purpose?
└─ Use Python's built-in sort (Timsort)
```

### Specific Use Cases

**Insertion Sort:**
- n < 50
- Nearly sorted data
- Online sorting
- Part of hybrid algorithm

**Merge Sort:**
- Need guaranteed O(n log n)
- Stability required
- Linked lists
- External sorting

**Quick Sort:**
- General purpose (fast average case)
- In-place required
- Cache-friendly sorting

**Heap Sort:**
- Guaranteed O(n log n) + O(1) space
- Embedded systems
- Priority queue applications

**Counting Sort:**
- Small integer range
- Need linear time
- Stability required

**Radix Sort:**
- Fixed-length integers
- Large datasets
- Multiple keys (strings)

**Bucket Sort:**
- Uniformly distributed floats
- Data naturally partitions

**Timsort (Python's default):**
- General purpose
- Real-world data
- Need both speed and stability

---

## Summary

**Key Takeaways:**

1. **No single best algorithm** - choose based on data characteristics
2. **Comparison sorts** can't do better than O(n log n) average
3. **Non-comparison sorts** can achieve O(n) with restrictions
4. **Stability matters** for multi-key sorting
5. **Python's Timsort** is excellent for general use
6. **Small data** → Insertion Sort
7. **Large data** → Merge/Quick/Heap/Timsort

**Interview Essentials:**
- Understand O(n²), O(n log n), and O(n) algorithms
- Know when each is appropriate
- Implement Merge Sort and Quick Sort from scratch
- Understand stability and in-place sorting
- Master Python's built-in sort with key functions

Practice implementing these algorithms to understand their mechanics deeply!
