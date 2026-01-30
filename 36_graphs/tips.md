# Chapter 36: Graphs - Tips and Tricks

## Table of Contents
1. [Common Pitfalls](#common-pitfalls)
2. [Pattern Recognition](#pattern-recognition)
3. [Interview Tips](#interview-tips)
4. [Performance Optimization](#performance-optimization)
5. [LeetCode Practice Problems](#leetcode-practice-problems)
6. [8-Week Study Plan](#8-week-study-plan)

---

## Common Pitfalls

### 1. Forgetting to Mark Nodes as Visited

```python
# ❌ WRONG: Infinite loop
def dfs(node, graph):
    for neighbor in graph[node]:
        dfs(neighbor, graph)  # No visited check!

# ✅ CORRECT: Track visited nodes
def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, graph, visited)
```

### 2. Not Handling Disconnected Graphs

```python
# ❌ WRONG: Only explores one component
visited = set()
dfs(0, graph, visited)  # Only explores component containing 0

# ✅ CORRECT: Check all components
visited = set()
for node in range(n):
    if node not in visited:
        dfs(node, graph, visited)
```

### 3. Confusing Directed vs Undirected

```python
# Building undirected graph
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # MUST add both directions!

# Building directed graph
for u, v in edges:
    graph[u].append(v)  # Only one direction
```

### 4. Not Converting Edge List to Adjacency List

```python
# ❌ WRONG: Using edge list directly is inefficient
def dfs(node, edges, visited):
    for u, v in edges:  # O(E) to find neighbors!
        if u == node:
            dfs(v, edges, visited)

# ✅ CORRECT: Build adjacency list first
graph = build_graph(n, edges)  # O(E) once
def dfs(node, graph, visited):
    for neighbor in graph[node]:  # O(degree) per node
        dfs(neighbor, graph, visited)
```

### 5. Incorrect Cycle Detection in Undirected Graph

```python
# ❌ WRONG: Counts parent as cycle
def has_cycle(node, graph, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor in visited:  # Parent will be visited!
            return True
        if has_cycle(neighbor, graph, visited):
            return True
    return False

# ✅ CORRECT: Track parent
def has_cycle(node, parent, graph, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor != parent:  # Don't check parent
            if neighbor in visited:
                return True
            if has_cycle(neighbor, node, graph, visited):
                return True
    return False
```

### 6. Wrong Topological Sort Validation

```python
# ❌ WRONG: Not checking if all nodes processed
def topological_sort(n, edges):
    # ... Kahn's algorithm
    return result  # May have cycle!

# ✅ CORRECT: Validate all nodes processed
def topological_sort(n, edges):
    # ... Kahn's algorithm
    if len(result) == n:
        return result
    else:
        return []  # Cycle detected
```

---

## Pattern Recognition

### Pattern 1: Standard DFS/BFS Traversal

**When to Use:**
- Finding paths
- Exploring all nodes
- Checking connectivity

**Template:**

```python
# DFS
def dfs(node, graph, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)

# BFS
from collections import deque

def bfs(start, graph):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**Problems:** Number of Islands, Clone Graph, Keys and Rooms

---

### Pattern 2: Shortest Path (Unweighted)

**When to Use:**
- Finding minimum steps/distance
- Unweighted graph

**Template:**

```python
def shortest_path_bfs(start, target, graph):
    queue = deque([(start, 0)])  # (node, distance)
    visited = {start}

    while queue:
        node, dist = queue.popleft()

        if node == target:
            return dist

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1  # No path
```

**Problems:** Word Ladder, Shortest Path in Binary Matrix

---

### Pattern 3: Connected Components

**When to Use:**
- Counting separate groups
- Grouping related items

**Template:**

```python
# DFS approach
def count_components(n, edges):
    graph = build_graph(n, edges)
    visited = set()
    count = 0

    for node in range(n):
        if node not in visited:
            dfs(node, graph, visited)
            count += 1

    return count
```

**Problems:** Number of Provinces, Number of Islands, Accounts Merge

---

### Pattern 4: Cycle Detection

**When to Use:**
- Validating DAG
- Detecting circular dependencies

**Directed Graph (3 Colors):**

```python
def has_cycle_directed(graph):
    # 0: white, 1: gray, 2: black
    color = {node: 0 for node in graph}

    def dfs(node):
        if color[node] == 1:
            return True  # Back edge = cycle
        if color[node] == 2:
            return False

        color[node] = 1
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        color[node] = 2
        return False

    for node in graph:
        if color[node] == 0 and dfs(node):
            return True
    return False
```

**Undirected Graph:**

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
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False
```

**Problems:** Course Schedule, Graph Valid Tree, Redundant Connection

---

### Pattern 5: Topological Sort

**When to Use:**
- Task scheduling with dependencies
- Course prerequisites
- Build order

**Kahn's Algorithm (BFS):**

```python
from collections import deque, defaultdict

def topological_sort(n, edges):
    graph = defaultdict(list)
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == n else []
```

**DFS Approach:**

```python
def topological_sort_dfs(n, edges):
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
        stack.append(node)

    for i in range(n):
        if i not in visited:
            dfs(i)

    return stack[::-1]
```

**Problems:** Course Schedule II, Alien Dictionary, Minimum Height Trees

---

### Pattern 6: Union Find

**When to Use:**
- Dynamic connectivity
- Grouping elements
- Cycle detection in undirected graphs

**Optimized Template:**

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
```

**Problems:** Number of Connected Components, Redundant Connection, Accounts Merge

---

### Pattern 7: Bipartite Graph

**When to Use:**
- Two-group partitioning
- Conflict checking
- Graph coloring with 2 colors

**Template:**

```python
from collections import deque

def is_bipartite(graph):
    n = len(graph)
    color = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue

        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False

    return True
```

**Problems:** Is Graph Bipartite?, Possible Bipartition

---

### Pattern 8: Grid as Graph

**When to Use:**
- 2D grid problems
- Islands, regions
- Pathfinding in matrix

**Template:**

```python
def grid_dfs(grid, r, c, visited):
    m, n = len(grid), len(grid[0])
    if (r < 0 or r >= m or c < 0 or c >= n or
        (r, c) in visited or grid[r][c] == 0):
        return

    visited.add((r, c))

    # 4 directions
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        grid_dfs(grid, r+dr, c+dc, visited)

    # 8 directions (include diagonals)
    # for dr in [-1, 0, 1]:
    #     for dc in [-1, 0, 1]:
    #         if dr != 0 or dc != 0:
    #             grid_dfs(grid, r+dr, c+dc, visited)
```

**Problems:** Number of Islands, Pacific Atlantic Water Flow, Surrounded Regions

---

## Interview Tips

### Clarifying Questions

```
Always ask:
1. "Is the graph directed or undirected?"
2. "Is the graph weighted or unweighted?"
3. "Can there be self-loops or multiple edges?"
4. "Can the graph be disconnected?"
5. "What's the size range? (V and E)"
6. "How is the graph represented? (adjacency list/matrix/edge list)"
```

### Communication Strategy

```
1. Identify the graph pattern
   "This looks like a [pattern] problem..."

2. Choose the algorithm
   "I'll use [DFS/BFS/Union Find] because..."

3. Explain the approach
   "First, I'll build the adjacency list..."
   "Then I'll traverse using..."

4. Discuss complexity
   "Time: O(V + E), Space: O(V) because..."

5. Handle edge cases
   "For disconnected graphs, I'll..."
   "For empty graph, I'll return..."
```

### When to Use DFS vs BFS

**Use DFS when:**
- Need to explore all paths
- Solving backtracking problems
- Detecting cycles
- Topological sorting
- Memory constrained (depth rather than width)

**Use BFS when:**
- Finding shortest path (unweighted)
- Level-order traversal needed
- Finding minimum steps/moves
- Graph is wide but not deep

**Use Union Find when:**
- Dynamic connectivity queries
- Checking if elements are connected
- Counting connected components
- Detecting cycles in undirected graphs
- Grouping/merging sets

---

## Performance Optimization

### Space Optimization

```python
# Instead of storing paths
paths = [[0, 1, 2], [0, 3, 2], ...]  # O(n × path_length)

# Store only current path
def dfs(node, path):
    if node == target:
        print(path)
    for neighbor in graph[node]:
        dfs(neighbor, path + [neighbor])
```

### Time Optimization

```python
# Build adjacency list once, not per query
# ❌ Inefficient
for query in queries:
    graph = build_graph(edges)  # O(E) per query
    answer = bfs(graph, query)

# ✅ Efficient
graph = build_graph(edges)  # O(E) once
for query in queries:
    answer = bfs(graph, query)
```

### Using Python Built-ins

```python
from collections import defaultdict, deque

# Adjacency list
graph = defaultdict(list)  # No need to initialize

# BFS queue
queue = deque()  # O(1) append and popleft

# Visited set
visited = set()  # O(1) lookup
```

---

## LeetCode Practice Problems

### Easy (20 problems)

#### Basic Traversal (7 problems)

1. **Number of Provinces** - https://leetcode.com/problems/number-of-provinces/
   - Pattern: Connected Components (DFS/BFS/Union Find)
   - Key: Count components in adjacency matrix
   - Difficulty: Easy

2. **Find if Path Exists in Graph** - https://leetcode.com/problems/find-if-path-exists-in-graph/
   - Pattern: Graph Traversal
   - Key: Simple BFS/DFS path checking
   - Difficulty: Easy

3. **Find Center of Star Graph** - https://leetcode.com/problems/find-center-of-star-graph/
   - Pattern: Graph Properties
   - Key: Center appears in all edges
   - Difficulty: Easy

4. **Find the Town Judge** - https://leetcode.com/problems/find-the-town-judge/
   - Pattern: In-degree/Out-degree
   - Key: Judge has in-degree n-1, out-degree 0
   - Difficulty: Easy

5. **All Paths From Source to Target** - https://leetcode.com/problems/all-paths-from-source-to-target/
   - Pattern: DFS Backtracking
   - Key: DAG, find all paths
   - Difficulty: Easy

6. **Number of Connected Components** - Premium
   - Pattern: Connected Components
   - Key: Union Find or DFS
   - Difficulty: Easy

7. **Graph Valid Tree** - Premium
   - Pattern: Cycle Detection + Connectivity
   - Key: n-1 edges, connected, no cycles
   - Difficulty: Easy

#### Simple BFS/DFS (6 problems)

8. **Flood Fill** - https://leetcode.com/problems/flood-fill/
   - Pattern: Grid DFS/BFS
   - Key: Change connected cells of same color
   - Difficulty: Easy

9. **Island Perimeter** - https://leetcode.com/problems/island-perimeter/
   - Pattern: Grid Traversal
   - Key: Count edges touching water
   - Difficulty: Easy

10. **Max Area of Island** - https://leetcode.com/problems/max-area-of-island/
    - Pattern: Grid DFS
    - Key: Find largest connected component
    - Difficulty: Easy-Medium

11. **Employee Importance** - https://leetcode.com/problems/employee-importance/
    - Pattern: Graph Traversal
    - Key: Sum values in subtree
    - Difficulty: Easy

12. **Shortest Bridge** - https://leetcode.com/problems/shortest-bridge/
    - Pattern: Multi-source BFS
    - Key: Find one island, BFS to other
    - Difficulty: Medium (but good practice)

13. **Minimum Depth of Binary Tree** - https://leetcode.com/problems/minimum-depth-of-binary-tree/
    - Pattern: BFS on Tree
    - Key: Level-order until first leaf
    - Difficulty: Easy

#### Basic Connectivity (7 problems)

14. **Find if Path Exists** - https://leetcode.com/problems/find-if-path-exists-in-graph/
    - Pattern: Simple Path Finding
    - Key: DFS/BFS from source to destination
    - Difficulty: Easy

15. **N-ary Tree Level Order Traversal** - https://leetcode.com/problems/n-ary-tree-level-order-traversal/
    - Pattern: BFS
    - Key: Level-by-level traversal
    - Difficulty: Easy

16. **Binary Tree Level Order Traversal** - https://leetcode.com/problems/binary-tree-level-order-traversal/
    - Pattern: BFS
    - Key: Classic level-order
    - Difficulty: Medium (but fundamental)

17. **Cousins in Binary Tree** - https://leetcode.com/problems/cousins-in-binary-tree/
    - Pattern: BFS with tracking
    - Key: Track parent and depth
    - Difficulty: Easy

18. **Deepest Leaves Sum** - https://leetcode.com/problems/deepest-leaves-sum/
    - Pattern: BFS
    - Key: Sum last level
    - Difficulty: Medium

19. **Average of Levels** - https://leetcode.com/problems/average-of-levels-in-binary-tree/
    - Pattern: BFS
    - Key: Calculate average per level
    - Difficulty: Easy

20. **Surrounded Regions** - https://leetcode.com/problems/surrounded-regions/
    - Pattern: Grid DFS from borders
    - Key: Mark border-connected, flip rest
    - Difficulty: Medium

---

### Medium (30 problems)

#### Core Graph Algorithms (10 problems)

21. **Clone Graph** - https://leetcode.com/problems/clone-graph/
    - Pattern: DFS/BFS with HashMap
    - Key: Map original to cloned nodes
    - Difficulty: Medium

22. **Course Schedule** - https://leetcode.com/problems/course-schedule/
    - Pattern: Cycle Detection (Directed)
    - Key: DFS with 3 states
    - Difficulty: Medium

23. **Course Schedule II** - https://leetcode.com/problems/course-schedule-ii/
    - Pattern: Topological Sort
    - Key: Kahn's algorithm or DFS
    - Difficulty: Medium

24. **Number of Islands** - https://leetcode.com/problems/number-of-islands/
    - Pattern: Grid DFS/BFS
    - Key: Count components
    - Difficulty: Medium

25. **Pacific Atlantic Water Flow** - https://leetcode.com/problems/pacific-atlantic-water-flow/
    - Pattern: Multi-source DFS
    - Key: Search from both oceans
    - Difficulty: Medium

26. **Is Graph Bipartite?** - https://leetcode.com/problems/is-graph-bipartite/
    - Pattern: Graph Coloring
    - Key: 2-color with BFS/DFS
    - Difficulty: Medium

27. **Redundant Connection** - https://leetcode.com/problems/redundant-connection/
    - Pattern: Union Find
    - Key: Find edge creating cycle
    - Difficulty: Medium

28. **Keys and Rooms** - https://leetcode.com/problems/keys-and-rooms/
    - Pattern: DFS/BFS
    - Key: Check if all nodes reachable
    - Difficulty: Medium

29. **Minimum Height Trees** - https://leetcode.com/problems/minimum-height-trees/
    - Pattern: Topological Sort variant
    - Key: Trim leaves layer by layer
    - Difficulty: Medium

30. **Shortest Path in Binary Matrix** - https://leetcode.com/problems/shortest-path-in-binary-matrix/
    - Pattern: BFS on Grid
    - Key: 8-directional BFS
    - Difficulty: Medium

#### Advanced Patterns (10 problems)

31. **Accounts Merge** - https://leetcode.com/problems/accounts-merge/
    - Pattern: Union Find
    - Key: Group by common emails
    - Difficulty: Medium

32. **Evaluate Division** - https://leetcode.com/problems/evaluate-division/
    - Pattern: Weighted Graph DFS
    - Key: Build graph with division values
    - Difficulty: Medium

33. **Shortest Bridge** - https://leetcode.com/problems/shortest-bridge/
    - Pattern: DFS + BFS
    - Key: Find island then expand
    - Difficulty: Medium

34. **Rotting Oranges** - https://leetcode.com/problems/rotting-oranges/
    - Pattern: Multi-source BFS
    - Key: BFS from all rotten simultaneously
    - Difficulty: Medium

35. **01 Matrix** - https://leetcode.com/problems/01-matrix/
    - Pattern: Multi-source BFS
    - Key: BFS from all 0s
    - Difficulty: Medium

36. **As Far from Land** - https://leetcode.com/problems/as-far-from-land-as-possible/
    - Pattern: Multi-source BFS
    - Key: BFS from all land cells
    - Difficulty: Medium

37. **Walls and Gates** - Premium
    - Pattern: Multi-source BFS
    - Key: BFS from all gates
    - Difficulty: Medium

38. **Number of Distinct Islands** - Premium
    - Pattern: DFS with Shape Tracking
    - Key: Normalize island shapes
    - Difficulty: Medium

39. **Graph Connectivity With Threshold** - https://leetcode.com/problems/graph-connectivity-with-threshold/
    - Pattern: Union Find
    - Key: Connect divisible numbers
    - Difficulty: Hard (but good Union Find practice)

40. **Regions Cut By Slashes** - https://leetcode.com/problems/regions-cut-by-slashes/
    - Pattern: Union Find
    - Key: Divide each cell into 4 parts
    - Difficulty: Medium

#### Complex Applications (10 problems)

41. **Snakes and Ladders** - https://leetcode.com/problems/snakes-and-ladders/
    - Pattern: BFS
    - Key: Model as graph, BFS for shortest
    - Difficulty: Medium

42. **Open the Lock** - https://leetcode.com/problems/open-the-lock/
    - Pattern: BFS
    - Key: State space exploration
    - Difficulty: Medium

43. **Minimum Knight Moves** - Premium
    - Pattern: BFS
    - Key: Chess piece movement
    - Difficulty: Medium

44. **Network Delay Time** - https://leetcode.com/problems/network-delay-time/
    - Pattern: Dijkstra's (Shortest Path)
    - Key: Find time to reach all nodes
    - Difficulty: Medium

45. **Cheapest Flights Within K Stops** - https://leetcode.com/problems/cheapest-flights-within-k-stops/
    - Pattern: Modified Dijkstra/BFS
    - Key: Shortest path with constraints
    - Difficulty: Medium

46. **Path with Maximum Probability** - https://leetcode.com/problems/path-with-maximum-probability/
    - Pattern: Modified Dijkstra
    - Key: Maximum instead of minimum
    - Difficulty: Medium

47. **Reconstruct Itinerary** - https://leetcode.com/problems/reconstruct-itinerary/
    - Pattern: Eulerian Path
    - Key: DFS with edge removal
    - Difficulty: Hard

48. **Longest Increasing Path** - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
    - Pattern: DFS with Memoization
    - Key: DP on grid
    - Difficulty: Hard

49. **Making A Large Island** - https://leetcode.com/problems/making-a-large-island/
    - Pattern: DFS + Union Find
    - Key: Calculate island sizes, try connecting
    - Difficulty: Hard

50. **Number of Operations to Make Network Connected** - https://leetcode.com/problems/number-of-operations-to-make-network-connected/
    - Pattern: Union Find
    - Key: Count components and extra edges
    - Difficulty: Medium

---

### Hard (25 problems)

#### Advanced Algorithms (10 problems)

51. **Word Ladder** - https://leetcode.com/problems/word-ladder/
    - Pattern: BFS
    - Key: Transform words, shortest path
    - Difficulty: Hard

52. **Word Ladder II** - https://leetcode.com/problems/word-ladder-ii/
    - Pattern: BFS + Backtracking
    - Key: Find all shortest paths
    - Difficulty: Hard

53. **Alien Dictionary** - Premium
    - Pattern: Topological Sort
    - Key: Build order from word comparisons
    - Difficulty: Hard

54. **Critical Connections in a Network** - https://leetcode.com/problems/critical-connections-in-a-network/
    - Pattern: Tarjan's Algorithm (Bridges)
    - Key: Find edges whose removal disconnects
    - Difficulty: Hard

55. **Minimum Number of Days to Disconnect Island** - https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/
    - Pattern: DFS + Articulation Points
    - Key: Try removing cells, check connectivity
    - Difficulty: Hard

56. **Count Subtrees With Max Distance** - https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/
    - Pattern: Enumeration + Tree Diameter
    - Key: Try all subsets, find diameter
    - Difficulty: Hard

57. **Shortest Path Visiting All Nodes** - https://leetcode.com/problems/shortest-path-visiting-all-nodes/
    - Pattern: BFS with Bitmask
    - Key: State = (node, visited_set)
    - Difficulty: Hard

58. **Bus Routes** - https://leetcode.com/problems/bus-routes/
    - Pattern: BFS on Routes
    - Key: Model routes as nodes
    - Difficulty: Hard

59. **Sliding Puzzle** - https://leetcode.com/problems/sliding-puzzle/
    - Pattern: BFS on States
    - Key: State space search
    - Difficulty: Hard

60. **Minimum Cost to Make at Least One Valid Path** - https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
    - Pattern: 0-1 BFS / Dijkstra
    - Key: Cost 0 for following arrows, 1 for changing
    - Difficulty: Hard

#### Minimum Spanning Tree (5 problems)

61. **Min Cost to Connect All Points** - https://leetcode.com/problems/min-cost-to-connect-all-points/
    - Pattern: Prim's/Kruskal's MST
    - Key: Manhattan distance MST
    - Difficulty: Medium-Hard

62. **Optimize Water Distribution** - Premium
    - Pattern: MST with Virtual Node
    - Key: Add virtual source for wells
    - Difficulty: Hard

63. **Connecting Cities With Minimum Cost** - Premium
    - Pattern: Kruskal's MST
    - Key: Standard MST problem
    - Difficulty: Medium

64. **Find Critical and Pseudo-Critical Edges in MST** - https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
    - Pattern: MST Analysis
    - Key: Try excluding/including each edge
    - Difficulty: Hard

65. **Minimum Cost to Reach Destination in Time** - https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/
    - Pattern: Dijkstra with Constraints
    - Key: Track time and cost
    - Difficulty: Hard

#### Advanced Grid Problems (5 problems)

66. **Escape a Large Maze** - https://leetcode.com/problems/escape-a-large-maze/
    - Pattern: BFS with Cycle Detection
    - Key: Check if trapped in finite region
    - Difficulty: Hard

67. **Bricks Falling When Hit** - https://leetcode.com/problems/bricks-falling-when-hit/
    - Pattern: Reverse Union Find
    - Key: Process removals in reverse
    - Difficulty: Hard

68. **Number of Islands II** - Premium
    - Pattern: Online Union Find
    - Key: Add lands incrementally
    - Difficulty: Hard

69. **Shortest Distance from All Buildings** - Premium
    - Pattern: Multi-source BFS
    - Key: BFS from each building
    - Difficulty: Hard

70. **Swim in Rising Water** - https://leetcode.com/problems/swim-in-rising-water/
    - Pattern: Binary Search + BFS or Dijkstra
    - Key: Find minimum time to reach end
    - Difficulty: Hard

#### Complex Graph Problems (5 problems)

71. **Reachable Nodes In Subdivided Graph** - https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/
    - Pattern: Dijkstra with Edge Traversal
    - Key: Track distance and nodes visited
    - Difficulty: Hard

72. **Second Minimum Node in DAG** - https://leetcode.com/problems/second-minimum-value-in-a-binary-tree/
    - Pattern: Modified Dijkstra
    - Key: Track second shortest path
    - Difficulty: Medium

73. **Path with Maximum Minimum Value** - Premium
    - Pattern: Binary Search + BFS or Union Find
    - Key: Maximize minimum edge weight
    - Difficulty: Medium-Hard

74. **All Ancestors of a Node in DAG** - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
    - Pattern: Reverse Graph DFS
    - Key: DFS from each node in reverse graph
    - Difficulty: Medium

75. **Parallel Courses II** - https://leetcode.com/problems/parallel-courses-ii/
    - Pattern: Topological Sort + Bitmask DP
    - Key: Minimize semesters with parallelism
    - Difficulty: Hard

---

## Pattern Mastery Checklist

### Core Patterns (Must Master)

- [ ] **DFS Traversal**
  - Recursive and iterative
  - With visited tracking
  - Path recording
  - Problems: #21, #24, #4

- [ ] **BFS Traversal**
  - Level-order
  - Shortest path (unweighted)
  - Multi-source BFS
  - Problems: #2, #24, #34

- [ ] **Union Find**
  - Path compression
  - Union by rank
  - Component counting
  - Problems: #27, #31, #6

- [ ] **Topological Sort**
  - Kahn's algorithm (BFS)
  - DFS-based
  - Cycle detection
  - Problems: #22, #23, #53

- [ ] **Cycle Detection**
  - Directed (3 colors)
  - Undirected (parent tracking)
  - Union Find approach
  - Problems: #22, #27

- [ ] **Bipartite Checking**
  - Graph coloring (2 colors)
  - BFS or DFS
  - Problems: #26

- [ ] **Grid as Graph**
  - 4-directional DFS/BFS
  - 8-directional movement
  - Multi-source problems
  - Problems: #24, #25, #34

### Advanced Patterns

- [ ] **Shortest Path Algorithms**
  - Dijkstra's
  - Bellman-Ford
  - Floyd-Warshall
  - Problems: #44, #45, #60

- [ ] **Minimum Spanning Tree**
  - Prim's algorithm
  - Kruskal's algorithm
  - Problems: #61, #62, #64

- [ ] **Special Algorithms**
  - Tarjan's (bridges/articulation points)
  - Eulerian path
  - Kosaraju's (SCC)
  - Problems: #54, #47

---

## 8-Week Study Plan

### Week 1-2: Foundations (Easy Problems)
**Goal**: Master basic DFS, BFS, and graph building

**Day 1-2**: DFS Basics
- Read theory on DFS
- Solve: #1, #2, #4
- Practice building adjacency lists

**Day 3-4**: BFS Basics
- Read theory on BFS
- Solve: #8, #9, #13
- Compare DFS vs BFS

**Day 5-6**: Connected Components
- Read theory on connectivity
- Solve: #6, #7, #10
- Practice counting components

**Day 7**: Grid as Graph
- Read grid patterns
- Solve: #8, #10
- Practice 4-directional traversal

**Week 1-2 Total**: ~15 easy problems

---

### Week 3-4: Core Patterns (Medium Problems)
**Goal**: Master cycle detection, topological sort, Union Find

**Day 8-9**: Cycle Detection
- Read theory on cycles
- Solve: #22, #27
- Practice 3-color DFS

**Day 10-11**: Topological Sort
- Read Kahn's algorithm
- Solve: #23, #29
- Implement both approaches

**Day 12-13**: Union Find
- Read Union Find theory
- Solve: #6, #27, #31
- Master path compression

**Day 14-15**: Bipartite Graphs
- Read bipartite theory
- Solve: #26
- Practice graph coloring

**Week 3-4 Total**: ~12 medium problems

---

### Week 5-6: Advanced Patterns (Medium/Hard)
**Goal**: Multi-source BFS, weighted graphs, MST

**Day 16-17**: Multi-source BFS
- Read multi-source patterns
- Solve: #34, #35, #36
- Practice from multiple starts

**Day 18-19**: Shortest Path
- Read Dijkstra's algorithm
- Solve: #44, #45, #46
- Handle weighted graphs

**Day 20-21**: MST Problems
- Read Prim's and Kruskal's
- Solve: #61, #62, #63
- Practice both algorithms

**Week 5-6 Total**: ~15 medium-hard problems

---

### Week 7-8: Hard Problems & Review
**Goal**: Master complex algorithms, review all patterns

**Day 22-23**: Word Ladder & Transformations
- Solve: #51, #52
- Practice state space BFS

**Day 24-25**: Special Algorithms
- Read Tarjan's algorithm
- Solve: #54, #55
- Practice bridge finding

**Day 26-27**: Complex Grid Problems
- Solve: #66, #67, #70
- Master advanced grid techniques

**Day 28**: Full Review
- Revisit weak areas
- Solve 3-5 random problems from each difficulty
- Review all patterns

**Week 7-8 Total**: ~10 hard problems + review

---

## Must-Know Problems (Top 20)

**Foundation (5 problems):**
1. Number of Islands (#24)
2. Clone Graph (#21)
3. Course Schedule (#22)
4. Course Schedule II (#23)
5. Number of Provinces (#1)

**Core Patterns (10 problems):**
6. Pacific Atlantic Water Flow (#25)
7. Is Graph Bipartite? (#26)
8. Redundant Connection (#27)
9. Accounts Merge (#31)
10. Evaluate Division (#32)
11. Rotting Oranges (#34)
12. Shortest Path in Binary Matrix (#30)
13. Network Delay Time (#44)
14. Minimum Height Trees (#29)
15. Word Ladder (#51)

**Advanced (5 problems):**
16. Alien Dictionary (#53)
17. Critical Connections (#54)
18. Min Cost to Connect All Points (#61)
19. Shortest Path Visiting All Nodes (#57)
20. Swim in Rising Water (#70)

---

## Interview Preparation Checklist

### Before Interview

- [ ] Can implement DFS (recursive and iterative) from memory
- [ ] Can implement BFS from memory
- [ ] Can implement Union Find with optimizations
- [ ] Know both topological sort approaches
- [ ] Can detect cycles in directed and undirected graphs
- [ ] Understand when to use DFS vs BFS vs Union Find
- [ ] Know time/space complexity for all patterns
- [ ] Practiced 50+ graph problems

### During Interview

- [ ] Clarify graph properties (directed/undirected, weighted/unweighted)
- [ ] Ask about graph representation
- [ ] Identify the pattern (DFS, BFS, Union Find, etc.)
- [ ] Build adjacency list if needed
- [ ] Handle disconnected graphs
- [ ] Check for cycles if relevant
- [ ] Track visited nodes
- [ ] Test with simple example
- [ ] Discuss time/space complexity

### After Interview

- [ ] Review problems you struggled with
- [ ] Identify pattern you missed
- [ ] Practice similar problems
- [ ] Update weak areas list

---

## Summary

**Most Important Patterns:**
1. DFS/BFS traversal (60% of problems)
2. Union Find (15% of problems)
3. Topological Sort (10% of problems)
4. Shortest Path algorithms (10% of problems)
5. MST algorithms (5% of problems)

**Time Complexity Master List:**
- DFS/BFS: O(V + E)
- Union Find: O(E × α(V)) ≈ O(E)
- Topological Sort: O(V + E)
- Dijkstra: O((V + E) log V)
- Prim's/Kruskal's: O(E log E)

**Practice Strategy:**
- Weeks 1-2: Easy problems (15 problems)
- Weeks 3-4: Medium problems (12 problems)
- Weeks 5-6: Advanced medium (15 problems)
- Weeks 7-8: Hard problems (10 problems) + review
- **Total**: 50+ problems in 8 weeks

**Success Formula:**
Master patterns → Recognize problems → Apply templates → Optimize → Succeed!

Good luck with your graph mastery journey!
