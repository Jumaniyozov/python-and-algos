# Chapter 33: Trees - Tips and Tricks

## Table of Contents
1. [Common Pitfalls](#common-pitfalls)
2. [Pattern Recognition](#pattern-recognition)
3. [Interview Tips](#interview-tips)
4. [Performance Optimization](#performance-optimization)
5. [LeetCode Practice Problems](#leetcode-practice-problems)

---

## Common Pitfalls

### 1. Forgetting Base Cases
```python
# ❌ WRONG: No base case
def max_depth(root):
    return 1 + max(max_depth(root.left), max_depth(root.right))

# ✅ CORRECT: Handle null nodes
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

### 2. Incorrect BST Validation
```python
# ❌ WRONG: Only checks immediate children
def is_valid_bst(root):
    if not root:
        return True
    if root.left and root.left.val >= root.val:
        return False
    if root.right and root.right.val <= root.val:
        return False
    return is_valid_bst(root.left) and is_valid_bst(root.right)

# ✅ CORRECT: Track valid range
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not root:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    return validate(root, float('-inf'), float('inf'))
```

### 3. Confusing Depth vs Height
```python
# Depth: Distance from root to node (top-down)
# Height: Distance from node to deepest leaf (bottom-up)

def node_depth(root, node, depth=0):
    """Depth of specific node."""
    if not root:
        return -1
    if root == node:
        return depth
    left = node_depth(root.left, node, depth + 1)
    if left != -1:
        return left
    return node_depth(root.right, node, depth + 1)

def tree_height(root):
    """Height of tree."""
    if not root:
        return -1  # or 0, depending on definition
    return 1 + max(tree_height(root.left), tree_height(root.right))
```

### 4. Modifying Tree During Traversal
```python
# ❌ WRONG: Losing reference while inverting
def invert_tree(root):
    if not root:
        return None
    root.left = invert_tree(root.right)   # Lost original left!
    root.right = invert_tree(root.left)   # Using modified left!
    return root

# ✅ CORRECT: Save references first
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left  # Swap first
    invert_tree(root.left)
    invert_tree(root.right)
    return root
```

### 5. Path Sum Edge Cases
```python
# ❌ WRONG: Not checking for leaf node
def has_path_sum(root, target_sum):
    if not root:
        return False
    if root.val == target_sum:  # Wrong! Could be internal node
        return True
    return (has_path_sum(root.left, target_sum - root.val) or
            has_path_sum(root.right, target_sum - root.val))

# ✅ CORRECT: Must be leaf node
def has_path_sum(root, target_sum):
    if not root:
        return False
    if not root.left and not root.right:  # Leaf check!
        return root.val == target_sum
    return (has_path_sum(root.left, target_sum - root.val) or
            has_path_sum(root.right, target_sum - root.val))
```

### 6. Level-Order Traversal Mistakes
```python
# ❌ WRONG: Adding children after processing all nodes
from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
    # Forgot to add children!
    return result

# ✅ CORRECT: Add children while processing
def level_order(root):
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

---

## Pattern Recognition

### When to Use Each Traversal

#### Inorder (Left → Root → Right)
**Use when:**
- Need sorted order from BST
- Processing nodes in sorted order
- Validating BST with inorder sequence

**Example problems:**
- Kth smallest in BST
- Validate BST
- BST to sorted doubly linked list

```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

#### Preorder (Root → Left → Right)
**Use when:**
- Creating copy of tree
- Prefix expression evaluation
- Tree serialization

**Example problems:**
- Serialize/deserialize tree
- Clone tree
- Flatten tree to linked list

```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)
```

#### Postorder (Left → Right → Root)
**Use when:**
- Deleting tree (delete children first)
- Postfix expression evaluation
- Bottom-up computation

**Example problems:**
- Delete tree
- Calculate tree size
- Lowest common ancestor

```python
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

#### Level-Order (BFS)
**Use when:**
- Level-by-level processing
- Shortest path in tree
- Right/left side view

**Example problems:**
- Level order traversal
- Zigzag traversal
- Right side view
- Minimum depth

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

### Common Tree Patterns

#### Pattern 1: Recursive Tree Processing
Most tree problems use recursion.

**Template:**
```python
def process_tree(root):
    # Base case
    if not root:
        return base_value

    # Recursive case
    left_result = process_tree(root.left)
    right_result = process_tree(root.right)

    # Combine results
    return combine(root.val, left_result, right_result)
```

**Examples:** Height, diameter, balanced check, path sum

#### Pattern 2: BST Property Exploitation
Use the ordering property to optimize.

**Template:**
```python
def bst_operation(root, target):
    if not root:
        return None

    if target < root.val:
        # Go left
        return bst_operation(root.left, target)
    elif target > root.val:
        # Go right
        return bst_operation(root.right, target)
    else:
        # Found it
        return root
```

**Examples:** Search, insert, delete, LCA in BST

#### Pattern 3: Path Tracking
Accumulate values along path.

**Template:**
```python
def find_path(root, target, path=[]):
    if not root:
        return False

    path.append(root.val)

    if root.val == target:
        return True

    if (find_path(root.left, target, path) or
        find_path(root.right, target, path)):
        return True

    path.pop()  # Backtrack
    return False
```

**Examples:** Path sum, all paths, path to node

#### Pattern 4: Bottom-Up Computation
Gather information from subtrees.

**Template:**
```python
def bottom_up(root):
    if not root:
        return base_value

    left_info = bottom_up(root.left)
    right_info = bottom_up(root.right)

    # Use left_info and right_info to compute current info
    current_info = compute(root, left_info, right_info)

    return current_info
```

**Examples:** Diameter, max path sum, balanced check

---

## Interview Tips

### 1. Clarify the Problem

**Questions to ask:**
- Is it a binary tree or BST?
- Can the tree be empty?
- Are values unique?
- Can values be negative?
- What should I return for empty tree?

### 2. Draw Examples

Always draw the tree and trace your algorithm:
```
Example tree:
      10
     /  \
    5    15
   / \
  3   7

Trace inorder:
1. Visit 10
2. Recurse left → Visit 5
3. Recurse left → Visit 3
   3 has no children → return [3]
4. Back to 5, append 5 → [3, 5]
5. Recurse right → Visit 7 → [3, 5, 7]
6. Back to 10, append 10 → [3, 5, 7, 10]
7. Recurse right → Visit 15 → [3, 5, 7, 10, 15]
```

### 3. Consider Edge Cases

**Common edge cases:**
- Empty tree (null root)
- Single node tree
- Skewed tree (all nodes on one side)
- Perfect binary tree
- Tree with negative values
- Tree with duplicate values

### 4. Think Recursively

Most tree problems have elegant recursive solutions:

**Steps:**
1. Define base case (usually empty tree)
2. Assume recursive call works for subtrees
3. Combine subtree results with current node
4. Return combined result

### 5. Space Complexity Awareness

**Recursive calls use stack space:**
- Balanced tree: O(log n) space
- Skewed tree: O(n) space

**For O(1) space, use iterative with parent pointers or Morris traversal**

### 6. BST Optimization

If the tree is a BST, exploit the ordering property:
- Don't search both subtrees if you can determine the direction
- Use inorder traversal for sorted order
- LCA can be found in O(h) time

---

## Performance Optimization

### 1. Avoid Redundant Recursion

```python
# ❌ Inefficient: Multiple calls for same subtree
def is_balanced_slow(root):
    if not root:
        return True
    left_height = max_depth(root.left)    # O(n)
    right_height = max_depth(root.right)  # O(n)
    return (abs(left_height - right_height) <= 1 and
            is_balanced_slow(root.left) and    # Calls max_depth again!
            is_balanced_slow(root.right))      # Calls max_depth again!

# ✅ Efficient: Compute height once
def is_balanced(root):
    def check(node):
        if not node:
            return 0, True
        left_h, left_balanced = check(node.left)
        right_h, right_balanced = check(node.right)
        balanced = (left_balanced and right_balanced and
                   abs(left_h - right_h) <= 1)
        return max(left_h, right_h) + 1, balanced
    return check(root)[1]
```

### 2. Early Termination

```python
# ✅ Stop as soon as we find the answer
def has_path_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target
    # Early return if found in left
    if has_path_sum(root.left, target - root.val):
        return True  # Don't check right!
    return has_path_sum(root.right, target - root.val)
```

### 3. Iterative vs Recursive

For very deep trees, iterative may be better to avoid stack overflow:

```python
# Iterative inorder (explicit stack)
def inorder_iterative(root):
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result
```

### 4. Memoization

For problems with overlapping subproblems:

```python
def count_paths_with_sum(root, target_sum):
    """Count paths with given sum (path can start/end anywhere)."""
    cache = {}

    def dfs(node, current_sum):
        if not node:
            return 0

        current_sum += node.val
        # How many paths end at current node
        count = cache.get(current_sum - target_sum, 0)
        if current_sum == target_sum:
            count += 1

        cache[current_sum] = cache.get(current_sum, 0) + 1
        count += dfs(node.left, current_sum)
        count += dfs(node.right, current_sum)
        cache[current_sum] -= 1  # Backtrack

        return count

    return dfs(root, 0)
```

---

## LeetCode Practice Problems

### Easy Problems (20 problems)

#### 1. Maximum Depth of Binary Tree
**Link:** https://leetcode.com/problems/maximum-depth-of-binary-tree/
**Pattern:** Recursive Tree Processing
**Topics:** Binary Tree, DFS, Recursion
**Description:** Find the maximum depth of a binary tree
**Why Practice:** Foundation for understanding tree recursion and height calculations

#### 2. Invert Binary Tree
**Link:** https://leetcode.com/problems/invert-binary-tree/
**Pattern:** Recursive Tree Processing
**Topics:** Binary Tree, DFS
**Description:** Invert/mirror a binary tree
**Why Practice:** Classic recursion problem, tests understanding of tree structure modification

#### 3. Same Tree
**Link:** https://leetcode.com/problems/same-tree/
**Pattern:** Recursive Comparison
**Topics:** Binary Tree, DFS
**Description:** Check if two trees are structurally identical
**Why Practice:** Learn to compare tree structures recursively

#### 4. Symmetric Tree
**Link:** https://leetcode.com/problems/symmetric-tree/
**Pattern:** Recursive Comparison
**Topics:** Binary Tree, DFS, BFS
**Description:** Check if tree is symmetric around its center
**Why Practice:** Practice comparing tree structures with mirroring logic

#### 5. Merge Two Binary Trees
**Link:** https://leetcode.com/problems/merge-two-binary-trees/
**Pattern:** Recursive Processing
**Topics:** Binary Tree, DFS
**Description:** Merge two trees by summing overlapping nodes
**Why Practice:** Learn to process two trees simultaneously

#### 6. Binary Tree Paths
**Link:** https://leetcode.com/problems/binary-tree-paths/
**Pattern:** Path Tracking
**Topics:** Binary Tree, DFS, Backtracking
**Description:** Find all root-to-leaf paths
**Why Practice:** Essential pattern for path problems

#### 7. Minimum Depth of Binary Tree
**Link:** https://leetcode.com/problems/minimum-depth-of-binary-tree/
**Pattern:** BFS, DFS
**Topics:** Binary Tree, BFS
**Description:** Find shortest path from root to leaf
**Why Practice:** Learn when BFS is better than DFS

#### 8. Balanced Binary Tree
**Link:** https://leetcode.com/problems/balanced-binary-tree/
**Pattern:** Bottom-Up Processing
**Topics:** Binary Tree, DFS
**Description:** Check if tree is height-balanced
**Why Practice:** Classic bottom-up recursion pattern

#### 9. Path Sum
**Link:** https://leetcode.com/problems/path-sum/
**Pattern:** Path Tracking
**Topics:** Binary Tree, DFS
**Description:** Check if root-to-leaf path exists with given sum
**Why Practice:** Foundation for more complex path sum problems

#### 10. Sum of Left Leaves
**Link:** https://leetcode.com/problems/sum-of-left-leaves/
**Pattern:** DFS with Conditions
**Topics:** Binary Tree, DFS
**Description:** Sum all left leaves in tree
**Why Practice:** Learn to identify and process specific node types

#### 11. Diameter of Binary Tree
**Link:** https://leetcode.com/problems/diameter-of-binary-tree/
**Pattern:** Bottom-Up Processing
**Topics:** Binary Tree, DFS
**Description:** Find longest path between any two nodes
**Why Practice:** Classic problem using global variable in recursion

#### 12. Subtree of Another Tree
**Link:** https://leetcode.com/problems/subtree-of-another-tree/
**Pattern:** Tree Matching
**Topics:** Binary Tree, DFS
**Description:** Check if one tree is subtree of another
**Why Practice:** Combine tree traversal with tree comparison

#### 13. Convert Sorted Array to Binary Search Tree
**Link:** https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
**Pattern:** Tree Construction
**Topics:** BST, Divide and Conquer
**Description:** Build balanced BST from sorted array
**Why Practice:** Learn divide and conquer for tree construction

#### 14. Increasing Order Search Tree
**Link:** https://leetcode.com/problems/increasing-order-search-tree/
**Pattern:** Inorder Traversal
**Topics:** BST, Inorder
**Description:** Rearrange BST to right-skewed tree in ascending order
**Why Practice:** Apply inorder traversal with tree modification

#### 15. Range Sum of BST
**Link:** https://leetcode.com/problems/range-sum-of-bst/
**Pattern:** BST Property
**Topics:** BST, DFS
**Description:** Sum values in BST within given range
**Why Practice:** Exploit BST property to prune search space

#### 16. Average of Levels in Binary Tree
**Link:** https://leetcode.com/problems/average-of-levels-in-binary-tree/
**Pattern:** Level-Order Traversal
**Topics:** Binary Tree, BFS
**Description:** Calculate average value at each level
**Why Practice:** Practice level-by-level processing

#### 17. Two Sum IV - Input is a BST
**Link:** https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
**Pattern:** BST + Hash Table
**Topics:** BST, Hash Table
**Description:** Find two numbers in BST that sum to target
**Why Practice:** Combine tree traversal with hash table

#### 18. N-ary Tree Preorder Traversal
**Link:** https://leetcode.com/problems/n-ary-tree-preorder-traversal/
**Pattern:** DFS
**Topics:** Tree, DFS
**Description:** Preorder traversal of N-ary tree
**Why Practice:** Extend binary tree concepts to N-ary trees

#### 19. N-ary Tree Level Order Traversal
**Link:** https://leetcode.com/problems/n-ary-tree-level-order-traversal/
**Pattern:** BFS
**Topics:** Tree, BFS
**Description:** Level-order traversal of N-ary tree
**Why Practice:** Apply BFS to N-ary trees

#### 20. Leaf-Similar Trees
**Link:** https://leetcode.com/problems/leaf-similar-trees/
**Pattern:** DFS
**Topics:** Binary Tree, DFS
**Description:** Check if two trees have same leaf sequence
**Why Practice:** Practice collecting specific nodes during traversal

### Medium Problems (35 problems)

#### 21. Validate Binary Search Tree
**Link:** https://leetcode.com/problems/validate-binary-search-tree/
**Pattern:** BST Property + Range Tracking
**Topics:** BST, DFS
**Description:** Determine if binary tree is valid BST
**Why Practice:** Most important BST validation problem, critical interview question

#### 22. Binary Tree Level Order Traversal
**Link:** https://leetcode.com/problems/binary-tree-level-order-traversal/
**Pattern:** BFS
**Topics:** Binary Tree, BFS
**Description:** Return level-order traversal as list of lists
**Why Practice:** Essential BFS pattern, appears in many variations

#### 23. Binary Tree Zigzag Level Order Traversal
**Link:** https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
**Pattern:** BFS with Direction
**Topics:** Binary Tree, BFS
**Description:** Level-order in zigzag pattern
**Why Practice:** BFS variation, tests alternating logic

#### 24. Construct Binary Tree from Preorder and Inorder
**Link:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
**Pattern:** Tree Construction
**Topics:** Binary Tree, Divide and Conquer
**Description:** Build tree from two traversals
**Why Practice:** Essential tree construction pattern

#### 25. Construct Binary Tree from Inorder and Postorder
**Link:** https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
**Pattern:** Tree Construction
**Topics:** Binary Tree, Divide and Conquer
**Description:** Build tree from inorder and postorder
**Why Practice:** Similar to #24, reinforces construction logic

#### 26. Path Sum II
**Link:** https://leetcode.com/problems/path-sum-ii/
**Pattern:** Path Tracking + Backtracking
**Topics:** Binary Tree, DFS, Backtracking
**Description:** Find all root-to-leaf paths with given sum
**Why Practice:** Classic backtracking with path collection

#### 27. Path Sum III
**Link:** https://leetcode.com/problems/path-sum-iii/
**Pattern:** Prefix Sum + DFS
**Topics:** Binary Tree, DFS, Hash Table
**Description:** Count paths with given sum (can start anywhere)
**Why Practice:** Advanced path problem, uses prefix sum technique

#### 28. Flatten Binary Tree to Linked List
**Link:** https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
**Pattern:** Preorder Traversal
**Topics:** Binary Tree, DFS
**Description:** Flatten tree to right-skewed linked list
**Why Practice:** Practice in-place tree modification

#### 29. Populating Next Right Pointers in Each Node
**Link:** https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
**Pattern:** Level-Order Traversal
**Topics:** Binary Tree, BFS
**Description:** Connect nodes at same level
**Why Practice:** Level processing with node linking

#### 30. Populating Next Right Pointers II
**Link:** https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
**Pattern:** Level-Order Traversal
**Topics:** Binary Tree, BFS
**Description:** Connect nodes at same level (any tree)
**Why Practice:** Variation of #29 for general trees

#### 31. Lowest Common Ancestor of a Binary Search Tree
**Link:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
**Pattern:** BST Property
**Topics:** BST
**Description:** Find LCA in BST
**Why Practice:** Exploit BST property for O(h) solution

#### 32. Lowest Common Ancestor of a Binary Tree
**Link:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
**Pattern:** Post-Order Traversal
**Topics:** Binary Tree, DFS
**Description:** Find LCA in binary tree
**Why Practice:** Classic LCA problem, essential pattern

#### 33. Binary Tree Right Side View
**Link:** https://leetcode.com/problems/binary-tree-right-side-view/
**Pattern:** BFS/DFS
**Topics:** Binary Tree, BFS
**Description:** View tree from right side
**Why Practice:** Level processing to find rightmost nodes

#### 34. Count Complete Tree Nodes
**Link:** https://leetcode.com/problems/count-complete-tree-nodes/
**Pattern:** Binary Search + Tree Properties
**Topics:** Complete Binary Tree, Binary Search
**Description:** Count nodes efficiently in complete tree
**Why Practice:** Exploit complete tree property for O(log²n) solution

#### 35. Kth Smallest Element in a BST
**Link:** https://leetcode.com/problems/kth-smallest-element-in-a-bst/
**Pattern:** Inorder Traversal
**Topics:** BST, Inorder
**Description:** Find kth smallest element
**Why Practice:** Classic inorder + early termination

#### 36. Binary Tree Level Order Traversal II
**Link:** https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
**Pattern:** BFS
**Topics:** Binary Tree, BFS
**Description:** Level-order from bottom to top
**Why Practice:** BFS variation with result reversal

#### 37. Binary Tree Inorder Traversal
**Link:** https://leetcode.com/problems/binary-tree-inorder-traversal/
**Pattern:** DFS
**Topics:** Binary Tree, Inorder, Stack
**Description:** Inorder traversal (recursive and iterative)
**Why Practice:** Must know both recursive and iterative solutions

#### 38. Binary Tree Preorder Traversal
**Link:** https://leetcode.com/problems/binary-tree-preorder-traversal/
**Pattern:** DFS
**Topics:** Binary Tree, Preorder, Stack
**Description:** Preorder traversal
**Why Practice:** Practice iterative DFS with stack

#### 39. Binary Tree Postorder Traversal
**Link:** https://leetcode.com/problems/binary-tree-postorder-traversal/
**Pattern:** DFS
**Topics:** Binary Tree, Postorder, Stack
**Description:** Postorder traversal
**Why Practice:** Most challenging iterative traversal

#### 40. Sum Root to Leaf Numbers
**Link:** https://leetcode.com/problems/sum-root-to-leaf-numbers/
**Pattern:** Path Tracking
**Topics:** Binary Tree, DFS
**Description:** Sum numbers formed by root-to-leaf paths
**Why Practice:** Path accumulation with numeric values

#### 41. Delete Node in a BST
**Link:** https://leetcode.com/problems/delete-node-in-a-bst/
**Pattern:** BST Operations
**Topics:** BST
**Description:** Delete node from BST
**Why Practice:** Essential BST operation, handles three cases

#### 42. Insert into a Binary Search Tree
**Link:** https://leetcode.com/problems/insert-into-a-binary-search-tree/
**Pattern:** BST Operations
**Topics:** BST
**Description:** Insert value into BST
**Why Practice:** Basic BST insertion

#### 43. Find Mode in Binary Search Tree
**Link:** https://leetcode.com/problems/find-mode-in-binary-search-tree/
**Pattern:** Inorder Traversal
**Topics:** BST, Inorder
**Description:** Find most frequent values in BST
**Why Practice:** Use inorder property to find mode efficiently

#### 44. House Robber III
**Link:** https://leetcode.com/problems/house-robber-iii/
**Pattern:** Tree DP
**Topics:** Binary Tree, Dynamic Programming
**Description:** Maximize sum without choosing adjacent nodes
**Why Practice:** Tree + DP combination

#### 45. All Nodes Distance K in Binary Tree
**Link:** https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
**Pattern:** Graph Conversion + BFS
**Topics:** Binary Tree, BFS, Graph
**Description:** Find all nodes at distance K from target
**Why Practice:** Convert tree to graph for bidirectional traversal

#### 46. Maximum Binary Tree
**Link:** https://leetcode.com/problems/maximum-binary-tree/
**Pattern:** Tree Construction
**Topics:** Binary Tree, Divide and Conquer
**Description:** Build tree where each root is max in its range
**Why Practice:** Divide and conquer construction pattern

#### 47. Find Duplicate Subtrees
**Link:** https://leetcode.com/problems/find-duplicate-subtrees/
**Pattern:** Tree Serialization + Hash
**Topics:** Binary Tree, Hash Table
**Description:** Find all duplicate subtrees
**Why Practice:** Tree serialization + hashing technique

#### 48. Most Frequent Subtree Sum
**Link:** https://leetcode.com/problems/most-frequent-subtree-sum/
**Pattern:** Post-Order + Hash Map
**Topics:** Binary Tree, Hash Table
**Description:** Find most frequent subtree sum
**Why Practice:** Bottom-up computation with frequency counting

#### 49. Longest Univalue Path
**Link:** https://leetcode.com/problems/longest-univalue-path/
**Pattern:** DFS
**Topics:** Binary Tree, DFS
**Description:** Find longest path with same values
**Why Practice:** Path problem with value constraint

#### 50. Binary Tree Pruning
**Link:** https://leetcode.com/problems/binary-tree-pruning/
**Pattern:** Post-Order
**Topics:** Binary Tree, DFS
**Description:** Remove subtrees containing only 0s
**Why Practice:** Practice bottom-up pruning

#### 51. Find Bottom Left Tree Value
**Link:** https://leetcode.com/problems/find-bottom-left-tree-value/
**Pattern:** BFS/DFS
**Topics:** Binary Tree, BFS
**Description:** Find leftmost value in last row
**Why Practice:** Level processing to find specific position

#### 52. Find Largest Value in Each Tree Row
**Link:** https://leetcode.com/problems/find-largest-value-in-each-tree-row/
**Pattern:** BFS
**Topics:** Binary Tree, BFS
**Description:** Find maximum value at each level
**Why Practice:** Level-by-level max tracking

#### 53. Add One Row to Tree
**Link:** https://leetcode.com/problems/add-one-row-to-tree/
**Pattern:** BFS/DFS
**Topics:** Binary Tree, DFS
**Description:** Add row of nodes at given depth
**Why Practice:** Tree modification at specific depth

#### 54. Deepest Leaves Sum
**Link:** https://leetcode.com/problems/deepest-leaves-sum/
**Pattern:** BFS
**Topics:** Binary Tree, BFS
**Description:** Sum values of deepest leaves
**Why Practice:** Find and process nodes at maximum depth

#### 55. Maximum Width of Binary Tree
**Link:** https://leetcode.com/problems/maximum-width-of-binary-tree/
**Pattern:** BFS with Indexing
**Topics:** Binary Tree, BFS
**Description:** Find maximum width (including null nodes)
**Why Practice:** Use node indexing in BFS

### Hard Problems (15 problems)

#### 56. Binary Tree Maximum Path Sum
**Link:** https://leetcode.com/problems/binary-tree-maximum-path-sum/
**Pattern:** Post-Order with Global Max
**Topics:** Binary Tree, DFS
**Description:** Find maximum path sum (path can start/end anywhere)
**Why Practice:** Classic hard tree problem, tests path understanding

#### 57. Serialize and Deserialize Binary Tree
**Link:** https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
**Pattern:** Preorder Traversal
**Topics:** Binary Tree, Design
**Description:** Convert tree to string and back
**Why Practice:** Essential design problem, tests tree traversal mastery

#### 58. Binary Tree Cameras
**Link:** https://leetcode.com/problems/binary-tree-cameras/
**Pattern:** Greedy + Post-Order
**Topics:** Binary Tree, Greedy
**Description:** Minimum cameras to monitor all nodes
**Why Practice:** Complex greedy problem on trees

#### 59. Recover Binary Search Tree
**Link:** https://leetcode.com/problems/recover-binary-search-tree/
**Pattern:** Inorder Traversal
**Topics:** BST, Inorder
**Description:** Fix two swapped nodes in BST
**Why Practice:** Advanced inorder application

#### 60. Vertical Order Traversal of a Binary Tree
**Link:** https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
**Pattern:** BFS + Sorting
**Topics:** Binary Tree, BFS, Hash Table
**Description:** Vertical traversal with coordinate sorting
**Why Practice:** Complex multi-dimensional sorting problem

#### 61. Binary Tree Maximum Path Sum II
**Link:** https://leetcode.com/problems/binary-tree-maximum-path-sum-ii/
**Pattern:** DFS
**Topics:** Binary Tree, DFS
**Description:** Maximum sum path (must go through root)
**Why Practice:** Variation of maximum path sum

#### 62. Count Good Nodes in Binary Tree
**Link:** https://leetcode.com/problems/count-good-nodes-in-binary-tree/
**Pattern:** DFS with Path Max
**Topics:** Binary Tree, DFS
**Description:** Count nodes that are max on their root-to-node path
**Why Practice:** Track maximum along path

#### 63. Distribute Coins in Binary Tree
**Link:** https://leetcode.com/problems/distribute-coins-in-binary-tree/
**Pattern:** Post-Order
**Topics:** Binary Tree, DFS
**Description:** Minimum moves to distribute coins evenly
**Why Practice:** Complex bottom-up calculation

#### 64. Smallest String Starting From Leaf
**Link:** https://leetcode.com/problems/smallest-string-starting-from-leaf/
**Pattern:** DFS with String Building
**Topics:** Binary Tree, DFS
**Description:** Find lexicographically smallest string from leaf to root
**Why Practice:** String accumulation in reverse order

#### 65. Flip Equivalent Binary Trees
**Link:** https://leetcode.com/problems/flip-equivalent-binary-trees/
**Pattern:** Recursive Comparison
**Topics:** Binary Tree, DFS
**Description:** Check if trees are flip equivalent
**Why Practice:** Tree comparison with transformation

#### 66. Sum of Distances in Tree
**Link:** https://leetcode.com/problems/sum-of-distances-in-tree/
**Pattern:** Tree DP
**Topics:** Tree, Dynamic Programming
**Description:** Calculate sum of distances for each node
**Why Practice:** Advanced tree DP with rerooting technique

#### 67. Longest Zigzag Path in a Binary Tree
**Link:** https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
**Pattern:** DFS with State
**Topics:** Binary Tree, DFS
**Description:** Find longest zigzag path
**Why Practice:** Track direction state in recursion

#### 68. Step-By-Step Directions From a Binary Tree Node to Another
**Link:** https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
**Pattern:** LCA + Path Finding
**Topics:** Binary Tree, LCA
**Description:** Find directions between two nodes
**Why Practice:** Combine LCA with path construction

#### 69. Delete Nodes And Return Forest
**Link:** https://leetcode.com/problems/delete-nodes-and-return-forest/
**Pattern:** Post-Order
**Topics:** Binary Tree, DFS
**Description:** Delete nodes and return resulting forest
**Why Practice:** Complex tree modification with forest creation

#### 70. Maximum Sum BST in Binary Tree
**Link:** https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
**Pattern:** Post-Order with Multiple Info
**Topics:** Binary Tree, BST, DFS
**Description:** Find maximum sum of any BST subtree
**Why Practice:** Validate BST while computing sum

---

## Pattern Mastery Checklist

### Core Patterns

- [ ] **Recursive Tree Processing**
  - Master: #1, #2, #3, #4
  - Practice: #5, #8, #10

- [ ] **Tree Traversals (DFS)**
  - Inorder: #37 (both recursive and iterative)
  - Preorder: #38
  - Postorder: #39
  - Practice: #24, #25, #28

- [ ] **Level-Order Traversal (BFS)**
  - Master: #22, #33
  - Practice: #16, #23, #36
  - Advanced: #55, #60

- [ ] **BST Operations**
  - Validation: #21 (must know!)
  - Search: #15
  - Insert: #42
  - Delete: #41
  - Inorder: #35, #43

- [ ] **Path Problems**
  - Basic: #9, #6
  - With Sum: #26, #27, #40
  - Advanced: #56, #49

- [ ] **Tree Construction**
  - From Traversals: #24, #25
  - From Array: #13
  - Special Rules: #46

- [ ] **Lowest Common Ancestor**
  - BST: #31
  - Binary Tree: #32 (must know!)
  - Application: #68

- [ ] **Bottom-Up Processing**
  - Height/Depth: #1, #7, #8
  - Diameter: #11
  - Path Sum: #56
  - Complex: #63, #66

### Must-Know Problems

**Top 20 for Interviews:**
1. Validate BST (#21)
2. Lowest Common Ancestor (#32)
3. Serialize/Deserialize (#57)
4. Maximum Path Sum (#56)
5. Level Order Traversal (#22)
6. Construct from Traversals (#24)
7. Invert Tree (#2)
8. Diameter (#11)
9. Path Sum II (#26)
10. Balanced Tree (#8)
11. Right Side View (#33)
12. Kth Smallest in BST (#35)
13. Binary Tree Cameras (#58)
14. Symmetric Tree (#4)
15. Same Tree (#3)
16. Zigzag Level Order (#23)
17. Flatten to Linked List (#28)
18. Delete Node in BST (#41)
19. Count Complete Tree Nodes (#34)
20. Recover BST (#59)

---

## Practice Progression

### Week 1-2: Foundations (Easy + Basic Medium)
**Goal:** Master recursion and basic traversals

- Day 1-2: #1, #2, #3, #4 (basic recursion)
- Day 3-4: #5, #6, #7 (more recursion patterns)
- Day 5-6: #8, #9, #10 (depth, balance, paths)
- Day 7-8: #37, #38, #39 (traversals - both recursive and iterative)
- Day 9-10: #22, #16 (BFS/level-order)
- Day 11-12: #11, #12, #13 (diameter, subtree, construction)
- Day 13-14: Review and practice weak areas

### Week 3-4: BST and Path Problems (Medium)
**Goal:** Master BST operations and path algorithms

- Day 15-16: #21 (validate BST - critical!)
- Day 17-18: #31, #32 (LCA - both versions)
- Day 19-20: #35, #41, #42 (BST operations)
- Day 21-22: #26, #27 (path sum variations)
- Day 23-24: #40, #49 (more path problems)
- Day 25-26: #24, #25 (tree construction)
- Day 27-28: Review BST and path patterns

### Week 5-6: Advanced Patterns (Medium + Hard)
**Goal:** Master complex tree algorithms

- Day 29-30: #28, #29, #30 (tree modification)
- Day 31-32: #33, #34 (right view, counting)
- Day 33-34: #44, #45 (tree DP, graph conversion)
- Day 35-36: #56 (maximum path sum - crucial!)
- Day 37-38: #57 (serialize/deserialize)
- Day 39-40: #58 (cameras - greedy)
- Day 41-42: Review hard problems

### Week 7-8: Mastery and Advanced Topics (Hard)
**Goal:** Solve challenging problems confidently

- Day 43-44: #59, #60 (recover BST, vertical order)
- Day 45-46: #63, #66 (distribute coins, sum of distances)
- Day 47-48: #68, #69, #70 (directions, delete forest, max sum BST)
- Day 49-50: #23, #36, #46, #47, #48 (medium problems for reinforcement)
- Day 51-52: #50, #51, #52, #53, #54, #55 (level processing variations)
- Day 53-54: Mock interviews with random tree problems
- Day 55-56: Final review of all must-know problems

### Total Practice Time Estimate
- Easy problems (20): ~20-25 hours
- Medium problems (35): ~50-65 hours
- Hard problems (15): ~30-40 hours
- **Total: 100-130 hours for complete mastery**

---

## Interview Preparation Checklist

### Before the Interview

- [ ] Can implement all four traversals (recursive and iterative) from memory
- [ ] Understand BST property and can validate BST correctly
- [ ] Know both BST and binary tree LCA algorithms
- [ ] Can implement level-order traversal with queue
- [ ] Understand path sum problems (root-to-leaf and any path)
- [ ] Know how to construct tree from traversals
- [ ] Can calculate height, diameter, and balance

### During the Interview

- [ ] Clarify if it's BST or binary tree
- [ ] Ask about edge cases (empty, single node, negatives)
- [ ] Draw example tree and trace algorithm
- [ ] Consider both recursive and iterative approaches
- [ ] Analyze time and space complexity
- [ ] Handle null checks in base cases
- [ ] Test with edge cases

### After the Interview

- [ ] Review problems you struggled with
- [ ] Implement alternative solutions
- [ ] Understand why your approach worked or didn't work
- [ ] Add problem to review list if needed

---

## Summary

**Trees are 25-30% of coding interviews** - mastering them is essential!

**Key Takeaways:**
1. Most tree problems use recursion - think recursively
2. Four traversals: inorder, preorder, postorder, level-order
3. BST problems can often be optimized using the ordering property
4. Draw examples and trace your algorithm
5. Consider edge cases: empty tree, single node, skewed tree
6. Practice both recursive and iterative solutions
7. Understand time/space complexity (especially recursion stack)

**Most Important Patterns:**
- Recursive tree processing (80% of problems)
- BST validation with range tracking
- Level-order traversal with BFS
- Path tracking with backtracking
- Bottom-up information gathering
- LCA algorithms

**Practice Strategy:**
- Start with easy problems to build intuition
- Master the must-know 20 problems
- Do 70+ problems across all difficulties
- Review patterns and templates regularly
- Practice explaining your thought process

Good luck with your tree mastery journey! 🌳
