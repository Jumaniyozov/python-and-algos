# Chapter 38: Sorting - Examples

## Table of Contents
1. [Simple Sorting Algorithms](#simple-sorting-algorithms)
2. [Efficient Sorting Algorithms](#efficient-sorting-algorithms)
3. [Non-Comparison Sorts](#non-comparison-sorts)
4. [Python Built-in Sorting](#python-built-in-sorting)
5. [Custom Comparisons](#custom-comparisons)

---

## Simple Sorting Algorithms

### Example 1: Bubble Sort

```python
def bubble_sort(arr):
    """
    Sort array using bubble sort.
    Time: O(n²), Space: O(1)
    Stable: Yes, In-place: Yes
    """
    n = len(arr)

    # Outer loop: n-1 passes
    for i in range(n):
        swapped = False  # Optimization flag

        # Inner loop: compare adjacent elements
        # Last i elements are already sorted
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps, array is sorted
        if not swapped:
            break

    return arr

# Test
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))  # [11, 12, 22, 25, 34, 64, 90]

# Best case: already sorted
arr = [1, 2, 3, 4, 5]
print(bubble_sort(arr))  # O(n) with optimization
```

**Trace:**
```
Pass 1: [64, 34, 25, 12, 22, 11, 90]
        [34, 64, 25, 12, 22, 11, 90]  swap 64,34
        [34, 25, 64, 12, 22, 11, 90]  swap 64,25
        [34, 25, 12, 64, 22, 11, 90]  swap 64,12
        [34, 25, 12, 22, 64, 11, 90]  swap 64,22
        [34, 25, 12, 22, 11, 64, 90]  swap 64,11
        90 is in final position

Pass 2: [25, 34, 12, 22, 11, 64, 90]
        ... (64 bubbles to second-last position)

Continue until sorted...
```

---

### Example 2: Selection Sort

```python
def selection_sort(arr):
    """
    Sort array using selection sort.
    Time: O(n²), Space: O(1)
    Stable: No, In-place: Yes
    """
    n = len(arr)

    # Move boundary of unsorted part
    for i in range(n):
        # Find minimum in unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap minimum with first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Test
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # [11, 12, 22, 25, 64]
```

**Trace:**
```
[64, 25, 12, 22, 11]
 ^               ^   min=11, swap
[11, 25, 12, 22, 64]
     ^       ^       min=12, swap
[11, 12, 25, 22, 64]
         ^   ^       min=22, swap
[11, 12, 22, 25, 64]
             ^  ^    already in order
[11, 12, 22, 25, 64]
```

---

### Example 3: Insertion Sort

```python
def insertion_sort(arr):
    """
    Sort array using insertion sort.
    Time: O(n²) worst, O(n) best, Space: O(1)
    Stable: Yes, In-place: Yes, Adaptive: Yes
    """
    # Start from second element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key at correct position
        arr[j + 1] = key

    return arr

# Test
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))  # [5, 6, 11, 12, 13]

# Best for nearly sorted data
arr = [1, 2, 3, 5, 4]
print(insertion_sort(arr))  # Very fast!
```

**Trace:**
```
[12, 11, 13, 5, 6]
[12] 11, 13, 5, 6      (12 is sorted)
[11, 12] 13, 5, 6      (insert 11 before 12)
[11, 12, 13] 5, 6      (13 already in place)
[5, 11, 12, 13] 6      (insert 5 at start)
[5, 6, 11, 12, 13]     (insert 6 after 5)
```

**Binary Insertion Sort** (optimization):
```python
def binary_insertion_sort(arr):
    """
    Use binary search to find insertion position.
    Reduces comparisons but not shifts.
    Time: O(n²), Space: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]

        # Binary search to find position
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1

        # Shift elements and insert
        j = i - 1
        while j >= left:
            arr[j + 1] = arr[j]
            j -= 1
        arr[left] = key

    return arr
```

---

## Efficient Sorting Algorithms

### Example 4: Merge Sort

```python
def merge_sort(arr):
    """
    Sort array using merge sort.
    Time: O(n log n), Space: O(n)
    Stable: Yes, In-place: No
    """
    # Base case: array of 0 or 1 element is sorted
    if len(arr) <= 1:
        return arr

    # Divide: split array in half
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer: merge sorted halves
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0

    # Compare elements from left and right
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= for stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Test
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  # [3, 9, 10, 27, 38, 43, 82]
```

**In-place Merge Sort** (space-optimized):
```python
def merge_sort_inplace(arr, left=0, right=None):
    """
    In-place merge sort.
    Still O(n) space for merge operation.
    """
    if right is None:
        right = len(arr) - 1

    if left < right:
        mid = (left + right) // 2
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        merge_inplace(arr, left, mid, right)

    return arr

def merge_inplace(arr, left, mid, right):
    """Merge two sorted portions of array."""
    # Create temp arrays
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1
```

---

### Example 5: Quick Sort

```python
def quick_sort(arr):
    """
    Sort array using quick sort (Pythonic version).
    Time: O(n log n) average, O(n²) worst
    Space: O(n) for list creation, O(log n) recursion
    Stable: No, In-place: No (this version)
    """
    if len(arr) <= 1:
        return arr

    # Choose pivot (middle element)
    pivot = arr[len(arr) // 2]

    # Partition into three parts
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort and combine
    return quick_sort(left) + middle + quick_sort(right)

# Test
arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr))  # [1, 5, 7, 8, 9, 10]
```

**In-place Quick Sort** (Hoare partition):
```python
def quick_sort_inplace(arr, low=0, high=None):
    """
    In-place quick sort using Hoare partition.
    Time: O(n log n) average, O(n²) worst
    Space: O(log n) recursion
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Partition and get pivot index
        pivot_idx = partition(arr, low, high)

        # Recursively sort left and right
        quick_sort_inplace(arr, low, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, high)

    return arr

def partition(arr, low, high):
    """
    Lomuto partition scheme.
    Places pivot at correct position.
    """
    # Choose last element as pivot
    pivot = arr[high]

    # Index of smaller element
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot at correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test
arr = [10, 7, 8, 9, 1, 5]
print(quick_sort_inplace(arr))  # [1, 5, 7, 8, 9, 10]
```

**Randomized Quick Sort** (avoids worst case):
```python
import random

def randomized_quick_sort(arr, low=0, high=None):
    """Quick sort with random pivot selection."""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot_idx - 1)
        randomized_quick_sort(arr, pivot_idx + 1, high)

    return arr

def randomized_partition(arr, low, high):
    """Randomly select pivot and partition."""
    # Random pivot
    random_idx = random.randint(low, high)
    arr[random_idx], arr[high] = arr[high], arr[random_idx]

    return partition(arr, low, high)
```

---

### Example 6: Heap Sort

```python
def heap_sort(arr):
    """
    Sort array using heap sort.
    Time: O(n log n), Space: O(1)
    Stable: No, In-place: Yes
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify reduced heap
        heapify(arr, i, 0)

    return arr

def heapify(arr, n, i):
    """
    Heapify subtree rooted at index i.
    n is size of heap.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify affected subtree
        heapify(arr, n, largest)

# Test
arr = [12, 11, 13, 5, 6, 7]
print(heap_sort(arr))  # [5, 6, 7, 11, 12, 13]
```

**Using Python's heapq** (easier):
```python
import heapq

def heap_sort_with_heapq(arr):
    """Sort using Python's heapq module."""
    return [heapq.heappop(heap) for heap in [arr.copy()]
            for _ in range(len(arr))]

# Or simply:
def heap_sort_simple(arr):
    """Transform to heap, then extract all."""
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]
```

---

## Non-Comparison Sorts

### Example 7: Counting Sort

```python
def counting_sort(arr):
    """
    Sort array of non-negative integers.
    Time: O(n + k), Space: O(k)
    where k is range of input.
    Stable: Yes, In-place: No
    """
    if not arr:
        return arr

    # Find range
    min_val = min(arr)
    max_val = max(arr)
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

# Test
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))  # [1, 2, 2, 3, 3, 4, 8]
```

**Stable Counting Sort** (preserves order):
```python
def counting_sort_stable(arr):
    """Stable version using cumulative counts."""
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    # Count occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1

    # Cumulative count
    for i in range(1, range_size):
        count[i] += count[i - 1]

    # Build output array (backwards for stability)
    output = [0] * len(arr)
    for num in reversed(arr):
        idx = count[num - min_val] - 1
        output[idx] = num
        count[num - min_val] -= 1

    return output
```

---

### Example 8: Radix Sort

```python
def radix_sort(arr):
    """
    Sort array of non-negative integers using radix sort.
    Time: O(d * (n + k)), Space: O(n + k)
    where d is number of digits, k is base (10)
    Stable: Yes, In-place: No
    """
    if not arr:
        return arr

    # Find maximum to know number of digits
    max_num = max(arr)

    # Do counting sort for every digit
    exp = 1  # 10^0, 10^1, 10^2, ...
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr

def counting_sort_by_digit(arr, exp):
    """Counting sort based on digit represented by exp."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 0-9 digits

    # Count occurrences of digits
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (backwards for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # Copy to original array
    for i in range(n):
        arr[i] = output[i]

# Test
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))  # [2, 24, 45, 66, 75, 90, 170, 802]
```

---

### Example 9: Bucket Sort

```python
def bucket_sort(arr):
    """
    Sort array of floats in range [0, 1).
    Time: O(n + k) average, O(n²) worst
    Space: O(n)
    Stable: Yes
    """
    if not arr:
        return arr

    # Create buckets
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Distribute elements into buckets
    for num in arr:
        idx = int(num * n)
        if idx == n:  # Handle edge case: num = 1.0
            idx = n - 1
        buckets[idx].append(num)

    # Sort each bucket and concatenate
    result = []
    for bucket in buckets:
        # Use insertion sort for small buckets
        result.extend(insertion_sort(bucket))

    return result

# Test
arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print(bucket_sort(arr))  # [0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]
```

**General Bucket Sort** (any range):
```python
def bucket_sort_general(arr):
    """Bucket sort for any numeric range."""
    if not arr:
        return arr

    # Find range
    min_val = min(arr)
    max_val = max(arr)

    # Create buckets
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Distribute elements
    range_size = max_val - min_val
    for num in arr:
        if range_size == 0:
            idx = 0
        else:
            idx = int((num - min_val) / range_size * (n - 1))
        buckets[idx].append(num)

    # Sort and concatenate
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))

    return result
```

---

## Python Built-in Sorting

### Example 10: Using sorted() and .sort()

```python
# sorted() - returns new sorted list
nums = [3, 1, 4, 1, 5, 9, 2, 6]
result = sorted(nums)
print(result)  # [1, 1, 2, 3, 4, 5, 6, 9]
print(nums)    # [3, 1, 4, 1, 5, 9, 2, 6] (unchanged)

# list.sort() - sorts in-place
nums.sort()
print(nums)    # [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse sorting
nums = [3, 1, 4, 1, 5]
sorted(nums, reverse=True)  # [5, 4, 3, 1, 1]

# Sort by length
words = ['banana', 'apple', 'cherry', 'date']
sorted(words, key=len)  # ['date', 'apple', 'banana', 'cherry']

# Sort by last character
sorted(words, key=lambda x: x[-1])  # ['banana', 'apple', 'date', 'cherry']

# Sort by multiple criteria
students = [
    ('Alice', 25, 85),
    ('Bob', 20, 90),
    ('Charlie', 25, 80),
    ('David', 20, 85)
]

# Sort by age, then score
sorted(students, key=lambda x: (x[1], x[2]))
# [('David', 20, 85), ('Bob', 20, 90), ('Charlie', 25, 80), ('Alice', 25, 85)]

# Using operator.itemgetter (faster)
from operator import itemgetter
sorted(students, key=itemgetter(1, 2))
```

---

## Custom Comparisons

### Example 11: Custom Key Functions

```python
# Sort strings by custom criteria
def custom_sort_strings():
    """Sort strings by length, then alphabetically."""
    words = ['banana', 'apple', 'cherry', 'date', 'fig']

    # By length, then alphabetically
    result = sorted(words, key=lambda x: (len(x), x))
    print(result)  # ['fig', 'date', 'apple', 'banana', 'cherry']

# Sort by absolute value
def sort_by_absolute():
    """Sort integers by absolute value."""
    nums = [-5, -2, 3, -8, 1, 4]
    result = sorted(nums, key=abs)
    print(result)  # [1, -2, 3, 4, -5, -8]

# Sort dictionaries
def sort_dictionaries():
    """Sort list of dictionaries."""
    people = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 20},
        {'name': 'Charlie', 'age': 25}
    ]

    # Sort by age
    sorted(people, key=lambda x: x['age'])

    # Sort by age, then name
    sorted(people, key=lambda x: (x['age'], x['name']))

# Custom comparison class
from functools import cmp_to_key

def custom_comparator():
    """Use custom comparison function."""
    def compare(a, b):
        """Custom comparison: odd numbers before even."""
        if a % 2 != b % 2:
            return -1 if a % 2 == 1 else 1
        return a - b

    nums = [1, 2, 3, 4, 5, 6]
    result = sorted(nums, key=cmp_to_key(compare))
    print(result)  # [1, 3, 5, 2, 4, 6]

# Sort by frequency
from collections import Counter

def sort_by_frequency(arr):
    """Sort elements by frequency."""
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))

arr = [1, 1, 2, 2, 2, 3]
print(sort_by_frequency(arr))  # [2, 2, 2, 1, 1, 3]
```

### Example 12: Sorting Complex Data

```python
# Sort 2D points by distance from origin
def sort_points_by_distance():
    """Sort points by distance from origin."""
    points = [(1, 2), (3, 1), (0, 0), (2, 2)]

    def distance(point):
        return point[0]**2 + point[1]**2

    result = sorted(points, key=distance)
    print(result)  # [(0, 0), (1, 2), (3, 1), (2, 2)]

# Sort intervals
def sort_intervals():
    """Sort intervals by start time, then end time."""
    intervals = [[1, 4], [3, 5], [1, 3], [2, 6]]
    result = sorted(intervals, key=lambda x: (x[0], x[1]))
    print(result)  # [[1, 3], [1, 4], [2, 6], [3, 5]]

# Sort linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sort_linked_list(head):
    """Sort linked list using merge sort."""
    if not head or not head.next:
        return head

    # Find middle
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Split into two halves
    prev.next = None

    # Recursively sort
    left = sort_linked_list(head)
    right = sort_linked_list(slow)

    # Merge sorted halves
    return merge_lists(left, right)

def merge_lists(l1, l2):
    """Merge two sorted linked lists."""
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2
    return dummy.next
```

---

## Performance Comparison

```python
import time
import random

def compare_sorting_algorithms():
    """Compare performance of different sorting algorithms."""
    sizes = [100, 1000, 5000]

    for n in sizes:
        # Random data
        arr = [random.randint(1, 1000) for _ in range(n)]

        print(f"\nArray size: {n}")

        # Bubble Sort (only for small n)
        if n <= 1000:
            test_arr = arr.copy()
            start = time.time()
            bubble_sort(test_arr)
            print(f"Bubble Sort: {time.time() - start:.4f}s")

        # Insertion Sort
        test_arr = arr.copy()
        start = time.time()
        insertion_sort(test_arr)
        print(f"Insertion Sort: {time.time() - start:.4f}s")

        # Merge Sort
        test_arr = arr.copy()
        start = time.time()
        merge_sort(test_arr)
        print(f"Merge Sort: {time.time() - start:.4f}s")

        # Quick Sort
        test_arr = arr.copy()
        start = time.time()
        quick_sort(test_arr)
        print(f"Quick Sort: {time.time() - start:.4f}s")

        # Python's Timsort
        test_arr = arr.copy()
        start = time.time()
        sorted(test_arr)
        print(f"Timsort (built-in): {time.time() - start:.4f}s")
```

---

## Summary

**Key Implementation Points:**

1. **Bubble Sort**: Simple but slow, use only for education
2. **Insertion Sort**: Best for small or nearly sorted arrays
3. **Merge Sort**: Stable, guaranteed O(n log n), uses extra space
4. **Quick Sort**: Fast average case, in-place, but unstable
5. **Heap Sort**: Guaranteed O(n log n), in-place, but unstable
6. **Counting Sort**: Linear time for small integer ranges
7. **Radix Sort**: Linear time for fixed-length integers
8. **Bucket Sort**: Good for uniformly distributed data
9. **Python's Timsort**: Best general-purpose choice

**In Practice:**
- Use Python's `sorted()` or `.sort()` for most cases
- Implement custom algorithms for learning or special requirements
- Choose algorithm based on data characteristics
- Consider stability, space, and time requirements

Practice implementing these algorithms to understand their mechanics!
