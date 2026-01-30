# Chapter 39: Searching

## Overview

Searching is one of the most fundamental operations in computer science. It involves finding a particular element or determining if it exists in a data structure. Binary search, in particular, is a critical skill for coding interviews and appears in approximately 20-25% of problems.

## Learning Objectives

By the end of this chapter, you will be able to:

1. Understand and implement various searching algorithms
2. Master binary search and its many variations
3. Apply the "binary search on answer" pattern
4. Recognize when to use binary search vs linear search
5. Implement binary search templates correctly
6. Solve complex search space problems
7. Analyze time and space complexity of search algorithms

## Chapter Structure

- **theory.md** - Comprehensive explanations of searching algorithms
- **examples.md** - Annotated implementations and variations
- **exercises.md** - Practice problems organized by difficulty
- **solutions.md** - Detailed solutions with complexity analysis
- **tips.md** - Tips, tricks, common pitfalls, and 50+ LeetCode practice problems

## Prerequisites

Before starting this chapter, you should be comfortable with:

- Arrays and Lists (Chapter 29)
- Recursion (Chapter 5)
- Complexity Analysis (Chapter 27)
- Sorting (Chapter 38)

## Key Concepts

### Basic Search Algorithms
- **Linear Search** - O(n), simple sequential search
- **Binary Search** - O(log n), for sorted data
- **Jump Search** - O(√n), jumping ahead by blocks
- **Interpolation Search** - O(log log n) average for uniform data
- **Exponential Search** - O(log n), for unbounded/infinite arrays

### Binary Search Variations
- **Standard Binary Search** - Find exact target
- **Leftmost/Rightmost Position** - Handle duplicates
- **Search Insert Position** - Where to insert target
- **Lower Bound/Upper Bound** - Find boundaries
- **Binary Search on Answer** - Search solution space

### Advanced Patterns
- **Binary Search on Sorted Array**
- **Binary Search on Rotated Array**
- **Binary Search on Matrix**
- **Binary Search on Abstract Search Space**
- **Ternary Search** - Finding maximum/minimum

## Time Complexity Summary

| Algorithm | Best | Average | Worst | Space | Use Case |
|-----------|------|---------|-------|-------|----------|
| Linear Search | O(1) | O(n) | O(n) | O(1) | Unsorted data, small n |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) | Sorted data |
| Jump Search | O(1) | O(√n) | O(√n) | O(1) | Sorted, expensive comparisons |
| Interpolation | O(1) | O(log log n) | O(n) | O(1) | Uniformly distributed |
| Exponential | O(1) | O(log n) | O(log n) | O(1) | Unbounded/infinite array |
| Ternary Search | O(1) | O(log₃ n) | O(log₃ n) | O(1) | Unimodal functions |

## Real-World Applications

- **Databases**: Index searching, query optimization
- **File Systems**: File and directory lookup
- **Search Engines**: Document retrieval, ranking
- **Autocomplete**: Prefix matching in dictionaries
- **E-commerce**: Product search, price filtering
- **Maps/GPS**: Location search, route finding
- **Machine Learning**: Hyperparameter tuning, optimization

## Study Approach

1. **Start with Theory** - Understand how each algorithm works
2. **Master Binary Search** - Practice until you can implement perfectly
3. **Learn Templates** - Memorize binary search templates
4. **Recognize Patterns** - Identify when to use binary search
5. **Practice Variations** - Handle duplicates, rotations, abstract spaces
6. **Solve Problems** - Work through 50+ LeetCode problems in tips.md

## Estimated Study Time

- Theory and concepts: 2-3 hours
- Binary search mastery: 3-4 hours
- Variations and templates: 3-4 hours
- Exercises: 6-8 hours
- LeetCode practice (50+ problems in tips.md): 40-55 hours

**Total**: 54-74 hours for mastery

## Navigation

- **Previous**: [Chapter 38: Sorting](../38_sorting/README.md)
- **Next**: [Chapter 40: Graph Algorithms](../40_graphs/README.md)
- **Home**: [Main README](../README.md)

---

## Quick Reference

### Binary Search Template

```python
def binary_search(nums, target):
    """
    Standard binary search template.
    Returns index if found, -1 otherwise.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### When to Use Binary Search

**Must have:**
- Sorted data (or can be sorted)
- Random access (arrays, not linked lists)

**Or:**
- Search space can be defined with monotonic property
- Can eliminate half of search space each iteration

**Examples:**
- Sorted array
- Rotated sorted array
- Search for answer in range [low, high]
- Peak finding
- Matrix search

### Common Pitfalls

```python
# ❌ WRONG: Integer overflow (in some languages)
mid = (left + right) // 2

# ✅ CORRECT: Avoid overflow
mid = left + (right - left) // 2

# ❌ WRONG: Infinite loop with duplicates
while left < right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid  # Can cause infinite loop!

# ✅ CORRECT: Always make progress
while left < right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1  # Always move forward
```

## Additional Resources

- [Binary Search Visualizer](https://www.cs.usfca.edu/~galles/visualization/Search.html)
- [LeetCode Binary Search Problems](https://leetcode.com/tag/binary-search/)
- [Python's bisect module documentation](https://docs.python.org/3/library/bisect.html)

---

Happy learning! Binary search is one of the most important algorithms in computer science. Master it well!
