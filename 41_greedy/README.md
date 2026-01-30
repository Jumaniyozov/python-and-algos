# Chapter 41: Greedy Algorithms

## Overview

Greedy algorithms make locally optimal choices at each step, hoping to find a global optimum. They're powerful when applicable but require careful analysis to ensure correctness. This chapter covers when greedy works, classic greedy problems, and how to recognize greedy patterns.

## Learning Objectives

By the end of this chapter, you will be able to:

1. Understand the greedy choice property and optimal substructure
2. Recognize when greedy algorithms are applicable
3. Implement classic greedy algorithms (interval scheduling, Huffman coding)
4. Apply greedy strategies to optimization problems
5. Prove correctness of greedy solutions
6. Solve interval, scheduling, and resource allocation problems
7. Combine greedy with other techniques

## Chapter Structure

- **theory.md** - Comprehensive explanations of greedy concepts and when they work
- **examples.md** - Annotated implementations of classic greedy algorithms
- **exercises.md** - 15-20 practice problems organized by difficulty
- **solutions.md** - Detailed solutions with correctness proofs
- **tips.md** - Tips, tricks, common pitfalls, and 40+ LeetCode practice problems

## Prerequisites

Before starting this chapter, you should be comfortable with:

- Sorting Algorithms (Chapter 38)
- Arrays and Strings (Chapter 29)
- Problem-Solving Patterns (Chapter 28)
- Complexity Analysis (Chapter 27)
- Priority Queues (Chapter 35)

## Key Concepts

### Greedy Fundamentals

- **Greedy Choice Property**
  - Local optimum leads to global optimum
  - Can make choice without considering future consequences
  - Choice can't be reverted later

- **Optimal Substructure**
  - Optimal solution contains optimal solutions to subproblems
  - Similar to dynamic programming but simpler
  - No need to solve overlapping subproblems

### Classic Greedy Problems

- **Interval Scheduling**
  - Activity selection
  - Meeting rooms
  - Non-overlapping intervals

- **Resource Allocation**
  - Job scheduling
  - Task assignment
  - Load balancing

- **Huffman Coding**
  - Optimal prefix-free encoding
  - Binary tree construction
  - Variable-length codes

- **Other Patterns**
  - Jump game variations
  - Gas station circuit
  - Partition problems

## When Greedy Works

### Requirements

1. **Greedy choice property**: Local optimum → global optimum
2. **Optimal substructure**: Problem can be broken down recursively
3. **No dependencies**: Current choice doesn't invalidate previous choices

### Common Indicators

- Sorting helps solve the problem
- Always taking min/max works
- Problem asks for "maximum/minimum number of..."
- Interval/scheduling problems
- Exchange argument can prove correctness

## Time Complexity Summary

| Problem Type | Typical Complexity | Notes |
|-------------|-------------------|-------|
| Interval scheduling | O(n log n) | Sorting dominates |
| Activity selection | O(n log n) | Sort by end time |
| Huffman coding | O(n log n) | Priority queue operations |
| Jump game | O(n) | Single pass |
| Two-pointer greedy | O(n) | Linear scan |

## Real-World Applications

- **Scheduling**: CPU scheduling, task assignment
- **Compression**: Huffman coding in ZIP, JPEG
- **Networking**: Dijkstra's algorithm (Chapter 37)
- **Finance**: Cashier's algorithm (making change)
- **Resource Management**: Load balancing, bin packing
- **Route Planning**: Greedy best-first search

## Study Approach

1. **Master the Theory** - Understand when greedy works vs fails
2. **Learn Classic Algorithms** - Activity selection, Huffman, interval problems
3. **Practice Pattern Recognition** - Identify greedy indicators
4. **Prove Correctness** - Use exchange arguments
5. **Solve Problems** - Work through exercises and LeetCode
6. **Compare with DP** - Understand the differences

## Estimated Study Time

- Theory and concepts: 3-4 hours
- Examples and implementation: 4-5 hours
- Exercises: 8-10 hours
- LeetCode practice (40+ problems in tips.md): 40-60 hours

**Total**: 55-80 hours for mastery

## Navigation

- **Previous**: [Chapter 40: Dynamic Programming](../40_dynamic_programming/README.md)
- **Next**: [Chapter 42: Backtracking](../42_backtracking/README.md)
- **Home**: [Main README](../README.md)

---

## Quick Reference

### Greedy vs Dynamic Programming

| Aspect | Greedy | Dynamic Programming |
|--------|--------|-------------------|
| Approach | Make best local choice | Consider all possibilities |
| Subproblems | Disjoint | Overlapping |
| Complexity | Usually O(n log n) | Usually O(n²) or higher |
| Correctness | Needs proof | Guaranteed if recurrence correct |
| Examples | Interval scheduling | Knapsack, LCS |

### Common Greedy Patterns

**1. Sort + Iterate**: Sort by key criterion, then greedily select
```python
intervals.sort(key=lambda x: x[1])  # Sort by end time
```

**2. Two Pointers**: Maintain pointers at extremes, move greedily
```python
while left < right:
    if condition:
        # Make greedy choice
```

**3. Priority Queue**: Always process min/max element
```python
heapq.heappush(pq, item)
best = heapq.heappop(pq)
```

**4. Counting/Frequency**: Track and greedily allocate
```python
count = Counter(items)
# Use counts greedily
```

## Additional Resources

- [VisuAlgo - Greedy Algorithms](https://visualgo.net/en/greedy)
- [LeetCode Greedy Problems](https://leetcode.com/tag/greedy/)
- "Introduction to Algorithms" (CLRS) - Chapter 16

---

Happy learning! Greedy algorithms are elegant and efficient when they work - learn to recognize when they apply!
