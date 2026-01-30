# Linked Lists: Tips and Best Practices

## Common Patterns

### 1. Two Pointer Techniques

**Fast and Slow Pointers (Floyd's Tortoise and Hare)**
```python
# Find middle of list
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is at middle

# Detect cycle
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # Cycle detected
return False
```

**Gap Pointers**
```python
# Remove nth node from end
# Create gap of n between fast and slow
fast = slow = head
for _ in range(n):
    fast = fast.next

while fast.next:
    fast = fast.next
    slow = slow.next
# slow is at node before target
```

**Prev-Current-Next Pattern**
```python
# Reversal and modification
prev = None
current = head
while current:
    next_temp = current.next  # Save next
    current.next = prev       # Reverse link
    prev = current            # Move prev
    current = next_temp       # Move current
return prev
```

---

### 2. Dummy Node Pattern

**When to Use:**
- Head might be removed/changed
- Simplifies edge cases
- Uniform handling of all nodes

```python
# Without dummy (complex)
if not head:
    return None
if head.val == target:
    return head.next
current = head
while current.next:
    if current.next.val == target:
        current.next = current.next.next
        break
    current = current.next

# With dummy (simple)
dummy = ListNode(0)
dummy.next = head
current = dummy
while current.next:
    if current.next.val == target:
        current.next = current.next.next
        break
    current = current.next
return dummy.next
```

**Pro Tip:** Always use dummy when:
- Deleting nodes (especially head)
- Building new list
- Merging lists
- Partitioning lists

---

### 3. Reversal Techniques

**Iterative (Preferred for Space)**
```python
def reverse_iterative(head):
    prev = None
    current = head
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev
```

**Recursive (Elegant)**
```python
def reverse_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

**Partial Reversal**
```python
# Reverse first k nodes
def reverse_k(head, k):
    prev = None
    current = head
    for _ in range(k):
        if not current:
            break
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev, current  # new_head, rest
```

---

### 4. Merging Patterns

**Merge Two Lists**
```python
# Always use dummy for merging
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

# Attach remaining (at most one is non-empty)
current.next = l1 or l2

return dummy.next
```

**Merge K Lists**
```python
# Use min heap for efficiency
import heapq

heap = []
for i, node in enumerate(lists):
    if node:
        heapq.heappush(heap, (node.val, i, node))

dummy = ListNode(0)
current = dummy

while heap:
    val, i, node = heapq.heappop(heap)
    current.next = node
    current = current.next
    if node.next:
        heapq.heappush(heap, (node.next.val, i, node.next))

return dummy.next
```

---

### 5. Cycle Detection and Handling

**Floyd's Algorithm (Detect)**
```python
def has_cycle(head):
    if not head or not head.next:
        return False

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**Find Cycle Start**
```python
def detect_cycle(head):
    # Phase 1: Detect
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    # Phase 2: Find start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
```

**Mathematical Proof:**
```
Let:
  a = distance from head to cycle start
  b = distance from cycle start to meeting point
  c = cycle length

When they meet:
  slow traveled: a + b
  fast traveled: a + b + nc (n cycles)

Since fast is 2x slow:
  2(a + b) = a + b + nc
  a + b = nc
  a = nc - b

Therefore: Starting from head and meeting point,
           both reach cycle start simultaneously!
```

---

### 6. Partitioning Patterns

**Two-List Partition**
```python
# Partition around value x
before = before_head = ListNode(0)
after = after_head = ListNode(0)

current = head
while current:
    if current.val < x:
        before.next = current
        before = before.next
    else:
        after.next = current
        after = after.next
    current = current.next

# Important: terminate after list!
after.next = None
before.next = after_head.next

return before_head.next
```

**Three-Way Partition (Dutch National Flag)**
```python
# Partition into <, ==, >
low = low_head = ListNode(0)
mid = mid_head = ListNode(0)
high = high_head = ListNode(0)

current = head
while current:
    if current.val < pivot:
        low.next = current
        low = low.next
    elif current.val == pivot:
        mid.next = current
        mid = mid.next
    else:
        high.next = current
        high = high.next
    current = current.next

# Terminate and connect
high.next = None
mid.next = high_head.next
low.next = mid_head.next

return low_head.next
```

---

### 7. In-Place Modifications

**Swap Adjacent Nodes**
```python
# Maintain three pointers: prev, first, second
dummy = ListNode(0)
dummy.next = head
prev = dummy

while prev.next and prev.next.next:
    first = prev.next
    second = first.next

    # Swap
    first.next = second.next
    second.next = first
    prev.next = second

    # Move prev
    prev = first
```

**Interweave Two Lists**
```python
# Example: Reorder list
# 1->2->3->4->5 becomes 1->5->2->4->3

first = head
second = reversed_second_half

while second:
    temp1 = first.next
    temp2 = second.next

    first.next = second
    second.next = temp1

    first = temp1
    second = temp2
```

---

## Common Mistakes to Avoid

### 1. Null Pointer Errors

**Bad:**
```python
# Doesn't check if head exists
def get_length(head):
    length = 0
    while head:  # If head is None, this works
        length += 1
        head = head.next
    return length

# But this crashes:
def get_value(head):
    return head.val  # Crashes if head is None!
```

**Good:**
```python
def get_value(head):
    if not head:
        return None
    return head.val

# Always check before accessing:
# - head.val
# - head.next
# - head.next.val
```

### 2. Creating Unintended Cycles

**Bad:**
```python
# Forgetting to terminate list
after.next = None  # MUST DO THIS!
before.next = after_head.next
```

**Good:**
```python
# Always terminate when splitting
def split_list(head, k):
    # ... find split point ...
    tail.next = None  # Critical!
    return head, rest
```

### 3. Off-by-One Errors

**Bad:**
```python
# Remove nth from end - WRONG
fast = head
for _ in range(n):  # Should be n+1
    fast = fast.next
```

**Good:**
```python
# Correct gap creation
dummy = ListNode(0)
dummy.next = head
fast = slow = dummy

for _ in range(n + 1):  # n+1 gap
    fast = fast.next

while fast:
    fast = fast.next
    slow = slow.next

slow.next = slow.next.next  # Now safe
```

### 4. Modifying Input When Not Allowed

**Bad:**
```python
# Problem says "don't modify input"
def is_palindrome(head):
    # ... reverses second half ...
    # List is now modified!
```

**Good:**
```python
# Restore original state
def is_palindrome(head):
    # ... find middle, reverse second half ...

    # Check palindrome
    result = compare(first, second)

    # Restore (reverse second half back)
    reverse(middle)

    return result
```

### 5. Memory Leaks (Language Dependent)

**Bad (in languages with manual memory):**
```python
# In C/C++: not freeing deleted nodes
def delete_node(node):
    temp = node.next
    node.val = temp.val
    node.next = temp.next
    # Should: free(temp)
```

**Good:**
```python
# In Python: automatic garbage collection
# But still, clear references if keeping nodes:
def delete_node(node):
    temp = node.next
    node.val = temp.val
    node.next = temp.next
    temp.next = None  # Help GC (optional in Python)
```

---

## Pointer Manipulation Tricks

### 1. Fast Node Finding

**Find Kth from End (One Pass)**
```python
# Create gap of k, move both together
fast = head
for _ in range(k):
    fast = fast.next

slow = head
while fast:
    fast = fast.next
    slow = slow.next

return slow  # kth from end
```

### 2. List Intersection

**Without Extra Space**
```python
# Key insight: if we switch heads when reaching end,
# both pointers travel same distance to intersection

pA = headA
pB = headB

while pA != pB:
    pA = pA.next if pA else headB
    pB = pB.next if pB else headA

return pA  # Intersection or None
```

### 3. Copy with Random Pointer

**Interweaving Technique**
```python
# Step 1: Interweave old and new
# Old: 1 -> 2 -> 3
# New: 1 -> 1' -> 2 -> 2' -> 3 -> 3'

current = head
while current:
    copy = Node(current.val)
    copy.next = current.next
    current.next = copy
    current = copy.next

# Step 2: Set random pointers
current = head
while current:
    if current.random:
        current.next.random = current.random.next
    current = current.next.next

# Step 3: Separate lists
# ... split interweaved list ...
```

### 4. Sorting Optimizations

**Merge Sort (Best for Linked Lists)**
```python
# Why merge sort? No random access needed
# Time: O(n log n), Space: O(log n) recursion

def merge_sort(head):
    if not head or not head.next:
        return head

    # Find middle
    mid = find_middle(head)
    right = mid.next
    mid.next = None

    # Sort halves
    left = merge_sort(head)
    right = merge_sort(right)

    # Merge
    return merge(left, right)
```

**Insertion Sort (When Nearly Sorted)**
```python
# Good when list is nearly sorted
# Time: O(n^2) worst, O(n) best
# Space: O(1)

def insertion_sort(head):
    dummy = ListNode(float('-inf'))
    current = head

    while current:
        prev = dummy
        # Find insertion point
        while prev.next and prev.next.val < current.val:
            prev = prev.next

        # Insert
        next_temp = current.next
        current.next = prev.next
        prev.next = current
        current = next_temp

    return dummy.next
```

---

## Optimization Techniques

### 1. Space Optimization

**Use O(1) Space Instead of O(n)**
```python
# Instead of storing in array:
def process_list_bad(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    # Process arr...

# Process in-place:
def process_list_good(head):
    current = head
    while current:
        # Process current
        current = current.next
```

### 2. Single Pass vs Multiple Passes

**When Single Pass Matters**
```python
# If list is very long or streaming data

# Bad: Multiple passes
def remove_nth_from_end(head, n):
    # Pass 1: Get length
    length = get_length(head)
    # Pass 2: Remove
    # ...

# Good: Single pass with gap pointers
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next
```

### 3. Early Termination

```python
# Stop as soon as answer found
def find_intersection(headA, headB):
    pA, pB = headA, headB

    while pA != pB:  # Stops when equal (intersection or None)
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA  # Early termination when found
```

### 4. Avoid Unnecessary Reversals

**Bad:**
```python
# Reverse entire list to check palindrome
def is_palindrome(head):
    reversed_list = reverse(copy_list(head))
    # Compare original and reversed
```

**Good:**
```python
# Only reverse second half
def is_palindrome(head):
    mid = find_middle(head)
    second = reverse(mid)
    # Compare first half and reversed second half
    # Can restore if needed
```

---

## Debugging Tips

### 1. Visualize with Print

```python
def print_list(head, name="List"):
    values = []
    current = head
    count = 0
    while current and count < 20:  # Limit for cycle detection
        values.append(str(current.val))
        current = current.next
        count += 1

    if count == 20 and current:
        values.append("... (cycle or long list)")

    print(f"{name}: {' -> '.join(values)}")
```

### 2. Check Invariants

```python
def validate_list(head):
    """Check list integrity."""
    # Check for cycles
    visited = set()
    current = head

    while current:
        if current in visited:
            print("ERROR: Cycle detected!")
            return False
        visited.add(current)
        current = current.next

    print("List is valid")
    return True
```

### 3. Step-by-Step Debugging

```python
def reverse_with_debug(head):
    print(f"Initial: {list_to_string(head)}")

    prev = None
    current = head

    while current:
        next_temp = current.next
        current.next = prev

        print(f"Reversed {current.val}, now points to {prev.val if prev else None}")

        prev = current
        current = next_temp

    print(f"Final: {list_to_string(prev)}")
    return prev
```

---

## Practice Strategy

### 1. Master These Patterns First
1. Two pointers (fast/slow)
2. Dummy node usage
3. Reversal (iterative)
4. Basic merging
5. Cycle detection

### 2. Then Progress To
1. Partial reversal
2. K-way merging
3. Complex partitioning
4. In-place modifications
5. Combined techniques

### 3. Problem-Solving Approach

```
1. Draw it out (visual representation)
2. Identify pattern (two pointers? reversal? merging?)
3. Consider edge cases (null, single, two nodes)
4. Write algorithm steps
5. Code with comments
6. Test systematically
7. Optimize if needed
```

### 4. Common Edge Cases Checklist

```python
# Always test:
test_cases = [
    None,           # Empty list
    [1],            # Single node
    [1, 2],         # Two nodes
    [1, 2, 3],      # Odd length
    [1, 2, 3, 4],   # Even length
    [1, 1, 1],      # All duplicates
    [-1, 0, 1],     # Negative numbers
    # Problem-specific cases
]
```

---

## Interview Tips

### What Interviewers Look For

1. **Null checks** - Always validate input
2. **Edge case handling** - Think of empty, single, two nodes
3. **Pointer management** - No memory leaks, correct updates
4. **Space efficiency** - Prefer O(1) when possible
5. **Code clarity** - Readable, well-commented

### Common Interview Questions

**Easy:**
- Reverse linked list
- Merge two sorted lists
- Remove duplicates
- Delete node (given node)
- Palindrome check

**Medium:**
- Reorder list
- Remove nth from end
- Copy with random pointer
- Add two numbers
- Sort list

**Hard:**
- Merge k sorted lists
- Reverse nodes in k-group
- LRU Cache

### How to Communicate

```python
# Good practice:
"I'll use two pointers here - slow and fast.
Fast moves twice as fast, so when fast reaches end,
slow will be at middle. This gives us O(n) time
and O(1) space. Let me code it up..."

# Then implement with clear variable names
slow = head
fast = head
# ... clear, commented code ...
```

---

## Summary

**Key Principles:**
1. **Draw first** - Visualize before coding
2. **Check nulls** - Always validate pointers
3. **Use dummy** - Simplifies edge cases
4. **Test edges** - Empty, one, two nodes
5. **Think space** - Can you do it in O(1)?
6. **Prefer iterative** - Usually clearer and more space-efficient
7. **Master basics** - Reversal, merging, two pointers
8. **Practice patterns** - Same techniques appear repeatedly

**Common Time Complexities:**
- Single pass: O(n)
- Reversal: O(n)
- Merge two lists: O(n + m)
- Find middle: O(n)
- Cycle detection: O(n)
- Sort (merge sort): O(n log n)
- K-way merge: O(N log k)

**Space Complexity Goals:**
- Iterative solutions: O(1)
- Recursive solutions: O(n) or O(log n)
- With hash map: O(n)

Master these patterns, and you'll be able to solve most linked list problems efficiently!

---

## LeetCode Practice Problems

### 📊 Problem Statistics
- **Total Problems:** 55+
- **Easy:** 18 problems
- **Medium:** 25 problems
- **Hard:** 12 problems
- **Estimated Time:** 35-50 hours

---

## Easy Problems (18)

### 1. Reverse Linked List
**Link:** https://leetcode.com/problems/reverse-linked-list/  
**Pattern:** Pointer Manipulation  
**Topics:** Linked List, Recursion  
**Description:** Reverse a singly linked list  
**Why Practice:** Foundation for many linked list problems

### 2. Merge Two Sorted Lists
**Link:** https://leetcode.com/problems/merge-two-sorted-lists/  
**Pattern:** Two Pointers  
**Topics:** Linked List, Recursion  
**Description:** Merge two sorted lists  
**Why Practice:** Classic merge technique

### 3. Remove Duplicates from Sorted List
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-list/  
**Pattern:** Single Pass  
**Topics:** Linked List  
**Description:** Remove duplicate values  
**Why Practice:** Basic list traversal and modification

### 4. Linked List Cycle
**Link:** https://leetcode.com/problems/linked-list-cycle/  
**Pattern:** Fast and Slow Pointers  
**Topics:** Linked List, Two Pointers, Hash Table  
**Description:** Detect if list has cycle  
**Why Practice:** Floyd's cycle detection algorithm

### 5. Intersection of Two Linked Lists
**Link:** https://leetcode.com/problems/intersection-of-two-linked-lists/  
**Pattern:** Two Pointers  
**Topics:** Linked List, Hash Table, Two Pointers  
**Description:** Find intersection node  
**Why Practice:** Two pointer synchronization

### 6. Remove Linked List Elements
**Link:** https://leetcode.com/problems/remove-linked-list-elements/  
**Pattern:** Dummy Head  
**Topics:** Linked List, Recursion  
**Description:** Remove all nodes with value  
**Why Practice:** Dummy head technique

### 7. Palindrome Linked List
**Link:** https://leetcode.com/problems/palindrome-linked-list/  
**Pattern:** Fast/Slow Pointers + Reverse  
**Topics:** Linked List, Two Pointers, Stack, Recursion  
**Description:** Check if list is palindrome  
**Why Practice:** Combining multiple techniques

### 8. Middle of the Linked List
**Link:** https://leetcode.com/problems/middle-of-the-linked-list/  
**Pattern:** Fast and Slow Pointers  
**Topics:** Linked List, Two Pointers  
**Description:** Find middle node  
**Why Practice:** Fast/slow pointer basics

### 9. Delete Node in a Linked List
**Link:** https://leetcode.com/problems/delete-node-in-a-linked-list/  
**Pattern:** Node Manipulation  
**Topics:** Linked List  
**Description:** Delete node given only that node  
**Why Practice:** Unique constraint handling

### 10. Convert Binary Number in a Linked List to Integer
**Link:** https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/  
**Pattern:** Traversal  
**Topics:** Linked List, Math  
**Description:** Convert binary linked list to integer  
**Why Practice:** List traversal with calculation

### 11. Merge In Between Linked Lists
**Link:** https://leetcode.com/problems/merge-in-between-linked-lists/  
**Pattern:** Pointer Manipulation  
**Topics:** Linked List  
**Description:** Replace part of list with another  
**Why Practice:** Multiple pointer tracking

### 12. Design Linked List
**Link:** https://leetcode.com/problems/design-linked-list/  
**Pattern:** Implementation  
**Topics:** Linked List, Design  
**Description:** Implement linked list operations  
**Why Practice:** Understanding all operations

### 13. Remove Nth Node From End of List (Can be Medium)
**Link:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/  
**Pattern:** Two Pointers  
**Topics:** Linked List, Two Pointers  
**Description:** Remove nth node from end  
**Why Practice:** Two pointer with gap

### 14. Reverse Linked List II (Medium but good for practice)
**Link:** https://leetcode.com/problems/reverse-linked-list-ii/  
**Pattern:** Pointer Manipulation  
**Topics:** Linked List  
**Description:** Reverse from position m to n  
**Why Practice:** Partial reversal technique

### 15. Odd Even Linked List
**Link:** https://leetcode.com/problems/odd-even-linked-list/  
**Pattern:** Two Pointers  
**Topics:** Linked List  
**Description:** Group odd/even nodes  
**Why Practice:** Two-list building

### 16. Design HashSet (using linked list)
**Link:** https://leetcode.com/problems/design-hashset/  
**Pattern:** Design  
**Topics:** Array, Hash Table, Linked List, Design  
**Description:** Implement HashSet  
**Why Practice:** Chaining implementation

### 17. Design HashMap (using linked list)
**Link:** https://leetcode.com/problems/design-hashmap/  
**Pattern:** Design  
**Topics:** Array, Hash Table, Linked List, Design  
**Description:** Implement HashMap  
**Why Practice:** Hash table with chaining

### 18. Next Greater Node In Linked List
**Link:** https://leetcode.com/problems/next-greater-node-in-linked-list/  
**Pattern:** Stack + Linked List  
**Topics:** Array, Linked List, Stack, Monotonic Stack  
**Description:** Find next greater value  
**Why Practice:** Combining list with stack

---

## Medium Problems (25)

### 19. Add Two Numbers
**Link:** https://leetcode.com/problems/add-two-numbers/  
**Pattern:** Math + Linked List  
**Topics:** Linked List, Math, Recursion  
**Description:** Add two numbers represented as linked lists  
**Why Practice:** Carry handling with lists

### 20. Remove Nth Node From End of List
**Link:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/  
**Pattern:** Two Pointers  
**Topics:** Linked List, Two Pointers  
**Description:** Remove nth from end in one pass  
**Why Practice:** Two pointers with fixed gap

### 21. Swap Nodes in Pairs
**Link:** https://leetcode.com/problems/swap-nodes-in-pairs/  
**Pattern:** Pointer Manipulation  
**Topics:** Linked List, Recursion  
**Description:** Swap every two adjacent nodes  
**Why Practice:** Pair-wise operations

### 22. Rotate List
**Link:** https://leetcode.com/problems/rotate-list/  
**Pattern:** Two Pointers  
**Topics:** Linked List, Two Pointers  
**Description:** Rotate list to the right by k  
**Why Practice:** Circular list technique

### 23. Partition List
**Link:** https://leetcode.com/problems/partition-list/  
**Pattern:** Two Lists  
**Topics:** Linked List, Two Pointers  
**Description:** Partition around value x  
**Why Practice:** Building two lists

### 24. Odd Even Linked List
**Link:** https://leetcode.com/problems/odd-even-linked-list/  
**Pattern:** Two Pointers  
**Topics:** Linked List  
**Description:** Group odd and even positioned nodes  
**Why Practice:** Maintaining two sublists

### 25. Reverse Linked List II
**Link:** https://leetcode.com/problems/reverse-linked-list-ii/  
**Pattern:** Pointer Manipulation  
**Topics:** Linked List  
**Description:** Reverse between positions m and n  
**Why Practice:** Partial reversal

### 26. Reorder List
**Link:** https://leetcode.com/problems/reorder-list/  
**Pattern:** Fast/Slow + Reverse + Merge  
**Topics:** Linked List, Two Pointers, Stack, Recursion  
**Description:** Reorder L0→L1→...→Ln-1→Ln to L0→Ln→L1→Ln-1→...  
**Why Practice:** Combining multiple operations

### 27. Linked List Cycle II
**Link:** https://leetcode.com/problems/linked-list-cycle-ii/  
**Pattern:** Fast and Slow Pointers  
**Topics:** Linked List, Hash Table, Two Pointers  
**Description:** Find cycle starting node  
**Why Practice:** Floyd's algorithm extension

### 28. Copy List with Random Pointer
**Link:** https://leetcode.com/problems/copy-list-with-random-pointer/  
**Pattern:** Hash Map / Interweaving  
**Topics:** Linked List, Hash Table  
**Description:** Deep copy list with random pointers  
**Why Practice:** Complex cloning technique

### 29. Sort List
**Link:** https://leetcode.com/problems/sort-list/  
**Pattern:** Merge Sort  
**Topics:** Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort  
**Description:** Sort linked list in O(n log n)  
**Why Practice:** Merge sort on linked list

### 30. Insertion Sort List
**Link:** https://leetcode.com/problems/insertion-sort-list/  
**Pattern:** Insertion Sort  
**Topics:** Linked List, Sorting  
**Description:** Sort using insertion sort  
**Why Practice:** Insertion in sorted list

### 31. Delete the Middle Node of a Linked List
**Link:** https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/  
**Pattern:** Fast and Slow Pointers  
**Topics:** Linked List, Two Pointers  
**Description:** Remove middle node  
**Why Practice:** Finding and deleting middle

### 32. Swapping Nodes in a Linked List
**Link:** https://leetcode.com/problems/swapping-nodes-in-a-linked-list/  
**Pattern:** Two Pointers  
**Topics:** Linked List, Two Pointers  
**Description:** Swap kth node from beginning and end  
**Why Practice:** Symmetric operations

### 33. Add Two Numbers II
**Link:** https://leetcode.com/problems/add-two-numbers-ii/  
**Pattern:** Stack  
**Topics:** Linked List, Math, Stack  
**Description:** Add without reversing lists  
**Why Practice:** Using stack for reverse order

### 34. Remove Zero Sum Consecutive Nodes
**Link:** https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/  
**Pattern:** Prefix Sum + Hash Map  
**Topics:** Linked List, Hash Table  
**Description:** Remove sequences that sum to zero  
**Why Practice:** Prefix sum with linked list

### 35. Split Linked List in Parts
**Link:** https://leetcode.com/problems/split-linked-list-in-parts/  
**Pattern:** Array of Lists  
**Topics:** Linked List  
**Description:** Split into k consecutive parts  
**Why Practice:** List partitioning

### 36. Flatten a Multilevel Doubly Linked List
**Link:** https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/  
**Pattern:** DFS / Stack  
**Topics:** Linked List, Depth-First Search, Doubly-Linked List  
**Description:** Flatten multilevel list  
**Why Practice:** Handling child pointers

### 37. Convert Sorted List to Binary Search Tree
**Link:** https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/  
**Pattern:** Divide and Conquer  
**Topics:** Linked List, Divide and Conquer, Tree, Binary Search Tree, Binary Tree  
**Description:** Build balanced BST from sorted list  
**Why Practice:** List to tree conversion

### 38. Design Browser History
**Link:** https://leetcode.com/problems/design-browser-history/  
**Pattern:** Doubly Linked List  
**Topics:** Array, Linked List, Stack, Design, Doubly-Linked List, Data Stream  
**Description:** Implement browser history  
**Why Practice:** Practical doubly-linked list application

### 39. LRU Cache
**Link:** https://leetcode.com/problems/lru-cache/  
**Pattern:** Hash Map + Doubly Linked List  
**Topics:** Hash Table, Linked List, Design, Doubly-Linked List  
**Description:** Implement LRU cache  
**Why Practice:** Classic design problem

### 40. Flatten Binary Tree to Linked List
**Link:** https://leetcode.com/problems/flatten-binary-tree-to-linked-list/  
**Pattern:** Tree to List  
**Topics:** Linked List, Stack, Tree, Depth-First Search, Binary Tree  
**Description:** Flatten tree to linked list  
**Why Practice:** Tree transformation

### 41. Maximum Twin Sum of a Linked List
**Link:** https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/  
**Pattern:** Fast/Slow + Reverse  
**Topics:** Linked List, Two Pointers, Stack  
**Description:** Find maximum twin sum  
**Why Practice:** Symmetric operations

### 42. Linked List Random Node
**Link:** https://leetcode.com/problems/linked-list-random-node/  
**Pattern:** Reservoir Sampling  
**Topics:** Linked List, Math, Reservoir Sampling, Randomized  
**Description:** Return random node value  
**Why Practice:** Reservoir sampling algorithm

### 43. Find the Minimum and Maximum Number of Nodes Between Critical Points
**Link:** https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/  
**Pattern:** Single Pass  
**Topics:** Linked List  
**Description:** Find critical point distances  
**Why Practice:** Pattern detection in list

---

## Hard Problems (12)

### 44. Merge k Sorted Lists
**Link:** https://leetcode.com/problems/merge-k-sorted-lists/  
**Pattern:** Heap / Divide and Conquer  
**Topics:** Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort  
**Description:** Merge k sorted linked lists  
**Why Practice:** K-way merge with heap

### 45. Reverse Nodes in k-Group
**Link:** https://leetcode.com/problems/reverse-nodes-in-k-group/  
**Pattern:** Pointer Manipulation  
**Topics:** Linked List, Recursion  
**Description:** Reverse nodes in groups of k  
**Why Practice:** Complex reversal pattern

### 46. Copy List with Random Pointer II (Design)
**Link:** https://leetcode.com/problems/copy-list-with-random-pointer/  
**Pattern:** Hash Map / Interweaving  
**Topics:** Linked List, Hash Table  
**Description:** Deep copy with O(1) space  
**Why Practice:** Space-optimized cloning

### 47. LFU Cache
**Link:** https://leetcode.com/problems/lfu-cache/  
**Pattern:** Hash Map + Doubly Linked List  
**Topics:** Hash Table, Linked List, Design, Doubly-Linked List  
**Description:** Implement LFU cache  
**Why Practice:** More complex than LRU

### 48. All O`one Data Structure
**Link:** https://leetcode.com/problems/all-oone-data-structure/  
**Pattern:** Hash Map + Doubly Linked List  
**Topics:** Hash Table, Linked List, Design, Doubly-Linked List  
**Description:** Inc, dec, getMax, getMin in O(1)  
**Why Practice:** Advanced data structure design

### 49. Design Skiplist
**Link:** https://leetcode.com/problems/design-skiplist/  
**Pattern:** Multi-level Linked List  
**Topics:** Linked List, Design  
**Description:** Implement skip list  
**Why Practice:** Probabilistic data structure

### 50. Median from Data Stream (using linked list approach)
**Link:** https://leetcode.com/problems/find-median-from-data-stream/  
**Pattern:** Two Heaps / Balanced Structure  
**Topics:** Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream  
**Description:** Find median in stream  
**Why Practice:** Balanced structure maintenance

### 51. Palindrome Linked List (O(1) space)
**Link:** https://leetcode.com/problems/palindrome-linked-list/  
**Pattern:** Fast/Slow + Reverse  
**Topics:** Linked List, Two Pointers, Stack, Recursion  
**Description:** Check palindrome with O(1) space  
**Why Practice:** Space-optimized solution

### 52. Rearrange String k Distance Apart (list-based)
**Link:** https://leetcode.com/problems/rearrange-string-k-distance-apart/  
**Pattern:** Greedy + Queue  
**Topics:** Hash Table, String, Greedy, Sorting, Heap (Priority Queue), Counting  
**Description:** Rearrange with distance k  
**Why Practice:** Complex constraint handling (Premium)

### 53. Design Phone Directory (using linked list)
**Link:** https://leetcode.com/problems/design-phone-directory/  
**Pattern:** Design  
**Topics:** Array, Hash Table, Linked List, Design, Queue  
**Description:** Implement phone directory  
**Why Practice:** Resource management (Premium)

### 54. Plus One Linked List
**Link:** https://leetcode.com/problems/plus-one-linked-list/  
**Pattern:** Recursion / Reverse  
**Topics:** Linked List, Math  
**Description:** Add one to number in list  
**Why Practice:** Carry propagation (Premium)

### 55. Remove Nth Node From End (One Pass, Hard constraints)
**Link:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/  
**Pattern:** Two Pointers  
**Topics:** Linked List, Two Pointers  
**Description:** Remove with strict constraints  
**Why Practice:** Optimal solution requirements

---

## Practice Progression

### Week 1: Basics (Easy 1-12)
Master fundamental operations:
- Reversal (1)
- Merging (2)
- Cycle detection (4)
- Fast/slow pointers (8)

### Week 2: Intermediate Easy (Easy 13-18)
More complex patterns:
- Two pointer gap (13)
- Design problems (16, 17)
- List modification (14, 15)

### Week 3-4: Medium Basics (Medium 19-30)
Foundation medium problems:
- Add numbers (19, 33)
- Sorting (29, 30)
- Complex operations (25, 26, 27)

### Week 5-6: Advanced Medium (Medium 31-43)
Complex patterns:
- LRU Cache (39) - MUST KNOW
- Tree/List conversion (37, 40)
- Advanced techniques (34, 35, 36)

### Week 7-8: Hard Problems (Hard 44-55)
Challenge problems:
- Merge k Lists (44) - Very common
- Reverse in k-Group (45)
- LFU Cache (47)
- Skip List (49)

---

## Pattern Mastery Guide

### Fast and Slow Pointers (Floyd's Algorithm)
**Problems:** 4, 8, 27, 31
**Key Insight:** Slow moves 1 step, fast moves 2 steps
**Applications:**
- Cycle detection
- Finding middle
- Finding cycle start
- Palindrome checking

### Dummy Head Technique
**Problems:** 2, 6, 19, 21
**Key Insight:** Use dummy node before head to handle edge cases
**When to Use:**
- Removing nodes
- Merging lists
- Building new lists

### Two Pointers with Gap
**Problems:** 13, 20, 32
**Key Insight:** Maintain fixed distance between pointers
**Applications:**
- Remove nth from end
- Symmetric operations

### Reversal Techniques
**Problems:** 1, 14, 25, 26, 45
**Key Insight:** Reverse iteratively or recursively
**Patterns:**
- Full reversal
- Partial reversal
- Reversal in groups

### Multi-List Operations
**Problems:** 23, 24, 29, 44
**Key Insight:** Maintain multiple pointers/lists
**Applications:**
- Partitioning
- Grouping
- Merging k lists

---

## Common Mistakes to Avoid

1. **Not handling null checks:** Always check for null pointers
2. **Losing references:** Save next node before modifying pointers
3. **Off-by-one errors:** Carefully handle edge cases
4. **Not using dummy head:** Makes code cleaner for many problems
5. **Forgetting to advance pointers:** Infinite loops are common
6. **Memory leaks:** Not freeing nodes in languages like C/C++

---

## Interview Tips

### Must-Know Problems (Top 10)
1. Reverse Linked List (1) - MUST KNOW
2. Merge Two Sorted Lists (2) - MUST KNOW
3. Linked List Cycle (4) - MUST KNOW
4. Remove Nth From End (20) - MUST KNOW
5. Reorder List (26) - IMPORTANT
6. Copy List with Random Pointer (28) - IMPORTANT
7. Sort List (29) - IMPORTANT
8. LRU Cache (39) - MUST KNOW FOR DESIGN
9. Merge k Sorted Lists (44) - VERY COMMON
10. Reverse Nodes in k-Group (45) - SHOWS MASTERY

### Time Allocation
- Easy: 10-15 minutes
- Medium: 20-30 minutes
- Hard: 35-45 minutes

### Strategy
1. Draw diagrams - visualize pointer movements
2. Handle edge cases - empty list, single node, two nodes
3. Test with examples - walk through your code
4. Discuss trade-offs - time vs space complexity

---

**Total Practice Time:** 35-50 hours  
**Recommended Pace:** 5-7 problems per week  
**Mastery Timeline:** 8-10 weeks

Remember: Linked list problems are about careful pointer manipulation. Draw diagrams!

