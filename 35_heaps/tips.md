# Chapter 35: Heaps - Tips and Tricks

## Table of Contents
1. [Common Pitfalls](#common-pitfalls)
2. [Pattern Recognition](#pattern-recognition)
3. [Interview Tips](#interview-tips)
4. [Performance Optimization](#performance-optimization)
5. [LeetCode Practice Problems](#leetcode-practice-problems)

---

## Common Pitfalls

### 1. Forgetting Python heapq is Min Heap Only

```python
# ❌ WRONG: Trying to use as max heap directly
import heapq
heap = [5, 3, 7, 1]
heapq.heapify(heap)
max_val = heapq.heappop(heap)  # Gets 1, not 7!

# ✅ CORRECT: Negate values for max heap
max_heap = [-x for x in [5, 3, 7, 1]]
heapq.heapify(max_heap)
max_val = -heapq.heappop(max_heap)  # Gets 7
```

### 2. Not Maintaining Heap Size in Top K Problems

```python
# ❌ WRONG: Heap grows unbounded
import heapq
def find_k_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    # Heap has all elements, defeats purpose!
    return heap

# ✅ CORRECT: Maintain size k
def find_k_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap
```

### 3. Using Wrong Heap for Top K

```python
# ❌ WRONG: Max heap for k largest
# This keeps k smallest, not k largest!
max_heap = []
for num in nums:
    heapq.heappush(max_heap, -num)
    if len(max_heap) > k:
        heapq.heappop(max_heap)

# ✅ CORRECT: Min heap for k largest
# Min heap root is kth largest
min_heap = []
for num in nums:
    heapq.heappush(min_heap, num)
    if len(min_heap) > k:
        heapq.heappop(min_heap)
```

### 4. Not Handling Ties in Priority Queue

```python
# ❌ WRONG: Can't compare non-comparable objects
import heapq
heap = []
heapq.heappush(heap, (1, {'name': 'Alice'}))  # TypeError if tie!

# ✅ CORRECT: Use counter for tie-breaking
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class Item:
    priority: int
    counter: int = field(compare=True)
    data: Any = field(compare=False)

heap = []
counter = 0
heapq.heappush(heap, Item(1, counter, {'name': 'Alice'}))
counter += 1
```

### 5. Modifying Heap Incorrectly

```python
# ❌ WRONG: Modifying heap array directly breaks heap property
heap = [1, 3, 2, 7, 5]
heapq.heapify(heap)
heap[0] = 10  # Breaks heap property!

# ✅ CORRECT: Use heappush/heappop or heapify after modification
heap = [1, 3, 2, 7, 5]
heapq.heapify(heap)
heapq.heapreplace(heap, 10)  # Properly maintains heap
```

### 6. Off-by-One in Two Heaps Pattern

```python
# ❌ WRONG: Unbalanced heaps
class MedianFinder:
    def addNum(self, num):
        heapq.heappush(self.small, -num)
        # Missing balance logic!

# ✅ CORRECT: Maintain size invariant
class MedianFinder:
    def addNum(self, num):
        heapq.heappush(self.small, -num)

        # Balance values
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
```

---

## Pattern Recognition

### Pattern 1: Top K Elements

**When to use:**
- Find k largest/smallest elements
- Kth largest/smallest element
- Top k frequent elements

**Template:**
```python
import heapq

def top_k_pattern(nums, k):
    """
    For k largest: use min heap of size k
    For k smallest: use max heap of size k
    """
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap
```

**Key insight:** Heap root is the kth element!

### Pattern 2: Two Heaps (Median Finding)

**When to use:**
- Find median in data stream
- Sliding window median
- Balance two groups

**Template:**
```python
class TwoHeaps:
    def __init__(self):
        self.small = []  # Max heap for smaller half
        self.large = []  # Min heap for larger half

    def add(self, num):
        # Add to appropriate heap
        heapq.heappush(self.small, -num)

        # Balance values
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

    def get_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
```

### Pattern 3: K-Way Merge

**When to use:**
- Merge k sorted arrays/lists
- Find smallest range covering k lists
- Merge intervals from multiple sources

**Template:**
```python
import heapq

def k_way_merge(lists):
    """Merge k sorted lists."""
    heap = []
    result = []

    # Initialize with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Add next from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result
```

### Pattern 4: Scheduling/Interval Problems

**When to use:**
- Task scheduling with priorities
- Meeting rooms
- CPU scheduling
- Interval processing by time

**Template:**
```python
import heapq

def schedule_pattern(tasks):
    """Process tasks by priority/time."""
    # Sort by start time/priority
    tasks.sort()

    heap = []
    for task in tasks:
        # Remove finished/expired tasks
        while heap and heap[0] <= task.start:
            heapq.heappop(heap)

        # Add current task
        heapq.heappush(heap, task.end)

    return len(heap)  # or other result
```

### Pattern 5: Stream Processing

**When to use:**
- Process data as it arrives
- Maintain running statistics
- Dynamic ranking

**Template:**
```python
import heapq

class StreamProcessor:
    def __init__(self):
        self.heap = []

    def add(self, val):
        heapq.heappush(self.heap, val)
        # Maintain heap invariants

    def query(self):
        return self.heap[0]
```

---

## Interview Tips

### 1. Identify Heap Problems

**Signals that suggest using a heap:**
- "Find k largest/smallest"
- "Find median"
- "Merge k sorted..."
- "Schedule by priority"
- "Top k frequent"
- "Minimum/maximum at any time"
- Need O(log n) insert/delete with O(1) access to min/max

### 2. Choose Right Heap Type

```python
# For k LARGEST: use MIN heap
# Root is kth largest, smaller elements get removed
min_heap = []
for num in nums:
    heapq.heappush(min_heap, num)
    if len(min_heap) > k:
        heapq.heappop(min_heap)

# For k SMALLEST: use MAX heap (negate)
# Root is kth smallest, larger elements get removed
max_heap = []
for num in nums:
    heapq.heappush(max_heap, -num)
    if len(max_heap) > k:
        heapq.heappop(max_heap)
```

### 3. State Complexity Analysis

```python
# Always mention:
# Time: O(n log k) for n elements, heap of size k
# Space: O(k) for the heap
```

### 4. Consider Alternatives

```python
# For top k: Quickselect is O(n) average
# But heap is O(n log k) and simpler to implement
# Choose based on:
# - k value (k << n → heap, k ≈ n → quickselect)
# - Implementation simplicity
# - Follow-up questions (streaming data → heap)
```

### 5. Handle Edge Cases

```python
# Always check:
if not nums or k <= 0:
    return []
if k >= len(nums):
    return nums  # or appropriate response
```

---

## Performance Optimization

### 1. Use heapq.heapify for Bulk Operations

```python
# ❌ Slower: Individual pushes
heap = []
for x in nums:
    heapq.heappush(heap, x)  # O(n log n)

# ✅ Faster: Heapify at once
heap = nums.copy()
heapq.heapify(heap)  # O(n)
```

### 2. Use heapreplace for Combined Pop/Push

```python
# ❌ Two operations
if len(heap) == k:
    heapq.heappop(heap)
    heapq.heappush(heap, new_val)

# ✅ One operation
if len(heap) == k:
    heapq.heapreplace(heap, new_val)
```

### 3. Use Built-in nlargest/nsmallest When Appropriate

```python
# Simple one-time query
k_largest = heapq.nlargest(k, nums)
k_smallest = heapq.nsmallest(k, nums)

# With custom key
top_k = heapq.nlargest(k, items, key=lambda x: x.value)
```

### 4. Avoid Unnecessary Comparisons

```python
# For distance-based problems, avoid sqrt
# ❌ Slower
dist = (x**2 + y**2) ** 0.5

# ✅ Faster (comparison order preserved)
dist = x**2 + y**2
```

---

## LeetCode Practice Problems

### Must-Practice Problems (Top 15)

These problems cover all essential heap patterns:

#### 1. Kth Largest Element in an Array
**Link:** https://leetcode.com/problems/kth-largest-element-in-an-array/
**Difficulty:** Medium
**Pattern:** Top K Elements (Min Heap)
**Why Practice:** Foundation of heap usage, appears in 10%+ of interviews
**Time to Solve:** 15-20 minutes

#### 2. Top K Frequent Elements
**Link:** https://leetcode.com/problems/top-k-frequent-elements/
**Difficulty:** Medium
**Pattern:** Top K with Frequency Count
**Why Practice:** Combines hash table and heap, very common pattern
**Time to Solve:** 20-25 minutes

#### 3. Find Median from Data Stream
**Link:** https://leetcode.com/problems/find-median-from-data-stream/
**Difficulty:** Hard
**Pattern:** Two Heaps
**Why Practice:** Classic two-heaps problem, asked by Google, Facebook, Amazon
**Time to Solve:** 30-40 minutes

#### 4. Merge K Sorted Lists
**Link:** https://leetcode.com/problems/merge-k-sorted-lists/
**Difficulty:** Hard
**Pattern:** K-Way Merge
**Why Practice:** Classic k-way merge, demonstrates heap mastery
**Time to Solve:** 25-35 minutes

#### 5. Task Scheduler
**Link:** https://leetcode.com/problems/task-scheduler/
**Difficulty:** Medium
**Pattern:** Scheduling with Cooldown
**Why Practice:** Real-world scheduling problem, tests greedy + heap
**Time to Solve:** 30-40 minutes

#### 6. Meeting Rooms II
**Link:** https://leetcode.com/problems/meeting-rooms-ii/
**Difficulty:** Medium
**Pattern:** Interval Scheduling
**Why Practice:** Common system design follow-up, practical application
**Time to Solve:** 20-25 minutes

#### 7. K Closest Points to Origin
**Link:** https://leetcode.com/problems/k-closest-points-to-origin/
**Difficulty:** Medium
**Pattern:** Top K with Distance
**Why Practice:** Geometric problems with heaps, quickselect alternative
**Time to Solve:** 15-20 minutes

#### 8. Sliding Window Median
**Link:** https://leetcode.com/problems/sliding-window-median/
**Difficulty:** Hard
**Pattern:** Two Heaps with Sliding Window
**Why Practice:** Advanced two-heaps, element removal complexity
**Time to Solve:** 40-50 minutes

#### 9. Smallest Range Covering Elements from K Lists
**Link:** https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
**Difficulty:** Hard
**Pattern:** K-Way Merge with Range Tracking
**Why Practice:** Complex k-way merge variant, tests deep understanding
**Time to Solve:** 35-45 minutes

#### 10. Reorganize String
**Link:** https://leetcode.com/problems/reorganize-string/
**Difficulty:** Medium
**Pattern:** Greedy String Scheduling
**Why Practice:** Creative heap application, greedy algorithm
**Time to Solve:** 25-30 minutes

#### 11. Last Stone Weight
**Link:** https://leetcode.com/problems/last-stone-weight/
**Difficulty:** Easy
**Pattern:** Simulation with Max Heap
**Why Practice:** Simple max heap usage, good warmup
**Time to Solve:** 10-15 minutes

#### 12. Kth Smallest Element in a Sorted Matrix
**Link:** https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
**Difficulty:** Medium
**Pattern:** K-Way Merge on Matrix
**Why Practice:** 2D array with heap, matrix-specific optimization
**Time to Solve:** 25-30 minutes

#### 13. Find K Pairs with Smallest Sums
**Link:** https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
**Difficulty:** Medium
**Pattern:** K-Way Merge with Pairs
**Why Practice:** Tests understanding of heap ordering with pairs
**Time to Solve:** 30-35 minutes

#### 14. IPO
**Link:** https://leetcode.com/problems/ipo/
**Difficulty:** Hard
**Pattern:** Two Heaps with Capital Maximization
**Why Practice:** Real-world optimization, combines multiple concepts
**Time to Solve:** 35-45 minutes

#### 15. Minimum Cost to Connect Sticks
**Link:** https://leetcode.com/problems/minimum-cost-to-connect-sticks/
**Difficulty:** Medium
**Pattern:** Greedy with Min Heap
**Why Practice:** Huffman encoding variant, greedy correctness proof
**Time to Solve:** 15-20 minutes

---

### Easy Problems (12 problems)

#### 16. Kth Largest Element in a Stream
**Link:** https://leetcode.com/problems/kth-largest-element-in-a-stream/
**Pattern:** Stream Processing with Min Heap
**Time:** 15 minutes

#### 17. Relative Ranks
**Link:** https://leetcode.com/problems/relative-ranks/
**Pattern:** Sorting with Heap
**Time:** 15 minutes

#### 18. Third Maximum Number
**Link:** https://leetcode.com/problems/third-maximum-number/
**Pattern:** Top K with Edge Cases
**Time:** 15 minutes

#### 19. The K Weakest Rows in a Matrix
**Link:** https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
**Pattern:** Top K with Custom Comparator
**Time:** 15 minutes

#### 20. Min Cost Climbing Stairs (Can use heap)
**Link:** https://leetcode.com/problems/min-cost-climbing-stairs/
**Pattern:** DP with Optional Heap
**Time:** 20 minutes

#### 21. Find Subsequence of Length K With the Largest Sum
**Link:** https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
**Pattern:** Top K with Index Preservation
**Time:** 20 minutes

#### 22. Maximum Product of Two Elements in an Array
**Link:** https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
**Pattern:** Finding Top 2
**Time:** 10 minutes

#### 23. Sort Characters by Frequency
**Link:** https://leetcode.com/problems/sort-characters-by-frequency/
**Pattern:** Frequency Sorting
**Time:** 15 minutes

#### 24. Remove Stones to Minimize the Total
**Link:** https://leetcode.com/problems/remove-stones-to-minimize-the-total/
**Pattern:** Max Heap Simulation
**Time:** 15 minutes

#### 25. Take Gifts From the Richest Pile
**Link:** https://leetcode.com/problems/take-gifts-from-the-richest-pile/
**Pattern:** Max Heap Simulation
**Time:** 15 minutes

#### 26. Maximum Score From Removing Stones
**Link:** https://leetcode.com/problems/maximum-score-from-removing-stones/
**Pattern:** Greedy with Heap
**Time:** 20 minutes

#### 27. Minimum Amount of Time to Fill Cups
**Link:** https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/
**Pattern:** Greedy Scheduling
**Time:** 20 minutes

---

### Medium Problems (35 problems)

#### 28. Kth Smallest Element in a BST
**Link:** https://leetcode.com/problems/kth-smallest-element-in-a-bst/
**Pattern:** Tree + Heap (or inorder)
**Time:** 20 minutes

#### 29. Sort an Array
**Link:** https://leetcode.com/problems/sort-an-array/
**Pattern:** Heap Sort Implementation
**Time:** 25 minutes

#### 30. Car Pooling
**Link:** https://leetcode.com/problems/car-pooling/
**Pattern:** Interval Events with Heap
**Time:** 25 minutes

#### 31. Course Schedule III
**Link:** https://leetcode.com/problems/course-schedule-iii/
**Pattern:** Greedy Scheduling with Heap
**Time:** 35 minutes

#### 32. Maximum Performance of a Team
**Link:** https://leetcode.com/problems/maximum-performance-of-a-team/
**Pattern:** Greedy with Min Heap
**Time:** 35 minutes

#### 33. Furthest Building You Can Reach
**Link:** https://leetcode.com/problems/furthest-building-you-can-reach/
**Pattern:** Resource Allocation with Heap
**Time:** 30 minutes

#### 34. Minimize Deviation in Array
**Link:** https://leetcode.com/problems/minimize-deviation-in-array/
**Pattern:** Range Minimization with Heap
**Time:** 40 minutes

#### 35. Maximum Subsequence Score
**Link:** https://leetcode.com/problems/maximum-subsequence-score/
**Pattern:** Greedy with Min Heap
**Time:** 35 minutes

#### 36. Maximum Number of Events That Can Be Attended
**Link:** https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
**Pattern:** Event Scheduling
**Time:** 35 minutes

#### 37. Seat Reservation Manager
**Link:** https://leetcode.com/problems/seat-reservation-manager/
**Pattern:** Available Resource Management
**Time:** 15 minutes

#### 38. Stock Price Fluctuation
**Link:** https://leetcode.com/problems/stock-price-fluctuation/
**Pattern:** Two Heaps with Updates
**Time:** 30 minutes

#### 39. Reducing Dishes
**Link:** https://leetcode.com/problems/reducing-dishes/
**Pattern:** Greedy with Sorting/Heap
**Time:** 25 minutes

#### 40. Find the Kth Largest Integer in the Array
**Link:** https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
**Pattern:** Top K with String Comparison
**Time:** 20 minutes

#### 41. Process Tasks Using Servers
**Link:** https://leetcode.com/problems/process-tasks-using-servers/
**Pattern:** Task Assignment with Two Heaps
**Time:** 40 minutes

#### 42. Single-Threaded CPU
**Link:** https://leetcode.com/problems/single-threaded-cpu/
**Pattern:** CPU Scheduling Simulation
**Time:** 35 minutes

#### 43. Find Servers That Handled Most Number of Requests
**Link:** https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
**Pattern:** Load Balancing with Heap
**Time:** 40 minutes

#### 44. Maximum Number of Events That Can Be Attended II
**Link:** https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
**Pattern:** DP + Heap
**Time:** 45 minutes

#### 45. Minimum Number of Refueling Stops
**Link:** https://leetcode.com/problems/minimum-number-of-refueling-stops/
**Pattern:** Greedy with Max Heap
**Time:** 35 minutes

#### 46. Ugly Number II
**Link:** https://leetcode.com/problems/ugly-number-ii/
**Pattern:** Multiple Pointers with Heap
**Time:** 30 minutes

#### 47. Super Ugly Number
**Link:** https://leetcode.com/problems/super-ugly-number/
**Pattern:** Generalized Ugly Number
**Time:** 35 minutes

#### 48. Design Twitter
**Link:** https://leetcode.com/problems/design-twitter/
**Pattern:** K-Way Merge for Social Feed
**Time:** 40 minutes

#### 49. Construct Target Array With Multiple Sums
**Link:** https://leetcode.com/problems/construct-target-array-with-multiple-sums/
**Pattern:** Reverse Engineering with Heap
**Time:** 40 minutes

#### 50. Number of Orders in the Backlog
**Link:** https://leetcode.com/problems/number-of-orders-in-the-backlog/
**Pattern:** Order Book Simulation
**Time:** 35 minutes

#### 51. Find K Closest Elements
**Link:** https://leetcode.com/problems/find-k-closest-elements/
**Pattern:** Top K with Distance
**Time:** 25 minutes

#### 52. Network Delay Time (Dijkstra)
**Link:** https://leetcode.com/problems/network-delay-time/
**Pattern:** Shortest Path with Min Heap
**Time:** 30 minutes

#### 53. Path with Maximum Minimum Value
**Link:** https://leetcode.com/problems/path-with-maximum-minimum-value/
**Pattern:** Modified Dijkstra
**Time:** 35 minutes

#### 54. Cheapest Flights Within K Stops
**Link:** https://leetcode.com/problems/cheapest-flights-within-k-stops/
**Pattern:** Modified Dijkstra with Constraints
**Time:** 35 minutes

#### 55. Path With Minimum Effort
**Link:** https://leetcode.com/problems/path-with-minimum-effort/
**Pattern:** Binary Search + BFS or Dijkstra
**Time:** 35 minutes

#### 56. Swim in Rising Water
**Link:** https://leetcode.com/problems/swim-in-rising-water/
**Pattern:** Modified Dijkstra for Minimum Maximum
**Time:** 30 minutes

#### 57. Minimum Cost to Hire K Workers
**Link:** https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
**Pattern:** Greedy with Max Heap
**Time:** 40 minutes

#### 58. Find K-th Smallest Pair Distance
**Link:** https://leetcode.com/problems/find-k-th-smallest-pair-distance/
**Pattern:** Binary Search (heap possible but inefficient)
**Time:** 40 minutes

#### 59. Distant Barcodes
**Link:** https://leetcode.com/problems/distant-barcodes/
**Pattern:** Reorganize with Heap
**Time:** 30 minutes

#### 60. Longest Happy String
**Link:** https://leetcode.com/problems/longest-happy-string/
**Pattern:** Greedy String Construction
**Time:** 30 minutes

#### 61. Minimize Maximum Pair Sum in Array
**Link:** https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
**Pattern:** Pairing Strategy (sorting better than heap)
**Time:** 20 minutes

#### 62. Minimum Deletions to Make Character Frequencies Unique
**Link:** https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
**Pattern:** Frequency Management
**Time:** 25 minutes

---

### Hard Problems (13 problems)

#### 63. Trapping Rain Water II
**Link:** https://leetcode.com/problems/trapping-rain-water-ii/
**Pattern:** 2D Min Heap BFS
**Time:** 50 minutes

#### 64. Employee Free Time
**Link:** https://leetcode.com/problems/employee-free-time/
**Pattern:** Interval Merging with Heap
**Time:** 35 minutes

#### 65. Median of Two Sorted Arrays (Binary search better)
**Link:** https://leetcode.com/problems/median-of-two-sorted-arrays/
**Pattern:** Two Heaps or Binary Search
**Time:** 45 minutes

#### 66. Find Minimum in Rotated Sorted Array II
**Link:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
**Pattern:** Can use heap but binary search better
**Time:** 30 minutes

#### 67. Maximum Number of Visible Points
**Link:** https://leetcode.com/problems/maximum-number-of-visible-points/
**Pattern:** Geometry with Sorting (heap alternative)
**Time:** 45 minutes

#### 68. Painting the Walls
**Link:** https://leetcode.com/problems/painting-the-walls/
**Pattern:** DP (heap not optimal)
**Time:** 40 minutes

#### 69. Maximum Number of Events That Can Be Attended III
**Link:** https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-iii/
**Pattern:** DP with Heap Optimization
**Time:** 50 minutes

#### 70. Parallel Courses III
**Link:** https://leetcode.com/problems/parallel-courses-iii/
**Pattern:** Topological Sort with Heap
**Time:** 40 minutes

#### 71. Maximum Profit in Job Scheduling
**Link:** https://leetcode.com/problems/maximum-profit-in-job-scheduling/
**Pattern:** DP with Heap
**Time:** 45 minutes

#### 72. Minimum Time to Finish the Race
**Link:** https://leetcode.com/problems/minimum-time-to-finish-the-race/
**Pattern:** DP with Preprocessing
**Time:** 50 minutes

#### 73. Minimum Cost to Reach Destination in Time
**Link:** https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/
**Pattern:** Modified Dijkstra with Constraints
**Time:** 45 minutes

#### 74. Count of Range Sum
**Link:** https://leetcode.com/problems/count-of-range-sum/
**Pattern:** Merge Sort (not heap, but good to know)
**Time:** 50 minutes

#### 75. Minimum Number of Days to Eat N Oranges
**Link:** https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/
**Pattern:** BFS with Heap (Dijkstra variant)
**Time:** 40 minutes

---

## Practice Progression

### Week 1-2: Fundamentals (10-15 hours)
Focus on basic heap operations and top k problems.
- Problems: 1, 7, 11, 16-27
- Master min/max heap distinction
- Practice maintaining heap size

### Week 3-4: Two Heaps Pattern (12-18 hours)
Master the two heaps pattern for median problems.
- Problems: 3, 8, 38
- Understand balancing strategy
- Practice element removal

### Week 5-6: K-Way Merge (15-20 hours)
Learn to merge multiple sorted sources.
- Problems: 4, 9, 12, 13, 48
- Master heap with indices
- Handle exhausted sources

### Week 7-8: Scheduling (12-16 hours)
Apply heaps to scheduling and interval problems.
- Problems: 5, 6, 10, 30, 31, 32, 33, 36, 41-44
- Understand event-driven simulation
- Practice resource allocation

### Week 9-10: Advanced (15-20 hours)
Tackle complex problems combining multiple patterns.
- Problems: 14, 34, 35, 45, 57, 63-75
- Combine heap with other algorithms
- Optimize for constraints

---

## Interview Preparation Checklist

- [ ] Can implement min heap from scratch
- [ ] Understand max heap using negation in Python
- [ ] Solve top k largest/smallest without looking
- [ ] Master two heaps pattern for median
- [ ] Can merge k sorted lists efficiently
- [ ] Understand greedy + heap for scheduling
- [ ] Know when to use heap vs. quickselect
- [ ] Can analyze time/space complexity
- [ ] Handle edge cases (empty input, k > n, etc.)
- [ ] Solve at least 40 heap problems

---

## Key Formulas to Remember

```python
# Array indices for heap
parent(i) = (i - 1) // 2
left_child(i) = 2 * i + 1
right_child(i) = 2 * i + 2

# Time complexities
Insert: O(log n)
Extract: O(log n)
Peek: O(1)
Heapify: O(n)
Heap Sort: O(n log n)

# Top k elements
k largest → min heap of size k
k smallest → max heap of size k (negate in Python)

# Two heaps median
If odd number: return top of larger heap
If even number: return average of both tops
```

---

Master these patterns and you'll be well-prepared for heap problems in interviews!
