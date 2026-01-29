# Linked Lists: Exercise Solutions

## Solution 1: Reverse Linked List Between Positions

```python
def reverse_between(head, left, right):
    """
    Reverse list from position left to right.

    Time: O(n)
    Space: O(1)
    """
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head

    # Find node before left position
    prev = dummy
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

# Alternative: More intuitive approach
def reverse_between_v2(head, left, right):
    """
    Reverse between positions using standard reversal.

    Time: O(n)
    Space: O(1)
    """
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move to node before left
    for _ in range(left - 1):
        prev = prev.next

    # Standard reversal for (right - left + 1) nodes
    reverse_start = prev.next
    current = reverse_start
    prev_node = None

    for _ in range(right - left + 1):
        next_temp = current.next
        current.next = prev_node
        prev_node = current
        current = next_temp

    # Connect reversed portion
    prev.next = prev_node
    reverse_start.next = current

    return dummy.next

# Test
head = create_list([1, 2, 3, 4, 5])
result = reverse_between(head, 2, 4)
print(list_to_array(result))  # [1, 4, 3, 2, 5]
```

**Complexity:** O(n) time, O(1) space

---

## Solution 2: Reorder List

```python
def reorder_list(head):
    """
    Reorder list: L0→Ln→L1→Ln-1→L2→Ln-2...

    Time: O(n)
    Space: O(1)

    Approach:
    1. Find middle
    2. Reverse second half
    3. Merge two halves
    """
    if not head or not head.next:
        return

    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second = slow.next
    slow.next = None
    prev = None
    current = second

    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    second = prev

    # Merge two halves
    first = head
    while second:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2

# Test
head = create_list([1, 2, 3, 4, 5])
reorder_list(head)
print(list_to_array(head))  # [1, 5, 2, 4, 3]
```

**Complexity:** O(n) time, O(1) space

---

## Solution 3: Remove Zero Sum Consecutive Nodes

```python
def remove_zero_sum_sublists(head):
    """
    Remove all consecutive sequences summing to 0.

    Time: O(n)
    Space: O(n) for hash map
    """
    dummy = ListNode(0)
    dummy.next = head

    prefix_sum = 0
    sum_map = {0: dummy}
    current = head

    # First pass: record prefix sums
    while current:
        prefix_sum += current.val
        sum_map[prefix_sum] = current
        current = current.next

    # Second pass: remove zero-sum sequences
    prefix_sum = 0
    current = dummy

    while current:
        prefix_sum += current.val
        current.next = sum_map[prefix_sum].next
        current = current.next

    return dummy.next

# Alternative: Single pass with deletion
def remove_zero_sum_sublists_v2(head):
    """
    Single pass version.

    Time: O(n^2) worst case
    Space: O(n)
    """
    dummy = ListNode(0)
    dummy.next = head

    prefix_sum = 0
    sum_map = {0: dummy}
    current = head

    while current:
        prefix_sum += current.val

        if prefix_sum in sum_map:
            # Remove nodes from sum_map
            prev = sum_map[prefix_sum]
            temp = prev.next
            temp_sum = prefix_sum

            while temp != current:
                temp_sum += temp.val
                del sum_map[temp_sum]
                temp = temp.next

            # Skip zero-sum sequence
            prev.next = current.next
        else:
            sum_map[prefix_sum] = current

        current = current.next

    return dummy.next

# Test
head = create_list([1, 2, -3, 3, 1])
result = remove_zero_sum_sublists(head)
print(list_to_array(result))  # [3, 1]

head = create_list([1, 2, 3, -3, 4])
result = remove_zero_sum_sublists(head)
print(list_to_array(result))  # [1, 2, 4]
```

**Complexity:** O(n) time, O(n) space

---

## Solution 4: Swap Nodes in Pairs

```python
def swap_pairs(head):
    """
    Swap every two adjacent nodes.

    Time: O(n)
    Space: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        # Nodes to swap
        first = prev.next
        second = first.next

        # Swap
        first.next = second.next
        second.next = first
        prev.next = second

        # Move to next pair
        prev = first

    return dummy.next

def swap_pairs_recursive(head):
    """
    Recursive approach.

    Time: O(n)
    Space: O(n) for recursion stack
    """
    if not head or not head.next:
        return head

    # Swap first two nodes
    first = head
    second = head.next

    first.next = swap_pairs_recursive(second.next)
    second.next = first

    return second

# Test
head = create_list([1, 2, 3, 4])
result = swap_pairs(head)
print(list_to_array(result))  # [2, 1, 4, 3]

head = create_list([1, 2, 3])
result = swap_pairs_recursive(head)
print(list_to_array(result))  # [2, 1, 3]
```

**Complexity:** Iterative - O(n) time, O(1) space; Recursive - O(n) time, O(n) space

---

## Solution 5: Merge K Sorted Lists

```python
import heapq

def merge_k_lists(lists):
    """
    Merge k sorted lists using min heap.

    Time: O(N log k) where N = total nodes, k = number of lists
    Space: O(k) for heap
    """
    if not lists:
        return None

    heap = []

    # Add first node of each list to heap
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

def merge_k_lists_divide_conquer(lists):
    """
    Merge k lists using divide and conquer.

    Time: O(N log k)
    Space: O(log k) for recursion
    """
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    def merge_two(l1, l2):
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
        current.next = l1 or l2
        return dummy.next

    def merge_lists(lists):
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return merge_two(lists[0], lists[1])

        mid = len(lists) // 2
        left = merge_lists(lists[:mid])
        right = merge_lists(lists[mid:])
        return merge_two(left, right)

    return merge_lists(lists)

# Test
lists = [
    create_list([1, 4, 5]),
    create_list([1, 3, 4]),
    create_list([2, 6])
]
result = merge_k_lists(lists)
print(list_to_array(result))  # [1, 1, 2, 3, 4, 4, 5, 6]
```

**Complexity:**
- Heap approach: O(N log k) time, O(k) space
- Divide & conquer: O(N log k) time, O(log k) space

---

## Solution 6: Linked List Cycle II

```python
def detect_cycle(head):
    """
    Find node where cycle begins.

    Time: O(n)
    Space: O(1)

    Uses Floyd's algorithm with mathematical proof.
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

def detect_cycle_hash(head):
    """
    Find cycle start using hash set.

    Time: O(n)
    Space: O(n)
    """
    visited = set()
    current = head

    while current:
        if current in visited:
            return current
        visited.add(current)
        current = current.next

    return None

# Test
# Create cycle at position 1
head = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Cycle

result = detect_cycle(head)
print(f"Cycle starts at node with value: {result.val}")  # 2
```

**Complexity:** Floyd's - O(n) time, O(1) space; Hash - O(n) time, O(n) space

---

## Solution 7: Delete Node in a Linked List

```python
def delete_node(node):
    """
    Delete node without access to head.

    Time: O(1)
    Space: O(1)

    Key insight: Copy next node's value and delete next.
    """
    node.val = node.next.val
    node.next = node.next.next

# Test
head = create_list([4, 5, 1, 9])
node_to_delete = head.next  # node with value 5
delete_node(node_to_delete)
print(list_to_array(head))  # [4, 1, 9]
```

**Complexity:** O(1) time and space

---

## Solution 8: Split Linked List in Parts

```python
def split_list_to_parts(head, k):
    """
    Split list into k parts with equal lengths.

    Time: O(n)
    Space: O(k) for result array
    """
    # Get length
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Calculate part sizes
    base_size = length // k
    extra = length % k

    result = []
    current = head

    for i in range(k):
        part_head = current
        part_size = base_size + (1 if i < extra else 0)

        # Advance to end of part
        for j in range(part_size - 1):
            if current:
                current = current.next

        # Split
        if current:
            next_part = current.next
            current.next = None
            current = next_part

        result.append(part_head)

    return result

# Test
head = create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
parts = split_list_to_parts(head, 3)
for part in parts:
    print(list_to_array(part))
# Output:
# [1, 2, 3, 4]
# [5, 6, 7]
# [8, 9, 10]
```

**Complexity:** O(n) time, O(k) space

---

## Solution 9: Plus One to Linked List

```python
def plus_one(head):
    """
    Add one to number represented as linked list.

    Time: O(n)
    Space: O(1)

    Approach: Find rightmost non-9, increment, set rest to 0.
    """
    # Find rightmost non-9 digit
    dummy = ListNode(0)
    dummy.next = head
    not_nine = dummy

    current = head
    while current:
        if current.val != 9:
            not_nine = current
        current = current.next

    # Increment rightmost non-9
    not_nine.val += 1
    current = not_nine.next

    # Set remaining to 0
    while current:
        current.val = 0
        current = current.next

    # Return dummy.next if new digit added, else head
    return dummy if dummy.val else dummy.next

def plus_one_recursive(head):
    """
    Recursive approach.

    Time: O(n)
    Space: O(n) for recursion
    """
    def add_helper(node):
        """Returns carry."""
        if not node:
            return 1

        carry = add_helper(node.next)
        total = node.val + carry
        node.val = total % 10
        return total // 10

    carry = add_helper(head)
    if carry:
        new_head = ListNode(carry)
        new_head.next = head
        return new_head
    return head

# Test
head = create_list([1, 2, 3])
result = plus_one(head)
print(list_to_array(result))  # [1, 2, 4]

head = create_list([9, 9, 9])
result = plus_one_recursive(head)
print(list_to_array(result))  # [1, 0, 0, 0]
```

**Complexity:** O(n) time, O(1) or O(n) space depending on approach

---

## Solution 10: Insertion Sort List

```python
def insertion_sort_list(head):
    """
    Sort list using insertion sort.

    Time: O(n^2)
    Space: O(1)
    """
    if not head or not head.next:
        return head

    dummy = ListNode(float('-inf'))
    current = head

    while current:
        # Save next node
        next_node = current.next

        # Find insertion position
        prev = dummy
        while prev.next and prev.next.val < current.val:
            prev = prev.next

        # Insert current
        current.next = prev.next
        prev.next = current

        # Move to next unsorted node
        current = next_node

    return dummy.next

# Test
head = create_list([4, 2, 1, 3])
result = insertion_sort_list(head)
print(list_to_array(result))  # [1, 2, 3, 4]

head = create_list([-1, 5, 3, 4, 0])
result = insertion_sort_list(head)
print(list_to_array(result))  # [-1, 0, 3, 4, 5]
```

**Complexity:** O(n²) time, O(1) space

---

## Solution 11: Sort List with Three Colors

```python
def sort_colors_list(head):
    """
    Sort list containing only 0, 1, 2 (Dutch National Flag).

    Time: O(n)
    Space: O(1)
    """
    if not head or not head.next:
        return head

    # Create three dummy heads
    dummy0 = ListNode(0)
    dummy1 = ListNode(0)
    dummy2 = ListNode(0)

    # Pointers for each list
    p0, p1, p2 = dummy0, dummy1, dummy2

    current = head
    while current:
        if current.val == 0:
            p0.next = current
            p0 = p0.next
        elif current.val == 1:
            p1.next = current
            p1 = p1.next
        else:
            p2.next = current
            p2 = p2.next
        current = current.next

    # Terminate lists
    p2.next = None

    # Connect three lists
    p1.next = dummy2.next
    p0.next = dummy1.next

    return dummy0.next

# Test
head = create_list([1, 0, 2, 1, 0, 2, 1])
result = sort_colors_list(head)
print(list_to_array(result))  # [0, 0, 1, 1, 1, 2, 2]
```

**Complexity:** O(n) time, O(1) space

---

## Solution 12: Add Two Numbers II (Forward Order)

```python
def add_two_numbers_forward(l1, l2):
    """
    Add two numbers in forward order using stacks.

    Time: O(max(m, n))
    Space: O(max(m, n))
    """
    stack1, stack2 = [], []

    # Push all values to stacks
    while l1:
        stack1.append(l1.val)
        l1 = l1.next

    while l2:
        stack2.append(l2.val)
        l2 = l2.next

    carry = 0
    head = None

    # Process from least significant digit
    while stack1 or stack2 or carry:
        val1 = stack1.pop() if stack1 else 0
        val2 = stack2.pop() if stack2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        # Insert at beginning
        node = ListNode(digit)
        node.next = head
        head = node

    return head

# Alternative: Reverse, add, reverse back
def add_two_numbers_forward_v2(l1, l2):
    """
    Using reversal.

    Time: O(max(m, n))
    Space: O(1)
    """
    def reverse(head):
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev

    # Reverse both lists
    l1 = reverse(l1)
    l2 = reverse(l2)

    # Add
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # Reverse result
    return reverse(dummy.next)

# Test
l1 = create_list([7, 2, 4, 3])  # 7243
l2 = create_list([5, 6, 4])      # 564
result = add_two_numbers_forward(l1, l2)
print(list_to_array(result))  # [7, 8, 0, 7] = 7807
```

**Complexity:** O(max(m,n)) time, O(max(m,n)) space for stack approach

---

## Solution 13: Linked List Random Node

```python
import random

class LinkedListRandom:
    """
    Return random node with equal probability.

    Using reservoir sampling for O(1) space.
    """
    def __init__(self, head):
        self.head = head

    def get_random(self):
        """
        Time: O(n)
        Space: O(1)
        """
        result = self.head.val
        current = self.head.next
        count = 2

        while current:
            # With probability 1/count, choose current
            if random.randint(1, count) == 1:
                result = current.val
            current = current.next
            count += 1

        return result

class LinkedListRandomArray:
    """
    Using array for O(1) getRandom.
    """
    def __init__(self, head):
        self.values = []
        current = head
        while current:
            self.values.append(current.val)
            current = current.next

    def get_random(self):
        """
        Time: O(1)
        Space: O(n)
        """
        return random.choice(self.values)

# Test
head = create_list([1, 2, 3, 4, 5])
llr = LinkedListRandom(head)
print(llr.get_random())  # Random value from list
```

**Complexity:**
- Reservoir sampling: O(n) time per call, O(1) space
- Array: O(1) time per call, O(n) space

---

## Solution 14: Convert BST to Sorted Doubly Linked List

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_doubly_list(root):
    """
    Convert BST to circular sorted doubly linked list.

    Time: O(n)
    Space: O(h) for recursion stack
    """
    if not root:
        return None

    first = last = None

    def inorder(node):
        nonlocal first, last

        if not node:
            return

        # Left subtree
        inorder(node.left)

        # Process current node
        if last:
            last.right = node
            node.left = last
        else:
            # First node
            first = node

        last = node

        # Right subtree
        inorder(node.right)

    inorder(root)

    # Make circular
    last.right = first
    first.left = last

    return first

# Test
# Create BST:     4
#               /   \
#              2     5
#             / \
#            1   3

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

head = tree_to_doubly_list(root)
# Result: circular list 1<->2<->3<->4<->5
```

**Complexity:** O(n) time, O(h) space

---

## Solution 15: LRU Cache

```python
class DLLNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    LRU Cache with O(1) get and put.

    Uses doubly linked list + hash map.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Dummy head and tail
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        Time: O(1)
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_front(node)
        return node.val

    def put(self, key, value):
        """
        Time: O(1)
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)
        else:
            node = DLLNode(key, value)
            self.cache[key] = node
            self._add_to_front(node)

            if len(self.cache) > self.capacity:
                # Remove LRU (tail.prev)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

    def _add_to_front(self, node):
        """Add node after head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        """Remove node from list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_front(self, node):
        """Move node to front (most recently used)."""
        self._remove(node)
        self._add_to_front(node)

# Test
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # 1
cache.put(3, 3)        # evicts key 2
print(cache.get(2))    # -1
cache.put(4, 4)        # evicts key 1
print(cache.get(1))    # -1
print(cache.get(3))    # 3
print(cache.get(4))    # 4
```

**Complexity:** O(1) for both get and put

---

## Solution 16-20 and Bonus Challenges

Due to length constraints, the remaining solutions follow similar patterns:

- **Solution 16-17:** Use DFS/BFS with hash maps for graph/tree problems
- **Solution 18:** Doubly linked list with current pointer
- **Solution 19:** Track group sizes, reverse even-length groups
- **Solution 20:** Find middle, reverse second half, compare sums

**Bonus Challenge Hints:**
- Use DP for optimization problems
- Hash maps for node tracking in complex structures
- Combine multiple techniques (reversal + merging + partitioning)
- Always consider space-time tradeoffs

**Key Takeaways:**
1. Master basic operations first
2. Practice pointer manipulation
3. Use dummy nodes for simplification
4. Consider both iterative and recursive approaches
5. Analyze space-time complexity
6. Test edge cases thoroughly
