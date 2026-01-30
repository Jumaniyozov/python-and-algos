# Graph Theory

## Table of Contents

1. [Graph Fundamentals](#graph-fundamentals)
2. [Graph Representations](#graph-representations)
3. [Graph Traversals](#graph-traversals)
4. [Topological Sort](#topological-sort)
5. [Cycle Detection](#cycle-detection)
6. [Connected Components](#connected-components)
7. [Union Find (Disjoint Set)](#union-find-disjoint-set)
8. [Bipartite Graphs](#bipartite-graphs)
9. [Graph Coloring](#graph-coloring)

---

## Graph Fundamentals

### What is a Graph?

A **graph** is a non-linear data structure consisting of:
- **Vertices (Nodes)**: V = {v₁, v₂, ..., vₙ}
- **Edges**: E = {(u, v) | u, v ∈ V}

A graph G is denoted as G = (V, E).

### Types of Graphs

#### 1. Directed vs Undirected

**Undirected Graph**:
- Edges have no direction
- If (u, v) exists, then (v, u) also exists
- Example: Facebook friendships (mutual)

```
    A --- B
    |     |
    |     |
    C --- D
```

**Directed Graph (Digraph)**:
- Edges have direction (arrows)
- (u, v) ≠ (v, u)
- Example: Twitter follows (one-way)

```
    A --> B
    ^     |
    |     v
    C <-- D
```

#### 2. Weighted vs Unweighted

**Unweighted Graph**:
- All edges have equal weight (or weight = 1)
- Example: Social connections

**Weighted Graph**:
- Edges have associated weights/costs
- Example: Road networks (distances)

```
    A --5-- B
    |       |
    3       2
    |       |
    C --7-- D
```

#### 3. Cyclic vs Acyclic

**Cyclic Graph**:
- Contains at least one cycle (path that starts and ends at same vertex)

```
    A --> B
    ^     |
    |     v
    C <-- D
```

**Acyclic Graph**:
- No cycles
- **DAG (Directed Acyclic Graph)**: Directed graph with no cycles

```
    A --> B
    |     |
    v     v
    C --> D
```

#### 4. Connected vs Disconnected

**Connected Graph** (Undirected):
- Path exists between every pair of vertices

**Strongly Connected** (Directed):
- Path exists from every vertex to every other vertex

**Weakly Connected** (Directed):
- Connected if we ignore edge directions

### Graph Properties

- **Degree**: Number of edges connected to a vertex
  - **In-degree**: Number of incoming edges (directed)
  - **Out-degree**: Number of outgoing edges (directed)

- **Path**: Sequence of vertices where each adjacent pair is connected by an edge
- **Cycle**: Path that starts and ends at the same vertex
- **Connected Component**: Maximal set of vertices where path exists between any two

### Common Graph Terminology

- **Adjacent**: Two vertices connected by an edge
- **Neighbor**: Adjacent vertices
- **Dense Graph**: Many edges (|E| ≈ |V|²)
- **Sparse Graph**: Few edges (|E| ≈ |V|)
- **Complete Graph**: Edge between every pair of vertices (|E| = V*(V-1)/2)
- **Self-loop**: Edge from vertex to itself
- **Multi-graph**: Multiple edges between same pair of vertices

---

## Graph Representations

### 1. Adjacency Matrix

A 2D array where `matrix[i][j] = 1` if edge exists from vertex i to vertex j.

**Structure**:
```python
# Undirected graph
matrix = [
    [0, 1, 1, 0],  # Vertex 0 connects to 1, 2
    [1, 0, 1, 1],  # Vertex 1 connects to 0, 2, 3
    [1, 1, 0, 1],  # Vertex 2 connects to 0, 1, 3
    [0, 1, 1, 0]   # Vertex 3 connects to 1, 2
]

# Weighted graph
matrix = [
    [0, 5, 3, 0],
    [5, 0, 2, 4],
    [3, 2, 0, 7],
    [0, 4, 7, 0]
]
```

**Pros**:
- O(1) edge lookup: Check if edge exists in constant time
- Simple implementation
- Good for dense graphs
- Easy to check edge existence

**Cons**:
- O(V²) space complexity - wasteful for sparse graphs
- O(V²) to iterate through all edges
- O(V) to find all neighbors of a vertex

**When to Use**:
- Dense graphs (many edges)
- Need fast edge existence checks
- Graph is small
- Need to represent weighted graphs simply

### 2. Adjacency List

A collection where each vertex stores a list of its neighbors.

**Structure**:
```python
# Using dictionary (most common in Python)
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

# Using list of lists
graph = [
    [1, 2],      # Vertex 0
    [0, 2, 3],   # Vertex 1
    [0, 1, 3],   # Vertex 2
    [1, 2]       # Vertex 3
]

# Weighted graph (list of tuples)
graph = {
    0: [(1, 5), (2, 3)],
    1: [(0, 5), (2, 2), (3, 4)],
    2: [(0, 3), (1, 2), (3, 7)],
    3: [(1, 4), (2, 7)]
}
```

**Pros**:
- O(V + E) space complexity - efficient for sparse graphs
- O(1) to add an edge
- O(degree) to iterate through neighbors
- Most common representation in interviews

**Cons**:
- O(degree) to check if specific edge exists
- Slightly more complex implementation

**When to Use**:
- Sparse graphs (most real-world graphs)
- Need to iterate through neighbors frequently
- Standard choice for most interview problems

### 3. Edge List

A list of all edges in the graph.

**Structure**:
```python
# Unweighted
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]

# Weighted
edges = [(0, 1, 5), (0, 2, 3), (1, 2, 2), (1, 3, 4), (2, 3, 7)]

# Or as list of objects
edges = [
    {'from': 0, 'to': 1, 'weight': 5},
    {'from': 0, 'to': 2, 'weight': 3},
    # ...
]
```

**Pros**:
- Simple structure
- Easy to sort by weight
- Good for Kruskal's MST algorithm
- Compact for sparse graphs

**Cons**:
- O(E) to find all neighbors of a vertex
- O(E) to check if edge exists
- Need to convert to adjacency list for most algorithms

**When to Use**:
- Input format in problems
- Algorithms that process edges (Kruskal's, Union Find)
- Need to sort edges by weight

### Converting Between Representations

```python
# Edge List to Adjacency List
def edge_list_to_adj_list(n, edges, directed=False):
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph

# Adjacency List to Edge List
def adj_list_to_edge_list(graph, directed=False):
    edges = []
    visited_edges = set()
    for u in graph:
        for v in graph[u]:
            if directed or (v, u) not in visited_edges:
                edges.append((u, v))
                visited_edges.add((u, v))
    return edges

# Adjacency Matrix to Adjacency List
def matrix_to_adj_list(matrix):
    n = len(matrix)
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                graph[i].append(j)
    return graph
```

---

## Graph Traversals

Graph traversal is the process of visiting all vertices in a graph. The two fundamental approaches are **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**.

### Depth-First Search (DFS)

DFS explores as far as possible along each branch before backtracking.

#### Recursive DFS

**Algorithm**:
1. Mark current node as visited
2. Process current node
3. Recursively visit all unvisited neighbors

**Implementation**:
```python
def dfs_recursive(node, graph, visited):
    # Base case: already visited
    if node in visited:
        return

    # Mark as visited
    visited.add(node)
    print(node)  # Process node

    # Recursively visit neighbors
    for neighbor in graph[node]:
        dfs_recursive(neighbor, graph, visited)

# Usage
graph = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [], 5: []}
visited = set()
dfs_recursive(0, graph, visited)
```

**Traversal Order** (for above graph): 0 → 1 → 3 → 4 → 2 → 5

#### Iterative DFS (Using Stack)

**Implementation**:
```python
def dfs_iterative(start, graph):
    stack = [start]
    visited = set([start])

    while stack:
        node = stack.pop()
        print(node)  # Process node

        # Add unvisited neighbors to stack
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
```

**Note**: Order may differ from recursive due to stack processing order.

#### DFS Properties

- **Time Complexity**: O(V + E)
  - Visit each vertex once: O(V)
  - Explore each edge once: O(E)

- **Space Complexity**: O(V)
  - Recursion stack: O(V) in worst case (linear graph)
  - Visited set: O(V)

#### DFS Applications

1. **Cycle Detection**: Track nodes in current path
2. **Topological Sort**: DFS with post-order recording
3. **Connected Components**: Run DFS from unvisited nodes
4. **Path Finding**: Find any path between two nodes
5. **Maze Solving**: Explore all possible paths
6. **Strongly Connected Components**: Kosaraju's or Tarjan's algorithm

#### When to Use DFS

- Need to explore all paths
- Solving backtracking problems
- Topological sorting
- Detecting cycles
- Finding strongly connected components
- Less memory than BFS in some cases

### Breadth-First Search (BFS)

BFS explores all neighbors at current depth before moving to next depth level.

#### BFS Algorithm

**Algorithm**:
1. Start from source node, add to queue
2. While queue not empty:
   - Dequeue a node
   - Process the node
   - Enqueue all unvisited neighbors

**Implementation**:
```python
from collections import deque

def bfs(start, graph):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        print(node)  # Process node

        # Add unvisited neighbors to queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Usage
graph = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [], 5: []}
bfs(0, graph)
```

**Traversal Order**: 0 → 1 → 2 → 3 → 4 → 5 (level by level)

#### BFS with Levels

```python
def bfs_with_levels(start, graph):
    queue = deque([(start, 0)])  # (node, level)
    visited = set([start])

    while queue:
        node, level = queue.popleft()
        print(f"Node {node} at level {level}")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))
```

#### BFS for Shortest Path (Unweighted)

```python
def shortest_path_bfs(start, target, graph):
    queue = deque([(start, [start])])  # (node, path)
    visited = set([start])

    while queue:
        node, path = queue.popleft()

        if node == target:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # No path found
```

#### BFS Properties

- **Time Complexity**: O(V + E)
  - Visit each vertex once: O(V)
  - Explore each edge once: O(E)

- **Space Complexity**: O(V)
  - Queue: O(V) in worst case
  - Visited set: O(V)

#### BFS Applications

1. **Shortest Path (Unweighted)**: BFS guarantees shortest path
2. **Level-Order Traversal**: Process nodes level by level
3. **Connected Components**: Similar to DFS
4. **Bipartite Graph Detection**: Color nodes while traversing
5. **Social Network Analysis**: Friends at distance k
6. **Web Crawling**: Explore pages level by level

#### When to Use BFS

- Finding shortest path in unweighted graph
- Level-order processing needed
- Exploring neighbors layer by layer
- Testing bipartiteness
- Finding minimum number of moves/steps

### DFS vs BFS Comparison

| Aspect | DFS | BFS |
|--------|-----|-----|
| Data Structure | Stack (recursion) | Queue |
| Memory | O(h) where h is height | O(w) where w is max width |
| Shortest Path | No | Yes (unweighted) |
| When to Use | Explore all paths, backtracking | Shortest path, level-order |
| Implementation | Simpler (recursive) | Slightly more complex |
| Path Finding | Any path | Shortest path |

**Decision Guide**:
- **Use DFS** when:
  - Need to explore all paths/solutions
  - Solving backtracking problems
  - Detecting cycles
  - Topological sorting
  - Graph is deep but not wide

- **Use BFS** when:
  - Need shortest path (unweighted)
  - Need level-order information
  - Finding minimum steps/moves
  - Graph is wide but not deep
  - Checking bipartiteness

---

## Topological Sort

**Topological sorting** is a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge (u, v), vertex u comes before v in the ordering.

### Properties

- Only possible for **Directed Acyclic Graphs (DAGs)**
- Not unique - multiple valid orderings may exist
- Used for scheduling tasks with dependencies

### Applications

- Course prerequisite scheduling
- Build system dependencies
- Task scheduling
- Compiler dependency resolution
- Package manager installation order

### Approach 1: Kahn's Algorithm (BFS-based)

**Algorithm**:
1. Calculate in-degree for all vertices
2. Add all vertices with in-degree 0 to queue
3. While queue not empty:
   - Dequeue vertex and add to result
   - Reduce in-degree of neighbors by 1
   - If neighbor's in-degree becomes 0, add to queue
4. If all vertices processed, return result; else graph has cycle

**Implementation**:
```python
from collections import deque, defaultdict

def topological_sort_kahn(n, edges):
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

# Example
n = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print(topological_sort_kahn(n, edges))  # [4, 5, 0, 2, 3, 1] or [5, 4, 0, 2, 3, 1]
```

**Complexity**:
- Time: O(V + E)
- Space: O(V + E)

**Advantages**:
- Easy to understand
- Naturally detects cycles
- Can count number of valid orderings

### Approach 2: DFS-based

**Algorithm**:
1. Perform DFS on all unvisited nodes
2. After visiting all neighbors, add node to stack (post-order)
3. Reverse the stack to get topological order

**Implementation**:
```python
def topological_sort_dfs(n, edges):
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
        stack.append(node)  # Add after visiting all neighbors

    # Run DFS from all unvisited nodes
    for i in range(n):
        if i not in visited:
            dfs(i)

    return stack[::-1]  # Reverse to get topological order

# Example
n = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print(topological_sort_dfs(n, edges))  # [5, 4, 2, 3, 0, 1] or similar
```

**Complexity**:
- Time: O(V + E)
- Space: O(V)

**Why Post-Order Works**:
- If u → v (edge from u to v), DFS visits v before returning to u
- When we return to u, all descendants are already in stack
- Reversing ensures u comes before v

### Cycle Detection in Topological Sort

```python
def has_cycle_topological(n, edges):
    graph = defaultdict(list)
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    count = 0

    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return count != n  # Cycle exists if not all nodes processed
```

---

## Cycle Detection

Detecting cycles is crucial for many graph algorithms and applications.

### Cycle Detection in Undirected Graph

**Using DFS**:

```python
def has_cycle_undirected(graph):
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
    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True

    return False
```

**Key Insight**: In undirected graph, if we visit a neighbor that's already visited and it's not our parent, we found a cycle.

**Using Union Find**:

```python
def has_cycle_undirected_uf(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False  # Cycle detected
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1
        return True

    for u, v in edges:
        if not union(u, v):
            return True  # Cycle found

    return False
```

### Cycle Detection in Directed Graph

**Using DFS with Colors (3-State)**:

```python
def has_cycle_directed(graph):
    # White (0): Unvisited
    # Gray (1): In current DFS path
    # Black (2): Completely processed

    color = {node: 0 for node in graph}

    def dfs(node):
        if color[node] == 1:
            return True  # Back edge to ancestor = cycle
        if color[node] == 2:
            return False  # Already processed

        color[node] = 1  # Mark as in current path

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        color[node] = 2  # Mark as processed
        return False

    for node in graph:
        if color[node] == 0:
            if dfs(node):
                return True

    return False
```

**Key Insight**: If we encounter a node in the current DFS path (gray), we found a back edge, indicating a cycle.

**Using Topological Sort**:

```python
def has_cycle_directed_topo(n, edges):
    # If topological sort processes all nodes, no cycle
    graph = defaultdict(list)
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    count = 0

    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return count != n
```

---

## Connected Components

A connected component is a maximal set of vertices where a path exists between any two vertices.

### Using DFS

```python
def count_components_dfs(n, edges):
    # Build adjacency list
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
    for node in range(n):
        if node not in visited:
            dfs(node)
            components += 1

    return components
```

### Using BFS

```python
def count_components_bfs(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    components = 0

    for node in range(n):
        if node not in visited:
            queue = deque([node])
            visited.add(node)

            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            components += 1

    return components
```

### Using Union Find

```python
def count_components_uf(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1

    for u, v in edges:
        union(u, v)

    # Count unique parents
    return len(set(find(i) for i in range(n)))
```

**Complexity**:
- DFS/BFS: O(V + E)
- Union Find: O(E * α(V)) ≈ O(E)

---

## Union Find (Disjoint Set)

Union Find is a data structure for efficiently managing disjoint sets with two operations:
- **Find**: Determine which set an element belongs to
- **Union**: Merge two sets into one

### Basic Implementation

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # Number of components

    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already in same set

        self.parent[px] = py
        self.count -= 1
        return True
```

**Complexity** (Basic):
- Find: O(n) worst case
- Union: O(n) worst case

### Optimization 1: Path Compression

Flatten the tree structure during find operations.

```python
def find(self, x):
    if self.parent[x] != x:
        self.parent[x] = self.find(self.parent[x])  # Path compression
    return self.parent[x]
```

**Effect**: Makes subsequent finds faster by directly connecting nodes to root.

### Optimization 2: Union by Rank

Always attach smaller tree under root of larger tree.

```python
def union(self, x, y):
    px, py = self.find(x), self.find(y)
    if px == py:
        return False

    # Union by rank
    if self.rank[px] < self.rank[py]:
        self.parent[px] = py
    elif self.rank[px] > self.rank[py]:
        self.parent[py] = px
    else:
        self.parent[py] = px
        self.rank[px] += 1

    self.count -= 1
    return True
```

### Complete Optimized Implementation

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        # Union by rank
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

        self.count -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_count(self):
        return self.count
```

**Complexity** (Optimized):
- Find: O(α(n)) ≈ O(1) amortized
- Union: O(α(n)) ≈ O(1) amortized
- α(n) is the inverse Ackermann function, grows extremely slowly

### Union Find Applications

1. **Detecting Cycles in Undirected Graph**
2. **Finding Connected Components**
3. **Kruskal's Minimum Spanning Tree**
4. **Network Connectivity**
5. **Image Processing** (connected regions)
6. **Social Networks** (friend groups)

### When to Use Union Find

- Need to track connected components dynamically
- Checking if two elements are in same set
- Detecting cycles in undirected graphs
- Problems involving grouping/clustering
- Better than DFS/BFS when many connectivity queries

---

## Bipartite Graphs

A **bipartite graph** is a graph whose vertices can be divided into two disjoint sets such that every edge connects vertices from different sets.

### Properties

- Can be colored using 2 colors such that no adjacent vertices have same color
- Contains no odd-length cycles
- Examples: Matching problems, task assignment

### Detection Using BFS (Coloring)

```python
def is_bipartite_bfs(graph):
    n = len(graph)
    color = [-1] * n  # -1: uncolored, 0: color A, 1: color B

    for start in range(n):
        if color[start] != -1:
            continue

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
```

### Detection Using DFS

```python
def is_bipartite_dfs(graph):
    n = len(graph)
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
```

**Complexity**: O(V + E)

### Applications

- Job matching (workers to tasks)
- Dating apps (matching two groups)
- Resource allocation
- Stable marriage problem
- Graph coloring with 2 colors

---

## Graph Coloring

**Graph coloring** assigns colors to vertices such that no two adjacent vertices have the same color.

### Chromatic Number

Minimum number of colors needed to color a graph.

- **Bipartite graph**: χ = 2
- **Odd cycle**: χ = 3
- **Complete graph Kₙ**: χ = n

### Greedy Coloring Algorithm

```python
def greedy_coloring(graph):
    n = len(graph)
    color = [-1] * n

    for node in range(n):
        # Find available colors
        used_colors = set()
        for neighbor in graph[node]:
            if color[neighbor] != -1:
                used_colors.add(color[neighbor])

        # Assign smallest available color
        c = 0
        while c in used_colors:
            c += 1
        color[node] = c

    return color

# Example
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
colors = greedy_coloring(graph)
print(colors)  # [0, 1, 2, 0] or similar
```

**Complexity**: O(V + E)

**Note**: Greedy doesn't guarantee minimum colors, but provides upper bound.

### Applications

- Register allocation in compilers
- Scheduling problems (exam timetabling)
- Map coloring (Four Color Theorem)
- Frequency assignment in mobile networks
- Sudoku solving

---

## Summary of Time Complexities

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| DFS | O(V + E) | O(V) |
| BFS | O(V + E) | O(V) |
| Topological Sort (Kahn) | O(V + E) | O(V + E) |
| Topological Sort (DFS) | O(V + E) | O(V) |
| Cycle Detection | O(V + E) | O(V) |
| Connected Components (DFS/BFS) | O(V + E) | O(V) |
| Connected Components (Union Find) | O(E * α(V)) | O(V) |
| Union Find (optimized) | O(α(V)) per op | O(V) |
| Bipartite Check | O(V + E) | O(V) |
| Graph Coloring (greedy) | O(V + E) | O(V) |

---

## Key Takeaways

1. **Choose the right representation**: Adjacency list for most problems, matrix for dense graphs
2. **Master DFS and BFS**: They're the foundation of most graph algorithms
3. **Visited set is crucial**: Always track visited nodes to avoid infinite loops
4. **DFS for depth, BFS for breadth**: DFS for cycles/paths, BFS for shortest paths
5. **Union Find is powerful**: Optimal for dynamic connectivity queries
6. **Topological sort requires DAG**: Always check for cycles first
7. **Path compression matters**: Makes Union Find nearly O(1)
8. **Think about edge cases**: Disconnected graphs, single nodes, self-loops

Understanding these core graph algorithms will enable you to solve a wide variety of complex problems in interviews and real-world applications.
