# Chapter 33: Trees - Exercises

## Instructions

- Try to solve each problem without looking at the solution first
- Start with Easy problems, then progress to Medium and Hard
- For each problem, analyze the time and space complexity
- Multiple approaches are encouraged - compare trade-offs

Solutions are available in `solutions.md`.

---

## Easy Problems

### E1: Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

```python
def max_depth(root: TreeNode) -> int:
    """
    Return maximum depth of binary tree.

    Example:
        Input:     3
                  / \
                 9  20
                   /  \
                  15   7
        Output: 3

    Args:
        root: Root of binary tree

    Returns:
        Maximum depth (number of nodes along longest path)
    """
    pass
```

---

### E2: Invert Binary Tree

Given the root of a binary tree, invert it (mirror it).

```python
def invert_tree(root: TreeNode) -> TreeNode:
    """
    Invert/mirror binary tree.

    Example:
        Input:     4              Output:     4
                  / \                        / \
                 2   7                      7   2
                / \ / \                    / \ / \
               1  3 6  9                  9  6 3  1

    Args:
        root: Root of binary tree

    Returns:
        Root of inverted tree
    """
    pass
```

---

### E3: Same Tree

Given roots of two binary trees p and q, check if they're identical.

```python
def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """
    Check if two trees are structurally identical with same values.

    Example:
        Input: p = [1,2,3], q = [1,2,3]
        Output: True

    Args:
        p: Root of first tree
        q: Root of second tree

    Returns:
        True if identical, False otherwise
    """
    pass
```

---

### E4: Symmetric Tree

Check if a binary tree is symmetric (mirror of itself).

```python
def is_symmetric(root: TreeNode) -> bool:
    """
    Check if tree is symmetric around its center.

    Example:
        Input:     1
                  / \
                 2   2
                / \ / \
               3  4 4  3
        Output: True

    Args:
        root: Root of binary tree

    Returns:
        True if symmetric, False otherwise
    """
    pass
```

---

### E5: Merge Two Binary Trees

Merge two binary trees by adding overlapping nodes' values.

```python
def merge_trees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    """
    Merge two binary trees.

    Example:
        Tree 1:    1          Tree 2:    2          Merged:    3
                  / \                   / \                   / \
                 3   2                 1   3                 4   5
                /                       \   \               / \   \
               5                         4   7             5   4   7

    Args:
        root1: Root of first tree
        root2: Root of second tree

    Returns:
        Root of merged tree
    """
    pass
```

---

### E6: Binary Tree Paths

Find all root-to-leaf paths in a binary tree.

```python
def binary_tree_paths(root: TreeNode) -> List[str]:
    """
    Return all root-to-leaf paths.

    Example:
        Input:   1
                / \
               2   3
                \
                 5
        Output: ["1->2->5", "1->3"]

    Args:
        root: Root of binary tree

    Returns:
        List of path strings
    """
    pass
```

---

### E7: Minimum Depth of Binary Tree

Find the minimum depth (shortest path from root to leaf).

```python
def min_depth(root: TreeNode) -> int:
    """
    Return minimum depth of binary tree.

    Example:
        Input:     3
                  / \
                 9  20
                   /  \
                  15   7
        Output: 2 (path 3→9)

    Args:
        root: Root of binary tree

    Returns:
        Minimum depth
    """
    pass
```

---

### E8: Balanced Binary Tree

Check if a binary tree is height-balanced (left and right subtree heights differ by at most 1 for all nodes).

```python
def is_balanced(root: TreeNode) -> bool:
    """
    Check if tree is height-balanced.

    Example:
        Input:     3
                  / \
                 9  20
                   /  \
                  15   7
        Output: True

    Args:
        root: Root of binary tree

    Returns:
        True if balanced, False otherwise
    """
    pass
```

---

## Medium Problems

### M1: Validate Binary Search Tree

Determine if a binary tree is a valid BST.

```python
def is_valid_bst(root: TreeNode) -> bool:
    """
    Validate if binary tree is valid BST.

    Example:
        Input:     2
                  / \
                 1   3
        Output: True

        Input:     5
                  / \
                 1   4
                    / \
                   3   6
        Output: False (3 < 5)

    Args:
        root: Root of binary tree

    Returns:
        True if valid BST, False otherwise
    """
    pass
```

---

### M2: Binary Tree Level Order Traversal

Return level-order traversal as list of lists.

```python
def level_order(root: TreeNode) -> List[List[int]]:
    """
    Level-order traversal (BFS).

    Example:
        Input:     3
                  / \
                 9  20
                   /  \
                  15   7
        Output: [[3], [9, 20], [15, 7]]

    Args:
        root: Root of binary tree

    Returns:
        List of lists (each inner list is one level)
    """
    pass
```

---

### M3: Binary Tree Zigzag Level Order Traversal

Return level-order traversal in zigzag pattern (left-to-right, then right-to-left, alternating).

```python
def zigzag_level_order(root: TreeNode) -> List[List[int]]:
    """
    Zigzag level-order traversal.

    Example:
        Input:     3
                  / \
                 9  20
                   /  \
                  15   7
        Output: [[3], [20, 9], [15, 7]]

    Args:
        root: Root of binary tree

    Returns:
        List of lists in zigzag order
    """
    pass
```

---

### M4: Construct Binary Tree from Preorder and Inorder

Build a binary tree from preorder and inorder traversal arrays.

```python
def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    Construct binary tree from traversals.

    Example:
        Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        Output:     3
                   / \
                  9  20
                    /  \
                   15   7

    Args:
        preorder: Preorder traversal
        inorder: Inorder traversal

    Returns:
        Root of constructed tree
    """
    pass
```

---

### M5: Path Sum II

Find all root-to-leaf paths where the sum equals target.

```python
def path_sum(root: TreeNode, target_sum: int) -> List[List[int]]:
    """
    Find all root-to-leaf paths with given sum.

    Example:
        Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
        Output: [[5,4,11,2], [5,8,4,5]]

    Args:
        root: Root of binary tree
        target_sum: Target path sum

    Returns:
        List of paths (each path is list of node values)
    """
    pass
```

---

### M6: Lowest Common Ancestor of BST

Find the lowest common ancestor of two nodes in a BST.

```python
def lowest_common_ancestor_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find LCA in BST.

    Example:
        Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
        Output: 6

    Args:
        root: Root of BST
        p: First node
        q: Second node

    Returns:
        LCA node
    """
    pass
```

---

### M7: Lowest Common Ancestor of Binary Tree

Find the lowest common ancestor of two nodes in a binary tree.

```python
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find LCA in binary tree.

    Example:
        Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
        Output: 3

    Args:
        root: Root of binary tree
        p: First node
        q: Second node

    Returns:
        LCA node
    """
    pass
```

---

### M8: Diameter of Binary Tree

Find the diameter (longest path between any two nodes).

```python
def diameter_of_binary_tree(root: TreeNode) -> int:
    """
    Find diameter of binary tree.

    Example:
        Input:     1
                  / \
                 2   3
                / \
               4   5
        Output: 3 (path 4→2→1→3 or 5→2→1→3)

    Args:
        root: Root of binary tree

    Returns:
        Diameter (number of edges in longest path)
    """
    pass
```

---

### M9: Binary Tree Right Side View

Return values of nodes you can see when viewing tree from the right side.

```python
def right_side_view(root: TreeNode) -> List[int]:
    """
    Return right side view of tree.

    Example:
        Input:     1
                  / \
                 2   3
                  \   \
                   5   4
        Output: [1, 3, 4]

    Args:
        root: Root of binary tree

    Returns:
        List of rightmost values at each level
    """
    pass
```

---

### M10: Kth Smallest Element in BST

Find the kth smallest element in a BST.

```python
def kth_smallest(root: TreeNode, k: int) -> int:
    """
    Find kth smallest element in BST.

    Example:
        Input: root = [3,1,4,null,2], k = 1
        Output: 1

    Args:
        root: Root of BST
        k: Position (1-indexed)

    Returns:
        kth smallest value
    """
    pass
```

---

## Hard Problems

### H1: Binary Tree Maximum Path Sum

Find the maximum path sum in a binary tree (path can start and end at any node).

```python
def max_path_sum(root: TreeNode) -> int:
    """
    Find maximum path sum.

    Example:
        Input:   -10
                 / \
                9  20
                  /  \
                 15   7
        Output: 42 (path 15→20→7)

    Args:
        root: Root of binary tree

    Returns:
        Maximum path sum
    """
    pass
```

---

### H2: Serialize and Deserialize Binary Tree

Design an algorithm to serialize and deserialize a binary tree.

```python
class Codec:
    """
    Serialize tree to string and deserialize back.

    Example:
        Input:     1
                  / \
                 2   3
                    / \
                   4   5
        Output: "1,2,null,null,3,4,null,null,5,null,null"
    """

    def serialize(self, root: TreeNode) -> str:
        """Encode tree to string."""
        pass

    def deserialize(self, data: str) -> TreeNode:
        """Decode string to tree."""
        pass
```

---

### H3: Binary Tree Cameras

Find minimum cameras needed to monitor all nodes (camera covers itself, parent, and children).

```python
def min_camera_cover(root: TreeNode) -> int:
    """
    Find minimum number of cameras to monitor all nodes.

    Example:
        Input:     0
                  / \
                 0   0
                    / \
                   0   0
        Output: 1 (place camera at root)

    Args:
        root: Root of binary tree

    Returns:
        Minimum number of cameras
    """
    pass
```

---

### H4: Recover Binary Search Tree

Two nodes of a BST are swapped by mistake. Recover the tree without changing its structure.

```python
def recover_tree(root: TreeNode) -> None:
    """
    Recover BST by swapping two nodes back.

    Example:
        Input:     3
                  / \
                 1   4
                    /
                   2
        Output:    2
                  / \
                 1   4
                    /
                   3

    Args:
        root: Root of BST (modified in-place)
    """
    pass
```

---

### H5: Vertical Order Traversal

Return vertical order traversal of binary tree (sorted by column, row, then value).

```python
def vertical_traversal(root: TreeNode) -> List[List[int]]:
    """
    Vertical order traversal.

    Example:
        Input:     3
                  / \
                 9  20
                   /  \
                  15   7
        Output: [[9], [3, 15], [20], [7]]

    Args:
        root: Root of binary tree

    Returns:
        List of lists (each list is one vertical column)
    """
    pass
```

---

## Bonus Challenges

### B1: Count Complete Tree Nodes

Count nodes in a complete binary tree (all levels filled except possibly last, which is filled left-to-right).

```python
def count_nodes(root: TreeNode) -> int:
    """
    Count nodes efficiently using complete tree property.
    Better than O(n).

    Args:
        root: Root of complete binary tree

    Returns:
        Number of nodes
    """
    pass
```

---

### B2: Maximum Width of Binary Tree

Find the maximum width (maximum number of nodes at any level, including null nodes).

```python
def width_of_binary_tree(root: TreeNode) -> int:
    """
    Find maximum width of binary tree.

    Example:
        Input:     1
                  / \
                 3   2
                / \   \
               5   3   9
        Output: 4 (level with 5, 3, null, 9)

    Args:
        root: Root of binary tree

    Returns:
        Maximum width
    """
    pass
```

---

### B3: All Nodes Distance K

Find all nodes at distance K from a target node.

```python
def distance_k(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    """
    Find all nodes at distance K from target.

    Example:
        Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
        Output: [7, 4, 1]

    Args:
        root: Root of binary tree
        target: Target node
        k: Distance

    Returns:
        List of node values at distance K
    """
    pass
```

---

## Summary

**Easy Problems (8)**: Basic tree operations and properties
- Focus on recursion, tree traversal, and simple tree properties

**Medium Problems (10)**: More complex tree algorithms
- BST validation, construction, LCA, level-order variations

**Hard Problems (5)**: Advanced tree algorithms
- Path sums with complex constraints, serialization, optimization problems

**Bonus Challenges (3)**: Interview favorites
- Exploit special tree properties for efficient solutions

### Recommended Practice Order

1. Start with Easy problems to build foundation
2. Master tree traversals (recursive and iterative)
3. Practice Medium problems focusing on BST and LCA
4. Attempt Hard problems after mastering Medium
5. Review solutions and understand different approaches

### Key Patterns to Master

- Recursive tree processing
- BFS using queue (level-order)
- DFS using stack (iterative)
- BST property exploitation
- Path tracking with accumulated values
- Bottom-up information gathering

Good luck with the exercises! 🌳
