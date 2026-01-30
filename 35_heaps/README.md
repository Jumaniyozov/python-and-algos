# Chapter 35: Heaps

## Overview
This chapter covers heap data structures and priority queues, essential tools for efficiently managing and retrieving elements based on priority. Heaps are fundamental to many algorithms including graph algorithms (Dijkstra's), sorting (heap sort), and solving problems involving top/bottom K elements.

## Learning Objectives
By the end of this chapter, you will:
- Understand heap properties and the complete binary tree structure
- Master min heap and max heap operations
- Implement heaps using arrays and Python's heapq module
- Apply priority queues to solve scheduling and optimization problems
- Recognize and solve Top K Elements and Two Heaps patterns
- Analyze time and space complexity of heap operations
- Use heaps for heap sort and finding running medians

## Prerequisites
Before starting this chapter, you should be familiar with:
- **Trees** (Chapter 30): Binary trees and tree traversals
- **Arrays** (Chapter 5): Array manipulation and indexing
- **Complexity Analysis** (Chapter 3): Big O notation for time and space
- **Recursion** (Chapter 12): Recursive thinking for heapify operations
- **Sorting** (Chapter 15): Basic sorting algorithms for comparison

## Chapter Structure

### 1. Theory (`theory.md`)
- Heap fundamentals and properties
- Binary heap representation using arrays
- Min heap vs max heap
- Core operations: insert, extract, peek, heapify
- Python's heapq module comprehensive guide
- Priority queue implementation
- Heap sort algorithm
- Complexity analysis

### 2. Examples (`examples.md`)
- Min heap implementation from scratch
- Max heap using heapq (negation trick)
- Priority queue examples
- Top K elements pattern
- K-way merge pattern
- Running median problem
- Task scheduling examples
- Heap sort implementation

### 3. Exercises (`exercises.md`)
- **Easy**: 6-8 problems on basic heap operations
- **Medium**: 10-12 problems on top K, scheduling, merging
- **Hard**: 4-6 problems on median finding and complex scheduling

### 4. Solutions (`solutions.md`)
- Complete Python implementations
- Detailed explanations and intuition
- Time and space complexity analysis
- Alternative approaches and optimizations
- Heap vs. sorting trade-offs

### 5. Tips (`tips.md`)
- Common pitfalls and how to avoid them
- Pattern recognition guide
- Interview strategies
- 60+ LeetCode practice problems organized by difficulty
- Must-know problems (Top 15)
- 4-6 week practice progression
- Pattern mastery checklist

## Study Time Estimates

### Initial Learning (12-15 hours)
- Theory and fundamentals: 3-4 hours
- Examples and implementations: 4-5 hours
- Basic exercises: 5-6 hours

### Practice and Mastery (50-65 hours)
- Easy problems: 10-15 hours (15-20 problems)
- Medium problems: 25-35 hours (30-35 problems)
- Hard problems: 15-15 hours (10-15 problems)

### Total Time: 62-80 hours

## Key Concepts

### Heap Properties
- **Complete Binary Tree**: All levels filled except possibly the last, filled left to right
- **Heap Property**: Parent-child relationship determines order
- **Array Representation**: Efficient storage without pointers
- **Height**: O(log n) for n elements

### Min Heap vs Max Heap
- **Min Heap**: Parent smaller than children (root is minimum)
- **Max Heap**: Parent larger than children (root is maximum)
- **Python Default**: heapq implements min heap
- **Max Heap Trick**: Negate values to simulate max heap

### Core Operations
- **Insert**: Add element and bubble up - O(log n)
- **Extract Min/Max**: Remove root and bubble down - O(log n)
- **Peek**: Access root without removal - O(1)
- **Heapify**: Convert array to heap - O(n)
- **Build Heap**: Create heap from scratch - O(n)

### Common Patterns
1. **Top K Elements**: Find K largest/smallest elements
2. **Two Heaps**: Maintain two heaps for median finding
3. **K-way Merge**: Merge K sorted arrays efficiently
4. **Scheduling**: Task scheduling with priorities
5. **Graph Algorithms**: Dijkstra's shortest path

## Real-World Applications

### Operating Systems
- **Process Scheduling**: CPU assigns time based on priority
- **Memory Management**: Allocate memory to highest priority tasks
- **Event-Driven Simulation**: Process events in time order

### Algorithms
- **Dijkstra's Algorithm**: Shortest path using min heap
- **Huffman Coding**: Build optimal prefix codes
- **Heap Sort**: In-place sorting algorithm
- **Prim's Algorithm**: Minimum spanning tree

### Applications
- **Task Scheduling**: Execute tasks by priority or deadline
- **Data Streaming**: Find top K elements in stream
- **Median Finding**: Running median in data stream
- **Load Balancing**: Assign jobs to least loaded server
- **Route Planning**: Find shortest paths in navigation

### System Design
- **Priority Queues**: Message queues with priorities
- **Rate Limiting**: Process requests by priority
- **Cache Eviction**: LFU cache with frequency counts
- **Job Schedulers**: Batch processing systems

## Why Heaps Matter

### Efficiency
- **Fast Operations**: O(log n) for insert and extract
- **Space Efficient**: Array-based implementation
- **Optimal for Priority**: Better than sorting for top K problems

### Versatility
- **Multiple Patterns**: Solves various problem types
- **Building Block**: Used in many algorithms
- **Practical**: Common in real systems

### Interview Frequency
- **Very Common**: Appears in 15-20% of interviews
- **Pattern-Based**: Once you know patterns, many problems become easy
- **Multiple Contexts**: Can appear as direct heap problem or as optimization

## Navigation
- **Previous**: [Chapter 34: Tries](../34_tries/README.md)
- **Next**: [Chapter 36: Graphs](../36_graphs/README.md)
- **Main**: [Back to Main Index](../README.md)

## Quick Reference

### Python heapq Cheat Sheet
```python
import heapq

# Create heap
heap = []
heapq.heapify(arr)  # In-place O(n)

# Operations
heapq.heappush(heap, item)      # O(log n)
item = heapq.heappop(heap)      # O(log n)
item = heap[0]                  # Peek O(1)
heapq.heappushpop(heap, item)   # O(log n)
item = heapq.heapreplace(heap, item)  # O(log n)

# K largest/smallest
heapq.nlargest(k, arr)          # O(n log k)
heapq.nsmallest(k, arr)         # O(n log k)

# Max heap trick
heapq.heappush(max_heap, -item)
item = -heapq.heappop(max_heap)
```

### Time Complexities
| Operation | Average | Worst Case |
|-----------|---------|------------|
| Insert | O(log n) | O(log n) |
| Extract | O(log n) | O(log n) |
| Peek | O(1) | O(1) |
| Heapify | O(n) | O(n) |
| Build Heap | O(n) | O(n) |
| Heap Sort | O(n log n) | O(n log n) |

## Getting Started
1. Read `theory.md` to understand heap fundamentals
2. Study `examples.md` for practical implementations
3. Practice with `exercises.md` starting from easy problems
4. Check `solutions.md` for detailed solutions
5. Use `tips.md` for interview preparation and LeetCode practice
6. Focus on mastering Top K and Two Heaps patterns first
