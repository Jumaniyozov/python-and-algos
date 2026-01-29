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
