# Chapter 37: Advanced Graphs - Tips and Tricks

## Table of Contents
1. [Common Pitfalls](#common-pitfalls)
2. [Pattern Recognition](#pattern-recognition)
3. [Algorithm Selection Guide](#algorithm-selection-guide)
4. [Implementation Tips](#implementation-tips)
5. [LeetCode Practice Problems](#leetcode-practice-problems)

---

## Common Pitfalls

### 1. Wrong Algorithm Choice

```python
# ❌ WRONG: Using Dijkstra with negative weights
def shortest_path_negative(graph, start):
    # Dijkstra fails with negative weights!
    return dijkstra(graph, start)  # Will give wrong answer

# ✅ CORRECT: Use Bellman-Ford for negative weights
def shortest_path_negative(graph, start):
    return bellman_ford(graph, start)
```

**Why it fails**: Dijkstra's greedy choice assumption breaks down with negative weights.

---

### 2. Forgetting to Check Reachability

```python
# ❌ WRONG: Assuming all nodes are reachable
def network_delay(times, n, k):
    distances = dijkstra(times, k)
    return max(distances.values())  # Could be infinity!

# ✅ CORRECT: Check if all nodes reachable
def network_delay(times, n, k):
    distances = dijkstra(times, k)
    max_dist = max(distances.values())
    return max_dist if max_dist != float('inf') else -1
```

---

### 3. Not Handling Visited Nodes in Dijkstra

```python
# ❌ WRONG: Not skipping already-processed nodes
def dijkstra_wrong(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)
        # Missing check! Will process same node multiple times

        for neighbor, weight in graph[node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

# ✅ CORRECT: Skip if better path already found
def dijkstra_correct(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        # Skip if we already found a better path
        if curr_dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
```

---

### 4. Union-Find Without Optimizations

```python
# ❌ WRONG: Naive union-find (O(n) per operation)
class UnionFindSlow:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

# ✅ CORRECT: With path compression and union by rank
class UnionFindFast:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True
```

---

### 5. Bellman-Ford Early Termination Missing

```python
# ❌ WRONG: Always doing V-1 iterations
def bellman_ford_slow(num_vertices, edges, start):
    distances = [float('inf')] * num_vertices
    distances[start] = 0

    for _ in range(num_vertices - 1):
        for u, v, weight in edges:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    # Always does V-1 iterations even if no changes

# ✅ CORRECT: Early termination when no updates
def bellman_ford_fast(num_vertices, edges, start):
    distances = [float('inf')] * num_vertices
    distances[start] = 0

    for _ in range(num_vertices - 1):
        updated = False
        for u, v, weight in edges:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                updated = True

        if not updated:  # No changes, can stop early
            break
```

---

### 6. MST Edge Count

```python
# ❌ WRONG: Not stopping at V-1 edges
def kruskal_wrong(num_vertices, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(num_vertices)
    mst = []

    for u, v, weight in edges:  # Processes all edges!
        if uf.union(u, v):
            mst.append((u, v, weight))

# ✅ CORRECT: Stop when MST complete
def kruskal_correct(num_vertices, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(num_vertices)
    mst = []

    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            if len(mst) == num_vertices - 1:  # MST complete
                break
```

---

## Pattern Recognition

### Pattern 1: Single-Source Shortest Path (Non-Negative)

**Use Dijkstra's Algorithm**

**Indicators:**
- Find shortest path from one source
- All weights are non-negative
- Need efficient solution

**Template:**
```python
import heapq

def dijkstra_pattern(graph, start):
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

**Example Problems:**
- Network Delay Time
- Path with Minimum Effort
- Shortest Path in Grid

---

### Pattern 2: Negative Weights or Limited Steps

**Use Bellman-Ford**

**Indicators:**
- Graph has negative edge weights
- Need to detect negative cycles
- Limited number of edges allowed (k stops)

**Template:**
```python
def bellman_ford_pattern(num_vertices, edges, start, max_steps=None):
    distances = [float('inf')] * num_vertices
    distances[start] = 0

    iterations = max_steps + 1 if max_steps else num_vertices - 1

    for _ in range(iterations):
        temp = distances.copy()
        for u, v, weight in edges:
            if distances[u] != float('inf'):
                temp[v] = min(temp[v], distances[u] + weight)
        distances = temp

    return distances
```

**Example Problems:**
- Cheapest Flights Within K Stops
- Negative weight graph shortest paths

---

### Pattern 3: All-Pairs Shortest Paths

**Use Floyd-Warshall**

**Indicators:**
- Need distances between all pairs of vertices
- Graph is small (n < 400)
- Dense graph

**Template:**
```python
def floyd_warshall_pattern(num_vertices, edges):
    INF = float('inf')
    dist = [[INF] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        dist[i][i] = 0

    for u, v, weight in edges:
        dist[u][v] = weight

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
```

**Example Problems:**
- Find the City
- All pairs shortest distance queries

---

### Pattern 4: Minimum Spanning Tree (Sparse Graph)

**Use Kruskal's Algorithm**

**Indicators:**
- Need to connect all vertices with minimum cost
- Sparse graph (E << V²)
- Easy to sort edges

**Template:**
```python
def kruskal_pattern(num_vertices, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(num_vertices)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            if len(mst) == num_vertices - 1:
                break

    return mst, total_weight
```

**Example Problems:**
- Min Cost to Connect All Points
- Connecting Cities with Minimum Cost

---

### Pattern 5: Minimum Spanning Tree (Dense Graph)

**Use Prim's Algorithm**

**Indicators:**
- MST needed
- Dense graph (E ≈ V²)
- Starting from specific vertex

**Template:**
```python
import heapq

def prim_pattern(graph, start=0):
    visited = set()
    mst = []
    total_weight = 0
    pq = [(0, None, start)]

    while pq:
        weight, from_node, to_node = heapq.heappop(pq)

        if to_node in visited:
            continue

        visited.add(to_node)
        if from_node is not None:
            mst.append((from_node, to_node, weight))
            total_weight += weight

        for neighbor, edge_weight in graph[to_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, to_node, neighbor))

    return mst, total_weight
```

**Example Problems:**
- MST in dense graphs
- Network design problems

---

### Pattern 6: Modified Dijkstra (Maximize/Track Constraints)

**Indicators:**
- Need to maximize instead of minimize
- Track additional constraints (effort, probability)
- Early termination possible

**Template:**
```python
import heapq

def modified_dijkstra_pattern(graph, start, end, is_maximize=False):
    if is_maximize:
        best = {node: 0 for node in graph}
        best[start] = 1
        pq = [(-1, start)]  # Negative for max-heap
    else:
        best = {node: float('inf') for node in graph}
        best[start] = 0
        pq = [(0, start)]

    while pq:
        curr_val, node = heapq.heappop(pq)

        if is_maximize:
            curr_val = -curr_val

        if node == end:
            return curr_val

        if (is_maximize and curr_val < best[node]) or \
           (not is_maximize and curr_val > best[node]):
            continue

        for neighbor, edge_val in graph[node]:
            if is_maximize:
                new_val = curr_val * edge_val  # Or other operation
                if new_val > best[neighbor]:
                    best[neighbor] = new_val
                    heapq.heappush(pq, (-new_val, neighbor))
            else:
                new_val = max(curr_val, edge_val)  # Or other operation
                if new_val < best[neighbor]:
                    best[neighbor] = new_val
                    heapq.heappush(pq, (new_val, neighbor))

    return best[end]
```

**Example Problems:**
- Path with Maximum Probability
- Path with Minimum Effort

---

## Algorithm Selection Guide

### Decision Tree

```
Need shortest path?
├─ Single source?
│  ├─ Non-negative weights? → Dijkstra's O((V+E) log V)
│  └─ Negative weights? → Bellman-Ford O(VE)
└─ All pairs?
   ├─ Small graph (V < 400)? → Floyd-Warshall O(V³)
   └─ Large graph? → Run Dijkstra V times

Need MST?
├─ Sparse graph (E << V²)? → Kruskal's O(E log E)
└─ Dense graph (E ≈ V²)? → Prim's O((V+E) log V)

Special constraints?
├─ Limited steps? → Modified Bellman-Ford
├─ Maximize instead of minimize? → Modified Dijkstra (max-heap)
└─ Track additional metrics? → Modified Dijkstra
```

---

## Implementation Tips

### Tip 1: Priority Queue in Python

```python
import heapq

# Min-heap (default)
min_heap = []
heapq.heappush(min_heap, (distance, node))
dist, node = heapq.heappop(min_heap)

# Max-heap (use negative values)
max_heap = []
heapq.heappush(max_heap, (-probability, node))
neg_prob, node = heapq.heappop(max_heap)
prob = -neg_prob
```

### Tip 2: Graph Representation

```python
# Adjacency list (best for most algorithms)
from collections import defaultdict

graph = defaultdict(list)
for u, v, weight in edges:
    graph[u].append((v, weight))
    # For undirected:
    graph[v].append((u, weight))

# Adjacency matrix (for Floyd-Warshall)
n = num_vertices
adj_matrix = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    adj_matrix[i][i] = 0
for u, v, weight in edges:
    adj_matrix[u][v] = weight
```

### Tip 3: Path Reconstruction

```python
def dijkstra_with_path(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parent = {node: None for node in graph}
    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        if node == end:
            break

        if curr_dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = node  # Track parent
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()

    return distances[end], path
```

### Tip 4: Handling Disconnected Graphs

```python
# Check if all nodes reachable
def is_connected(distances):
    return all(d != float('inf') for d in distances.values())

# For MST, check number of edges
def is_valid_mst(mst, num_vertices):
    return len(mst) == num_vertices - 1
```

---

## LeetCode Practice Problems

### Dijkstra's Algorithm (15 problems)

**Easy:**
1. [Path with Maximum Probability (1514)](https://leetcode.com/problems/path-with-maximum-probability/) - Modified Dijkstra
2. [The Maze (505)](https://leetcode.com/problems/the-maze/) - BFS/Dijkstra

**Medium:**
3. [Network Delay Time (743)](https://leetcode.com/problems/network-delay-time/) - Classic Dijkstra
4. [Path with Minimum Effort (1631)](https://leetcode.com/problems/path-with-minimum-effort/) - Modified Dijkstra
5. [Cheapest Flights Within K Stops (787)](https://leetcode.com/problems/cheapest-flights-within-k-stops/) - Dijkstra variant
6. [Minimum Cost to Reach Destination in Time (1928)](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/) - Dijkstra with constraints
7. [Reachable Nodes In Subdivided Graph (882)](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/) - Dijkstra
8. [Swim in Rising Water (778)](https://leetcode.com/problems/swim-in-rising-water/) - Binary search + BFS or Dijkstra
9. [Shortest Path to Get All Keys (864)](https://leetcode.com/problems/shortest-path-to-get-all-keys/) - BFS with state
10. [Minimum Obstacle Removal to Reach Corner (2290)](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/) - 0-1 BFS or Dijkstra

**Hard:**
11. [Minimum Cost to Make at Least One Valid Path (1368)](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/) - 0-1 BFS
12. [Shortest Path Visiting All Nodes (847)](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) - BFS with bitmask
13. [Shortest Path in a Grid with Obstacles Elimination (1293)](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) - BFS with state
14. [Minimum Time to Visit All Points (1266)](https://leetcode.com/problems/minimum-time-to-visit-all-points/) - Math/Greedy
15. [Find Shortest Path with K Hops (2093)](https://leetcode.com/problems/find-shortest-path-with-k-hops/) - Dijkstra variant

---

### Bellman-Ford (8 problems)

16. [Cheapest Flights Within K Stops (787)](https://leetcode.com/problems/cheapest-flights-within-k-stops/) - Modified Bellman-Ford
17. [Network Delay Time (743)](https://leetcode.com/problems/network-delay-time/) - Can use Bellman-Ford
18. [Find the City With the Smallest Number of Neighbors (1334)](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) - Floyd-Warshall or Bellman-Ford
19. [Number of Ways to Arrive at Destination (1976)](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) - Bellman-Ford variant
20. [Minimum Weighted Subgraph With Required Paths (2203)](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/) - Multiple source Bellman-Ford
21. [Checking Existence of Edge Length Limited Paths (1697)](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/) - Union-Find + sorting
22. [Second Minimum Time to Reach Destination (2045)](https://leetcode.com/problems/second-minimum-time-to-reach-destination/) - BFS/Dijkstra variant
23. [Minimum Time to Visit Disappearing Nodes (3112)](https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/) - Dijkstra with constraints

---

### Floyd-Warshall (6 problems)

24. [Find the City (1334)](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) - Classic Floyd-Warshall
25. [Network Delay Time (743)](https://leetcode.com/problems/network-delay-time/) - Can use Floyd-Warshall
26. [Evaluate Division (399)](https://leetcode.com/problems/evaluate-division/) - Graph + Floyd-Warshall or DFS
27. [Find Eventual Safe States (802)](https://leetcode.com/problems/find-eventual-safe-states/) - Topological sort or DFS
28. [Course Schedule IV (1462)](https://leetcode.com/problems/course-schedule-iv/) - Floyd-Warshall for reachability
29. [Shortest Path in Binary Matrix (1091)](https://leetcode.com/problems/shortest-path-in-binary-matrix/) - BFS (simpler than Floyd-Warshall)

---

### Minimum Spanning Tree - Kruskal's/Prim's (12 problems)

**Medium:**
30. [Min Cost to Connect All Points (1584)](https://leetcode.com/problems/min-cost-to-connect-all-points/) - Classic MST
31. [Connecting Cities With Minimum Cost (1135)](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) - MST
32. [Find Critical and Pseudo-Critical Edges (1489)](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) - MST variants
33. [Optimize Water Distribution (1168)](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) - MST with virtual node
34. [Redundant Connection (684)](https://leetcode.com/problems/redundant-connection/) - Union-Find
35. [Redundant Connection II (685)](https://leetcode.com/problems/redundant-connection-ii/) - Directed graph cycle
36. [Number of Operations to Make Network Connected (1319)](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) - Union-Find

**Hard:**
37. [Min Cost to Connect All Points (1584)](https://leetcode.com/problems/min-cost-to-connect-all-points/) - MST advanced
38. [Minimum Cost to Reach City (Traveling Salesman variant)](https://leetcode.com/problems/find-the-shortest-superstring/) - Related concepts
39. [Number of Ways to Reconstruct a Tree (1719)](https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/) - Tree construction
40. [Maximum Total Importance of Roads (2285)](https://leetcode.com/problems/maximum-total-importance-of-roads/) - Greedy graph
41. [Minimize Malware Spread (924)](https://leetcode.com/problems/minimize-malware-spread/) - Union-Find + simulation

---

### Union-Find Applications (10 problems)

42. [Number of Provinces (547)](https://leetcode.com/problems/number-of-provinces/) - Basic Union-Find
43. [Accounts Merge (721)](https://leetcode.com/problems/accounts-merge/) - Union-Find with strings
44. [Most Stones Removed (947)](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) - Union-Find
45. [Satisfiability of Equality Equations (990)](https://leetcode.com/problems/satisfiability-of-equality-equations/) - Union-Find
46. [Smallest String With Swaps (1202)](https://leetcode.com/problems/smallest-string-with-swaps/) - Union-Find + sorting
47. [Longest Consecutive Sequence (128)](https://leetcode.com/problems/longest-consecutive-sequence/) - Union-Find or hash
48. [Regions Cut By Slashes (959)](https://leetcode.com/problems/regions-cut-by-slashes/) - Union-Find on grid
49. [Bricks Falling When Hit (803)](https://leetcode.com/problems/bricks-falling-when-hit/) - Reverse Union-Find
50. [Checking Existence of Edge Length Limited Paths (1697)](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/) - Union-Find + sorting
51. [Number of Islands II (305)](https://leetcode.com/problems/number-of-islands-ii/) - Dynamic Union-Find

---

### Mixed/Advanced (5+ problems)

52. [Word Ladder II (126)](https://leetcode.com/problems/word-ladder-ii/) - BFS + backtracking
53. [Bus Routes (815)](https://leetcode.com/problems/bus-routes/) - Graph modeling + BFS
54. [Reconstruct Itinerary (332)](https://leetcode.com/problems/reconstruct-itinerary/) - Eulerian path
55. [Critical Connections (1192)](https://leetcode.com/problems/critical-connections-in-a-network/) - Tarjan's algorithm (bridges)
56. [Minimum Height Trees (310)](https://leetcode.com/problems/minimum-height-trees/) - Topological sort variant
57. [Parallel Courses III (2050)](https://leetcode.com/problems/parallel-courses-iii/) - Topological sort + DP
58. [Shortest Bridge (934)](https://leetcode.com/problems/shortest-bridge/) - DFS + BFS

---

## Practice Strategy

### Week 1-2: Master Dijkstra
- Solve problems 1-15
- Focus on variations (max probability, min effort)
- Practice path reconstruction

### Week 3: Bellman-Ford and Floyd-Warshall
- Solve problems 16-29
- Understand when to use each
- Practice negative weight handling

### Week 4-5: MST Algorithms
- Solve problems 30-41
- Master Union-Find implementation
- Compare Kruskal vs Prim performance

### Week 6: Union-Find Applications
- Solve problems 42-51
- Practice path compression
- Learn union by rank

### Week 7+: Advanced Problems
- Solve problems 52-58
- Combine multiple techniques
- Focus on problem modeling

---

## Summary

**Key Takeaways:**
1. **Choose the right algorithm** based on problem constraints
2. **Implement Union-Find correctly** with optimizations
3. **Handle edge cases**: disconnected graphs, unreachable nodes, negative cycles
4. **Practice modifications**: maximize vs minimize, additional constraints
5. **Master the templates** - they apply to 90% of graph shortest path/MST problems

**Complexity Checklist:**
- Dijkstra: O((V+E) log V) - use for non-negative weights
- Bellman-Ford: O(VE) - use for negative weights or limited steps
- Floyd-Warshall: O(V³) - use for all-pairs, small graphs
- Kruskal: O(E log E) - use for sparse MST
- Prim: O((V+E) log V) - use for dense MST

These algorithms are fundamental to graph problems - master them well!
