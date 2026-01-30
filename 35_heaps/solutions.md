# Chapter 35: Heaps - Solutions

This document contains detailed solutions for all heap exercises, organized by difficulty level.

---

## Easy Problems

### E1: Kth Largest Element in Array

**Problem**: Find the kth largest element in an unsorted array.

**Approach 1: Min Heap of Size K (Optimal)**

Use a min heap to maintain the k largest elements. The root is the kth largest.

```python
import heapq

def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Find kth largest using min heap.

    Time: O(n log k)
    Space: O(k)
    """
    # Maintain min heap of size k
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]
```

**Approach 2: Using heapq.nlargest**

```python
def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Using built-in function.

    Time: O(n log k)
    Space: O(k)
    """
    return heapq.nlargest(k, nums)[-1]
```

**Approach 3: Quickselect (Best Average Case)**

```python
def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Quickselect algorithm.

    Time: O(n) average, O(n^2) worst
    Space: O(1)
    """
    k = len(nums) - k  # Convert to kth smallest (0-indexed)

    def quickselect(left, right):
        pivot = nums[right]
        p = left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        nums[p], nums[right] = nums[right], nums[p]

        if p > k:
            return quickselect(left, p - 1)
        elif p < k:
            return quickselect(p + 1, right)
        else:
            return nums[p]

    return quickselect(0, len(nums) - 1)
```

**Time Complexity**: O(n log k) for heap, O(n) average for quickselect
**Space Complexity**: O(k) for heap, O(1) for quickselect

---

### E2: Last Stone Weight

**Problem**: Smash two heaviest stones together repeatedly.

**Approach**: Max Heap

```python
import heapq

def last_stone_weight(stones: List[int]) -> int:
    """
    Use max heap (negate values).

    Time: O(n log n)
    Space: O(n)
    """
    # Convert to max heap by negating
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        # Get two heaviest
        first = -heapq.heappop(max_heap)
        second = -heapq.heappop(max_heap)

        # If different weights, add difference back
        if first != second:
            heapq.heappush(max_heap, -(first - second))

    # Return last stone or 0
    return -max_heap[0] if max_heap else 0
```

**Time Complexity**: O(n log n) - n pops/pushes, each O(log n)
**Space Complexity**: O(n) for heap

---

### E3: Relative Ranks

**Problem**: Assign ranks to athletes based on scores.

**Approach**: Heap with Original Indices

```python
import heapq

def find_relative_ranks(score: List[int]) -> List[str]:
    """
    Use max heap to get sorted order.

    Time: O(n log n)
    Space: O(n)
    """
    n = len(score)
    result = [''] * n

    # Max heap: (score, index)
    max_heap = [(-s, i) for i, s in enumerate(score)]
    heapq.heapify(max_heap)

    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    rank = 1

    while max_heap:
        _, idx = heapq.heappop(max_heap)
        if rank <= 3:
            result[idx] = medals[rank - 1]
        else:
            result[idx] = str(rank)
        rank += 1

    return result
```

**Time Complexity**: O(n log n)
**Space Complexity**: O(n)

---

### E4: Kth Largest Element in a Stream

**Problem**: Design class to maintain kth largest in stream.

**Approach**: Min Heap of Size K

```python
import heapq

class KthLargest:
    """
    Maintain min heap of k largest elements.
    Root is kth largest.

    Time: __init__ O(n log k), add O(log k)
    Space: O(k)
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        # Add initial elements
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add to heap
        heapq.heappush(self.min_heap, val)

        # Remove if exceeds size k
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
```

**Time Complexity**: O(log k) per add
**Space Complexity**: O(k)

---

### E5: Minimum Cost to Connect Sticks

**Problem**: Connect sticks with minimum cost.

**Approach**: Greedy with Min Heap

Always connect two smallest sticks first.

```python
import heapq

def connect_sticks(sticks: List[int]) -> int:
    """
    Always connect smallest two sticks.

    Time: O(n log n)
    Space: O(n)
    """
    heapq.heapify(sticks)
    total_cost = 0

    while len(sticks) > 1:
        # Get two smallest
        first = heapq.heappop(sticks)
        second = heapq.heappop(sticks)

        # Combine and add cost
        cost = first + second
        total_cost += cost

        # Add combined stick back
        heapq.heappush(sticks, cost)

    return total_cost
```

**Time Complexity**: O(n log n)
**Space Complexity**: O(n)

---

### E6: Meeting Rooms

**Problem**: Check if person can attend all meetings.

**Approach**: Sort and Check Overlap

```python
def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """
    Sort by start time, check for overlaps.

    Time: O(n log n)
    Space: O(1) or O(n) depending on sort implementation
    """
    if not intervals:
        return True

    # Sort by start time
    intervals.sort()

    # Check each pair of consecutive meetings
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True
```

**Time Complexity**: O(n log n) for sorting
**Space Complexity**: O(1)

---

### E7: Sort Characters By Frequency

**Problem**: Sort string by character frequency.

**Approach**: Max Heap with Frequencies

```python
import heapq
from collections import Counter

def frequency_sort(s: str) -> str:
    """
    Use max heap to sort by frequency.

    Time: O(n log k) where k is unique characters
    Space: O(n)
    """
    # Count frequencies
    freq = Counter(s)

    # Max heap: (-frequency, character)
    max_heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(max_heap)

    # Build result
    result = []
    while max_heap:
        count, char = heapq.heappop(max_heap)
        result.append(char * (-count))

    return ''.join(result)
```

**Time Complexity**: O(n log k) where k = unique characters
**Space Complexity**: O(n)

---

## Medium Problems

### M1: Top K Frequent Elements

**Problem**: Return k most frequent elements.

**Approach**: Min Heap of Size K

```python
import heapq
from collections import Counter

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Min heap of (frequency, element) pairs.

    Time: O(n log k)
    Space: O(n)
    """
    # Count frequencies
    freq = Counter(nums)

    # Min heap of size k
    min_heap = []

    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for count, num in min_heap]
```

**Alternative: Using heapq.nlargest**

```python
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Time: O(n log k)
    Space: O(n)
    """
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key=freq.get)
```

**Time Complexity**: O(n log k)
**Space Complexity**: O(n)

---

### M2: K Closest Points to Origin

**Problem**: Find k closest points to origin.

**Approach**: Max Heap of Size K

```python
import heapq

def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Max heap of distances. Keep k smallest.

    Time: O(n log k)
    Space: O(k)
    """
    # Max heap: (-distance, point)
    max_heap = []

    for x, y in points:
        dist = x*x + y*y  # No need for sqrt
        heapq.heappush(max_heap, (-dist, [x, y]))
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [point for dist, point in max_heap]
```

**Time Complexity**: O(n log k)
**Space Complexity**: O(k)

---

### M3: Task Scheduler

**Problem**: Minimum intervals to complete tasks with cooldown.

**Approach**: Max Heap with Greedy

```python
import heapq
from collections import Counter

def least_interval(tasks: List[str], n: int) -> int:
    """
    Use max heap to always pick most frequent task.

    Time: O(total_intervals)
    Space: O(26) = O(1)
    """
    freq = Counter(tasks)
    max_heap = [-count for count in freq.values()]
    heapq.heapify(max_heap)

    time = 0

    while max_heap:
        cycle = []

        # Process n+1 tasks (or until heap empty)
        for _ in range(n + 1):
            if max_heap:
                count = heapq.heappop(max_heap)
                if count < -1:
                    cycle.append(count + 1)

        # Add tasks back
        for count in cycle:
            heapq.heappush(max_heap, count)

        # Add time
        if max_heap:
            time += n + 1
        else:
            time += len(cycle)

    return time
```

**Alternative: Mathematical Approach**

```python
def least_interval(tasks: List[str], n: int) -> int:
    """
    Formula-based approach.

    Time: O(n) where n is number of tasks
    Space: O(1)
    """
    freq = Counter(tasks)
    max_freq = max(freq.values())
    max_count = sum(1 for f in freq.values() if f == max_freq)

    # Formula: (max_freq - 1) * (n + 1) + max_count
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
```

**Time Complexity**: O(total_intervals) or O(n) for mathematical
**Space Complexity**: O(1)

---

### M4: Meeting Rooms II

**Problem**: Minimum conference rooms needed.

**Approach**: Min Heap of End Times

```python
import heapq

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Track end times of ongoing meetings.

    Time: O(n log n)
    Space: O(n)
    """
    if not intervals:
        return 0

    # Sort by start time
    intervals.sort()

    # Min heap of end times
    min_heap = []
    heapq.heappush(min_heap, intervals[0][1])

    for i in range(1, len(intervals)):
        # If earliest meeting ended, reuse room
        if intervals[i][0] >= min_heap[0]:
            heapq.heappop(min_heap)

        # Add current meeting's end time
        heapq.heappush(min_heap, intervals[i][1])

    return len(min_heap)
```

**Time Complexity**: O(n log n)
**Space Complexity**: O(n)

---

### M10: Find Median from Data Stream

**Problem**: Design structure for running median.

**Approach**: Two Heaps

```python
import heapq

class MedianFinder:
    """
    Two heaps: max heap for smaller half, min heap for larger half.

    Time: addNum O(log n), findMedian O(1)
    Space: O(n)
    """

    def __init__(self):
        self.small = []  # Max heap (negate values)
        self.large = []  # Min heap

    def addNum(self, num: int) -> None:
        # Add to small (max heap)
        heapq.heappush(self.small, -num)

        # Ensure max(small) <= min(large)
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

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
```

**Time Complexity**: O(log n) add, O(1) find median
**Space Complexity**: O(n)

---

## Hard Problems

### H1: Merge K Sorted Lists

**Problem**: Merge k sorted linked lists.

**Approach**: Min Heap

```python
import heapq

def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Use min heap to track smallest available node.

    Time: O(N log k) where N = total nodes
    Space: O(k)
    """
    min_heap = []

    # Initialize heap with first node from each list
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(min_heap, (head.val, i, head))

    dummy = ListNode(0)
    current = dummy

    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next

        # Add next node from same list
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next
```

**Time Complexity**: O(N log k)
**Space Complexity**: O(k)

---

### H2: Smallest Range Covering Elements from K Lists

**Problem**: Find smallest range including element from each list.

**Approach**: Min Heap with Current Max

```python
import heapq

def smallest_range(nums: List[List[int]]) -> List[int]:
    """
    Track current range while iterating through lists.

    Time: O(N log k) where N = total elements
    Space: O(k)
    """
    min_heap = []
    current_max = float('-inf')

    # Initialize with first element from each list
    for i, lst in enumerate(nums):
        heapq.heappush(min_heap, (lst[0], i, 0))
        current_max = max(current_max, lst[0])

    smallest_range = [float('-inf'), float('inf')]

    while len(min_heap) == len(nums):
        current_min, list_idx, elem_idx = heapq.heappop(min_heap)

        # Update smallest range
        if current_max - current_min < smallest_range[1] - smallest_range[0]:
            smallest_range = [current_min, current_max]

        # Add next element from same list
        if elem_idx + 1 < len(nums[list_idx]):
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))
            current_max = max(current_max, next_val)
        else:
            break

    return smallest_range
```

**Time Complexity**: O(N log k)
**Space Complexity**: O(k)

---

## Key Insights

1. **Min heap of size k**: Perfect for "k largest" problems
2. **Max heap of size k**: Perfect for "k smallest" problems
3. **Two heaps**: Split data for median/balance problems
4. **K-way merge**: Heap of size k tracks current minimums
5. **Greedy + Heap**: Many scheduling problems
6. **Time tracking**: Heap for managing time-based events

Master these patterns for heap interview success!
