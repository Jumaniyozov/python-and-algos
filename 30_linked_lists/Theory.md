# Linked Lists: Theory and Fundamentals

## Table of Contents
1. [Introduction](#introduction)
2. [Singly Linked Lists](#singly-linked-lists)
3. [Doubly Linked Lists](#doubly-linked-lists)
4. [Circular Linked Lists](#circular-linked-lists)
5. [Common Techniques](#common-techniques)
6. [Complexity Analysis](#complexity-analysis)

---

## Introduction

A **linked list** is a linear data structure where elements are stored in nodes. Each node contains:
- **Data**: The value stored
- **Pointer(s)**: Reference to next (and possibly previous) node(s)

Unlike arrays, linked lists don't require contiguous memory allocation.

### Visual Representation

```
Singly Linked List:
HEAD -> [1|●] -> [2|●] -> [3|●] -> [4|NULL]

Doubly Linked List:
HEAD <-> [1] <-> [2] <-> [3] <-> [4] <-> NULL
NULL

Circular Linked List:
     ┌─────────────────────┐
     ↓                     │
   [1|●] -> [2|●] -> [3|●]─┘
```

---

## Singly Linked Lists

### Structure

Each node has:
- A data field
- A pointer to the next node

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Basic Operations

#### 1. Traversal
Visit each node from head to tail.

```
HEAD -> [1] -> [2] -> [3] -> [4] -> NULL
        ↑      ↑      ↑      ↑
      Step1  Step2  Step3  Step4
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

```python
def traverse(head):
    current = head
    while current:
        print(current.val)
        current = current.next
```

#### 2. Insertion

**At Head** - O(1):
```
Before: HEAD -> [2] -> [3] -> NULL
After:  HEAD -> [1] -> [2] -> [3] -> NULL
```

```python
def insert_at_head(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node  # new head
```

**At Tail** - O(n):
```
Before: HEAD -> [1] -> [2] -> [3] -> NULL
After:  HEAD -> [1] -> [2] -> [3] -> [4] -> NULL
```

```python
def insert_at_tail(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node

    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head
```

**At Position** - O(n):
```
Insert 5 at position 2:
Before: HEAD -> [1] -> [2] -> [3] -> NULL
After:  HEAD -> [1] -> [5] -> [2] -> [3] -> NULL
```

```python
def insert_at_position(head, val, pos):
    if pos == 0:
        return insert_at_head(head, val)

    current = head
    for _ in range(pos - 1):
        if not current:
            return head  # position out of bounds
        current = current.next

    new_node = ListNode(val)
    new_node.next = current.next
    current.next = new_node
    return head
```

#### 3. Deletion

**At Head** - O(1):
```
Before: HEAD -> [1] -> [2] -> [3] -> NULL
After:  HEAD -> [2] -> [3] -> NULL
```

```python
def delete_at_head(head):
    if not head:
        return None
    return head.next
```

**By Value** - O(n):
```
Delete node with value 2:
Before: HEAD -> [1] -> [2] -> [3] -> NULL
After:  HEAD -> [1] -> [3] -> NULL
```

```python
def delete_by_value(head, val):
    # Handle head deletion
    if head and head.val == val:
        return head.next

    current = head
    while current and current.next:
        if current.next.val == val:
            current.next = current.next.next
            return head
        current = current.next

    return head
```

**At Position** - O(n):
```python
def delete_at_position(head, pos):
    if pos == 0 and head:
        return head.next

    current = head
    for _ in range(pos - 1):
        if not current or not current.next:
            return head
        current = current.next

    if current.next:
        current.next = current.next.next
    return head
```

#### 4. Search

**Time Complexity**: O(n)
**Space Complexity**: O(1)

```python
def search(head, val):
    current = head
    position = 0
    while current:
        if current.val == val:
            return position
        current = current.next
        position += 1
    return -1  # not found
```

---

## Doubly Linked Lists

### Structure

Each node has:
- Data field
- Pointer to next node
- Pointer to previous node

```python
class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
```

### Advantages Over Singly Linked Lists

1. **Bidirectional Traversal**: Can traverse forward and backward
2. **Easier Deletion**: Can delete node without traversing from head
3. **Easier Insertion**: Can insert before a node more easily

### Disadvantages

1. **Extra Memory**: Each node stores two pointers instead of one
2. **Complex Operations**: More pointer updates needed

### Basic Operations

#### Insertion at Head - O(1)

```
Before: HEAD <-> [2] <-> [3] <-> NULL
After:  HEAD <-> [1] <-> [2] <-> [3] <-> NULL
```

```python
def insert_at_head(head, val):
    new_node = DoublyListNode(val)
    if head:
        new_node.next = head
        head.prev = new_node
    return new_node
```

#### Deletion - O(1) with Node Reference

```python
def delete_node(node):
    """Delete a node (not head) from doubly linked list"""
    if node.prev:
        node.prev.next = node.next
    if node.next:
        node.next.prev = node.prev
```

---

## Circular Linked Lists

### Structure

The last node points back to the first node (or head), forming a circle.

```
     ┌─────────────────────┐
     ↓                     │
   [1] -> [2] -> [3] -> [4]┘
```

### Use Cases

1. **Round-robin scheduling**: CPU scheduling, game turns
2. **Music playlists**: Loop back to first song
3. **Buffer management**: Circular buffers

### Detection

To detect if a linked list is circular:

```python
def is_circular(head):
    if not head:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False
```

---

## Common Techniques

### 1. Fast and Slow Pointers (Floyd's Algorithm)

Move two pointers at different speeds. Used for:
- Cycle detection
- Finding middle element
- Finding nth node from end

```
Cycle Detection:
slow →    [1] -> [2] -> [3] -> [4]
                        ↑      ↓
fast →                  [6] <- [5]

Step 1: slow=[1], fast=[2]
Step 2: slow=[2], fast=[4]
Step 3: slow=[3], fast=[6]
Step 4: slow=[4], fast=[3]
Step 5: slow=[5], fast=[5] ← CYCLE DETECTED!
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

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

### 2. Finding Middle Element

Use slow and fast pointers. When fast reaches end, slow is at middle.

```
[1] -> [2] -> [3] -> [4] -> [5] -> NULL
       slow         fast

Final: slow at [3] (middle)
```

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

### 3. Two Pointers Technique

Use two pointers with different starting positions or speeds.

**Finding nth Node from End**:
```
Find 2nd node from end in: [1] -> [2] -> [3] -> [4] -> [5] -> NULL

Step 1: Move fast n steps ahead
        [1] -> [2] -> [3] -> [4] -> [5] -> NULL
        slow        fast

Step 2: Move both until fast reaches end
        [1] -> [2] -> [3] -> [4] -> [5] -> NULL
                      slow         fast
```

```python
def nth_from_end(head, n):
    fast = head
    # Move fast n steps ahead
    for _ in range(n):
        if not fast:
            return None
        fast = fast.next

    slow = head
    while fast:
        slow = slow.next
        fast = fast.next

    return slow
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

### 4. Dummy Head Technique

Create a dummy node before head to simplify edge cases.

```
Dummy Head Pattern:
dummy -> [1] -> [2] -> [3] -> NULL
  ↑
 HEAD
```

**Benefits**:
- No special handling for head deletion
- Simpler insertion logic
- Easier to handle empty lists

```python
def delete_value_with_dummy(head, val):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next
```

### 5. Reversing Linked Lists

**Iterative Approach**:
```
Before: [1] -> [2] -> [3] -> [4] -> NULL
After:  [4] -> [3] -> [2] -> [1] -> NULL

Process:
prev = NULL, curr = [1]
NULL <- [1]    [2] -> [3] -> [4] -> NULL
        prev   curr

NULL <- [1] <- [2]    [3] -> [4] -> NULL
               prev   curr

NULL <- [1] <- [2] <- [3]    [4] -> NULL
                      prev   curr

NULL <- [1] <- [2] <- [3] <- [4]    NULL
                             prev   curr
```

```python
def reverse_iterative(head):
    prev = None
    current = head

    while current:
        next_temp = current.next  # Save next
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_temp       # Move current forward

    return prev
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

**Recursive Approach**:
```python
def reverse_recursive(head):
    # Base case
    if not head or not head.next:
        return head

    # Recursive case
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head
```

**Time Complexity**: O(n)
**Space Complexity**: O(n) - recursion stack

### 6. Merging Linked Lists

Merge two sorted linked lists into one sorted list.

```
List1: [1] -> [3] -> [5] -> NULL
List2: [2] -> [4] -> [6] -> NULL

Result: [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> NULL
```

```python
def merge_sorted_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach remaining nodes
    current.next = l1 if l1 else l2

    return dummy.next
```

**Time Complexity**: O(n + m) where n, m are lengths
**Space Complexity**: O(1)

### 7. Cycle Detection and Finding Cycle Start

**Detecting Cycle**: Use Floyd's algorithm (fast/slow pointers)

**Finding Cycle Start**:
```
     [1] -> [2] -> [3] -> [4]
                   ↑      ↓
                   [6] <- [5]

Algorithm:
1. Detect cycle using fast/slow
2. Reset one pointer to head
3. Move both one step at a time
4. They meet at cycle start
```

```python
def detect_cycle_start(head):
    # Phase 1: Detect cycle
    slow = fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

---

## Complexity Analysis

### Time Complexity Summary

| Operation | Singly | Doubly | Array | Notes |
|-----------|--------|--------|-------|-------|
| Access by index | O(n) | O(n) | O(1) | Must traverse from head |
| Search | O(n) | O(n) | O(n) | Linear search |
| Insert at head | O(1) | O(1) | O(n) | LL wins |
| Insert at tail | O(n)* | O(1)** | O(1)*** | *O(1) with tail ptr, **with tail ptr, ***amortized |
| Insert at position | O(n) | O(n) | O(n) | Must find position |
| Delete at head | O(1) | O(1) | O(n) | LL wins |
| Delete at tail | O(n) | O(1) | O(1) | DLL wins |
| Delete at position | O(n) | O(n) | O(n) | Must find position |
| Delete given node | O(1)* | O(1) | O(n) | *Only if have prev reference |

### Space Complexity

**Per Node**:
- Singly Linked List: O(1) + pointer overhead
- Doubly Linked List: O(1) + 2× pointer overhead
- Array: O(1)

**Total for n elements**:
- All structures: O(n)
- But linked lists have higher constant factor due to pointers

### Cache Performance

**Arrays**: Excellent cache locality (contiguous memory)
**Linked Lists**: Poor cache locality (scattered memory)

Impact: Arrays often faster in practice for small to medium datasets, even when LL has better theoretical complexity.

---

## When to Use Linked Lists

### Use Linked Lists When:

✅ **Frequent insertions/deletions at beginning**
- Example: Implementing a stack

✅ **Don't know size in advance**
- Example: Reading data from stream

✅ **Memory fragmentation is an issue**
- Example: Embedded systems with limited contiguous memory

✅ **Implementing other data structures**
- Example: Adjacency lists for graphs, chaining in hash tables

### Use Arrays When:

✅ **Need random access**
- Example: Binary search

✅ **Cache performance matters**
- Example: Iterating frequently over data

✅ **Memory overhead is critical**
- Example: Storing millions of small objects

✅ **Size is known and fixed**
- Example: Fixed configuration data

---

## Common Pitfalls and Best Practices

### Pitfalls

1. **Forgetting to update head**: When inserting/deleting at head
2. **Memory leaks**: Not freeing deleted nodes (in languages with manual memory management)
3. **Infinite loops**: When modifying pointers incorrectly
4. **Null pointer exceptions**: Not checking for null before accessing .next
5. **Lost tail reference**: Forgetting to maintain tail pointer

### Best Practices

1. **Always check for null**: Before accessing node.next
2. **Use dummy nodes**: To simplify edge cases
3. **Draw diagrams**: Visualize pointer changes
4. **Test edge cases**: Empty list, single node, two nodes
5. **Consider maintaining tail pointer**: For O(1) tail operations
6. **Use slow/fast pointers**: For efficient algorithms

### Edge Cases to Consider

- Empty list (head = null)
- Single node list
- Two node list
- Operations at boundaries (head, tail)
- Circular references
- Even vs odd length lists (for middle element)

---

## Advanced Topics

### 1. Skip Lists

A probabilistic data structure that allows O(log n) search, insert, and delete on average.

```
Level 2:  1 ----------------> 9 -> NULL
Level 1:  1 ------> 4 ------> 9 -> NULL
Level 0:  1 -> 2 -> 4 -> 6 -> 9 -> NULL
```

### 2. Self-Organizing Lists

Lists that reorganize based on access patterns:
- Move-to-Front: Accessed item moved to front
- Transpose: Accessed item swapped with previous
- Frequency Count: Sort by access frequency

### 3. XOR Linked Lists

Use XOR to store both prev and next in single pointer (memory optimization).

```python
# Each node stores: prev XOR next
# To traverse: next = prev XOR current.link
```

**Pros**: Memory efficient
**Cons**: Complex, not cache-friendly, debugging difficult

---

## Summary

Linked lists are fundamental data structures with unique advantages:

**Key Strengths**:
- Dynamic size
- Efficient insertion/deletion at beginning
- No wasted memory
- Foundation for other structures

**Key Weaknesses**:
- No random access
- Poor cache locality
- Extra memory for pointers
- Traversal required for most operations

**Master These Patterns**:
1. Two pointers (fast/slow)
2. Dummy head
3. Reversal (iterative and recursive)
4. Cycle detection
5. Merging sorted lists

Understanding these fundamentals will prepare you for complex data structures and algorithms!
