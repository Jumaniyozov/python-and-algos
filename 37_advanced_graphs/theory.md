# Chapter 37: Advanced Graphs - Theory

## Table of Contents
1. [Introduction](#introduction)
2. [Dijkstra's Algorithm](#dijkstras-algorithm)
3. [Bellman-Ford Algorithm](#bellman-ford-algorithm)
4. [Floyd-Warshall Algorithm](#floyd-warshall-algorithm)
5. [Minimum Spanning Trees](#minimum-spanning-trees)
6. [Kruskal's Algorithm](#kruskals-algorithm)
7. [Prim's Algorithm](#prims-algorithm)
8. [Union-Find Data Structure](#union-find-data-structure)
9. [Complexity Analysis](#complexity-analysis)

---

## Introduction

Advanced graph algorithms solve two fundamental problems:

1. **Shortest Path Problems**: Finding the minimum-cost path between vertices
2. **Minimum Spanning Tree Problems**: Connecting all vertices with minimum total edge weight

These algorithms power everything from GPS navigation to network routing protocols.

---

## Dijkstra's Algorithm

### Overview

Dijkstra's algorithm finds the shortest path from a single source vertex to all other vertices in a weighted graph. It only works with **non-negative edge weights**.

### How It Works

1. Initialize distances: source = 0, all others = ∞
2. Use a priority queue (min-heap) to always process the closest unvisited vertex
3. For each vertex, relax all its neighbors (update if shorter path found)
4. Mark vertex as visited (never revisit)
5. Repeat until all vertices are processed

### Visualization

```
Graph:
    (A)---3---(B)
     |         |
     4         2
     |         |
    (C)---1---(D)

Starting from A:

Step 1: distances = {A:0, B:∞, C:∞, D:∞}
        Process A, relax neighbors B and C
        distances = {A:0, B:3, C:4, D:∞}

Step 2: Process B (distance 3), relax D
        distances = {A:0, B:3, C:4, D:5}

Step 3: Process C (distance 4), relax D
        distances = {A:0, B:3, C:4, D:5} (no change, 4+1=5 not better)

Step 4: Process D (distance 5)
        Final: {A:0, B:3, C:4, D:5}
```

### Implementation

```python
import heapq

def dijkstra(graph, start):
    """
    Dijkstra's shortest path algorithm.

    Args:
        graph: Dict of adjacency lists {node: [(neighbor, weight), ...]}
        start: Starting vertex

    Returns:
        Dictionary of shortest distances from start to each vertex

    Time: O((V + E) log V) with binary heap
    Space: O(V)
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue: (distance, node)
    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        # Skip if we've already found a better path
        if curr_dist > distances[node]:
            continue

        # Relax all neighbors
        for neighbor, weight in graph[node]:
            distance = curr_dist + weight

            # If shorter path found, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
```

### Key Properties

- **Greedy algorithm**: Always processes the closest unvisited vertex
- **Optimal substructure**: Shortest path to B through A is shortest path to A + edge AB
- **Cannot handle negative weights**: Greedy choice fails with negative edges
- **Single-source**: Computes distances from one vertex to all others

### Time Complexity

- **Binary heap**: O((V + E) log V)
- **Fibonacci heap**: O(E + V log V) - better for dense graphs
- **Array-based**: O(V²) - better for very dense graphs

---

## Bellman-Ford Algorithm

### Overview

Bellman-Ford finds shortest paths from a single source, **even with negative edge weights**. It can also **detect negative cycles**.

### How It Works

1. Initialize distances: source = 0, all others = ∞
2. Relax all edges V-1 times (where V is number of vertices)
3. Check for negative cycles by relaxing once more
4. If any distance decreases in step 3, a negative cycle exists

### Why V-1 Iterations?

In a graph with V vertices, the longest simple path has at most V-1 edges. After V-1 iterations of relaxing all edges, all shortest paths are guaranteed to be found.

### Visualization

```
Graph with negative weight:
    (A)---2-->(B)
     |         |
     4        -3
     ↓         ↓
    (C)<--1---(D)

Iteration 0: distances = {A:0, B:∞, C:∞, D:∞}

Iteration 1: Relax all edges
  A→B: 0+2=2 < ∞  → B:2
  A→C: 0+4=4 < ∞  → C:4
  B→D: 2+(-3)=-1 < ∞ → D:-1
  D→C: -1+1=0 < 4 → C:0

Iteration 2: Relax all edges
  (no changes)

Final: {A:0, B:2, C:0, D:-1}
```

### Implementation

```python
def bellman_ford(graph, start, num_vertices):
    """
    Bellman-Ford shortest path algorithm.

    Args:
        graph: List of edges [(u, v, weight), ...]
        start: Starting vertex
        num_vertices: Number of vertices

    Returns:
        Tuple: (distances dict, has_negative_cycle bool)

    Time: O(VE)
    Space: O(V)
    """
    distances = {i: float('inf') for i in range(num_vertices)}
    distances[start] = 0

    # Relax all edges V-1 times
    for _ in range(num_vertices - 1):
        for u, v, weight in graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative cycles
    has_negative_cycle = False
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            has_negative_cycle = True
            break

    return distances, has_negative_cycle
```

### Key Properties

- **Handles negative weights**: Unlike Dijkstra's
- **Detects negative cycles**: Returns True if one exists
- **Slower than Dijkstra's**: O(VE) vs O((V+E) log V)
- **Simpler to implement**: No need for priority queue

### When to Use

- Graph has negative edge weights
- Need to detect negative cycles
- Graph is small (performance doesn't matter)

---

## Floyd-Warshall Algorithm

### Overview

Floyd-Warshall finds shortest paths between **all pairs of vertices**. It uses dynamic programming and works with negative weights (but not negative cycles).

### How It Works

The algorithm considers paths through intermediate vertices. For each pair (i, j), it checks if going through intermediate vertex k gives a shorter path.

**DP Formula**:
```
dist[i][j] = min(
    dist[i][j],                    # Direct path
    dist[i][k] + dist[k][j]       # Path through k
)
```

### Visualization

```
Graph:
    1 --5--> 2
    |        |
    2        1
    ↓        ↓
    3 --2--> 4

Initial distance matrix:
     1   2   3   4
1 [  0   5   2   ∞ ]
2 [  ∞   0   ∞   1 ]
3 [  ∞   ∞   0   2 ]
4 [  ∞   ∞   ∞   0 ]

After considering vertex 1 as intermediate:
(No changes, no paths improved through 1)

After considering vertex 2 as intermediate:
     1   2   3   4
1 [  0   5   2   6 ]  ← 1→2→4 = 5+1 = 6
2 [  ∞   0   ∞   1 ]
3 [  ∞   ∞   0   2 ]
4 [  ∞   ∞   ∞   0 ]

After considering vertex 3 as intermediate:
     1   2   3   4
1 [  0   5   2   4 ]  ← 1→3→4 = 2+2 = 4 (better than 6!)
2 [  ∞   0   ∞   1 ]
3 [  ∞   ∞   0   2 ]
4 [  ∞   ∞   ∞   0 ]

After considering vertex 4 as intermediate:
(No changes)

Final all-pairs shortest distances:
     1   2   3   4
1 [  0   5   2   4 ]
2 [  ∞   0   ∞   1 ]
3 [  ∞   ∞   0   2 ]
4 [  ∞   ∞   ∞   0 ]
```

### Implementation

```python
def floyd_warshall(num_vertices, edges):
    """
    Floyd-Warshall all-pairs shortest path algorithm.

    Args:
        num_vertices: Number of vertices
        edges: List of edges [(u, v, weight), ...]

    Returns:
        2D list of shortest distances between all pairs

    Time: O(V³)
    Space: O(V²)
    """
    # Initialize distance matrix
    INF = float('inf')
    dist = [[INF] * num_vertices for _ in range(num_vertices)]

    # Distance from vertex to itself is 0
    for i in range(num_vertices):
        dist[i][i] = 0

    # Add edge weights
    for u, v, weight in edges:
        dist[u][v] = weight

    # Try all intermediate vertices
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Can we improve path from i to j by going through k?
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
```

### Key Properties

- **All-pairs shortest paths**: Finds distances between every pair
- **Dynamic programming**: Bottom-up approach
- **Handles negative weights**: But not negative cycles
- **Simple implementation**: Just 3 nested loops
- **Dense graph friendly**: O(V³) better than V times Dijkstra when graph is dense

### When to Use

- Need all-pairs shortest paths
- Small graphs (V < 400 typically)
- Graph is dense
- Want simple implementation

---

## Minimum Spanning Trees

### Definition

A **Minimum Spanning Tree (MST)** is a subset of edges that:
1. Connects all vertices (spanning tree)
2. Has minimum total edge weight
3. Contains no cycles
4. Has exactly V-1 edges (where V is number of vertices)

### Properties

- Not unique: Multiple MSTs can exist with same total weight
- Removing any edge disconnects the tree
- Adding any edge creates a cycle
- Used in network design to minimize cost

### Visualization

```
Original graph:
       A
      /|\
     4 | 2
    /  |  \
   B---5---C
    \ 3 \ /1
     \   X
      \ / \
       D---6---E

Possible MSTs (both have weight 10):

MST 1:          MST 2:
    A               A
    |               |
    2               2
    |               |
    C               C
   /|              /|
  1 3             1 5
 /  |            /  |
E   D           E   B
    |               |
    3               3
    |               |
    B               D

Both have total weight: 2+1+3+3 = 10
```

---

## Kruskal's Algorithm

### Overview

Kruskal's is a **greedy algorithm** that builds the MST by adding edges in order of increasing weight, skipping edges that would create cycles.

### How It Works

1. Sort all edges by weight (ascending)
2. Initialize Union-Find structure for all vertices
3. For each edge (u, v):
   - If u and v are in different components (adding edge won't create cycle):
     - Add edge to MST
     - Union the components
4. Stop when MST has V-1 edges

### Visualization

```
Graph edges (sorted by weight):
1: C-E (1)
2: A-C (2)
3: B-D (3)
4: D-E (3)
5: A-B (4)
6: B-C (5)
7: E-F (6)

Step-by-step:

1. Add C-E (1): Components: {A},{B},{C,E},{D},{F}
   MST edges: [(C,E,1)]

2. Add A-C (2): Components: {A,C,E},{B},{D},{F}
   MST edges: [(C,E,1), (A,C,2)]

3. Add B-D (3): Components: {A,C,E},{B,D},{F}
   MST edges: [(C,E,1), (A,C,2), (B,D,3)]

4. Add D-E (3): Components: {A,B,C,D,E},{F}
   MST edges: [(C,E,1), (A,C,2), (B,D,3), (D,E,3)]

5. Skip A-B (4): Would create cycle in {A,B,C,D,E}

6. Skip B-C (5): Would create cycle

7. Add E-F (6): Components: {A,B,C,D,E,F}
   MST edges: [(C,E,1), (A,C,2), (B,D,3), (D,E,3), (E,F,6)]

Total weight: 1+2+3+3+6 = 15
```

### Implementation

```python
class UnionFind:
    """Union-Find data structure for Kruskal's algorithm."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """Find with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union by rank."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same set

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(num_vertices, edges):
    """
    Kruskal's MST algorithm.

    Args:
        num_vertices: Number of vertices
        edges: List of edges [(u, v, weight), ...]

    Returns:
        Tuple: (MST edges list, total weight)

    Time: O(E log E) - dominated by sorting
    Space: O(V)
    """
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(num_vertices)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        # If adding edge doesn't create cycle
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

            # MST complete when we have V-1 edges
            if len(mst) == num_vertices - 1:
                break

    return mst, total_weight
```

### Key Properties

- **Edge-based**: Processes edges, not vertices
- **Requires sorting**: O(E log E)
- **Uses Union-Find**: To detect cycles efficiently
- **Best for sparse graphs**: When E is much less than V²

---

## Prim's Algorithm

### Overview

Prim's is a **greedy algorithm** that builds the MST by starting from a vertex and always adding the minimum-weight edge that connects a new vertex to the growing tree.

### How It Works

1. Start with arbitrary vertex
2. Initialize priority queue with all edges from starting vertex
3. While MST doesn't have all vertices:
   - Pop minimum-weight edge from queue
   - If edge connects to unvisited vertex:
     - Add edge to MST
     - Mark vertex as visited
     - Add all edges from new vertex to queue

### Visualization

```
Graph:
       A
      /|\
     4 | 2
    /  |  \
   B---5---C
    \ 3   /1
     \   /
      \ /
       D

Start from A:

Step 1: Start with A, add edges: (A,B,4), (A,C,2)
        Choose (A,C,2) - minimum
        MST: [(A,C,2)], In tree: {A,C}

Step 2: From C, add edges: (C,D,1), (C,B,5)
        Min of all: (C,D,1)
        MST: [(A,C,2), (C,D,1)], In tree: {A,C,D}

Step 3: From D, add edge: (D,B,3)
        Choose (D,B,3)
        MST: [(A,C,2), (C,D,1), (D,B,3)], In tree: {A,B,C,D}

Total weight: 2+1+3 = 6
```

### Implementation

```python
import heapq

def prim(graph, start=0):
    """
    Prim's MST algorithm.

    Args:
        graph: Dict of adjacency lists {node: [(neighbor, weight), ...]}
        start: Starting vertex

    Returns:
        Tuple: (MST edges list, total weight)

    Time: O((V + E) log V) with binary heap
    Space: O(V)
    """
    visited = set()
    mst = []
    total_weight = 0

    # Priority queue: (weight, from_node, to_node)
    pq = [(0, start, start)]

    while pq and len(visited) < len(graph):
        weight, from_node, to_node = heapq.heappop(pq)

        # Skip if already visited
        if to_node in visited:
            continue

        # Add to MST
        visited.add(to_node)
        if from_node != to_node:  # Skip first dummy edge
            mst.append((from_node, to_node, weight))
            total_weight += weight

        # Add all edges from newly added vertex
        for neighbor, edge_weight in graph[to_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, to_node, neighbor))

    return mst, total_weight
```

### Key Properties

- **Vertex-based**: Grows tree one vertex at a time
- **Requires priority queue**: To find minimum edge efficiently
- **Best for dense graphs**: When E approaches V²
- **Simpler than Kruskal**: No need for Union-Find

---

## Union-Find Data Structure

### Overview

Union-Find (Disjoint Set Union) efficiently tracks disjoint sets and supports two operations:
- **Find**: Determine which set an element belongs to
- **Union**: Merge two sets

### Optimizations

**1. Path Compression**: Make tree flatter during find operations
```python
def find(self, x):
    if self.parent[x] != x:
        self.parent[x] = self.find(self.parent[x])  # Path compression
    return self.parent[x]
```

**2. Union by Rank**: Attach smaller tree under larger tree
```python
def union(self, x, y):
    root_x, root_y = self.find(x), self.find(y)
    if self.rank[root_x] < self.rank[root_y]:
        self.parent[root_x] = root_y
    elif self.rank[root_x] > self.rank[root_y]:
        self.parent[root_y] = root_x
    else:
        self.parent[root_y] = root_x
        self.rank[root_x] += 1
```

### Time Complexity

With both optimizations:
- **Find**: O(α(n)) - inverse Ackermann function, effectively O(1)
- **Union**: O(α(n)) - effectively O(1)

---

## Complexity Analysis

### Comparison Table

| Algorithm | Time Complexity | Space | Best For |
|-----------|----------------|-------|----------|
| Dijkstra | O((V+E) log V) | O(V) | Non-negative, single-source |
| Bellman-Ford | O(VE) | O(V) | Negative weights, small graphs |
| Floyd-Warshall | O(V³) | O(V²) | All-pairs, dense small graphs |
| Kruskal | O(E log E) | O(V) | Sparse graphs MST |
| Prim | O((V+E) log V) | O(V) | Dense graphs MST |

### When to Use Each Algorithm

**Shortest Path:**
- **Dijkstra**: Default choice for non-negative weights
- **Bellman-Ford**: Negative weights or need cycle detection
- **Floyd-Warshall**: All-pairs, small dense graph

**Minimum Spanning Tree:**
- **Kruskal**: Sparse graph (E << V²)
- **Prim**: Dense graph (E ≈ V²)

---

## Summary

**Shortest Path Algorithms:**
1. **Dijkstra's**: Greedy, uses priority queue, non-negative weights only
2. **Bellman-Ford**: Dynamic programming, handles negative weights, detects cycles
3. **Floyd-Warshall**: All-pairs, dynamic programming, O(V³)

**MST Algorithms:**
1. **Kruskal's**: Edge-based greedy, uses Union-Find, best for sparse
2. **Prim's**: Vertex-based greedy, uses priority queue, best for dense

**Key Takeaways:**
- Choose algorithm based on graph properties (negative weights? all-pairs? dense/sparse?)
- Use appropriate data structures (priority queue, Union-Find)
- Understand trade-offs between time and space complexity
- These algorithms are fundamental to many real-world applications

Master these algorithms - they appear frequently in interviews and competitive programming!
