# Chapter 33: Trees - Solutions

This document contains detailed solutions for all tree exercises, organized by difficulty level.

---

## Easy Problems

### E1: Maximum Depth of Binary Tree

**Problem**: Find the maximum depth of a binary tree.

**Approach**: Use recursion to compute depth as 1 + max of left and right subtree depths.

```python
def max_depth(root: TreeNode) -> int:
    """
    Return maximum depth of binary tree.

    Time: O(n) - visit each node once
    Space: O(h) - recursion stack where h is height
    """
    # Base case: empty tree has depth 0
    if not root:
        return 0

    # Recursively find depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # Current depth is 1 + max of subtree depths
    return 1 + max(left_depth, right_depth)
```

**Alternative Iterative Approach (BFS)**:

```python
def max_depth_iterative(root: TreeNode) -> int:
    """
    Iterative approach using level-order traversal.

    Time: O(n)
    Space: O(w) where w is maximum width
    """
    if not root:
        return 0

    from collections import deque
    queue = deque([root])
    depth = 0

    while queue:
        depth += 1
        # Process all nodes at current level
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth
```

**Time Complexity**: O(n) - must visit every node
**Space Complexity**: O(h) recursive, O(w) iterative where h=height, w=max width

---

### E2: Invert Binary Tree

**Problem**: Invert/mirror a binary tree.

**Approach**: Recursively swap left and right children at each node.

```python
def invert_tree(root: TreeNode) -> TreeNode:
    """
    Invert/mirror binary tree.

    Time: O(n) - visit each node once
    Space: O(h) - recursion stack
    """
    # Base case: empty tree stays empty
    if not root:
        return None

    # Swap left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root
```

**Alternative Iterative Approach**:

```python
def invert_tree_iterative(root: TreeNode) -> TreeNode:
    """
    Iterative approach using queue.

    Time: O(n)
    Space: O(w) where w is maximum width
    """
    if not root:
        return None

    from collections import deque
    queue = deque([root])

    while queue:
        node = queue.popleft()

        # Swap children
        node.left, node.right = node.right, node.left

        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root
```

**Time Complexity**: O(n)
**Space Complexity**: O(h) recursive, O(w) iterative

---

### E3: Same Tree

**Problem**: Check if two binary trees are identical.

**Approach**: Recursively compare structure and values.

```python
def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """
    Check if two trees are structurally identical with same values.

    Time: O(min(n, m)) where n, m are sizes of trees
    Space: O(min(h1, h2)) for recursion
    """
    # Both empty - identical
    if not p and not q:
        return True

    # One empty, one not - different
    if not p or not q:
        return False

    # Check current node values and recursively check subtrees
    return (p.val == q.val and
            is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))
```

**Alternative Iterative Approach**:

```python
def is_same_tree_iterative(p: TreeNode, q: TreeNode) -> bool:
    """
    Iterative approach using stack.

    Time: O(min(n, m))
    Space: O(min(h1, h2))
    """
    stack = [(p, q)]

    while stack:
        node1, node2 = stack.pop()

        # Both None - continue
        if not node1 and not node2:
            continue

        # One None - not same
        if not node1 or not node2:
            return False

        # Different values - not same
        if node1.val != node2.val:
            return False

        # Add children to stack
        stack.append((node1.left, node2.left))
        stack.append((node1.right, node2.right))

    return True
```

**Time Complexity**: O(min(n, m)) - stops at first difference
**Space Complexity**: O(min(h1, h2))

---

### E4: Symmetric Tree

**Problem**: Check if a binary tree is symmetric around its center.

**Approach**: Create helper function to check if two subtrees are mirrors.

```python
def is_symmetric(root: TreeNode) -> bool:
    """
    Check if tree is symmetric around its center.

    Time: O(n) - visit each node once
    Space: O(h) - recursion stack
    """
    def is_mirror(left: TreeNode, right: TreeNode) -> bool:
        """Check if two subtrees are mirrors."""
        # Both empty - symmetric
        if not left and not right:
            return True

        # One empty - not symmetric
        if not left or not right:
            return False

        # Check values and recursively check mirrored subtrees
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))

    # Empty tree is symmetric
    if not root:
        return True

    # Check if left and right subtrees are mirrors
    return is_mirror(root.left, root.right)
```

**Alternative Iterative Approach**:

```python
def is_symmetric_iterative(root: TreeNode) -> bool:
    """
    Iterative approach using queue.

    Time: O(n)
    Space: O(w) where w is maximum width
    """
    if not root:
        return True

    from collections import deque
    queue = deque([(root.left, root.right)])

    while queue:
        left, right = queue.popleft()

        if not left and not right:
            continue

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        # Add mirrored pairs
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))

    return True
```

**Time Complexity**: O(n)
**Space Complexity**: O(h) recursive, O(w) iterative

---

### E5: Merge Two Binary Trees

**Problem**: Merge two binary trees by summing overlapping node values.

**Approach**: Recursively merge corresponding nodes.

```python
def merge_trees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    """
    Merge two binary trees.

    Time: O(min(n, m)) where n, m are sizes
    Space: O(min(h1, h2)) for recursion
    """
    # If one tree is empty, return the other
    if not root1:
        return root2
    if not root2:
        return root1

    # Create new node with sum of values
    merged = TreeNode(root1.val + root2.val)

    # Recursively merge subtrees
    merged.left = merge_trees(root1.left, root2.left)
    merged.right = merge_trees(root1.right, root2.right)

    return merged
```

**Alternative In-place Modification**:

```python
def merge_trees_inplace(root1: TreeNode, root2: TreeNode) -> TreeNode:
    """
    Merge into root1 (modifies root1).

    Time: O(min(n, m))
    Space: O(min(h1, h2))
    """
    if not root1:
        return root2
    if not root2:
        return root1

    # Modify root1 in place
    root1.val += root2.val
    root1.left = merge_trees_inplace(root1.left, root2.left)
    root1.right = merge_trees_inplace(root1.right, root2.right)

    return root1
```

**Iterative Approach**:

```python
def merge_trees_iterative(root1: TreeNode, root2: TreeNode) -> TreeNode:
    """
    Iterative approach using stack.

    Time: O(min(n, m))
    Space: O(min(h1, h2))
    """
    if not root1:
        return root2
    if not root2:
        return root1

    stack = [(root1, root2)]

    while stack:
        node1, node2 = stack.pop()

        if not node1 or not node2:
            continue

        # Merge values
        node1.val += node2.val

        # Handle left children
        if not node1.left:
            node1.left = node2.left
        else:
            stack.append((node1.left, node2.left))

        # Handle right children
        if not node1.right:
            node1.right = node2.right
        else:
            stack.append((node1.right, node2.right))

    return root1
```

**Time Complexity**: O(min(n, m))
**Space Complexity**: O(min(h1, h2))

---

### E6: Binary Tree Paths

**Problem**: Find all root-to-leaf paths.

**Approach**: Use DFS with path tracking.

```python
def binary_tree_paths(root: TreeNode) -> List[str]:
    """
    Return all root-to-leaf paths.

    Time: O(n) - visit each node once
    Space: O(h) for recursion + O(n) for paths
    """
    def dfs(node: TreeNode, path: str, paths: List[str]):
        """Helper to perform DFS and collect paths."""
        if not node:
            return

        # Add current node to path
        path += str(node.val)

        # If leaf node, add complete path
        if not node.left and not node.right:
            paths.append(path)
        else:
            # Continue building path
            path += "->"
            dfs(node.left, path, paths)
            dfs(node.right, path, paths)

    paths = []
    dfs(root, "", paths)
    return paths
```

**Alternative Approach with List Path**:

```python
def binary_tree_paths_alt(root: TreeNode) -> List[str]:
    """
    Using list to build path (easier to backtrack).

    Time: O(n)
    Space: O(h) for recursion + O(n) for paths
    """
    def dfs(node: TreeNode, path: List[int], paths: List[str]):
        if not node:
            return

        # Add current node
        path.append(node.val)

        # If leaf, add path string
        if not node.left and not node.right:
            paths.append("->".join(map(str, path)))
        else:
            dfs(node.left, path, paths)
            dfs(node.right, path, paths)

        # Backtrack
        path.pop()

    paths = []
    dfs(root, [], paths)
    return paths
```

**Iterative Approach**:

```python
def binary_tree_paths_iterative(root: TreeNode) -> List[str]:
    """
    Iterative approach using stack.

    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []

    paths = []
    stack = [(root, str(root.val))]

    while stack:
        node, path = stack.pop()

        # If leaf, add path
        if not node.left and not node.right:
            paths.append(path)

        # Add children with updated paths
        if node.right:
            stack.append((node.right, path + "->" + str(node.right.val)))
        if node.left:
            stack.append((node.left, path + "->" + str(node.left.val)))

    return paths
```

**Time Complexity**: O(n)
**Space Complexity**: O(h) for recursion + O(n*h) for storing paths

---

### E7: Minimum Depth of Binary Tree

**Problem**: Find the minimum depth (shortest path from root to leaf).

**Approach**: Use BFS for optimal solution (stops at first leaf).

```python
def min_depth(root: TreeNode) -> int:
    """
    Return minimum depth using BFS (optimal).

    Time: O(n) worst case, but often much faster
    Space: O(w) where w is maximum width
    """
    if not root:
        return 0

    from collections import deque
    queue = deque([(root, 1)])

    while queue:
        node, depth = queue.popleft()

        # If leaf node, return depth (first leaf found is minimum)
        if not node.left and not node.right:
            return depth

        # Add children with incremented depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return 0
```

**Recursive Approach**:

```python
def min_depth_recursive(root: TreeNode) -> int:
    """
    Recursive approach (visits all nodes).

    Time: O(n)
    Space: O(h)
    """
    if not root:
        return 0

    # If one child is missing, only consider the other
    if not root.left:
        return 1 + min_depth_recursive(root.right)
    if not root.right:
        return 1 + min_depth_recursive(root.left)

    # Both children exist - take minimum
    return 1 + min(min_depth_recursive(root.left),
                   min_depth_recursive(root.right))
```

**Time Complexity**: O(n) worst case, O(w) average for BFS
**Space Complexity**: O(w) for BFS, O(h) for recursive

**Note**: BFS is preferred for minimum depth as it stops at first leaf.

---

### E8: Balanced Binary Tree

**Problem**: Check if tree is height-balanced (subtree heights differ by at most 1).

**Approach**: Use bottom-up recursion to check balance and compute heights simultaneously.

```python
def is_balanced(root: TreeNode) -> bool:
    """
    Check if tree is height-balanced.

    Time: O(n) - visit each node once
    Space: O(h) - recursion stack
    """
    def check_height(node: TreeNode) -> int:
        """
        Return height if balanced, -1 if unbalanced.
        """
        if not node:
            return 0

        # Check left subtree
        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        # Check right subtree
        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        # Check if current node is balanced
        if abs(left_height - right_height) > 1:
            return -1

        # Return height
        return 1 + max(left_height, right_height)

    return check_height(root) != -1
```

**Alternative Approach with Tuple**:

```python
def is_balanced_alt(root: TreeNode) -> bool:
    """
    Return (is_balanced, height) tuple.

    Time: O(n)
    Space: O(h)
    """
    def check(node: TreeNode) -> tuple:
        """Return (is_balanced, height)."""
        if not node:
            return (True, 0)

        left_balanced, left_height = check(node.left)
        if not left_balanced:
            return (False, 0)

        right_balanced, right_height = check(node.right)
        if not right_balanced:
            return (False, 0)

        balanced = abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)

        return (balanced, height)

    return check(root)[0]
```

**Time Complexity**: O(n) - each node visited once
**Space Complexity**: O(h) - recursion stack

---

## Medium Problems

### M1: Validate Binary Search Tree

**Problem**: Determine if a binary tree is a valid BST.

**Approach**: Use range checking - each node must be within valid range.

```python
def is_valid_bst(root: TreeNode) -> bool:
    """
    Validate if binary tree is valid BST.

    Time: O(n) - visit each node once
    Space: O(h) - recursion stack
    """
    def validate(node: TreeNode, min_val: float, max_val: float) -> bool:
        """Check if node is within valid range."""
        if not node:
            return True

        # Check if current node violates BST property
        if node.val <= min_val or node.val >= max_val:
            return False

        # Recursively validate subtrees with updated ranges
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))
```

**Inorder Traversal Approach**:

```python
def is_valid_bst_inorder(root: TreeNode) -> bool:
    """
    Using inorder traversal (should be strictly increasing).

    Time: O(n)
    Space: O(h)
    """
    def inorder(node: TreeNode) -> bool:
        """Perform inorder traversal and check ordering."""
        if not node:
            return True

        # Check left subtree
        if not inorder(node.left):
            return False

        # Check current node against previous
        if node.val <= inorder.prev:
            return False
        inorder.prev = node.val

        # Check right subtree
        return inorder(node.right)

    inorder.prev = float('-inf')
    return inorder(root)
```

**Iterative Inorder Approach**:

```python
def is_valid_bst_iterative(root: TreeNode) -> bool:
    """
    Iterative inorder traversal.

    Time: O(n)
    Space: O(h)
    """
    stack = []
    prev = float('-inf')
    current = root

    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Process node
        current = stack.pop()

        # Check if strictly increasing
        if current.val <= prev:
            return False
        prev = current.val

        # Move to right subtree
        current = current.right

    return True
```

**Time Complexity**: O(n)
**Space Complexity**: O(h)

---

### M2: Binary Tree Level Order Traversal

**Problem**: Return level-order traversal as list of lists.

**Approach**: Use BFS with queue.

```python
def level_order(root: TreeNode) -> List[List[int]]:
    """
    Level-order traversal (BFS).

    Time: O(n) - visit each node once
    Space: O(w) where w is maximum width
    """
    if not root:
        return []

    from collections import deque
    result = []
    queue = deque([root])

    while queue:
        level = []
        level_size = len(queue)

        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

**Recursive Approach**:

```python
def level_order_recursive(root: TreeNode) -> List[List[int]]:
    """
    Recursive approach using DFS with level tracking.

    Time: O(n)
    Space: O(h)
    """
    def dfs(node: TreeNode, level: int, result: List[List[int]]):
        if not node:
            return

        # Create new level list if needed
        if level >= len(result):
            result.append([])

        # Add current node to its level
        result[level].append(node.val)

        # Recursively process children
        dfs(node.left, level + 1, result)
        dfs(node.right, level + 1, result)

    result = []
    dfs(root, 0, result)
    return result
```

**Time Complexity**: O(n)
**Space Complexity**: O(w) for BFS, O(h) for recursive

---

### M3: Binary Tree Zigzag Level Order Traversal

**Problem**: Return level-order traversal in zigzag pattern.

**Approach**: BFS with alternating direction flag.

```python
def zigzag_level_order(root: TreeNode) -> List[List[int]]:
    """
    Zigzag level-order traversal.

    Time: O(n) - visit each node once
    Space: O(w) where w is maximum width
    """
    if not root:
        return []

    from collections import deque
    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Reverse level if going right to left
        if not left_to_right:
            level.reverse()

        result.append(level)
        left_to_right = not left_to_right

    return result
```

**Alternative with Deque for Bidirectional Insertion**:

```python
def zigzag_level_order_deque(root: TreeNode) -> List[List[int]]:
    """
    Using deque for efficient reversal.

    Time: O(n)
    Space: O(w)
    """
    if not root:
        return []

    from collections import deque
    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level = deque()
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            # Add to left or right based on direction
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level))
        left_to_right = not left_to_right

    return result
```

**Time Complexity**: O(n)
**Space Complexity**: O(w)

---

### M4: Construct Binary Tree from Preorder and Inorder

**Problem**: Build binary tree from preorder and inorder traversals.

**Approach**: Use preorder to identify root, inorder to split left/right subtrees.

```python
def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    Construct binary tree from traversals.

    Time: O(n) with hashmap optimization
    Space: O(n) for hashmap and recursion
    """
    # Build hashmap for O(1) lookup of inorder indices
    inorder_map = {val: idx for idx, val in enumerate(inorder)}

    def build(pre_start: int, pre_end: int, in_start: int, in_end: int) -> TreeNode:
        """Build tree from subarray ranges."""
        if pre_start > pre_end or in_start > in_end:
            return None

        # First element in preorder is root
        root_val = preorder[pre_start]
        root = TreeNode(root_val)

        # Find root position in inorder
        in_root_idx = inorder_map[root_val]

        # Calculate left subtree size
        left_size = in_root_idx - in_start

        # Recursively build left and right subtrees
        root.left = build(
            pre_start + 1,
            pre_start + left_size,
            in_start,
            in_root_idx - 1
        )
        root.right = build(
            pre_start + left_size + 1,
            pre_end,
            in_root_idx + 1,
            in_end
        )

        return root

    return build(0, len(preorder) - 1, 0, len(inorder) - 1)
```

**Alternative Simplified Approach**:

```python
def build_tree_simple(preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    Simpler implementation using list slicing.

    Time: O(n^2) due to slicing
    Space: O(n^2) due to slicing
    """
    if not preorder or not inorder:
        return None

    # Root is first element in preorder
    root = TreeNode(preorder[0])

    # Find root in inorder to split subtrees
    mid = inorder.index(root.val)

    # Recursively build subtrees
    root.left = build_tree_simple(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree_simple(preorder[mid+1:], inorder[mid+1:])

    return root
```

**Time Complexity**: O(n) with hashmap, O(n^2) with list slicing
**Space Complexity**: O(n) with hashmap, O(n^2) with slicing

---

### M5: Path Sum II

**Problem**: Find all root-to-leaf paths with given sum.

**Approach**: DFS with path tracking and backtracking.

```python
def path_sum(root: TreeNode, target_sum: int) -> List[List[int]]:
    """
    Find all root-to-leaf paths with given sum.

    Time: O(n) - visit each node once
    Space: O(h) for recursion + O(k*h) for k paths
    """
    def dfs(node: TreeNode, remaining: int, path: List[int], result: List[List[int]]):
        """DFS with path tracking."""
        if not node:
            return

        # Add current node to path
        path.append(node.val)
        remaining -= node.val

        # If leaf and sum matches, add path
        if not node.left and not node.right and remaining == 0:
            result.append(path[:])  # Make a copy

        # Recursively explore children
        dfs(node.left, remaining, path, result)
        dfs(node.right, remaining, path, result)

        # Backtrack
        path.pop()

    result = []
    dfs(root, target_sum, [], result)
    return result
```

**Iterative Approach**:

```python
def path_sum_iterative(root: TreeNode, target_sum: int) -> List[List[int]]:
    """
    Iterative approach using stack.

    Time: O(n)
    Space: O(h)
    """
    if not root:
        return []

    result = []
    stack = [(root, [root.val], root.val)]

    while stack:
        node, path, current_sum = stack.pop()

        # If leaf and sum matches
        if not node.left and not node.right and current_sum == target_sum:
            result.append(path)

        # Add children with updated paths
        if node.right:
            stack.append((
                node.right,
                path + [node.right.val],
                current_sum + node.right.val
            ))
        if node.left:
            stack.append((
                node.left,
                path + [node.left.val],
                current_sum + node.left.val
            ))

    return result
```

**Time Complexity**: O(n)
**Space Complexity**: O(h) for recursion + O(k*h) for storing k paths

---

### M6: Lowest Common Ancestor of BST

**Problem**: Find LCA of two nodes in a BST.

**Approach**: Use BST property - split point is LCA.

```python
def lowest_common_ancestor_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find LCA in BST.

    Time: O(h) where h is height
    Space: O(1) iterative, O(h) recursive
    """
    # Ensure p <= q for easier comparison
    if p.val > q.val:
        p, q = q, p

    current = root

    while current:
        # Both nodes in left subtree
        if current.val > q.val:
            current = current.left
        # Both nodes in right subtree
        elif current.val < p.val:
            current = current.right
        # Split point - this is LCA
        else:
            return current

    return None
```

**Recursive Approach**:

```python
def lowest_common_ancestor_bst_recursive(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Recursive approach.

    Time: O(h)
    Space: O(h)
    """
    # Both in left subtree
    if root.val > p.val and root.val > q.val:
        return lowest_common_ancestor_bst_recursive(root.left, p, q)

    # Both in right subtree
    if root.val < p.val and root.val < q.val:
        return lowest_common_ancestor_bst_recursive(root.right, p, q)

    # Split point - this is LCA
    return root
```

**Time Complexity**: O(h) - follows one path down
**Space Complexity**: O(1) iterative, O(h) recursive

---

### M7: Lowest Common Ancestor of Binary Tree

**Problem**: Find LCA of two nodes in a binary tree.

**Approach**: Bottom-up search - first node to have both p and q in subtrees.

```python
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find LCA in binary tree.

    Time: O(n) - may need to visit all nodes
    Space: O(h) - recursion stack
    """
    # Base case: reached leaf or found one of the nodes
    if not root or root == p or root == q:
        return root

    # Search in left and right subtrees
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # If both subtrees return non-null, current node is LCA
    if left and right:
        return root

    # Otherwise, return whichever is non-null
    return left if left else right
```

**Alternative with Parent Pointers**:

```python
def lowest_common_ancestor_with_parent(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Using parent pointers (if available).

    Time: O(h)
    Space: O(h)
    """
    # Build path from p to root
    ancestors = set()
    current = p
    while current:
        ancestors.add(current)
        current = current.parent  # Assumes parent pointer exists

    # Find first common ancestor from q to root
    current = q
    while current:
        if current in ancestors:
            return current
        current = current.parent

    return None
```

**Time Complexity**: O(n)
**Space Complexity**: O(h)

---

### M8: Diameter of Binary Tree

**Problem**: Find the longest path between any two nodes.

**Approach**: At each node, diameter through node is left_height + right_height.

```python
def diameter_of_binary_tree(root: TreeNode) -> int:
    """
    Find diameter of binary tree.

    Time: O(n) - visit each node once
    Space: O(h) - recursion stack
    """
    def height(node: TreeNode) -> int:
        """Return height and update max diameter."""
        if not node:
            return 0

        # Get heights of subtrees
        left_height = height(node.left)
        right_height = height(node.right)

        # Update diameter (path through current node)
        height.diameter = max(height.diameter, left_height + right_height)

        # Return height of current subtree
        return 1 + max(left_height, right_height)

    height.diameter = 0
    height(root)
    return height.diameter
```

**Alternative with Tuple Return**:

```python
def diameter_of_binary_tree_alt(root: TreeNode) -> int:
    """
    Return (diameter, height) tuple.

    Time: O(n)
    Space: O(h)
    """
    def dfs(node: TreeNode) -> tuple:
        """Return (diameter, height)."""
        if not node:
            return (0, 0)

        left_diameter, left_height = dfs(node.left)
        right_diameter, right_height = dfs(node.right)

        # Diameter is max of:
        # 1. Left subtree diameter
        # 2. Right subtree diameter
        # 3. Path through current node
        diameter = max(
            left_diameter,
            right_diameter,
            left_height + right_height
        )

        height = 1 + max(left_height, right_height)

        return (diameter, height)

    return dfs(root)[0]
```

**Time Complexity**: O(n)
**Space Complexity**: O(h)

---

### M9: Binary Tree Right Side View

**Problem**: Return values visible from right side.

**Approach**: BFS level-order, take last node at each level.

```python
def right_side_view(root: TreeNode) -> List[int]:
    """
    Return right side view of tree.

    Time: O(n) - visit each node once
    Space: O(w) where w is maximum width
    """
    if not root:
        return []

    from collections import deque
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # Last node in level is rightmost
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
```

**DFS Approach**:

```python
def right_side_view_dfs(root: TreeNode) -> List[int]:
    """
    DFS approach - visit right subtree first.

    Time: O(n)
    Space: O(h)
    """
    def dfs(node: TreeNode, level: int, result: List[int]):
        if not node:
            return

        # First time visiting this level - add node
        if level == len(result):
            result.append(node.val)

        # Visit right subtree first
        dfs(node.right, level + 1, result)
        dfs(node.left, level + 1, result)

    result = []
    dfs(root, 0, result)
    return result
```

**Time Complexity**: O(n)
**Space Complexity**: O(w) for BFS, O(h) for DFS

---

### M10: Kth Smallest Element in BST

**Problem**: Find kth smallest element in BST.

**Approach**: Inorder traversal gives sorted order.

```python
def kth_smallest(root: TreeNode, k: int) -> int:
    """
    Find kth smallest element in BST.

    Time: O(h + k) where h is height
    Space: O(h) for stack
    """
    stack = []
    current = root
    count = 0

    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Process node
        current = stack.pop()
        count += 1

        # If kth element, return it
        if count == k:
            return current.val

        # Move to right subtree
        current = current.right

    return -1
```

**Recursive Approach**:

```python
def kth_smallest_recursive(root: TreeNode, k: int) -> int:
    """
    Recursive inorder traversal.

    Time: O(h + k)
    Space: O(h)
    """
    def inorder(node: TreeNode) -> int:
        if not node:
            return None

        # Search left subtree
        result = inorder(node.left)
        if result is not None:
            return result

        # Process current node
        inorder.count += 1
        if inorder.count == k:
            return node.val

        # Search right subtree
        return inorder(node.right)

    inorder.count = 0
    return inorder(root)
```

**With Augmented BST (Follow-up)**:

```python
class TreeNodeWithCount:
    """BST node with subtree size for O(h) kth smallest."""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_count = 0  # Number of nodes in left subtree

def kth_smallest_optimized(root: TreeNodeWithCount, k: int) -> int:
    """
    Using augmented BST with subtree counts.

    Time: O(h)
    Space: O(1)
    """
    current = root

    while current:
        left_count = current.left_count

        if k == left_count + 1:
            return current.val
        elif k <= left_count:
            current = current.left
        else:
            k -= left_count + 1
            current = current.right

    return -1
```

**Time Complexity**: O(h + k) standard, O(h) with augmentation
**Space Complexity**: O(h)

---

## Hard Problems

### H1: Binary Tree Maximum Path Sum

**Problem**: Find maximum path sum (path can start/end anywhere).

**Approach**: At each node, calculate max path through it and update global max.

```python
def max_path_sum(root: TreeNode) -> int:
    """
    Find maximum path sum.

    Time: O(n) - visit each node once
    Space: O(h) - recursion stack
    """
    def max_gain(node: TreeNode) -> int:
        """
        Return max gain from this node downward.
        Update global max with path through this node.
        """
        if not node:
            return 0

        # Max gain from left and right (ignore negative paths)
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        # Path through current node
        path_sum = node.val + left_gain + right_gain

        # Update global maximum
        max_gain.max_sum = max(max_gain.max_sum, path_sum)

        # Return max gain going through this node
        # (can only use one branch)
        return node.val + max(left_gain, right_gain)

    max_gain.max_sum = float('-inf')
    max_gain(root)
    return max_gain.max_sum
```

**Explanation**:
- At each node, we have 4 options:
  1. Node only
  2. Node + left path
  3. Node + right path
  4. Node + left path + right path (for max_sum only)
- We return max of options 1-3 (single path going down)
- We update global max with option 4 (path through node)

**Time Complexity**: O(n)
**Space Complexity**: O(h)

---

### H2: Serialize and Deserialize Binary Tree

**Problem**: Convert tree to string and back.

**Approach**: Use preorder traversal with null markers.

```python
class Codec:
    """
    Serialize tree to string and deserialize back.

    Time: O(n) for both operations
    Space: O(n)
    """

    def serialize(self, root: TreeNode) -> str:
        """Encode tree to string using preorder traversal."""
        def dfs(node):
            if not node:
                result.append("null")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        result = []
        dfs(root)
        return ",".join(result)

    def deserialize(self, data: str) -> TreeNode:
        """Decode string to tree."""
        def dfs():
            val = next(values)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        values = iter(data.split(","))
        return dfs()
```

**Alternative Level-Order Approach**:

```python
class CodecLevelOrder:
    """Using level-order (BFS) serialization."""

    def serialize(self, root: TreeNode) -> str:
        """Serialize using level-order traversal."""
        if not root:
            return ""

        from collections import deque
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return ",".join(result)

    def deserialize(self, data: str) -> TreeNode:
        """Deserialize from level-order format."""
        if not data:
            return None

        from collections import deque
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # Process left child
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            # Process right child
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root
```

**Time Complexity**: O(n)
**Space Complexity**: O(n)

---

### H3: Binary Tree Cameras

**Problem**: Minimum cameras to monitor all nodes.

**Approach**: Greedy bottom-up - place camera when child needs monitoring.

```python
def min_camera_cover(root: TreeNode) -> int:
    """
    Find minimum number of cameras to monitor all nodes.

    Time: O(n) - visit each node once
    Space: O(h) - recursion stack

    States:
    0 - Node not monitored (needs camera on parent)
    1 - Node has camera
    2 - Node monitored (but no camera on it)
    """
    def dfs(node: TreeNode) -> int:
        """Return monitoring state of node."""
        if not node:
            return 2  # Null nodes are "monitored"

        left = dfs(node.left)
        right = dfs(node.right)

        # If any child not monitored, need camera here
        if left == 0 or right == 0:
            dfs.cameras += 1
            return 1

        # If any child has camera, this node is monitored
        if left == 1 or right == 1:
            return 2

        # Both children monitored but no camera - not monitored
        return 0

    dfs.cameras = 0

    # If root not monitored, need camera there
    if dfs(root) == 0:
        dfs.cameras += 1

    return dfs.cameras
```

**Explanation**:
- Process tree bottom-up (post-order)
- States: 0=needs monitoring, 1=has camera, 2=monitored
- Place camera only when child needs monitoring (greedy)
- Leaf nodes return 0 (not monitored)
- Parent of leaf gets camera (returns 1)
- Grandparent is monitored (returns 2)

**Time Complexity**: O(n)
**Space Complexity**: O(h)

---

### H4: Recover Binary Search Tree

**Problem**: Two nodes are swapped - recover the tree.

**Approach**: Find the two swapped nodes using inorder traversal.

```python
def recover_tree(root: TreeNode) -> None:
    """
    Recover BST by swapping two nodes back.

    Time: O(n) - inorder traversal
    Space: O(h) - recursion stack
    """
    def inorder(node: TreeNode):
        """Inorder traversal to find swapped nodes."""
        if not node:
            return

        inorder(node.left)

        # Check if current node violates BST property
        if inorder.prev and inorder.prev.val > node.val:
            # First violation - mark both nodes
            if not inorder.first:
                inorder.first = inorder.prev
            # Second violation - update second node
            inorder.second = node

        inorder.prev = node
        inorder(node.right)

    # Initialize tracking variables
    inorder.prev = None
    inorder.first = None
    inorder.second = None

    # Find the two swapped nodes
    inorder(root)

    # Swap their values back
    if inorder.first and inorder.second:
        inorder.first.val, inorder.second.val = inorder.second.val, inorder.first.val
```

**Iterative Morris Traversal (O(1) Space)**:

```python
def recover_tree_morris(root: TreeNode) -> None:
    """
    Using Morris traversal for O(1) space.

    Time: O(n)
    Space: O(1)
    """
    first = second = prev = None
    current = root

    while current:
        if not current.left:
            # Process current node
            if prev and prev.val > current.val:
                if not first:
                    first = prev
                second = current
            prev = current
            current = current.right
        else:
            # Find predecessor
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if not predecessor.right:
                # Create thread
                predecessor.right = current
                current = current.left
            else:
                # Remove thread and process current
                predecessor.right = None
                if prev and prev.val > current.val:
                    if not first:
                        first = prev
                    second = current
                prev = current
                current = current.right

    # Swap values
    if first and second:
        first.val, second.val = second.val, first.val
```

**Time Complexity**: O(n)
**Space Complexity**: O(h) recursive, O(1) Morris traversal

---

### H5: Vertical Order Traversal

**Problem**: Return vertical order traversal (by column, row, then value).

**Approach**: Track (column, row, value) for each node, then sort.

```python
def vertical_traversal(root: TreeNode) -> List[List[int]]:
    """
    Vertical order traversal.

    Time: O(n log n) - sorting nodes
    Space: O(n) - storing all nodes
    """
    from collections import defaultdict

    # Store (row, col, val) for each node
    nodes = []

    def dfs(node: TreeNode, row: int, col: int):
        """Collect node positions."""
        if not node:
            return
        nodes.append((col, row, node.val))
        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)

    # Sort by column, then row, then value
    nodes.sort()

    # Group by column
    result = []
    prev_col = float('-inf')

    for col, row, val in nodes:
        if col != prev_col:
            result.append([])
            prev_col = col
        result[-1].append(val)

    return result
```

**Alternative with Dictionary**:

```python
def vertical_traversal_dict(root: TreeNode) -> List[List[int]]:
    """
    Using dictionary to group by column.

    Time: O(n log n)
    Space: O(n)
    """
    from collections import defaultdict

    column_table = defaultdict(list)

    def dfs(node: TreeNode, row: int, col: int):
        if not node:
            return
        column_table[col].append((row, node.val))
        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)

    # Sort columns and values within each column
    result = []
    for col in sorted(column_table.keys()):
        # Sort by row, then value
        column_table[col].sort()
        result.append([val for row, val in column_table[col]])

    return result
```

**BFS Approach**:

```python
def vertical_traversal_bfs(root: TreeNode) -> List[List[int]]:
    """
    BFS approach.

    Time: O(n log n)
    Space: O(n)
    """
    from collections import defaultdict, deque

    if not root:
        return []

    column_table = defaultdict(list)
    queue = deque([(root, 0, 0)])  # (node, row, col)

    while queue:
        node, row, col = queue.popleft()
        column_table[col].append((row, node.val))

        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))

    result = []
    for col in sorted(column_table.keys()):
        column_table[col].sort()
        result.append([val for row, val in column_table[col]])

    return result
```

**Time Complexity**: O(n log n) - sorting dominates
**Space Complexity**: O(n)

---

## Bonus Challenges

### B1: Count Complete Tree Nodes

**Problem**: Count nodes in complete binary tree efficiently.

**Approach**: Use complete tree property to count without visiting all nodes.

```python
def count_nodes(root: TreeNode) -> int:
    """
    Count nodes efficiently using complete tree property.

    Time: O(log^2 n) - O(log n) levels, O(log n) height check each
    Space: O(log n) - recursion depth
    """
    if not root:
        return 0

    def get_height(node: TreeNode, go_left: bool) -> int:
        """Get height going left or right."""
        height = 0
        while node:
            height += 1
            node = node.left if go_left else node.right
        return height

    left_height = get_height(root, True)
    right_height = get_height(root, False)

    # If same height, tree is perfect
    if left_height == right_height:
        return (1 << left_height) - 1  # 2^h - 1

    # Otherwise, recursively count
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

**Alternative Implementation**:

```python
def count_nodes_alt(root: TreeNode) -> int:
    """
    Alternative with explicit perfect tree check.

    Time: O(log^2 n)
    Space: O(log n)
    """
    if not root:
        return 0

    # Get leftmost and rightmost heights
    left_depth = 0
    node = root
    while node.left:
        left_depth += 1
        node = node.left

    right_depth = 0
    node = root
    while node.right:
        right_depth += 1
        node = node.right

    # If heights equal, perfect binary tree
    if left_depth == right_depth:
        return (1 << (left_depth + 1)) - 1

    # Otherwise recursively count
    return 1 + count_nodes_alt(root.left) + count_nodes_alt(root.right)
```

**Binary Search Approach**:

```python
def count_nodes_binary_search(root: TreeNode) -> int:
    """
    Using binary search on last level.

    Time: O(log^2 n)
    Space: O(1) iterative
    """
    if not root:
        return 0

    # Get tree height
    height = 0
    node = root
    while node.left:
        height += 1
        node = node.left

    # If height 0, just root
    if height == 0:
        return 1

    # Binary search for last node on last level
    def exists(idx: int) -> bool:
        """Check if node at index exists on last level."""
        left, right = 0, (1 << height) - 1
        node = root

        for _ in range(height):
            mid = (left + right) // 2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1

        return node is not None

    # Binary search for rightmost node on last level
    left, right = 0, (1 << height) - 1
    while left <= right:
        mid = (left + right) // 2
        if exists(mid):
            left = mid + 1
        else:
            right = mid - 1

    # Total nodes = full levels + last level
    return (1 << height) - 1 + left
```

**Time Complexity**: O(log²n)
**Space Complexity**: O(log n) recursive, O(1) iterative

---

### B2: Maximum Width of Binary Tree

**Problem**: Find maximum width (including null nodes between leftmost and rightmost).

**Approach**: Track positions using binary tree indexing.

```python
def width_of_binary_tree(root: TreeNode) -> int:
    """
    Find maximum width of binary tree.

    Time: O(n) - visit each node once
    Space: O(w) where w is maximum width
    """
    if not root:
        return 0

    from collections import deque
    max_width = 0
    queue = deque([(root, 0)])  # (node, position)

    while queue:
        level_length = len(queue)
        _, level_start = queue[0]

        for i in range(level_length):
            node, pos = queue.popleft()

            # Add children with calculated positions
            if node.left:
                queue.append((node.left, 2 * pos))
            if node.right:
                queue.append((node.right, 2 * pos + 1))

        # Width is difference between first and last positions
        max_width = max(max_width, pos - level_start + 1)

    return max_width
```

**Optimized to Prevent Overflow**:

```python
def width_of_binary_tree_optimized(root: TreeNode) -> int:
    """
    Prevent integer overflow by normalizing positions.

    Time: O(n)
    Space: O(w)
    """
    if not root:
        return 0

    from collections import deque
    max_width = 0
    queue = deque([(root, 0)])

    while queue:
        level_length = len(queue)
        _, level_start = queue[0]

        for i in range(level_length):
            node, pos = queue.popleft()

            # Normalize position to prevent overflow
            pos -= level_start

            if node.left:
                queue.append((node.left, 2 * pos))
            if node.right:
                queue.append((node.right, 2 * pos + 1))

        max_width = max(max_width, pos + 1)

    return max_width
```

**DFS Approach**:

```python
def width_of_binary_tree_dfs(root: TreeNode) -> int:
    """
    DFS approach tracking leftmost position at each level.

    Time: O(n)
    Space: O(h)
    """
    level_min = {}  # Track leftmost position at each level

    def dfs(node: TreeNode, depth: int, pos: int) -> int:
        if not node:
            return 0

        # Track leftmost position at this level
        if depth not in level_min:
            level_min[depth] = pos

        # Width at current node
        current_width = pos - level_min[depth] + 1

        # Max width in subtrees
        left_width = dfs(node.left, depth + 1, 2 * pos)
        right_width = dfs(node.right, depth + 1, 2 * pos + 1)

        return max(current_width, left_width, right_width)

    return dfs(root, 0, 0)
```

**Time Complexity**: O(n)
**Space Complexity**: O(w) for BFS, O(h) for DFS

---

### B3: All Nodes Distance K

**Problem**: Find all nodes at distance K from target node.

**Approach**: Build parent pointers, then BFS from target.

```python
def distance_k(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    """
    Find all nodes at distance K from target.

    Time: O(n) - build parent map + BFS
    Space: O(n) - parent map + queue
    """
    from collections import deque, defaultdict

    # Build parent pointers
    parent = {}

    def build_parent(node: TreeNode, par: TreeNode = None):
        if not node:
            return
        parent[node] = par
        build_parent(node.left, node)
        build_parent(node.right, node)

    build_parent(root)

    # BFS from target
    visited = {target}
    queue = deque([(target, 0)])
    result = []

    while queue:
        node, dist = queue.popleft()

        # If at distance k, add to result
        if dist == k:
            result.append(node.val)
            continue

        # If beyond k, stop
        if dist > k:
            break

        # Explore neighbors (left, right, parent)
        for neighbor in [node.left, node.right, parent[node]]:
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return result
```

**DFS Approach**:

```python
def distance_k_dfs(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    """
    DFS approach with distance tracking.

    Time: O(n)
    Space: O(n)
    """
    from collections import defaultdict

    # Build adjacency list (undirected graph)
    graph = defaultdict(list)

    def build_graph(node: TreeNode, parent: TreeNode = None):
        if not node:
            return
        if parent:
            graph[node].append(parent)
            graph[parent].append(node)
        build_graph(node.left, node)
        build_graph(node.right, node)

    build_graph(root)

    # DFS from target
    result = []
    visited = set()

    def dfs(node: TreeNode, dist: int):
        if not node or node in visited:
            return

        visited.add(node)

        if dist == k:
            result.append(node.val)
            return

        for neighbor in graph[node]:
            dfs(neighbor, dist + 1)

    dfs(target, 0)
    return result
```

**Optimized Single Pass**:

```python
def distance_k_optimized(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    """
    Single pass DFS - find distance from each node to target.

    Time: O(n)
    Space: O(h)
    """
    result = []

    def dfs(node: TreeNode) -> int:
        """
        Return distance from node to target.
        -1 if target not in subtree.
        """
        if not node:
            return -1

        # Found target
        if node == target:
            # Find all nodes k distance down
            subtree_add(node, k)
            return 0

        # Check left subtree
        left_dist = dfs(node.left)
        if left_dist != -1:
            # Target in left subtree
            if left_dist + 1 == k:
                result.append(node.val)
            else:
                # Search right subtree for nodes at remaining distance
                subtree_add(node.right, k - left_dist - 2)
            return left_dist + 1

        # Check right subtree
        right_dist = dfs(node.right)
        if right_dist != -1:
            # Target in right subtree
            if right_dist + 1 == k:
                result.append(node.val)
            else:
                # Search left subtree for nodes at remaining distance
                subtree_add(node.left, k - right_dist - 2)
            return right_dist + 1

        return -1

    def subtree_add(node: TreeNode, dist: int):
        """Add all nodes at distance dist in subtree."""
        if not node or dist < 0:
            return
        if dist == 0:
            result.append(node.val)
            return
        subtree_add(node.left, dist - 1)
        subtree_add(node.right, dist - 1)

    dfs(root)
    return result
```

**Time Complexity**: O(n)
**Space Complexity**: O(n) for parent map approach, O(h) for optimized

---

## Summary and Key Patterns

### Pattern Recognition

**1. Tree Traversal Patterns**
- **Preorder**: Root → Left → Right (useful for copying trees)
- **Inorder**: Left → Root → Right (gives sorted order in BST)
- **Postorder**: Left → Right → Root (useful for deletion, bottom-up processing)
- **Level-order**: BFS, useful for level-based problems

**2. Common Techniques**
- **Recursion**: Most tree problems naturally fit recursive solutions
- **Global Variables**: Track max/min values across recursion (diameter, path sum)
- **Bottom-up**: Return information from subtrees (height, balance)
- **Top-down**: Pass information down (ranges for BST validation)
- **Two Pointers/Nodes**: Comparing subtrees (symmetric, same tree)

**3. Time Complexity Patterns**
- O(n): Visit each node once (most problems)
- O(n log n): Sorting involved (vertical traversal)
- O(h): Path-based operations (BST search, LCA in BST)
- O(log²n): Complete tree optimizations

**4. Space Complexity Patterns**
- O(h): Recursion stack / iterative stack
- O(w): BFS queue (w = maximum width)
- O(n): Storing all nodes (serialization, vertical traversal)

### Problem-Solving Tips

1. **Start with Base Cases**: Always handle null nodes first
2. **Choose Right Traversal**: Match traversal to problem requirements
3. **BFS vs DFS**: Use BFS for level-based, shortest path; DFS for paths, subtree problems
4. **BST Properties**: Leverage ordering for O(h) solutions
5. **Auxiliary Data Structures**: Use hashmaps for O(1) lookups, queues for BFS
6. **In-place vs New Tree**: Decide if modifying original or creating new

### Common Pitfalls

1. **Forgetting Null Checks**: Always check if node is null
2. **Off-by-One Errors**: Especially in level counting (depth vs height)
3. **Leaf Node Definition**: Node with no children (not null node)
4. **Return Values**: Ensure you're returning what's needed (node vs value vs boolean)
5. **Side Effects**: Be careful with global variables in recursion
6. **Integer Overflow**: In problems like maximum width (use normalization)

### Practice Recommendations

**Week 1: Foundations**
- Master E1-E8 (Easy problems)
- Practice both recursive and iterative solutions
- Understand tree traversals thoroughly

**Week 2: Intermediate**
- Complete M1-M5 (Medium BST and traversal)
- Focus on BST properties and validation
- Practice BFS and level-order variations

**Week 3: Advanced**
- Complete M6-M10 (Medium LCA and advanced)
- Tackle H1-H3 (Hard path problems)
- Study greedy and optimization techniques

**Week 4: Mastery**
- Complete H4-H5 and B1-B3
- Review all solutions and alternative approaches
- Practice explaining approaches clearly

Good luck with your tree algorithm practice!
