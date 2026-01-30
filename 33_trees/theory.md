# Chapter 33: Trees - Theory

## Table of Contents
1. [Introduction to Trees](#introduction-to-trees)
2. [Tree Terminology](#tree-terminology)
3. [Types of Trees](#types-of-trees)
4. [Binary Trees](#binary-trees)
5. [Binary Search Trees (BST)](#binary-search-trees-bst)
6. [Tree Traversals](#tree-traversals)
7. [Common Tree Algorithms](#common-tree-algorithms)
8. [Time and Space Complexity](#time-and-space-complexity)

---

## Introduction to Trees

A **tree** is a hierarchical data structure consisting of nodes connected by edges. Unlike linear data structures (arrays, linked lists, stacks, queues), trees have a hierarchical parent-child relationship.

### Why Trees Matter

Trees are everywhere in computer science:
- **File systems**: Directories and files form a tree structure
- **Databases**: B-trees and B+ trees for efficient indexing
- **Compilers**: Parse trees represent program structure
- **AI**: Decision trees for classification
- **Networks**: Routing protocols use spanning trees
- **Web**: HTML DOM is a tree structure

### Tree Properties

1. **Hierarchical**: Clear parent-child relationships
2. **Recursive**: Each subtree is itself a tree
3. **Connected**: There's exactly one path between any two nodes
4. **Acyclic**: No cycles (unlike graphs)
5. **One Root**: Exactly one node with no parent (unless empty)

---

## Tree Terminology

Understanding tree terminology is crucial for discussing tree algorithms:

### Basic Terms

**Node**: An element in the tree containing data and references to children
```
      10        ← Node
     /  \
   5     15     ← Child nodes
```

**Root**: The topmost node (has no parent)
```
      10        ← Root
     /  \
   5     15
```

**Leaf (External Node)**: A node with no children
```
      10
     /  \
   5     15     ← 5 and 15 are leaves
```

**Internal Node**: A node with at least one child
```
      10        ← Internal node
     /  \
   5     15
  / \
 3   7          ← 5 is also internal, 3 and 7 are leaves
```

**Parent**: A node that has children
```
      10        ← Parent of 5 and 15
     /  \
   5     15
```

**Child**: A node that has a parent
```
      10
     /  \
   5     15     ← Children of 10
```

**Siblings**: Nodes that share the same parent
```
      10
     /  \
   5     15     ← 5 and 15 are siblings
```

**Ancestor**: A node on the path from root to that node
```
      10        ← Ancestor of all nodes
     /  \
   5     15     ← Ancestor of 3 and 7
  / \
 3   7
```

**Descendant**: A node reachable by following child links
```
      10
     /  \
   5     15     ← Descendants of 10
  / \
 3   7          ← Also descendants of 10
```

### Measurement Terms

**Edge**: Connection between two nodes
- A tree with n nodes has exactly n-1 edges

**Path**: Sequence of nodes connected by edges
```
      10
     /  \
   5     15
  /
 3
Path from 10 to 3: 10 → 5 → 3 (length 2)
```

**Height of a node**: Length of longest path from that node to a leaf
```
      10        ← Height 2
     /  \
   5     15     ← Height 1 (for node 5), Height 0 (for node 15)
  / \
 3   7          ← Height 0
```

**Height of a tree**: Height of the root node

**Depth of a node**: Length of path from root to that node
```
      10        ← Depth 0
     /  \
   5     15     ← Depth 1
  / \
 3   7          ← Depth 2
```

**Level**: All nodes at the same depth
```
Level 0:       10
Level 1:      /  \
            5     15
Level 2:   / \
          3   7
```

---

## Types of Trees

### General Tree
- Each node can have any number of children
```
       A
     / | \
    B  C  D
   /|  |
  E F  G
```

### Binary Tree
- Each node has at most two children (left and right)
```
      10
     /  \
   5     15
  / \
 3   7
```

### Binary Search Tree (BST)
- Binary tree with ordering property:
  - Left subtree values < node value
  - Right subtree values > node value
```
      10
     /  \
   5     15
  / \   /  \
 3   7 12  20
```

### Complete Binary Tree
- All levels filled except possibly the last
- Last level filled from left to right
```
      10
     /  \
   5     15      ← Complete
  / \   /
 3   7 12
```

### Full Binary Tree
- Every node has 0 or 2 children (no nodes with 1 child)
```
      10
     /  \
   5     15      ← Full
         /  \
       12    20
```

### Perfect Binary Tree
- All internal nodes have 2 children
- All leaves at the same level
```
      10
     /  \
   5     15      ← Perfect
  / \   /  \
 3   7 12  20
```

### Balanced Binary Tree
- Height of left and right subtrees differ by at most 1 for all nodes
```
      10
     /  \
   5     15      ← Balanced
  / \   /
 3   7 12
```

---

## Binary Trees

### Binary Tree Node Structure

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Properties of Binary Trees

**Maximum nodes at level L**: 2^L nodes
- Level 0: 2^0 = 1 node (root)
- Level 1: 2^1 = 2 nodes
- Level 2: 2^2 = 4 nodes
- Level L: 2^L nodes

**Maximum nodes in tree of height h**: 2^(h+1) - 1
- Height 0: 2^1 - 1 = 1 node
- Height 1: 2^2 - 1 = 3 nodes
- Height 2: 2^3 - 1 = 7 nodes

**Minimum height for n nodes**: ⌈log₂(n+1)⌉ - 1

**Relation between leaves (L) and internal nodes (I) with 2 children**:
- L = I + 1 (in a full binary tree)

---

## Binary Search Trees (BST)

### BST Property

For every node in a BST:
- **All values in left subtree** < node value
- **All values in right subtree** > node value
- Both left and right subtrees are also BSTs

```
        10              Valid BST
       /  \
      5    15
     / \   / \
    3   7 12 20

        10              Invalid BST
       /  \
      5    15
     / \   / \
    3  12 7  20         12 is in wrong subtree!
```

### BST Operations

#### 1. Search

```python
def search(root, target):
    """
    Search for target in BST.
    Time: O(log n) average, O(n) worst
    Space: O(h) for recursion stack
    """
    if not root or root.val == target:
        return root

    if target < root.val:
        return search(root.left, target)
    else:
        return search(root.right, target)
```

**Iterative version** (saves space):
```python
def search_iterative(root, target):
    """
    Iterative search.
    Time: O(log n) average, O(n) worst
    Space: O(1)
    """
    while root and root.val != target:
        if target < root.val:
            root = root.left
        else:
            root = root.right
    return root
```

#### 2. Insert

```python
def insert(root, val):
    """
    Insert value into BST.
    Time: O(log n) average, O(n) worst
    Space: O(h) for recursion
    """
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    # If val == root.val, we can choose to not insert duplicates

    return root
```

#### 3. Delete

Deletion is the most complex BST operation. Three cases:

**Case 1**: Node has no children (leaf)
- Simply remove it

**Case 2**: Node has one child
- Replace node with its child

**Case 3**: Node has two children
- Find inorder successor (smallest in right subtree)
- Replace node's value with successor's value
- Delete the successor

```python
def delete(root, val):
    """
    Delete value from BST.
    Time: O(log n) average, O(n) worst
    Space: O(h) for recursion
    """
    if not root:
        return None

    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        # Found the node to delete

        # Case 1 & 2: Node has 0 or 1 child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Case 3: Node has 2 children
        # Find inorder successor (smallest in right subtree)
        successor = find_min(root.right)
        root.val = successor.val
        root.right = delete(root.right, successor.val)

    return root

def find_min(node):
    """Find minimum value node in tree."""
    while node.left:
        node = node.left
    return node
```

### BST Validation

A common interview question: determine if a binary tree is a valid BST.

**Wrong approach**: Check if left < root < right (only checks immediate children)
```python
# WRONG!
def is_valid_bst_wrong(root):
    if not root:
        return True
    if root.left and root.left.val >= root.val:
        return False
    if root.right and root.right.val <= root.val:
        return False
    return is_valid_bst_wrong(root.left) and is_valid_bst_wrong(root.right)
```

**Correct approach**: Track valid range for each node
```python
def is_valid_bst(root):
    """
    Validate BST by tracking min/max bounds.
    Time: O(n)
    Space: O(h)
    """
    def validate(node, min_val, max_val):
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))
```

---

## Tree Traversals

Tree traversal means visiting all nodes in a specific order. There are two main categories:

### Depth-First Search (DFS)

DFS explores as far as possible along each branch before backtracking.

#### 1. Inorder Traversal (Left-Root-Right)

```python
def inorder(root):
    """
    Inorder: Left → Root → Right
    For BST, gives nodes in sorted order.
    Time: O(n), Space: O(h)
    """
    if not root:
        return []

    result = []
    result.extend(inorder(root.left))
    result.append(root.val)
    result.extend(inorder(root.right))
    return result
```

**Example**:
```
      10
     /  \
    5    15
   / \
  3   7

Inorder: 3, 5, 7, 10, 15  (sorted for BST!)
```

**Iterative** (using stack):
```python
def inorder_iterative(root):
    """
    Iterative inorder using stack.
    Time: O(n), Space: O(h)
    """
    result = []
    stack = []
    current = root

    while current or stack:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Process node
        current = stack.pop()
        result.append(current.val)

        # Move to right subtree
        current = current.right

    return result
```

#### 2. Preorder Traversal (Root-Left-Right)

```python
def preorder(root):
    """
    Preorder: Root → Left → Right
    Used for creating copy of tree, prefix expression.
    Time: O(n), Space: O(h)
    """
    if not root:
        return []

    result = [root.val]
    result.extend(preorder(root.left))
    result.extend(preorder(root.right))
    return result
```

**Example**:
```
      10
     /  \
    5    15
   / \
  3   7

Preorder: 10, 5, 3, 7, 15
```

#### 3. Postorder Traversal (Left-Right-Root)

```python
def postorder(root):
    """
    Postorder: Left → Right → Root
    Used for deleting tree, postfix expression.
    Time: O(n), Space: O(h)
    """
    if not root:
        return []

    result = []
    result.extend(postorder(root.left))
    result.extend(postorder(root.right))
    result.append(root.val)
    return result
```

**Example**:
```
      10
     /  \
    5    15
   / \
  3   7

Postorder: 3, 7, 5, 15, 10
```

### Breadth-First Search (BFS)

BFS explores all nodes at the current level before moving to the next level.

#### Level-Order Traversal

```python
from collections import deque

def level_order(root):
    """
    Level-order (BFS): Visit level by level.
    Time: O(n), Space: O(w) where w is max width
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
```

**Example**:
```
      10
     /  \
    5    15
   / \
  3   7

Level-order: 10, 5, 15, 3, 7
```

**Level-by-level** (return as list of lists):
```python
def level_order_by_level(root):
    """
    Return levels as separate lists.
    Time: O(n), Space: O(w)
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

Result: `[[10], [5, 15], [3, 7]]`

---

## Common Tree Algorithms

### 1. Tree Height/Depth

```python
def max_depth(root):
    """
    Calculate height of tree.
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

### 2. Count Nodes

```python
def count_nodes(root):
    """
    Count total nodes in tree.
    Time: O(n), Space: O(h)
    """
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

### 3. Check if Balanced

```python
def is_balanced(root):
    """
    Check if tree is balanced (height difference ≤ 1).
    Time: O(n), Space: O(h)
    """
    def check_height(node):
        if not node:
            return 0

        left_height = check_height(node.left)
        if left_height == -1:  # Left subtree not balanced
            return -1

        right_height = check_height(node.right)
        if right_height == -1:  # Right subtree not balanced
            return -1

        if abs(left_height - right_height) > 1:
            return -1  # Current node not balanced

        return 1 + max(left_height, right_height)

    return check_height(root) != -1
```

### 4. Lowest Common Ancestor (LCA)

For BST:
```python
def lowest_common_ancestor_bst(root, p, q):
    """
    LCA for BST using BST property.
    Time: O(h), Space: O(1)
    """
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
```

For general binary tree:
```python
def lowest_common_ancestor(root, p, q):
    """
    LCA for binary tree.
    Time: O(n), Space: O(h)
    """
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root  # p and q on different sides
    return left if left else right  # Both on same side
```

### 5. Path Sum

```python
def has_path_sum(root, target_sum):
    """
    Check if there's a root-to-leaf path with given sum.
    Time: O(n), Space: O(h)
    """
    if not root:
        return False

    if not root.left and not root.right:  # Leaf
        return root.val == target_sum

    target_sum -= root.val
    return (has_path_sum(root.left, target_sum) or
            has_path_sum(root.right, target_sum))
```

### 6. Invert Binary Tree

```python
def invert_tree(root):
    """
    Mirror/invert binary tree.
    Time: O(n), Space: O(h)
    """
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root
```

### 7. Diameter of Binary Tree

```python
def diameter_of_binary_tree(root):
    """
    Find diameter (longest path between any two nodes).
    Time: O(n), Space: O(h)
    """
    diameter = [0]  # Use list to modify in nested function

    def height(node):
        if not node:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        # Update diameter (path through this node)
        diameter[0] = max(diameter[0], left_height + right_height)

        return 1 + max(left_height, right_height)

    height(root)
    return diameter[0]
```

---

## Time and Space Complexity

### Binary Tree Operations

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Search | O(n) | O(h) | May need to visit all nodes |
| Insert | O(n) | O(h) | Finding position |
| Delete | O(n) | O(h) | Finding and removing node |
| Traversal | O(n) | O(h) | Visit every node once |
| Height | O(n) | O(h) | May need to check all nodes |

### BST Operations (Balanced)

| Operation | Average | Worst | Space |
|-----------|---------|-------|-------|
| Search | O(log n) | O(n) | O(h) |
| Insert | O(log n) | O(n) | O(h) |
| Delete | O(log n) | O(n) | O(h) |
| Min/Max | O(log n) | O(n) | O(1) iterative |
| Successor | O(log n) | O(n) | O(1) iterative |

**Note**: BST worst case O(n) occurs when tree degenerates into a linked list (all nodes on one side).

### Space Complexity Notes

- **Recursive algorithms**: O(h) space for call stack, where h is tree height
  - Balanced tree: h = O(log n)
  - Skewed tree: h = O(n)

- **BFS algorithms**: O(w) space for queue, where w is maximum width
  - Perfect binary tree: maximum width = n/2 at last level
  - Worst case: O(n)

---

## Summary

Trees are hierarchical data structures with one root and parent-child relationships:

**Key Points**:
1. Binary trees have at most 2 children per node
2. BSTs maintain ordering: left < root < right
3. Four main traversals: inorder, preorder, postorder, level-order
4. Most tree algorithms use recursion
5. Inorder traversal of BST gives sorted order
6. Tree height determines time/space complexity

**Common Patterns**:
- Recursive processing (most tree problems)
- Level-order traversal using queue (BFS)
- Inorder traversal using stack (DFS)
- Path tracking with accumulated values
- Bottom-up information gathering

**Interview Tips**:
- Draw examples to visualize the problem
- Consider edge cases: empty tree, single node, skewed tree
- Think recursively: solve for subtrees, combine results
- BST problems often use the ordering property
- Remember: inorder of BST = sorted array

Practice these concepts thoroughly - trees appear in approximately 30% of coding interviews!
