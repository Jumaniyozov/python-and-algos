# Quick Reference Guide - Algorithms and Data Structures

**Essential patterns, templates, and cheat sheets for coding interviews**

---

## Table of Contents
1. [15 Essential Patterns](#15-essential-patterns)
2. [Data Structure Quick Reference](#data-structure-quick-reference)
3. [Algorithm Templates](#algorithm-templates)
4. [Time Complexity Cheat Sheet](#time-complexity-cheat-sheet)
5. [Top 100 Must-Practice Problems](#top-100-must-practice-problems)
6. [Interview Day Checklist](#interview-day-checklist)

---

## 15 Essential Patterns

Learn these patterns to solve 80% of coding interview problems. ([Full details in Chapter 28](28_patterns/README.md))

### 1. Two Pointers
**When to use:** Sorted arrays, pairs, triplets, partitioning
**Template:**
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process current pair
        if condition:
            left += 1
        else:
            right -= 1
```
**Key Problems:** Two Sum II, 3Sum, Container With Most Water

### 2. Sliding Window
**When to use:** Subarrays, substrings, contiguous elements
**Template:**
```python
def sliding_window(arr, k):
    window_sum = 0
    max_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
```
**Key Problems:** Longest Substring Without Repeating, Minimum Window Substring

### 3. Fast and Slow Pointers
**When to use:** Linked list cycles, middle of list
**Template:**
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
**Key Problems:** Linked List Cycle, Happy Number, Middle of Linked List

### 4. Merge Intervals
**When to use:** Overlapping intervals, scheduling
**Template:**
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    return merged
```
**Key Problems:** Merge Intervals, Insert Interval, Meeting Rooms II

### 5. Modified Binary Search
**When to use:** Sorted/rotated arrays, search space reduction
**Template:**
```python
def binary_search(arr, target):
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
**Key Problems:** Search in Rotated Sorted Array, Find Peak Element

### 6. Tree DFS
**When to use:** Tree traversal, path problems
**Template:**
```python
def dfs(root):
    if not root:
        return

    # Preorder: process root first
    # Process root
    dfs(root.left)
    dfs(root.right)
```
**Key Problems:** Maximum Depth, Path Sum, Invert Binary Tree

### 7. Tree BFS
**When to use:** Level-order traversal, shortest path in tree
**Template:**
```python
from collections import deque

def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)
    return result
```
**Key Problems:** Level Order Traversal, Right Side View, Zigzag Traversal

### 8. Top K Elements
**When to use:** Finding top/bottom K, Kth largest/smallest
**Template:**
```python
import heapq

def top_k_elements(arr, k):
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return list(min_heap)
```
**Key Problems:** Kth Largest Element, Top K Frequent Elements

### 9. Two Heaps
**When to use:** Median finding, dual priorities
**Template:**
```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max heap (negated)
        self.large = []  # min heap

    def addNum(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
```
**Key Problems:** Find Median from Data Stream, Sliding Window Median

### 10. Graph DFS
**When to use:** Connected components, cycle detection, path finding
**Template:**
```python
def dfs(graph, start, visited):
    if start in visited:
        return

    visited.add(start)
    for neighbor in graph[start]:
        dfs(graph, neighbor, visited)
```
**Key Problems:** Number of Islands, Clone Graph, Course Schedule

### 11. Graph BFS
**When to use:** Shortest path, level-wise processing
**Template:**
```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```
**Key Problems:** Word Ladder, Shortest Path in Binary Matrix

### 12. Union Find
**When to use:** Connected components, cycle detection in undirected graphs
**Template:**
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True
```
**Key Problems:** Number of Connected Components, Redundant Connection

### 13. Dynamic Programming
**When to use:** Overlapping subproblems, optimal substructure
**Template (1D):**
```python
def dp_1d(arr):
    if not arr:
        return 0

    dp = [0] * len(arr)
    dp[0] = arr[0]

    for i in range(1, len(arr)):
        dp[i] = max(dp[i-1], arr[i])  # State transition

    return dp[-1]
```
**Key Problems:** Climbing Stairs, House Robber, Coin Change

### 14. Backtracking
**When to use:** Permutations, combinations, constraint satisfaction
**Template:**
```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:])
        return

    for choice in choices:
        if is_valid(choice):
            path.append(choice)
            backtrack(path, get_next_choices())
            path.pop()  # Backtrack
```
**Key Problems:** Permutations, N-Queens, Sudoku Solver

### 15. Monotonic Stack
**When to use:** Next greater/smaller element
**Template:**
```python
def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result
```
**Key Problems:** Next Greater Element, Daily Temperatures

---

## Data Structure Quick Reference

### Arrays and Strings
**Time Complexity:**
- Access: O(1)
- Search: O(n)
- Insert: O(n)
- Delete: O(n)

**Common Operations:**
```python
# Reverse
arr[::-1]

# Sort
sorted(arr)  # Returns new
arr.sort()   # In-place

# Two pointers
left, right = 0, len(arr) - 1
```

**Chapter:** [29: Arrays and Strings](29_arrays_strings/README.md)

### Linked Lists
**Time Complexity:**
- Access: O(n)
- Search: O(n)
- Insert: O(1)
- Delete: O(1)

**Common Patterns:**
```python
# Fast & slow pointers
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

# Reverse
prev, curr = None, head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
```

**Chapter:** [30: Linked Lists](30_linked_lists/README.md)

### Stacks and Queues
**Stack (LIFO):**
```python
stack = []
stack.append(x)  # Push
stack.pop()      # Pop
stack[-1]        # Peek
```

**Queue (FIFO):**
```python
from collections import deque
queue = deque()
queue.append(x)     # Enqueue
queue.popleft()     # Dequeue
```

**Chapter:** [31: Stacks and Queues](31_stacks_queues/README.md)

### Hash Tables
**Time Complexity:**
- Search: O(1) average
- Insert: O(1) average
- Delete: O(1) average

**Common Patterns:**
```python
# Frequency counter
freq = {}
for item in arr:
    freq[item] = freq.get(item, 0) + 1

# Prefix sum
prefix = {0: 1}
curr_sum = 0
for num in arr:
    curr_sum += num
    # Use prefix for subarray problems
```

**Chapter:** [32: Hash Tables](32_hash_tables/README.md)

### Binary Trees
**Traversals:**
```python
# Inorder (Left-Root-Right)
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

# Preorder (Root-Left-Right)
def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

# Postorder (Left-Right-Root)
def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []

# Level-order (BFS)
from collections import deque
def levelorder(root):
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return result
```

**Chapter:** [33: Trees](33_trees/README.md)

### Heaps
**Min Heap in Python:**
```python
import heapq

heap = []
heapq.heappush(heap, item)  # O(log n)
smallest = heapq.heappop(heap)  # O(log n)
smallest = heap[0]  # Peek O(1)

# Max heap (negate values)
heapq.heappush(heap, -item)
```

**Chapter:** [35: Heaps](35_heaps/README.md)

### Graphs
**Representations:**
```python
# Adjacency List (most common)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# From edge list
edges = [[0,1], [1,2], [2,0]]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # Undirected
```

**Chapter:** [36: Graphs](36_graphs/README.md)

---

## Algorithm Templates

### Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found
```

### Topological Sort (Kahn's Algorithm)
```python
from collections import deque, defaultdict

def topological_sort(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(n) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == n else []
```

### Dijkstra's Algorithm
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        if curr_dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = curr_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
```

---

## Time Complexity Cheat Sheet

| Data Structure | Access | Search | Insert | Delete |
|----------------|--------|--------|--------|--------|
| **Array** | O(1) | O(n) | O(n) | O(n) |
| **Linked List** | O(n) | O(n) | O(1) | O(1) |
| **Stack** | O(n) | O(n) | O(1) | O(1) |
| **Queue** | O(n) | O(n) | O(1) | O(1) |
| **Hash Table** | - | O(1)* | O(1)* | O(1)* |
| **Binary Tree** | O(n) | O(n) | O(n) | O(n) |
| **BST (balanced)** | O(log n) | O(log n) | O(log n) | O(log n) |
| **Heap** | O(n) | O(n) | O(log n) | O(log n) |

*Average case

### Common Algorithm Complexities

| Algorithm | Time | Space |
|-----------|------|-------|
| **Binary Search** | O(log n) | O(1) |
| **Merge Sort** | O(n log n) | O(n) |
| **Quick Sort** | O(n log n) avg | O(log n) |
| **DFS** | O(V + E) | O(V) |
| **BFS** | O(V + E) | O(V) |
| **Dijkstra** | O((V+E) log V) | O(V) |
| **Dynamic Programming** | Varies | Usually O(n) or O(n²) |

---

## Top 100 Must-Practice Problems

### Easy (20 problems) - Master these first

**Arrays:**
1. Two Sum
2. Best Time to Buy and Sell Stock
3. Contains Duplicate
4. Maximum Subarray
5. Product of Array Except Self

**Strings:**
6. Valid Anagram
7. Valid Parentheses
8. Longest Substring Without Repeating Characters
9. Longest Palindromic Substring
10. Palindrome Number

**Linked Lists:**
11. Reverse Linked List
12. Merge Two Sorted Lists
13. Linked List Cycle
14. Remove Nth Node From End

**Trees:**
15. Maximum Depth of Binary Tree
16. Invert Binary Tree
17. Same Tree
18. Symmetric Tree

**Other:**
19. Climbing Stairs
20. Fibonacci Number

### Medium (50 problems) - Core interview questions

**Arrays & Strings:**
21. 3Sum
22. Container With Most Water
23. Longest Palindromic Substring
24. Group Anagrams
25. Longest Consecutive Sequence

**Linked Lists:**
26. Add Two Numbers
27. Remove Nth Node From End of List
28. Reorder List
29. LRU Cache

**Trees:**
30. Binary Tree Level Order Traversal
31. Validate Binary Search Tree
32. Kth Smallest Element in BST
33. Lowest Common Ancestor
34. Binary Tree Right Side View
35. Construct Binary Tree from Preorder and Inorder

**Graphs:**
36. Number of Islands
37. Clone Graph
38. Course Schedule
39. Pacific Atlantic Water Flow
40. Word Ladder

**Dynamic Programming:**
41. Coin Change
42. Longest Increasing Subsequence
43. Word Break
44. Combination Sum
45. Unique Paths
46. House Robber
47. Decode Ways
48. Maximum Product Subarray
49. Partition Equal Subset Sum
50. Target Sum

**Heaps:**
51. Top K Frequent Elements
52. Find Median from Data Stream
53. K Closest Points to Origin
54. Kth Largest Element in Array

**Backtracking:**
55. Permutations
56. Subsets
57. Combination Sum
58. Word Search
59. Palindrome Partitioning

**Binary Search:**
60. Search in Rotated Sorted Array
61. Find Minimum in Rotated Sorted Array
62. Search a 2D Matrix
63. Koko Eating Bananas
64. Capacity To Ship Packages

**Intervals:**
65. Merge Intervals
66. Insert Interval
67. Meeting Rooms II
68. Non-overlapping Intervals

**Misc:**
69. Evaluate Reverse Polish Notation
70. Daily Temperatures

### Hard (30 problems) - Advanced preparation

**Arrays:**
71. Trapping Rain Water
72. Sliding Window Maximum
73. Minimum Window Substring
74. Longest Valid Parentheses

**Trees:**
75. Binary Tree Maximum Path Sum
76. Serialize and Deserialize Binary Tree
77. Binary Tree Cameras

**Graphs:**
78. Word Ladder II
79. Alien Dictionary
80. Critical Connections in Network

**Dynamic Programming:**
81. Regular Expression Matching
82. Wildcard Matching
83. Edit Distance
84. Distinct Subsequences
85. Interleaving String
86. Burst Balloons
87. Russian Doll Envelopes
88. Best Time to Buy and Sell Stock III/IV
89. Palindrome Partitioning II

**Design:**
90. LRU Cache
91. LFU Cache
92. Design Twitter

**Heaps:**
93. Merge k Sorted Lists
94. Find Median from Data Stream

**Advanced:**
95. N-Queens
96. Sudoku Solver
97. Largest Rectangle in Histogram
98. Maximal Rectangle
99. Word Search II
100. Reconstruct Itinerary

**See [Chapter 45](45_interview_strategy/README.md) for complete lists with links**

---

## Interview Day Checklist

### Before the Interview

- [ ] **Review key patterns** - Quickly scan Chapter 28 patterns
- [ ] **Practice one Easy and one Medium problem** - Warm up
- [ ] **Prepare your environment** - Test camera, mic, internet, IDE
- [ ] **Have materials ready** - Pen, paper, water, list of questions

### During the Interview

**UMPIRE Framework:**

1. **Understand** - Clarify the problem
   - What are the inputs? What are the outputs?
   - What are the constraints? Edge cases?
   - Can I use extra space?

2. **Match** - Identify the pattern
   - Does this match any of the 15 patterns?
   - What data structure would be most helpful?
   - Have I seen a similar problem before?

3. **Plan** - Design your approach
   - Explain your high-level approach
   - Discuss time and space complexity
   - Get interviewer buy-in before coding

4. **Implement** - Write clean code
   - Start with a brute force if needed
   - Write modular, readable code
   - Add comments for complex logic

5. **Review** - Test and optimize
   - Walk through your code with example inputs
   - Check edge cases
   - Optimize if asked

6. **Evaluate** - Analyze complexity
   - State time and space complexity
   - Discuss trade-offs
   - Suggest improvements

### Communication Tips

- **Think out loud** - Explain your reasoning as you work
- **Ask clarifying questions** - Don't make assumptions
- **Be honest** - If you're stuck, say so and ask for hints
- **Stay positive** - Even if struggling, maintain composure
- **Listen to hints** - Interviewers want to help you succeed

### Common Mistakes to Avoid

- ❌ Jumping into code without understanding the problem
- ❌ Not discussing approach before coding
- ❌ Writing messy, unorganized code
- ❌ Not testing your solution
- ❌ Getting defensive about mistakes
- ❌ Not asking questions when stuck
- ❌ Giving up too easily

---

## Resource Links

- **Main Curriculum:** [README.md](README.md)
- **LeetCode:** https://leetcode.com/
- **Chapter 28: Patterns:** [28_patterns/README.md](28_patterns/README.md)
- **Chapter 45: Interview Strategy:** [45_interview_strategy/README.md](45_interview_strategy/README.md)
- **Python Documentation:** https://docs.python.org/3/

---

**Remember: Pattern recognition is the key to solving coding interview problems efficiently!**

Master the 15 patterns in Chapter 28, practice 200+ problems, and you'll be ready for any interview.

Good luck! 🚀
