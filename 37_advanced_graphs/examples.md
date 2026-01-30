# Chapter 37: Advanced Graphs - Examples

## Table of Contents
1. [Dijkstra's Algorithm Examples](#dijkstras-algorithm-examples)
2. [Bellman-Ford Examples](#bellman-ford-examples)
3. [Floyd-Warshall Examples](#floyd-warshall-examples)
4. [Kruskal's Algorithm Examples](#kruskals-algorithm-examples)
5. [Prim's Algorithm Examples](#prims-algorithm-examples)
6. [Shortest Path Variations](#shortest-path-variations)

---

## Dijkstra's Algorithm Examples

### Example 1: Basic Dijkstra Implementation

```python
import heapq
from collections import defaultdict

def dijkstra_basic(graph, start):
    """
    Basic Dijkstra's algorithm for shortest paths.

    Args:
        graph: Dict of adjacency lists {node: [(neighbor, weight), ...]}
        start: Starting vertex

    Returns:
        Dict of shortest distances from start

    Time: O((V + E) log V)
    Space: O(V)
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Min-heap: (distance, node)
    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        # Skip if we've found a better path already
        if curr_dist > distances[node]:
            continue

        # Check all neighbors
        for neighbor, weight in graph[node]:
            distance = curr_dist + weight

            # If we found a shorter path, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Example usage:
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8), ('E', 10)],
    'D': [('E', 2)],
    'E': []
}

result = dijkstra_basic(graph, 'A')
print(result)
# Output: {'A': 0, 'B': 4, 'C': 2, 'D': 9, 'E': 11}
```

---

### Example 2: Dijkstra with Path Reconstruction

```python
import heapq

def dijkstra_with_path(graph, start, end):
    """
    Dijkstra's algorithm that also reconstructs the shortest path.

    Returns:
        Tuple: (shortest_distance, path_list)

    Time: O((V + E) log V)
    Space: O(V)
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Track parent of each node for path reconstruction
    parent = {node: None for node in graph}

    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        # Early termination if we reached the destination
        if node == end:
            break

        if curr_dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = curr_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = node
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct path
    path = []
    if distances[end] != float('inf'):
        current = end
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()

    return distances[end], path


# Example:
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8), ('E', 10)],
    'D': [('E', 2)],
    'E': []
}

distance, path = dijkstra_with_path(graph, 'A', 'E')
print(f"Distance: {distance}")  # 11
print(f"Path: {' -> '.join(path)}")  # A -> C -> E
```

---

### Example 3: Network Delay Time (LeetCode 743)

```python
import heapq
from collections import defaultdict

def network_delay_time(times, n, k):
    """
    Find minimum time for signal to reach all nodes.

    Args:
        times: List of [u, v, w] representing edge from u to v with time w
        n: Number of nodes (labeled 1 to n)
        k: Starting node

    Returns:
        Minimum time for all nodes to receive signal, or -1 if impossible

    Example:
        times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        Output: 2
        Explanation: Signal reaches 2(0), 1(1), 3(1), 4(2)

    Time: O((V + E) log V)
    Space: O(V + E)
    """
    # Build adjacency list
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    # Dijkstra's
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[k] = 0

    pq = [(0, k)]

    while pq:
        curr_time, node = heapq.heappop(pq)

        if curr_time > distances[node]:
            continue

        for neighbor, time in graph[node]:
            new_time = curr_time + time
            if new_time < distances[neighbor]:
                distances[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))

    # Find maximum distance (time for last node to receive signal)
    max_time = max(distances.values())

    # If any node unreachable, return -1
    return max_time if max_time != float('inf') else -1


# Test:
times = [[2,1,1],[2,3,1],[3,4,1]]
print(network_delay_time(times, 4, 2))  # 2
```

---

## Bellman-Ford Examples

### Example 4: Basic Bellman-Ford

```python
def bellman_ford(num_vertices, edges, start):
    """
    Bellman-Ford algorithm for shortest paths with negative weights.

    Args:
        num_vertices: Number of vertices (0 to num_vertices-1)
        edges: List of tuples [(u, v, weight), ...]
        start: Starting vertex

    Returns:
        Tuple: (distances dict, has_negative_cycle bool)

    Time: O(VE)
    Space: O(V)
    """
    # Initialize distances
    distances = [float('inf')] * num_vertices
    distances[start] = 0

    # Relax all edges V-1 times
    for _ in range(num_vertices - 1):
        updated = False
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                updated = True

        # Early termination if no updates
        if not updated:
            break

    # Check for negative cycles
    has_negative_cycle = False
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            has_negative_cycle = True
            break

    return distances, has_negative_cycle


# Example with negative weight:
edges = [
    (0, 1, 4),
    (0, 2, 2),
    (1, 2, -3),  # Negative weight
    (2, 3, 2),
    (1, 3, 5)
]

distances, has_cycle = bellman_ford(4, edges, 0)
print(f"Distances: {distances}")  # [0, 4, 1, 3]
print(f"Has negative cycle: {has_cycle}")  # False
```

---

### Example 5: Cheapest Flights Within K Stops (LeetCode 787)

```python
def find_cheapest_price(n, flights, src, dst, k):
    """
    Find cheapest price from src to dst with at most k stops.

    Uses modified Bellman-Ford (only k+1 iterations).

    Args:
        n: Number of cities
        flights: List of [from, to, price]
        src: Source city
        dst: Destination city
        k: Maximum number of stops

    Returns:
        Minimum price, or -1 if no path exists

    Time: O(k * E)
    Space: O(n)
    """
    # Initialize prices
    prices = [float('inf')] * n
    prices[src] = 0

    # Relax edges k+1 times (k stops = k+1 flights)
    for _ in range(k + 1):
        # Use temporary array to avoid using updated values in same iteration
        temp_prices = prices.copy()

        for u, v, price in flights:
            if prices[u] != float('inf'):
                temp_prices[v] = min(temp_prices[v], prices[u] + price)

        prices = temp_prices

    return prices[dst] if prices[dst] != float('inf') else -1


# Example:
flights = [[0,1,100],[1,2,100],[0,2,500]]
print(find_cheapest_price(3, flights, 0, 2, 1))  # 200 (0->1->2)
print(find_cheapest_price(3, flights, 0, 2, 0))  # 500 (0->2 direct)
```

---

## Floyd-Warshall Examples

### Example 6: Basic Floyd-Warshall

```python
def floyd_warshall(num_vertices, edges):
    """
    Floyd-Warshall all-pairs shortest path algorithm.

    Args:
        num_vertices: Number of vertices
        edges: List of tuples [(u, v, weight), ...]

    Returns:
        2D list of shortest distances between all pairs

    Time: O(V³)
    Space: O(V²)
    """
    INF = float('inf')

    # Initialize distance matrix
    dist = [[INF] * num_vertices for _ in range(num_vertices)]

    # Distance from vertex to itself is 0
    for i in range(num_vertices):
        dist[i][i] = 0

    # Add edges
    for u, v, weight in edges:
        dist[u][v] = weight

    # Try each vertex as intermediate
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Is path i->k->j better than direct i->j?
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


# Example:
edges = [
    (0, 1, 3),
    (0, 2, 8),
    (0, 3, -4),
    (1, 3, 1),
    (1, 4, 7),
    (2, 1, 4),
    (3, 2, 2),
    (3, 4, 6),
    (4, 0, 2)
]

distances = floyd_warshall(5, edges)

# Print distance from 0 to all vertices
print("Distances from vertex 0:")
for i, dist in enumerate(distances[0]):
    print(f"  to {i}: {dist}")
```

---

### Example 7: Find the City (LeetCode 1334)

```python
def find_the_city(n, edges, distance_threshold):
    """
    Find city with smallest number of reachable cities within distance threshold.

    Uses Floyd-Warshall to compute all-pairs shortest paths.

    Args:
        n: Number of cities (0 to n-1)
        edges: List of [from, to, weight]
        distance_threshold: Maximum distance

    Returns:
        City number with fewest reachable cities (largest number if tie)

    Time: O(n³)
    Space: O(n²)
    """
    INF = float('inf')

    # Initialize distance matrix
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    # Add edges (undirected)
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w

    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Count reachable cities for each city
    min_reachable = n
    result_city = 0

    for i in range(n):
        reachable = sum(1 for j in range(n) if i != j and dist[i][j] <= distance_threshold)

        if reachable <= min_reachable:
            min_reachable = reachable
            result_city = i  # Take largest city number in case of tie

    return result_city


# Example:
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
print(find_the_city(4, edges, 4))  # 3
```

---

## Kruskal's Algorithm Examples

### Example 8: Basic Kruskal Implementation

```python
class UnionFind:
    """Union-Find data structure with path compression and union by rank."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """Find with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union by rank. Returns True if union performed, False if already connected."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same component

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
    Kruskal's algorithm for Minimum Spanning Tree.

    Args:
        num_vertices: Number of vertices (0 to num_vertices-1)
        edges: List of tuples [(u, v, weight), ...]

    Returns:
        Tuple: (MST edge list, total weight)

    Time: O(E log E)
    Space: O(V)
    """
    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])

    uf = UnionFind(num_vertices)
    mst = []
    total_weight = 0

    for u, v, weight in sorted_edges:
        # If adding edge doesn't create cycle
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

            # MST complete when we have V-1 edges
            if len(mst) == num_vertices - 1:
                break

    return mst, total_weight


# Example:
edges = [
    (0, 1, 4),
    (0, 2, 4),
    (1, 2, 2),
    (1, 3, 6),
    (2, 3, 8),
    (3, 4, 9),
    (2, 4, 11)
]

mst, weight = kruskal(5, edges)
print(f"MST edges: {mst}")
print(f"Total weight: {weight}")  # 21
```

---

### Example 9: Min Cost to Connect All Points (LeetCode 1584)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


def min_cost_connect_points(points):
    """
    Find minimum cost to connect all points (Manhattan distance).

    Uses Kruskal's algorithm.

    Args:
        points: List of [x, y] coordinates

    Returns:
        Minimum cost to connect all points

    Time: O(n² log n) where n is number of points
    Space: O(n²)
    """
    n = len(points)

    # Generate all edges with Manhattan distance
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            distance = abs(x1 - x2) + abs(y1 - y2)
            edges.append((i, j, distance))

    # Sort edges by distance
    edges.sort(key=lambda x: x[2])

    # Kruskal's algorithm
    uf = UnionFind(n)
    total_cost = 0
    edges_added = 0

    for u, v, cost in edges:
        if uf.union(u, v):
            total_cost += cost
            edges_added += 1
            if edges_added == n - 1:
                break

    return total_cost


# Example:
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(min_cost_connect_points(points))  # 20
```

---

## Prim's Algorithm Examples

### Example 10: Basic Prim Implementation

```python
import heapq
from collections import defaultdict

def prim(graph, start=0):
    """
    Prim's algorithm for Minimum Spanning Tree.

    Args:
        graph: Dict of adjacency lists {node: [(neighbor, weight), ...]}
        start: Starting vertex (default 0)

    Returns:
        Tuple: (MST edge list, total weight)

    Time: O((V + E) log V)
    Space: O(V)
    """
    visited = set()
    mst = []
    total_weight = 0

    # Priority queue: (weight, from_node, to_node)
    # Start with dummy edge to starting vertex
    pq = [(0, None, start)]

    while pq:
        weight, from_node, to_node = heapq.heappop(pq)

        # Skip if already in MST
        if to_node in visited:
            continue

        # Add to MST
        visited.add(to_node)
        if from_node is not None:  # Skip dummy edge
            mst.append((from_node, to_node, weight))
            total_weight += weight

        # Add all edges from newly added vertex
        for neighbor, edge_weight in graph[to_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, to_node, neighbor))

    return mst, total_weight


# Example:
graph = {
    0: [(1, 4), (2, 4)],
    1: [(0, 4), (2, 2), (3, 6)],
    2: [(0, 4), (1, 2), (3, 8), (4, 11)],
    3: [(1, 6), (2, 8), (4, 9)],
    4: [(2, 11), (3, 9)]
}

mst, weight = prim(graph, 0)
print(f"MST edges: {mst}")
print(f"Total weight: {weight}")  # 21
```

---

## Shortest Path Variations

### Example 11: Path with Maximum Probability (LeetCode 1514)

```python
import heapq
from collections import defaultdict

def max_probability(n, edges, succ_prob, start, end):
    """
    Find path with maximum probability of success.

    Modified Dijkstra using max-heap.

    Args:
        n: Number of nodes
        edges: List of [a, b] edges
        succ_prob: List of success probabilities for each edge
        start: Starting node
        end: Ending node

    Returns:
        Maximum probability from start to end

    Time: O((V + E) log V)
    Space: O(V + E)
    """
    # Build graph
    graph = defaultdict(list)
    for i, (a, b) in enumerate(edges):
        prob = succ_prob[i]
        graph[a].append((b, prob))
        graph[b].append((a, prob))

    # Max-heap (use negative probabilities for max-heap behavior)
    max_prob = [0.0] * n
    max_prob[start] = 1.0

    pq = [(-1.0, start)]  # Negative for max-heap

    while pq:
        curr_prob, node = heapq.heappop(pq)
        curr_prob = -curr_prob  # Convert back to positive

        if node == end:
            return curr_prob

        if curr_prob < max_prob[node]:
            continue

        for neighbor, edge_prob in graph[node]:
            new_prob = curr_prob * edge_prob
            if new_prob > max_prob[neighbor]:
                max_prob[neighbor] = new_prob
                heapq.heappush(pq, (-new_prob, neighbor))

    return 0.0


# Example:
n = 3
edges = [[0,1],[1,2],[0,2]]
succ_prob = [0.5,0.5,0.2]
print(max_probability(n, edges, succ_prob, 0, 2))  # 0.25 (0->1->2)
```

---

### Example 12: Path with Minimum Effort (LeetCode 1631)

```python
import heapq

def minimum_effort_path(heights):
    """
    Find path with minimum maximum absolute difference.

    Modified Dijkstra tracking maximum difference along path.

    Args:
        heights: 2D grid of heights

    Returns:
        Minimum effort (max absolute difference) from top-left to bottom-right

    Time: O(mn log(mn))
    Space: O(mn)
    """
    rows, cols = len(heights), len(heights[0])

    # Track minimum effort to reach each cell
    efforts = [[float('inf')] * cols for _ in range(rows)]
    efforts[0][0] = 0

    # Min-heap: (effort, row, col)
    pq = [(0, 0, 0)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while pq:
        effort, row, col = heapq.heappop(pq)

        # Reached destination
        if row == rows - 1 and col == cols - 1:
            return effort

        if effort > efforts[row][col]:
            continue

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols:
                # Effort is max difference along path
                new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))

                if new_effort < efforts[new_row][new_col]:
                    efforts[new_row][new_col] = new_effort
                    heapq.heappush(pq, (new_effort, new_row, new_col))

    return 0


# Example:
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(minimum_effort_path(heights))  # 2
```

---

## Summary

These examples demonstrate:

1. **Dijkstra's Algorithm**: Basic implementation, path reconstruction, network problems
2. **Bellman-Ford**: Handling negative weights, limited iterations variant
3. **Floyd-Warshall**: All-pairs shortest paths, finding special cities
4. **Kruskal's MST**: Union-Find based, connecting points
5. **Prim's MST**: Priority queue based, vertex-centric approach
6. **Variations**: Maximum probability, minimum effort, creative applications

**Key Techniques**:
- Priority queue for greedy selection
- Union-Find for cycle detection
- Path reconstruction with parent tracking
- Modified algorithms for optimization variants
- Early termination for efficiency

Practice these implementations until you can code them from memory!
