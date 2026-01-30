# Chapter 33: Trees - Examples

## Table of Contents
1. [Tree Node Implementation](#tree-node-implementation)
2. [BST Operations](#bst-operations)
3. [Tree Traversals](#tree-traversals)
4. [Common Tree Problems](#common-tree-problems)
5. [Path Problems](#path-problems)
6. [Tree Construction](#tree-construction)

---

## Tree Node Implementation

### Example 1: Basic Tree Node

```python
class TreeNode:
    """
    Basic binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left       # Left child
        self.right = right     # Right child

    def __repr__(self):
        return f"TreeNode({self.val})"


# Create a simple tree:
#       10
#      /  \
#     5    15

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
```

---

## BST Operations

### Example 2: Insert into BST

```python
def insert_bst(root, val):
    """
    Insert value into BST.

    Time: O(log n) average, O(n) worst
    Space: O(h) for recursion stack

    Args:
        root: Root of BST
        val: Value to insert

    Returns:
        Root of modified BST
    """
    # Base case: found position to insert
    if not root:
        return TreeNode(val)

    # Recursive case: navigate to correct position
    if val < root.val:
        root.left = insert_bst(root.left, val)
    elif val > root.val:
        root.right = insert_bst(root.right, val)
    # If val == root.val, don't insert duplicates

    return root


# Example usage:
root = None
values = [10, 5, 15, 3, 7, 12, 20]

for val in values:
    root = insert_bst(root, val)

# Resulting BST:
#       10
#      /  \
#     5    15
#    / \   / \
#   3   7 12 20
```

### Example 3: Search in BST

```python
def search_bst(root, target):
    """
    Search for target in BST.

    Time: O(log n) average, O(n) worst
    Space: O(h) for recursion

    Args:
        root: Root of BST
        target: Value to search for

    Returns:
        Node with target value, or None if not found
    """
    # Base cases
    if not root or root.val == target:
        return root

    # Recursive cases using BST property
    if target < root.val:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)


def search_bst_iterative(root, target):
    """
    Iterative search - better space complexity.

    Time: O(log n) average, O(n) worst
    Space: O(1)
    """
    while root and root.val != target:
        if target < root.val:
            root = root.left
        else:
            root = root.right
    return root


# Example usage:
result = search_bst(root, 7)
print(result)  # TreeNode(7)

result = search_bst_iterative(root, 25)
print(result)  # None (not found)
```

### Example 4: Delete from BST

```python
def delete_bst(root, val):
    """
    Delete value from BST.

    Three cases:
    1. Node has no children: simply remove
    2. Node has one child: replace with child
    3. Node has two children: replace with inorder successor

    Time: O(log n) average, O(n) worst
    Space: O(h) for recursion
    """
    if not root:
        return None

    # Find the node to delete
    if val < root.val:
        root.left = delete_bst(root.left, val)
    elif val > root.val:
        root.right = delete_bst(root.right, val)
    else:
        # Found node to delete

        # Case 1 & 2: Node has 0 or 1 child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Case 3: Node has 2 children
        # Find inorder successor (smallest in right subtree)
        successor = find_min(root.right)
        root.val = successor.val  # Replace value
        root.right = delete_bst(root.right, successor.val)  # Delete successor

    return root


def find_min(node):
    """Find minimum value node in tree (leftmost node)."""
    while node.left:
        node = node.left
    return node


# Example:
#       10
#      /  \
#     5    15
#    / \   / \
#   3   7 12 20
#
# Delete 15:
#       10
#      /  \
#     5    20
#    / \   /
#   3   7 12

root = delete_bst(root, 15)
```

### Example 5: Validate BST

```python
def is_valid_bst(root):
    """
    Check if binary tree is valid BST.

    Key insight: Track valid range for each node.
    - Left subtree: values must be in range (min_val, root.val)
    - Right subtree: values must be in range (root.val, max_val)

    Time: O(n) - visit each node once
    Space: O(h) - recursion stack
    """
    def validate(node, min_val, max_val):
        # Empty tree is valid
        if not node:
            return True

        # Check if current node violates constraints
        if node.val <= min_val or node.val >= max_val:
            return False

        # Recursively validate left and right subtrees
        # Left: values must be < node.val
        # Right: values must be > node.val
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))


# Example valid BST:
#       10
#      /  \
#     5    15
#    / \   / \
#   3   7 12 20

valid_root = TreeNode(10)
valid_root.left = TreeNode(5)
valid_root.right = TreeNode(15)
valid_root.left.left = TreeNode(3)
valid_root.left.right = TreeNode(7)
valid_root.right.left = TreeNode(12)
valid_root.right.right = TreeNode(20)

print(is_valid_bst(valid_root))  # True

# Example invalid BST:
#       10
#      /  \
#     5    15
#    / \   / \
#   3  12 7  20  ← 12 is in wrong subtree!

invalid_root = TreeNode(10)
invalid_root.left = TreeNode(5)
invalid_root.right = TreeNode(15)
invalid_root.left.left = TreeNode(3)
invalid_root.left.right = TreeNode(12)  # Invalid!
invalid_root.right.left = TreeNode(7)
invalid_root.right.right = TreeNode(20)

print(is_valid_bst(invalid_root))  # False
```

---

## Tree Traversals

### Example 6: All Four Traversals

```python
from collections import deque


def inorder_traversal(root):
    """
    Inorder: Left → Root → Right
    For BST, gives sorted order.

    Time: O(n), Space: O(h)
    """
    if not root:
        return []

    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.val)
    result.extend(inorder_traversal(root.right))
    return result


def preorder_traversal(root):
    """
    Preorder: Root → Left → Right
    Used for creating copy of tree.

    Time: O(n), Space: O(h)
    """
    if not root:
        return []

    result = [root.val]
    result.extend(preorder_traversal(root.left))
    result.extend(preorder_traversal(root.right))
    return result


def postorder_traversal(root):
    """
    Postorder: Left → Right → Root
    Used for deleting tree.

    Time: O(n), Space: O(h)
    """
    if not root:
        return []

    result = []
    result.extend(postorder_traversal(root.left))
    result.extend(postorder_traversal(root.right))
    result.append(root.val)
    return result


def level_order_traversal(root):
    """
    Level-order (BFS): Level by level.

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


# Example tree:
#       10
#      /  \
#     5    15
#    / \
#   3   7

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

print("Inorder:", inorder_traversal(root))      # [3, 5, 7, 10, 15]
print("Preorder:", preorder_traversal(root))    # [10, 5, 3, 7, 15]
print("Postorder:", postorder_traversal(root))  # [3, 7, 5, 15, 10]
print("Level-order:", level_order_traversal(root))  # [10, 5, 15, 3, 7]
```

### Example 7: Iterative Inorder Traversal

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


# Example:
print(inorder_iterative(root))  # [3, 5, 7, 10, 15]
```

### Example 8: Level-Order by Levels

```python
def level_order_by_level(root):
    """
    Return level-order as list of lists (each level separate).

    Time: O(n), Space: O(w)
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


# Example:
print(level_order_by_level(root))
# [[10], [5, 15], [3, 7]]
```

---

## Common Tree Problems

### Example 9: Maximum Depth

```python
def max_depth(root):
    """
    Calculate height/depth of tree.

    Time: O(n), Space: O(h)
    """
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


# Example:
#       10         Depth 3
#      /  \
#     5    15      Depth 2
#    / \
#   3   7          Depth 1

print(max_depth(root))  # 3
```

### Example 10: Invert Binary Tree

```python
def invert_tree(root):
    """
    Mirror/invert binary tree.

    Time: O(n), Space: O(h)
    """
    if not root:
        return None

    # Swap children
    root.left, root.right = root.right, root.left

    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root


# Before:
#       10
#      /  \
#     5    15
#    / \
#   3   7
#
# After:
#       10
#      /  \
#    15    5
#         / \
#        7   3

inverted = invert_tree(root)
print(level_order_traversal(inverted))  # [10, 15, 5, 7, 3]
```

### Example 11: Same Tree

```python
def is_same_tree(p, q):
    """
    Check if two trees are identical.

    Time: O(n), Space: O(h)
    """
    # Both empty
    if not p and not q:
        return True

    # One empty, one not
    if not p or not q:
        return False

    # Values differ
    if p.val != q.val:
        return False

    # Check both subtrees
    return (is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))


# Example:
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

print(is_same_tree(tree1, tree2))  # True
```

### Example 12: Symmetric Tree

```python
def is_symmetric(root):
    """
    Check if tree is symmetric (mirror of itself).

    Time: O(n), Space: O(h)
    """
    def is_mirror(left, right):
        # Both null
        if not left and not right:
            return True

        # One null, one not
        if not left or not right:
            return False

        # Values must match and subtrees must be mirrors
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))

    if not root:
        return True

    return is_mirror(root.left, root.right)


# Symmetric tree:
#       1
#      / \
#     2   2
#    / \ / \
#   3  4 4  3

sym_root = TreeNode(1)
sym_root.left = TreeNode(2)
sym_root.right = TreeNode(2)
sym_root.left.left = TreeNode(3)
sym_root.left.right = TreeNode(4)
sym_root.right.left = TreeNode(4)
sym_root.right.right = TreeNode(3)

print(is_symmetric(sym_root))  # True
```

### Example 13: Lowest Common Ancestor (BST)

```python
def lowest_common_ancestor_bst(root, p, q):
    """
    Find LCA in BST using BST property.

    Time: O(h), Space: O(1) iterative / O(h) recursive
    """
    while root:
        # Both in left subtree
        if p.val < root.val and q.val < root.val:
            root = root.left
        # Both in right subtree
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            # Split point - this is LCA
            return root


# Example BST:
#       10
#      /  \
#     5    15
#    / \   / \
#   3   7 12 20

bst = TreeNode(10)
bst.left = TreeNode(5)
bst.right = TreeNode(15)
bst.left.left = TreeNode(3)
bst.left.right = TreeNode(7)
bst.right.left = TreeNode(12)
bst.right.right = TreeNode(20)

lca = lowest_common_ancestor_bst(bst, bst.left.left, bst.left.right)
print(lca.val)  # 5 (LCA of 3 and 7)
```

### Example 14: Lowest Common Ancestor (Binary Tree)

```python
def lowest_common_ancestor(root, p, q):
    """
    Find LCA in general binary tree.

    Time: O(n), Space: O(h)
    """
    # Base cases
    if not root or root == p or root == q:
        return root

    # Search in left and right subtrees
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # If both found in different subtrees, current node is LCA
    if left and right:
        return root

    # Return whichever is not None (or None if both are None)
    return left if left else right


# Example:
lca = lowest_common_ancestor(bst, bst.left.left, bst.right.right)
print(lca.val)  # 10 (LCA of 3 and 20)
```

---

## Path Problems

### Example 15: Path Sum

```python
def has_path_sum(root, target_sum):
    """
    Check if there's a root-to-leaf path with given sum.

    Time: O(n), Space: O(h)
    """
    if not root:
        return False

    # Leaf node
    if not root.left and not root.right:
        return root.val == target_sum

    # Recurse with reduced target
    remaining = target_sum - root.val
    return (has_path_sum(root.left, remaining) or
            has_path_sum(root.right, remaining))


# Example:
#       10
#      /  \
#     5    15
#    / \
#   3   7

path_root = TreeNode(10)
path_root.left = TreeNode(5)
path_root.right = TreeNode(15)
path_root.left.left = TreeNode(3)
path_root.left.right = TreeNode(7)

print(has_path_sum(path_root, 18))  # True (10→5→3)
print(has_path_sum(path_root, 25))  # True (10→15)
print(has_path_sum(path_root, 30))  # False
```

### Example 16: All Root-to-Leaf Paths

```python
def binary_tree_paths(root):
    """
    Find all root-to-leaf paths.

    Time: O(n), Space: O(h)
    """
    if not root:
        return []

    # Leaf node
    if not root.left and not root.right:
        return [str(root.val)]

    paths = []

    # Get paths from left subtree
    for path in binary_tree_paths(root.left):
        paths.append(str(root.val) + "->" + path)

    # Get paths from right subtree
    for path in binary_tree_paths(root.right):
        paths.append(str(root.val) + "->" + path)

    return paths


# Example:
print(binary_tree_paths(path_root))
# ['10->5->3', '10->5->7', '10->15']
```

---

## Tree Construction

### Example 17: Build Tree from Inorder and Preorder

```python
def build_tree_from_inorder_preorder(preorder, inorder):
    """
    Construct binary tree from preorder and inorder traversals.

    Key insight:
    - Preorder[0] is root
    - Everything left of root in inorder is left subtree
    - Everything right of root in inorder is right subtree

    Time: O(n), Space: O(n)
    """
    if not preorder or not inorder:
        return None

    # First element in preorder is root
    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find root position in inorder
    mid = inorder.index(root_val)

    # Recursively build subtrees
    # Left subtree: next mid elements in preorder, first mid in inorder
    root.left = build_tree_from_inorder_preorder(preorder[1:mid+1], inorder[:mid])
    # Right subtree: remaining in preorder, after mid in inorder
    root.right = build_tree_from_inorder_preorder(preorder[mid+1:], inorder[mid+1:])

    return root


# Example:
preorder = [10, 5, 3, 7, 15]
inorder = [3, 5, 7, 10, 15]

constructed = build_tree_from_inorder_preorder(preorder, inorder)
print(level_order_traversal(constructed))  # [10, 5, 15, 3, 7]
```

---

## Summary

These examples demonstrate:

1. **BST Operations**: Insert, search, delete, validate
2. **Traversals**: Inorder, preorder, postorder, level-order (both recursive and iterative)
3. **Common Problems**: Depth, inversion, tree comparison, symmetry
4. **LCA**: Both BST and general binary tree approaches
5. **Path Problems**: Path sum, all paths
6. **Construction**: Building trees from traversals

**Key Techniques**:
- Recursion for most tree problems
- Queue for BFS (level-order)
- Stack for iterative DFS
- BST property for optimization
- Tracking ranges/paths for validation

Practice these examples until you can implement them from memory!
