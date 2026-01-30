# Chapter 37: Advanced Graphs

## Overview

Advanced graph algorithms are essential for solving complex problems involving networks, paths, and connectivity. This chapter covers the most important shortest path and minimum spanning tree algorithms, which are fundamental to competitive programming and real-world applications.

## Learning Objectives

By the end of this chapter, you will be able to:

1. Implement Dijkstra's algorithm for single-source shortest paths
2. Apply Bellman-Ford algorithm for graphs with negative weights
3. Use Floyd-Warshall for all-pairs shortest paths
4. Construct minimum spanning trees with Kruskal's and Prim's algorithms
5. Understand when to use each algorithm
6. Optimize graph algorithms with appropriate data structures
7. Solve complex path and connectivity problems

## Chapter Structure

- **theory.md** - Comprehensive explanations of advanced graph algorithms
- **examples.md** - Annotated implementations with detailed walkthroughs
- **exercises.md** - 15-20 practice problems organized by difficulty
- **solutions.md** - Detailed solutions with complexity analysis
- **tips.md** - Tips, tricks, common pitfalls, and 50+ LeetCode practice problems

## Prerequisites

Before starting this chapter, you should be comfortable with:

- Basic Graph Theory (Chapter 36)
- Priority Queues and Heaps (Chapter 35)
- Union-Find/Disjoint Set (covered in this chapter)
- Complexity Analysis (Chapter 27)
- Hash Tables (Chapter 32)

## Key Concepts

### Shortest Path Algorithms

- **Dijkstra's Algorithm**
  - Single-source shortest paths (non-negative weights)
  - Priority queue optimization
  - Time complexity: O((V + E) log V) with binary heap

- **Bellman-Ford Algorithm**
  - Single-source shortest paths (handles negative weights)
  - Detects negative cycles
  - Time complexity: O(VE)

- **Floyd-Warshall Algorithm**
  - All-pairs shortest paths
  - Dynamic programming approach
  - Time complexity: O(V³)

### Minimum Spanning Tree (MST) Algorithms

- **Kruskal's Algorithm**
  - Edge-based greedy approach
  - Uses Union-Find data structure
  - Time complexity: O(E log E)

- **Prim's Algorithm**
  - Vertex-based greedy approach
  - Uses priority queue
  - Time complexity: O((V + E) log V)

## Time Complexity Summary

| Algorithm | Time Complexity | Space | Use Case |
|-----------|----------------|-------|----------|
| Dijkstra's | O((V + E) log V) | O(V) | Non-negative weights, single-source |
| Bellman-Ford | O(VE) | O(V) | Negative weights, detect negative cycles |
| Floyd-Warshall | O(V³) | O(V²) | All-pairs shortest paths, small graphs |
| Kruskal's MST | O(E log E) | O(V) | Sparse graphs |
| Prim's MST | O((V + E) log V) | O(V) | Dense graphs |

## Real-World Applications

- **Network Routing**: Internet packet routing (OSPF uses Dijkstra)
- **GPS Navigation**: Finding shortest routes
- **Telecommunications**: Network design with MST
- **Social Networks**: Finding degrees of separation
- **Game Development**: Pathfinding in games
- **Supply Chain**: Optimizing transportation networks
- **VLSI Design**: Chip layout optimization

## Study Approach

1. **Master the Theory** - Understand how each algorithm works
2. **Learn Data Structures** - Priority queues, Union-Find are crucial
3. **Implement from Scratch** - Code each algorithm multiple times
4. **Recognize Patterns** - Know when to use which algorithm
5. **Practice Problems** - Work through exercises and LeetCode problems
6. **Optimize** - Learn to choose the right implementation for the problem

## Estimated Study Time

- Theory and concepts: 4-5 hours
- Examples and implementation: 6-8 hours
- Exercises: 10-12 hours
- LeetCode practice (50+ problems in tips.md): 60-80 hours

**Total**: 80-105 hours for mastery

## Navigation

- **Previous**: [Chapter 36: Graphs](../36_graphs/README.md)
- **Next**: [Chapter 38: Sorting](../38_sorting/README.md)
- **Home**: [Main README](../README.md)

---

## Quick Reference

### Dijkstra's Algorithm Template
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        if curr_dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
```

### When to Use Which Algorithm

**Dijkstra's**: Non-negative weights, single-source shortest path
**Bellman-Ford**: Negative weights allowed, detect negative cycles
**Floyd-Warshall**: All-pairs shortest paths, small dense graphs
**Kruskal's**: Minimum spanning tree, sparse graphs
**Prim's**: Minimum spanning tree, dense graphs

## Additional Resources

- [VisuAlgo - Graph Algorithms](https://visualgo.net/en/sssp)
- [LeetCode Graph Problems](https://leetcode.com/tag/graph/)
- [Priority Queue Implementation](https://docs.python.org/3/library/heapq.html)

---

Happy learning! Advanced graph algorithms are the foundation of many efficient solutions in computer science.
