# Chapter 34: Advanced Trees - Solutions

## Table of Contents
1. [Easy Problems](#easy-problems)
2. [Medium Problems](#medium-problems)
3. [Hard Problems](#hard-problems)

---

## Easy Problems

### 1. Implement Trie (Prefix Tree)
**LeetCode:** 208 | **Difficulty:** Easy

**Problem:**
Implement a trie with `insert`, `search`, and `startsWith` methods.

**Solution:**
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Time Complexity:
    - insert: O(m) where m = word length
    - search: O(m)
    - startsWith: O(m)

    Space Complexity: O(ALPHABET_SIZE * m * n) where n = number of words
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
        """Return True if word exists in trie."""
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
```

**Explanation:**
- Use dictionary for children (more flexible than fixed array)
- `is_end_of_word` marks complete words
- For `startsWith`, don't check `is_end_of_word` flag

**Alternative Approach (Array-based for lowercase letters):**
```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # For 'a' to 'z'
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end_of_word = True
```

---

### 2. Longest Common Prefix
**LeetCode:** 14 | **Difficulty:** Easy

**Solution 1: Horizontal Scanning**
```python
def longest_common_prefix(strs):
    """
    Time: O(S) where S = sum of all characters
    Space: O(1)
    """
    if not strs:
        return ""

    prefix = strs[0]
    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
```

**Solution 2: Using Trie**
```python
def longest_common_prefix(strs):
    """
    Time: O(S) where S = sum of all characters
    Space: O(S) for trie
    """
    if not strs:
        return ""

    # Build trie
    root = TrieNode()
    for word in strs:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Find common path
    prefix = []
    node = root

    while len(node.children) == 1 and not node.is_end_of_word:
        char = list(node.children.keys())[0]
        prefix.append(char)
        node = node.children[char]

    return ''.join(prefix)
```

---

### 3. Range Sum Query - Immutable
**LeetCode:** 303 | **Difficulty:** Easy

**Solution:**
```python
class NumArray:
    """
    Time: O(n) for __init__, O(1) for sumRange
    Space: O(n)
    """

    def __init__(self, nums):
        # Build prefix sum array
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sum_range(self, left: int, right: int) -> int:
        """Sum of elements from index left to right inclusive."""
        return self.prefix[right + 1] - self.prefix[left]
```

**Explanation:**
- `prefix[i]` stores sum of elements from index 0 to i-1
- `sum(left, right) = prefix[right+1] - prefix[left]`
- Example: nums = [1, 2, 3, 4]
  - prefix = [0, 1, 3, 6, 10]
  - sum(1, 2) = prefix[3] - prefix[1] = 6 - 1 = 5 (2 + 3)

---

### 4. Range Sum Query - Mutable
**LeetCode:** 307 | **Difficulty:** Medium

**Solution 1: Segment Tree**
```python
class NumArray:
    """
    Time: O(n) build, O(log n) update/query
    Space: O(n)
    """

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.nums = nums
        if nums:
            self._build(0, 0, self.n - 1)

    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = self.nums[start]
        else:
            mid = (start + end) // 2
            self._build(2 * node + 1, start, mid)
            self._build(2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index: int, val: int) -> None:
        self._update(0, 0, self.n - 1, index, val)

    def _update(self, node, start, end, index, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if index <= mid:
                self._update(2 * node + 1, start, mid, index, val)
            else:
                self._update(2 * node + 2, mid + 1, end, index, val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def sum_range(self, left: int, right: int) -> int:
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        if right < start or left > end:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return (self._query(2 * node + 1, start, mid, left, right) +
                self._query(2 * node + 2, mid + 1, end, left, right))
```

**Solution 2: Fenwick Tree (Binary Indexed Tree)**
```python
class NumArray:
    """
    Time: O(n log n) build, O(log n) update/query
    Space: O(n)
    """

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = [0] * self.n
        self.tree = [0] * (self.n + 1)

        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val

        index += 1  # Fenwick tree is 1-indexed
        while index <= self.n:
            self.tree[index] += delta
            index += index & (-index)

    def sum_range(self, left: int, right: int) -> int:
        def prefix_sum(i):
            s = 0
            i += 1
            while i > 0:
                s += self.tree[i]
                i -= i & (-i)
            return s

        return prefix_sum(right) - (prefix_sum(left - 1) if left > 0 else 0)
```

---

### 5. Count Nodes Equal to Average of Subtree
**LeetCode:** 2265 | **Difficulty:** Medium

**Solution:**
```python
def average_of_subtree(root):
    """
    Time: O(n) - visit each node once
    Space: O(h) - recursion stack
    """
    result = 0

    def dfs(node):
        nonlocal result
        if not node:
            return 0, 0  # sum, count

        left_sum, left_count = dfs(node.left)
        right_sum, right_count = dfs(node.right)

        total_sum = left_sum + right_sum + node.val
        total_count = left_count + right_count + 1

        # Check if current node equals average
        if node.val == total_sum // total_count:
            result += 1

        return total_sum, total_count

    dfs(root)
    return result
```

**Explanation:**
- Return tuple `(sum, count)` from each subtree
- Check if `node.val == sum // count` (integer division)
- Use `nonlocal` to track result count

---

### 6. Shortest Word Distance II
**Difficulty:** Medium

**Solution:**
```python
class WordDistance:
    """
    Time: O(n) init, O(m + n) shortest where m, n = word occurrences
    Space: O(n) for storing all indices
    """

    def __init__(self, words_dict):
        from collections import defaultdict
        self.locations = defaultdict(list)

        for i, word in enumerate(words_dict):
            self.locations[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        loc1 = self.locations[word1]
        loc2 = self.locations[word2]

        # Two pointers on two sorted lists
        i, j = 0, 0
        min_dist = float('inf')

        while i < len(loc1) and j < len(loc2):
            min_dist = min(min_dist, abs(loc1[i] - loc2[j]))

            # Move pointer with smaller index
            if loc1[i] < loc2[j]:
                i += 1
            else:
                j += 1

        return min_dist
```

---

### 7. Design Add and Search Words Data Structure
**LeetCode:** 211 | **Difficulty:** Medium

**Solution:**
```python
class WordDictionary:
    """
    Time: O(m) for add, O(26^k) for search with k wildcards
    Space: O(total chars)
    """

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end_of_word

            if word[i] == '.':
                # Try all possible children
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

**Explanation:**
- For wildcard '.', try all children nodes
- Use DFS to explore all possible matches
- Return True as soon as valid match found

---

### 8. Map Sum Pairs
**LeetCode:** 677 | **Difficulty:** Medium

**Solution:**
```python
class MapSum:
    """
    Time: O(m) for insert, O(m) for sum
    Space: O(total chars)
    """

    def __init__(self):
        self.root = TrieNode()
        self.map = {}  # Store actual values for update handling

    def insert(self, key: str, val: int) -> None:
        # Calculate delta for update
        delta = val - self.map.get(key, 0)
        self.map[key] = val

        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sum += delta  # Update cumulative sum
        node.is_end_of_word = True

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.sum


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.sum = 0
```

---

## Medium Problems

### 9. Replace Words
**LeetCode:** 648 | **Difficulty:** Medium

**Solution:**
```python
def replace_words(dictionary, sentence):
    """
    Time: O(n + m) where n = total chars in dictionary, m = sentence length
    Space: O(n)
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
                return word
            node = node.children[char]
            prefix.append(char)
            if node.is_end_of_word:
                return ''.join(prefix)

        return word

    words = sentence.split()
    return ' '.join(find_root(word) for word in words)
```

**Explanation:**
- Build trie from dictionary
- For each word, find shortest matching root
- Stop at first complete word in trie

---

### 10. Implement Trie II (Prefix Tree)
**LeetCode:** 1804 | **Difficulty:** Medium

**Solution:**
```python
class Trie:
    """
    Time: O(m) for all operations
    Space: O(total chars)
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        node.word_count += 1

    def count_words_equal_to(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.word_count

    def count_words_starting_with(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.prefix_count

    def erase(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
            node.prefix_count -= 1
        node.word_count -= 1


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_count = 0      # How many times word ends here
        self.prefix_count = 0    # How many words pass through here
```

---

### 11. Word Search II
**LeetCode:** 212 | **Difficulty:** Hard

**Solution:**
```python
def find_words(board, words):
    """
    Time: O(m * n * 4^L) where L = max word length
    Space: O(total chars in words)
    """
    # Build trie
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    def dfs(i, j, node):
        if node.is_end_of_word:
            result.add(node.word)
            # Optional: remove word from trie to avoid duplicates
            node.is_end_of_word = False

        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if board[i][j] not in node.children:
            return

        char = board[i][j]
        board[i][j] = '#'  # Mark visited

        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            dfs(i + di, j + dj, node.children[char])

        board[i][j] = char  # Restore

    m, n = len(board), len(board[0])
    result = set()

    for i in range(m):
        for j in range(n):
            dfs(i, j, root)

    return list(result)
```

**Optimization:**
- Prune trie nodes after finding words
- Use set to avoid duplicate results
- Mark visited cells with '#'

---

### 12. Range Sum Query 2D - Immutable
**LeetCode:** 304 | **Difficulty:** Medium

**Solution:**
```python
class NumMatrix:
    """
    Time: O(mn) init, O(1) query
    Space: O(mn)
    """

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.prefix = [[]]
            return

        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = (matrix[i-1][j-1] +
                                    self.prefix[i-1][j] +
                                    self.prefix[i][j-1] -
                                    self.prefix[i-1][j-1])

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return (self.prefix[row2][col2] -
                self.prefix[row1-1][col2] -
                self.prefix[row2][col1-1] +
                self.prefix[row1-1][col1-1])
```

**Explanation:**
- `prefix[i][j]` = sum from (0,0) to (i-1, j-1)
- Use inclusion-exclusion principle
- Add 1 to indices to handle 1-indexed prefix array

---

### 13. Range Sum Query 2D - Mutable
**LeetCode:** 308 | **Difficulty:** Hard

**Solution:**
```python
class NumMatrix:
    """
    Time: O(mn) init, O(log m * log n) update/query
    Space: O(mn)
    """

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return

        self.m, self.n = len(matrix), len(matrix[0])
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        self.matrix = [[0] * self.n for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val

        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def prefix_sum(row, col):
            s = 0
            i = row + 1
            while i > 0:
                j = col + 1
                while j > 0:
                    s += self.tree[i][j]
                    j -= j & (-j)
                i -= i & (-i)
            return s

        return (prefix_sum(row2, col2) -
                prefix_sum(row1 - 1, col2) if row1 > 0 else prefix_sum(row2, col2)) - \
               (prefix_sum(row2, col1 - 1) if col1 > 0 else 0) + \
               (prefix_sum(row1 - 1, col1 - 1) if row1 > 0 and col1 > 0 else 0)
```

---

### 14. Count of Smaller Numbers After Self
**LeetCode:** 315 | **Difficulty:** Hard

**Solution:**
```python
def count_smaller(nums):
    """
    Time: O(n log m) where m = range of values
    Space: O(m)
    """
    # Coordinate compression
    sorted_nums = sorted(set(nums))
    rank = {v: i for i, v in enumerate(sorted_nums)}

    n = len(sorted_nums)
    tree = [0] * (n + 1)

    def update(i):
        i += 1
        while i <= n:
            tree[i] += 1
            i += i & (-i)

    def query(i):
        if i < 0:
            return 0
        s = 0
        i += 1
        while i > 0:
            s += tree[i]
            i -= i & (-i)
        return s

    result = []
    for num in reversed(nums):
        r = rank[num]
        # Count smaller elements
        count = query(r - 1)
        result.append(count)
        # Add current number
        update(r)

    return result[::-1]
```

**Explanation:**
- Use coordinate compression to map values to small range
- Process from right to left
- Query count < current, then insert current

---

## Hard Problems

### 21. Maximum XOR of Two Numbers in Array
**LeetCode:** 421 | **Difficulty:** Medium

**Solution:**
```python
def find_maximum_xor(nums):
    """
    Time: O(32n) = O(n)
    Space: O(32n) = O(n)
    """
    class TrieNode:
        def __init__(self):
            self.children = {}

    root = TrieNode()

    # Insert all numbers into binary trie
    for num in nums:
        node = root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    max_xor = 0

    # For each number, find maximum XOR
    for num in nums:
        node = root
        current_xor = 0

        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # Try to go opposite direction for max XOR
            opposite = 1 - bit

            if opposite in node.children:
                current_xor |= (1 << i)
                node = node.children[opposite]
            else:
                node = node.children[bit]

        max_xor = max(max_xor, current_xor)

    return max_xor
```

**Explanation:**
- Build binary trie with 0/1 children
- For each number, greedily choose opposite bits
- Track maximum XOR found

---

### 22. Stream of Characters
**LeetCode:** 1032 | **Difficulty:** Hard

**Solution:**
```python
class StreamChecker:
    """
    Time: O(m) init where m = total chars, O(max_word_len) query
    Space: O(m)
    """

    def __init__(self, words):
        self.root = TrieNode()
        self.stream = []
        self.max_len = 0

        # Build trie with reversed words
        for word in words:
            node = self.root
            self.max_len = max(self.max_len, len(word))
            for char in reversed(word):
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)

        # Keep only last max_len characters
        if len(self.stream) > self.max_len:
            self.stream.pop(0)

        # Search from end of stream
        node = self.root
        for i in range(len(self.stream) - 1, -1, -1):
            char = self.stream[i]
            if char not in node.children:
                return False
            node = node.children[char]
            if node.is_end_of_word:
                return True

        return False
```

**Explanation:**
- Reverse words when building trie
- Store recent characters in stream
- Search from end for suffix matching

---

### 23. The Skyline Problem
**LeetCode:** 218 | **Difficulty:** Hard

**Solution:**
```python
def get_skyline(buildings):
    """
    Time: O(n log n)
    Space: O(n)
    """
    from heapq import heappush, heappop
    from collections import defaultdict

    # Create events: (x, start/end, height)
    events = []
    for left, right, height in buildings:
        events.append((left, 0, height))    # Start event
        events.append((right, 1, height))   # End event

    # Sort: x ascending, starts before ends, higher heights first
    events.sort(key=lambda x: (x[0], x[1], -x[2] if x[1] == 0 else x[2]))

    result = []
    max_heap = [0]  # Active heights
    height_count = defaultdict(int)
    height_count[0] = 1

    for x, event_type, h in events:
        if event_type == 0:  # Start
            heappush(max_heap, -h)
            height_count[h] += 1
        else:  # End
            height_count[h] -= 1
            if height_count[h] == 0:
                del height_count[h]

        # Find current max height
        while max_heap and -max_heap[0] not in height_count:
            heappop(max_heap)

        current_max = -max_heap[0]

        # Add to result if height changed
        if not result or result[-1][1] != current_max:
            result.append([x, current_max])

    return result
```

---

### 24. Palindrome Pairs
**LeetCode:** 336 | **Difficulty:** Hard

**Solution:**
```python
def palindrome_pairs(words):
    """
    Time: O(n * k^2) where n = number of words, k = max word length
    Space: O(n * k)
    """
    def is_palindrome(s):
        return s == s[::-1]

    word_dict = {word: i for i, word in enumerate(words)}
    result = []

    for i, word in enumerate(words):
        # Check all splits of current word
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]

            # If prefix is palindrome, check if reversed suffix exists
            if is_palindrome(prefix):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_dict and word_dict[reversed_suffix] != i:
                    result.append([word_dict[reversed_suffix], i])

            # If suffix is palindrome, check if reversed prefix exists
            # j != len(word) to avoid duplicate when j = len(word)
            if j != len(word) and is_palindrome(suffix):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_dict and word_dict[reversed_prefix] != i:
                    result.append([i, word_dict[reversed_prefix]])

    return result
```

---

## Summary

**Key Patterns:**
1. **Trie Construction**: Build from words, use for prefix matching
2. **Segment Tree**: Range queries with updates
3. **Fenwick Tree**: Efficient prefix sums
4. **Binary Trie**: For XOR problems
5. **Reversed Trie**: For suffix matching

**Complexity Tips:**
- Trie operations: O(m) where m = word length
- Segment Tree: O(log n) query/update
- Fenwick Tree: O(log n) operations
- Binary Trie: O(32) = O(1) for integers

**Common Mistakes:**
- Forgetting to mark end of words in trie
- Not handling updates in mutable range queries
- Missing coordinate compression for large ranges
- Incorrect handling of wildcards in search
