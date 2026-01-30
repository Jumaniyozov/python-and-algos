# Chapter 36: Graphs - Examples

## Table of Contents
1. [Graph Representation](#graph-representation)
2. [Depth-First Search (DFS)](#depth-first-search-dfs)
3. [Breadth-First Search (BFS)](#breadth-first-search-bfs)
4. [Union Find](#union-find)
5. [Topological Sort](#topological-sort)
6. [Cycle Detection](#cycle-detection)
7. [Connected Components](#connected-components)
8. [Bipartite Graph Checking](#bipartite-graph-checking)

---

## Graph Representation

### Example 1: Building Adjacency List from Edges

```python
def build_graph(n, edges, directed=False):
    """
    Build adjacency list from edge list.

    Time: O(E) where E is number of edges
    Space: O(V + E) where V is number of vertices

    Args:
        n: Number of vertices (0 to n-1)
        edges: List of [u, v] edges
        directed: True if directed graph

    Returns:
        Dictionary representing adjacency list
    """
    # Initialize empty adjacency list
    graph = {i: [] for i in range(n)}

    # Add edges
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)  # Add reverse edge for undirected

    return graph


# Example usage:
n = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]

# Undirected graph
graph_undirected = build_graph(n, edges, directed=False)
print(graph_undirected)
# {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3]}

# Directed graph
graph_directed = build_graph(n, edges, directed=True)
print(graph_directed)
# {0: [1, 2], 1: [3], 2: [3], 3: [4], 4: []}
```

### Example 2: Building Weighted Graph

```python
def build_weighted_graph(n, edges, directed=False):
    """
    Build adjacency list with edge weights.

    Args:
        n: Number of vertices
        edges: List of [u, v, weight] edges
        directed: True if directed

    Returns:
        Dictionary with {vertex: [(neighbor, weight), ...]}
    """
    graph = {i: [] for i in range(n)}

    for u, v, weight in edges:
        graph[u].append((v, weight))
        if not directed:
            graph[v].append((u, weight))

    return graph


# Example usage:
edges_weighted = [[0, 1, 5], [0, 2, 3], [1, 3, 2], [2, 3, 7]]
graph_w = build_weighted_graph(4, edges_weighted)
print(graph_w)
# {0: [(1, 5), (2, 3)], 1: [(0, 5), (3, 2)], 2: [(0, 3), (3, 7)], 3: [(1, 2), (2, 7)]}
```

---

## Depth-First Search (DFS)

### Example 3: DFS Recursive

```python
def dfs_recursive(graph, start, visited=None):
    """
    Recursive DFS traversal.

    Time: O(V + E)
    Space: O(V) for visited set + O(V) for recursion stack

    Args:
        graph: Adjacency list
        start: Starting vertex
        visited: Set of visited vertices (for external tracking)

    Returns:
        List of visited vertices in DFS order
    """
    if visited is None:
        visited = set()

    result = []

    # Base case: already visited
    if start in visited:
        return result

    # Mark as visited and add to result
    visited.add(start)
    result.append(start)

    # Recursively visit neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

print(dfs_recursive(graph, 0))
# Output: [0, 1, 3, 4, 2, 5] (order may vary)
```

### Example 4: DFS Iterative (Using Stack)

```python
def dfs_iterative(graph, start):
    """
    Iterative DFS using explicit stack.

    Time: O(V + E)
    Space: O(V) for visited set and stack

    Args:
        graph: Adjacency list
        start: Starting vertex

    Returns:
        List of visited vertices in DFS order
    """
    visited = set()
    stack = [start]
    result = []

    while stack:
        # Pop from stack
        node = stack.pop()

        # Skip if already visited
        if node in visited:
            continue

        # Mark as visited
        visited.add(node)
        result.append(node)

        # Add unvisited neighbors to stack
        # Reverse to maintain left-to-right order (optional)
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return result


# Example usage:
print(dfs_iterative(graph, 0))
# Output: [0, 1, 3, 4, 2, 5] (order may vary based on neighbor order)
```

### Example 5: DFS for Path Finding

```python
def find_path_dfs(graph, start, target):
    """
    Find path from start to target using DFS.

    Time: O(V + E)
    Space: O(V)

    Args:
        graph: Adjacency list
        start: Start vertex
        target: Target vertex

    Returns:
        Path as list if found, None otherwise
    """
    def dfs(node, path, visited):
        # Found target
        if node == target:
            return path + [node]

        # Mark as visited
        visited.add(node)

        # Try all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                result = dfs(neighbor, path + [node], visited)
                if result:
                    return result

        return None

    return dfs(start, [], set())


# Example usage:
path = find_path_dfs(graph, 0, 5)
print(path)
# Output: [0, 2, 5] (one possible path)
```

---

## Breadth-First Search (BFS)

### Example 6: BFS Standard

```python
from collections import deque

def bfs(graph, start):
    """
    Standard BFS traversal.

    Time: O(V + E)
    Space: O(V) for visited set and queue

    Args:
        graph: Adjacency list
        start: Starting vertex

    Returns:
        List of visited vertices in BFS order
    """
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        # Dequeue from front
        node = queue.popleft()
        result.append(node)

        # Enqueue unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# Example usage:
print(bfs(graph, 0))
# Output: [0, 1, 2, 3, 4, 5] (level-by-level order)
```

### Example 7: BFS with Levels

```python
def bfs_with_levels(graph, start):
    """
    BFS that tracks level/distance from start.

    Time: O(V + E)
    Space: O(V)

    Args:
        graph: Adjacency list
        start: Starting vertex

    Returns:
        Dictionary {vertex: level}
    """
    levels = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        current_level = levels[node]

        for neighbor in graph[node]:
            if neighbor not in levels:
                levels[neighbor] = current_level + 1
                queue.append(neighbor)

    return levels


# Example usage:
levels = bfs_with_levels(graph, 0)
print(levels)
# Output: {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2}
```

### Example 8: BFS Shortest Path (Unweighted)

```python
def shortest_path_bfs(graph, start, target):
    """
    Find shortest path in unweighted graph.

    Time: O(V + E)
    Space: O(V)

    Args:
        graph: Adjacency list
        start: Start vertex
        target: Target vertex

    Returns:
        Shortest path as list, None if no path
    """
    if start == target:
        return [start]

    visited = {start}
    queue = deque([(start, [start])])  # (node, path)

    while queue:
        node, path = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = path + [neighbor]

                if neighbor == target:
                    return new_path

                visited.add(neighbor)
                queue.append((neighbor, new_path))

    return None  # No path found


# Example usage:
path = shortest_path_bfs(graph, 0, 5)
print(path)
# Output: [0, 2, 5]
```

---

## Union Find

### Example 9: Union Find with Path Compression

```python
class UnionFind:
    """
    Union Find (Disjoint Set) with path compression and union by rank.

    Operations:
    - find: O(α(n)) amortized, nearly O(1)
    - union: O(α(n)) amortized, nearly O(1)

    where α(n) is the inverse Ackermann function
    """

    def __init__(self, n):
        """
        Initialize Union Find with n elements.

        Args:
            n: Number of elements (0 to n-1)
        """
        self.parent = list(range(n))  # Each element is its own parent initially
        self.rank = [0] * n  # Rank for union by rank optimization
        self.count = n  # Number of connected components

    def find(self, x):
        """
        Find root of element x with path compression.

        Args:
            x: Element to find root of

        Returns:
            Root of x's set
        """
        if self.parent[x] != x:
            # Path compression: make x point directly to root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Union sets containing x and y.

        Args:
            x: First element
            y: Second element

        Returns:
            True if union performed, False if already in same set
        """
        root_x = self.find(x)
        root_y = self.find(y)

        # Already in same set
        if root_x == root_y:
            return False

        # Union by rank: attach smaller tree under larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.count -= 1
        return True

    def connected(self, x, y):
        """Check if x and y are in same set."""
        return self.find(x) == self.find(y)

    def get_count(self):
        """Get number of connected components."""
        return self.count


# Example usage:
uf = UnionFind(6)
print(f"Initial components: {uf.get_count()}")  # 6

uf.union(0, 1)
uf.union(1, 2)
print(f"After unions (0-1, 1-2): {uf.get_count()}")  # 4

uf.union(3, 4)
print(f"After union (3-4): {uf.get_count()}")  # 3

print(f"Are 0 and 2 connected? {uf.connected(0, 2)}")  # True
print(f"Are 0 and 3 connected? {uf.connected(0, 3)}")  # False
```

---

## Topological Sort

### Example 10: Topological Sort - Kahn's Algorithm (BFS)

```python
from collections import deque, defaultdict

def topological_sort_kahn(n, edges):
    """
    Topological sort using Kahn's algorithm (BFS-based).

    Time: O(V + E)
    Space: O(V + E)

    Args:
        n: Number of vertices
        edges: List of directed edges [u, v]

    Returns:
        Topological order as list, empty list if cycle detected
    """
    # Build graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Add all nodes with in-degree 0 to queue
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # Reduce in-degree of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all nodes processed, valid topological order
    if len(result) == n:
        return result
    else:
        return []  # Cycle detected


# Example usage: Course Schedule
n = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
# Course 3 depends on 1 and 2, which depend on 0

order = topological_sort_kahn(n, prerequisites)
print(order)
# Output: [0, 1, 2, 3] or [0, 2, 1, 3] (both valid)
```

### Example 11: Topological Sort - DFS Based

```python
def topological_sort_dfs(n, edges):
    """
    Topological sort using DFS.

    Time: O(V + E)
    Space: O(V)

    Args:
        n: Number of vertices
        edges: List of directed edges [u, v]

    Returns:
        Topological order as list
    """
    # Build graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        # Add to stack after visiting all neighbors (post-order)
        stack.append(node)

    # Run DFS from all unvisited nodes
    for i in range(n):
        if i not in visited:
            dfs(i)

    # Reverse stack to get topological order
    return stack[::-1]


# Example usage:
order_dfs = topological_sort_dfs(n, prerequisites)
print(order_dfs)
# Output: [0, 1, 2, 3] or [0, 2, 1, 3]
```

---

## Cycle Detection

### Example 12: Cycle Detection in Undirected Graph (DFS)

```python
def has_cycle_undirected(n, edges):
    """
    Detect cycle in undirected graph using DFS.

    Time: O(V + E)
    Space: O(V)

    Args:
        n: Number of vertices
        edges: List of edges [u, v]

    Returns:
        True if cycle exists, False otherwise
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                # Visited neighbor that's not parent = cycle
                return True

        return False

    # Check all components
    for i in range(n):
        if i not in visited:
            if dfs(i, -1):
                return True

    return False


# Example usage:
# Graph with cycle: 0-1-2-0
edges_cycle = [[0, 1], [1, 2], [2, 0]]
print(has_cycle_undirected(3, edges_cycle))  # True

# Graph without cycle: 0-1-2
edges_no_cycle = [[0, 1], [1, 2]]
print(has_cycle_undirected(3, edges_no_cycle))  # False
```

### Example 13: Cycle Detection in Directed Graph (DFS - 3 Colors)

```python
def has_cycle_directed(n, edges):
    """
    Detect cycle in directed graph using DFS with 3 colors.

    Colors:
    - White (0): Unvisited
    - Gray (1): In current DFS path (being processed)
    - Black (2): Completely processed

    Time: O(V + E)
    Space: O(V)

    Args:
        n: Number of vertices
        edges: List of directed edges [u, v]

    Returns:
        True if cycle exists, False otherwise
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    # 0: white, 1: gray, 2: black
    color = [0] * n

    def dfs(node):
        if color[node] == 1:
            # Gray = back edge to ancestor = cycle
            return True
        if color[node] == 2:
            # Black = already processed
            return False

        # Mark as gray (in current path)
        color[node] = 1

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        # Mark as black (completely processed)
        color[node] = 2
        return False

    # Check all nodes
    for i in range(n):
        if color[i] == 0:
            if dfs(i):
                return True

    return False


# Example usage:
# Directed graph with cycle: 0→1→2→0
directed_cycle = [[0, 1], [1, 2], [2, 0]]
print(has_cycle_directed(3, directed_cycle))  # True

# Directed graph without cycle (DAG): 0→1→2
directed_no_cycle = [[0, 1], [1, 2]]
print(has_cycle_directed(3, directed_no_cycle))  # False
```

### Example 14: Cycle Detection Using Union Find

```python
def has_cycle_union_find(n, edges):
    """
    Detect cycle in undirected graph using Union Find.

    Time: O(E × α(n)) ≈ O(E)
    Space: O(V)

    Args:
        n: Number of vertices
        edges: List of edges [u, v]

    Returns:
        True if cycle exists, False otherwise
    """
    uf = UnionFind(n)

    for u, v in edges:
        # If u and v already in same set, adding edge creates cycle
        if not uf.union(u, v):
            return True

    return False


# Example usage:
print(has_cycle_union_find(3, edges_cycle))  # True
print(has_cycle_union_find(3, edges_no_cycle))  # False
```

---

## Connected Components

### Example 15: Count Connected Components (DFS)

```python
def count_components_dfs(n, edges):
    """
    Count connected components using DFS.

    Time: O(V + E)
    Space: O(V)

    Args:
        n: Number of vertices
        edges: List of edges [u, v]

    Returns:
        Number of connected components
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    components = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            components += 1

    return components


# Example usage:
# Graph: 0-1-2  3-4  5 (3 components)
edges_comp = [[0, 1], [1, 2], [3, 4]]
print(count_components_dfs(6, edges_comp))  # 3
```

### Example 16: Count Connected Components (Union Find)

```python
def count_components_union_find(n, edges):
    """
    Count connected components using Union Find.

    Time: O(E × α(n)) ≈ O(E)
    Space: O(V)

    Args:
        n: Number of vertices
        edges: List of edges [u, v]

    Returns:
        Number of connected components
    """
    uf = UnionFind(n)

    for u, v in edges:
        uf.union(u, v)

    return uf.get_count()


# Example usage:
print(count_components_union_find(6, edges_comp))  # 3
```

---

## Bipartite Graph Checking

### Example 17: Check Bipartite Graph (BFS - Coloring)

```python
def is_bipartite_bfs(n, edges):
    """
    Check if graph is bipartite using BFS coloring.

    A graph is bipartite if it can be colored with 2 colors
    such that no adjacent vertices have the same color.

    Time: O(V + E)
    Space: O(V)

    Args:
        n: Number of vertices
        edges: List of edges [u, v]

    Returns:
        True if bipartite, False otherwise
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # -1: uncolored, 0: color A, 1: color B
    color = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue

        # BFS to color component
        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    # Color with opposite color
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    # Same color = not bipartite
                    return False

    return True


# Example usage:
# Bipartite: 0-1-2-3 (can color alternately)
bipartite_edges = [[0, 1], [1, 2], [2, 3]]
print(is_bipartite_bfs(4, bipartite_edges))  # True

# Not bipartite: 0-1-2-0 (triangle)
not_bipartite = [[0, 1], [1, 2], [2, 0]]
print(is_bipartite_bfs(3, not_bipartite))  # False
```

### Example 18: Check Bipartite Graph (DFS)

```python
def is_bipartite_dfs(n, edges):
    """
    Check if graph is bipartite using DFS.

    Time: O(V + E)
    Space: O(V)

    Args:
        n: Number of vertices
        edges: List of edges [u, v]

    Returns:
        True if bipartite, False otherwise
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n

    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    for i in range(n):
        if color[i] == -1:
            if not dfs(i, 0):
                return False

    return True


# Example usage:
print(is_bipartite_dfs(4, bipartite_edges))  # True
print(is_bipartite_dfs(3, not_bipartite))  # False
```

---

## Summary

These examples demonstrate:

1. **Graph Representation**: Building adjacency lists from edge lists
2. **DFS**: Recursive and iterative implementations, path finding
3. **BFS**: Standard traversal, level tracking, shortest path
4. **Union Find**: Optimized with path compression and union by rank
5. **Topological Sort**: Both Kahn's (BFS) and DFS approaches
6. **Cycle Detection**: For directed and undirected graphs, using DFS and Union Find
7. **Connected Components**: Using DFS and Union Find
8. **Bipartite Checking**: Using BFS and DFS with graph coloring

**Key Patterns:**
- Always build adjacency list first for most algorithms
- Use visited set to avoid infinite loops
- DFS: Use recursion or stack
- BFS: Use queue (deque)
- Union Find: Excellent for dynamic connectivity
- Topological Sort: Only works on DAGs
- Graph coloring: Powerful technique for bipartiteness

Practice these implementations until they become second nature!
