# Linked Lists: Code Examples

## Example 1: Singly Linked List Class Implementation

```python
class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Complete implementation of a singly linked list."""
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        """Add element to end of list. O(n) time."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, data):
        """Add element to beginning of list. O(1) time."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert(self, index, data):
        """Insert element at given index. O(n) time."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def delete(self, data):
        """Delete first occurrence of data. O(n) time."""
        if not self.head:
            raise ValueError("List is empty")

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if not current.next:
            raise ValueError(f"Data {data} not found")

        current.next = current.next.next
        self.size -= 1

    def find(self, data):
        """Find first node with given data. O(n) time."""
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def __len__(self):
        """Return size of list. O(1) time."""
        return self.size

    def __str__(self):
        """String representation. O(n) time."""
        if not self.head:
            return "[]"

        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)

# Test cases
if __name__ == "__main__":
    # Create linked list
    ll = SinglyLinkedList()

    # Test append
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(f"After appends: {ll}")  # 1 -> 2 -> 3

    # Test prepend
    ll.prepend(0)
    print(f"After prepend: {ll}")  # 0 -> 1 -> 2 -> 3

    # Test insert
    ll.insert(2, 1.5)
    print(f"After insert at index 2: {ll}")  # 0 -> 1 -> 1.5 -> 2 -> 3

    # Test delete
    ll.delete(1.5)
    print(f"After delete 1.5: {ll}")  # 0 -> 1 -> 2 -> 3

    # Test find
    print(f"Index of 2: {ll.find(2)}")  # 2
    print(f"Index of 5: {ll.find(5)}")  # -1

    # Test length
    print(f"Length: {len(ll)}")  # 4
```

**Output:**
```
After appends: 1 -> 2 -> 3
After prepend: 0 -> 1 -> 2 -> 3
After insert at index 2: 0 -> 1 -> 1.5 -> 2 -> 3
After delete 1.5: 0 -> 1 -> 2 -> 3
Index of 2: 2
Index of 5: -1
Length: 4
```

**Complexity Analysis:**
- append(): O(n) time, O(1) space
- prepend(): O(1) time, O(1) space
- insert(): O(n) time, O(1) space
- delete(): O(n) time, O(1) space
- find(): O(n) time, O(1) space

---

## Example 2: Reverse Linked List (Iterative)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list_iterative(head):
    """
    Reverse a singly linked list iteratively.

    Time: O(n) - visit each node once
    Space: O(1) - only use three pointers
    """
    prev = None
    current = head

    while current:
        # Save next node
        next_temp = current.next

        # Reverse the link
        current.next = prev

        # Move pointers forward
        prev = current
        current = next_temp

    return prev

# Helper function to create list from array
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert list to array
def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
print("Test 1: Normal list")
head = create_list([1, 2, 3, 4, 5])
reversed_head = reverse_list_iterative(head)
print(f"Input:  [1, 2, 3, 4, 5]")
print(f"Output: {list_to_array(reversed_head)}")  # [5, 4, 3, 2, 1]

print("\nTest 2: Single element")
head = create_list([1])
reversed_head = reverse_list_iterative(head)
print(f"Input:  [1]")
print(f"Output: {list_to_array(reversed_head)}")  # [1]

print("\nTest 3: Empty list")
head = create_list([])
reversed_head = reverse_list_iterative(head)
print(f"Input:  []")
print(f"Output: {list_to_array(reversed_head)}")  # []

print("\nTest 4: Two elements")
head = create_list([1, 2])
reversed_head = reverse_list_iterative(head)
print(f"Input:  [1, 2]")
print(f"Output: {list_to_array(reversed_head)}")  # [2, 1]
```

**Visual Explanation:**
```
Initial:    1 -> 2 -> 3 -> 4 -> 5 -> None
Step 1:     None <- 1    2 -> 3 -> 4 -> 5 -> None
Step 2:     None <- 1 <- 2    3 -> 4 -> 5 -> None
Step 3:     None <- 1 <- 2 <- 3    4 -> 5 -> None
Step 4:     None <- 1 <- 2 <- 3 <- 4    5 -> None
Step 5:     None <- 1 <- 2 <- 3 <- 4 <- 5
```

**Output:**
```
Test 1: Normal list
Input:  [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Test 2: Single element
Input:  [1]
Output: [1]

Test 3: Empty list
Input:  []
Output: []

Test 4: Two elements
Input:  [1, 2]
Output: [2, 1]
```

---

## Example 3: Reverse Linked List (Recursive)

```python
def reverse_list_recursive(head):
    """
    Reverse a singly linked list recursively.

    Time: O(n) - visit each node once
    Space: O(n) - recursion stack
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head

    # Recursively reverse the rest of the list
    new_head = reverse_list_recursive(head.next)

    # Reverse the link between current and next
    head.next.next = head
    head.next = None

    return new_head

# Test cases
print("Test 1: Normal list")
head = create_list([1, 2, 3, 4, 5])
reversed_head = reverse_list_recursive(head)
print(f"Input:  [1, 2, 3, 4, 5]")
print(f"Output: {list_to_array(reversed_head)}")  # [5, 4, 3, 2, 1]

print("\nTest 2: Single element")
head = create_list([42])
reversed_head = reverse_list_recursive(head)
print(f"Input:  [42]")
print(f"Output: {list_to_array(reversed_head)}")  # [42]

print("\nTest 3: Two elements")
head = create_list([10, 20])
reversed_head = reverse_list_recursive(head)
print(f"Input:  [10, 20]")
print(f"Output: {list_to_array(reversed_head)}")  # [20, 10]
```

**Recursive Call Stack Visualization:**
```
reverse(1->2->3->4->5)
  reverse(2->3->4->5)
    reverse(3->4->5)
      reverse(4->5)
        reverse(5)  <- base case, return 5
        4.next.next = 4, 4.next = None  <- 5->4->None
      3.next.next = 3, 3.next = None    <- 5->4->3->None
    2.next.next = 2, 2.next = None      <- 5->4->3->2->None
  1.next.next = 1, 1.next = None        <- 5->4->3->2->1->None
return 5
```

**Output:**
```
Test 1: Normal list
Input:  [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Test 2: Single element
Input:  [42]
Output: [42]

Test 3: Two elements
Input:  [10, 20]
Output: [20, 10]
```

---

## Example 4: Detect Cycle (Floyd's Tortoise and Hare)

```python
def has_cycle(head):
    """
    Detect if linked list has a cycle using Floyd's algorithm.

    Time: O(n) - fast pointer visits at most 2n nodes
    Space: O(1) - only two pointers
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

# Test cases
print("Test 1: List with cycle")
# Create: 1 -> 2 -> 3 -> 4 -> 5
#              ^              |
#              |______________|
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # Create cycle
print(f"Has cycle: {has_cycle(head)}")  # True

print("\nTest 2: List without cycle")
head = create_list([1, 2, 3, 4, 5])
print(f"Has cycle: {has_cycle(head)}")  # False

print("\nTest 3: Single node with self cycle")
head = ListNode(1)
head.next = head
print(f"Has cycle: {has_cycle(head)}")  # True

print("\nTest 4: Empty list")
print(f"Has cycle: {has_cycle(None)}")  # False

print("\nTest 5: Single node without cycle")
head = ListNode(1)
print(f"Has cycle: {has_cycle(head)}")  # False
```

**Visual Explanation:**
```
List with cycle:
1 -> 2 -> 3 -> 4 -> 5
     ^              |
     |______________|

Step 1: slow=1, fast=1
Step 2: slow=2, fast=3
Step 3: slow=3, fast=5
Step 4: slow=4, fast=3
Step 5: slow=5, fast=5  <- They meet! Cycle detected
```

**Output:**
```
Test 1: List with cycle
Has cycle: True

Test 2: List without cycle
Has cycle: False

Test 3: Single node with self cycle
Has cycle: True

Test 4: Empty list
Has cycle: False

Test 5: Single node without cycle
Has cycle: False
```

---

## Example 5: Find Cycle Starting Point

```python
def detect_cycle(head):
    """
    Find the node where cycle begins.

    Time: O(n)
    Space: O(1)

    Algorithm:
    1. Use Floyd's algorithm to detect if cycle exists
    2. If cycle found, reset one pointer to head
    3. Move both pointers one step at a time
    4. They will meet at the cycle start
    """
    if not head or not head.next:
        return None

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

# Test cases
print("Test 1: Cycle at position 1")
# 1 -> 2 -> 3 -> 4 -> 5
#      ^              |
#      |______________|
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2
result = detect_cycle(head)
print(f"Cycle starts at node with value: {result.val}")  # 2

print("\nTest 2: Cycle at position 0")
# 1 -> 2 -> 3
# ^         |
# |_________|
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
head.next = node2
node2.next = node3
node3.next = head
result = detect_cycle(head)
print(f"Cycle starts at node with value: {result.val}")  # 1

print("\nTest 3: No cycle")
head = create_list([1, 2, 3, 4, 5])
result = detect_cycle(head)
print(f"Cycle starts at: {result}")  # None

print("\nTest 4: Self loop")
head = ListNode(1)
head.next = head
result = detect_cycle(head)
print(f"Cycle starts at node with value: {result.val}")  # 1
```

**Mathematical Proof:**
```
Let's say:
- Distance from head to cycle start = a
- Distance from cycle start to meeting point = b
- Cycle length = c

When slow and fast meet:
- Slow traveled: a + b
- Fast traveled: a + b + nc (n is number of complete cycles)

Since fast is 2x slower: 2(a + b) = a + b + nc
Simplifying: a + b = nc
Therefore: a = nc - b

This means if we start from head and meeting point,
moving one step at a time, they meet at cycle start!
```

**Output:**
```
Test 1: Cycle at position 1
Cycle starts at node with value: 2

Test 2: Cycle at position 0
Cycle starts at node with value: 1

Test 3: No cycle
Cycle starts at: None

Test 4: Self loop
Cycle starts at node with value: 1
```

---

## Example 6: Find Middle Element (Fast/Slow Pointers)

```python
def find_middle(head):
    """
    Find middle node of linked list.
    If two middle nodes, return second one.

    Time: O(n) - traverse list once
    Space: O(1) - only two pointers
    """
    if not head:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def find_middle_first(head):
    """
    Find middle node of linked list.
    If two middle nodes, return first one.

    Time: O(n)
    Space: O(1)
    """
    if not head:
        return None

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Test cases
print("Test 1: Odd length list")
head = create_list([1, 2, 3, 4, 5])
middle = find_middle(head)
print(f"List: [1, 2, 3, 4, 5]")
print(f"Middle (second): {middle.val}")  # 3

print("\nTest 2: Even length list")
head = create_list([1, 2, 3, 4, 5, 6])
middle = find_middle(head)
print(f"List: [1, 2, 3, 4, 5, 6]")
print(f"Middle (second): {middle.val}")  # 4

middle_first = find_middle_first(head)
print(f"Middle (first): {middle_first.val}")  # 3

print("\nTest 3: Single element")
head = create_list([1])
middle = find_middle(head)
print(f"List: [1]")
print(f"Middle: {middle.val}")  # 1

print("\nTest 4: Two elements")
head = create_list([1, 2])
middle = find_middle(head)
print(f"List: [1, 2]")
print(f"Middle: {middle.val}")  # 2

print("\nTest 5: Three elements")
head = create_list([1, 2, 3])
middle = find_middle(head)
print(f"List: [1, 2, 3]")
print(f"Middle: {middle.val}")  # 2
```

**Visual Explanation:**
```
List: 1 -> 2 -> 3 -> 4 -> 5

Step 0: slow=1, fast=1
Step 1: slow=2, fast=3
Step 2: slow=3, fast=5
Step 3: slow=3, fast=None (stop)

Middle is at slow pointer: 3

List: 1 -> 2 -> 3 -> 4 -> 5 -> 6

Step 0: slow=1, fast=1
Step 1: slow=2, fast=3
Step 2: slow=3, fast=5
Step 3: slow=4, fast=None (stop)

Middle is at slow pointer: 4
```

**Output:**
```
Test 1: Odd length list
List: [1, 2, 3, 4, 5]
Middle (second): 3

Test 2: Even length list
List: [1, 2, 3, 4, 5, 6]
Middle (second): 4
Middle (first): 3

Test 3: Single element
List: [1]
Middle: 1

Test 4: Two elements
List: [1, 2]
Middle: 2

Test 5: Three elements
List: [1, 2, 3]
Middle: 2
```

---

## Example 7: Merge Two Sorted Lists

```python
def merge_two_lists(l1, l2):
    """
    Merge two sorted linked lists.

    Time: O(n + m) where n, m are lengths
    Space: O(1) - only pointers, no extra space
    """
    # Create dummy head
    dummy = ListNode(0)
    current = dummy

    # Merge while both lists have nodes
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach remaining nodes
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next

def merge_two_lists_recursive(l1, l2):
    """
    Merge two sorted lists recursively.

    Time: O(n + m)
    Space: O(n + m) - recursion stack
    """
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val <= l2.val:
        l1.next = merge_two_lists_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists_recursive(l1, l2.next)
        return l2

# Test cases
print("Test 1: Both lists non-empty")
l1 = create_list([1, 3, 5, 7])
l2 = create_list([2, 4, 6, 8])
merged = merge_two_lists(l1, l2)
print(f"List 1: [1, 3, 5, 7]")
print(f"List 2: [2, 4, 6, 8]")
print(f"Merged: {list_to_array(merged)}")  # [1, 2, 3, 4, 5, 6, 7, 8]

print("\nTest 2: Different lengths")
l1 = create_list([1, 2, 4])
l2 = create_list([1, 3, 4, 5, 6])
merged = merge_two_lists(l1, l2)
print(f"List 1: [1, 2, 4]")
print(f"List 2: [1, 3, 4, 5, 6]")
print(f"Merged: {list_to_array(merged)}")  # [1, 1, 2, 3, 4, 4, 5, 6]

print("\nTest 3: One empty list")
l1 = create_list([])
l2 = create_list([0, 1, 2])
merged = merge_two_lists(l1, l2)
print(f"List 1: []")
print(f"List 2: [0, 1, 2]")
print(f"Merged: {list_to_array(merged)}")  # [0, 1, 2]

print("\nTest 4: Both empty")
l1 = create_list([])
l2 = create_list([])
merged = merge_two_lists(l1, l2)
print(f"List 1: []")
print(f"List 2: []")
print(f"Merged: {list_to_array(merged)}")  # []

print("\nTest 5: Recursive approach")
l1 = create_list([1, 2, 4])
l2 = create_list([1, 3, 4])
merged = merge_two_lists_recursive(l1, l2)
print(f"List 1: [1, 2, 4]")
print(f"List 2: [1, 3, 4]")
print(f"Merged (recursive): {list_to_array(merged)}")  # [1, 1, 2, 3, 4, 4]
```

**Visual Explanation:**
```
l1: 1 -> 3 -> 5
l2: 2 -> 4 -> 6

Step 1: dummy -> 1 (from l1)
        l1: 3 -> 5
        l2: 2 -> 4 -> 6

Step 2: dummy -> 1 -> 2 (from l2)
        l1: 3 -> 5
        l2: 4 -> 6

Step 3: dummy -> 1 -> 2 -> 3 (from l1)
        l1: 5
        l2: 4 -> 6

Step 4: dummy -> 1 -> 2 -> 3 -> 4 (from l2)
        l1: 5
        l2: 6

Step 5: dummy -> 1 -> 2 -> 3 -> 4 -> 5 (from l1)
        l1: empty
        l2: 6

Step 6: dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 (attach remaining)
```

**Output:**
```
Test 1: Both lists non-empty
List 1: [1, 3, 5, 7]
List 2: [2, 4, 6, 8]
Merged: [1, 2, 3, 4, 5, 6, 7, 8]

Test 2: Different lengths
List 1: [1, 2, 4]
List 2: [1, 3, 4, 5, 6]
Merged: [1, 1, 2, 3, 4, 4, 5, 6]

Test 3: One empty list
List 1: []
List 2: [0, 1, 2]
Merged: [0, 1, 2]

Test 4: Both empty
List 1: []
List 2: []
Merged: []

Test 5: Recursive approach
List 1: [1, 2, 4]
List 2: [1, 3, 4]
Merged (recursive): [1, 1, 2, 3, 4, 4]
```

---

## Example 8: Remove Nth Node From End

```python
def remove_nth_from_end(head, n):
    """
    Remove nth node from end of list.

    Time: O(L) where L is length of list
    Space: O(1)

    Approach: Use two pointers with n gap between them
    """
    dummy = ListNode(0)
    dummy.next = head

    # Create gap of n between fast and slow
    fast = dummy
    slow = dummy

    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        if not fast:
            return head
        fast = fast.next

    # Move both until fast reaches end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove the nth node
    slow.next = slow.next.next

    return dummy.next

# Test cases
print("Test 1: Remove 2nd from end")
head = create_list([1, 2, 3, 4, 5])
result = remove_nth_from_end(head, 2)
print(f"Input:  [1, 2, 3, 4, 5], n=2")
print(f"Output: {list_to_array(result)}")  # [1, 2, 3, 5]

print("\nTest 2: Remove last node")
head = create_list([1, 2, 3, 4, 5])
result = remove_nth_from_end(head, 1)
print(f"Input:  [1, 2, 3, 4, 5], n=1")
print(f"Output: {list_to_array(result)}")  # [1, 2, 3, 4]

print("\nTest 3: Remove first node (from end)")
head = create_list([1, 2, 3, 4, 5])
result = remove_nth_from_end(head, 5)
print(f"Input:  [1, 2, 3, 4, 5], n=5")
print(f"Output: {list_to_array(result)}")  # [2, 3, 4, 5]

print("\nTest 4: Single node")
head = create_list([1])
result = remove_nth_from_end(head, 1)
print(f"Input:  [1], n=1")
print(f"Output: {list_to_array(result)}")  # []

print("\nTest 5: Two nodes, remove first")
head = create_list([1, 2])
result = remove_nth_from_end(head, 2)
print(f"Input:  [1, 2], n=2")
print(f"Output: {list_to_array(result)}")  # [2]
```

**Visual Explanation:**
```
Remove 2nd from end: [1, 2, 3, 4, 5], n=2

Step 1: Create gap of n+1=3
dummy -> 1 -> 2 -> 3 -> 4 -> 5
slow
              fast

Step 2: Move both until fast reaches end
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
                  slow          fast

Step 3: Remove node after slow
dummy -> 1 -> 2 -> 3 -> 5
                  slow

Result: [1, 2, 3, 5]
```

**Output:**
```
Test 1: Remove 2nd from end
Input:  [1, 2, 3, 4, 5], n=2
Output: [1, 2, 3, 5]

Test 2: Remove last node
Input:  [1, 2, 3, 4, 5], n=1
Output: [1, 2, 3, 4]

Test 3: Remove first node (from end)
Input:  [1, 2, 3, 4, 5], n=5
Output: [2, 3, 4, 5]

Test 4: Single node
Input:  [1], n=1
Output: []

Test 5: Two nodes, remove first
Input:  [1, 2], n=2
Output: [2]
```

---

## Example 9: Palindrome Linked List

```python
def is_palindrome(head):
    """
    Check if linked list is palindrome.

    Time: O(n)
    Space: O(1)

    Approach:
    1. Find middle using slow/fast pointers
    2. Reverse second half
    3. Compare first and second half
    4. Restore list (optional)
    """
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    current = slow
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    # Compare halves
    left = head
    right = prev
    result = True

    while right:  # right is shorter or equal
        if left.val != right.val:
            result = False
            break
        left = left.next
        right = right.next

    return result

def is_palindrome_with_restore(head):
    """
    Check palindrome and restore original list.

    Time: O(n)
    Space: O(1)
    """
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second_half = reverse_list_iterative(slow)

    # Compare
    first = head
    second = second_half
    is_palin = True

    while second:
        if first.val != second.val:
            is_palin = False
            break
        first = first.next
        second = second.next

    # Restore list
    slow.next = reverse_list_iterative(second_half)

    return is_palin

# Test cases
print("Test 1: Palindrome - odd length")
head = create_list([1, 2, 3, 2, 1])
print(f"List: [1, 2, 3, 2, 1]")
print(f"Is palindrome: {is_palindrome(head)}")  # True

print("\nTest 2: Palindrome - even length")
head = create_list([1, 2, 2, 1])
print(f"List: [1, 2, 2, 1]")
print(f"Is palindrome: {is_palindrome(head)}")  # True

print("\nTest 3: Not palindrome")
head = create_list([1, 2, 3, 4, 5])
print(f"List: [1, 2, 3, 4, 5]")
print(f"Is palindrome: {is_palindrome(head)}")  # False

print("\nTest 4: Single element")
head = create_list([1])
print(f"List: [1]")
print(f"Is palindrome: {is_palindrome(head)}")  # True

print("\nTest 5: Two same elements")
head = create_list([1, 1])
print(f"List: [1, 1]")
print(f"Is palindrome: {is_palindrome(head)}")  # True

print("\nTest 6: Two different elements")
head = create_list([1, 2])
print(f"List: [1, 2]")
print(f"Is palindrome: {is_palindrome(head)}")  # False

print("\nTest 7: With restore")
head = create_list([1, 2, 3, 2, 1])
result = is_palindrome_with_restore(head)
print(f"List: [1, 2, 3, 2, 1]")
print(f"Is palindrome: {result}")  # True
print(f"List after check: {list_to_array(head)}")  # [1, 2, 3, 2, 1]
```

**Visual Explanation:**
```
Check [1, 2, 3, 2, 1]:

Step 1: Find middle
1 -> 2 -> 3 -> 2 -> 1
          slow

Step 2: Reverse second half
1 -> 2 -> 3    1 -> 2
               ^    |
               |____|

Step 3: Compare
1 -> 2 -> 3    1 -> 2
^              ^
Match: 1 == 1

1 -> 2 -> 3    1 -> 2
     ^              ^
Match: 2 == 2

Result: Palindrome!
```

**Output:**
```
Test 1: Palindrome - odd length
List: [1, 2, 3, 2, 1]
Is palindrome: True

Test 2: Palindrome - even length
List: [1, 2, 2, 1]
Is palindrome: True

Test 3: Not palindrome
List: [1, 2, 3, 4, 5]
Is palindrome: False

Test 4: Single element
List: [1]
Is palindrome: True

Test 5: Two same elements
List: [1, 1]
Is palindrome: True

Test 6: Two different elements
List: [1, 2]
Is palindrome: False

Test 7: With restore
List: [1, 2, 3, 2, 1]
Is palindrome: True
List after check: [1, 2, 3, 2, 1]
```

---

## Example 10: Remove Duplicates from Sorted List

```python
def delete_duplicates(head):
    """
    Remove duplicates from sorted linked list.
    Keep one occurrence of each value.

    Time: O(n)
    Space: O(1)
    """
    if not head:
        return head

    current = head
    while current and current.next:
        if current.val == current.next.val:
            # Skip duplicate
            current.next = current.next.next
        else:
            # Move to next
            current = current.next

    return head

def delete_all_duplicates(head):
    """
    Remove all nodes that have duplicates.
    Don't keep any occurrence.

    Time: O(n)
    Space: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head

    while current:
        # Check if current is start of duplicates
        if current.next and current.val == current.next.val:
            # Skip all nodes with this value
            while current.next and current.val == current.next.val:
                current = current.next
            prev.next = current.next
        else:
            prev = current
        current = current.next

    return dummy.next

# Test cases
print("Test 1: Remove duplicates (keep one)")
head = create_list([1, 1, 2, 3, 3, 3, 4])
result = delete_duplicates(head)
print(f"Input:  [1, 1, 2, 3, 3, 3, 4]")
print(f"Output: {list_to_array(result)}")  # [1, 2, 3, 4]

print("\nTest 2: No duplicates")
head = create_list([1, 2, 3, 4, 5])
result = delete_duplicates(head)
print(f"Input:  [1, 2, 3, 4, 5]")
print(f"Output: {list_to_array(result)}")  # [1, 2, 3, 4, 5]

print("\nTest 3: All duplicates")
head = create_list([1, 1, 1, 1, 1])
result = delete_duplicates(head)
print(f"Input:  [1, 1, 1, 1, 1]")
print(f"Output: {list_to_array(result)}")  # [1]

print("\nTest 4: Remove ALL duplicates (keep none)")
head = create_list([1, 2, 3, 3, 4, 4, 5])
result = delete_all_duplicates(head)
print(f"Input:  [1, 2, 3, 3, 4, 4, 5]")
print(f"Output: {list_to_array(result)}")  # [1, 2, 5]

print("\nTest 5: Remove ALL duplicates - all removed")
head = create_list([1, 1, 2, 2, 3, 3])
result = delete_all_duplicates(head)
print(f"Input:  [1, 1, 2, 2, 3, 3]")
print(f"Output: {list_to_array(result)}")  # []
```

**Visual Explanation:**
```
Remove duplicates (keep one): [1, 1, 2, 3, 3, 3]

Initial: 1 -> 1 -> 2 -> 3 -> 3 -> 3
         ^
         current

Step 1: 1 == 1, skip
1 -> 2 -> 3 -> 3 -> 3
^
current

Step 2: 1 != 2, move
1 -> 2 -> 3 -> 3 -> 3
     ^
     current

Step 3: 2 != 3, move
1 -> 2 -> 3 -> 3 -> 3
          ^
          current

Step 4: 3 == 3, skip
1 -> 2 -> 3 -> 3
          ^
          current

Step 5: 3 == 3, skip
1 -> 2 -> 3
          ^
          current

Result: [1, 2, 3]
```

**Output:**
```
Test 1: Remove duplicates (keep one)
Input:  [1, 1, 2, 3, 3, 3, 4]
Output: [1, 2, 3, 4]

Test 2: No duplicates
Input:  [1, 2, 3, 4, 5]
Output: [1, 2, 3, 4, 5]

Test 3: All duplicates
Input:  [1, 1, 1, 1, 1]
Output: [1]

Test 4: Remove ALL duplicates (keep none)
Input:  [1, 2, 3, 3, 4, 4, 5]
Output: [1, 2, 5]

Test 5: Remove ALL duplicates - all removed
Input:  [1, 1, 2, 2, 3, 3]
Output: []
```

---

## Example 11: Intersection of Two Linked Lists

```python
def get_intersection_node(headA, headB):
    """
    Find node where two linked lists intersect.

    Time: O(m + n) where m, n are lengths
    Space: O(1)

    Approach: Two pointers, switch heads when reaching end
    """
    if not headA or not headB:
        return None

    pA = headA
    pB = headB

    # When they meet, it's either at intersection or None
    while pA != pB:
        # Switch to other list's head when reaching end
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA

def get_intersection_node_length(headA, headB):
    """
    Find intersection using length difference approach.

    Time: O(m + n)
    Space: O(1)
    """
    # Get lengths
    lenA = lenB = 0
    currA, currB = headA, headB

    while currA:
        lenA += 1
        currA = currA.next

    while currB:
        lenB += 1
        currB = currB.next

    # Align starting points
    currA, currB = headA, headB

    if lenA > lenB:
        for _ in range(lenA - lenB):
            currA = currA.next
    else:
        for _ in range(lenB - lenA):
            currB = currB.next

    # Find intersection
    while currA != currB:
        currA = currA.next
        currB = currB.next

    return currA

# Test cases
print("Test 1: Lists intersect")
# Create intersection
# A: 1 -> 2 -> 3
#              |
#              v
#              6 -> 7 -> 8
#              ^
#              |
# B: 4 -> 5 ->

# Common part
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node6.next = node7
node7.next = node8

# List A
headA = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
headA.next = node2
node2.next = node3
node3.next = node6

# List B
headB = ListNode(4)
node5 = ListNode(5)
headB.next = node5
node5.next = node6

intersection = get_intersection_node(headA, headB)
print(f"Lists intersect at node with value: {intersection.val}")  # 6

print("\nTest 2: No intersection")
headA = create_list([1, 2, 3])
headB = create_list([4, 5, 6])
intersection = get_intersection_node(headA, headB)
print(f"Intersection: {intersection}")  # None

print("\nTest 3: One list is suffix of another")
# A: 1 -> 2
# B: 1 -> 2 -> 3
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

headA = node2
headB = node1

intersection = get_intersection_node(headA, headB)
print(f"Intersection at node with value: {intersection.val}")  # 2

print("\nTest 4: Using length approach")
# Same as Test 1 setup
intersection = get_intersection_node_length(headA, headB)
print(f"Intersection (length method) at: {intersection.val}")  # 2
```

**Visual Explanation:**
```
Two pointer approach:

List A: 1 -> 2 -> 3 -> 6 -> 7 -> 8
List B: 4 -> 5 -> 6 -> 7 -> 8
                  ^
                  Intersection

Length A = 6, Length B = 5

Iteration 1-5: pA and pB traverse their lists
When pA reaches end, switch to headB
When pB reaches end, switch to headA

After switching:
pA travels: 6 (list A) + 5 (list B) = 11 steps
pB travels: 5 (list B) + 6 (list A) = 11 steps

They meet at intersection after same number of steps!
```

**Output:**
```
Test 1: Lists intersect
Lists intersect at node with value: 6

Test 2: No intersection
Intersection: None

Test 3: One list is suffix of another
Intersection at node with value: 2

Test 4: Using length approach
Intersection (length method) at: 2
```

---

## Example 12: Add Two Numbers (Linked List Representation)

```python
def add_two_numbers(l1, l2):
    """
    Add two numbers represented as linked lists.
    Digits stored in reverse order.

    Time: O(max(m, n))
    Space: O(max(m, n)) for result list

    Example: 342 + 465 = 807
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        # Get values
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        # Create new node
        current.next = ListNode(digit)
        current = current.next

        # Move pointers
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

def add_two_numbers_forward(l1, l2):
    """
    Add two numbers when digits stored in forward order.

    Time: O(max(m, n))
    Space: O(max(m, n))

    Approach: Reverse lists, add, reverse result
    """
    # Reverse both lists
    l1 = reverse_list_iterative(l1)
    l2 = reverse_list_iterative(l2)

    # Add reversed lists
    result = add_two_numbers(l1, l2)

    # Reverse result
    return reverse_list_iterative(result)

# Test cases
print("Test 1: Basic addition")
l1 = create_list([2, 4, 3])  # 342
l2 = create_list([5, 6, 4])  # 465
result = add_two_numbers(l1, l2)
print(f"342 + 465 = {list_to_array(result)}")  # [7, 0, 8] = 807

print("\nTest 2: Different lengths")
l1 = create_list([9, 9])  # 99
l2 = create_list([1])     # 1
result = add_two_numbers(l1, l2)
print(f"99 + 1 = {list_to_array(result)}")  # [0, 0, 1] = 100

print("\nTest 3: With carry propagation")
l1 = create_list([9, 9, 9])  # 999
l2 = create_list([1])         # 1
result = add_two_numbers(l1, l2)
print(f"999 + 1 = {list_to_array(result)}")  # [0, 0, 0, 1] = 1000

print("\nTest 4: Zero")
l1 = create_list([0])
l2 = create_list([0])
result = add_two_numbers(l1, l2)
print(f"0 + 0 = {list_to_array(result)}")  # [0]

print("\nTest 5: Large numbers")
l1 = create_list([9, 9, 9, 9, 9, 9, 9])  # 9999999
l2 = create_list([9, 9, 9, 9])           # 9999
result = add_two_numbers(l1, l2)
print(f"9999999 + 9999 = {list_to_array(result)}")  # [8, 9, 9, 9, 0, 0, 0, 1]

print("\nTest 6: Forward order")
l1 = create_list([3, 4, 2])  # 342 in forward order
l2 = create_list([4, 6, 5])  # 465 in forward order
result = add_two_numbers_forward(l1, l2)
print(f"342 + 465 (forward) = {list_to_array(result)}")  # [8, 0, 7]
```

**Visual Explanation:**
```
Add 342 + 465:

l1: 2 -> 4 -> 3
l2: 5 -> 6 -> 4

Step 1: 2 + 5 = 7, carry = 0
Result: 7

Step 2: 4 + 6 = 10, carry = 1
Result: 7 -> 0

Step 3: 3 + 4 + 1(carry) = 8, carry = 0
Result: 7 -> 0 -> 8

Final: 807
```

**Output:**
```
Test 1: Basic addition
342 + 465 = [7, 0, 8]

Test 2: Different lengths
99 + 1 = [0, 0, 1]

Test 3: With carry propagation
999 + 1 = [0, 0, 0, 1]

Test 4: Zero
0 + 0 = [0]

Test 5: Large numbers
9999999 + 9999 = [8, 9, 9, 9, 0, 0, 0, 1]

Test 6: Forward order
342 + 465 (forward) = [8, 0, 7]
```

---

## Example 13: Copy List with Random Pointer

```python
class NodeWithRandom:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    """
    Deep copy linked list with random pointers.

    Time: O(n)
    Space: O(n) for hash map

    Approach: Use hash map to track old -> new node mapping
    """
    if not head:
        return None

    # Map old nodes to new nodes
    old_to_new = {}

    # First pass: create all nodes
    current = head
    while current:
        old_to_new[current] = NodeWithRandom(current.val)
        current = current.next

    # Second pass: set next and random pointers
    current = head
    while current:
        if current.next:
            old_to_new[current].next = old_to_new[current.next]
        if current.random:
            old_to_new[current].random = old_to_new[current.random]
        current = current.next

    return old_to_new[head]

def copy_random_list_optimized(head):
    """
    Deep copy without extra space (except for output).

    Time: O(n)
    Space: O(1)

    Approach: Interweave old and new nodes
    """
    if not head:
        return None

    # Step 1: Create interweaved list
    # Old: 1 -> 2 -> 3
    # New: 1 -> 1' -> 2 -> 2' -> 3 -> 3'
    current = head
    while current:
        new_node = NodeWithRandom(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    # Step 2: Set random pointers for new nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate lists
    dummy = NodeWithRandom(0)
    copy_prev = dummy
    current = head

    while current:
        # Extract copy
        copy = current.next
        copy_prev.next = copy
        copy_prev = copy

        # Restore original list
        current.next = copy.next
        current = current.next

    return dummy.next

# Test cases
print("Test 1: List with random pointers")
# Create list: 1 -> 2 -> 3
# Random: 1->3, 2->1, 3->2
node1 = NodeWithRandom(1)
node2 = NodeWithRandom(2)
node3 = NodeWithRandom(3)
node1.next = node2
node2.next = node3
node1.random = node3
node2.random = node1
node3.random = node2

copied = copy_random_list(node1)
print(f"Original node 1 val: {node1.val}, random val: {node1.random.val}")
print(f"Copied node 1 val: {copied.val}, random val: {copied.random.val}")
print(f"Are they different objects? {node1 is not copied}")

print("\nTest 2: List with None random pointers")
node1 = NodeWithRandom(1)
node2 = NodeWithRandom(2)
node1.next = node2
node1.random = None
node2.random = None

copied = copy_random_list(node1)
print(f"Copied successfully: {copied.val == 1 and copied.next.val == 2}")

print("\nTest 3: Empty list")
copied = copy_random_list(None)
print(f"Copied empty list: {copied}")

print("\nTest 4: Single node with self random")
node = NodeWithRandom(1)
node.random = node

copied = copy_random_list(node)
print(f"Copied node val: {copied.val}")
print(f"Random points to self: {copied.random is copied}")

print("\nTest 5: Optimized approach")
node1 = NodeWithRandom(1)
node2 = NodeWithRandom(2)
node3 = NodeWithRandom(3)
node1.next = node2
node2.next = node3
node1.random = node3
node2.random = node1
node3.random = node2

copied = copy_random_list_optimized(node1)
print(f"Optimized copy val: {copied.val}, random val: {copied.random.val}")
print(f"Is deep copy: {node1 is not copied}")
```

**Visual Explanation:**
```
Hash Map Approach:

Original:
1 -> 2 -> 3
|    |    |
v    v    v
3    1    2

Pass 1: Create nodes
old_to_new = {1: 1', 2: 2', 3: 3'}

Pass 2: Set pointers
1' -> 2' -> 3'
|     |     |
v     v     v
3'    1'    2'

Optimized Approach (interweaving):

Step 1: Interweave
1 -> 1' -> 2 -> 2' -> 3 -> 3'

Step 2: Set random pointers
1.random = 3, so 1'.random = 3'
2.random = 1, so 2'.random = 1'
3.random = 2, so 3'.random = 2'

Step 3: Separate
Original: 1 -> 2 -> 3
Copy:     1' -> 2' -> 3'
```

**Output:**
```
Test 1: List with random pointers
Original node 1 val: 1, random val: 3
Copied node 1 val: 1, random val: 3
Are they different objects? True

Test 2: List with None random pointers
Copied successfully: True

Test 3: Empty list
Copied empty list: None

Test 4: Single node with self random
Copied node val: 1
Random points to self: True

Test 5: Optimized approach
Optimized copy val: 1, random val: 3
Is deep copy: True
```

---

## Example 14: Flatten Multilevel Doubly Linked List

```python
class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    """
    Flatten multilevel doubly linked list.

    Time: O(n) where n is total number of nodes
    Space: O(d) where d is maximum depth (recursion stack)

    Approach: DFS traversal
    """
    if not head:
        return head

    def flatten_helper(node):
        """Returns tail of flattened list starting at node."""
        current = node
        tail = None

        while current:
            next_node = current.next

            # If child exists, flatten it
            if current.child:
                child_tail = flatten_helper(current.child)

                # Connect current to child
                current.next = current.child
                current.child.prev = current

                # Connect child tail to next
                if next_node:
                    child_tail.next = next_node
                    next_node.prev = child_tail

                # Remove child pointer
                current.child = None

                tail = child_tail
            else:
                tail = current

            current = next_node

        return tail

    flatten_helper(head)
    return head

def flatten_iterative(head):
    """
    Flatten using stack (iterative).

    Time: O(n)
    Space: O(d) for stack
    """
    if not head:
        return head

    stack = []
    current = head

    while current:
        if current.child:
            # Save next for later
            if current.next:
                stack.append(current.next)

            # Connect to child
            current.next = current.child
            current.child.prev = current
            current.child = None

        # If no next and stack not empty, pop from stack
        if not current.next and stack:
            next_node = stack.pop()
            current.next = next_node
            next_node.prev = current

        current = current.next

    return head

# Helper to create multilevel list for testing
def create_multilevel_list():
    """
    Create: 1 - 2 - 3 - 4 - 5 - 6
                |
                7 - 8 - 9 - 10
                    |
                    11 - 12
    """
    # Main level
    n1 = DoublyListNode(1)
    n2 = DoublyListNode(2)
    n3 = DoublyListNode(3)
    n4 = DoublyListNode(4)
    n5 = DoublyListNode(5)
    n6 = DoublyListNode(6)

    n1.next = n2
    n2.prev = n1
    n2.next = n3
    n3.prev = n2
    n3.next = n4
    n4.prev = n3
    n4.next = n5
    n5.prev = n4
    n5.next = n6
    n6.prev = n5

    # Second level
    n7 = DoublyListNode(7)
    n8 = DoublyListNode(8)
    n9 = DoublyListNode(9)
    n10 = DoublyListNode(10)

    n7.next = n8
    n8.prev = n7
    n8.next = n9
    n9.prev = n8
    n9.next = n10
    n10.prev = n9

    # Third level
    n11 = DoublyListNode(11)
    n12 = DoublyListNode(12)

    n11.next = n12
    n12.prev = n11

    # Connect levels
    n3.child = n7
    n8.child = n11

    return n1

def print_flattened(head):
    """Print flattened list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
print("Test 1: Multilevel list")
head = create_multilevel_list()
flattened = flatten(head)
print(f"Flattened: {print_flattened(flattened)}")
# [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]

print("\nTest 2: No child pointers")
n1 = DoublyListNode(1)
n2 = DoublyListNode(2)
n3 = DoublyListNode(3)
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2

flattened = flatten(n1)
print(f"Flattened: {print_flattened(flattened)}")
# [1, 2, 3]

print("\nTest 3: Single node")
head = DoublyListNode(1)
flattened = flatten(head)
print(f"Flattened: {print_flattened(flattened)}")
# [1]

print("\nTest 4: Iterative approach")
head = create_multilevel_list()
flattened = flatten_iterative(head)
print(f"Flattened (iterative): {print_flattened(flattened)}")
# [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]
```

**Visual Explanation:**
```
Original:
1 - 2 - 3 - 4 - 5 - 6
        |
        7 - 8 - 9 - 10
            |
            11 - 12

Flattening process:
1. Start at 1
2. Go to 2
3. Go to 3, see child 7
4. Flatten child: 7 - 8 - 11 - 12 - 9 - 10
5. Insert flattened child after 3
6. Continue with 4, 5, 6

Result:
1 - 2 - 3 - 7 - 8 - 11 - 12 - 9 - 10 - 4 - 5 - 6
```

**Output:**
```
Test 1: Multilevel list
Flattened: [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]

Test 2: No child pointers
Flattened: [1, 2, 3]

Test 3: Single node
Flattened: [1]

Test 4: Iterative approach
Flattened (iterative): [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]
```

---

## Example 15: Sort Linked List (Merge Sort)

```python
def sort_list(head):
    """
    Sort linked list using merge sort.

    Time: O(n log n)
    Space: O(log n) for recursion stack
    """
    if not head or not head.next:
        return head

    # Find middle
    slow = fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Split list
    prev.next = None

    # Recursively sort both halves
    left = sort_list(head)
    right = sort_list(slow)

    # Merge sorted halves
    return merge_two_lists(left, right)

def sort_list_bottom_up(head):
    """
    Sort using bottom-up merge sort (iterative).

    Time: O(n log n)
    Space: O(1) - no recursion
    """
    if not head or not head.next:
        return head

    # Get length
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    dummy = ListNode(0)
    dummy.next = head

    step = 1
    while step < length:
        curr = dummy.next
        tail = dummy

        while curr:
            left = curr
            right = split(left, step)
            curr = split(right, step)
            tail = merge(left, right, tail)

        step *= 2

    return dummy.next

def split(head, n):
    """Split first n nodes and return rest."""
    while n > 1 and head:
        head = head.next
        n -= 1

    if not head:
        return None

    rest = head.next
    head.next = None
    return rest

def merge(l1, l2, tail):
    """Merge two lists after tail, return new tail."""
    current = tail

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2

    while current.next:
        current = current.next

    return current

# Test cases
print("Test 1: Unsorted list")
head = create_list([4, 2, 1, 3])
sorted_head = sort_list(head)
print(f"Input:  [4, 2, 1, 3]")
print(f"Sorted: {list_to_array(sorted_head)}")  # [1, 2, 3, 4]

print("\nTest 2: Already sorted")
head = create_list([1, 2, 3, 4, 5])
sorted_head = sort_list(head)
print(f"Input:  [1, 2, 3, 4, 5]")
print(f"Sorted: {list_to_array(sorted_head)}")  # [1, 2, 3, 4, 5]

print("\nTest 3: Reverse sorted")
head = create_list([5, 4, 3, 2, 1])
sorted_head = sort_list(head)
print(f"Input:  [5, 4, 3, 2, 1]")
print(f"Sorted: {list_to_array(sorted_head)}")  # [1, 2, 3, 4, 5]

print("\nTest 4: Duplicates")
head = create_list([3, 1, 4, 1, 5, 9, 2, 6])
sorted_head = sort_list(head)
print(f"Input:  [3, 1, 4, 1, 5, 9, 2, 6]")
print(f"Sorted: {list_to_array(sorted_head)}")  # [1, 1, 2, 3, 4, 5, 6, 9]

print("\nTest 5: Single element")
head = create_list([1])
sorted_head = sort_list(head)
print(f"Input:  [1]")
print(f"Sorted: {list_to_array(sorted_head)}")  # [1]

print("\nTest 6: Negative numbers")
head = create_list([-1, 5, -3, 4, 0])
sorted_head = sort_list(head)
print(f"Input:  [-1, 5, -3, 4, 0]")
print(f"Sorted: {list_to_array(sorted_head)}")  # [-3, -1, 0, 4, 5]

print("\nTest 7: Bottom-up approach")
head = create_list([4, 2, 1, 3])
sorted_head = sort_list_bottom_up(head)
print(f"Input:  [4, 2, 1, 3]")
print(f"Sorted (bottom-up): {list_to_array(sorted_head)}")  # [1, 2, 3, 4]
```

**Visual Explanation:**
```
Merge Sort: [4, 2, 1, 3]

Split phase:
         [4, 2, 1, 3]
        /            \
    [4, 2]          [1, 3]
    /    \          /    \
  [4]    [2]      [1]    [3]

Merge phase:
  [4]    [2]      [1]    [3]
    \    /          \    /
    [2, 4]          [1, 3]
        \            /
         [1, 2, 3, 4]

Time: O(n log n) - log n levels, O(n) work per level
Space: O(log n) - recursion depth
```

**Output:**
```
Test 1: Unsorted list
Input:  [4, 2, 1, 3]
Sorted: [1, 2, 3, 4]

Test 2: Already sorted
Input:  [1, 2, 3, 4, 5]
Sorted: [1, 2, 3, 4, 5]

Test 3: Reverse sorted
Input:  [5, 4, 3, 2, 1]
Sorted: [1, 2, 3, 4, 5]

Test 4: Duplicates
Input:  [3, 1, 4, 1, 5, 9, 2, 6]
Sorted: [1, 1, 2, 3, 4, 5, 6, 9]

Test 5: Single element
Input:  [1]
Sorted: [1]

Test 6: Negative numbers
Input:  [-1, 5, -3, 4, 0]
Sorted: [-3, -1, 0, 4, 5]

Test 7: Bottom-up approach
Input:  [4, 2, 1, 3]
Sorted (bottom-up): [1, 2, 3, 4]
```

---

## Example 16: Rotate List

```python
def rotate_right(head, k):
    """
    Rotate list to the right by k places.

    Time: O(n)
    Space: O(1)

    Example: [1,2,3,4,5], k=2 -> [4,5,1,2,3]
    """
    if not head or not head.next or k == 0:
        return head

    # Get length and connect tail to head
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Normalize k
    k = k % length
    if k == 0:
        return head

    # Find new tail (at position length - k - 1)
    steps_to_new_tail = length - k - 1
    new_tail = head
    for _ in range(steps_to_new_tail):
        new_tail = new_tail.next

    # Break and reconnect
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head

    return new_head

def rotate_left(head, k):
    """
    Rotate list to the left by k places.

    Time: O(n)
    Space: O(1)
    """
    if not head or not head.next or k == 0:
        return head

    # Get length
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Normalize k
    k = k % length
    if k == 0:
        return head

    # Find new tail (at position k - 1)
    new_tail = head
    for _ in range(k - 1):
        new_tail = new_tail.next

    # Reconnect
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head

    return new_head

# Test cases
print("Test 1: Rotate right by 2")
head = create_list([1, 2, 3, 4, 5])
rotated = rotate_right(head, 2)
print(f"Input:  [1, 2, 3, 4, 5], k=2")
print(f"Output: {list_to_array(rotated)}")  # [4, 5, 1, 2, 3]

print("\nTest 2: Rotate by length (no change)")
head = create_list([1, 2, 3])
rotated = rotate_right(head, 3)
print(f"Input:  [1, 2, 3], k=3")
print(f"Output: {list_to_array(rotated)}")  # [1, 2, 3]

print("\nTest 3: Rotate by more than length")
head = create_list([1, 2, 3])
rotated = rotate_right(head, 7)  # 7 % 3 = 1
print(f"Input:  [1, 2, 3], k=7")
print(f"Output: {list_to_array(rotated)}")  # [3, 1, 2]

print("\nTest 4: Rotate by 0")
head = create_list([1, 2, 3])
rotated = rotate_right(head, 0)
print(f"Input:  [1, 2, 3], k=0")
print(f"Output: {list_to_array(rotated)}")  # [1, 2, 3]

print("\nTest 5: Single node")
head = create_list([1])
rotated = rotate_right(head, 99)
print(f"Input:  [1], k=99")
print(f"Output: {list_to_array(rotated)}")  # [1]

print("\nTest 6: Two nodes")
head = create_list([1, 2])
rotated = rotate_right(head, 1)
print(f"Input:  [1, 2], k=1")
print(f"Output: {list_to_array(rotated)}")  # [2, 1]

print("\nTest 7: Rotate left")
head = create_list([1, 2, 3, 4, 5])
rotated = rotate_left(head, 2)
print(f"Input:  [1, 2, 3, 4, 5], k=2 (left)")
print(f"Output: {list_to_array(rotated)}")  # [3, 4, 5, 1, 2]
```

**Visual Explanation:**
```
Rotate right [1, 2, 3, 4, 5] by k=2:

Original: 1 -> 2 -> 3 -> 4 -> 5

Step 1: Connect tail to head
1 -> 2 -> 3 -> 4 -> 5 -> 1 (circular)

Step 2: Find new tail at position length-k-1 = 5-2-1 = 2
        (node with value 3)

Step 3: Break at new tail
New head: 4
4 -> 5 -> 1 -> 2 -> 3

Result: [4, 5, 1, 2, 3]
```

**Output:**
```
Test 1: Rotate right by 2
Input:  [1, 2, 3, 4, 5], k=2
Output: [4, 5, 1, 2, 3]

Test 2: Rotate by length (no change)
Input:  [1, 2, 3], k=3
Output: [1, 2, 3]

Test 3: Rotate by more than length
Input:  [1, 2, 3], k=7
Output: [3, 1, 2]

Test 4: Rotate by 0
Input:  [1, 2, 3], k=0
Output: [1, 2, 3]

Test 5: Single node
Input:  [1], k=99
Output: [1]

Test 6: Two nodes
Input:  [1, 2], k=1
Output: [2, 1]

Test 7: Rotate left
Input:  [1, 2, 3, 4, 5], k=2 (left)
Output: [3, 4, 5, 1, 2]
```

---

## Example 17: Partition List

```python
def partition(head, x):
    """
    Partition list around value x.
    Nodes < x come before nodes >= x.
    Preserve original relative order.

    Time: O(n)
    Space: O(1)
    """
    # Create two dummy heads
    before_head = ListNode(0)
    after_head = ListNode(0)

    before = before_head
    after = after_head

    # Partition nodes
    current = head
    while current:
        if current.val < x:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next
        current = current.next

    # Important: terminate after list
    after.next = None

    # Connect before and after
    before.next = after_head.next

    return before_head.next

# Test cases
print("Test 1: Basic partition")
head = create_list([1, 4, 3, 2, 5, 2])
result = partition(head, 3)
print(f"Input:  [1, 4, 3, 2, 5, 2], x=3")
print(f"Output: {list_to_array(result)}")  # [1, 2, 2, 4, 3, 5]

print("\nTest 2: All less than x")
head = create_list([1, 2, 3])
result = partition(head, 5)
print(f"Input:  [1, 2, 3], x=5")
print(f"Output: {list_to_array(result)}")  # [1, 2, 3]

print("\nTest 3: All greater or equal to x")
head = create_list([5, 6, 7])
result = partition(head, 3)
print(f"Input:  [5, 6, 7], x=3")
print(f"Output: {list_to_array(result)}")  # [5, 6, 7]

print("\nTest 4: Single node")
head = create_list([1])
result = partition(head, 0)
print(f"Input:  [1], x=0")
print(f"Output: {list_to_array(result)}")  # [1]

print("\nTest 5: Already partitioned")
head = create_list([1, 2, 5, 6])
result = partition(head, 3)
print(f"Input:  [1, 2, 5, 6], x=3")
print(f"Output: {list_to_array(result)}")  # [1, 2, 5, 6]

print("\nTest 6: Reverse partitioned")
head = create_list([5, 6, 1, 2])
result = partition(head, 3)
print(f"Input:  [5, 6, 1, 2], x=3")
print(f"Output: {list_to_array(result)}")  # [1, 2, 5, 6]
```

**Visual Explanation:**
```
Partition [1, 4, 3, 2, 5, 2] around x=3:

Before list: nodes < 3
After list: nodes >= 3

Processing:
1 < 3: before -> 1
4 >= 3: after -> 4
3 >= 3: after -> 4 -> 3
2 < 3: before -> 1 -> 2
5 >= 3: after -> 4 -> 3 -> 5
2 < 3: before -> 1 -> 2 -> 2

Connect:
before: 1 -> 2 -> 2
after:  4 -> 3 -> 5

Result: 1 -> 2 -> 2 -> 4 -> 3 -> 5
```

**Output:**
```
Test 1: Basic partition
Input:  [1, 4, 3, 2, 5, 2], x=3
Output: [1, 2, 2, 4, 3, 5]

Test 2: All less than x
Input:  [1, 2, 3], x=5
Output: [1, 2, 3]

Test 3: All greater or equal to x
Input:  [5, 6, 7], x=3
Output: [5, 6, 7]

Test 4: Single node
Input:  [1], x=0
Output: [1]

Test 5: Already partitioned
Input:  [1, 2, 5, 6], x=3
Output: [1, 2, 5, 6]

Test 6: Reverse partitioned
Input:  [5, 6, 1, 2], x=3
Output: [1, 2, 5, 6]
```

---

## Example 18: Remove Linked List Elements

```python
def remove_elements(head, val):
    """
    Remove all nodes with given value.

    Time: O(n)
    Space: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head

    current = dummy
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next

def remove_elements_recursive(head, val):
    """
    Remove elements recursively.

    Time: O(n)
    Space: O(n) for recursion stack
    """
    if not head:
        return None

    head.next = remove_elements_recursive(head.next, val)

    return head.next if head.val == val else head

# Test cases
print("Test 1: Remove middle elements")
head = create_list([1, 2, 6, 3, 4, 5, 6])
result = remove_elements(head, 6)
print(f"Input:  [1, 2, 6, 3, 4, 5, 6], val=6")
print(f"Output: {list_to_array(result)}")  # [1, 2, 3, 4, 5]

print("\nTest 2: Remove all elements")
head = create_list([7, 7, 7, 7])
result = remove_elements(head, 7)
print(f"Input:  [7, 7, 7, 7], val=7")
print(f"Output: {list_to_array(result)}")  # []

print("\nTest 3: Remove first element")
head = create_list([1, 2, 3, 4])
result = remove_elements(head, 1)
print(f"Input:  [1, 2, 3, 4], val=1")
print(f"Output: {list_to_array(result)}")  # [2, 3, 4]

print("\nTest 4: Remove last element")
head = create_list([1, 2, 3, 4])
result = remove_elements(head, 4)
print(f"Input:  [1, 2, 3, 4], val=4")
print(f"Output: {list_to_array(result)}")  # [1, 2, 3]

print("\nTest 5: Value not in list")
head = create_list([1, 2, 3, 4])
result = remove_elements(head, 5)
print(f"Input:  [1, 2, 3, 4], val=5")
print(f"Output: {list_to_array(result)}")  # [1, 2, 3, 4]

print("\nTest 6: Empty list")
head = create_list([])
result = remove_elements(head, 1)
print(f"Input:  [], val=1")
print(f"Output: {list_to_array(result)}")  # []

print("\nTest 7: Recursive approach")
head = create_list([1, 2, 6, 3, 4, 5, 6])
result = remove_elements_recursive(head, 6)
print(f"Input:  [1, 2, 6, 3, 4, 5, 6], val=6")
print(f"Output (recursive): {list_to_array(result)}")  # [1, 2, 3, 4, 5]
```

**Output:**
```
Test 1: Remove middle elements
Input:  [1, 2, 6, 3, 4, 5, 6], val=6
Output: [1, 2, 3, 4, 5]

Test 2: Remove all elements
Input:  [7, 7, 7, 7], val=7
Output: []

Test 3: Remove first element
Input:  [1, 2, 3, 4], val=1
Output: [2, 3, 4]

Test 4: Remove last element
Input:  [1, 2, 3, 4], val=4
Output: [1, 2, 3]

Test 5: Value not in list
Input:  [1, 2, 3, 4], val=5
Output: [1, 2, 3, 4]

Test 6: Empty list
Input:  [], val=1
Output: []

Test 7: Recursive approach
Input:  [1, 2, 6, 3, 4, 5, 6], val=6
Output (recursive): [1, 2, 3, 4, 5]
```

---

## Example 19: Odd-Even Linked List

```python
def odd_even_list(head):
    """
    Group odd-indexed nodes followed by even-indexed nodes.

    Time: O(n)
    Space: O(1)

    Example: [1,2,3,4,5] -> [1,3,5,2,4]
    """
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head

# Test cases
print("Test 1: Odd length list")
head = create_list([1, 2, 3, 4, 5])
result = odd_even_list(head)
print(f"Input:  [1, 2, 3, 4, 5]")
print(f"Output: {list_to_array(result)}")  # [1, 3, 5, 2, 4]

print("\nTest 2: Even length list")
head = create_list([2, 1, 3, 5, 6, 4, 7])
result = odd_even_list(head)
print(f"Input:  [2, 1, 3, 5, 6, 4, 7]")
print(f"Output: {list_to_array(result)}")  # [2, 3, 6, 7, 1, 5, 4]

print("\nTest 3: Two nodes")
head = create_list([1, 2])
result = odd_even_list(head)
print(f"Input:  [1, 2]")
print(f"Output: {list_to_array(result)}")  # [1, 2]

print("\nTest 4: Single node")
head = create_list([1])
result = odd_even_list(head)
print(f"Input:  [1]")
print(f"Output: {list_to_array(result)}")  # [1]

print("\nTest 5: Three nodes")
head = create_list([1, 2, 3])
result = odd_even_list(head)
print(f"Input:  [1, 2, 3]")
print(f"Output: {list_to_array(result)}")  # [1, 3, 2]

print("\nTest 6: Four nodes")
head = create_list([1, 2, 3, 4])
result = odd_even_list(head)
print(f"Input:  [1, 2, 3, 4]")
print(f"Output: {list_to_array(result)}")  # [1, 3, 2, 4]
```

**Visual Explanation:**
```
Input: 1 -> 2 -> 3 -> 4 -> 5

Odd indices:  1 (index 0), 3 (index 2), 5 (index 4)
Even indices: 2 (index 1), 4 (index 3)

Process:
odd:  1 ----------> 3 ----------> 5
even:      2 ----------> 4

Connect odd tail to even head:
1 -> 3 -> 5 -> 2 -> 4

Result: [1, 3, 5, 2, 4]
```

**Output:**
```
Test 1: Odd length list
Input:  [1, 2, 3, 4, 5]
Output: [1, 3, 5, 2, 4]

Test 2: Even length list
Input:  [2, 1, 3, 5, 6, 4, 7]
Output: [2, 3, 6, 7, 1, 5, 4]

Test 3: Two nodes
Input:  [1, 2]
Output: [1, 2]

Test 4: Single node
Input:  [1]
Output: [1]

Test 5: Three nodes
Input:  [1, 2, 3]
Output: [1, 3, 2]

Test 6: Four nodes
Input:  [1, 2, 3, 4]
Output: [1, 3, 2, 4]
```

---

## Example 20: Reverse Nodes in K-Group

```python
def reverse_k_group(head, k):
    """
    Reverse nodes in groups of k.

    Time: O(n)
    Space: O(1)

    Example: [1,2,3,4,5], k=2 -> [2,1,4,3,5]
             [1,2,3,4,5], k=3 -> [3,2,1,4,5]
    """
    if not head or k == 1:
        return head

    # Check if we have k nodes remaining
    count = 0
    curr = head
    while curr and count < k:
        curr = curr.next
        count += 1

    if count < k:
        return head

    # Reverse first k nodes
    prev = None
    curr = head
    for _ in range(k):
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # Recursively reverse remaining groups
    head.next = reverse_k_group(curr, k)

    return prev

def reverse_k_group_iterative(head, k):
    """
    Iterative version.

    Time: O(n)
    Space: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head

    prev_group = dummy

    while True:
        # Check if k nodes exist
        kth = prev_group
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next

        # Reverse k nodes
        group_start = prev_group.next
        prev = kth.next
        curr = group_start

        for _ in range(k):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Connect with previous group
        prev_group.next = kth
        prev_group = group_start

# Test cases
print("Test 1: k=2, exact groups")
head = create_list([1, 2, 3, 4])
result = reverse_k_group(head, 2)
print(f"Input:  [1, 2, 3, 4], k=2")
print(f"Output: {list_to_array(result)}")  # [2, 1, 4, 3]

print("\nTest 2: k=3, with remainder")
head = create_list([1, 2, 3, 4, 5])
result = reverse_k_group(head, 3)
print(f"Input:  [1, 2, 3, 4, 5], k=3")
print(f"Output: {list_to_array(result)}")  # [3, 2, 1, 4, 5]

print("\nTest 3: k=1, no reversal")
head = create_list([1, 2, 3])
result = reverse_k_group(head, 1)
print(f"Input:  [1, 2, 3], k=1")
print(f"Output: {list_to_array(result)}")  # [1, 2, 3]

print("\nTest 4: k equals list length")
head = create_list([1, 2, 3, 4, 5])
result = reverse_k_group(head, 5)
print(f"Input:  [1, 2, 3, 4, 5], k=5")
print(f"Output: {list_to_array(result)}")  # [5, 4, 3, 2, 1]

print("\nTest 5: k greater than list length")
head = create_list([1, 2])
result = reverse_k_group(head, 3)
print(f"Input:  [1, 2], k=3")
print(f"Output: {list_to_array(result)}")  # [1, 2]

print("\nTest 6: Multiple complete groups")
head = create_list([1, 2, 3, 4, 5, 6])
result = reverse_k_group(head, 3)
print(f"Input:  [1, 2, 3, 4, 5, 6], k=3")
print(f"Output: {list_to_array(result)}")  # [3, 2, 1, 6, 5, 4]

print("\nTest 7: Iterative approach")
head = create_list([1, 2, 3, 4, 5])
result = reverse_k_group_iterative(head, 2)
print(f"Input:  [1, 2, 3, 4, 5], k=2")
print(f"Output (iterative): {list_to_array(result)}")  # [2, 1, 4, 3, 5]
```

**Visual Explanation:**
```
Reverse [1, 2, 3, 4, 5] in groups of k=2:

Original: 1 -> 2 -> 3 -> 4 -> 5

Group 1: [1, 2]
Reverse: 2 -> 1

Group 2: [3, 4]
Reverse: 4 -> 3

Group 3: [5]
No reverse (less than k)

Connect: 2 -> 1 -> 4 -> 3 -> 5

Result: [2, 1, 4, 3, 5]

Reverse [1, 2, 3, 4, 5, 6] in groups of k=3:

Original: 1 -> 2 -> 3 -> 4 -> 5 -> 6

Group 1: [1, 2, 3]
Reverse: 3 -> 2 -> 1

Group 2: [4, 5, 6]
Reverse: 6 -> 5 -> 4

Connect: 3 -> 2 -> 1 -> 6 -> 5 -> 4

Result: [3, 2, 1, 6, 5, 4]
```

**Output:**
```
Test 1: k=2, exact groups
Input:  [1, 2, 3, 4], k=2
Output: [2, 1, 4, 3]

Test 2: k=3, with remainder
Input:  [1, 2, 3, 4, 5], k=3
Output: [3, 2, 1, 4, 5]

Test 3: k=1, no reversal
Input:  [1, 2, 3], k=1
Output: [1, 2, 3]

Test 4: k equals list length
Input:  [1, 2, 3, 4, 5], k=5
Output: [5, 4, 3, 2, 1]

Test 5: k greater than list length
Input:  [1, 2], k=3
Output: [1, 2]

Test 6: Multiple complete groups
Input:  [1, 2, 3, 4, 5, 6], k=3
Output: [3, 2, 1, 6, 5, 4]

Test 7: Iterative approach
Input:  [1, 2, 3, 4, 5], k=2
Output (iterative): [2, 1, 4, 3, 5]
```

---

**Summary of Complexity:**

| Example | Time | Space | Key Technique |
|---------|------|-------|---------------|
| 1. Singly Linked List | O(n) ops | O(1) | Basic operations |
| 2. Reverse (Iterative) | O(n) | O(1) | Three pointers |
| 3. Reverse (Recursive) | O(n) | O(n) | Recursion |
| 4. Detect Cycle | O(n) | O(1) | Floyd's algorithm |
| 5. Cycle Start | O(n) | O(1) | Two-phase detection |
| 6. Find Middle | O(n) | O(1) | Fast/slow pointers |
| 7. Merge Two Lists | O(n+m) | O(1) | Two pointers |
| 8. Remove Nth from End | O(n) | O(1) | Gap pointers |
| 9. Palindrome | O(n) | O(1) | Reverse half |
| 10. Remove Duplicates | O(n) | O(1) | Single pass |
| 11. Intersection | O(n+m) | O(1) | Length alignment |
| 12. Add Numbers | O(max(n,m)) | O(max(n,m)) | Carry handling |
| 13. Copy Random | O(n) | O(n) or O(1) | Hash map or interweave |
| 14. Flatten Multilevel | O(n) | O(d) | DFS |
| 15. Sort List | O(n log n) | O(log n) | Merge sort |
| 16. Rotate List | O(n) | O(1) | Circular connection |
| 17. Partition | O(n) | O(1) | Two lists |
| 18. Remove Elements | O(n) | O(1) | Dummy head |
| 19. Odd-Even List | O(n) | O(1) | Two pointers |
| 20. Reverse K-Group | O(n) | O(1) or O(n/k) | Group reversal |
