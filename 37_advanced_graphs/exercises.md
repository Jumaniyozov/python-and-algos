# Chapter 37: Advanced Graphs - Exercises

## Instructions

- Try to solve each problem without looking at the solution first
- Start with Easy problems, then progress to Medium and Hard
- For each problem, analyze the time and space complexity
- Consider which algorithm is most appropriate for each problem

Solutions are available in `solutions.md`.

---

## Easy Problems

### E1: Implement Dijkstra's Algorithm

Implement Dijkstra's algorithm to find shortest paths from a source vertex.

```python
def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """
    Find shortest distances from start to all vertices.

    Args:
        graph: Adjacency list {node: [(neighbor, weight), ...]}
        start: Starting vertex

    Returns:
        Dictionary of shortest distances from start

    Example:
        graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
        dijkstra(graph, 0) -> {0: 0, 1: 3, 2: 1, 3: 4}
    """
    pass
```

---

### E2: Shortest Path in Binary Matrix (LeetCode 1091)

Find shortest path from top-left to bottom-right in binary matrix (0 = passable).

```python
def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """
    Find shortest clear path from (0,0) to (n-1,n-1).
    Can move in 8 directions.

    Args:
        grid: Binary matrix (0 = clear, 1 = blocked)

    Returns:
        Length of shortest path, or -1 if no path exists

    Example:
        grid = [[0,1],[1,0]]
        Output: 2
    """
    pass
```

---

### E3: Find if Path Exists in Graph (LeetCode 1971)

Check if a path exists between two vertices in undirected graph.

```python
def valid_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    Check if path exists from source to destination.

    Args:
        n: Number of vertices (0 to n-1)
        edges: Undirected edges [[u, v], ...]
        source: Starting vertex
        destination: Ending vertex

    Returns:
        True if path exists, False otherwise

    Example:
        n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
        Output: True
    """
    pass
```

---

## Medium Problems

### M1: Network Delay Time (LeetCode 743)

Find time for signal to reach all nodes from starting node.

```python
def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """
    Find minimum time for signal to reach all n nodes.

    Args:
        times: List of [u, v, w] (signal takes w time from u to v)
        n: Number of nodes (1 to n)
        k: Starting node

    Returns:
        Time for all nodes to receive signal, or -1 if impossible

    Example:
        times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        Output: 2
    """
    pass
```

---

### M2: Path with Minimum Effort (LeetCode 1631)

Find path with minimum maximum absolute difference between consecutive cells.

```python
def minimum_effort_path(heights: List[List[int]]) -> int:
    """
    Find path from top-left to bottom-right minimizing maximum effort.
    Effort = max absolute difference in heights along path.

    Args:
        heights: 2D grid of heights

    Returns:
        Minimum effort needed

    Example:
        heights = [[1,2,2],[3,8,2],[5,3,5]]
        Output: 2
    """
    pass
```

---

### M3: Cheapest Flights Within K Stops (LeetCode 787)

Find cheapest flight from src to dst with at most k stops.

```python
def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    """
    Find cheapest price with at most k stops.

    Args:
        n: Number of cities
        flights: List of [from, to, price]
        src: Source city
        dst: Destination city
        k: Maximum stops allowed

    Returns:
        Minimum price, or -1 if no valid route

    Example:
        n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
        Output: 200
    """
    pass
```

---

### M4: Path with Maximum Probability (LeetCode 1514)

Find path with highest success probability.

```python
def max_probability(n: int, edges: List[List[int]], succ_prob: List[float],
                   start: int, end: int) -> float:
    """
    Find path with maximum probability from start to end.

    Args:
        n: Number of nodes
        edges: List of [a, b]
        succ_prob: Success probability for each edge
        start: Starting node
        end: Ending node

    Returns:
        Maximum probability (0 to 1)

    Example:
        n = 3, edges = [[0,1],[1,2],[0,2]], succ_prob = [0.5,0.5,0.2]
        Output: 0.25
    """
    pass
```

---

### M5: Min Cost to Connect All Points (LeetCode 1584)

Find minimum cost to connect all points using Manhattan distance.

```python
def min_cost_connect_points(points: List[List[int]]) -> int:
    """
    Connect all points with minimum total Manhattan distance.

    Args:
        points: List of [x, y] coordinates

    Returns:
        Minimum cost to connect all points

    Example:
        points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        Output: 20
    """
    pass
```

---

### M6: Find the City (LeetCode 1334)

Find city with smallest number of reachable cities within distance threshold.

```python
def find_the_city(n: int, edges: List[List[int]], distance_threshold: int) -> int:
    """
    Find city with fewest reachable cities within threshold.

    Args:
        n: Number of cities (0 to n-1)
        edges: List of [from, to, weight]
        distance_threshold: Maximum distance

    Returns:
        City with smallest number of reachable neighbors
        (return largest number if tie)

    Example:
        n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], threshold = 4
        Output: 3
    """
    pass
```

---

### M7: Implement Kruskal's Algorithm

Implement Kruskal's algorithm for minimum spanning tree.

```python
def kruskal_mst(num_vertices: int, edges: List[Tuple[int, int, int]]) -> Tuple[List, int]:
    """
    Find MST using Kruskal's algorithm.

    Args:
        num_vertices: Number of vertices
        edges: List of (u, v, weight) tuples

    Returns:
        Tuple of (MST edges list, total weight)

    Example:
        edges = [(0,1,4),(0,2,4),(1,2,2),(1,3,6),(2,3,8)]
        Output: ([(1,2,2),(0,1,4),(0,2,4),(1,3,6)], 16)
    """
    pass
```

---

### M8: Implement Prim's Algorithm

Implement Prim's algorithm for minimum spanning tree.

```python
def prim_mst(graph: Dict[int, List[Tuple[int, int]]], start: int = 0) -> Tuple[List, int]:
    """
    Find MST using Prim's algorithm.

    Args:
        graph: Adjacency list {node: [(neighbor, weight), ...]}
        start: Starting vertex

    Returns:
        Tuple of (MST edges list, total weight)

    Example:
        graph = {0: [(1,4),(2,4)], 1: [(0,4),(2,2)], 2: [(0,4),(1,2)]}
        Output: ([(1,2,2),(0,1,4)], 6)
    """
    pass
```

---

### M9: Minimum Spanning Tree (Generic)

Find MST of weighted undirected graph.

```python
def minimum_spanning_tree(num_vertices: int, edges: List[List[int]]) -> int:
    """
    Find total weight of minimum spanning tree.

    Args:
        num_vertices: Number of vertices
        edges: List of [u, v, weight]

    Returns:
        Total weight of MST

    Example:
        num_vertices = 4
        edges = [[0,1,10],[0,2,6],[0,3,5],[1,3,15],[2,3,4]]
        Output: 19
    """
    pass
```

---

### M10: Redundant Connection (LeetCode 684)

Find edge that when removed makes tree (detect cycle).

```python
def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    """
    Find edge that creates cycle in graph.

    Args:
        edges: List of [u, v] edges added sequentially

    Returns:
        Last edge that creates a cycle

    Example:
        edges = [[1,2],[1,3],[2,3]]
        Output: [2,3]
    """
    pass
```

---

## Hard Problems

### H1: Swim in Rising Water (LeetCode 778)

Find minimum time to swim from top-left to bottom-right.

```python
def swim_in_water(grid: List[List[int]]) -> int:
    """
    Find minimum time to reach bottom-right from top-left.
    At time t, can be in cells with elevation <= t.

    Args:
        grid: n x n grid with unique elevations 0 to n²-1

    Returns:
        Minimum time needed

    Example:
        grid = [[0,2],[1,3]]
        Output: 3
    """
    pass
```

---

### H2: Optimize Water Distribution (LeetCode 1168)

Minimize cost to supply water to all houses.

```python
def min_cost_to_supply_water(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    """
    Minimize cost to supply water to all houses.
    Can build well in house i (cost wells[i]) or connect pipes.

    Args:
        n: Number of houses (1 to n)
        wells: Cost to build well in each house
        pipes: List of [house1, house2, cost]

    Returns:
        Minimum cost to supply all houses

    Example:
        n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
        Output: 3
    """
    pass
```

---

### H3: Critical Connections (LeetCode 1192)

Find all critical connections (bridges) in network.

```python
def critical_connections(n: int, connections: List[List[int]]) -> List[List[int]]:
    """
    Find all critical connections (edges whose removal disconnects graph).

    Args:
        n: Number of servers (0 to n-1)
        connections: List of [a, b] connections

    Returns:
        List of critical connections

    Example:
        n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
        Output: [[1,3]]
    """
    pass
```

---

### H4: Bellman-Ford with Negative Cycle Detection

Implement Bellman-Ford algorithm with negative cycle detection.

```python
def bellman_ford(num_vertices: int, edges: List[Tuple[int, int, int]],
                start: int) -> Tuple[List[float], bool]:
    """
    Bellman-Ford algorithm with negative cycle detection.

    Args:
        num_vertices: Number of vertices
        edges: List of (u, v, weight) tuples
        start: Starting vertex

    Returns:
        Tuple of (distances list, has_negative_cycle bool)

    Example:
        edges = [(0,1,1),(1,2,3),(2,0,-5)]
        Output: ([inf, inf, inf], True)  # Has negative cycle
    """
    pass
```

---

### H5: Minimize Malware Spread (LeetCode 924)

Choose node to remove to minimize malware spread.

```python
def min_malware_spread(graph: List[List[int]], initial: List[int]) -> int:
    """
    Choose which initially infected node to remove to minimize final infections.

    Args:
        graph: Adjacency matrix (graph[i][j] = 1 if connected)
        initial: List of initially infected nodes

    Returns:
        Node to remove (smallest index if tie)

    Example:
        graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
        Output: 0
    """
    pass
```

---

### H6: Floyd-Warshall Implementation

Implement Floyd-Warshall for all-pairs shortest paths.

```python
def floyd_warshall(num_vertices: int, edges: List[Tuple[int, int, int]]) -> List[List[float]]:
    """
    Floyd-Warshall all-pairs shortest path algorithm.

    Args:
        num_vertices: Number of vertices
        edges: List of (u, v, weight) tuples

    Returns:
        2D list of shortest distances between all pairs

    Example:
        edges = [(0,1,3),(1,2,1),(0,2,7)]
        Output: [[0,3,4],[inf,0,1],[inf,inf,0]]
    """
    pass
```

---

### H7: Shortest Path Visiting All Nodes (LeetCode 847)

Find shortest path that visits all nodes.

```python
def shortest_path_length(graph: List[List[int]]) -> int:
    """
    Find length of shortest path visiting all nodes (can revisit).

    Args:
        graph: Adjacency list (undirected)

    Returns:
        Length of shortest path visiting all nodes

    Example:
        graph = [[1,2,3],[0],[0],[0]]
        Output: 4
    """
    pass
```

---

## Bonus Challenges

### B1: Dijkstra with Path Reconstruction

Extend Dijkstra to return both distances and actual paths.

```python
def dijkstra_with_path(graph: Dict[int, List[Tuple[int, int]]],
                       start: int, end: int) -> Tuple[int, List[int]]:
    """
    Find shortest path and distance from start to end.

    Returns:
        Tuple of (distance, path_list)
    """
    pass
```

---

### B2: A* Algorithm

Implement A* pathfinding algorithm with heuristic.

```python
def a_star(grid: List[List[int]], start: Tuple[int, int],
          end: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    A* pathfinding from start to end using Manhattan distance heuristic.

    Returns:
        List of coordinates representing shortest path
    """
    pass
```

---

### B3: Parallel Edges and Multiple MSTs

Handle graph with parallel edges and find if multiple MSTs exist.

```python
def count_msts(num_vertices: int, edges: List[Tuple[int, int, int]]) -> int:
    """
    Count number of distinct minimum spanning trees.

    Returns:
        Number of different MSTs with same minimum weight
    """
    pass
```

---

## Summary

**Algorithm Selection Guide:**

| Problem Type | Algorithm | Time Complexity |
|-------------|-----------|----------------|
| Single-source, non-negative | Dijkstra's | O((V+E) log V) |
| Single-source, negative weights | Bellman-Ford | O(VE) |
| All-pairs shortest paths | Floyd-Warshall | O(V³) |
| MST sparse graph | Kruskal's | O(E log E) |
| MST dense graph | Prim's | O((V+E) log V) |

**Practice Strategy:**
1. Master basic implementations first (E1, M7, M8)
2. Learn variations (M1-M6)
3. Tackle complex applications (H1-H7)
4. Understand when to use which algorithm

Good luck with the exercises!
