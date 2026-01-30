# Chapter 34: Advanced Trees

## Overview

Advanced trees are specialized data structures that extend the concepts of binary trees and BSTs to solve specific problems efficiently. These structures are the backbone of modern databases, search engines, routing algorithms, and many other performance-critical systems.

## Learning Objectives

By the end of this chapter, you will be able to:

1. Understand and implement Tries (Prefix Trees) for string operations
2. Build and query Segment Trees for range operations
3. Implement Fenwick Trees (Binary Indexed Trees) for cumulative queries
4. Understand AVL tree rotations and self-balancing concepts
5. Comprehend Red-Black tree properties and applications
6. Recognize when to use each advanced tree structure
7. Apply these structures to solve complex interview problems
8. Analyze time and space complexity of advanced tree operations

## Chapter Structure

- **theory.md** - Comprehensive explanations of advanced tree concepts
- **examples.md** - Annotated code examples with detailed implementations
- **exercises.md** - Practice problems organized by difficulty
- **solutions.md** - Detailed solutions with complexity analysis
- **tips.md** - Tips, tricks, common pitfalls, and 60+ LeetCode practice problems

## Prerequisites

Before starting this chapter, you should be comfortable with:

- Binary Trees and BSTs (Chapter 33)
- Tree Traversals and DFS/BFS (Chapter 33)
- Recursion (Chapter 5)
- Complexity Analysis (Chapter 27)
- Strings and Arrays (Chapters 29)
- Hash Tables (Chapter 32)

## Key Concepts

### Trie (Prefix Tree)
- String-specialized tree structure
- Efficient prefix matching and autocomplete
- Insert, search, startsWith operations
- Memory-efficient string storage
- Applications: autocomplete, spell checkers, IP routing

### Segment Trees
- Range query optimization
- Support for range sum, min, max, GCD queries
- Efficient updates (O(log n))
- Tree construction from arrays
- Applications: competitive programming, databases

### Fenwick Trees (Binary Indexed Trees)
- Specialized for prefix sum queries
- More space-efficient than Segment Trees
- Point updates and range queries
- Implementation using bit manipulation
- Applications: cumulative frequency tables

### Self-Balancing BSTs
- **AVL Trees**
  - Strict height balancing (|left_h - right_h| ≤ 1)
  - Four rotation types: LL, RR, LR, RL
  - O(log n) guaranteed operations
- **Red-Black Trees**
  - Looser balancing (black height property)
  - Faster insertion/deletion than AVL
  - Used in C++ STL and Java TreeMap

### Multi-Way Trees
- **B-Trees**
  - Generalization of BST (more than 2 children)
  - Self-balancing, optimized for disk storage
  - Used in databases and file systems
- **B+ Trees**
  - Variation of B-Tree
  - All values stored in leaves
  - Efficient range scans

## Time Complexity Summary

| Operation | Trie | Segment Tree | Fenwick Tree | AVL Tree | Red-Black Tree |
|-----------|------|--------------|--------------|----------|----------------|
| Insert | O(m) | O(n) build | O(n) build | O(log n) | O(log n) |
| Search | O(m) | O(log n) | - | O(log n) | O(log n) |
| Range Query | - | O(log n) | O(log n) | - | - |
| Update | O(m) | O(log n) | O(log n) | O(log n) | O(log n) |
| Space | O(ALPHABET_SIZE * m * n) | O(4n) | O(n) | O(n) | O(n) |

*m = string length, n = number of elements*

## Real-World Applications

### Tries
- **Search Engines**: Autocomplete suggestions
- **Spell Checkers**: Word validation and suggestions
- **IP Routing**: Longest prefix matching
- **Text Editors**: Auto-completion and spell-check
- **DNS**: Domain name resolution

### Segment Trees
- **Competitive Programming**: Range query problems
- **Databases**: Aggregate queries on ranges
- **Graphics**: Interval scheduling
- **Finance**: Stock price queries over time ranges

### Fenwick Trees
- **Cumulative Statistics**: Running totals
- **Order Statistics**: Rank queries
- **Data Compression**: Arithmetic encoding
- **Inversion Counting**: Array analysis

### Self-Balancing Trees
- **Databases**: Indexing (B-Trees, B+ Trees)
- **Programming Languages**:
  - C++ std::map (Red-Black Tree)
  - Java TreeMap (Red-Black Tree)
  - Python (not used, uses hash tables)
- **File Systems**: Directory structures
- **Memory Management**: Free block tracking

## Interview Frequency

**Most Common in Interviews:**
1. **Tries** - 40% (Very Common)
   - Autocomplete, word search, prefix matching
2. **Segment Trees** - 25% (Common in competitive programming background)
   - Range queries, lazy propagation
3. **Fenwick Trees** - 20% (Common for specific problems)
   - Prefix sums, range updates

**Less Common but Important:**
4. **AVL Trees** - 10% (Mostly conceptual)
   - Usually asked about rotations and balancing concept
5. **Red-Black Trees** - 5% (Rarely asked to implement)
   - Conceptual understanding, comparison with AVL

**Note:** B-Trees and B+ Trees are more common in system design interviews than coding interviews.

## Study Approach

1. **Start with Tries** (Most Important)
   - Implement basic trie structure
   - Practice insert, search, startsWith
   - Solve word search problems
   - Master prefix-based problems

2. **Learn Segment Trees** (Important for Range Queries)
   - Understand tree construction
   - Practice range sum/min/max queries
   - Learn lazy propagation for advanced use

3. **Study Fenwick Trees** (Alternative to Segment Trees)
   - Understand bit manipulation approach
   - Compare with Segment Trees
   - Practice prefix sum problems

4. **Understand Self-Balancing Concepts** (Mostly Conceptual)
   - Learn AVL rotations (visual understanding)
   - Understand Red-Black properties
   - Focus on when to use vs hash tables

5. **Practice, Practice, Practice**
   - Work through exercises in this chapter
   - Solve 60+ LeetCode problems in tips.md
   - Focus heavily on Trie problems (most common)

## Estimated Study Time

- Theory and concepts: 5-6 hours
- Examples and implementation: 6-8 hours
- Exercises: 10-12 hours
- LeetCode practice (60+ problems in tips.md): 50-70 hours

**Total**: 70-95 hours for mastery

## When to Use Each Structure

### Use Trie When:
- Working with strings and prefixes
- Need autocomplete functionality
- Searching for words with common prefixes
- Implementing spell checkers
- IP routing tables

### Use Segment Tree When:
- Need range queries (sum, min, max, GCD)
- Need to update ranges efficiently
- Array doesn't change much after construction
- Can afford O(n) space

### Use Fenwick Tree When:
- Only need prefix sums (not general range queries)
- Want more space efficiency than Segment Tree
- Need simple implementation
- Point updates with range queries

### Use AVL Tree When:
- Need guaranteed O(log n) operations
- Read-heavy workload (more searches than inserts/deletes)
- Can afford stricter balancing overhead

### Use Red-Black Tree When:
- Need good average performance
- Insert/delete heavy workload
- Already implemented (use standard library)

### Use Hash Table Instead When:
- Don't need ordering
- Don't need range queries
- Want O(1) average operations

## Navigation

- **Previous**: [Chapter 33: Trees](../33_trees/README.md)
- **Next**: [Chapter 35: Heaps](../35_heaps/README.md)
- **Home**: [Main README](../README.md)

---

## Quick Reference

### Trie Node Structure
```python
class TrieNode:
    def __init__(self):
        self.children = {}  # or [None] * 26 for lowercase only
        self.is_end_of_word = False
```

### Segment Tree Template
```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2*node+1, start, mid)
            self.build(arr, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
```

### Fenwick Tree Template
```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
```

## Additional Resources

- [VisuAlgo - Advanced Tree Visualizations](https://visualgo.net/en)
- [CP-Algorithms - Segment Tree](https://cp-algorithms.com/data_structures/segment_tree.html)
- [CP-Algorithms - Fenwick Tree](https://cp-algorithms.com/data_structures/fenwick.html)
- [LeetCode Trie Problems](https://leetcode.com/tag/trie/)
- [LeetCode Segment Tree Problems](https://leetcode.com/tag/segment-tree/)

---

## Focus Areas for Interviews

**High Priority (Practice Extensively):**
- Trie implementation and variations
- Segment Tree for range sum/min/max
- Fenwick Tree for prefix sums

**Medium Priority (Conceptual Understanding):**
- AVL rotations and balancing
- Red-Black tree properties
- When to use each structure

**Low Priority (Basic Awareness):**
- B-Tree and B+ Tree concepts
- Detailed rotation implementations
- Advanced segment tree with lazy propagation

---

Happy learning! Advanced trees open up a whole new world of efficient problem solving!
