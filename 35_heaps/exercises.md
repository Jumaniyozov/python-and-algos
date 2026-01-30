# Chapter 35: Heaps - Exercises

## Instructions

- Try to solve each problem without looking at the solution first
- Start with Easy problems, then progress to Medium and Hard
- For each problem, analyze the time and space complexity
- Consider multiple approaches and trade-offs

Solutions are available in `solutions.md`.

---

## Easy Problems

### E1: Kth Largest Element in Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in sorted order, not the kth distinct element.

```python
def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Find kth largest element (1-indexed).

    Example 1:
        Input: nums = [3,2,1,5,6,4], k = 2
        Output: 5

    Example 2:
        Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
        Output: 4

    Constraints:
        - 1 <= k <= nums.length <= 10^5
        - -10^4 <= nums[i] <= 10^4
    """
    pass
```

---

### E2: Last Stone Weight

You have stones with different weights. Each turn, choose the two heaviest stones and smash them together. If they have different weights, the remaining stone has weight x - y.

```python
def last_stone_weight(stones: List[int]) -> int:
    """
    Return weight of last remaining stone, or 0 if none remain.

    Example:
        Input: stones = [2,7,4,1,8,1]
        Output: 1
        Explanation:
        - Combine 7 and 8 → 1 (8-7), stones = [2,4,1,1,1]
        - Combine 2 and 4 → 2, stones = [2,1,1,1]
        - Combine 2 and 1 → 1, stones = [1,1,1]
        - Combine 1 and 1 → 0, stones = [1]
        - Return 1

    Constraints:
        - 1 <= stones.length <= 30
        - 1 <= stones[i] <= 1000
    """
    pass
```

---

### E3: Relative Ranks

Given scores of athletes, assign ranks: "Gold Medal", "Silver Medal", "Bronze Medal", and 4th, 5th, etc.

```python
def find_relative_ranks(score: List[int]) -> List[str]:
    """
    Return array of ranks for each athlete.

    Example:
        Input: score = [5,4,3,2,1]
        Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

    Example 2:
        Input: score = [10,3,8,9,4]
        Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

    Constraints:
        - n == score.length
        - 1 <= n <= 10^4
        - 0 <= score[i] <= 10^6
        - All values in score are unique
    """
    pass
```

---

### E4: Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream.

```python
class KthLargest:
    """
    Design class that maintains kth largest element in stream.

    Example:
        kthLargest = KthLargest(3, [4, 5, 8, 2])
        kthLargest.add(3)   # returns 4
        kthLargest.add(5)   # returns 5
        kthLargest.add(10)  # returns 5
        kthLargest.add(9)   # returns 8
        kthLargest.add(4)   # returns 8

    Constraints:
        - 1 <= k <= 10^4
        - 0 <= nums.length <= 10^4
        - -10^4 <= nums[i] <= 10^4
        - -10^4 <= val <= 10^4
        - At most 10^4 calls to add
    """

    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass
```

---

### E5: Minimum Cost to Connect Sticks

You have some sticks with positive integer lengths. Connect sticks in pairs, where the cost is the sum of their lengths. Find minimum total cost.

```python
def connect_sticks(sticks: List[int]) -> int:
    """
    Return minimum cost to connect all sticks.

    Example:
        Input: sticks = [2,4,3]
        Output: 14
        Explanation:
        - Connect 2 and 3 for cost 5, sticks = [5,4]
        - Connect 5 and 4 for cost 9, sticks = [9]
        - Total cost: 5 + 9 = 14

    Example 2:
        Input: sticks = [1,8,3,5]
        Output: 30
        Explanation:
        - Connect 1 and 3 for cost 4, sticks = [4,8,5]
        - Connect 4 and 5 for cost 9, sticks = [9,8]
        - Connect 9 and 8 for cost 17
        - Total: 4 + 9 + 17 = 30

    Constraints:
        - 1 <= sticks.length <= 10^4
        - 1 <= sticks[i] <= 10^4
    """
    pass
```

---

### E6: Meeting Rooms

Given an array of meeting time intervals, determine if a person could attend all meetings.

```python
def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """
    Check if person can attend all meetings (no overlap).

    Example 1:
        Input: intervals = [[0,30],[5,10],[15,20]]
        Output: false
        Explanation: [0,30] and [5,10] overlap

    Example 2:
        Input: intervals = [[7,10],[2,4]]
        Output: true

    Constraints:
        - 0 <= intervals.length <= 10^4
        - intervals[i].length == 2
        - 0 <= start_i < end_i <= 10^6
    """
    pass
```

---

### E7: Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

```python
def frequency_sort(s: str) -> str:
    """
    Return string sorted by character frequency (descending).

    Example 1:
        Input: s = "tree"
        Output: "eert" or "eetr"
        Explanation: 'e' appears twice, 't' and 'r' once

    Example 2:
        Input: s = "cccaaa"
        Output: "aaaccc" or "cccaaa"

    Example 3:
        Input: s = "Aabb"
        Output: "bbAa" or "bbaA"

    Constraints:
        - 1 <= s.length <= 5 * 10^5
        - s consists of uppercase/lowercase English letters and digits
    """
    pass
```

---

## Medium Problems

### M1: Top K Frequent Elements

Given an integer array and an integer k, return the k most frequent elements.

```python
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Return k most frequent elements in any order.

    Example 1:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]

    Example 2:
        Input: nums = [1], k = 1
        Output: [1]

    Constraints:
        - 1 <= nums.length <= 10^5
        - -10^4 <= nums[i] <= 10^4
        - k is in range [1, number of unique elements]
        - Answer is guaranteed to be unique
    """
    pass
```

---

### M2: K Closest Points to Origin

Given array of points on X-Y plane and integer k, return k closest points to origin (0, 0).

```python
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Return k closest points. Answer can be in any order.

    Distance from point (x,y) to origin: sqrt(x^2 + y^2)

    Example 1:
        Input: points = [[1,3],[-2,2]], k = 1
        Output: [[-2,2]]
        Explanation: Distance: (1,3) = sqrt(10), (-2,2) = sqrt(8)

    Example 2:
        Input: points = [[3,3],[5,-1],[-2,4]], k = 2
        Output: [[3,3],[-2,4]]

    Constraints:
        - 1 <= k <= points.length <= 10^4
        - -10^4 <= xi, yi <= 10^4
    """
    pass
```

---

### M3: Task Scheduler

Given char array tasks representing CPU tasks and integer n (cooling time), return minimum intervals needed.

```python
def least_interval(tasks: List[str], n: int) -> int:
    """
    Return minimum number of intervals needed to complete all tasks.

    Same task must be separated by at least n intervals.
    CPU can be idle during cooling period.

    Example 1:
        Input: tasks = ["A","A","A","B","B","B"], n = 2
        Output: 8
        Explanation: A -> B -> idle -> A -> B -> idle -> A -> B

    Example 2:
        Input: tasks = ["A","A","A","B","B","B"], n = 0
        Output: 6
        Explanation: No cooling needed: A -> A -> A -> B -> B -> B

    Example 3:
        Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
        Output: 16
        Explanation: One optimal order: A->B->C->A->D->E->A->F->G->A->idle->idle->A->idle->idle->A

    Constraints:
        - 1 <= tasks.length <= 10^4
        - tasks[i] is uppercase English letter
        - 0 <= n <= 100
    """
    pass
```

---

### M4: Meeting Rooms II

Find minimum number of conference rooms required for all meetings.

```python
def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Return minimum number of rooms needed.

    Example 1:
        Input: intervals = [[0,30],[5,10],[15,20]]
        Output: 2
        Explanation: [0,30] overlaps with both others

    Example 2:
        Input: intervals = [[7,10],[2,4]]
        Output: 1

    Constraints:
        - 1 <= intervals.length <= 10^4
        - 0 <= start_i < end_i <= 10^6
    """
    pass
```

---

### M5: Reorganize String

Rearrange string so no two adjacent characters are the same. Return any valid answer or empty string if impossible.

```python
def reorganize_string(s: str) -> str:
    """
    Return reorganized string or "" if impossible.

    Example 1:
        Input: s = "aab"
        Output: "aba"

    Example 2:
        Input: s = "aaab"
        Output: ""
        Explanation: Impossible

    Constraints:
        - 1 <= s.length <= 500
        - s consists of lowercase English letters
    """
    pass
```

---

### M6: Kth Smallest Element in a Sorted Matrix

Given n x n matrix where rows and columns are sorted, find kth smallest element.

```python
def kth_smallest(matrix: List[List[int]], k: int) -> int:
    """
    Find kth smallest element (1-indexed).

    Example:
        Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
        Output: 13
        Explanation: Elements in order: [1,5,9,10,11,12,13,13,15]

    Constraints:
        - n == matrix.length == matrix[i].length
        - 1 <= n <= 300
        - -10^9 <= matrix[i][j] <= 10^9
        - All rows and columns sorted in ascending order
        - 1 <= k <= n^2
    """
    pass
```

---

### M7: Find K Pairs with Smallest Sums

Given two sorted arrays and integer k, find k pairs with smallest sums.

```python
def k_smallest_pairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    """
    Return k pairs (u, v) where u from nums1 and v from nums2.

    Example 1:
        Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
        Output: [[1,2],[1,4],[1,6]]
        Explanation: First 3 pairs: [1,2], [1,4], [1,6]

    Example 2:
        Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
        Output: [[1,1],[1,1]]

    Example 3:
        Input: nums1 = [1,2], nums2 = [3], k = 3
        Output: [[1,3],[2,3]]

    Constraints:
        - 1 <= nums1.length, nums2.length <= 10^5
        - -10^9 <= nums1[i], nums2[i] <= 10^9
        - nums1 and nums2 are sorted in ascending order
        - 1 <= k <= 10^4
    """
    pass
```

---

### M8: Ugly Number II

Find nth ugly number (positive number whose prime factors are 2, 3, or 5).

```python
def nth_ugly_number(n: int) -> int:
    """
    Return nth ugly number.

    1 is typically treated as ugly number.

    Example 1:
        Input: n = 10
        Output: 12
        Explanation: [1,2,3,4,5,6,8,9,10,12] are first 10 ugly numbers

    Example 2:
        Input: n = 1
        Output: 1

    Constraints:
        - 1 <= n <= 1690
    """
    pass
```

---

### M9: Furthest Building You Can Reach

Given array of building heights and bricks/ladders, find furthest building you can reach.

```python
def furthest_building(heights: List[int], bricks: int, ladders: int) -> int:
    """
    Return furthest building index (0-indexed).

    Use bricks or ladders to climb up. Ladder can climb any height.
    Bricks can only climb difference in height.

    Example 1:
        Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
        Output: 4
        Explanation: Starting at 0, you can follow this path:
        - 0->1 (down, no resources)
        - 1->2 (up 5, use 5 bricks)
        - 2->3 (down, no resources)
        - 3->4 (up 3, no more bricks, use ladder)
        - Can't go to 5 (up 5, no resources)

    Example 2:
        Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
        Output: 7

    Example 3:
        Input: heights = [14,3,19,3], bricks = 17, ladders = 0
        Output: 3

    Constraints:
        - 1 <= heights.length <= 10^5
        - 1 <= heights[i] <= 10^6
        - 0 <= bricks <= 10^9
        - 0 <= ladders <= heights.length
    """
    pass
```

---

### M10: Find Median from Data Stream

Design a data structure that supports adding numbers and finding median.

```python
class MedianFinder:
    """
    Design structure to find median from data stream.

    Example:
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        mf.findMedian()  # 1.5
        mf.addNum(3)
        mf.findMedian()  # 2.0

    Constraints:
        - -10^5 <= num <= 10^5
        - At most 5 * 10^4 calls to addNum and findMedian
    """

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        """Add integer to data structure."""
        pass

    def findMedian(self) -> float:
        """Return median of all elements so far."""
        pass
```

---

## Hard Problems

### H1: Merge K Sorted Lists

Merge k sorted linked lists and return as one sorted list.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge all linked lists into one sorted list.

    Example 1:
        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]

    Example 2:
        Input: lists = []
        Output: []

    Example 3:
        Input: lists = [[]]
        Output: []

    Constraints:
        - k == lists.length
        - 0 <= k <= 10^4
        - 0 <= lists[i].length <= 500
        - -10^4 <= lists[i][j] <= 10^4
        - Lists are sorted in ascending order
        - Sum of all list lengths <= 10^4
    """
    pass
```

---

### H2: Smallest Range Covering Elements from K Lists

Find smallest range that includes at least one number from each of k lists.

```python
def smallest_range(nums: List[List[int]]) -> List[int]:
    """
    Return smallest range [a, b] that includes at least one number from each list.

    If multiple answers, return the one with smallest a.

    Example 1:
        Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
        Output: [20,24]
        Explanation: [20,24] includes 24 from list1, 20 from list2, 22 from list3

    Example 2:
        Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
        Output: [1,1]

    Constraints:
        - nums.length == k
        - 1 <= k <= 3500
        - 1 <= nums[i].length <= 50
        - -10^5 <= nums[i][j] <= 10^5
        - nums[i] is sorted in ascending order
    """
    pass
```

---

### H3: Sliding Window Median

Find median in sliding window of size k.

```python
def median_sliding_window(nums: List[int], k: int) -> List[float]:
    """
    Return array of medians for each sliding window.

    Example 1:
        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [1.0,-1.0,-1.0,3.0,5.0,6.0]
        Explanation:
        Window [1,3,-1] → median 1
        Window [3,-1,-3] → median -1
        Window [-1,-3,5] → median -1
        Window [-3,5,3] → median 3
        Window [5,3,6] → median 5
        Window [3,6,7] → median 6

    Constraints:
        - 1 <= k <= nums.length <= 10^5
        - -2^31 <= nums[i] <= 2^31 - 1
    """
    pass
```

---

### H4: IPO

Given k projects with capital requirements and profits, maximize capital starting with w.

```python
def find_maximized_capital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    """
    Find maximum capital after completing at most k projects.

    Can only do project if current capital >= required capital.

    Example 1:
        Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
        Output: 4
        Explanation:
        - Start with w=0, do project 0 (capital=0, profit=1), now w=1
        - Do project 1 or 2 (both need capital=1, profit=2 or 3), choose project 2
        - Final capital: 0 + 1 + 3 = 4

    Example 2:
        Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
        Output: 6

    Constraints:
        - 1 <= k <= 10^5
        - 0 <= w <= 10^9
        - n == profits.length == capital.length
        - 1 <= n <= 10^5
        - 0 <= profits[i] <= 10^4
        - 0 <= capital[i] <= 10^9
    """
    pass
```

---

### H5: Super Ugly Number

Find nth super ugly number (positive number whose prime factors are in given array).

```python
def nth_super_ugly_number(n: int, primes: List[int]) -> int:
    """
    Return nth super ugly number.

    Example 1:
        Input: n = 12, primes = [2,7,13,19]
        Output: 32
        Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] are first 12

    Example 2:
        Input: n = 1, primes = [2,3,5]
        Output: 1

    Constraints:
        - 1 <= n <= 10^5
        - 1 <= primes.length <= 100
        - 2 <= primes[i] <= 1000
        - primes[i] is guaranteed to be prime
        - All primes[i] are unique and sorted
    """
    pass
```

---

### H6: Trapping Rain Water II

Given m x n matrix of heights, compute how much water can be trapped after raining.

```python
def trap_rain_water(height_map: List[List[int]]) -> int:
    """
    Return volume of water that can be trapped.

    Example 1:
        Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
        Output: 4

    Example 2:
        Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
        Output: 10

    Constraints:
        - m == heightMap.length
        - n == heightMap[i].length
        - 1 <= m, n <= 200
        - 0 <= heightMap[i][j] <= 2 * 10^4
    """
    pass
```

---

## Key Patterns

### Pattern 1: Top K Elements
- Use min heap of size k for k largest
- Use max heap of size k for k smallest
- Examples: E1, M1, M2

### Pattern 2: Two Heaps
- Split data into two halves
- Max heap for smaller half, min heap for larger half
- Examples: M10, H3

### Pattern 3: K-Way Merge
- Use heap to merge k sorted sequences
- Examples: H1, M6, M7, H2

### Pattern 4: Scheduling
- Use heap to track ongoing events
- Examples: M3, M4, M9

### Pattern 5: Stream Processing
- Maintain heap as data arrives
- Examples: E4, M10

---

## Complexity Goals

- **Easy**: O(n log k) or O(n log n)
- **Medium**: O(n log k) with optimization
- **Hard**: O(n log k) with multiple heaps or complex logic

Good luck solving these problems!
