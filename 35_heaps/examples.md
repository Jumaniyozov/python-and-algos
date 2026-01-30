# Chapter 35: Heaps - Examples

## Table of Contents
1. [Min Heap Implementation](#min-heap-implementation)
2. [Max Heap Using heapq](#max-heap-using-heapq)
3. [Priority Queue Implementation](#priority-queue-implementation)
4. [Top K Elements Pattern](#top-k-elements-pattern)
5. [K-Way Merge Pattern](#k-way-merge-pattern)
6. [Running Median (Two Heaps)](#running-median-two-heaps)
7. [Task Scheduling](#task-scheduling)
8. [Heap Sort](#heap-sort)

---

## Min Heap Implementation

### Example 1: Complete Min Heap from Scratch

```python
class MinHeap:
    """
    Complete min heap implementation using array.

    Properties:
    - Complete binary tree (all levels filled left to right)
    - Parent is always smaller than children
    - Root is the minimum element
    """

    def __init__(self):
        self.heap = []

    def parent(self, i):
        """Get parent index."""
        return (i - 1) // 2

    def left_child(self, i):
        """Get left child index."""
        return 2 * i + 1

    def right_child(self, i):
        """Get right child index."""
        return 2 * i + 2

    def _swap(self, i, j):
        """Swap elements at indices i and j."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, val):
        """
        Insert element into heap.
        Time: O(log n)
        Space: O(1)
        """
        # Add to end
        self.heap.append(val)
        # Bubble up to maintain heap property
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        """Move element up until heap property is satisfied."""
        parent_idx = self.parent(index)

        # Continue while not at root and current < parent
        if index > 0 and self.heap[index] < self.heap[parent_idx]:
            self._swap(index, parent_idx)
            self._bubble_up(parent_idx)

    def extract_min(self):
        """
        Remove and return minimum element (root).
        Time: O(log n)
        Space: O(1)
        """
        if not self.heap:
            return None

        # Save min value
        min_val = self.heap[0]

        # Move last element to root
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        # Bubble down to restore heap property
        if self.heap:
            self._bubble_down(0)

        return min_val

    def _bubble_down(self, index):
        """Move element down until heap property is satisfied."""
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        # Find smallest among parent and children
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # Swap if needed and continue
        if smallest != index:
            self._swap(index, smallest)
            self._bubble_down(smallest)

    def peek(self):
        """Return minimum without removing. Time: O(1)"""
        return self.heap[0] if self.heap else None

    def size(self):
        """Return number of elements. Time: O(1)"""
        return len(self.heap)

    def is_empty(self):
        """Check if heap is empty. Time: O(1)"""
        return len(self.heap) == 0

    def heapify(self, arr):
        """
        Build heap from array in-place.
        Time: O(n)
        Space: O(1)
        """
        self.heap = arr.copy()
        # Start from last non-leaf node
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._bubble_down(i)


# Example usage
heap = MinHeap()

# Insert elements
for val in [5, 3, 7, 1, 9, 4]:
    heap.insert(val)
    print(f"Inserted {val}, min is now: {heap.peek()}")

# Extract minimums
print("\nExtracting minimums:")
while not heap.is_empty():
    print(heap.extract_min(), end=" ")
# Output: 1 3 4 5 7 9

# Build heap from array
heap.heapify([64, 34, 25, 12, 22, 11, 90])
print(f"\nHeapified array, min: {heap.peek()}")  # 11
```

---

## Max Heap Using heapq

### Example 2: Max Heap by Negating Values

```python
import heapq

class MaxHeap:
    """
    Max heap implementation using heapq (which is min heap).
    Negate values to simulate max heap behavior.
    """

    def __init__(self):
        self.heap = []

    def push(self, val):
        """
        Add element to max heap.
        Time: O(log n)
        """
        # Negate value for max heap behavior
        heapq.heappush(self.heap, -val)

    def pop(self):
        """
        Remove and return maximum element.
        Time: O(log n)
        """
        if self.heap:
            return -heapq.heappop(self.heap)
        return None

    def peek(self):
        """
        Return maximum without removing.
        Time: O(1)
        """
        return -self.heap[0] if self.heap else None

    def size(self):
        """Return number of elements."""
        return len(self.heap)

    def is_empty(self):
        """Check if heap is empty."""
        return len(self.heap) == 0


# Example usage
max_heap = MaxHeap()

# Push elements
for val in [5, 3, 7, 1, 9, 4]:
    max_heap.push(val)

print("Max heap elements (in descending order):")
while not max_heap.is_empty():
    print(max_heap.pop(), end=" ")
# Output: 9 7 5 4 3 1
```

---

## Priority Queue Implementation

### Example 3: Priority Queue with Items

```python
import heapq
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PriorityItem:
    """
    Item with priority for priority queue.
    Lower priority number = higher priority.
    """
    priority: int
    count: int = field(compare=True)  # For tie-breaking by insertion order
    item: Any = field(compare=False)  # Actual item


class PriorityQueue:
    """
    Priority queue implementation using heap.
    Items with lower priority number are served first.
    """

    def __init__(self):
        self.heap = []
        self.counter = 0  # For maintaining insertion order

    def push(self, item, priority):
        """
        Add item with given priority.
        Time: O(log n)
        """
        heapq.heappush(
            self.heap,
            PriorityItem(priority, self.counter, item)
        )
        self.counter += 1

    def pop(self):
        """
        Remove and return highest priority item.
        Time: O(log n)
        """
        if self.heap:
            priority_item = heapq.heappop(self.heap)
            return priority_item.item
        return None

    def peek(self):
        """
        Return highest priority item without removing.
        Time: O(1)
        """
        if self.heap:
            return self.heap[0].item
        return None

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


# Example usage: Task scheduling
pq = PriorityQueue()

# Add tasks with priorities (1 = highest, 5 = lowest)
pq.push("Fix critical bug", priority=1)
pq.push("Write documentation", priority=3)
pq.push("Code review", priority=2)
pq.push("Refactor code", priority=4)
pq.push("Fix security issue", priority=1)  # Same priority as first

print("Processing tasks by priority:")
while not pq.is_empty():
    task = pq.pop()
    print(f"- {task}")

# Output:
# - Fix critical bug (priority 1, inserted first)
# - Fix security issue (priority 1, inserted second)
# - Code review (priority 2)
# - Write documentation (priority 3)
# - Refactor code (priority 4)
```

---

## Top K Elements Pattern

### Example 4: K Largest Elements

```python
import heapq

def find_k_largest(nums, k):
    """
    Find k largest elements using min heap of size k.

    Intuition:
    - Maintain min heap of k largest seen so far
    - If new element > heap min, it's in top k
    - Replace min with new element

    Time: O(n log k)
    Space: O(k)

    Example:
        nums = [3, 2, 1, 5, 6, 4], k = 2
        Output: [5, 6]
    """
    # Edge case
    if k <= 0 or not nums:
        return []

    # Initialize heap with first k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    # Process remaining elements
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heapreplace(min_heap, num)

    return min_heap


# Alternative: Using heapq.nlargest (simpler but less educational)
def find_k_largest_simple(nums, k):
    """
    Using built-in heapq.nlargest.
    Time: O(n log k)
    """
    return heapq.nlargest(k, nums)


# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2

result = find_k_largest(nums, k)
print(f"K largest elements: {sorted(result, reverse=True)}")  # [6, 5]

# Larger example
nums = [7, 10, 4, 3, 20, 15, 8, 12]
k = 3
result = find_k_largest(nums, k)
print(f"Top 3: {sorted(result, reverse=True)}")  # [20, 15, 12]
```

### Example 5: Kth Largest Element

```python
import heapq

def find_kth_largest(nums, k):
    """
    Find kth largest element (1-indexed).

    Approach: Min heap of size k
    - Heap always contains k largest elements
    - Root of heap is kth largest

    Time: O(n log k)
    Space: O(k)

    Example:
        nums = [3,2,1,5,6,4], k = 2
        Output: 5 (2nd largest)
    """
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


# Example usage
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(f"2nd largest: {find_kth_largest(nums, 2)}")  # 5
print(f"4th largest: {find_kth_largest(nums, 4)}")  # 4
```

---

## K-Way Merge Pattern

### Example 6: Merge K Sorted Lists

```python
import heapq

def merge_k_sorted_lists(lists):
    """
    Merge k sorted lists into one sorted list.

    Approach: Min heap with (value, list_index, element_index)
    - Initialize heap with first element from each list
    - Pop minimum, add next element from same list

    Time: O(N log k) where N = total elements, k = number of lists
    Space: O(k) for heap

    Example:
        lists = [
            [1, 4, 5],
            [1, 3, 4],
            [2, 6]
        ]
        Output: [1, 1, 2, 3, 4, 4, 5, 6]
    """
    min_heap = []
    result = []

    # Initialize heap with first element from each list
    for list_idx, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], list_idx, 0))

    # Process heap
    while min_heap:
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))

    return result


# Example usage
lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]
result = merge_k_sorted_lists(lists)
print(f"Merged: {result}")
# Output: [1, 1, 2, 3, 4, 4, 5, 6]

# Another example
lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = merge_k_sorted_lists(lists)
print(f"Merged: {result}")
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Example 7: Smallest Range Covering Elements from K Lists

```python
import heapq

def smallest_range(lists):
    """
    Find smallest range that includes at least one number from each list.

    Time: O(N log k) where N = total elements
    Space: O(k)

    Example:
        lists = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
        Output: [20,24]
    """
    min_heap = []
    current_max = float('-inf')

    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        heapq.heappush(min_heap, (lst[0], i, 0))
        current_max = max(current_max, lst[0])

    smallest_range = [float('-inf'), float('inf')]

    while len(min_heap) == len(lists):
        current_min, list_idx, elem_idx = heapq.heappop(min_heap)

        # Update smallest range if current range is smaller
        if current_max - current_min < smallest_range[1] - smallest_range[0]:
            smallest_range = [current_min, current_max]

        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))
            current_max = max(current_max, next_val)
        else:
            break

    return smallest_range


# Example usage
lists = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
result = smallest_range(lists)
print(f"Smallest range: {result}")  # [20, 24]
```

---

## Running Median (Two Heaps)

### Example 8: Find Median from Data Stream

```python
import heapq

class MedianFinder:
    """
    Find median from data stream using two heaps.

    Strategy:
    - Max heap for smaller half (left side)
    - Min heap for larger half (right side)
    - Keep heaps balanced: |left| == |right| or |left| == |right| + 1
    - Median is either top of left or average of both tops

    Time: add_num O(log n), find_median O(1)
    Space: O(n)
    """

    def __init__(self):
        # Max heap for smaller half (negate values)
        self.small = []
        # Min heap for larger half
        self.large = []

    def add_num(self, num):
        """
        Add number to data stream.

        Strategy:
        1. Add to max heap (small)
        2. Balance: ensure max(small) <= min(large)
        3. Balance sizes: keep |small| == |large| or |small| == |large| + 1
        """
        # Add to small heap (negate for max heap)
        heapq.heappush(self.small, -num)

        # Ensure every element in small <= every element in large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def find_median(self):
        """
        Return median of all elements so far.
        """
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0


# Example usage
mf = MedianFinder()

stream = [5, 15, 1, 3, 8, 7, 9, 10, 20, 12]

print("Number -> Median")
for num in stream:
    mf.add_num(num)
    print(f"{num:3d} -> {mf.find_median()}")

# Output:
#   5 -> 5.0
#  15 -> 10.0
#   1 -> 5.0
#   3 -> 4.0
#   8 -> 5.0
#   7 -> 6.0
#   9 -> 7.0
#  10 -> 7.5
#  20 -> 8.0
#  12 -> 8.5
```

---

## Task Scheduling

### Example 9: Task Scheduler with Cooldown

```python
import heapq
from collections import Counter, deque

def least_interval(tasks, n):
    """
    Schedule tasks with cooldown period n.
    Same task must wait n intervals before executing again.

    Strategy:
    - Use max heap to always pick most frequent task
    - Use queue to track tasks in cooldown
    - Process in rounds of (n+1) to ensure cooldown

    Time: O(total_time)
    Space: O(26) = O(1) for at most 26 unique tasks

    Example:
        tasks = ["A","A","A","B","B","B"], n = 2
        Output: 8
        Explanation: A -> B -> idle -> A -> B -> idle -> A -> B
    """
    # Count task frequencies
    freq = Counter(tasks)

    # Max heap with frequencies (negate for max heap)
    max_heap = [-count for count in freq.values()]
    heapq.heapify(max_heap)

    time = 0

    while max_heap:
        cycle = 0
        temp = []

        # Process up to n+1 tasks in this round
        for _ in range(n + 1):
            if max_heap:
                count = heapq.heappop(max_heap)
                cycle += 1
                # If task still has remaining executions
                if count < -1:
                    temp.append(count + 1)

        # Add tasks back to heap
        for count in temp:
            heapq.heappush(max_heap, count)

        # Add time for this cycle
        if max_heap:
            time += n + 1  # Full cycle
        else:
            time += cycle  # Last cycle, no idle needed

    return time


# Example usage
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(f"Minimum intervals: {least_interval(tasks, n)}")  # 8

tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
print(f"Minimum intervals: {least_interval(tasks, n)}")  # 16
```

### Example 10: Meeting Rooms II (Minimum Rooms Required)

```python
import heapq

def min_meeting_rooms(intervals):
    """
    Find minimum number of meeting rooms required.

    Strategy:
    - Sort meetings by start time
    - Use min heap to track end times of ongoing meetings
    - When new meeting starts, remove finished meetings
    - Heap size = rooms needed at that time

    Time: O(n log n)
    Space: O(n)

    Example:
        intervals = [[0,30],[5,10],[15,20]]
        Output: 2
    """
    if not intervals:
        return 0

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    # Min heap for end times
    min_heap = []
    heapq.heappush(min_heap, intervals[0][1])

    for i in range(1, len(intervals)):
        # If earliest meeting has ended, reuse room
        if intervals[i][0] >= min_heap[0]:
            heapq.heappop(min_heap)

        # Add current meeting's end time
        heapq.heappush(min_heap, intervals[i][1])

    # Heap size = number of rooms needed
    return len(min_heap)


# Example usage
intervals = [[0, 30], [5, 10], [15, 20]]
print(f"Rooms needed: {min_meeting_rooms(intervals)}")  # 2

intervals = [[7, 10], [2, 4]]
print(f"Rooms needed: {min_meeting_rooms(intervals)}")  # 1

intervals = [[1, 5], [2, 3], [4, 6], [5, 7]]
print(f"Rooms needed: {min_meeting_rooms(intervals)}")  # 2
```

---

## Heap Sort

### Example 11: Heap Sort Implementation

```python
def heap_sort(arr):
    """
    Sort array using heap sort algorithm.

    Steps:
    1. Build max heap from array - O(n)
    2. Repeatedly extract max to end - O(n log n)

    Time: O(n log n)
    Space: O(1) - in-place sorting

    Properties:
    - Not stable (equal elements may change relative order)
    - In-place sorting
    - Guaranteed O(n log n) worst case
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify_down(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify reduced heap
        _heapify_down(arr, i, 0)

    return arr


def _heapify_down(arr, n, i):
    """
    Heapify subtree rooted at index i.
    n is size of heap.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Find largest among root and children
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and continue if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify_down(arr, n, largest)


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {arr}")

heap_sort(arr)
print(f"Sorted: {arr}")
# Output: [11, 12, 22, 25, 34, 64, 90]

# Verify with different array
arr = [5, 1, 1, 2, 0, 0]
heap_sort(arr)
print(f"Sorted with duplicates: {arr}")
# Output: [0, 0, 1, 1, 2, 5]
```

---

## Key Takeaways

1. **Min Heap Implementation**: Complete binary tree stored in array with parent-child relationships
2. **Max Heap Trick**: Negate values when using Python's heapq (min heap only)
3. **Top K Pattern**: Use min heap of size k to maintain k largest elements
4. **Two Heaps Pattern**: Split data into two halves for median finding
5. **K-Way Merge**: Use heap of size k to merge k sorted sequences efficiently
6. **Priority Queue**: Heaps are perfect for priority-based scheduling
7. **Heap Sort**: O(n log n) in-place sorting using heap property
8. **Time Complexity**: Insert/Extract O(log n), Peek O(1), Heapify O(n)

These patterns appear frequently in interviews. Master them for success!
