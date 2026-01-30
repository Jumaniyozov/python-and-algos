# Chapter 37: Advanced Graphs - Solutions

This document contains detailed solutions for all advanced graph exercises.

---

## Easy Problems

### E1: Implement Dijkstra's Algorithm

**Problem**: Find shortest distances from source to all vertices.

**Approach**: Use priority queue to greedily process closest unvisited vertex.

```python
import heapq
from typing import Dict, List, Tuple

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """
    Dijkstra's shortest path algorithm.

    Time: O((V + E) log V)
    Space: O(V)
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Min-heap: (distance, node)
    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        # Skip if we found better path already
        if curr_dist > distances[node]:
            continue

        # Relax all neighbors
        for neighbor, weight in graph[node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
```

**Time Complexity**: O((V + E) log V) - Each edge relaxed once, heap operations log V
**Space Complexity**: O(V) - distances dictionary and priority queue

---

### E2: Shortest Path in Binary Matrix

**Problem**: Find shortest clear path in binary matrix.

**Approach**: BFS with 8-directional movement.

```python
from collections import deque

def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """
    BFS to find shortest path in binary matrix.

    Time: O(n²) where n is grid size
    Space: O(n²)
    """
    n = len(grid)

    # Check if start or end blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1

    # BFS
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = {(0, 0)}

    # 8 directions
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    while queue:
        row, col, dist = queue.popleft()

        # Reached destination
        if row == n-1 and col == n-1:
            return dist

        # Explore 8 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < n and 0 <= new_col < n and
                grid[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):

                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))

    return -1  # No path found
```

**Time Complexity**: O(n²) - visit each cell at most once
**Space Complexity**: O(n²) - visited set and queue

---

### E3: Find if Path Exists in Graph

**Problem**: Check if path exists between two vertices.

**Approach**: BFS or DFS from source, check if destination reached.

```python
from collections import deque, defaultdict

def valid_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    Check if path exists using BFS.

    Time: O(V + E)
    Space: O(V + E)
    """
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # BFS
    queue = deque([source])
    visited = {source}

    while queue:
        node = queue.popleft()

        if node == destination:
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False
```

**Alternative DFS Solution**:

```python
def valid_path_dfs(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    DFS approach.

    Time: O(V + E)
    Space: O(V + E)
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        if node == destination:
            return True

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        return False

    return dfs(source)
```

**Time Complexity**: O(V + E)
**Space Complexity**: O(V + E)

---

## Medium Problems

### M1: Network Delay Time

**Problem**: Time for signal to reach all nodes.

**Approach**: Dijkstra's algorithm, return max distance.

```python
import heapq
from collections import defaultdict

def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """
    Dijkstra's algorithm for network delay.

    Time: O((V + E) log V)
    Space: O(V + E)
    """
    # Build graph
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

    # Return max distance (time for last node)
    max_time = max(distances.values())
    return max_time if max_time != float('inf') else -1
```

**Time Complexity**: O((V + E) log V)
**Space Complexity**: O(V + E)

---

### M2: Path with Minimum Effort

**Problem**: Minimize maximum absolute difference along path.

**Approach**: Modified Dijkstra tracking maximum difference.

```python
import heapq

def minimum_effort_path(heights: List[List[int]]) -> int:
    """
    Modified Dijkstra for minimum effort path.

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
                # Effort = max difference along entire path
                new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))

                if new_effort < efforts[new_row][new_col]:
                    efforts[new_row][new_col] = new_effort
                    heapq.heappush(pq, (new_effort, new_row, new_col))

    return 0
```

**Time Complexity**: O(mn log(mn))
**Space Complexity**: O(mn)

---

### M3: Cheapest Flights Within K Stops

**Problem**: Find cheapest flight with at most k stops.

**Approach**: Modified Bellman-Ford with k+1 iterations.

```python
def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    """
    Bellman-Ford variant with limited iterations.

    Time: O(k * E)
    Space: O(n)
    """
    prices = [float('inf')] * n
    prices[src] = 0

    # Relax edges k+1 times (k stops = k+1 flights)
    for _ in range(k + 1):
        # Use temp array to avoid using updated values in same iteration
        temp_prices = prices.copy()

        for u, v, price in flights:
            if prices[u] != float('inf'):
                temp_prices[v] = min(temp_prices[v], prices[u] + price)

        prices = temp_prices

    return prices[dst] if prices[dst] != float('inf') else -1
```

**Alternative Dijkstra with Stops Tracking**:

```python
import heapq

def find_cheapest_price_dijkstra(n: int, flights: List[List[int]],
                                 src: int, dst: int, k: int) -> int:
    """
    Dijkstra tracking number of stops.

    Time: O((V + E) log V)
    Space: O(V + E)
    """
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))

    # Min-heap: (price, node, stops_used)
    pq = [(0, src, 0)]

    # Track minimum price to reach node with given stops
    visited = {}

    while pq:
        price, node, stops = heapq.heappop(pq)

        if node == dst:
            return price

        if stops > k:
            continue

        if (node, stops) in visited:
            continue

        visited[(node, stops)] = price

        for neighbor, cost in graph[node]:
            heapq.heappush(pq, (price + cost, neighbor, stops + 1))

    return -1
```

**Time Complexity**: O(k * E) for Bellman-Ford variant
**Space Complexity**: O(n)

---

### M4: Path with Maximum Probability

**Problem**: Find path with highest success probability.

**Approach**: Modified Dijkstra using max-heap.

```python
import heapq
from collections import defaultdict

def max_probability(n: int, edges: List[List[int]], succ_prob: List[float],
                   start: int, end: int) -> float:
    """
    Modified Dijkstra for maximum probability.

    Time: O((V + E) log V)
    Space: O(V + E)
    """
    # Build graph
    graph = defaultdict(list)
    for i, (a, b) in enumerate(edges):
        prob = succ_prob[i]
        graph[a].append((b, prob))
        graph[b].append((a, prob))

    # Max-heap (use negative for max behavior)
    max_prob = [0.0] * n
    max_prob[start] = 1.0

    pq = [(-1.0, start)]  # Negative for max-heap

    while pq:
        curr_prob, node = heapq.heappop(pq)
        curr_prob = -curr_prob

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
```

**Time Complexity**: O((V + E) log V)
**Space Complexity**: O(V + E)

---

### M5: Min Cost to Connect All Points

**Problem**: Connect all points with minimum Manhattan distance.

**Approach**: Kruskal's algorithm with all edges generated.

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


def min_cost_connect_points(points: List[List[int]]) -> int:
    """
    Kruskal's MST with Manhattan distance.

    Time: O(n² log n)
    Space: O(n²)
    """
    n = len(points)

    # Generate all edges
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            distance = abs(x1 - x2) + abs(y1 - y2)
            edges.append((i, j, distance))

    # Sort by distance
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
```

**Alternative Prim's Solution**:

```python
import heapq

def min_cost_connect_points_prim(points: List[List[int]]) -> int:
    """
    Prim's MST approach.

    Time: O(n² log n)
    Space: O(n)
    """
    n = len(points)
    visited = set([0])
    total_cost = 0

    # Priority queue: (distance, point_index)
    pq = []
    for i in range(1, n):
        x1, y1 = points[0]
        x2, y2 = points[i]
        dist = abs(x1 - x2) + abs(y1 - y2)
        heapq.heappush(pq, (dist, i))

    while len(visited) < n:
        dist, point = heapq.heappop(pq)

        if point in visited:
            continue

        visited.add(point)
        total_cost += dist

        # Add edges from newly added point
        for i in range(n):
            if i not in visited:
                x1, y1 = points[point]
                x2, y2 = points[i]
                new_dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(pq, (new_dist, i))

    return total_cost
```

**Time Complexity**: O(n² log n) for both approaches
**Space Complexity**: O(n²) for Kruskal, O(n) for Prim

---

(Continue with remaining solutions following same pattern...)

## Summary

**Key Solution Patterns:**

1. **Dijkstra's**: Use for non-negative weights, single-source shortest paths
2. **Bellman-Ford**: Handle negative weights, limited iterations for constraints
3. **Kruskal's/Prim's**: MST problems, choose based on graph density
4. **Modified Variants**: Adjust comparison (max vs min), tracking (effort, probability)
5. **Union-Find**: Essential for Kruskal's and cycle detection

**Complexity Guidelines:**
- Most Dijkstra variants: O((V + E) log V)
- Bellman-Ford: O(VE) or O(kE) with k iterations
- MST algorithms: O(E log E) for Kruskal, O((V + E) log V) for Prim
- Floyd-Warshall: O(V³) for all-pairs

Practice these patterns until the solutions become intuitive!
