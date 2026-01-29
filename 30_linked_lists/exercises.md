# Linked Lists: Practice Exercises

## Exercise 1: Reverse Linked List Between Positions

**Difficulty:** Medium

Reverse a linked list from position `left` to position `right` (1-indexed).

**Example:**
```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

**Constraints:**
- 1 <= left <= right <= length of list
- 1 <= list length <= 500

**Hints:**
- Use dummy node for edge cases
- Find node before left position
- Reverse nodes from left to right
- Reconnect the reversed portion

---

## Exercise 2: Reorder List

**Difficulty:** Medium

Reorder list: L0 → L1 → ... → Ln-1 → Ln to L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

**Example:**
```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

**Constraints:**
- 1 <= list length <= 5 * 10^4
- Modify list in-place

**Hints:**
- Find middle of list
- Reverse second half
- Merge two halves alternately

---

## Exercise 3: Remove Zero Sum Consecutive Nodes

**Difficulty:** Medium

Remove all consecutive sequences of nodes that sum to 0.

**Example:**
```
Input: head = [1,2,-3,3,1]
Output: [3,1]
Explanation: [1,2,-3] sums to 0, remove it

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Explanation: [3,-3] sums to 0
```

**Constraints:**
- -1000 <= Node.val <= 1000
- 1 <= list length <= 1000

**Hints:**
- Use prefix sum with hash map
- If prefix sum repeats, nodes between sum to 0
- Delete nodes between same prefix sums

---

## Exercise 4: Swap Nodes in Pairs

**Difficulty:** Easy

Swap every two adjacent nodes.

**Example:**
```
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = [1]
Output: [1]

Input: head = [1,2,3]
Output: [2,1,3]
```

**Constraints:**
- 0 <= list length <= 100
- Don't modify node values, only pointers

**Hints:**
- Use dummy node
- Track prev, first, second nodes
- Update pointers carefully

---

## Exercise 5: Merge K Sorted Lists

**Difficulty:** Hard

Merge k sorted linked lists into one sorted list.

**Example:**
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**Constraints:**
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500

**Hints:**
- Use min heap (priority queue)
- Add first node of each list to heap
- Pop min, add its next to heap
- Or: divide and conquer with merge sort

---

## Exercise 6: Linked List Cycle II

**Difficulty:** Medium

Return the node where cycle begins. Return null if no cycle.

**Example:**
```
Input: head = [3,2,0,-4], pos = 1 (tail connects to index 1)
Output: Node with value 2

Input: head = [1], pos = -1
Output: null
```

**Constraints:**
- 0 <= list length <= 10^4
- -10^5 <= Node.val <= 10^5
- pos is -1 or valid index

**Hints:**
- Use Floyd's algorithm to detect cycle
- Mathematical proof for finding start
- Two pointers with different speeds

---

## Exercise 7: Delete Node in a Linked List

**Difficulty:** Easy

Delete a node (not tail) given only access to that node.

**Example:**
```
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: Delete the node with value 5
```

**Constraints:**
- 2 <= list length <= 1000
- -1000 <= Node.val <= 1000
- Given node is not tail

**Hints:**
- You can't access previous node
- Copy next node's value to current
- Delete next node instead

---

## Exercise 8: Split Linked List in Parts

**Difficulty:** Medium

Split list into k consecutive parts with lengths as equal as possible.

**Example:**
```
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]

Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
```

**Constraints:**
- 0 <= list length <= 1000
- 1 <= k <= 50

**Hints:**
- Calculate total length
- Determine base size and extra nodes
- Split carefully, setting tail.next = None

---

## Exercise 9: Plus One to Linked List

**Difficulty:** Medium

Given non-negative integer as linked list, add one to it.

**Example:**
```
Input: head = [1,2,3]
Output: [1,2,4]

Input: head = [9,9,9]
Output: [1,0,0,0]
```

**Constraints:**
- 1 <= list length <= 100
- 0 <= Node.val <= 9

**Hints:**
- Reverse list, add one, reverse back
- Or use recursion returning carry
- Or find rightmost non-9 node

---

## Exercise 10: Insertion Sort List

**Difficulty:** Medium

Sort linked list using insertion sort.

**Example:**
```
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

**Constraints:**
- 0 <= list length <= 5000
- -5000 <= Node.val <= 5000

**Hints:**
- Create sorted portion starting with dummy
- For each node, find insertion position
- Insert and move to next unsorted node

---

## Exercise 11: Sort List with Three Colors

**Difficulty:** Medium

Sort list containing only 0s, 1s, and 2s (Dutch National Flag).

**Example:**
```
Input: head = [1,0,2,1,0,2,1]
Output: [0,0,1,1,1,2,2]
```

**Constraints:**
- 1 <= list length <= 1000
- Node.val in {0, 1, 2}
- O(n) time, O(1) space

**Hints:**
- Create three separate lists
- Traverse once, distribute nodes
- Connect three lists at end

---

## Exercise 12: Add Two Numbers II (Forward Order)

**Difficulty:** Medium

Add two numbers represented as linked lists (most significant digit first).

**Example:**
```
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Explanation: 7243 + 564 = 7807
```

**Constraints:**
- 1 <= list length <= 100
- 0 <= Node.val <= 9
- No leading zeros except 0 itself

**Hints:**
- Use stack to reverse digits
- Or reverse lists, add, reverse result
- Handle different lengths and carry

---

## Exercise 13: Linked List Random Node

**Difficulty:** Medium

Design class to return random node's value with equal probability.

**Example:**
```
LinkedListRandom llr = new LinkedListRandom(head)
llr.getRandom()  // returns random value
```

**Constraints:**
- 1 <= list length <= 10^4
- getRandom() called at most 10^4 times

**Hints:**
- Store nodes in array
- Or use reservoir sampling
- Two-pass: count then random index

---

## Exercise 14: Convert Binary Search Tree to Sorted Doubly Linked List

**Difficulty:** Medium

Convert BST to sorted circular doubly linked list in-place.

**Example:**
```
Input: BST with values [4,2,5,1,3]
Output: Circular doubly linked list: 1<->2<->3<->4<->5
```

**Constraints:**
- 0 <= tree nodes <= 2000
- -1000 <= Node.val <= 1000

**Hints:**
- In-order traversal gives sorted order
- Track prev pointer during traversal
- Connect first and last for circular

---

## Exercise 15: LRU Cache

**Difficulty:** Medium

Design LRU cache with get and put in O(1).

**Example:**
```
LRUCache cache = new LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       // returns 1
cache.put(3, 3)    // evicts key 2
cache.get(2)       // returns -1
```

**Constraints:**
- 1 <= capacity <= 3000
- 0 <= key, value <= 10^4
- At most 2 * 10^5 calls

**Hints:**
- Use doubly linked list + hash map
- Move accessed items to front
- Remove from tail when capacity exceeded

---

## Exercise 16: Flatten a Multilevel Linked List (Binary Tree Style)

**Difficulty:** Medium

Flatten multilevel list where each node can have child pointer.

**Example:**
```
Input: 1---2---3---4
           |
           5---6

Output: 1-2-5-6-3-4
```

**Constraints:**
- 0 <= nodes <= 1000
- Use DFS preorder traversal

**Hints:**
- Recursively flatten child first
- Insert flattened child after current
- Continue with original next

---

## Exercise 17: Clone Graph (Linked List Variant)

**Difficulty:** Medium

Deep copy a graph represented as adjacency list.

**Example:**
```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: Deep copy with same structure
```

**Constraints:**
- 0 <= nodes <= 100
- Node values are unique

**Hints:**
- Use hash map: original -> copy
- BFS or DFS traversal
- Create nodes first, then edges

---

## Exercise 18: Design Browser History

**Difficulty:** Medium

Design browser history with back, forward, and visit operations.

**Example:**
```
BrowserHistory bh = new BrowserHistory("google.com")
bh.visit("facebook.com")
bh.visit("youtube.com")
bh.back(1)      // returns "facebook.com"
bh.forward(1)   // returns "youtube.com"
```

**Constraints:**
- 1 <= url.length <= 20
- 1 <= steps <= 100

**Hints:**
- Use doubly linked list
- Track current position
- Visit clears forward history

---

## Exercise 19: Reverse Nodes in Even Length Groups

**Difficulty:** Medium

Reverse nodes in groups of consecutive even lengths.

**Example:**
```
Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]
```

**Constraints:**
- 1 <= list length <= 10^5
- 0 <= Node.val <= 10^5

**Hints:**
- Groups have length 1, 2, 3, 4, ...
- Reverse only even-length groups
- Track group boundaries carefully

---

## Exercise 20: Maximum Twin Sum of a Linked List

**Difficulty:** Medium

Find maximum twin sum in list. Twin of node at position i is at n-1-i.

**Example:**
```
Input: head = [5,4,2,1]
Output: 6
Explanation: max(5+1, 4+2) = 6

Input: head = [4,2,2,3]
Output: 7
Explanation: max(4+3, 2+2) = 7
```

**Constraints:**
- List length is even: 2 <= n <= 10^5
- 1 <= Node.val <= 10^5

**Hints:**
- Find middle using slow/fast pointers
- Reverse second half
- Traverse both halves simultaneously
- Calculate twin sums

---

## Bonus Challenge Problems

### Challenge 1: Palindrome Partitioning of Linked List

**Difficulty:** Hard

Partition linked list into minimum number of palindrome sublists.

**Example:**
```
Input: [1,2,3,2,1]
Output: 1 (entire list is palindrome)

Input: [1,2,3,4,5]
Output: 5 (each element is palindrome)
```

**Hints:**
- Dynamic programming approach
- Check all possible partitions
- Verify palindrome for each segment

---

### Challenge 2: Copy List with Multiple Random Pointers

**Difficulty:** Hard

Deep copy linked list where each node has array of random pointers.

**Example:**
```
Input: Node with val=1, random=[node2, node3, node5]
Output: Deep copy with same structure
```

**Hints:**
- Hash map for old -> new mapping
- Multiple passes for different pointers
- Or interweaving technique

---

### Challenge 3: Merge Sorted Lists with Alternating Order

**Difficulty:** Hard

Merge k sorted lists taking nodes alternately from each.

**Example:**
```
Input: [[1,4,7],[2,5,8],[3,6,9]]
Output: [1,2,3,4,5,6,7,8,9]
```

**Hints:**
- Round-robin selection
- Handle lists of different lengths
- Track active lists

---

### Challenge 4: Serialize and Deserialize Linked List with Random Pointer

**Difficulty:** Hard

Design algorithm to serialize and deserialize linked list with random pointers.

**Example:**
```
Input: 1(->3)->2(->1)->3(->1)
Output: Same structure after deserialize(serialize(head))
```

**Hints:**
- Assign unique IDs to nodes
- Store value, next ID, random ID
- Reconstruct using hash map

---

### Challenge 5: Find Kth Element from Two Sorted Lists

**Difficulty:** Hard

Find kth smallest element from two sorted linked lists.

**Example:**
```
Input: l1 = [1,3,5,7], l2 = [2,4,6,8], k = 4
Output: 4
```

**Hints:**
- Binary search on value range
- Count elements less than mid
- Or merge approach with early stop

---

## Testing Your Solutions

For each exercise, test with:
1. Empty list
2. Single node
3. Two nodes
4. Lists with odd/even lengths
5. Lists with duplicate values
6. Lists with negative values (where applicable)
7. Maximum constraint values
8. Edge cases specific to problem

**Example Test Template:**
```python
def test_solution():
    # Edge cases
    assert solution(None) == expected
    assert solution(create_list([1])) == expected

    # Normal cases
    assert solution(create_list([1,2,3,4,5])) == expected

    # Duplicates
    assert solution(create_list([1,1,1])) == expected

    # Large input
    assert solution(create_list(range(1000))) == expected

    print("All tests passed!")
```

**Common Patterns to Practice:**

1. **Two Pointers:** Fast/slow, gap pointers, dummy node
2. **Reversal:** Iterative, recursive, partial reversal
3. **Cycle Detection:** Floyd's algorithm, hash set
4. **Merging:** Two lists, k lists, sorted/unsorted
5. **Partitioning:** Value-based, position-based, pattern-based
6. **In-place Modification:** Pointer manipulation, no extra space
7. **Recursion:** Base cases, recursive calls, backtracking
8. **Dummy Nodes:** Simplify edge cases, temporary head
9. **Stack/Queue:** Order preservation, LIFO/FIFO operations
10. **Hash Maps:** Node mapping, value tracking, memoization

**Time Complexity Goals:**

- Most problems: O(n) or O(n log n)
- Space: O(1) for iterative, O(n) or O(log n) for recursive
- Always clarify if input can be modified

**Common Mistakes to Avoid:**

1. Not handling null/empty lists
2. Forgetting to update all pointers
3. Creating cycles accidentally
4. Off-by-one errors in counting
5. Memory leaks (not clearing references)
6. Not considering lists of length 1 or 2
7. Modifying input when not allowed
8. Infinite loops in cycle problems
