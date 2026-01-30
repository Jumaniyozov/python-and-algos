# Heaps Theory

## Table of Contents

1. [Heap Fundamentals](#heap-fundamentals)
2. [Binary Heap Structure](#binary-heap-structure)
3. [Heap Operations](#heap-operations)
4. [Python heapq Module](#python-heapq-module)
5. [Priority Queue](#priority-queue)
6. [Heap Sort](#heap-sort)
7. [Common Patterns](#common-patterns)

---

## Heap Fundamentals

### What is a Heap?

A **heap** is a specialized tree-based data structure that satisfies the **heap property**. It's a complete binary tree where each parent node has a specific ordering relationship with its children.

### Heap Property

**Min Heap Property:**
- Every parent node is **less than or equal to** its children
- The **minimum** element is at the root
- For any node i: `parent(i) ≤ left_child(i)` and `parent(i) ≤ right_child(i)`

```
Min Heap Example:
       1
      / \
     3   2
    / \ / \
   7  5 8  6
```

**Max Heap Property:**
- Every parent node is **greater than or equal to** its children
- The **maximum** element is at the root
- For any node i: `parent(i) ≥ left_child(i)` and `parent(i) ≥ right_child(i)`

```
Max Heap Example:
       9
      / \
     7   8
    / \ / \
   3  5 4  6
```

### Complete Binary Tree

A heap is a **complete binary tree**, meaning:
1. All levels are fully filled except possibly the last level
2. The last level is filled from left to right
3. Height is always O(log n) for n nodes

**Valid Complete Binary Tree:**
```
       1
      / \
     2   3
    / \
   4   5
```

**Invalid (not complete):**
```
       1
      / \
     2   3
      \
       4    ← Gap on left
```

### Why Heaps?

| Feature | Heap | Sorted Array | BST |
|---------|------|--------------|-----|
| Find Min/Max | O(1) | O(1) | O(log n) |
| Insert | O(log n) | O(n) | O(log n) avg |
| Delete Min/Max | O(log n) | O(n) | O(log n) |
| Space | O(n) | O(n) | O(n) |
| Build | O(n) | O(n log n) | O(n log n) |

**Use heap when:**
- Need fast access to min/max element
- Frequently insert and remove extremes
- Don't need full sorting
- Implementing priority queue

---

## Binary Heap Structure

### Array Representation

Heaps are efficiently stored in arrays due to complete binary tree property.

**Index Relationships:**
```python
For node at index i:
- Parent index: (i - 1) // 2
- Left child: 2 * i + 1
- Right child: 2 * i + 2
```

**Example:**
```
Array: [1, 3, 2, 7, 5, 8, 6]
Index:  0  1  2  3  4  5  6

Tree:
       1 (i=0)
      / \
     3   2 (i=1,2)
    / \ / \
   7  5 8  6 (i=3,4,5,6)

Parent of 5 (i=4): (4-1)//2 = 1 → value 3 ✓
Left child of 3 (i=1): 2*1+1 = 3 → value 7 ✓
Right child of 3 (i=1): 2*1+2 = 4 → value 5 ✓
```

### Heap Height

For n elements:
- Height h = ⌊log₂ n⌋
- This guarantees O(log n) operations

Example:
- n = 7: h = 2
- n = 15: h = 3
- n = 1000: h = 9

---

## Heap Operations

### 1. Insert (Push)

Add element and maintain heap property by "bubbling up".

**Algorithm:**
1. Add element at end of array (next available position)
2. Compare with parent
3. If violates heap property, swap with parent
4. Repeat until heap property satisfied or reach root

**Min Heap Insert:**
```python
def insert(self, val):
    # Add to end
    self.heap.append(val)
    # Bubble up
    self._bubble_up(len(self.heap) - 1)

def _bubble_up(self, index):
    parent = (index - 1) // 2
    # If current less than parent, swap
    if index > 0 and self.heap[index] < self.heap[parent]:
        self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
        self._bubble_up(parent)
```

**Example: Insert 1 into min heap [3, 5, 7, 9, 11]**
```
Initial: [3, 5, 7, 9, 11]
         3
        / \
       5   7
      / \
     9  11

Step 1: Add 1 at end
[3, 5, 7, 9, 11, 1]
         3
        / \
       5   7
      / \ /
     9 11 1

Step 2: Compare with parent (7), swap
[3, 5, 1, 9, 11, 7]
         3
        / \
       5   1
      / \ /
     9 11 7

Step 3: Compare with parent (3), swap
[1, 5, 3, 9, 11, 7]
         1
        / \
       5   3
      / \ /
     9 11 7

Done! Heap property maintained.
```

**Time Complexity:** O(log n) - worst case bubble up to root

### 2. Extract Min/Max (Pop)

Remove root and maintain heap property by "bubbling down".

**Algorithm:**
1. Save root value (to return)
2. Replace root with last element
3. Remove last element
4. Bubble down from root:
   - Compare with both children
   - Swap with smaller child (min heap) or larger child (max heap)
   - Repeat until heap property satisfied or reach leaf

**Min Heap Extract:**
```python
def extract_min(self):
    if not self.heap:
        return None

    # Save min value
    min_val = self.heap[0]

    # Replace root with last element
    self.heap[0] = self.heap[-1]
    self.heap.pop()

    # Bubble down
    if self.heap:
        self._bubble_down(0)

    return min_val

def _bubble_down(self, index):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    # Find smallest among parent and children
    if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
        smallest = left
    if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
        smallest = right

    # Swap if needed and continue
    if smallest != index:
        self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
        self._bubble_down(smallest)
```

**Example: Extract min from [1, 3, 2, 7, 5, 8, 6]**
```
Initial:
         1
        / \
       3   2
      / \ / \
     7  5 8  6

Step 1: Save 1, replace with last (6)
         6
        / \
       3   2
      / \ /
     7  5 8

Step 2: Compare 6 with children (3, 2), swap with 2
         2
        / \
       3   6
      / \ /
     7  5 8

Step 3: Compare 6 with children (8), no swap needed

Final: [2, 3, 6, 7, 5, 8]
         2
        / \
       3   6
      / \ /
     7  5 8
```

**Time Complexity:** O(log n) - worst case bubble down to leaf

### 3. Peek

Get min/max without removing.

```python
def peek(self):
    return self.heap[0] if self.heap else None
```

**Time Complexity:** O(1)

### 4. Heapify

Convert an unsorted array into a heap.

**Algorithm:**
1. Start from last non-leaf node: `(n // 2) - 1`
2. Apply bubble_down to each node moving towards root
3. This is bottom-up heapification

**Why start from `(n // 2) - 1`?**
- Nodes from `n // 2` to `n - 1` are leaves
- Leaves are already valid heaps
- We only need to fix internal nodes

```python
def heapify(self, arr):
    self.heap = arr.copy()
    n = len(self.heap)

    # Start from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        self._bubble_down(i)
```

**Example: Heapify [7, 3, 8, 4, 1, 5, 9]**
```
Initial (as tree):
         7
        / \
       3   8
      / \ / \
     4  1 5  9

Last non-leaf: index 2 (value 8)

Step 1: Bubble down at index 2 (8)
         7
        / \
       3   5
      / \ / \
     4  1 8  9

Step 2: Bubble down at index 1 (3)
         7
        / \
       1   5
      / \ / \
     4  3 8  9

Step 3: Bubble down at index 0 (7)
         1
        / \
       3   5
      / \ / \
     4  7 8  9

Result: [1, 3, 5, 4, 7, 8, 9]
```

**Time Complexity:** O(n) - not O(n log n)!

**Why O(n)?**
- Most nodes are near leaves (require fewer swaps)
- Mathematical proof: Sum of (nodes at level h) × (distance to bottom) = O(n)

### 5. Build Heap

Two approaches:

**Approach 1: Repeated Insert - O(n log n)**
```python
def build_heap_insert(arr):
    heap = []
    for val in arr:
        insert(heap, val)  # O(log n) each
    return heap
```

**Approach 2: Heapify - O(n)**
```python
def build_heap_heapify(arr):
    heap = arr.copy()
    for i in range(len(heap) // 2 - 1, -1, -1):
        bubble_down(heap, i)
    return heap
```

**Always prefer heapify for building from existing array!**

---

## Python heapq Module

Python's `heapq` module implements a min heap.

### Core Functions

```python
import heapq

# Create empty heap
heap = []

# heappush: Add element - O(log n)
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)

# heappop: Remove and return smallest - O(log n)
min_val = heapq.heappop(heap)  # Returns 3

# heap[0]: Peek at smallest - O(1)
smallest = heap[0]  # Just access, don't pop

# heapify: Convert list to heap in-place - O(n)
arr = [7, 3, 8, 4, 1]
heapq.heapify(arr)  # arr becomes [1, 3, 8, 4, 7]

# heappushpop: Push then pop - O(log n)
# More efficient than separate push and pop
result = heapq.heappushpop(heap, 6)

# heapreplace: Pop then push - O(log n)
result = heapq.heapreplace(heap, 6)
```

### Finding K Largest/Smallest

```python
# nlargest: K largest elements - O(n log k)
arr = [7, 3, 8, 4, 1, 5, 9, 2]
largest_3 = heapq.nlargest(3, arr)  # [9, 8, 7]

# nsmallest: K smallest elements - O(n log k)
smallest_3 = heapq.nsmallest(3, arr)  # [1, 2, 3]

# With key function
people = [{'name': 'Alice', 'age': 30},
          {'name': 'Bob', 'age': 25}]
oldest = heapq.nlargest(1, people, key=lambda x: x['age'])
```

### Max Heap in Python

Python only has min heap. To simulate max heap, negate values.

```python
# Max heap by negating values
max_heap = []

# Push
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -7)

# Pop (remember to negate back)
max_val = -heapq.heappop(max_heap)  # Returns 7

# Peek
max_val = -max_heap[0]  # 5
```

### Heap with Custom Objects

```python
from dataclasses import dataclass
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any

heap = []
heapq.heappush(heap, PrioritizedItem(2, "task2"))
heapq.heappush(heap, PrioritizedItem(1, "task1"))

task = heapq.heappop(heap)  # Gets task1 (priority 1)
```

### Heap with Tuples

```python
# Tuples are compared element by element
heap = []
heapq.heappush(heap, (1, "high priority"))
heapq.heappush(heap, (5, "low priority"))
heapq.heappush(heap, (1, "also high"))  # Secondary sort by string

priority, task = heapq.heappop(heap)  # (1, "also high")
```

---

## Priority Queue

A priority queue is an abstract data type where each element has a priority. Elements are served based on priority, not insertion order.

### Implementation Using Heap

```python
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0  # For tie-breaking

    def push(self, item, priority):
        # Use counter to maintain insertion order for same priority
        heapq.heappush(self.heap, (priority, self.counter, item))
        self.counter += 1

    def pop(self):
        if self.heap:
            priority, _, item = heapq.heappop(self.heap)
            return item
        return None

    def peek(self):
        if self.heap:
            return self.heap[0][2]
        return None

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)
```

**Usage:**
```python
pq = PriorityQueue()
pq.push("task1", priority=2)
pq.push("task2", priority=1)
pq.push("task3", priority=2)

print(pq.pop())  # "task2" (priority 1)
print(pq.pop())  # "task1" (priority 2, inserted first)
print(pq.pop())  # "task3" (priority 2, inserted second)
```

### Python queue.PriorityQueue

```python
from queue import PriorityQueue

# Thread-safe priority queue
pq = PriorityQueue()

# Put items (priority, item)
pq.put((2, "task1"))
pq.put((1, "task2"))

# Get items
priority, task = pq.get()  # (1, "task2")
```

---

## Heap Sort

Heap sort uses a heap to sort an array in O(n log n) time.

### Algorithm

1. Build max heap from array - O(n)
2. Repeatedly extract max and place at end - O(n log n)

### Implementation

```python
def heap_sort(arr):
    """
    Sort array in ascending order using heap sort.
    Time: O(n log n)
    Space: O(1) in-place
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify_down(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Swap root (max) with last element
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify root with reduced size
        _heapify_down(arr, i, 0)

    return arr

def _heapify_down(arr, n, i):
    """Heapify subtree rooted at index i."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify_down(arr, n, largest)
```

**Example:**
```python
arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)
print(arr)  # [11, 12, 22, 25, 34, 64, 90]
```

### Heap Sort Properties

**Advantages:**
- O(n log n) worst case (better than quick sort's O(n²))
- O(1) space (in-place sorting)
- No recursion needed

**Disadvantages:**
- Not stable (equal elements may change relative order)
- Poor cache locality (random memory access)
- Slower than quick sort in practice

**When to use:**
- Need guaranteed O(n log n)
- Memory is limited (can't use merge sort)
- Don't need stability

---

## Common Patterns

### Pattern 1: Top K Elements

Find K largest or smallest elements.

```python
def find_k_largest(nums, k):
    """Use min heap of size k."""
    import heapq
    # Keep min heap of k largest
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)

    return heap

# Or simply:
def find_k_largest_simple(nums, k):
    return heapq.nlargest(k, nums)
```

### Pattern 2: Two Heaps (Median Finding)

Maintain two heaps to find running median.

```python
class MedianFinder:
    def __init__(self):
        self.max_heap = []  # Left half (negated for max heap)
        self.min_heap = []  # Right half

    def add_num(self, num):
        # Add to max heap first
        heapq.heappush(self.max_heap, -num)

        # Balance: ensure max of left ≤ min of right
        if self.max_heap and self.min_heap and \
           -self.max_heap[0] > self.min_heap[0]:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # Balance sizes
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
```

### Pattern 3: K-Way Merge

Merge K sorted arrays efficiently.

```python
def merge_k_sorted(arrays):
    """
    Merge k sorted arrays.
    Time: O(N log k) where N = total elements
    """
    import heapq

    heap = []
    result = []

    # Initialize heap with first element from each array
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Add next element from same array
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))

    return result
```

### Pattern 4: Scheduling with Priorities

```python
def schedule_tasks(tasks, k):
    """
    Schedule tasks with cooldown period k.
    Each task has frequency count.
    """
    from collections import Counter
    import heapq

    freq = Counter(tasks)
    max_heap = [-count for count in freq.values()]
    heapq.heapify(max_heap)

    time = 0
    while max_heap:
        temp = []
        for _ in range(k + 1):
            if max_heap:
                count = heapq.heappop(max_heap)
                if count < -1:
                    temp.append(count + 1)
            time += 1
            if not max_heap and not temp:
                break

        for count in temp:
            heapq.heappush(max_heap, count)

    return time
```

---

## Complexity Summary

| Operation | Average | Worst Case | Notes |
|-----------|---------|------------|-------|
| Peek | O(1) | O(1) | Access root |
| Insert | O(log n) | O(log n) | Bubble up |
| Extract | O(log n) | O(log n) | Bubble down |
| Search | O(n) | O(n) | Not optimized for search |
| Build Heap | O(n) | O(n) | Heapify |
| Heap Sort | O(n log n) | O(n log n) | In-place |
| Space | O(n) | O(n) | Array storage |

---

## Key Takeaways

1. **Heap is a complete binary tree** stored efficiently in an array
2. **Min heap** has smallest at root, **max heap** has largest at root
3. **Insert and extract are O(log n)**, peek is O(1)
4. **Build heap is O(n)**, faster than repeated inserts
5. **Python heapq** is min heap only, negate for max heap
6. **Two heaps pattern** is powerful for median finding
7. **Top K problems** naturally use heaps
8. **Priority queue** is abstract type, heap is common implementation
9. **Heap sort** is O(n log n) in-place but not stable
10. **K-way merge** efficiently uses heap of size k

Understanding heaps is essential for priority queue problems and optimization scenarios in interviews!
