# Chapter 32: Hash Tables

## Overview

Hash tables are one of the most important and widely-used data structures in computer science. They provide average O(1) time complexity for insertion, deletion, and lookup operations by using a hash function to map keys to array indices. Understanding hash tables is crucial for writing efficient code and solving many algorithmic problems.

## What You'll Learn

- **Hash Table Fundamentals**: Hash functions, collision resolution, load factor
- **Python dict Implementation**: How Python's dict works under the hood
- **Hash Function Design**: Division, multiplication, universal hashing
- **Collision Resolution**: Chaining, open addressing, linear/quadratic probing
- **Advanced Collections**: OrderedDict, defaultdict, Counter
- **Set Operations**: Union, intersection, difference with O(1) lookup
- **Common Patterns**: Two Sum, anagrams, frequency counting, subarray sums

## Structure

1. **theory.md** - Complete theoretical foundations
   - Hash table concepts and terminology
   - Hash function design principles
   - Collision resolution strategies
   - Dynamic resizing and load factor
   - Python's dict implementation details
   - Complexity analysis (average vs worst case)

2. **examples.md** - 20 complete, runnable examples
   - Hash table from scratch
   - Classic problems (Two Sum, anagrams)
   - Frequency counting patterns
   - Subarray and substring problems
   - Design problems

3. **exercises.md** - 20 LeetCode-style problems
   - Easy, medium, and hard difficulty levels
   - Covers all important hash table patterns

4. **solutions.md** - Complete solutions with:
   - Multiple approaches
   - Complexity analysis
   - Hash function considerations
   - Trade-offs discussion

5. **tips.md** - Practical patterns and optimization tricks

## Key Concepts

### Why Hash Tables?

- **Fast Lookup**: O(1) average time to find, insert, or delete
- **Flexible Keys**: Use any hashable type as key
- **Natural Mapping**: Perfect for key-value relationships
- **Set Operations**: Efficient membership testing
- **Frequency Counting**: Track occurrence counts easily

### When to Use Hash Tables

✅ **Use when:**
- Need fast lookup by key (O(1) average)
- Tracking frequency or counts
- Detecting duplicates
- Grouping related items
- Caching or memoization
- Two Sum and similar pairing problems

❌ **Avoid when:**
- Need ordered traversal (use TreeMap/SortedDict)
- Keys are not hashable
- Memory is extremely constrained
- Need guaranteed O(1) worst case (use perfect hashing)

## Common Patterns

1. **Frequency Counting**: Count occurrences using dict or Counter
2. **Two Pointer Alternative**: Hash table for O(n) instead of O(n²)
3. **Grouping**: Group items by common property
4. **Caching/Memoization**: Store computed results
5. **Set Operations**: Fast membership testing with sets
6. **Sliding Window**: Track elements in current window

## Complexity Quick Reference

| Operation | Average | Worst Case | Notes |
|-----------|---------|------------|-------|
| Insert | O(1) | O(n) | Amortized for resizing |
| Delete | O(1) | O(n) | Rare worst case |
| Lookup | O(1) | O(n) | With good hash function |
| Space | O(n) | O(n) | Plus overhead |

**Worst case occurs when:**
- All keys hash to same bucket (poor hash function)
- Many collisions due to hash function quality
- Resizing operation (amortized O(1))

## Getting Started

Start with **theory.md** to understand hash table internals, then work through **examples.md** to see implementations and patterns. Practice with **exercises.md** and verify your solutions against **solutions.md**.

## Prerequisites

- Basic Python knowledge
- Understanding of arrays (Chapter 28)
- Basic complexity analysis (Chapter 27)

## Practice Strategy

1. Master Python dict, set, defaultdict, Counter
2. Learn frequency counting patterns
3. Practice Two Sum variations
4. Solve anagram and grouping problems
5. Understand sliding window with hash table
6. Learn subarray sum patterns
7. Tackle design problems (LRU cache, HashMap)

## Real-World Applications

- **Databases**: Index structures for fast lookup
- **Caching**: Redis, Memcached use hash tables
- **Compilers**: Symbol tables for variables
- **Routers**: IP address lookup tables
- **Spell Checkers**: Dictionary lookup
- **Deduplication**: Detect duplicate files/records
- **Password Storage**: Hash table with salted hashes

## Python Collections Overview

```python
# dict - Basic hash table
d = {'a': 1, 'b': 2}
d['a']           # Get value
d['c'] = 3       # Set value

# set - Hash table without values
s = {1, 2, 3}
1 in s           # O(1) membership test

# defaultdict - Auto-initialize missing keys
from collections import defaultdict
dd = defaultdict(int)
dd['a'] += 1     # No KeyError

# Counter - Frequency counting
from collections import Counter
c = Counter(['a', 'b', 'a'])
c['a']           # Returns 2

# OrderedDict - Maintains insertion order
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2      # Order preserved
```

## Interview Frequency

- **Very Common:** Two Sum, valid anagram, group anagrams
- **Common:** Longest substring without repeating, subarray sum
- **Moderate:** LRU cache, design HashMap, four sum

## Next Steps

After mastering this chapter:
- Chapter 32: Trees (BST for ordered data)
- Chapter 35: Graphs (adjacency lists use hash tables)
- Chapter 37: Advanced sorting (counting sort uses hash tables)

## Additional Resources

- Python dict implementation (CPython source)
- Hash table visualizations
- LeetCode hash table tag
- "Understanding Python dictionaries" by Brandon Rhodes

Happy hashing!
