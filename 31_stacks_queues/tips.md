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
