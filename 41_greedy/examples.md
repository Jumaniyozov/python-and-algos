# Chapter 41: Greedy Algorithms - Examples

## Table of Contents
1. [Interval Problems](#interval-problems)
2. [Scheduling Problems](#scheduling-problems)
3. [Resource Allocation](#resource-allocation)
4. [Jump and Reach Problems](#jump-and-reach-problems)
5. [Partitioning Problems](#partitioning-problems)
6. [String and Array Greedy](#string-and-array-greedy)

---

## Interval Problems

### Example 1: Non-overlapping Intervals (LeetCode 435)

```python
def erase_overlap_intervals(intervals):
    """
    Minimum intervals to remove to make non-overlapping.

    Greedy: Sort by end time, keep earliest-ending intervals.

    Time: O(n log n)
    Space: O(1)
    """
    intervals.sort(key=lambda x: x[1])  # Sort by end time

    count = 0
    last_end = intervals[0][1]

    for i in range(1, len(intervals)):
        start, end = intervals[i]

        if start >= last_end:
            # Non-overlapping, keep it
            last_end = end
        else:
            # Overlapping, remove it
            count += 1

    return count

# Example
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(erase_overlap_intervals(intervals))  # 1 (remove [1,3])
```

---

### Example 2: Meeting Rooms II (LeetCode 253)

```python
import heapq

def min_meeting_rooms(intervals):
    """
    Minimum conference rooms needed.

    Greedy: Track overlapping meetings with min-heap.

    Time: O(n log n)
    Space: O(n)
    """
    intervals.sort(key=lambda x: x[0])  # Sort by start time

    rooms = []  # Min-heap of end times

    for start, end in intervals:
        # If earliest meeting ended, reuse room
        if rooms and start >= rooms[0]:
            heapq.heappop(rooms)

        # Add current meeting
        heapq.heappush(rooms, end)

    return len(rooms)

# Example
intervals = [[0,30],[5,10],[15,20]]
print(min_meeting_rooms(intervals))  # 2
```

---

### Example 3: Merge Intervals (LeetCode 56)

```python
def merge_intervals(intervals):
    """
    Merge all overlapping intervals.

    Greedy: Sort and merge consecutively.

    Time: O(n log n)
    Space: O(n)
    """
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            # Overlapping, merge
            merged[-1][1] = max(merged[-1][1], end)
        else:
            # Non-overlapping, add new interval
            merged.append([start, end])

    return merged

# Example
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))  # [[1,6],[8,10],[15,18]]
```

---

## Scheduling Problems

### Example 4: Task Scheduler (LeetCode 621)

```python
from collections import Counter
import heapq

def least_interval(tasks, n):
    """
    Minimum time to complete all tasks with cooldown n.

    Greedy: Schedule most frequent task first.

    Time: O(m log m) where m is unique tasks
    Space: O(m)
    """
    # Count task frequencies
    freq = Counter(tasks)

    # Max heap (use negative for max behavior)
    max_heap = [-count for count in freq.values()]
    heapq.heapify(max_heap)

    time = 0
    cooldown = []  # Tasks in cooldown

    while max_heap or cooldown:
        time += 1

        if max_heap:
            # Schedule task with highest frequency
            count = heapq.heappop(max_heap)
            count += 1  # Decrease frequency (was negative)

            if count < 0:  # Still has instances left
                cooldown.append((time + n, count))

        # Release tasks from cooldown
        if cooldown and cooldown[0][0] == time:
            _, count = cooldown.pop(0)
            heapq.heappush(max_heap, count)

    return time

# Example
tasks = ["A","A","A","B","B","B"]
n = 2
print(least_interval(tasks, n))  # 8: A->B->idle->A->B->idle->A->B
```

---

## Resource Allocation

### Example 5: Assign Cookies (LeetCode 455)

```python
def find_content_children(g, s):
    """
    Maximize children satisfied with cookies.

    Greedy: Sort both, give smallest sufficient cookie.

    Time: O(n log n + m log m)
    Space: O(1)
    """
    g.sort()  # Greed factors
    s.sort()  # Cookie sizes

    child = cookie = 0

    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            # Cookie satisfies child
            child += 1
        cookie += 1

    return child

# Example
g = [1,2,3]  # Children's greed
s = [1,1]    # Cookie sizes
print(find_content_children(g, s))  # 1
```

---

### Example 6: Boats to Save People (LeetCode 881)

```python
def num_rescue_boats(people, limit):
    """
    Minimum boats needed (each holds max 2 people, weight <= limit).

    Greedy: Pair heaviest with lightest.

    Time: O(n log n)
    Space: O(1)
    """
    people.sort()

    left, right = 0, len(people) - 1
    boats = 0

    while left <= right:
        # Try to pair heaviest with lightest
        if people[left] + people[right] <= limit:
            left += 1  # Both fit
        right -= 1  # Heaviest always goes
        boats += 1

    return boats

# Example
people = [3,2,2,1]
limit = 3
print(num_rescue_boats(people, limit))  # 3
```

---

## Jump and Reach Problems

### Example 7: Jump Game (LeetCode 55)

```python
def can_jump(nums):
    """
    Can reach last index?

    Greedy: Track farthest reachable.

    Time: O(n)
    Space: O(1)
    """
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False

        max_reach = max(max_reach, i + nums[i])

        if max_reach >= len(nums) - 1:
            return True

    return False

# Example
nums = [2,3,1,1,4]
print(can_jump(nums))  # True
```

---

### Example 8: Jump Game II (LeetCode 45)

```python
def jump(nums):
    """
    Minimum jumps to reach last index.

    Greedy: Track farthest reachable in current jump.

    Time: O(n)
    Space: O(1)
    """
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        # Reached end of current jump range
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps

# Example
nums = [2,3,1,1,4]
print(jump(nums))  # 2 (jump 1 step to index 1, then 3 steps to end)
```

---

### Example 9: Gas Station (LeetCode 134)

```python
def can_complete_circuit(gas, cost):
    """
    Starting station to complete circular route.

    Greedy: Start where surplus begins.

    Time: O(n)
    Space: O(1)
    """
    total_surplus = 0
    current_surplus = 0
    start = 0

    for i in range(len(gas)):
        surplus = gas[i] - cost[i]
        total_surplus += surplus
        current_surplus += surplus

        if current_surplus < 0:
            # Can't start from any station up to i
            start = i + 1
            current_surplus = 0

    return start if total_surplus >= 0 else -1

# Example
gas =  [1,2,3,4,5]
cost = [3,4,5,1,2]
print(can_complete_circuit(gas, cost))  # 3
```

---

## Partitioning Problems

### Example 10: Partition Labels (LeetCode 763)

```python
def partition_labels(s):
    """
    Partition string into max parts where each letter in at most one part.

    Greedy: Track last occurrence, extend partition.

    Time: O(n)
    Space: O(1)
    """
    # Find last occurrence of each character
    last = {char: i for i, char in enumerate(s)}

    partitions = []
    start = 0
    end = 0

    for i, char in enumerate(s):
        end = max(end, last[char])

        if i == end:
            # Reached end of current partition
            partitions.append(end - start + 1)
            start = i + 1

    return partitions

# Example
s = "ababcbacadefegdehijhklij"
print(partition_labels(s))  # [9,7,8]
```

---

## String and Array Greedy

### Example 11: Remove K Digits (LeetCode 402)

```python
def remove_k_digits(num, k):
    """
    Remove k digits to make smallest number.

    Greedy: Remove larger digits from left.

    Time: O(n)
    Space: O(n)
    """
    stack = []

    for digit in num:
        # Remove larger digits while possible
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    # Remove remaining k digits from end
    if k > 0:
        stack = stack[:-k]

    # Remove leading zeros
    result = ''.join(stack).lstrip('0')

    return result if result else '0'

# Example
num = "1432219"
k = 3
print(remove_k_digits(num, k))  # "1219"
```

---

### Example 12: Maximum Swap (LeetCode 670)

```python
def maximum_swap(num):
    """
    Swap two digits once to maximize number.

    Greedy: Find rightmost max digit, swap with leftmost smaller.

    Time: O(n)
    Space: O(n)
    """
    digits = list(str(num))
    n = len(digits)

    # Track last occurrence of each digit
    last = {int(d): i for i, d in enumerate(digits)}

    for i, digit in enumerate(digits):
        # Try to find larger digit to swap with
        for d in range(9, int(digit), -1):
            if last.get(d, -1) > i:
                # Swap
                digits[i], digits[last[d]] = digits[last[d]], digits[i]
                return int(''.join(digits))

    return num

# Example
num = 2736
print(maximum_swap(num))  # 7236
```

---

## Summary

These examples demonstrate core greedy patterns:

1. **Interval Problems**: Sort by end time, greedily select
2. **Scheduling**: Use priority queue for dynamic ordering
3. **Resource Allocation**: Sort and match greedily
4. **Jump Problems**: Track reachable positions
5. **Partitioning**: Extend partitions greedily
6. **String/Array**: Use stack or two pointers

**Key Techniques**:
- Sorting to establish order
- Priority queue for dynamic best choice
- Two pointers for pairing
- Stack for maintaining increasing/decreasing order
- Tracking last occurrence or farthest reach

Practice until you can recognize the greedy approach intuitively!
