# Stacks and Queues: Theory and Fundamentals

## Table of Contents
1. [Stack ADT](#stack-adt)
2. [Queue ADT](#queue-adt)
3. [Deque](#deque)
4. [Priority Queue](#priority-queue)
5. [Monotonic Stack](#monotonic-stack)
6. [Monotonic Queue](#monotonic-queue)
7. [Implementation Strategies](#implementation-strategies)
8. [Complexity Analysis](#complexity-analysis)

---

## Stack ADT

A **stack** is a linear data structure that follows the **Last-In-First-Out (LIFO)** principle. The last element added is the first one to be removed.

### Core Operations

1. **push(item)**: Add item to top of stack - O(1)
2. **pop()**: Remove and return top item - O(1)
3. **peek()/top()**: View top item without removing - O(1)
4. **isEmpty()**: Check if stack is empty - O(1)
5. **size()**: Return number of elements - O(1)

### Visual Representation

```
Stack Operations:

Initial:     []
Push(1):     [1]
Push(2):     [1, 2]
Push(3):     [1, 2, 3]  <- TOP
Peek():      Returns 3, stack unchanged
Pop():       [1, 2]     (returned 3)
Pop():       [1]        (returned 2)
```

### Implementation in Python

**Using List (Array-based):**
```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # O(1) amortized

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()  # O(1)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]  # O(1)

    def is_empty(self):
        return len(self.items) == 0  # O(1)

    def size(self):
        return len(self.items)  # O(1)
```

**Using Linked List:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinked:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size
```

### Applications

1. **Expression Evaluation**: Infix to postfix conversion, calculator
2. **Syntax Parsing**: Matching parentheses, XML/HTML validation
3. **Backtracking**: DFS, maze solving, undo operations
4. **Function Calls**: Call stack in programming languages
5. **Browser History**: Back button navigation

---

## Queue ADT

A **queue** is a linear data structure that follows the **First-In-First-Out (FIFO)** principle. The first element added is the first one to be removed.

### Core Operations

1. **enqueue(item)**: Add item to rear - O(1)
2. **dequeue()**: Remove and return front item - O(1)
3. **front()/peek()**: View front item without removing - O(1)
4. **isEmpty()**: Check if queue is empty - O(1)
5. **size()**: Return number of elements - O(1)

### Visual Representation

```
Queue Operations:

Initial:        FRONT [] REAR
Enqueue(1):     FRONT [1] REAR
Enqueue(2):     FRONT [1, 2] REAR
Enqueue(3):     FRONT [1, 2, 3] REAR
Dequeue():      FRONT [2, 3] REAR  (returned 1)
Dequeue():      FRONT [3] REAR     (returned 2)
```

### Implementation Using List (Inefficient)

```python
# DON'T USE THIS - O(n) dequeue!
class QueueBad:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # O(1)

    def dequeue(self):
        return self.items.pop(0)  # O(n) - shifts all elements!
```

### Implementation Using collections.deque (Best)

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)  # O(1)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()  # O(1)

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]  # O(1)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

### Circular Queue

A **circular queue** uses a fixed-size array with wraparound. When the rear reaches the end, it wraps to the beginning.

```
Circular Queue (size = 5):

Initial:     [_, _, _, _, _]  front=0, rear=0, size=0

Enqueue(1):  [1, _, _, _, _]  front=0, rear=1, size=1
Enqueue(2):  [1, 2, _, _, _]  front=0, rear=2, size=2
Enqueue(3):  [1, 2, 3, _, _]  front=0, rear=3, size=3

Dequeue():   [_, 2, 3, _, _]  front=1, rear=3, size=2

Enqueue(4):  [_, 2, 3, 4, _]  front=1, rear=4, size=3
Enqueue(5):  [_, 2, 3, 4, 5]  front=1, rear=0, size=4  <- wraparound!
Enqueue(6):  [6, 2, 3, 4, 5]  front=1, rear=1, size=5  <- full!
```

**Implementation:**
```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")
        rear = (self.front + self.size) % self.capacity
        self.items[rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity
```

### Applications

1. **BFS Traversal**: Level-order tree/graph traversal
2. **Task Scheduling**: CPU scheduling, print queue
3. **Request Handling**: Server request queues
4. **Buffer**: Data streaming, IO buffering
5. **Cache**: LRU cache with queue for order

---

## Deque

A **deque** (double-ended queue) allows insertion and deletion at both ends in O(1) time.

### Operations

1. **append(item)**: Add to right end - O(1)
2. **appendleft(item)**: Add to left end - O(1)
3. **pop()**: Remove from right end - O(1)
4. **popleft()**: Remove from left end - O(1)
5. **peek_right()**: View right end - O(1)
6. **peek_left()**: View left end - O(1)

### Visual Representation

```
Deque Operations:

Initial:           []
append(1):         [1]
append(2):         [1, 2]
appendleft(0):     [0, 1, 2]
pop():             [0, 1]         (returned 2)
popleft():         [1]            (returned 0)
```

### Python Implementation

```python
from collections import deque

# Python's deque is highly optimized
dq = deque()

# Add elements
dq.append(1)        # Add to right: [1]
dq.appendleft(0)    # Add to left: [0, 1]
dq.extend([2, 3])   # Add multiple to right: [0, 1, 2, 3]

# Remove elements
dq.pop()            # Remove from right: [0, 1, 2]
dq.popleft()        # Remove from left: [1, 2]

# Access elements
dq[0]               # Left end
dq[-1]              # Right end
```

### Applications

1. **Sliding Window**: Maintain window maximum/minimum
2. **Palindrome Check**: Compare from both ends
3. **Undo/Redo**: Navigation in both directions
4. **Work Stealing**: Task scheduling algorithms

---

## Priority Queue

A **priority queue** serves elements based on priority, not insertion order. Typically implemented using a heap.

### Operations

1. **insert(item, priority)**: Add item with priority - O(log n)
2. **extract_min()/extract_max()**: Remove highest priority - O(log n)
3. **peek()**: View highest priority without removing - O(1)

### Python Implementation (Min Heap)

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty priority queue")
        return heapq.heappop(self.heap)[1]

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty priority queue")
        return self.heap[0][1]

    def is_empty(self):
        return len(self.heap) == 0
```

### Applications

1. **Dijkstra's Algorithm**: Shortest path
2. **Huffman Coding**: Data compression
3. **Event Simulation**: Process events by time
4. **Task Scheduling**: Process highest priority tasks

---

## Monotonic Stack

A **monotonic stack** maintains elements in increasing or decreasing order. When a new element violates the order, pop elements until the invariant is restored.

### Monotonic Increasing Stack

Elements increase from bottom to top.

```
Finding Next Greater Element:

Array: [2, 1, 5, 6, 2, 3]

Process 2:  Stack: [2]
Process 1:  Stack: [2, 1]      (1 < 2, maintain increasing)
Process 5:  Stack: [5]         (pop 1, 2; both < 5)
            Next greater for 1: 5
            Next greater for 2: 5
Process 6:  Stack: [5, 6]      (6 > 5, maintain increasing)
Process 2:  Stack: [5, 6]      (2 < 6, don't pop)
Process 3:  Stack: [5, 6]      (3 < 6, don't pop)
```

### Monotonic Decreasing Stack

Elements decrease from bottom to top.

```python
def monotonic_decreasing_stack(arr):
    """
    Maintain decreasing stack.
    Useful for finding next smaller element.
    """
    stack = []
    result = []

    for num in arr:
        # Pop all elements smaller than current
        while stack and stack[-1] < num:
            stack.pop()

        # Current element's next smaller is top of stack
        result.append(stack[-1] if stack else -1)

        # Push current element
        stack.append(num)

    return result
```

### Applications

1. **Next Greater Element**: Find next larger element for each element
2. **Next Smaller Element**: Find next smaller element for each element
3. **Daily Temperatures**: Days until warmer temperature
4. **Stock Span**: Days with price less than or equal to today
5. **Largest Rectangle**: Maximum rectangle in histogram
6. **Trapping Rain Water**: Calculate trapped water

### Pattern Recognition

Use monotonic stack when:
- Finding next greater/smaller element
- Need to maintain order while processing sequentially
- Problem involves comparing current element with previous ones
- O(n) time with single pass is required

---

## Monotonic Queue

A **monotonic queue** (usually using deque) maintains elements in sorted order while supporting efficient front/back operations.

### Sliding Window Maximum Pattern

```
Find maximum in each window of size k:

Array: [1, 3, -1, -3, 5, 3, 6, 7]  k=3

Window [1, 3, -1]:
    Deque: [3, -1]   (max = 3)

Window [3, -1, -3]:
    Deque: [3, -1, -3]   (max = 3)

Window [-1, -3, 5]:
    Deque: [5]   (max = 5, removed all smaller)

Window [-3, 5, 3]:
    Deque: [5, 3]   (max = 5)
```

**Implementation:**
```python
from collections import deque

def max_sliding_window(nums, k):
    """
    Find maximum in each sliding window of size k.

    Time: O(n) - each element pushed/popped once
    Space: O(k) - deque stores at most k elements
    """
    dq = deque()  # Store indices
    result = []

    for i in range(len(nums)):
        # Remove elements outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements (they can't be max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add current element index
        dq.append(i)

        # Add maximum to result (front of deque)
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

### Applications

1. **Sliding Window Maximum**: Maximum in each window
2. **Sliding Window Minimum**: Minimum in each window
3. **Shortest Subarray with Sum ≥ K**: Monotonic queue optimization
4. **Jump Game VI**: Dynamic programming with monotonic deque

---

## Implementation Strategies

### Array-Based vs Linked List

**Array-Based Stack:**
```
Pros:
✓ Simple implementation
✓ Better cache locality
✓ Less memory overhead (no pointers)

Cons:
✗ Resize overhead (amortized O(1))
✗ Wasted space if oversized
```

**Linked List Stack:**
```
Pros:
✓ No resize needed
✓ Exact memory usage
✓ True O(1) for all operations

Cons:
✗ Extra memory for pointers
✗ Poor cache locality
✗ More complex implementation
```

### Queue Implementation Comparison

| Implementation | Enqueue | Dequeue | Space | Notes |
|----------------|---------|---------|-------|-------|
| Python list | O(1) | O(n) | O(n) | DON'T USE |
| collections.deque | O(1) | O(1) | O(n) | BEST |
| Circular array | O(1) | O(1) | O(n) | Fixed size |
| Linked list | O(1) | O(1) | O(n) | Extra pointers |

---

## Complexity Analysis

### Stack Operations

| Operation | Array | Linked List |
|-----------|-------|-------------|
| push() | O(1)* | O(1) |
| pop() | O(1) | O(1) |
| peek() | O(1) | O(1) |
| search() | O(n) | O(n) |
| Space | O(n) | O(n) |

\* Amortized O(1) due to occasional resize

### Queue Operations

| Operation | Deque | Circular Array | Linked List |
|-----------|-------|----------------|-------------|
| enqueue() | O(1) | O(1) | O(1) |
| dequeue() | O(1) | O(1) | O(1) |
| front() | O(1) | O(1) | O(1) |
| Space | O(n) | O(capacity) | O(n) |

### Monotonic Stack/Queue Complexity

**Amortized Analysis:**
- Each element pushed once: O(n)
- Each element popped at most once: O(n)
- Total: O(n) for n elements
- **Per operation: O(1) amortized**

---

## Key Insights

1. **LIFO vs FIFO**: Choose based on access pattern needed
2. **Python Lists**: Good for stack, BAD for queue
3. **collections.deque**: Best for both stack and queue
4. **Monotonic Structures**: Powerful O(n) pattern for "next greater/smaller"
5. **Circular Queue**: Efficient fixed-size buffer
6. **Priority Queue**: Use heapq for priority-based access
7. **Amortized O(1)**: Average cost over many operations

## When to Use What

**Stack:**
- Reversing order
- Backtracking
- Expression parsing
- DFS traversal

**Queue:**
- Processing in order
- BFS traversal
- Task scheduling
- Level-order processing

**Deque:**
- Sliding window max/min
- Both-end access
- Palindrome checking

**Priority Queue:**
- Always need min/max element
- Event simulation
- Greedy algorithms
- Graph algorithms (Dijkstra, Prim)

**Monotonic Stack:**
- Next greater/smaller element
- Stock span problems
- Histogram problems

**Monotonic Queue:**
- Sliding window extrema
- Range queries with moving window
