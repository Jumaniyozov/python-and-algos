# Chapter 38: Sorting

## Overview

Sorting is one of the most fundamental operations in computer science. A sorting algorithm arranges elements in a specific order (ascending or descending). Understanding various sorting algorithms, their trade-offs, and when to use each is essential for any software engineer.

## Learning Objectives

By the end of this chapter, you will be able to:

1. Understand and implement major sorting algorithms
2. Analyze time and space complexity of different sorting methods
3. Choose the appropriate sorting algorithm for specific scenarios
4. Understand stability in sorting and why it matters
5. Master Python's built-in sorting (Timsort)
6. Solve complex sorting problems efficiently
7. Recognize sorting patterns in interview problems

## Chapter Structure

- **theory.md** - Comprehensive explanations of all major sorting algorithms
- **examples.md** - Annotated implementations of sorting algorithms
- **exercises.md** - Practice problems organized by difficulty
- **solutions.md** - Detailed solutions with complexity analysis
- **tips.md** - Tips, tricks, common pitfalls, and 40+ LeetCode practice problems

## Prerequisites

Before starting this chapter, you should be comfortable with:

- Arrays and Lists (Chapter 29)
- Recursion (Chapter 5)
- Complexity Analysis (Chapter 27)
- Problem-Solving Patterns (Chapter 28)

## Key Concepts

### Comparison-Based Sorts
- Bubble Sort - Simple but inefficient (O(n²))
- Selection Sort - Simple selection of minimum (O(n²))
- Insertion Sort - Efficient for small/nearly sorted arrays (O(n²))
- Merge Sort - Divide and conquer, stable (O(n log n))
- Quick Sort - Fast average case, in-place (O(n log n))
- Heap Sort - Guaranteed O(n log n), in-place

### Non-Comparison Sorts
- Counting Sort - Linear time for small range (O(n+k))
- Radix Sort - Sorts by digits (O(d·n))
- Bucket Sort - Distributes into buckets (O(n+k))

### Sorting Properties
- **Stability**: Maintains relative order of equal elements
- **In-place**: Uses O(1) extra space
- **Adaptive**: Performs better on partially sorted data
- **Online**: Can sort data as it arrives

## Time Complexity Summary

| Algorithm | Best | Average | Worst | Space | Stable | In-Place |
|-----------|------|---------|-------|-------|--------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes | No |
| Radix Sort | O(d·n) | O(d·n) | O(d·n) | O(n+k) | Yes | No |
| Bucket Sort | O(n+k) | O(n+k) | O(n²) | O(n+k) | Yes | No |
| Timsort | O(n) | O(n log n) | O(n log n) | O(n) | Yes | No |

## Real-World Applications

- **Databases**: Query result ordering, index creation
- **E-commerce**: Product sorting (price, rating, date)
- **Search Engines**: Ranking search results
- **Operating Systems**: Process scheduling
- **Data Analysis**: Organizing data for visualization
- **Machine Learning**: K-nearest neighbors, preprocessing
- **Gaming**: Leaderboards and rankings

## Study Approach

1. **Start with Theory** - Understand how each algorithm works
2. **Visualize** - Draw diagrams and trace algorithm steps
3. **Implement** - Code each algorithm from scratch
4. **Compare** - Understand trade-offs between algorithms
5. **Practice** - Solve exercises and LeetCode problems
6. **Optimize** - Learn when to use each sorting method

## Estimated Study Time

- Theory and concepts: 3-4 hours
- Implementation practice: 4-5 hours
- Exercises: 6-8 hours
- LeetCode practice (40+ problems in tips.md): 35-45 hours

**Total**: 48-62 hours for mastery

## Navigation

- **Previous**: [Chapter 37: Problem-Solving Patterns](../37_problem_patterns/README.md)
- **Next**: [Chapter 39: Searching](../39_searching/README.md)
- **Home**: [Main README](../README.md)

---

## Quick Reference

### Python's Built-in Sorting

```python
# sorted() - returns new sorted list
nums = [3, 1, 4, 1, 5]
sorted_nums = sorted(nums)  # [1, 1, 3, 4, 5]

# list.sort() - sorts in-place
nums.sort()  # nums is now [1, 1, 3, 4, 5]

# Custom key function
words = ['banana', 'apple', 'cherry']
sorted(words, key=len)  # ['apple', 'banana', 'cherry']

# Reverse sorting
sorted(nums, reverse=True)  # [5, 4, 3, 1, 1]

# Sort by multiple criteria
students = [('Alice', 25), ('Bob', 20), ('Charlie', 25)]
sorted(students, key=lambda x: (x[1], x[0]))  # By age, then name
```

### When to Use Each Algorithm

- **Nearly sorted data**: Insertion Sort
- **Small arrays (n < 50)**: Insertion Sort
- **Need guaranteed O(n log n)**: Merge Sort or Heap Sort
- **Average case speed, in-place**: Quick Sort
- **Stability required**: Merge Sort or Timsort
- **Small integer range**: Counting Sort
- **Fixed-length integers**: Radix Sort
- **Uniformly distributed data**: Bucket Sort
- **General purpose**: Use Python's built-in sort (Timsort)

## Additional Resources

- [VisuAlgo - Sorting Visualizations](https://visualgo.net/en/sorting)
- [LeetCode Sorting Problems](https://leetcode.com/tag/sorting/)
- [Python's Timsort Explained](https://github.com/python/cpython/blob/main/Objects/listsort.txt)

---

Happy learning! Mastering sorting algorithms is essential for coding interviews and efficient programming!
