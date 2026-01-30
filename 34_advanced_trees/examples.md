# Chapter 34: Advanced Trees - Examples

## Table of Contents
1. [Trie Implementation](#trie-implementation)
2. [Trie Advanced Operations](#trie-advanced-operations)
3. [Segment Tree Implementation](#segment-tree-implementation)
4. [Fenwick Tree Implementation](#fenwick-tree-implementation)
5. [AVL Tree Rotations](#avl-tree-rotations)

---

## Trie Implementation

### Example 1: Basic Trie

```python
class TrieNode:
    """Node in a Trie."""
    def __init__(self):
        self.children = {}  # Map from char to TrieNode
        self.is_end_of_word = False


class Trie:
    """
    Implement a trie with insert, search, and startsWith methods.

    Time: O(m) for all operations where m = word length
    Space: O(ALPHABET_SIZE * m * n) where n = number of words
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert word into trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Return True if word is in trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Return True if any word starts with prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("application")

print(trie.search("apple"))        # True
print(trie.search("app"))          # True
print(trie.search("appl"))         # False
print(trie.starts_with("appl"))    # True
print(trie.starts_with("ban"))     # False
```

### Example 2: Word Search II (Using Trie)

```python
def find_words(board, words):
    """
    Find all words from list that exist in 2D board.

    Time: O(m * n * 4^L) where L = max word length
    Space: O(total chars in words)

    This is significantly faster than checking each word individually.
    """
    # Build trie from words
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word  # Store word at end

    def dfs(i, j, node):
        """DFS to find words starting from (i, j)."""
        if node.is_end_of_word:
            result.add(node.word)

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] not in node.children:
            return

        char = board[i][j]
        board[i][j] = '#'  # Mark visited

        # Explore all 4 directions
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            dfs(i + di, j + dj, node.children[char])

        board[i][j] = char  # Restore

    result = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, root)

    return list(result)


# Example:
board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
words = ["oath", "pea", "eat", "rain"]
print(find_words(board, words))  # ["oath", "eat"]
```

### Example 3: Autocomplete System

```python
class AutocompleteSystem:
    """
    Design autocomplete system that returns top 3 historical hot sentences.

    Time: O(m) for input, O(n log k) for search where n = matching sentences
    Space: O(total chars in all sentences)
    """

    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.current = self.root
        self.search_term = ""

        # Build trie with frequencies
        for sentence, time in zip(sentences, times):
            self._add(sentence, time)

    def _add(self, sentence, time):
        """Add sentence with frequency to trie."""
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.sentence = sentence
        node.freq = node.freq + time if hasattr(node, 'freq') else time

    def input(self, c: str):
        """
        User inputs character c.
        Return top 3 historical hot sentences with prefix.
        """
        if c == '#':
            # End of sentence, add to trie
            self._add(self.search_term, 1)
            self.search_term = ""
            self.current = self.root
            return []

        self.search_term += c

        if self.current and c in self.current.children:
            self.current = self.current.children[c]
        else:
            self.current = None
            return []

        # Find all sentences with current prefix
        results = []

        def dfs(node):
            if node.is_end_of_word:
                results.append((node.freq, node.sentence))
            for child in node.children.values():
                dfs(child)

        dfs(self.current)

        # Sort by frequency (desc) then lexicographically
        results.sort(key=lambda x: (-x[0], x[1]))
        return [sentence for _, sentence in results[:3]]


# Example usage:
system = AutocompleteSystem(
    ["i love you", "island", "iroman", "i love leetcode"],
    [5, 3, 2, 2]
)

print(system.input('i'))   # ["i love you", "island", "i love leetcode"]
print(system.input(' '))   # ["i love you", "i love leetcode"]
print(system.input('a'))   # []
print(system.input('#'))   # []
```

---

## Trie Advanced Operations

### Example 4: Word Dictionary with Wildcard Search

```python
class WordDictionary:
    """
    Add and search words. '.' matches any letter.

    Time: O(m) for add, O(m * 26^k) for search with k wildcards
    Space: O(total chars)
    """

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        """Add word to dictionary."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Search word. '.' matches any letter."""
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


# Example:
wd = WordDictionary()
wd.add_word("bad")
wd.add_word("dad")
wd.add_word("mad")

print(wd.search("pad"))   # False
print(wd.search("bad"))   # True
print(wd.search(".ad"))   # True
print(wd.search("b.."))   # True
```

### Example 5: Replace Words (Trie Application)

```python
def replace_words(dictionary, sentence):
    """
    Replace words with their roots from dictionary.

    Time: O(n + m) where n = total chars in dictionary, m = sentence length
    Space: O(n)

    Example:
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    Output: "the cat was rat by the bat"
    """
    # Build trie
    root = TrieNode()
    for word in dictionary:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def find_root(word):
        """Find shortest root for word."""
        node = root
        prefix = []

        for char in word:
            if char not in node.children:
                return word  # No root found
            node = node.children[char]
            prefix.append(char)
            if node.is_end_of_word:
                return ''.join(prefix)  # Found root

        return word  # Word is shorter than any root

    words = sentence.split()
    return ' '.join(find_root(word) for word in words)


# Example:
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(replace_words(dictionary, sentence))
# Output: "the cat was rat by the bat"
```

---

## Segment Tree Implementation

### Example 6: Range Sum Query with Updates

```python
class SegmentTree:
    """
    Segment tree for range sum queries with point updates.

    Time: O(n) build, O(log n) query/update
    Space: O(4n) = O(n)
    """

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        if arr:
            self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        """Build segment tree recursively."""
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            self._build(arr, left_child, start, mid)
            self._build(arr, right_child, mid + 1, end)

            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, index, value):
        """Update value at index."""
        self._update(0, 0, self.n - 1, index, value)

    def _update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            if index <= mid:
                self._update(left_child, start, mid, index, value)
            else:
                self._update(right_child, mid + 1, end, index, value)

            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, left, right):
        """Query sum in range [left, right]."""
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
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


# Example usage:
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

print(seg_tree.query(1, 3))   # 3 + 5 + 7 = 15
seg_tree.update(1, 10)         # Change 3 to 10
print(seg_tree.query(1, 3))   # 10 + 5 + 7 = 22
```

### Example 7: Range Minimum Query

```python
class SegmentTreeMin:
    """
    Segment tree for range minimum queries.

    Time: O(n) build, O(log n) query/update
    Space: O(n)
    """

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (4 * self.n)
        if arr:
            self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left = 2 * node + 1
            right = 2 * node + 2

            self._build(arr, left, start, mid)
            self._build(arr, right, mid + 1, end)

            self.tree[node] = min(self.tree[left], self.tree[right])

    def query_min(self, left, right):
        """Find minimum in range [left, right]."""
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        if right < start or left > end:
            return float('inf')

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_min = self._query(2 * node + 1, start, mid, left, right)
        right_min = self._query(2 * node + 2, mid + 1, end, left, right)
        return min(left_min, right_min)


# Example:
arr = [1, 3, 5, 2, 9, 11]
seg_tree = SegmentTreeMin(arr)

print(seg_tree.query_min(0, 3))   # min(1,3,5,2) = 1
print(seg_tree.query_min(2, 5))   # min(5,2,9,11) = 2
```

---

## Fenwick Tree Implementation

### Example 8: Basic Fenwick Tree

```python
class FenwickTree:
    """
    Binary Indexed Tree for prefix sums and point updates.

    Time: O(log n) for update and query
    Space: O(n)
    """

    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed

    def update(self, index, delta):
        """Add delta to element at index (0-indexed)."""
        index += 1  # Convert to 1-indexed
        while index <= self.n:
            self.tree[index] += delta
            index += index & (-index)  # Add LSB

    def prefix_sum(self, index):
        """Get sum of elements [0, index] (0-indexed)."""
        index += 1  # Convert to 1-indexed
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)  # Remove LSB
        return total

    def range_sum(self, left, right):
        """Get sum of elements [left, right] (0-indexed)."""
        if left == 0:
            return self.prefix_sum(right)
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


# Example usage:
# Array: [3, 2, -1, 6, 5, 4, -3, 3]
n = 8
fenwick = FenwickTree(n)

# Build from array
arr = [3, 2, -1, 6, 5, 4, -3, 3]
for i, val in enumerate(arr):
    fenwick.update(i, val)

print(fenwick.prefix_sum(2))      # 3 + 2 + (-1) = 4
print(fenwick.range_sum(2, 5))    # (-1) + 6 + 5 + 4 = 14

fenwick.update(2, 5)               # Change -1 to 4 (add 5)
print(fenwick.range_sum(2, 5))    # 4 + 6 + 5 + 4 = 19
```

### Example 9: Count Smaller Numbers After Self

```python
def count_smaller(nums):
    """
    For each element, count how many smaller elements appear after it.

    Time: O(n log m) where m = range of values
    Space: O(m)

    Example: nums = [5, 2, 6, 1]
    Output: [2, 1, 1, 0]
    Explanation: After 5 there are [2, 1] (2 numbers smaller)
    """
    # Coordinate compression
    sorted_nums = sorted(set(nums))
    rank = {v: i + 1 for i, v in enumerate(sorted_nums)}

    fenwick = FenwickTree(len(sorted_nums))
    result = []

    # Process from right to left
    for num in reversed(nums):
        r = rank[num]
        # Count numbers smaller than current (< r means index r-1)
        count = fenwick.prefix_sum(r - 2) if r > 1 else 0
        result.append(count)
        # Add current number
        fenwick.update(r - 1, 1)

    return result[::-1]


# Example:
nums = [5, 2, 6, 1]
print(count_smaller(nums))  # [2, 1, 1, 0]
```

---

## AVL Tree Rotations

### Example 10: AVL Tree with Rotations

```python
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
    Self-balancing AVL tree.

    Time: O(log n) for all operations
    Space: O(n)
    """

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, z):
        """Right rotation for LL case."""
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def left_rotate(self, z):
        """Left rotation for RR case."""
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, val):
        """Insert value and maintain balance."""
        # 1. Normal BST insertion
        if not root:
            return AVLNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        else:
            return root  # No duplicates

        # 2. Update height
        root.height = 1 + max(self.get_height(root.left),
                               self.get_height(root.right))

        # 3. Get balance factor
        balance = self.get_balance(root)

        # 4. Rebalance if needed
        # Left-Left Case
        if balance > 1 and val < root.left.val:
            return self.right_rotate(root)

        # Right-Right Case
        if balance < -1 and val > root.right.val:
            return self.left_rotate(root)

        # Left-Right Case
        if balance > 1 and val > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left Case
        if balance < -1 and val < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


# Example usage:
avl = AVLTree()
root = None

values = [10, 20, 30, 40, 50, 25]
for val in values:
    root = avl.insert(root, val)

# Tree is automatically balanced during insertions
```

---

These examples demonstrate the core implementations and practical applications of advanced tree structures. Practice these patterns to master advanced tree problems in interviews.
