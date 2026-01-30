# Chapter 36: Graphs - Solutions

This file provides detailed solutions to all exercises with multiple approaches, complexity analysis, and explanations.

## Table of Contents
- [Easy Problems](#easy-problems)
- [Medium Problems](#medium-problems)
- [Hard Problems](#hard-problems)

---

## Easy Problems

### E1: Number of Provinces

**Problem**: Count connected components in adjacency matrix.

**Approach 1: DFS**

```python
def findCircleNum(isConnected):
    """
    Time: O(n²) - visit all cells
    Space: O(n) - visited set + recursion
    """
    n = len(isConnected)
    visited = set()

    def dfs(city):
        visited.add(city)
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and neighbor not in visited:
                dfs(neighbor)

    provinces = 0
    for city in range(n):
        if city not in visited:
            dfs(city)
            provinces += 1

    return provinces
```

**Approach 2: Union Find**

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.count -= 1

def findCircleNum(isConnected):
    """
    Time: O(n² × α(n))
    Space: O(n)
    """
    n = len(isConnected)
    uf = UnionFind(n)

    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                uf.union(i, j)

    return uf.count
```

---

### E2: Find if Path Exists in Graph

**Approach: BFS**

```python
from collections import deque, defaultdict

def validPath(n, edges, source, destination):
    """
    Time: O(V + E)
    Space: O(V + E)
    """
    if source == destination:
        return True

    # Build graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # BFS
    visited = {source}
    queue = deque([source])

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

---

### E3: Find Center of Star Graph

**Approach: Check First Two Edges**

```python
def findCenter(edges):
    """
    Center must appear in every edge.
    Check first two edges - common node is center.

    Time: O(1)
    Space: O(1)
    """
    # Center must be in both first and second edge
    if edges[0][0] in edges[1]:
        return edges[0][0]
    return edges[0][1]
```

---

### E4: Find the Town Judge

**Approach: In-degree and Out-degree**

```python
def findJudge(n, trust):
    """
    Judge: in-degree = n-1, out-degree = 0

    Time: O(T) where T is trust relationships
    Space: O(n)
    """
    if n == 1 and not trust:
        return 1

    # Count trust: positive for trusted, negative for trusting
    trust_count = [0] * (n + 1)

    for a, b in trust:
        trust_count[a] -= 1  # a trusts someone
        trust_count[b] += 1  # b is trusted

    for person in range(1, n + 1):
        if trust_count[person] == n - 1:
            return person

    return -1
```

---

### E5: All Paths From Source to Target

**Approach: DFS with Backtracking**

```python
def allPathsSourceTarget(graph):
    """
    Time: O(2^n × n) - exponential paths
    Space: O(n) - recursion depth
    """
    n = len(graph)
    target = n - 1
    result = []

    def dfs(node, path):
        if node == target:
            result.append(path + [node])
            return

        for neighbor in graph[node]:
            dfs(neighbor, path + [node])

    dfs(0, [])
    return result
```

---

### E6: Number of Connected Components

**Approach: Union Find**

```python
def countComponents(n, edges):
    """
    Time: O(E × α(n))
    Space: O(n)
    """
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1
        return True

    components = n
    for u, v in edges:
        if union(u, v):
            components -= 1

    return components
```

---

### E7: Graph Valid Tree

**Approach: Union Find + Validation**

```python
def validTree(n, edges):
    """
    Valid tree must have exactly n-1 edges, be connected, and have no cycles.

    Time: O(E × α(n))
    Space: O(n)
    """
    # Tree must have exactly n-1 edges
    if len(edges) != n - 1:
        return False

    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False  # Cycle detected
        parent[px] = py
        return True

    for u, v in edges:
        if not union(u, v):
            return False  # Cycle found

    return True  # n-1 edges, no cycles = valid tree
```

---

## Medium Problems

### M1: Clone Graph

**Approach: DFS with HashMap**

```python
def cloneGraph(node):
    """
    Time: O(V + E)
    Space: O(V)
    """
    if not node:
        return None

    # Map original to cloned nodes
    cloned = {}

    def dfs(original):
        if original in cloned:
            return cloned[original]

        # Create clone
        clone = Node(original.val)
        cloned[original] = clone

        # Clone neighbors
        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)
```

---

### M2: Course Schedule

**Approach: Detect Cycle in Directed Graph**

```python
from collections import defaultdict

def canFinish(numCourses, prerequisites):
    """
    Time: O(V + E)
    Space: O(V)
    """
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    # 0: unvisited, 1: visiting, 2: visited
    state = [0] * numCourses

    def has_cycle(course):
        if state[course] == 1:
            return True  # Cycle detected
        if state[course] == 2:
            return False  # Already processed

        state[course] = 1  # Mark as visiting
        for prereq in graph[course]:
            if has_cycle(prereq):
                return True
        state[course] = 2  # Mark as visited
        return False

    for course in range(numCourses):
        if has_cycle(course):
            return False

    return True
```

---

### M3: Course Schedule II

**Approach: Topological Sort (Kahn's Algorithm)**

```python
from collections import deque, defaultdict

def findOrder(numCourses, prerequisites):
    """
    Time: O(V + E)
    Space: O(V + E)
    """
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Add courses with no prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    result = []

    while queue:
        course = queue.popleft()
        result.append(course)

        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    return result if len(result) == numCourses else []
```

---

### M4: Pacific Atlantic Water Flow

**Approach: Reverse DFS from Oceans**

```python
def pacificAtlantic(heights):
    """
    Time: O(m × n)
    Space: O(m × n)
    """
    if not heights:
        return []

    m, n = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(r, c, visited):
        visited.add((r, c))
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited
                and heights[nr][nc] >= heights[r][c]):
                dfs(nr, nc, visited)

    # Start from Pacific (top and left)
    for i in range(m):
        dfs(i, 0, pacific)
    for j in range(n):
        dfs(0, j, pacific)

    # Start from Atlantic (bottom and right)
    for i in range(m):
        dfs(i, n-1, atlantic)
    for j in range(n):
        dfs(m-1, j, atlantic)

    # Find intersection
    return list(pacific & atlantic)
```

---

### M5: Number of Islands

**Approach: DFS**

```python
def numIslands(grid):
    """
    Time: O(m × n)
    Space: O(m × n) worst case for recursion
    """
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return

        grid[r][c] = '0'  # Mark as visited

        # Explore 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(m):
        for c in range(n):
            if grid[r][c] == '1':
                dfs(r, c)
                islands += 1

    return islands
```

---

### M6: Surrounded Regions

**Approach: DFS from Borders**

```python
def solve(board):
    """
    Time: O(m × n)
    Space: O(m × n)
    """
    if not board:
        return

    m, n = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
            return
        board[r][c] = 'T'  # Mark as temporary
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    # Mark border-connected 'O's as 'T'
    for i in range(m):
        dfs(i, 0)
        dfs(i, n-1)
    for j in range(n):
        dfs(0, j)
        dfs(m-1, j)

    # Flip surrounded 'O' to 'X', restore 'T' to 'O'
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'T':
                board[i][j] = 'O'
```

---

### M7: Is Graph Bipartite?

**Approach: BFS with Coloring**

```python
from collections import deque

def isBipartite(graph):
    """
    Time: O(V + E)
    Space: O(V)
    """
    n = len(graph)
    color = [-1] * n  # -1: uncolored, 0/1: two colors

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

---

### M8: Redundant Connection

**Approach: Union Find**

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

def findRedundantConnection(edges):
    """
    Time: O(E × α(V))
    Space: O(V)
    """
    uf = UnionFind(len(edges))

    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]

    return []
```

---

### M9: Keys and Rooms

**Approach: DFS/BFS**

```python
def canVisitAllRooms(rooms):
    """
    Time: O(n + k) where k is total keys
    Space: O(n)
    """
    visited = set([0])
    stack = [0]

    while stack:
        room = stack.pop()
        for key in rooms[room]:
            if key not in visited:
                visited.add(key)
                stack.append(key)

    return len(visited) == len(rooms)
```

---

### M10: Minimum Height Trees

**Approach: Trim Leaves Layer by Layer**

```python
from collections import deque, defaultdict

def findMinHeightTrees(n, edges):
    """
    Time: O(n)
    Space: O(n)
    """
    if n == 1:
        return [0]

    # Build adjacency list
    graph = defaultdict(list)
    degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # Start with leaves (degree 1)
    queue = deque([i for i in range(n) if degree[i] == 1])
    remaining = n

    # Trim leaves layer by layer
    while remaining > 2:
        size = len(queue)
        remaining -= size

        for _ in range(size):
            leaf = queue.popleft()
            for neighbor in graph[leaf]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    queue.append(neighbor)

    return list(queue)
```

---

### M11: Accounts Merge

**Approach: Union Find with Email Mapping**

```python
from collections import defaultdict

def accountsMerge(accounts):
    """
    Time: O(n × k × α(n)) where k is avg emails per account
    Space: O(n × k)
    """
    parent = {}

    def find(x):
        if x not in parent:
            parent[x] = x
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    # Map email to name
    email_to_name = {}

    # Union emails in same account
    for account in accounts:
        name = account[0]
        first_email = account[1]

        for email in account[1:]:
            email_to_name[email] = name
            union(email, first_email)

    # Group emails by root
    groups = defaultdict(list)
    for email in email_to_name:
        groups[find(email)].append(email)

    # Format result
    result = []
    for emails in groups.values():
        result.append([email_to_name[emails[0]]] + sorted(emails))

    return result
```

---

### M12: Evaluate Division

**Approach: Build Weighted Graph and DFS**

```python
from collections import defaultdict

def calcEquation(equations, values, queries):
    """
    Time: O(Q × (V + E)) for Q queries
    Space: O(V + E)
    """
    # Build graph: a/b = 2.0 means a->b with weight 2.0, b->a with weight 0.5
    graph = defaultdict(dict)

    for (a, b), value in zip(equations, values):
        graph[a][b] = value
        graph[b][a] = 1.0 / value

    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0

        visited.add(start)

        for neighbor in graph[start]:
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return graph[start][neighbor] * result

        return -1.0

    results = []
    for dividend, divisor in queries:
        results.append(dfs(dividend, divisor, set()))

    return results
```

---

## Hard Problems

### H1: Word Ladder

**Approach: BFS**

```python
from collections import deque

def ladderLength(beginWord, endWord, wordList):
    """
    Time: O(M² × N) where M is word length, N is word list size
    Space: O(M × N)
    """
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    queue = deque([(beginWord, 1)])
    visited = {beginWord}

    while queue:
        word, steps = queue.popleft()

        if word == endWord:
            return steps

        # Try all possible one-letter changes
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]

                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, steps + 1))

    return 0
```

---

### H2: Alien Dictionary

**Approach: Topological Sort**

```python
from collections import defaultdict, deque

def alienOrder(words):
    """
    Time: O(C) where C is total characters
    Space: O(1) for alphabet, O(C) for graph
    """
    # Initialize graph
    graph = defaultdict(set)
    in_degree = {c: 0 for word in words for c in word}

    # Build graph from adjacent words
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))

        # Invalid: word1 is prefix but longer
        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""

        # Find first different character
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break

    # Kahn's algorithm
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = []

    while queue:
        char = queue.popleft()
        result.append(char)

        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ''.join(result) if len(result) == len(in_degree) else ""
```

---

### H3: Critical Connections in a Network

**Approach: Tarjan's Algorithm**

```python
from collections import defaultdict

def criticalConnections(n, connections):
    """
    Time: O(V + E)
    Space: O(V + E)
    """
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    discovery = [-1] * n
    low = [-1] * n
    time = [0]
    bridges = []

    def dfs(node, parent):
        discovery[node] = low[node] = time[0]
        time[0] += 1

        for neighbor in graph[node]:
            if neighbor == parent:
                continue

            if discovery[neighbor] == -1:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])

                # Bridge condition
                if low[neighbor] > discovery[node]:
                    bridges.append([node, neighbor])
            else:
                low[node] = min(low[node], discovery[neighbor])

    dfs(0, -1)
    return bridges
```

---

### H5: Minimum Cost to Connect All Points

**Approach: Prim's Algorithm (MST)**

```python
import heapq

def minCostConnectPoints(points):
    """
    Time: O(n² log n)
    Space: O(n²)
    """
    n = len(points)

    def manhattan(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    # Start from point 0
    visited = set([0])
    min_heap = []

    # Add all edges from point 0
    for i in range(1, n):
        cost = manhattan(points[0], points[i])
        heapq.heappush(min_heap, (cost, i))

    total_cost = 0

    while len(visited) < n:
        cost, point = heapq.heappop(min_heap)

        if point in visited:
            continue

        visited.add(point)
        total_cost += cost

        # Add edges from new point
        for i in range(n):
            if i not in visited:
                new_cost = manhattan(points[point], points[i])
                heapq.heappush(min_heap, (new_cost, i))

    return total_cost
```

---

## Key Takeaways

**Pattern Summary:**

1. **DFS Patterns**:
   - Path finding: Recursive with path tracking
   - Cycle detection: Use visiting/visited states
   - Connected components: Count DFS starts

2. **BFS Patterns**:
   - Shortest path: Use queue with distance/level
   - Level-order: Track level explicitly
   - Transformations: State space exploration

3. **Union Find Patterns**:
   - Dynamic connectivity: Union edges, check cycles
   - Connected components: Count after all unions
   - Redundant connections: Find edge creating cycle

4. **Topological Sort Patterns**:
   - Kahn's Algorithm: BFS with in-degrees
   - DFS-based: Post-order traversal, reverse result
   - Cycle detection: If not all nodes processed

**Complexity Guidelines:**
- DFS/BFS: O(V + E) time, O(V) space
- Union Find: O(E × α(V)) ≈ O(E) time, O(V) space
- Grid DFS/BFS: O(m × n) time and space

**Common Mistakes:**
- Forgetting to mark nodes as visited (infinite loop)
- Not handling disconnected graphs (check all components)
- Confusing directed vs undirected graphs
- Not converting edge list to adjacency list first
- Forgetting base cases in recursion

Practice these solutions and understand the patterns!
