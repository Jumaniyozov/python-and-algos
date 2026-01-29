# Problem-Solving Patterns - Theory

## Table of Contents

1. [Two Pointers Pattern](#two-pointers-pattern)
2. [Sliding Window Pattern](#sliding-window-pattern)
3. [Fast and Slow Pointers](#fast-and-slow-pointers)
4. [Merge Intervals Pattern](#merge-intervals-pattern)
5. [Cyclic Sort Pattern](#cyclic-sort-pattern)
6. [In-place Reversal of Linked List](#in-place-reversal-of-linked-list)
7. [Tree BFS (Level Order Traversal)](#tree-bfs-level-order-traversal)
8. [Tree DFS](#tree-dfs)
9. [Two Heaps Pattern](#two-heaps-pattern)
10. [Subsets Pattern](#subsets-pattern)
11. [Modified Binary Search](#modified-binary-search)
12. [Top K Elements Pattern](#top-k-elements-pattern)
13. [K-way Merge Pattern](#k-way-merge-pattern)
14. [Monotonic Stack Pattern](#monotonic-stack-pattern)
15. [Dynamic Programming Patterns](#dynamic-programming-patterns)

---

## Two Pointers Pattern

### When to Use

The Two Pointers pattern is useful when:
- Dealing with sorted arrays or linked lists
- Need to find pairs, triplets, or subarray with specific properties
- Want to avoid nested loops (reduce O(n²) to O(n))
- Processing elements from both ends or same direction
- Comparing elements at different positions

### How It Works

Use two pointers to iterate through the data structure:
1. **Opposite Ends**: One pointer starts at beginning, other at end
2. **Same Direction**: Both pointers move in same direction at different speeds
3. **Move Based on Condition**: Adjust pointers based on comparison or condition

### Variations

#### 1. Opposite Direction (Converging)

```python
def two_sum_sorted(arr, target):
    """
    Find pair that sums to target in sorted array.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum

    return None
```

#### 2. Same Direction (Fast and Slow)

```python
def remove_duplicates(arr):
    """
    Remove duplicates from sorted array in-place.
    Time: O(n), Space: O(1)
    """
    if not arr:
        return 0

    slow = 0  # Points to position for next unique element

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1  # Length of unique elements
```

#### 3. Partition Pattern

```python
def partition_array(arr, pivot):
    """
    Partition array around pivot (like quicksort).
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        if arr[left] < pivot:
            left += 1
        elif arr[right] >= pivot:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left
```

### Time and Space Complexity

- **Time**: O(n) - Single pass through data
- **Space**: O(1) - Only two pointer variables

### Common Problems

- Two Sum (sorted array)
- Three Sum
- Remove Duplicates
- Container With Most Water
- Trapping Rain Water
- Palindrome checking
- Dutch National Flag problem

---

## Sliding Window Pattern

### When to Use

The Sliding Window pattern is ideal when:
- Finding contiguous subarray/substring with specific property
- Problem involves sequences or arrays
- Need to track elements within a range
- Looking for max/min/average of subarrays of size K
- Finding longest/shortest substring with certain conditions

### How It Works

Maintain a window that slides across the data:
1. **Expand**: Add elements to window (move right pointer)
2. **Contract**: Remove elements from window (move left pointer)
3. **Track**: Update result when window meets condition

### Fixed-Size Window

```python
def max_sum_subarray(arr, k):
    """
    Find maximum sum of subarray of size k.
    Time: O(n), Space: O(1)
    """
    if len(arr) < k:
        return None

    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### Variable-Size Window

```python
def longest_substring_k_distinct(s, k):
    """
    Find longest substring with at most k distinct characters.
    Time: O(n), Space: O(k)
    """
    char_count = {}
    max_length = 0
    window_start = 0

    for window_end in range(len(s)):
        # Expand window
        right_char = s[window_end]
        char_count[right_char] = char_count.get(right_char, 0) + 1

        # Contract window while condition violated
        while len(char_count) > k:
            left_char = s[window_start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            window_start += 1

        # Update result
        max_length = max(max_length, window_end - window_start + 1)

    return max_length
```

### Template Code

```python
def sliding_window_template(arr):
    """
    Generic sliding window template.
    """
    window_start = 0
    result = 0

    for window_end in range(len(arr)):
        # 1. Add arr[window_end] to window

        # 2. While window is invalid:
        while window_invalid():
            # Remove arr[window_start] from window
            window_start += 1

        # 3. Update result based on current window
        result = update_result(result, window_end - window_start + 1)

    return result
```

### Time and Space Complexity

- **Time**: O(n) - Each element visited at most twice
- **Space**: O(k) - For tracking window contents (where k is window size or distinct elements)

### Common Problems

- Maximum Sum Subarray of Size K
- Longest Substring Without Repeating Characters
- Fruits Into Baskets
- Longest Substring with K Distinct Characters
- Minimum Window Substring
- Find All Anagrams in a String

---

## Fast and Slow Pointers

### When to Use

Fast and Slow Pointers (Floyd's Algorithm) is useful when:
- Detecting cycles in linked list or array
- Finding middle of linked list
- Finding k-th element from end
- Determining if structure forms a cycle

### How It Works

Use two pointers moving at different speeds:
- **Slow pointer**: Moves one step at a time
- **Fast pointer**: Moves two steps at a time
- **Cycle detection**: If fast catches slow, there's a cycle

### Cycle Detection

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    """
    Detect if linked list has cycle.
    Time: O(n), Space: O(1)
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

### Finding Cycle Start

```python
def find_cycle_start(head):
    """
    Find node where cycle begins.
    Time: O(n), Space: O(1)
    """
    slow = fast = head

    # Find meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    # Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
```

### Finding Middle Element

```python
def find_middle(head):
    """
    Find middle node of linked list.
    Time: O(n), Space: O(1)
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

### Time and Space Complexity

- **Time**: O(n) - At most 2n iterations
- **Space**: O(1) - Only two pointers

### Common Problems

- Linked List Cycle
- Linked List Cycle II (find cycle start)
- Happy Number
- Middle of Linked List
- Palindrome Linked List
- Reorder List

---

## Merge Intervals Pattern

### When to Use

Merge Intervals pattern applies when:
- Dealing with overlapping intervals
- Need to merge, insert, or check intersection of intervals
- Scheduling or calendar problems
- Range overlap detection

### How It Works

1. **Sort intervals** by start time
2. **Iterate and merge** overlapping intervals
3. **Track current interval** being built

### Basic Merge

```python
def merge_intervals(intervals):
    """
    Merge overlapping intervals.
    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]

        if current[0] <= last_merged[1]:
            # Overlapping: merge
            merged[-1] = [last_merged[0], max(last_merged[1], current[1])]
        else:
            # Non-overlapping: add new interval
            merged.append(current)

    return merged
```

### Insert Interval

```python
def insert_interval(intervals, new_interval):
    """
    Insert interval and merge if necessary.
    Time: O(n), Space: O(n)
    """
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
```

### Time and Space Complexity

- **Time**: O(n log n) for sorting, O(n) for merging
- **Space**: O(n) for result

### Common Problems

- Merge Intervals
- Insert Interval
- Interval List Intersections
- Employee Free Time
- Meeting Rooms I & II
- Minimum Meeting Rooms

---

## Cyclic Sort Pattern

### When to Use

Cyclic Sort is perfect when:
- Array contains numbers in given range (usually 1 to n)
- Need to find missing or duplicate numbers
- Can modify array in-place
- Numbers should be at their correct index positions

### How It Works

Place each number at its correct index (number i goes to index i-1):
1. **Iterate through array**
2. **If number not at correct position**, swap with element at correct position
3. **Repeat until number is at correct position or we find duplicate**

### Basic Cyclic Sort

```python
def cyclic_sort(nums):
    """
    Sort array containing numbers from 1 to n.
    Time: O(n), Space: O(1)
    """
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1

        if nums[i] != nums[correct_index]:
            # Swap to correct position
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1

    return nums
```

### Find Missing Number

```python
def find_missing_number(nums):
    """
    Find missing number in array containing 0 to n.
    Time: O(n), Space: O(1)
    """
    i = 0
    n = len(nums)

    # Place each number at its index
    while i < n:
        correct_index = nums[i]
        if nums[i] < n and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1

    # Find the missing number
    for i in range(n):
        if nums[i] != i:
            return i

    return n
```

### Find Duplicate Number

```python
def find_duplicate(nums):
    """
    Find duplicate in array of n+1 integers (1 to n).
    Time: O(n), Space: O(1)
    """
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            correct_index = nums[i] - 1
            if nums[i] == nums[correct_index]:
                return nums[i]  # Found duplicate
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1

    return -1
```

### Time and Space Complexity

- **Time**: O(n) - Each number swapped at most once
- **Space**: O(1) - In-place sorting

### Common Problems

- Missing Number
- Find All Missing Numbers
- Find Duplicate Number
- Find All Duplicates
- First Missing Positive
- Find Corrupt Pair

---

## In-place Reversal of Linked List

### When to Use

Use in-place reversal when:
- Need to reverse linked list or part of it
- Want O(1) space complexity
- Modifying original list is acceptable

### How It Works

Reverse pointers one by one:
1. **Track three nodes**: previous, current, next
2. **Reverse current's pointer** to previous
3. **Move all three pointers** one step forward

### Basic Reversal

```python
def reverse_linked_list(head):
    """
    Reverse entire linked list.
    Time: O(n), Space: O(1)
    """
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
```

### Reverse Sublist

```python
def reverse_between(head, left, right):
    """
    Reverse sublist from position left to right.
    Time: O(n), Space: O(1)
    """
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move to node before left
    for _ in range(left - 1):
        prev = prev.next

    # Reverse from left to right
    current = prev.next
    for _ in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next
```

### Reverse in K-Groups

```python
def reverse_k_group(head, k):
    """
    Reverse linked list in groups of k.
    Time: O(n), Space: O(1)
    """
    def reverse_group(start, k):
        prev = None
        current = start
        for _ in range(k):
            if not current:
                return prev, start
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev, start

    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy

    while True:
        kth_node = prev_group_end
        for _ in range(k):
            kth_node = kth_node.next
            if not kth_node:
                return dummy.next

        next_group_start = kth_node.next
        new_head, new_tail = reverse_group(prev_group_end.next, k)

        prev_group_end.next = new_head
        new_tail.next = next_group_start
        prev_group_end = new_tail
```

### Time and Space Complexity

- **Time**: O(n) - Single pass
- **Space**: O(1) - Only pointer variables

### Common Problems

- Reverse Linked List
- Reverse Linked List II
- Reverse Nodes in k-Group
- Rotate List
- Swap Nodes in Pairs
- Palindrome Linked List

---

## Tree BFS (Level Order Traversal)

### When to Use

Tree BFS is ideal when:
- Need to process tree level by level
- Finding shortest path in tree
- Need level-order traversal
- Solving problems involving tree levels or depths

### How It Works

Use a queue to process nodes level by level:
1. **Start with root** in queue
2. **Process all nodes** at current level
3. **Add children** of current level to queue
4. **Repeat** until queue is empty

### Basic Level Order

```python
from collections import deque

def level_order_traversal(root):
    """
    Traverse tree level by level.
    Time: O(n), Space: O(n)
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

### Zigzag Level Order

```python
def zigzag_level_order(root):
    """
    Traverse in zigzag pattern.
    Time: O(n), Space: O(n)
    """
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        current_level = deque()

        for _ in range(level_size):
            node = queue.popleft()

            if left_to_right:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(current_level))
        left_to_right = not left_to_right

    return result
```

### Template Code

```python
def bfs_template(root):
    """
    Generic BFS template.
    """
    if not root:
        return result_for_empty_tree

    queue = deque([root])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            # Process node
            # ...

            # Add children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
```

### Time and Space Complexity

- **Time**: O(n) - Visit each node once
- **Space**: O(n) - Queue stores up to one level (worst case: n/2 for complete tree)

### Common Problems

- Binary Tree Level Order Traversal
- Zigzag Level Order Traversal
- Binary Tree Right Side View
- Average of Levels in Binary Tree
- Minimum Depth of Binary Tree
- Maximum Depth of Binary Tree
- Level Order Successor

---

## Tree DFS

### When to Use

Tree DFS is useful when:
- Exploring all paths from root to leaf
- Need inorder/preorder/postorder traversal
- Solving problems involving root-to-leaf paths
- Tree structure modification problems

### Traversal Types

#### Preorder (Root → Left → Right)

```python
def preorder_traversal(root):
    """
    Preorder: Process root, then left, then right.
    Time: O(n), Space: O(h) where h is height
    """
    result = []

    def dfs(node):
        if not node:
            return

        result.append(node.val)  # Process root
        dfs(node.left)          # Process left
        dfs(node.right)         # Process right

    dfs(root)
    return result
```

#### Inorder (Left → Root → Right)

```python
def inorder_traversal(root):
    """
    Inorder: Process left, then root, then right.
    For BST, this gives sorted order.
    Time: O(n), Space: O(h)
    """
    result = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)          # Process left
        result.append(node.val)  # Process root
        dfs(node.right)         # Process right

    dfs(root)
    return result
```

#### Postorder (Left → Right → Root)

```python
def postorder_traversal(root):
    """
    Postorder: Process left, then right, then root.
    Time: O(n), Space: O(h)
    """
    result = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)          # Process left
        dfs(node.right)         # Process right
        result.append(node.val)  # Process root

    dfs(root)
    return result
```

### Path Sum Problems

```python
def has_path_sum(root, target_sum):
    """
    Check if root-to-leaf path sums to target.
    Time: O(n), Space: O(h)
    """
    def dfs(node, current_sum):
        if not node:
            return False

        current_sum += node.val

        # Check if leaf node with target sum
        if not node.left and not node.right:
            return current_sum == target_sum

        # Recurse on children
        return dfs(node.left, current_sum) or dfs(node.right, current_sum)

    return dfs(root, 0)
```

### When to Use Each Traversal

```
Preorder:  Use when you need to explore root before leaves
           - Tree copying, serialization
           - Prefix expression evaluation

Inorder:   Use for BST operations
           - Getting sorted elements
           - BST validation

Postorder: Use when you need to process children before parent
           - Deleting tree
           - Postfix expression evaluation
           - Calculating subtree properties
```

### Time and Space Complexity

- **Time**: O(n) - Visit each node once
- **Space**: O(h) - Recursion stack (h is height)
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)

### Common Problems

- Path Sum I, II, III
- Sum Root to Leaf Numbers
- Binary Tree Maximum Path Sum
- Diameter of Binary Tree
- Lowest Common Ancestor
- Validate BST
- Balanced Binary Tree

---

## Two Heaps Pattern

### When to Use

Two Heaps pattern is useful when:
- Finding median in stream of numbers
- Dividing dataset into two halves
- Need to track both min and max efficiently
- Maintaining dynamic sorted order

### How It Works

Use two heaps to partition data:
- **Max heap**: Stores smaller half of numbers
- **Min heap**: Stores larger half of numbers
- **Median**: Either max of max-heap or average of both tops

### Find Median in Data Stream

```python
import heapq

class MedianFinder:
    """
    Find median from data stream.
    Time: O(log n) for insert, O(1) for median
    Space: O(n)
    """
    def __init__(self):
        self.small = []  # Max heap (invert values)
        self.large = []  # Min heap

    def add_num(self, num):
        # Add to max heap (small half)
        heapq.heappush(self.small, -num)

        # Balance: move largest from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance sizes: large should not have more than small
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
```

### Sliding Window Median

```python
def median_sliding_window(nums, k):
    """
    Find median of each window of size k.
    Time: O(n * k), Space: O(k)
    """
    def get_median(window):
        sorted_window = sorted(window)
        mid = k // 2
        if k % 2 == 0:
            return (sorted_window[mid-1] + sorted_window[mid]) / 2.0
        return float(sorted_window[mid])

    result = []
    window = []

    for i in range(len(nums)):
        window.append(nums[i])

        if len(window) == k:
            result.append(get_median(window))
            window.pop(0)

    return result
```

### Time and Space Complexity

- **Time**: O(log n) for insertion, O(1) for median
- **Space**: O(n) for storing n elements

### Common Problems

- Find Median from Data Stream
- Sliding Window Median
- IPO (Maximize Capital)
- Next Interval

---

## Subsets Pattern

### When to Use

Subsets pattern applies when:
- Generating all combinations or permutations
- Need to explore all possible solutions
- Backtracking problems
- Problems asking for "all possible" results

### How It Works

Use backtracking to build solutions incrementally:
1. **Choose**: Pick an element to include
2. **Explore**: Recurse with that choice
3. **Unchoose**: Backtrack and try next option

### Generate All Subsets

```python
def subsets(nums):
    """
    Generate all subsets (power set).
    Time: O(2^n), Space: O(2^n)
    """
    result = []

    def backtrack(start, current):
        result.append(current[:])

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

### Generate Permutations

```python
def permutations(nums):
    """
    Generate all permutations.
    Time: O(n!), Space: O(n!)
    """
    result = []

    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return

        for num in nums:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()

    backtrack([])
    return result
```

### Combination Sum

```python
def combination_sum(candidates, target):
    """
    Find all combinations that sum to target.
    Time: O(2^n), Space: O(target)
    """
    result = []

    def backtrack(start, current, current_sum):
        if current_sum == target:
            result.append(current[:])
            return

        if current_sum > target:
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, current_sum + candidates[i])
            current.pop()

    backtrack(0, [], 0)
    return result
```

### Template Code

```python
def backtracking_template(nums):
    """
    Generic backtracking template.
    """
    result = []

    def backtrack(start, current):
        # Base case: solution found
        if is_valid_solution(current):
            result.append(current[:])
            return

        # Try all possibilities
        for i in range(start, len(nums)):
            # Choose
            current.append(nums[i])

            # Explore
            backtrack(i + 1, current)

            # Unchoose (backtrack)
            current.pop()

    backtrack(0, [])
    return result
```

### Time and Space Complexity

- **Time**: O(2^n) for subsets, O(n!) for permutations
- **Space**: O(n) for recursion depth

### Common Problems

- Subsets I & II
- Permutations I & II
- Combinations
- Combination Sum I, II, III
- Palindrome Partitioning
- Letter Combinations of Phone Number

---

## Modified Binary Search

### When to Use

Modified Binary Search works when:
- Array is sorted or rotated
- Finding target or insertion position
- Search space can be reduced by half
- Problem has monotonic property

### Variations

#### 1. Find First/Last Occurrence

```python
def binary_search_first(arr, target):
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

#### 2. Search in Rotated Array

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
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

#### 3. Find Peak Element

```python
def find_peak_element(nums):
    """
    Find a peak element (greater than neighbors).
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[mid + 1]:
            # Peak is on left side (including mid)
            right = mid
        else:
            # Peak is on right side
            left = mid + 1

    return left
```

### Template Code

```python
def binary_search_template(arr, target):
    """
    Generic binary search template.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if condition_met(arr[mid], target):
            return mid
        elif go_left(arr[mid], target):
            right = mid - 1
        else:
            left = mid + 1

    return -1
```

### Time and Space Complexity

- **Time**: O(log n) - Halves search space each iteration
- **Space**: O(1) - Only pointer variables

### Common Problems

- Binary Search
- Search in Rotated Sorted Array I & II
- Find Minimum in Rotated Sorted Array
- Find Peak Element
- Search Insert Position
- First Bad Version
- Kth Smallest Element in Sorted Matrix

---

## Top K Elements Pattern

### When to Use

Top K Elements pattern is ideal when:
- Finding K largest/smallest elements
- Need K most frequent elements
- Solving optimization problems with K constraint
- Can use heap to maintain K elements

### How It Works

Use a heap of size K:
- **Min heap** for K largest elements
- **Max heap** for K smallest elements
- **Maintain heap size K** by removing root when size exceeds K

### K Largest Elements

```python
import heapq

def find_k_largest(nums, k):
    """
    Find k largest elements.
    Time: O(n log k), Space: O(k)
    """
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return sorted(min_heap, reverse=True)
```

### K Most Frequent Elements

```python
def top_k_frequent(nums, k):
    """
    Find k most frequent elements.
    Time: O(n log k), Space: O(n)
    """
    from collections import Counter

    count = Counter(nums)

    # Use min heap with negative frequencies
    return heapq.nlargest(k, count.keys(), key=count.get)
```

### Kth Largest in Stream

```python
class KthLargest:
    """
    Find kth largest element in stream.
    Time: O(log k) per add, Space: O(k)
    """
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
```

### Time and Space Complexity

- **Time**: O(n log k) - n insertions, each O(log k)
- **Space**: O(k) - Heap stores k elements

### Common Problems

- Kth Largest Element in Array
- K Closest Points to Origin
- Top K Frequent Elements
- Kth Largest Element in Stream
- Find K Pairs with Smallest Sums
- Reorganize String

---

## K-way Merge Pattern

### When to Use

K-way Merge applies when:
- Merging K sorted lists/arrays
- Finding smallest/largest element from K sources
- Problems involving K sorted sequences

### How It Works

Use a min heap to track smallest element from each list:
1. **Add first element** from each list to heap
2. **Extract min** from heap
3. **Add next element** from same list to heap
4. **Repeat** until all elements processed

### Merge K Sorted Lists

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists):
    """
    Merge k sorted linked lists.
    Time: O(n log k), Space: O(k)
    """
    min_heap = []

    # Add first node from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst.val, i, lst))

    dummy = ListNode(0)
    current = dummy

    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next
```

### Kth Smallest in Sorted Matrix

```python
def kth_smallest_in_matrix(matrix, k):
    """
    Find kth smallest element in row and column sorted matrix.
    Time: O(k log n), Space: O(n)
    """
    n = len(matrix)
    min_heap = []

    # Add first element from each row
    for i in range(min(k, n)):
        heapq.heappush(min_heap, (matrix[i][0], i, 0))

    result = 0
    for _ in range(k):
        result, row, col = heapq.heappop(min_heap)

        if col + 1 < len(matrix[row]):
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))

    return result
```

### Time and Space Complexity

- **Time**: O(n log k) where n is total elements, k is number of lists
- **Space**: O(k) for heap

### Common Problems

- Merge K Sorted Lists
- Kth Smallest Element in Sorted Matrix
- Smallest Range Covering Elements from K Lists
- Find K Pairs with Smallest Sums

---

## Monotonic Stack Pattern

### When to Use

Monotonic Stack is useful when:
- Finding next greater/smaller element
- Need to track increasing/decreasing sequence
- Problems involving visibility or spanning
- Can eliminate elements that won't be useful

### How It Works

Maintain stack in monotonic order:
- **Increasing stack**: Elements in increasing order (for next smaller)
- **Decreasing stack**: Elements in decreasing order (for next greater)
- **Pop elements** that violate monotonic property

### Next Greater Element

```python
def next_greater_elements(nums):
    """
    Find next greater element for each element.
    Time: O(n), Space: O(n)
    """
    result = [-1] * len(nums)
    stack = []  # Store indices

    for i in range(len(nums)):
        # Pop elements smaller than current
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]

        stack.append(i)

    return result
```

### Daily Temperatures

```python
def daily_temperatures(temperatures):
    """
    Find number of days until warmer temperature.
    Time: O(n), Space: O(n)
    """
    result = [0] * len(temperatures)
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx

        stack.append(i)

    return result
```

### Largest Rectangle in Histogram

```python
def largest_rectangle_histogram(heights):
    """
    Find largest rectangle in histogram.
    Time: O(n), Space: O(n)
    """
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height_idx = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, heights[height_idx] * width)

        stack.append(i)

    while stack:
        height_idx = stack.pop()
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, heights[height_idx] * width)

    return max_area
```

### Time and Space Complexity

- **Time**: O(n) - Each element pushed and popped at most once
- **Space**: O(n) - Stack storage

### Common Problems

- Next Greater Element I & II
- Daily Temperatures
- Largest Rectangle in Histogram
- Trapping Rain Water
- Remove K Digits
- Online Stock Span

---

## Dynamic Programming Patterns

### Common DP Patterns

Dynamic Programming has several recurring patterns:

#### 1. 0/1 Knapsack

**When to Use**: Can include item at most once

```python
def knapsack(weights, values, capacity):
    """
    0/1 Knapsack problem.
    Time: O(n × capacity), Space: O(n × capacity)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                # Max of include vs exclude
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
```

#### 2. Unbounded Knapsack

**When to Use**: Can include item unlimited times

```python
def unbounded_knapsack(weights, values, capacity):
    """
    Unbounded knapsack (can reuse items).
    Time: O(n × capacity), Space: O(capacity)
    """
    dp = [0] * (capacity + 1)

    for w in range(capacity + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]
```

#### 3. Fibonacci Pattern (Linear DP)

```python
def fibonacci(n):
    """
    Fibonacci using DP.
    Time: O(n), Space: O(1)
    """
    if n <= 1:
        return n

    prev, curr = 0, 1

    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr
```

#### 4. Longest Common Subsequence (LCS)

```python
def longest_common_subsequence(s1, s2):
    """
    Find length of longest common subsequence.
    Time: O(m × n), Space: O(m × n)
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

#### 5. Longest Increasing Subsequence (LIS)

```python
def longest_increasing_subsequence(nums):
    """
    Find length of longest increasing subsequence.
    Time: O(n²), Space: O(n)
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
```

### DP Problem-Solving Steps

```
1. Identify if it's a DP problem:
   - Optimal substructure?
   - Overlapping subproblems?

2. Define the state:
   - What does dp[i] represent?
   - What are the dimensions?

3. Find the recurrence relation:
   - How to compute dp[i] from previous states?

4. Initialize base cases:
   - What are the smallest subproblems?

5. Determine traversal order:
   - Bottom-up or top-down?
   - Which direction to iterate?

6. Optimize space:
   - Can we reduce dimensions?
   - Rolling array technique?
```

### Time and Space Complexity

Varies by problem:
- **1D DP**: Usually O(n) time and space
- **2D DP**: Usually O(n²) time and space
- **Space optimization**: Often can reduce to O(n) or O(1)

### Common DP Problems

- Climbing Stairs
- House Robber I & II
- Coin Change I & II
- Longest Common Subsequence
- Longest Increasing Subsequence
- Edit Distance
- Maximum Subarray
- Unique Paths
- Partition Equal Subset Sum

---

## Pattern Selection Guide

### Quick Reference

```
Input Type              Likely Pattern
─────────────────────────────────────────────────
Sorted array           Two Pointers, Binary Search
Subarray/substring     Sliding Window
Linked list            Fast/Slow Pointers, Reversal
Intervals              Merge Intervals
Numbers 1 to n         Cyclic Sort
Tree level by level    BFS
Tree paths             DFS
Find median            Two Heaps
All combinations       Subsets/Backtracking
K largest/smallest     Top K Elements
K sorted lists         K-way Merge
Next greater/smaller   Monotonic Stack
Optimal solution       Dynamic Programming
```

### Problem Keywords

```
Keywords                Pattern
─────────────────────────────────────────────────
"two sum"              Two Pointers
"subarray"             Sliding Window
"cycle"                Fast/Slow Pointers
"merge", "overlap"     Merge Intervals
"missing number"       Cyclic Sort
"reverse"              In-place Reversal
"level"                Tree BFS
"path"                 Tree DFS
"median"               Two Heaps
"all possible"         Subsets
"sorted array"         Binary Search
"k largest"            Top K Elements
"k lists"              K-way Merge
"next greater"         Monotonic Stack
"maximum/minimum"      Dynamic Programming
```
