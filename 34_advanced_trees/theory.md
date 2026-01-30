# Advanced Trees Theory

## Table of Contents

1. [Trie (Prefix Tree)](#trie-prefix-tree)
2. [Segment Trees](#segment-trees)
3. [Fenwick Trees (Binary Indexed Trees)](#fenwick-trees-binary-indexed-trees)
4. [AVL Trees](#avl-trees)
5. [Red-Black Trees](#red-black-trees)
6. [B-Trees and B+ Trees](#b-trees-and-b-trees)

---

## Trie (Prefix Tree)

### What is a Trie?

A **Trie** (pronounced "try") is a tree-like data structure optimized for storing and searching strings. Each node represents a character, and paths from root to nodes form strings.

### Structure

```
         root
        / | \
       a  b  c
      /   |   \
     p    a    a
    /     |     \
   p      t      t
          |
          h
```

This trie stores: "app", "bat", "bath", "cat"

### Trie Node Structure

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary mapping char -> TrieNode
        self.is_end_of_word = False  # True if word ends here
        self.word = None  # Optional: store complete word at end

# Alternative: Fixed-size array for lowercase letters
class TrieNodeArray:
    def __init__(self):
        self.children = [None] * 26  # For 'a' to 'z'
        self.is_end_of_word = False
```

### Core Operations

#### 1. Insert

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert word into trie. O(m) where m is word length."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
```

**Time Complexity:** O(m) where m = length of word
**Space Complexity:** O(m) for new word

#### 2. Search

```python
def search(self, word: str) -> bool:
    """Check if word exists in trie. O(m)."""
    node = self.root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return node.is_end_of_word
```

**Time Complexity:** O(m)

#### 3. StartsWith (Prefix Search)

```python
def starts_with(self, prefix: str) -> bool:
    """Check if any word starts with prefix. O(m)."""
    node = self.root
    for char in prefix:
        if char not in node.children:
            return False
        node = node.children[char]
    return True  # Don't need is_end_of_word
```

**Time Complexity:** O(m)

#### 4. Delete

```python
def delete(self, word: str) -> bool:
    """Delete word from trie. O(m)."""
    def _delete(node, word, index):
        if index == len(word):
            # Reached end of word
            if not node.is_end_of_word:
                return False  # Word doesn't exist
            node.is_end_of_word = False
            # Delete node only if it has no children
            return len(node.children) == 0

        char = word[index]
        if char not in node.children:
            return False

        should_delete = _delete(node.children[char], word, index + 1)

        if should_delete:
            del node.children[char]
            # Delete current node if:
            # 1. It's not end of another word
            # 2. It has no other children
            return len(node.children) == 0 and not node.is_end_of_word

        return False

    return _delete(self.root, word, 0)
```

### Trie Variations

#### 1. Wildcard Search (with '.')

```python
def search_with_wildcard(self, word: str) -> bool:
    """'.' matches any character."""
    def dfs(node, i):
        if i == len(word):
            return node.is_end_of_word

        if word[i] == '.':
            # Try all possible characters
            for child in node.children.values():
                if dfs(child, i + 1):
                    return True
            return False
        else:
            if word[i] not in node.children:
                return False
            return dfs(node.children[word[i]], i + 1)

    return dfs(self.root, 0)
```

#### 2. Autocomplete

```python
def autocomplete(self, prefix: str, limit: int = 5) -> list:
    """Return up to 'limit' words starting with prefix."""
    # Navigate to prefix node
    node = self.root
    for char in prefix:
        if char not in node.children:
            return []
        node = node.children[char]

    # DFS to collect all words from this node
    results = []

    def dfs(node, path):
        if len(results) >= limit:
            return
        if node.is_end_of_word:
            results.append(prefix + path)
        for char, child in node.children.items():
            dfs(child, path + char)

    dfs(node, "")
    return results
```

#### 3. Count Words with Prefix

```python
def count_with_prefix(self, prefix: str) -> int:
    """Count words starting with prefix."""
    node = self.root
    for char in prefix:
        if char not in node.children:
            return 0
        node = node.children[char]

    # Count all words from this node
    def count_words(node):
        count = 1 if node.is_end_of_word else 0
        for child in node.children.values():
            count += count_words(child)
        return count

    return count_words(node)
```

### Time and Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(m) | O(m) per word |
| Search | O(m) | O(1) |
| StartsWith | O(m) | O(1) |
| Delete | O(m) | O(1) |
| Autocomplete | O(ALPHABET_SIZE * n) | O(n) for results |

Where:
- m = length of word
- n = number of words with prefix
- ALPHABET_SIZE = 26 for lowercase letters

**Overall Space:** O(ALPHABET_SIZE * m * n) in worst case, but typically much less due to shared prefixes.

### When to Use Trie

**Use Trie when:**
- Need fast prefix matching
- Implementing autocomplete
- Spell checking
- IP routing (longest prefix match)
- String searching with patterns

**Don't use Trie when:**
- Only exact matching needed (use hash table)
- Memory is very limited
- Small dataset (hash table is simpler)

### Real-World Applications

1. **Autocomplete Systems**: Search engines, IDEs
2. **Spell Checkers**: Dictionary lookup and suggestions
3. **IP Routing**: Longest prefix matching for routing tables
4. **Phone Directory**: T9 predictive text
5. **Browser History**: URL suggestions

---

## Segment Trees

### What is a Segment Tree?

A **Segment Tree** is a binary tree used for storing intervals or segments. It efficiently answers range queries (sum, min, max, GCD) and allows updates in O(log n) time.

### Structure

For array: [1, 3, 5, 7, 9, 11]

```
                [0,5] = 36
              /              \
        [0,2] = 9           [3,5] = 27
        /      \            /        \
    [0,1]=4  [2,2]=5   [3,4]=16   [5,5]=11
    /    \              /      \
[0,0]=1 [1,1]=3    [3,3]=7  [4,4]=9
```

Each node represents a range and stores the aggregate value for that range.

### Implementation

```python
class SegmentTree:
    def __init__(self, arr):
        """Build segment tree from array. O(n)."""
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # Safe size
        if arr:
            self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        """Build tree recursively."""
        if start == end:
            # Leaf node
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            self._build(arr, left_child, start, mid)
            self._build(arr, right_child, mid + 1, end)

            # Merge operation (sum in this case)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, index, value):
        """Update value at index. O(log n)."""
        self._update(0, 0, self.n - 1, index, value)

    def _update(self, node, start, end, index, value):
        """Update recursively."""
        if start == end:
            # Leaf node - update value
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            if index <= mid:
                self._update(left_child, start, mid, index, value)
            else:
                self._update(right_child, mid + 1, end, index, value)

            # Recalculate current node
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, left, right):
        """Query sum in range [left, right]. O(log n)."""
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        """Query recursively."""
        # No overlap
        if right < start or left > end:
            return 0

        # Complete overlap
        if left <= start and end <= right:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        left_sum = self._query(2 * node + 1, start, mid, left, right)
        right_sum = self._query(2 * node + 2, mid + 1, end, left, right)
        return left_sum + right_sum
```

### Segment Tree Variations

#### 1. Range Minimum Query (RMQ)

```python
class SegmentTreeMin:
    def _merge(self, left_val, right_val):
        return min(left_val, right_val)

    def _query(self, node, start, end, left, right):
        if right < start or left > end:
            return float('inf')  # Neutral element for min
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_min = self._query(2 * node + 1, start, mid, left, right)
        right_min = self._query(2 * node + 2, mid + 1, end, left, right)
        return min(left_min, right_min)
```

#### 2. Lazy Propagation

For range updates efficiently:

```python
class SegmentTreeLazy:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)  # Lazy array
        self._build(arr, 0, 0, self.n - 1)

    def _push(self, node, start, end):
        """Push lazy value down to children."""
        if self.lazy[node] != 0:
            # Apply pending update
            self.tree[node] += (end - start + 1) * self.lazy[node]

            if start != end:  # Not a leaf
                # Pass to children
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]

            self.lazy[node] = 0  # Clear lazy value

    def range_update(self, left, right, value):
        """Add value to range [left, right]. O(log n)."""
        self._range_update(0, 0, self.n - 1, left, right, value)

    def _range_update(self, node, start, end, left, right, value):
        self._push(node, start, end)

        if right < start or left > end:
            return

        if left <= start and end <= right:
            # Complete overlap - lazy update
            self.lazy[node] += value
            self._push(node, start, end)
            return

        # Partial overlap
        mid = (start + end) // 2
        self._range_update(2 * node + 1, start, mid, left, right, value)
        self._range_update(2 * node + 2, mid + 1, end, left, right, value)

        # Recalculate
        self._push(2 * node + 1, start, mid)
        self._push(2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
```

### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Build | O(n) | O(4n) |
| Point Update | O(log n) | O(1) |
| Range Query | O(log n) | O(1) |
| Range Update (Lazy) | O(log n) | O(1) |

### When to Use Segment Tree

**Use when:**
- Need range queries (sum, min, max, GCD)
- Need updates (point or range)
- Array doesn't change frequently
- Can afford O(n) space

**Don't use when:**
- Only point queries (use array)
- Only prefix queries (use Fenwick tree)
- Space is critical constraint

---

## Fenwick Trees (Binary Indexed Trees)

### What is a Fenwick Tree?

A **Fenwick Tree** or **Binary Indexed Tree (BIT)** efficiently calculates prefix sums and handles updates. It's simpler and more space-efficient than segment trees for this specific use case.

### Key Insight

Fenwick tree uses the binary representation of indices to store cumulative information. Each index is responsible for a range determined by its least significant bit (LSB).

### Structure

For array: [3, 2, -1, 6, 5, 4, -3, 3]

```
Index:  1  2  3  4  5  6  7  8
Array:  3  2 -1  6  5  4 -3  3
BIT:    3  5 -1 10  5  9 -3 19
```

Each BIT[i] stores sum of elements in range determined by LSB of i.

### Implementation

```python
class FenwickTree:
    def __init__(self, n):
        """Initialize Fenwick tree for n elements. O(n)."""
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed

    def update(self, index, delta):
        """Add delta to element at index. O(log n)."""
        index += 1  # Convert to 1-indexed
        while index <= self.n:
            self.tree[index] += delta
            index += index & (-index)  # Add LSB

    def prefix_sum(self, index):
        """Get sum of elements [0, index]. O(log n)."""
        index += 1  # Convert to 1-indexed
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)  # Remove LSB
        return total

    def range_sum(self, left, right):
        """Get sum in range [left, right]. O(log n)."""
        if left == 0:
            return self.prefix_sum(right)
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
```

### Building from Array

```python
def build_from_array(arr):
    """Build Fenwick tree from array. O(n)."""
    n = len(arr)
    tree = FenwickTree(n)
    for i, val in enumerate(arr):
        tree.update(i, val)
    return tree

# Or more efficient:
class FenwickTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (self.n + 1)
        # Build in O(n)
        for i, val in enumerate(arr):
            self.tree[i + 1] = val
        for i in range(1, self.n + 1):
            j = i + (i & -i)
            if j <= self.n:
                self.tree[j] += self.tree[i]
```

### Understanding LSB Operation

```python
def get_lsb(x):
    """Get least significant bit."""
    return x & (-x)

# Examples:
# 6 (110) -> LSB = 2 (010)
# 8 (1000) -> LSB = 8 (1000)
# 5 (101) -> LSB = 1 (001)
```

### 2D Fenwick Tree

For 2D range sum queries:

```python
class FenwickTree2D:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tree = [[0] * (cols + 1) for _ in range(rows + 1)]

    def update(self, row, col, delta):
        """Update point (row, col). O(log m * log n)."""
        i = row + 1
        while i <= self.rows:
            j = col + 1
            while j <= self.cols:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def prefix_sum(self, row, col):
        """Sum of rectangle from (0,0) to (row, col)."""
        total = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                total += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return total

    def range_sum(self, r1, c1, r2, c2):
        """Sum in rectangle from (r1,c1) to (r2,c2)."""
        return (self.prefix_sum(r2, c2)
                - self.prefix_sum(r1 - 1, c2)
                - self.prefix_sum(r2, c1 - 1)
                + self.prefix_sum(r1 - 1, c1 - 1))
```

### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Build | O(n) or O(n log n) | O(n) |
| Update | O(log n) | O(1) |
| Prefix Sum | O(log n) | O(1) |
| Range Sum | O(log n) | O(1) |

### Fenwick vs Segment Tree

| Feature | Fenwick Tree | Segment Tree |
|---------|--------------|--------------|
| Space | O(n) | O(4n) |
| Code Complexity | Simpler | More complex |
| Range Queries | Prefix sums | Any associative op |
| Range Updates | Harder | Easy with lazy prop |
| Use Case | Prefix sums | General range queries |

---

## AVL Trees

### What is an AVL Tree?

An **AVL tree** is a self-balancing Binary Search Tree where the heights of left and right subtrees differ by at most 1. Named after inventors Adelson-Velsky and Landis.

### Balance Factor

```python
balance_factor = height(left_subtree) - height(right_subtree)
```

For AVL tree: -1 ≤ balance_factor ≤ 1

### AVL Node Structure

```python
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # Height of node
```

### Rotations

Four types of rotations to restore balance:

#### 1. Left-Left (LL) Case - Right Rotation

```
       z                   y
      / \                 / \
     y   T4    =>        x   z
    / \                 / \ / \
   x   T3              T1 T2 T3 T4
  / \
 T1  T2
```

```python
def right_rotate(z):
    y = z.left
    T3 = y.right

    # Perform rotation
    y.right = z
    z.left = T3

    # Update heights
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y  # New root
```

#### 2. Right-Right (RR) Case - Left Rotation

```
   z                       y
  / \                     / \
 T1  y        =>         z   x
    / \                 / \ / \
   T2  x               T1 T2 T3 T4
      / \
     T3 T4
```

```python
def left_rotate(z):
    y = z.right
    T2 = y.left

    # Perform rotation
    y.left = z
    z.right = T2

    # Update heights
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y  # New root
```

#### 3. Left-Right (LR) Case - Left then Right Rotation

```
     z                    z                   x
    / \                  / \                 / \
   y   T4    =>         x   T4    =>        y   z
  / \                  / \                 / \ / \
 T1  x                y   T3              T1 T2 T3 T4
    / \              / \
   T2 T3            T1 T2
```

```python
# First left rotate on left child, then right rotate on root
z.left = left_rotate(z.left)
return right_rotate(z)
```

#### 4. Right-Left (RL) Case - Right then Left Rotation

```
   z                    z                     x
  / \                  / \                   / \
 T1  y      =>        T1  x       =>        z   y
    / \                  / \               / \ / \
   x   T4               T2  y             T1 T2 T3 T4
  / \                      / \
 T2 T3                    T3 T4
```

```python
# First right rotate on right child, then left rotate on root
z.right = right_rotate(z.right)
return left_rotate(z)
```

### AVL Tree Implementation

```python
class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def insert(self, val):
        """Insert value and rebalance. O(log n)."""
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        # 1. Normal BST insertion
        if not node:
            return AVLNode(val)

        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        else:
            return node  # Duplicate not allowed

        # 2. Update height
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        # 3. Get balance factor
        balance = self.get_balance(node)

        # 4. Balance if needed
        # Left-Left Case
        if balance > 1 and val < node.left.val:
            return self.right_rotate(node)

        # Right-Right Case
        if balance < -1 and val > node.right.val:
            return self.left_rotate(node)

        # Left-Right Case
        if balance > 1 and val > node.left.val:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right-Left Case
        if balance < -1 and val < node.right.val:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node
```

### Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Search | O(log n) | O(log n) |
| Insert | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |
| Space | O(n) | O(n) |

### AVL vs Red-Black Tree

| Feature | AVL | Red-Black |
|---------|-----|-----------|
| Balance | Strict (∆h ≤ 1) | Looser |
| Rotations | More on insert | Fewer on insert |
| Search | Faster | Slightly slower |
| Insert/Delete | Slower | Faster |
| Use Case | Read-heavy | Write-heavy |

---

## Red-Black Trees

### Properties

A Red-Black tree is a BST with these properties:

1. Every node is either RED or BLACK
2. Root is always BLACK
3. All leaves (NIL) are BLACK
4. RED node cannot have RED children
5. Every path from node to descendant leaves has same number of BLACK nodes (black height)

### Why Red-Black Trees?

- Guarantee O(log n) operations
- Less strict than AVL (fewer rotations)
- Used in C++ STL map, Java TreeMap
- Height ≤ 2 * log(n + 1)

### Implementation Overview

Due to complexity, full implementation not typically required in interviews. Understanding properties and use cases is more important.

```python
class RBNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = "RED"  # New nodes are red
```

### When to Use

**Use AVL when:**
- Search-intensive application
- Need strict balancing
- Slightly slower inserts/deletes acceptable

**Use Red-Black when:**
- Insert/delete intensive
- Standard library implementation available
- Slightly slower searches acceptable

---

## B-Trees and B+ Trees

### B-Tree

A **B-Tree** is a self-balancing tree optimized for systems that read/write large blocks of data (databases, file systems).

### Properties

For B-Tree of order m:
- Each node has at most m children
- Each internal node (except root) has at least ⌈m/2⌉ children
- Root has at least 2 children (unless it's a leaf)
- All leaves at same level
- Internal node with k children has k-1 keys

### B+ Tree

Similar to B-Tree but:
- All values stored in leaves
- Internal nodes only store keys for navigation
- Leaves linked for efficient range scans
- Better for databases (MySQL, PostgreSQL)

### When to Use

**B-Trees:**
- Database indexing
- File systems
- When data doesn't fit in memory
- Need efficient range queries on disk

**B+ Trees:**
- Database systems (most common)
- Range scans needed
- Sequential access important

---

## Summary

### Comparison Table

| Structure | Best For | Time (Search) | Time (Insert) | Space |
|-----------|----------|---------------|---------------|-------|
| Trie | Prefix matching | O(m) | O(m) | O(ALPHABET * m * n) |
| Segment Tree | Range queries | O(log n) | O(log n) | O(4n) |
| Fenwick Tree | Prefix sums | O(log n) | O(log n) | O(n) |
| AVL Tree | Read-heavy BST | O(log n) | O(log n) | O(n) |
| Red-Black | Write-heavy BST | O(log n) | O(log n) | O(n) |
| B/B+ Tree | Disk storage | O(log n) | O(log n) | O(n) |

### Interview Focus

**High Priority:**
1. Trie - Implementation and variations
2. Segment Tree - Range queries
3. Fenwick Tree - Prefix sums

**Medium Priority:**
4. AVL - Understanding rotations
5. Red-Black - Properties and comparisons

**Low Priority:**
6. B/B+ Trees - Conceptual understanding

Understanding these advanced trees opens up solutions to complex problems and is essential for senior-level interviews.
