# Stacks and Queues: Tips and Patterns

## Table of Contents
1. [When to Use Stack vs Queue](#when-to-use-stack-vs-queue)
2. [Common Patterns](#common-patterns)
3. [Python Implementation Tips](#python-implementation-tips)
4. [Monotonic Stack/Queue Mastery](#monotonic-stackqueue-mastery)
5. [Design Problem Strategies](#design-problem-strategies)
6. [Common Pitfalls](#common-pitfalls)
7. [Optimization Techniques](#optimization-techniques)
8. [Interview Tips](#interview-tips)

---

## When to Use Stack vs Queue

### Use Stack When:

**Pattern Recognition:**
- Need to **reverse** order (LIFO)
- **Backtracking** or undo operations
- **Nesting** or **matching** (parentheses, brackets)
- **DFS** traversal
- Need to access **most recent** elements

**Examples:**
```python
# Reverse a string
def reverse_string(s):
    stack = list(s)
    return ''.join(stack[::-1])

# Function call stack simulation
def factorial(n, call_stack=[]):
    call_stack.append(f"factorial({n})")
    if n <= 1:
        return 1
    result = n * factorial(n-1, call_stack)
    call_stack.pop()
    return result

# Undo/Redo operations
class TextEditor:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def type(self, text):
        self.undo_stack.append(("type", text))
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.redo_stack.append(action)

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.undo_stack.append(action)
```

### Use Queue When:

**Pattern Recognition:**
- Need to process in **arrival order** (FIFO)
- **BFS** traversal
- **Level-order** processing
- **Scheduling** or **buffering**
- Need to access **oldest** elements first

**Examples:**
```python
from collections import deque

# BFS traversal
def bfs(graph, start):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Task scheduling
class TaskScheduler:
    def __init__(self):
        self.queue = deque()

    def add_task(self, task):
        self.queue.append(task)

    def process_next(self):
        if self.queue:
            return self.queue.popleft()

# Level-order tree traversal
def level_order(root):
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

### Use Deque When:

**Pattern Recognition:**
- Need access to **both ends**
- **Sliding window** with min/max
- **Palindrome** checking
- **Work stealing** algorithms

**Examples:**
```python
from collections import deque

# Sliding window maximum
def max_sliding_window(nums, k):
    dq = deque()  # Store indices
    result = []

    for i in range(len(nums)):
        # Remove outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Maintain decreasing order
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Palindrome check
def is_palindrome(s):
    dq = deque(s.lower())

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True
```

---

## Common Patterns

### Pattern 1: Monotonic Stack

**Definition:** Stack that maintains elements in increasing or decreasing order.

**When to Use:**
- Next greater/smaller element
- Stock span problems
- Histogram problems
- Trapping water problems

**Templates:**

```python
# Monotonic Increasing Stack
# Find next smaller element for each element
def next_smaller(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        # Pop larger elements
        while stack and arr[stack[-1]] > arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]

        stack.append(i)

    return result


# Monotonic Decreasing Stack
# Find next greater element for each element
def next_greater(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        # Pop smaller elements
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]

        stack.append(i)

    return result


# Template for "previous greater/smaller"
def previous_greater(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        # Pop smaller elements
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        # Top of stack is previous greater
        if stack:
            result[i] = arr[stack[-1]]

        stack.append(i)

    return result
```

**Key Insight:** Each element is pushed and popped at most once → **O(n) amortized**

### Pattern 2: Monotonic Queue (Deque)

**Definition:** Deque that maintains elements in sorted order for sliding window.

**When to Use:**
- Sliding window maximum/minimum
- Range queries with moving window

**Template:**

```python
from collections import deque

def sliding_window_max(nums, k):
    """
    Maintain decreasing deque of indices.
    Front has index of maximum element.
    """
    dq = deque()
    result = []

    for i in range(len(nums)):
        # 1. Remove elements outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # 2. Remove smaller elements (can't be max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # 3. Add current element
        dq.append(i)

        # 4. Record maximum if window is full
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

**Three-Step Process:**
1. Remove elements outside window (left end)
2. Maintain monotonic property (right end)
3. Add current element

### Pattern 3: Two Stacks

**Use Cases:**
- Implement queue with stacks
- Min/max stack
- Browser history (back/forward)

**Template:**

```python
class QueueWithStacks:
    """
    Amortized O(1) for all operations.
    """
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def enqueue(self, x):
        self.input_stack.append(x)

    def dequeue(self):
        self._transfer()
        return self.output_stack.pop()

    def _transfer(self):
        """Transfer when output is empty."""
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())


class MinStack:
    """
    O(1) getMin using parallel stack.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def getMin(self):
        return self.min_stack[-1]
```

### Pattern 4: Expression Evaluation

**Types:**
- Infix: `3 + 4 * 2`
- Postfix (RPN): `3 4 2 * +`
- Prefix: `+ 3 * 4 2`

**Template for RPN:**

```python
def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if token in {'+', '-', '*', '/'}:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:  # '/'
                result = int(a / b)

            stack.append(result)
        else:
            stack.append(int(token))

    return stack[0]
```

**Template for Infix with Parentheses:**

```python
def calculate(s):
    stack = []
    result = 0
    sign = 1
    num = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in '+-':
            result += sign * num
            sign = 1 if char == '+' else -1
            num = 0
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            num = 0
            result *= stack.pop()
            result += stack.pop()

    return result + sign * num
```

### Pattern 5: Parentheses Matching

**Template:**

```python
def is_valid(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0
```

**Variations:**
```python
# Count minimum insertions needed
def min_add_to_make_valid(s):
    stack = []
    insertions = 0

    for char in s:
        if char == '(':
            stack.append(char)
        else:  # ')'
            if stack:
                stack.pop()
            else:
                insertions += 1

    return insertions + len(stack)


# Remove invalid parentheses
def remove_invalid(s):
    # First pass: mark valid indices
    stack = []
    to_remove = set()

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)

    # Add unmatched opening brackets
    to_remove.update(stack)

    # Build result
    return ''.join(char for i, char in enumerate(s) if i not in to_remove)
```

---

## Python Implementation Tips

### Stack in Python

```python
# Using list (BEST for stack)
stack = []
stack.append(x)      # Push - O(1) amortized
stack.pop()          # Pop - O(1)
stack[-1]            # Peek - O(1)
len(stack)           # Size - O(1)
bool(stack)          # Is empty - O(1)

# DON'T use deque for simple stack (overhead)
# DON'T use queue.LifoQueue (thread-safe overhead)
```

### Queue in Python

```python
# Using collections.deque (BEST for queue)
from collections import deque

queue = deque()
queue.append(x)      # Enqueue - O(1)
queue.popleft()      # Dequeue - O(1)
queue[0]             # Front - O(1)
queue[-1]            # Rear - O(1)

# DON'T use list (pop(0) is O(n))
# DON'T use queue.Queue (thread-safe overhead)
```

### Deque in Python

```python
from collections import deque

dq = deque()

# Both ends O(1)
dq.append(x)         # Add right
dq.appendleft(x)     # Add left
dq.pop()             # Remove right
dq.popleft()         # Remove left

# Access
dq[0]                # Left end
dq[-1]               # Right end

# Useful methods
dq.rotate(n)         # Rotate n steps right
dq.extend(iterable)  # Add multiple right
dq.extendleft(iter)  # Add multiple left (reversed)
```

### Priority Queue in Python

```python
import heapq

# Min heap by default
pq = []
heapq.heappush(pq, x)           # O(log n)
heapq.heappop(pq)               # O(log n)
pq[0]                           # Peek - O(1)

# Max heap (negate values)
heapq.heappush(pq, -x)
max_val = -heapq.heappop(pq)

# Custom priority
heapq.heappush(pq, (priority, item))
priority, item = heapq.heappop(pq)

# Heapify existing list
heapq.heapify(lst)              # O(n)

# Top k elements
heapq.nlargest(k, iterable)     # O(n log k)
heapq.nsmallest(k, iterable)    # O(n log k)
```

---

## Monotonic Stack/Queue Mastery

### Identifying Problems

**Keywords that suggest monotonic stack:**
- "Next greater element"
- "Next smaller element"
- "Previous greater/smaller"
- "Largest rectangle"
- "Histogram"
- "Trapped water"
- "Stock span"
- "Temperature"

**Keywords that suggest monotonic deque:**
- "Sliding window maximum"
- "Sliding window minimum"
- "Window with constraint"

### Decision Tree

```
                    Need next/previous greater/smaller?
                                  |
                            +-----+-----+
                           YES          NO
                            |            |
                    Monotonic Stack    Is it sliding window?
                            |                  |
                            |            +-----+-----+
                            |           YES          NO
                            |            |            |
                            |      Monotonic        Regular
                            |         Deque       Stack/Queue
                            |
                    +-------+-------+
                    |               |
            Next/Previous?    Greater/Smaller?
                    |               |
            +-+----+----+-+    +----+----+
            | |         | |    |         |
          Next Prev  Left Right  Greater Smaller
```

### Increasing vs Decreasing

**Monotonic Increasing Stack:** (bottom → top)
- **Use for:** Next/previous **smaller** element
- **Pop when:** `stack[-1] > current`
- **Maintains:** Increasing order

**Monotonic Decreasing Stack:** (bottom → top)
- **Use for:** Next/previous **greater** element
- **Pop when:** `stack[-1] < current`
- **Maintains:** Decreasing order

**Memory Trick:**
- Want next **greater**? Use **decreasing** stack (pop smaller)
- Want next **smaller**? Use **increasing** stack (pop larger)

### Common Variations

```python
# 1. Next Greater Element
def next_greater(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result


# 2. Previous Greater Element
def previous_greater(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = arr[stack[-1]]

        stack.append(i)

    return result


# 3. Next Greater in Circular Array
def next_greater_circular(arr):
    n = len(arr)
    stack = []
    result = [-1] * n

    # Process array twice for circular
    for i in range(2 * n):
        idx = i % n

        while stack and arr[stack[-1]] < arr[idx]:
            result[stack.pop()] = arr[idx]

        if i < n:
            stack.append(idx)

    return result


# 4. Count of Greater Elements to Right
def count_greater_right(arr):
    stack = []
    count = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        # Count elements in stack greater than current
        temp_count = 0
        temp = []

        while stack and stack[-1] > arr[i]:
            temp_count += 1
            temp.append(stack.pop())

        count[i] = temp_count

        # Restore stack
        while temp:
            stack.append(temp.pop())

        stack.append(arr[i])

    return count
```

---

## Design Problem Strategies

### General Approach

1. **Understand operations:** What operations are supported?
2. **Identify bottleneck:** Which operation must be O(1)?
3. **Choose data structures:** What combination achieves target complexity?
4. **Trade-offs:** Space vs time, operation vs operation

### Common Designs

**1. Stack with Min/Max in O(1)**

```python
class MinStack:
    """
    Strategy: Parallel stack tracking min at each level.
    Space trade-off: 2x space for O(1) getMin.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))


class MinStackOptimized:
    """
    Strategy: Only push to min_stack when new minimum.
    Space: Better average case, same worst case.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
```

**2. Queue with Stacks**

```python
class QueueWithStacks:
    """
    Strategy: Input stack for enqueue, output stack for dequeue.
    Transfer only when output is empty → amortized O(1).
    """
    def __init__(self):
        self.input = []
        self.output = []

    def enqueue(self, x):
        self.input.append(x)  # Always O(1)

    def dequeue(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()  # Amortized O(1)
```

**3. LRU Cache**

```python
from collections import OrderedDict

class LRUCache:
    """
    Strategy: OrderedDict maintains insertion order.
    Move to end on access → O(1) get and put.
    """
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

---

## Common Pitfalls

### Pitfall 1: Not Checking Empty Stack/Queue

```python
# BAD
def pop_stack(stack):
    return stack.pop()  # May raise IndexError

# GOOD
def pop_stack(stack):
    if stack:
        return stack.pop()
    return None  # or raise custom exception
```

### Pitfall 2: Using List for Queue

```python
# BAD - O(n) dequeue!
queue = []
queue.append(x)  # O(1)
queue.pop(0)     # O(n) - shifts all elements

# GOOD - O(1) dequeue
from collections import deque
queue = deque()
queue.append(x)    # O(1)
queue.popleft()    # O(1)
```

### Pitfall 3: Forgetting to Store Indices

```python
# BAD - Can't track position
def next_greater(arr):
    stack = []
    for num in arr:
        while stack and stack[-1] < num:
            stack.pop()  # Lost position!
        stack.append(num)

# GOOD - Store indices
def next_greater(arr):
    stack = []
    result = [-1] * len(arr)

    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)

    return result
```

### Pitfall 4: Off-by-One in Sliding Window

```python
# BAD - Wrong window size check
for i in range(len(nums)):
    # ... maintain deque ...
    if i > k:  # WRONG!
        result.append(nums[dq[0]])

# GOOD - Correct check
for i in range(len(nums)):
    # ... maintain deque ...
    if i >= k - 1:  # Start recording at index k-1
        result.append(nums[dq[0]])
```

### Pitfall 5: Not Handling Duplicates

```python
# For "next greater or equal" vs "next greater"
# Careful with <= vs <

# Next greater (strictly)
while stack and arr[stack[-1]] < arr[i]:
    stack.pop()

# Next greater or equal
while stack and arr[stack[-1]] <= arr[i]:
    stack.pop()
```

---

## Optimization Techniques

### 1. Space Optimization

**Use single variable instead of stack when possible:**

```python
# Count valid parentheses
def min_add(s):
    # Instead of stack, use counter
    open_count = 0
    close_needed = 0

    for char in s:
        if char == '(':
            open_count += 1
        else:
            if open_count > 0:
                open_count -= 1
            else:
                close_needed += 1

    return open_count + close_needed
```

### 2. In-place Operations

**Modify input array instead of using result array:**

```python
# If input can be modified
def next_greater_inplace(arr):
    stack = []

    for i in range(len(arr) - 1, -1, -1):
        temp = arr[i]

        while stack and stack[-1] <= temp:
            stack.pop()

        arr[i] = stack[-1] if stack else -1
        stack.append(temp)

    return arr
```

### 3. Early Termination

```python
# Check if all brackets can be matched
def can_match(s):
    count = 0

    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                return False  # Early termination

    return count == 0
```

### 4. Amortized Analysis

**Understand amortized O(1):**

```python
# Queue with stacks
# Each element:
# - Pushed to input once: O(1)
# - Moved to output once: O(1)
# - Popped from output once: O(1)
# Total: 3 operations per element → O(1) amortized
```

---

## Interview Tips

### 1. Problem Recognition

**Ask yourself:**
- Need most recent elements? → Stack
- Need oldest elements? → Queue
- Need both ends? → Deque
- Next greater/smaller? → Monotonic stack
- Sliding window max/min? → Monotonic deque
- Matching pairs? → Stack

### 2. Clarify Constraints

**Important questions:**
- Can input be empty?
- What's the range of values?
- Are there duplicates?
- Can I modify input?
- What's the expected time/space complexity?

### 3. Start Simple

```python
# Start with brute force
def next_greater_brute(arr):
    n = len(arr)
    result = [-1] * n

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break

    return result  # O(n²)

# Then optimize with stack
def next_greater_optimal(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result  # O(n)
```

### 4. Walk Through Example

```
Always trace with concrete example:

arr = [4, 5, 2, 25]

i=0: stack=[0]           result=[-1,-1,-1,-1]
i=1: stack=[1]           result=[5,-1,-1,-1]   (popped 0)
i=2: stack=[1,2]         result=[5,-1,-1,-1]
i=3: stack=[3]           result=[5,25,25,-1]   (popped 1,2)
```

### 5. Test Edge Cases

```python
# Always test:
# - Empty input
# - Single element
# - All increasing
# - All decreasing
# - Duplicates
# - Maximum/minimum values

test_cases = [
    [],              # Empty
    [1],             # Single
    [1,2,3,4,5],     # Increasing
    [5,4,3,2,1],     # Decreasing
    [1,1,1,1],       # All same
    [1,3,2,4],       # Mixed
]
```

### 6. Complexity Analysis

**Always state:**
- **Time complexity** with reasoning
- **Space complexity** with reasoning
- **Amortized** if applicable

```python
def solution():
    """
    Time: O(n) - each element pushed/popped once
    Space: O(n) - stack stores up to n elements
    Amortized: O(1) per operation
    """
    pass
```

### 7. Common Follow-ups

**Be prepared for:**
- "Can you optimize space?"
- "What if array is circular?"
- "What if we need previous instead of next?"
- "Can you do it in one pass?"
- "What if there are duplicates?"

---

## Quick Reference Cheat Sheet

```python
# Stack (use list)
stack = []
stack.append(x)    # push
stack.pop()        # pop
stack[-1]          # peek

# Queue (use deque)
from collections import deque
queue = deque()
queue.append(x)    # enqueue
queue.popleft()    # dequeue
queue[0]           # front

# Deque
dq = deque()
dq.append(x)       # right
dq.appendleft(x)   # left
dq.pop()           # right
dq.popleft()       # left

# Priority Queue
import heapq
pq = []
heapq.heappush(pq, x)
heapq.heappop(pq)

# Monotonic Stack Pattern
stack = []
for i, num in enumerate(arr):
    while stack and arr[stack[-1]] < num:
        result[stack.pop()] = num
    stack.append(i)

# Monotonic Deque Pattern
dq = deque()
for i in range(len(nums)):
    while dq and dq[0] < i - k + 1:
        dq.popleft()
    while dq and nums[dq[-1]] < nums[i]:
        dq.pop()
    dq.append(i)
```

---

## Summary

**Key Takeaways:**
1. **Stack** for LIFO, backtracking, nesting
2. **Queue** for FIFO, BFS, scheduling
3. **Deque** for both ends, sliding window
4. **Monotonic structures** for next/previous greater/smaller
5. **Amortized O(1)** is often good enough
6. **Store indices** in monotonic structures
7. **Check empty** before pop/peek
8. **Use deque for queue**, not list

Practice these patterns until they become second nature!

---

## LeetCode Practice Problems

### 📊 Problem Statistics
- **Total Problems:** 60+
- **Easy:** 15 problems
- **Medium:** 30 problems
- **Hard:** 15 problems
- **Estimated Time:** 40-55 hours

---

## Easy Problems (15)

### 1. Valid Parentheses
**Link:** https://leetcode.com/problems/valid-parentheses/  
**Pattern:** Stack  
**Topics:** String, Stack  
**Description:** Check if parentheses are valid  
**Why Practice:** Classic stack application

### 2. Implement Queue using Stacks
**Link:** https://leetcode.com/problems/implement-queue-using-stacks/  
**Pattern:** Design  
**Topics:** Stack, Design, Queue  
**Description:** Implement queue with two stacks  
**Why Practice:** Understanding data structure relationships

### 3. Implement Stack using Queues
**Link:** https://leetcode.com/problems/implement-stack-using-queues/  
**Pattern:** Design  
**Topics:** Stack, Design, Queue  
**Description:** Implement stack with queues  
**Why Practice:** Inverse relationship

### 4. Min Stack
**Link:** https://leetcode.com/problems/min-stack/  
**Pattern:** Design  
**Topics:** Stack, Design  
**Description:** Stack with O(1) getMin()  
**Why Practice:** Tracking auxiliary information

### 5. Backspace String Compare
**Link:** https://leetcode.com/problems/backspace-string-compare/  
**Pattern:** Stack  
**Topics:** Two Pointers, String, Stack, Simulation  
**Description:** Compare strings with backspaces  
**Why Practice:** Stack for character deletion

### 6. Next Greater Element I
**Link:** https://leetcode.com/problems/next-greater-element-i/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Hash Table, Stack, Monotonic Stack  
**Description:** Find next greater element  
**Why Practice:** Introduction to monotonic stack

### 7. Baseball Game
**Link:** https://leetcode.com/problems/baseball-game/  
**Pattern:** Stack  
**Topics:** Array, Stack, Simulation  
**Description:** Calculate score with operations  
**Why Practice:** Stack operations practice

### 8. Remove All Adjacent Duplicates In String
**Link:** https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/  
**Pattern:** Stack  
**Topics:** String, Stack  
**Description:** Remove adjacent duplicates  
**Why Practice:** Stack for matching

### 9. Remove Outermost Parentheses
**Link:** https://leetcode.com/problems/remove-outermost-parentheses/  
**Pattern:** Stack  
**Topics:** String, Stack  
**Description:** Remove outer parentheses  
**Why Practice:** Tracking depth with stack

### 10. Make The String Great
**Link:** https://leetcode.com/problems/make-the-string-great/  
**Pattern:** Stack  
**Topics:** String, Stack  
**Description:** Remove adjacent bad pairs  
**Why Practice:** Stack matching pattern

### 11. Crawler Log Folder
**Link:** https://leetcode.com/problems/crawler-log-folder/  
**Pattern:** Stack  
**Topics:** Array, String, Stack  
**Description:** Track folder operations  
**Why Practice:** Stack for path tracking

### 12. Maximum Nesting Depth of Parentheses
**Link:** https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/  
**Pattern:** Stack / Counter  
**Topics:** String, Stack  
**Description:** Find maximum depth  
**Why Practice:** Depth tracking

### 13. Build an Array With Stack Operations
**Link:** https://leetcode.com/problems/build-an-array-with-stack-operations/  
**Pattern:** Stack Simulation  
**Topics:** Array, Stack, Simulation  
**Description:** Generate push/pop sequence  
**Why Practice:** Stack operation simulation

### 14. Final Prices With a Special Discount
**Link:** https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Stack, Monotonic Stack  
**Description:** Apply discounts using next smaller  
**Why Practice:** Monotonic stack variation

### 15. Number of Recent Calls
**Link:** https://leetcode.com/problems/number-of-recent-calls/  
**Pattern:** Queue  
**Topics:** Design, Queue, Data Stream  
**Description:** Track requests in time window  
**Why Practice:** Queue for sliding window

---

## Medium Problems (30)

### 16. Evaluate Reverse Polish Notation
**Link:** https://leetcode.com/problems/evaluate-reverse-polish-notation/  
**Pattern:** Stack  
**Topics:** Array, Math, Stack  
**Description:** Evaluate postfix expression  
**Why Practice:** Stack for expression evaluation

### 17. Daily Temperatures
**Link:** https://leetcode.com/problems/daily-temperatures/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Stack, Monotonic Stack  
**Description:** Days until warmer temperature  
**Why Practice:** Classic monotonic stack problem

### 18. Next Greater Element II
**Link:** https://leetcode.com/problems/next-greater-element-ii/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Stack, Monotonic Stack  
**Description:** Next greater in circular array  
**Why Practice:** Circular array with monotonic stack

### 19. Online Stock Span
**Link:** https://leetcode.com/problems/online-stock-span/  
**Pattern:** Monotonic Stack  
**Topics:** Stack, Design, Monotonic Stack, Data Stream  
**Description:** Calculate stock price spans  
**Why Practice:** Real-time monotonic stack

### 20. Decode String
**Link:** https://leetcode.com/problems/decode-string/  
**Pattern:** Stack  
**Topics:** String, Stack, Recursion  
**Description:** Decode encoded string  
**Why Practice:** Nested structure parsing

### 21. Remove K Digits
**Link:** https://leetcode.com/problems/remove-k-digits/  
**Pattern:** Monotonic Stack  
**Topics:** String, Stack, Greedy, Monotonic Stack  
**Description:** Remove k digits to minimize number  
**Why Practice:** Greedy with monotonic stack

### 22. Asteroid Collision
**Link:** https://leetcode.com/problems/asteroid-collision/  
**Pattern:** Stack  
**Topics:** Array, Stack, Simulation  
**Description:** Simulate asteroid collisions  
**Why Practice:** Stack for collision detection

### 23. Car Fleet
**Link:** https://leetcode.com/problems/car-fleet/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Stack, Sorting, Monotonic Stack  
**Description:** Count car fleets  
**Why Practice:** Complex monotonic stack

### 24. Simplify Path
**Link:** https://leetcode.com/problems/simplify-path/  
**Pattern:** Stack  
**Topics:** String, Stack  
**Description:** Simplify Unix file path  
**Why Practice:** Stack for path resolution

### 25. Validate Stack Sequences
**Link:** https://leetcode.com/problems/validate-stack-sequences/  
**Pattern:** Stack Simulation  
**Topics:** Array, Stack, Simulation  
**Description:** Validate push/pop sequence  
**Why Practice:** Stack sequence validation

### 26. 132 Pattern
**Link:** https://leetcode.com/problems/132-pattern/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Binary Search, Stack, Monotonic Stack, Ordered Set  
**Description:** Find 132 pattern in array  
**Why Practice:** Complex pattern detection

### 27. Remove All Adjacent Duplicates In String II
**Link:** https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/  
**Pattern:** Stack with Count  
**Topics:** String, Stack  
**Description:** Remove k adjacent duplicates  
**Why Practice:** Stack with frequency tracking

### 28. Shortest Unsorted Continuous Subarray
**Link:** https://leetcode.com/problems/shortest-unsorted-continuous-subarray/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Two Pointers, Stack, Greedy, Sorting, Monotonic Stack  
**Description:** Find shortest subarray to sort  
**Why Practice:** Multiple solution approaches

### 29. Number of Visible People in a Queue
**Link:** https://leetcode.com/problems/number-of-visible-people-in-a-queue/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Stack, Monotonic Stack  
**Description:** Count visible people to the right  
**Why Practice:** Visibility with monotonic stack

### 30. Sum of Subarray Minimums
**Link:** https://leetcode.com/problems/sum-of-subarray-minimums/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Dynamic Programming, Stack, Monotonic Stack  
**Description:** Sum of minimums of all subarrays  
**Why Practice:** Advanced monotonic stack application

### 31. Score of Parentheses
**Link:** https://leetcode.com/problems/score-of-parentheses/  
**Pattern:** Stack  
**Topics:** String, Stack  
**Description:** Calculate parentheses score  
**Why Practice:** Nested structure scoring

### 32. Minimum Add to Make Parentheses Valid
**Link:** https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/  
**Pattern:** Stack / Counter  
**Topics:** String, Stack, Greedy  
**Description:** Minimum additions for validity  
**Why Practice:** Stack for balance tracking

### 33. Design Circular Queue
**Link:** https://leetcode.com/problems/design-circular-queue/  
**Pattern:** Design  
**Topics:** Array, Linked List, Design, Queue  
**Description:** Implement circular queue  
**Why Practice:** Understanding circular buffer

### 34. Design Circular Deque
**Link:** https://leetcode.com/problems/design-circular-deque/  
**Pattern:** Design  
**Topics:** Array, Linked List, Design, Queue  
**Description:** Implement circular deque  
**Why Practice:** Bidirectional queue

### 35. Flatten Nested List Iterator
**Link:** https://leetcode.com/problems/flatten-nested-list-iterator/  
**Pattern:** Stack  
**Topics:** Stack, Tree, Depth-First Search, Design, Queue, Iterator  
**Description:** Iterator for nested list  
**Why Practice:** Stack for nested iteration

### 36. Mini Parser
**Link:** https://leetcode.com/problems/mini-parser/  
**Pattern:** Stack  
**Topics:** String, Stack, Depth-First Search  
**Description:** Parse nested integer list  
**Why Practice:** Complex parsing with stack

### 37. Exclusive Time of Functions
**Link:** https://leetcode.com/problems/exclusive-time-of-functions/  
**Pattern:** Stack  
**Topics:** Array, Stack  
**Description:** Calculate exclusive execution time  
**Why Practice:** Stack for time tracking

### 38. Binary Tree Inorder Traversal (iterative)
**Link:** https://leetcode.com/problems/binary-tree-inorder-traversal/  
**Pattern:** Stack  
**Topics:** Stack, Tree, Depth-First Search, Binary Tree  
**Description:** Inorder traversal without recursion  
**Why Practice:** Stack for tree traversal

### 39. Binary Tree Preorder Traversal (iterative)
**Link:** https://leetcode.com/problems/binary-tree-preorder-traversal/  
**Pattern:** Stack  
**Topics:** Stack, Tree, Depth-First Search, Binary Tree  
**Description:** Preorder traversal iteratively  
**Why Practice:** Stack traversal pattern

### 40. Binary Tree Postorder Traversal (iterative)
**Link:** https://leetcode.com/problems/binary-tree-postorder-traversal/  
**Pattern:** Stack  
**Topics:** Stack, Tree, Depth-First Search, Binary Tree  
**Description:** Postorder traversal iteratively  
**Why Practice:** Complex stack traversal

### 41. Maximum Frequency Stack
**Link:** https://leetcode.com/problems/maximum-frequency-stack/  
**Pattern:** Stack + Hash Map  
**Topics:** Hash Table, Stack, Design, Ordered Set  
**Description:** Stack that pops most frequent  
**Why Practice:** Complex data structure design

### 42. Minimum Remove to Make Valid Parentheses
**Link:** https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/  
**Pattern:** Stack  
**Topics:** String, Stack  
**Description:** Remove minimum to make valid  
**Why Practice:** Two-pass stack technique

### 43. Check If Word Is Valid After Substitutions
**Link:** https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/  
**Pattern:** Stack  
**Topics:** String, Stack  
**Description:** Check validity after substitutions  
**Why Practice:** Pattern matching with stack

### 44. Number of Atoms
**Link:** https://leetcode.com/problems/number-of-atoms/  
**Pattern:** Stack  
**Topics:** Hash Table, String, Stack, Sorting  
**Description:** Parse chemical formula  
**Why Practice:** Complex nested parsing

### 45. Remove Duplicate Letters
**Link:** https://leetcode.com/problems/remove-duplicate-letters/  
**Pattern:** Monotonic Stack + Hash  
**Topics:** String, Stack, Greedy, Monotonic Stack  
**Description:** Remove duplicates, keep lexicographically smallest  
**Why Practice:** Greedy with monotonic stack

---

## Hard Problems (15)

### 46. Trapping Rain Water
**Link:** https://leetcode.com/problems/trapping-rain-water/  
**Pattern:** Stack / Two Pointers  
**Topics:** Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack  
**Description:** Calculate trapped rainwater  
**Why Practice:** Multiple solution approaches, common interview problem

### 47. Largest Rectangle in Histogram
**Link:** https://leetcode.com/problems/largest-rectangle-in-histogram/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Stack, Monotonic Stack  
**Description:** Find largest rectangle in histogram  
**Why Practice:** Classic monotonic stack problem

### 48. Maximal Rectangle
**Link:** https://leetcode.com/problems/maximal-rectangle/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Dynamic Programming, Stack, Matrix, Monotonic Stack  
**Description:** Largest rectangle in binary matrix  
**Why Practice:** Extension of histogram problem

### 49. Basic Calculator
**Link:** https://leetcode.com/problems/basic-calculator/  
**Pattern:** Stack  
**Topics:** Math, String, Stack, Recursion  
**Description:** Evaluate expression with parentheses  
**Why Practice:** Complex expression parsing

### 50. Basic Calculator II
**Link:** https://leetcode.com/problems/basic-calculator-ii/  
**Pattern:** Stack  
**Topics:** Math, String, Stack  
**Description:** Evaluate with +, -, *, /  
**Why Practice:** Operator precedence handling

### 51. Basic Calculator III
**Link:** https://leetcode.com/problems/basic-calculator-iii/  
**Pattern:** Stack  
**Topics:** Math, String, Stack, Recursion  
**Description:** Complete calculator  
**Why Practice:** Combining all calculator concepts (Premium)

### 52. Sliding Window Maximum
**Link:** https://leetcode.com/problems/sliding-window-maximum/  
**Pattern:** Monotonic Deque  
**Topics:** Array, Queue, Sliding Window, Heap, Monotonic Queue  
**Description:** Max in each sliding window  
**Why Practice:** Classic monotonic deque problem

### 53. Longest Valid Parentheses
**Link:** https://leetcode.com/problems/longest-valid-parentheses/  
**Pattern:** Stack / DP  
**Topics:** String, Dynamic Programming, Stack  
**Description:** Length of longest valid parentheses  
**Why Practice:** Complex validity checking

### 54. Reverse Substrings Between Each Pair of Parentheses
**Link:** https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/  
**Pattern:** Stack  
**Topics:** String, Stack  
**Description:** Reverse within parentheses  
**Why Practice:** Nested reversal operations

### 55. Tag Validator
**Link:** https://leetcode.com/problems/tag-validator/  
**Pattern:** Stack  
**Topics:** String, Stack  
**Description:** Validate XML-like tags  
**Why Practice:** Complex nested structure validation

### 56. Car Fleet II
**Link:** https://leetcode.com/problems/car-fleet-ii/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Math, Stack, Heap, Monotonic Stack  
**Description:** Time when cars collide  
**Why Practice:** Advanced monotonic stack with simulation

### 57. Find the Most Competitive Subsequence
**Link:** https://leetcode.com/problems/find-the-most-competitive-subsequence/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Stack, Greedy, Monotonic Stack  
**Description:** Find lexicographically smallest subsequence  
**Why Practice:** Greedy with monotonic stack

### 58. Shortest Subarray with Sum at Least K
**Link:** https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/  
**Pattern:** Monotonic Deque + Prefix Sum  
**Topics:** Array, Binary Search, Queue, Sliding Window, Heap, Prefix Sum, Monotonic Queue  
**Description:** Shortest subarray with sum >= K  
**Why Practice:** Combining multiple advanced techniques

### 59. Constrained Subsequence Sum
**Link:** https://leetcode.com/problems/constrained-subsequence-sum/  
**Pattern:** Monotonic Deque + DP  
**Topics:** Array, Dynamic Programming, Queue, Sliding Window, Heap, Monotonic Queue  
**Description:** Max sum with constraint  
**Why Practice:** DP optimization with monotonic deque

### 60. Minimum Cost Tree From Leaf Values
**Link:** https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/  
**Pattern:** Monotonic Stack  
**Topics:** Array, Dynamic Programming, Stack, Greedy, Monotonic Stack  
**Description:** Build tree with minimum cost  
**Why Practice:** Greedy with monotonic stack

---

## Practice Progression

### Week 1: Stack Basics (Easy 1-10)
Master fundamental stack operations:
- Valid parentheses (1)
- Stack design (2, 3, 4)
- Basic stack operations (7, 8, 9, 10)

### Week 2: Queue & Advanced Easy (Easy 11-15)
Complete easy problems:
- Path tracking (11)
- Queue applications (15)
- Simple monotonic stack (6, 14)

### Week 3-4: Medium Basics (Medium 16-25)
Core medium patterns:
- Expression evaluation (16)
- Monotonic stack (17, 18, 19)
- Stack simulation (24, 25)

### Week 5-6: Advanced Medium (Medium 26-35)
Complex patterns:
- Pattern detection (26)
- Design problems (33, 34, 41)
- Advanced monotonic stack (30, 45)

### Week 7: Tree Traversal (Medium 36-40)
Stack for tree operations:
- Iterative traversals (38, 39, 40)
- Complex parsing (36, 44)

### Week 8-9: Hard Problems (Hard 46-60)
Master hard patterns:
- **Trapping Rain Water (46)** - MUST KNOW
- **Largest Rectangle (47)** - MUST KNOW
- **Maximal Rectangle (48)** - Extension
- Calculators (49, 50, 51)
- **Sliding Window Maximum (52)** - MUST KNOW
- Advanced monotonic (56, 57, 59, 60)

---

## Pattern Mastery Guide

### Monotonic Stack Pattern
**Key Problems:** 17, 18, 21, 23, 26, 30, 45, 47, 48
**Template:**
```python
def monotonic_stack(arr):
    stack = []  # Stores indices
    result = []
    for i, val in enumerate(arr):
        while stack and arr[stack[-1]] < val:
            idx = stack.pop()
            # Process: found next greater for arr[idx]
        stack.append(i)
    return result
```

### Monotonic Deque Pattern
**Key Problems:** 52, 58, 59
**When to Use:** Sliding window with min/max queries
**Key Insight:** Maintain decreasing (for max) or increasing (for min) order

### Expression Evaluation
**Key Problems:** 16, 20, 49, 50, 51
**Patterns:**
- Postfix: Single stack
- Infix: Operator stack + operand stack or output
- With parentheses: Nested evaluation

### Stack for Tree Traversal
**Key Problems:** 38, 39, 40
**Inorder Template:**
```python
def inorder(root):
    stack, result = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result
```

---

## Must-Know Problems (Top 12)

1. **Valid Parentheses (1)** - MUST KNOW
2. **Min Stack (4)** - MUST KNOW
3. **Daily Temperatures (17)** - MUST KNOW for monotonic stack
4. **Evaluate RPN (16)** - Common interview problem
5. **Decode String (20)** - Nested structures
6. **Asteroid Collision (22)** - Simulation with stack
7. **Trapping Rain Water (46)** - VERY COMMON, multiple approaches
8. **Largest Rectangle in Histogram (47)** - CLASSIC monotonic stack
9. **Basic Calculator (49/50)** - Shows mastery
10. **Sliding Window Maximum (52)** - MUST KNOW monotonic deque
11. **Design Circular Queue (33)** - System design
12. **Maximum Frequency Stack (41)** - Advanced design

---

## Common Mistakes

1. **Not checking empty stack:** Always check before pop/peek
2. **Forgetting to track indices:** Often need both value and index
3. **Wrong monotonic order:** Increasing vs decreasing stack
4. **Not handling edge cases:** Empty input, single element
5. **Infinite loops:** Ensure progress in while loops
6. **Memory issues:** Clean up stack when done

---

## Interview Tips

### Monotonic Stack Recognition
**Keywords:** "next greater", "next smaller", "largest", "histogram", "visible"
**Pattern:** When you need to find next/previous greater/smaller element

### Time Allocation
- Easy: 10-15 minutes
- Medium: 20-30 minutes
- Hard: 35-50 minutes

### Strategy
1. **Draw examples:** Visualize stack state
2. **State clearly:** What does stack store - values or indices?
3. **Handle edge cases:** Empty, single element, all same
4. **Discuss trade-offs:** Stack vs two pointers vs DP

---

**Total Practice Time:** 40-55 hours  
**Recommended Pace:** 6-8 problems per week  
**Mastery Timeline:** 8-10 weeks

Remember: Stack/Queue problems are about choosing the right data structure. Monotonic stack is a game-changer!

