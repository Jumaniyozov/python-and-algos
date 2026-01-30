# Chapter 34: Advanced Trees - Tips and Tricks

## Table of Contents
1. [Common Pitfalls](#common-pitfalls)
2. [Pattern Recognition](#pattern-recognition)
3. [Interview Tips](#interview-tips)
4. [Performance Optimization](#performance-optimization)
5. [LeetCode Practice Problems](#leetcode-practice-problems)

---

## Common Pitfalls

### 1. Forgetting to Mark End of Word in Trie

```python
# ❌ WRONG: Word not marked
def insert(self, word):
    node = self.root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    # Missing: node.is_end_of_word = True

# ✅ CORRECT: Mark end of word
def insert(self, word):
    node = self.root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True  # Essential!
```

### 2. Confusing startsWith and search in Trie

```python
# ❌ WRONG: Checking is_end_of_word for prefix
def starts_with(self, prefix):
    node = self.root
    for char in prefix:
        if char not in node.children:
            return False
        node = node.children[char]
    return node.is_end_of_word  # Wrong!

# ✅ CORRECT: Don't check is_end_of_word for prefix
def starts_with(self, prefix):
    node = self.root
    for char in prefix:
        if char not in node.children:
            return False
        node = node.children[char]
    return True  # Just need to reach end of prefix
```

### 3. Incorrect Segment Tree Size

```python
# ❌ WRONG: Tree too small
self.tree = [0] * (2 * n)  # May cause index out of bounds

# ✅ CORRECT: Safe size for segment tree
self.tree = [0] * (4 * n)  # Safe for all cases
```

### 4. Fenwick Tree Index Confusion

```python
# ❌ WRONG: Using 0-indexed directly
def update(self, i, delta):
    while i <= self.n:
        self.tree[i] += delta
        i += i & (-i)  # Wrong! i starts at 0

# ✅ CORRECT: Convert to 1-indexed
def update(self, i, delta):
    i += 1  # Convert to 1-indexed
    while i <= self.n:
        self.tree[i] += delta
        i += i & (-i)
```

### 5. Not Handling Empty Trie Prefix

```python
# ❌ WRONG: Crashes on empty prefix
def autocomplete(self, prefix):
    node = self.root
    for char in prefix:
        node = node.children[char]  # KeyError if not found!
    return self.collect_words(node)

# ✅ CORRECT: Check if prefix exists
def autocomplete(self, prefix):
    node = self.root
    for char in prefix:
        if char not in node.children:
            return []  # No words with this prefix
        node = node.children[char]
    return self.collect_words(node)
```

### 6. Missing Coordinate Compression

```python
# ❌ WRONG: Using values directly with large range
nums = [1000000, -5000000, 3000000]
tree = [0] * (max(nums) + 1)  # Huge memory!

# ✅ CORRECT: Use coordinate compression
sorted_nums = sorted(set(nums))
rank = {v: i for i, v in enumerate(sorted_nums)}
tree = [0] * (len(sorted_nums) + 1)
```

### 7. Wildcard Search Inefficiency

```python
# ❌ WRONG: Not pruning early
def search(self, word):
    def dfs(node, i):
        if i == len(word):
            return node.is_end_of_word
        if word[i] == '.':
            for child in node.children.values():
                if dfs(child, i + 1):  # Continue even after finding
                    pass
            return False  # Wrong!

# ✅ CORRECT: Return early
def search(self, word):
    def dfs(node, i):
        if i == len(word):
            return node.is_end_of_word
        if word[i] == '.':
            for child in node.children.values():
                if dfs(child, i + 1):
                    return True  # Found it, return immediately!
            return False
```

---

## Pattern Recognition

### When to Use Each Structure

#### Use Trie When:
- Need fast prefix matching
- Implementing autocomplete
- Word search with common prefixes
- Spell checking
- IP routing
- String pattern matching

**Example problems:**
- Implement Trie
- Word Search II
- Replace Words
- Autocomplete System
- Design Search Autocomplete System

```python
# Trie template
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
```

#### Use Segment Tree When:
- Range queries (sum, min, max, GCD)
- Need both range queries and updates
- Can afford O(n) space
- Need lazy propagation for range updates

**Example problems:**
- Range Sum Query - Mutable
- Range Minimum Query
- Count of Range Sum
- My Calendar problems

```python
# Segment tree template (range sum)
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(arr, 0, 0, self.n - 1)

    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)
```

#### Use Fenwick Tree When:
- Only need prefix sums
- Want simpler implementation than segment tree
- Space efficiency matters
- Point updates with range queries

**Example problems:**
- Range Sum Query - Mutable
- Count of Smaller Numbers After Self
- Count of Range Sum
- Reverse Pairs

```python
# Fenwick tree template
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
```

### Common Trie Patterns

#### Pattern 1: Basic Trie Operations
```python
def insert(self, word):
    node = self.root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True
```

#### Pattern 2: Trie with Wildcards
```python
def search_with_wildcard(self, word):
    def dfs(node, i):
        if i == len(word):
            return node.is_end_of_word
        if word[i] == '.':
            return any(dfs(child, i + 1) for child in node.children.values())
        if word[i] not in node.children:
            return False
        return dfs(node.children[word[i]], i + 1)
    return dfs(self.root, 0)
```

#### Pattern 3: Trie with DFS (Word Search)
```python
def find_words(self, board, trie_root):
    def dfs(i, j, node):
        if node.is_end_of_word:
            result.add(node.word)
        char = board[i][j]
        if char not in node.children:
            return
        board[i][j] = '#'
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            if 0 <= i+di < m and 0 <= j+dj < n:
                dfs(i+di, j+dj, node.children[char])
        board[i][j] = char
```

### Range Query Decision Tree

```
Need range queries?
├─ No → Use simple array
└─ Yes
   ├─ Only prefix sums?
   │  └─ Yes → Fenwick Tree
   └─ No (general range operations)
      ├─ Updates needed?
      │  ├─ No → Prefix sum array
      │  └─ Yes
      │     ├─ Range updates?
      │     │  └─ Yes → Segment Tree with lazy propagation
      │     └─ Point updates → Segment Tree or Fenwick Tree
      └─ Just queries, no updates → Sparse Table or prefix sum
```

---

## Interview Tips

### 1. Clarify Requirements

**For Trie problems:**
- Case sensitivity?
- Character set (lowercase only, alphanumeric, etc.)?
- Need to handle duplicates?
- Memory constraints?

**For Range Query problems:**
- Mutable or immutable?
- Type of queries (sum, min, max, etc.)?
- Frequency of updates vs queries?
- Size of the array?

### 2. Start with Simple Cases

**For Trie:**
```
Example: words = ["cat", "car", "card"]
Draw the trie:
       root
        |
        c
        |
        a
       / \
      t   r
          |
          d
```

**For Segment Tree:**
```
Array: [1, 3, 5, 7, 9, 11]
Tree structure:
         [0-5]=36
        /         \
    [0-2]=9      [3-5]=27
    /    \        /     \
[0-1]=4 [2]=5 [3-4]=16 [5]=11
```

### 3. Consider Edge Cases

**Trie edge cases:**
- Empty string
- Single character
- Prefix is complete word
- Word not in trie
- All words share common prefix

**Range query edge cases:**
- Empty array
- Single element
- Query entire range
- Left == right (single element)
- Multiple updates to same index

### 4. Optimize Space

**Dictionary vs Array for Trie:**
```python
# Dictionary (flexible)
node.children = {}  # Good for sparse, any characters

# Array (faster but limited)
node.children = [None] * 26  # Only for lowercase letters
```

### 5. Time Complexity Analysis

**Trie:**
- Insert/Search/StartsWith: O(m) where m = word length
- Space: O(ALPHABET_SIZE × m × n) worst case

**Segment Tree:**
- Build: O(n)
- Query/Update: O(log n)
- Space: O(4n) = O(n)

**Fenwick Tree:**
- Build: O(n log n)
- Query/Update: O(log n)
- Space: O(n)

---

## Performance Optimization

### 1. Trie Memory Optimization

```python
# ❌ Less efficient: Always use dictionary
class TrieNode:
    def __init__(self):
        self.children = {}

# ✅ More efficient: Use array for fixed alphabet
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # For lowercase only

# ✅ Hybrid approach
class TrieNode:
    def __init__(self, use_array=True):
        if use_array:
            self.children = [None] * 26
        else:
            self.children = {}
```

### 2. Early Termination in Trie

```python
# ✅ Stop early when possible
def autocomplete(self, prefix, limit=5):
    node = self.root
    for char in prefix:
        if char not in node.children:
            return []
        node = node.children[char]

    results = []
    def dfs(node, path):
        if len(results) >= limit:  # Early termination!
            return
        if node.is_end_of_word:
            results.append(prefix + path)
        for char, child in node.children.items():
            dfs(child, path + char)

    dfs(node, "")
    return results
```

### 3. Fenwick Tree with Batch Updates

```python
# ✅ More efficient for multiple queries
def range_update(self, left, right, delta):
    """Update range [left, right] efficiently."""
    self.update(left, delta)
    self.update(right + 1, -delta)
```

### 4. Segment Tree Lazy Propagation

```python
# For range updates, use lazy propagation
class SegmentTreeLazy:
    def _push(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[2*node+1] += self.lazy[node]
                self.lazy[2*node+2] += self.lazy[node]
            self.lazy[node] = 0
```

---

## LeetCode Practice Problems

### Trie Problems (30 problems)

#### Easy (6 problems)

#### 1. Implement Trie (Prefix Tree)
**Link:** https://leetcode.com/problems/implement-trie-prefix-tree/
**Pattern:** Basic Trie
**Topics:** Trie, Design
**Description:** Implement insert, search, and startsWith operations
**Why Practice:** Foundation for all trie problems, must-know

#### 2. Longest Common Prefix
**Link:** https://leetcode.com/problems/longest-common-prefix/
**Pattern:** Trie or String Manipulation
**Topics:** String, Trie
**Description:** Find longest common prefix among strings
**Why Practice:** Can be solved with or without trie

#### 3. Design Add and Search Words Data Structure
**Link:** https://leetcode.com/problems/design-add-and-search-words-data-structure/
**Pattern:** Trie with Wildcards
**Topics:** Trie, DFS
**Description:** Support '.' wildcard in search
**Why Practice:** Learn wildcard matching with trie

#### 4. Map Sum Pairs
**Link:** https://leetcode.com/problems/map-sum-pairs/
**Pattern:** Trie with Values
**Topics:** Trie, Hash Table
**Description:** Sum all values with given prefix
**Why Practice:** Trie with additional data storage

#### 5. Longest Word in Dictionary
**Link:** https://leetcode.com/problems/longest-word-in-dictionary/
**Pattern:** Trie Construction
**Topics:** Trie, DFS
**Description:** Find longest buildable word
**Why Practice:** Word building with trie validation

#### 6. Implement Trie II (Prefix Tree)
**Link:** https://leetcode.com/problems/implement-trie-ii-prefix-tree/
**Pattern:** Trie with Counters
**Topics:** Trie, Design
**Description:** Trie with count operations and erase
**Why Practice:** Advanced trie with frequency tracking

#### Medium (16 problems)

#### 7. Replace Words
**Link:** https://leetcode.com/problems/replace-words/
**Pattern:** Trie for Dictionary
**Topics:** Trie, String
**Description:** Replace words with their roots
**Why Practice:** Classic trie application for prefix matching

#### 8. Word Search II
**Link:** https://leetcode.com/problems/word-search-ii/
**Pattern:** Trie + Backtracking
**Topics:** Trie, DFS, Matrix
**Description:** Find words in 2D board
**Why Practice:** Essential pattern combining trie with grid DFS

#### 9. Search Suggestions System
**Link:** https://leetcode.com/problems/search-suggestions-system/
**Pattern:** Autocomplete
**Topics:** Trie, Sorting
**Description:** Return top 3 suggestions for each prefix
**Why Practice:** Real-world autocomplete implementation

#### 10. Design Search Autocomplete System
**Link:** https://leetcode.com/problems/design-search-autocomplete-system/
**Pattern:** Autocomplete with Frequency
**Topics:** Trie, Design
**Description:** Autocomplete with hot sentence ranking
**Why Practice:** Advanced autocomplete with sorting

#### 11. Maximum XOR of Two Numbers in an Array
**Link:** https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
**Pattern:** Binary Trie
**Topics:** Trie, Bit Manipulation
**Description:** Find maximum XOR between two numbers
**Why Practice:** Binary trie for XOR optimization

#### 12. Word Squares
**Link:** https://leetcode.com/problems/word-squares/
**Pattern:** Trie + Backtracking
**Topics:** Trie, Backtracking
**Description:** Build valid word squares
**Why Practice:** Complex backtracking with trie pruning

#### 13. Concatenated Words
**Link:** https://leetcode.com/problems/concatenated-words/
**Pattern:** Trie + DP
**Topics:** Trie, DFS, DP
**Description:** Find words made from other words
**Why Practice:** Combine trie with dynamic programming

#### 14. Top K Frequent Words
**Link:** https://leetcode.com/problems/top-k-frequent-words/
**Pattern:** Frequency + Sorting
**Topics:** Hash Table, Heap, Trie
**Description:** Return k most frequent words
**Why Practice:** Can use trie for lexicographic ordering

#### 15. Camelcase Matching
**Link:** https://leetcode.com/problems/camelcase-matching/
**Pattern:** Pattern Matching
**Topics:** String, Trie
**Description:** Match queries with pattern
**Why Practice:** Advanced pattern matching

#### 16. Short Encoding of Words
**Link:** https://leetcode.com/problems/short-encoding-of-words/
**Pattern:** Reverse Trie
**Topics:** Trie, String
**Description:** Find shortest encoding of words
**Why Practice:** Trie with suffix matching

#### 17. Extra Characters in a String
**Link:** https://leetcode.com/problems/extra-characters-in-a-string/
**Pattern:** Trie + DP
**Topics:** Trie, DP
**Description:** Minimize extra characters when breaking string
**Why Practice:** Word break variation with trie

#### 18. Lexicographical Numbers
**Link:** https://leetcode.com/problems/lexicographical-numbers/
**Pattern:** Trie / DFS
**Topics:** DFS, Trie
**Description:** Generate numbers in lexicographical order
**Why Practice:** Number generation with trie-like traversal

#### 19. Word Abbreviation
**Link:** https://leetcode.com/problems/word-abbreviation/
**Pattern:** Trie for Grouping
**Topics:** Trie, String
**Description:** Find shortest unique abbreviations
**Why Practice:** Trie for prefix-based grouping

#### 20. Add and Search Word - Data structure design
**Link:** https://leetcode.com/problems/add-and-search-word-data-structure-design/
**Pattern:** Trie with Wildcards
**Topics:** Trie, DFS
**Description:** Word dictionary with wildcard support
**Why Practice:** Wildcard search pattern

#### 21. Stream of Characters
**Link:** https://leetcode.com/problems/stream-of-characters/
**Pattern:** Reverse Trie
**Topics:** Trie, Data Stream
**Description:** Check if suffix matches any word
**Why Practice:** Suffix matching with reverse trie

#### 22. Index Pairs of a String
**Link:** https://leetcode.com/problems/index-pairs-of-a-string/
**Pattern:** Trie Matching
**Topics:** Trie, String
**Description:** Find all occurrences of words in text
**Why Practice:** Multiple pattern matching

#### Hard (8 problems)

#### 23. Palindrome Pairs
**Link:** https://leetcode.com/problems/palindrome-pairs/
**Pattern:** Trie + Palindrome
**Topics:** Trie, String
**Description:** Find word pairs that form palindromes
**Why Practice:** Advanced trie with palindrome checking

#### 24. Word Search II
**Link:** https://leetcode.com/problems/word-search-ii/
**Pattern:** Trie + Backtracking
**Topics:** Trie, DFS
**Description:** Find multiple words in grid
**Why Practice:** Must-know pattern for grid word search

#### 25. Design Search Autocomplete System
**Link:** https://leetcode.com/problems/design-search-autocomplete-system/
**Pattern:** Autocomplete
**Topics:** Trie, Design
**Description:** Build autocomplete with ranking
**Why Practice:** Real interview problem at major companies

#### 26. Longest Word in Dictionary through Deleting
**Link:** https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
**Pattern:** Trie / Two Pointers
**Topics:** Trie, String
**Description:** Find longest valid subsequence
**Why Practice:** Subsequence matching

#### 27. Maximum XOR With an Element From Array
**Link:** https://leetcode.com/problems/maximum-xor-with-an-element-from-array/
**Pattern:** Binary Trie with Constraints
**Topics:** Trie, Bit Manipulation
**Description:** Maximum XOR with value constraint
**Why Practice:** Advanced binary trie

#### 28. Count Pairs With XOR in a Range
**Link:** https://leetcode.com/problems/count-pairs-with-xor-in-a-range/
**Pattern:** Binary Trie
**Topics:** Trie, Bit Manipulation
**Description:** Count pairs with XOR in range
**Why Practice:** Complex XOR problem with trie

#### 29. Encrypt and Decrypt Strings
**Link:** https://leetcode.com/problems/encrypt-and-decrypt-strings/
**Pattern:** Trie + Mapping
**Topics:** Trie, String
**Description:** Encrypt/decrypt with mapping
**Why Practice:** Trie with transformation

#### 30. Find the Longest Valid Obstacle Course at Each Position
**Link:** https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
**Pattern:** Segment Tree / Binary Search
**Topics:** Segment Tree, Binary Search
**Description:** Find longest increasing subsequence variations
**Why Practice:** Advanced segment tree application

### Segment Tree Problems (15 problems)

#### Easy (3 problems)

#### 31. Range Sum Query - Immutable
**Link:** https://leetcode.com/problems/range-sum-query-immutable/
**Pattern:** Prefix Sum
**Topics:** Array, Prefix Sum
**Description:** Range sum queries without updates
**Why Practice:** Foundation for mutable version

#### 32. Range Sum Query 2D - Immutable
**Link:** https://leetcode.com/problems/range-sum-query-2d-immutable/
**Pattern:** 2D Prefix Sum
**Topics:** Matrix, Prefix Sum
**Description:** 2D range sum queries
**Why Practice:** Extend to 2D understanding

#### 33. Count Nodes Equal to Average of Subtree
**Link:** https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
**Pattern:** Tree Traversal
**Topics:** Tree, DFS
**Description:** Count nodes equal to subtree average
**Why Practice:** Bottom-up computation

#### Medium (8 problems)

#### 34. Range Sum Query - Mutable
**Link:** https://leetcode.com/problems/range-sum-query-mutable/
**Pattern:** Segment Tree / Fenwick Tree
**Topics:** Segment Tree, Binary Indexed Tree
**Description:** Range sum with updates
**Why Practice:** Core segment tree/Fenwick tree problem

#### 35. Count of Smaller Numbers After Self
**Link:** https://leetcode.com/problems/count-of-smaller-numbers-after-self/
**Pattern:** Fenwick Tree / Merge Sort
**Topics:** Binary Indexed Tree, Divide and Conquer
**Description:** Count smaller elements after each element
**Why Practice:** Classic Fenwick tree application

#### 36. Range Sum Query 2D - Mutable
**Link:** https://leetcode.com/problems/range-sum-query-2d-mutable/
**Pattern:** 2D Binary Indexed Tree
**Topics:** Binary Indexed Tree
**Description:** 2D range sum with updates
**Why Practice:** 2D Fenwick tree implementation

#### 37. My Calendar I
**Link:** https://leetcode.com/problems/my-calendar-i/
**Pattern:** Interval Management
**Topics:** Design, Segment Tree
**Description:** Book events without overlap
**Why Practice:** Interval overlap detection

#### 38. My Calendar II
**Link:** https://leetcode.com/problems/my-calendar-ii/
**Pattern:** Interval Management
**Topics:** Design, Segment Tree
**Description:** Allow at most 1 overlap
**Why Practice:** Track overlapping intervals

#### 39. My Calendar III
**Link:** https://leetcode.com/problems/my-calendar-iii/
**Pattern:** Interval Management
**Topics:** Design, Segment Tree
**Description:** Find maximum k-booking
**Why Practice:** Count concurrent intervals

#### 40. Falling Squares
**Link:** https://leetcode.com/problems/falling-squares/
**Pattern:** Segment Tree with Lazy Propagation
**Topics:** Segment Tree, Coordinate Compression
**Description:** Track heights after dropping squares
**Why Practice:** Coordinate compression with segment tree

#### 41. The Skyline Problem
**Link:** https://leetcode.com/problems/the-skyline-problem/
**Pattern:** Line Sweep / Segment Tree
**Topics:** Heap, Segment Tree
**Description:** Find skyline outline
**Why Practice:** Classic hard problem with multiple approaches

#### Hard (4 problems)

#### 42. Count of Range Sum
**Link:** https://leetcode.com/problems/count-of-range-sum/
**Pattern:** Segment Tree / Merge Sort
**Topics:** Segment Tree, Binary Indexed Tree
**Description:** Count ranges with sum in given range
**Why Practice:** Advanced range counting

#### 43. Reverse Pairs
**Link:** https://leetcode.com/problems/reverse-pairs/
**Pattern:** Segment Tree / Merge Sort
**Topics:** Segment Tree, Divide and Conquer
**Description:** Count pairs where i < j and nums[i] > 2*nums[j]
**Why Practice:** Inversion counting variation

#### 44. Create Sorted Array through Instructions
**Link:** https://leetcode.com/problems/create-sorted-array-through-instructions/
**Pattern:** Fenwick Tree
**Topics:** Binary Indexed Tree
**Description:** Calculate cost of building sorted array
**Why Practice:** Dynamic order statistics

#### 45. Count Integers in Intervals
**Link:** https://leetcode.com/problems/count-integers-in-intervals/
**Pattern:** Segment Tree
**Topics:** Design, Segment Tree
**Description:** Add intervals and count unique integers
**Why Practice:** Interval merging with segment tree

### Fenwick Tree Specific (10 problems)

#### 46. Range Addition
**Link:** https://leetcode.com/problems/range-addition/
**Pattern:** Difference Array / Fenwick
**Topics:** Array, Prefix Sum
**Description:** Perform range additions efficiently
**Why Practice:** Difference array technique

#### 47. Global and Local Inversions
**Link:** https://leetcode.com/problems/global-and-local-inversions/
**Pattern:** Inversion Counting
**Topics:** Array, Math
**Description:** Check if global and local inversions equal
**Why Practice:** Understand inversion relationships

#### 48. Kth Smallest Number in Multiplication Table
**Link:** https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
**Pattern:** Binary Search
**Topics:** Binary Search
**Description:** Find kth smallest in multiplication table
**Why Practice:** Order statistics application

#### 49. Number of Longest Increasing Subsequence
**Link:** https://leetcode.com/problems/number-of-longest-increasing-subsequence/
**Pattern:** DP + Segment Tree
**Topics:** Dynamic Programming, Segment Tree
**Description:** Count longest increasing subsequences
**Why Practice:** Combine DP with segment tree

#### 50. Longest Increasing Subsequence II
**Link:** https://leetcode.com/problems/longest-increasing-subsequence-ii/
**Pattern:** Segment Tree + DP
**Topics:** Segment Tree, Dynamic Programming
**Description:** LIS with difference constraint
**Why Practice:** Advanced DP with segment tree

#### 51. Booking Concert Tickets in Groups
**Link:** https://leetcode.com/problems/booking-concert-tickets-in-groups/
**Pattern:** Segment Tree
**Topics:** Design, Segment Tree
**Description:** Book seats with constraints
**Why Practice:** Real-world segment tree application

#### 52. Number of Visible People in a Queue
**Link:** https://leetcode.com/problems/number-of-visible-people-in-a-queue/
**Pattern:** Monotonic Stack / Segment Tree
**Topics:** Stack, Segment Tree
**Description:** Count visible people in queue
**Why Practice:** Can solve with segment tree or stack

#### 53. Find Servers That Handled Most Number of Requests
**Link:** https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
**Pattern:** Segment Tree / Priority Queue
**Topics:** Heap, Segment Tree
**Description:** Simulate server requests
**Why Practice:** Complex simulation problem

#### 54. Process Restricted Friend Requests
**Link:** https://leetcode.com/problems/process-restricted-friend-requests/
**Pattern:** Union Find / Segment Tree
**Topics:** Union Find, Graph
**Description:** Process friend requests with restrictions
**Why Practice:** Graph connectivity with constraints

#### 55. Handling Sum Queries After Update
**Link:** https://leetcode.com/problems/handling-sum-queries-after-update/
**Pattern:** Segment Tree with Lazy Propagation
**Topics:** Segment Tree
**Description:** Range flip and sum queries
**Why Practice:** Lazy propagation pattern

### Additional Mixed Problems (5 problems)

#### 56. Maximum Genetic Difference Query
**Link:** https://leetcode.com/problems/maximum-genetic-difference-query/
**Pattern:** Binary Trie + DFS
**Topics:** Trie, DFS, Bit Manipulation
**Description:** Find maximum XOR in tree paths
**Why Practice:** Combine trie with tree traversal

#### 57. Maximum Strong Pair XOR I & II
**Link:** https://leetcode.com/problems/maximum-strong-pair-xor-ii/
**Pattern:** Binary Trie
**Topics:** Trie, Bit Manipulation
**Description:** Find maximum XOR with constraints
**Why Practice:** Advanced XOR optimization

#### 58. Count Different Palindromic Subsequences
**Link:** https://leetcode.com/problems/count-different-palindromic-subsequences/
**Pattern:** DP / Segment Tree
**Topics:** Dynamic Programming
**Description:** Count unique palindromic subsequences
**Why Practice:** Complex DP problem

#### 59. Fancy Sequence
**Link:** https://leetcode.com/problems/fancy-sequence/
**Pattern:** Segment Tree with Lazy Propagation
**Topics:** Design, Segment Tree, Math
**Description:** Sequence with range operations
**Why Practice:** Lazy propagation with multiple operations

#### 60. Count of Range Sum
**Link:** https://leetcode.com/problems/count-of-range-sum/
**Pattern:** Segment Tree / Fenwick Tree
**Topics:** Divide and Conquer
**Description:** Count subarrays with sum in range
**Why Practice:** Advanced range counting

---

## Pattern Mastery Checklist

### Trie Patterns

- [ ] **Basic Trie Operations**
  - Master: #1, #3
  - Practice: #4, #6

- [ ] **Trie with DFS/Backtracking**
  - Master: #8 (Word Search II - critical!)
  - Practice: #12, #17

- [ ] **Autocomplete Systems**
  - Master: #9, #10
  - Practice: #7, #16

- [ ] **Binary Trie (XOR)**
  - Master: #11
  - Practice: #27, #28, #56

- [ ] **Reverse Trie**
  - Master: #21
  - Practice: #16

### Segment Tree Patterns

- [ ] **Basic Range Queries**
  - Master: #34
  - Practice: #31, #32

- [ ] **2D Range Queries**
  - Master: #36
  - Practice: #33

- [ ] **Interval Management**
  - Master: #37, #38, #39
  - Practice: #45

- [ ] **Lazy Propagation**
  - Master: #40
  - Practice: #55, #59

### Fenwick Tree Patterns

- [ ] **Prefix Sum Queries**
  - Master: #34
  - Practice: #46

- [ ] **Order Statistics**
  - Master: #35
  - Practice: #42, #43

- [ ] **Inversion Counting**
  - Master: #43
  - Practice: #47

- [ ] **Dynamic Range Queries**
  - Master: #44
  - Practice: #49, #50

### Must-Know Problems

**Top 15 for Interviews:**
1. Implement Trie (#1)
2. Word Search II (#8)
3. Range Sum Query - Mutable (#34)
4. Count of Smaller Numbers After Self (#35)
5. Design Add and Search Words (#3)
6. Maximum XOR of Two Numbers (#11)
7. Replace Words (#7)
8. Autocomplete System (#10)
9. Palindrome Pairs (#23)
10. My Calendar problems (#37, #38, #39)
11. The Skyline Problem (#41)
12. Count of Range Sum (#42)
13. Falling Squares (#40)
14. Reverse Pairs (#43)
15. Stream of Characters (#21)

---

## Practice Progression

### Week 1-2: Trie Foundations
**Goal:** Master basic trie operations

- Day 1-2: #1, #2 (basic trie)
- Day 3-4: #3, #4 (wildcards and values)
- Day 5-6: #5, #6 (advanced trie)
- Day 7-8: #7, #9 (autocomplete)
- Day 9-10: #8 (word search - critical!)
- Day 11-12: #10, #11 (advanced patterns)
- Day 13-14: Review and practice weak areas

### Week 3-4: Segment Trees and Fenwick Trees
**Goal:** Master range query structures

- Day 15-16: #31, #32 (prefix sum foundation)
- Day 17-18: #34 (range sum mutable - critical!)
- Day 19-20: #35 (Fenwick tree application)
- Day 21-22: #36 (2D range queries)
- Day 23-24: #37, #38, #39 (calendar problems)
- Day 25-26: #40, #46 (lazy propagation)
- Day 27-28: Review segment/Fenwick patterns

### Week 5-6: Advanced Applications
**Goal:** Master complex problems

- Day 29-30: #12, #17, #22 (advanced trie)
- Day 31-32: #21, #23 (reverse trie, palindrome)
- Day 33-34: #41 (skyline - multiple approaches)
- Day 35-36: #42, #43 (range counting)
- Day 37-38: #44, #49 (order statistics)
- Day 39-40: #50, #55 (DP with segment tree)
- Day 41-42: Review hard problems

### Week 7-8: Mastery and Integration
**Goal:** Solve complex problems confidently

- Day 43-44: #24, #25, #26 (hard trie)
- Day 45-46: #27, #28 (XOR problems)
- Day 47-48: #56, #57 (trie with other structures)
- Day 49-50: #51, #52, #53 (real-world applications)
- Day 51-52: #58, #59, #60 (complex combinations)
- Day 53-54: Mock interviews
- Day 55-56: Final review of must-know problems

### Total Practice Time Estimate
- Trie problems (30): ~40-50 hours
- Segment Tree problems (15): ~25-35 hours
- Fenwick Tree problems (10): ~20-25 hours
- Mixed problems (5): ~10-15 hours
- **Total: 95-125 hours for complete mastery**

---

## Interview Preparation Checklist

### Before the Interview

- [ ] Can implement basic trie from memory
- [ ] Know when to use trie vs hash table
- [ ] Understand segment tree vs Fenwick tree trade-offs
- [ ] Can implement range sum query with updates
- [ ] Know binary trie for XOR problems
- [ ] Understand lazy propagation concept
- [ ] Can apply coordinate compression

### During the Interview

- [ ] Clarify character set for trie problems
- [ ] Ask about frequency of queries vs updates
- [ ] Consider space-time trade-offs
- [ ] Explain why choosing specific structure
- [ ] Handle edge cases (empty, single element)
- [ ] Optimize for the specific problem constraints
- [ ] Code cleanly with helper methods

### Red Flags to Avoid

- [ ] Using trie for simple exact-match lookups (use hash table)
- [ ] Building segment tree when only queries needed (use prefix sum)
- [ ] Forgetting to mark end of words in trie
- [ ] Incorrect Fenwick tree indexing
- [ ] Not considering coordinate compression for large ranges
- [ ] Missing lazy propagation for range updates
- [ ] Inefficient wildcard search without pruning

---

## Summary

**Advanced trees appear in 5-10% of coding interviews** but are critical for certain companies.

**Key Takeaways:**
1. Trie is essential for prefix-based string operations
2. Choose Segment Tree for general range queries
3. Choose Fenwick Tree for simpler prefix sum operations
4. Binary Trie is powerful for XOR optimization
5. Coordinate compression enables large range handling
6. Lazy propagation is key for range updates

**Most Important Patterns:**
- Trie with DFS for word search (Word Search II)
- Autocomplete with trie and sorting
- Binary trie for XOR maximization
- Segment tree for range sum with updates
- Fenwick tree for order statistics

**Practice Strategy:**
- Master basic trie implementation first
- Learn when to use each structure
- Practice 60+ problems across all patterns
- Focus on must-know top 15 problems
- Understand trade-offs between structures

**Companies that frequently test these:**
- Google (trie, segment tree)
- Facebook (autocomplete, range queries)
- Amazon (text processing)
- Microsoft (data structure design)
- Bloomberg (range queries)

Good luck with your advanced trees mastery! 🌲
