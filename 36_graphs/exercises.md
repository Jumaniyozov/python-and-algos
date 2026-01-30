# Chapter 36: Graphs - Exercises

## Instructions

- Try to solve each problem without looking at the solution first
- Start with Easy problems, then progress to Medium and Hard
- For each problem, analyze the time and space complexity
- Multiple approaches are encouraged - compare DFS vs BFS vs Union Find

Solutions are available in `solutions.md`.

---

## Easy Problems

### E1: Number of Provinces

Given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if cities i and j are directly connected, and `isConnected[i][j] = 0` otherwise. Find the total number of provinces (connected components).

```python
def find_circle_num(is_connected: List[List[int]]) -> int:
    """
    Find number of provinces (connected components).

    Example:
        Input: isConnected = [[1,1,0],
                              [1,1,0],
                              [0,0,1]]
        Output: 2
        Explanation: Cities 0 and 1 are connected, city 2 is separate.

    Args:
        is_connected: n x n adjacency matrix

    Returns:
        Number of provinces
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/number-of-provinces/

---

### E2: Find if Path Exists in Graph

Given a bi-directional graph with `n` vertices and a list of edges, determine if there is a valid path from `source` to `destination`.

```python
def valid_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    Check if path exists from source to destination.

    Example:
        Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
        Output: True

    Args:
        n: Number of vertices (0 to n-1)
        edges: List of edges [u, v]
        source: Source vertex
        destination: Destination vertex

    Returns:
        True if path exists, False otherwise
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/find-if-path-exists-in-graph/

---

### E3: Find Center of Star Graph

A star graph is a graph where there is a center node connected to all other nodes. Find the center node.

```python
def find_center(edges: List[List[int]]) -> int:
    """
    Find center of star graph.

    Example:
        Input: edges = [[1,2],[2,3],[4,2]]
        Output: 2
        Explanation: Node 2 is connected to all other nodes.

    Args:
        edges: List of edges [u, v]

    Returns:
        Center node
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/find-center-of-star-graph/

---

### E4: Find the Town Judge

In a town, there is a person labeled as the town judge. The town judge trusts nobody, and everybody trusts the town judge. Find the town judge.

```python
def find_judge(n: int, trust: List[List[int]]) -> int:
    """
    Find the town judge.

    Example:
        Input: n = 3, trust = [[1,3],[2,3]]
        Output: 3
        Explanation: Person 3 is trusted by 1 and 2, and trusts nobody.

    Args:
        n: Number of people (1 to n)
        trust: List of [a, b] meaning a trusts b

    Returns:
        Label of town judge, or -1 if none exists
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/find-the-town-judge/

---

### E5: All Paths From Source to Target

Given a directed acyclic graph (DAG) of `n` nodes labeled from 0 to n-1, find all possible paths from node 0 to node n-1.

```python
def all_paths_source_target(graph: List[List[int]]) -> List[List[int]]:
    """
    Find all paths from source (0) to target (n-1).

    Example:
        Input: graph = [[1,2],[3],[3],[]]
        Output: [[0,1,3],[0,2,3]]
        Explanation: Paths from 0 to 3 are [0,1,3] and [0,2,3].

    Args:
        graph: Adjacency list (graph[i] = neighbors of node i)

    Returns:
        List of all paths from 0 to n-1
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/all-paths-from-source-to-target/

---

### E6: Number of Connected Components in an Undirected Graph

Given `n` nodes and a list of edges, find the number of connected components.

```python
def count_components(n: int, edges: List[List[int]]) -> int:
    """
    Count connected components in undirected graph.

    Example:
        Input: n = 5, edges = [[0,1],[1,2],[3,4]]
        Output: 2
        Explanation: Components are {0,1,2} and {3,4}

    Args:
        n: Number of nodes
        edges: List of edges [u, v]

    Returns:
        Number of connected components
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/ (Premium)

---

### E7: Graph Valid Tree

Given `n` nodes and a list of edges, determine if the edges form a valid tree.

```python
def valid_tree(n: int, edges: List[List[int]]) -> bool:
    """
    Check if graph forms a valid tree.

    A valid tree must be:
    - Connected (single component)
    - Acyclic (no cycles)
    - Has exactly n-1 edges

    Example:
        Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
        Output: True

    Args:
        n: Number of nodes
        edges: List of edges [u, v]

    Returns:
        True if forms valid tree, False otherwise
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/graph-valid-tree/ (Premium)

---

## Medium Problems

### M1: Clone Graph

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: 'Node') -> 'Node':
    """
    Clone an undirected graph.

    Example:
        Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
        Output: [[2,4],[1,3],[2,4],[1,3]]

    Args:
        node: Reference node in original graph

    Returns:
        Reference to cloned graph
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/clone-graph/

---

### M2: Course Schedule

There are `n` courses, some with prerequisites. Determine if you can finish all courses.

```python
def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Check if all courses can be completed (detect cycle in directed graph).

    Example:
        Input: numCourses = 2, prerequisites = [[1,0]]
        Output: True
        Explanation: Take course 0, then course 1.

    Args:
        num_courses: Number of courses (0 to numCourses-1)
        prerequisites: [a, b] means course a requires course b

    Returns:
        True if can finish all courses, False otherwise
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/course-schedule/

---

### M3: Course Schedule II

Return the ordering of courses you should take to finish all courses.

```python
def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Find course order (topological sort).

    Example:
        Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        Output: [0,2,1,3] or [0,1,2,3]

    Args:
        num_courses: Number of courses
        prerequisites: [a, b] means course a requires course b

    Returns:
        Course order, or empty list if impossible
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/course-schedule-ii/

---

### M4: Pacific Atlantic Water Flow

Given an `m x n` grid representing island heights, find all cells where water can flow to both the Pacific (top/left) and Atlantic (bottom/right) oceans.

```python
def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    """
    Find cells that can reach both oceans.

    Water flows from higher to equal or lower elevation.

    Example:
        Input: heights = [[1,2,2,3,5],
                          [3,2,3,4,4],
                          [2,4,5,3,1],
                          [6,7,1,4,5],
                          [5,1,1,2,4]]
        Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    Args:
        heights: m x n grid of heights

    Returns:
        List of [row, col] coordinates
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/pacific-atlantic-water-flow/

---

### M5: Number of Islands

Given a 2D grid of '1's (land) and '0's (water), count the number of islands.

```python
def num_islands(grid: List[List[str]]) -> int:
    """
    Count number of islands (connected components of 1's).

    Example:
        Input: grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        Output: 3

    Args:
        grid: m x n grid of '1's and '0's

    Returns:
        Number of islands
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/number-of-islands/

---

### M6: Surrounded Regions

Given an `m x n` matrix with 'X' and 'O', capture all regions that are surrounded by 'X'.

```python
def solve(board: List[List[str]]) -> None:
    """
    Capture surrounded regions (modify in-place).

    Captured regions: 'O' regions completely surrounded by 'X'.
    Border 'O's and connected 'O's are not captured.

    Example:
        Input: board = [["X","X","X","X"],
                        ["X","O","O","X"],
                        ["X","X","O","X"],
                        ["X","O","X","X"]]
        Output: [["X","X","X","X"],
                 ["X","X","X","X"],
                 ["X","X","X","X"],
                 ["X","O","X","X"]]

    Args:
        board: m x n grid (modified in-place)
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/surrounded-regions/

---

### M7: Is Graph Bipartite?

Determine if an undirected graph is bipartite (can be colored with 2 colors).

```python
def is_bipartite(graph: List[List[int]]) -> bool:
    """
    Check if graph is bipartite.

    Example:
        Input: graph = [[1,3],[0,2],[1,3],[0,2]]
        Output: True
        Explanation: Can color with 2 colors: {0,2} and {1,3}

    Args:
        graph: Adjacency list

    Returns:
        True if bipartite, False otherwise
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/is-graph-bipartite/

---

### M8: Redundant Connection

Given a graph that started as a tree with n nodes, but one edge was added. Find the edge that when removed makes it a tree again.

```python
def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    """
    Find redundant edge that creates a cycle.

    Example:
        Input: edges = [[1,2],[1,3],[2,3]]
        Output: [2,3]

    Args:
        edges: List of edges [u, v] added in order

    Returns:
        The last edge that creates a cycle
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/redundant-connection/

---

### M9: Keys and Rooms

There are `n` rooms and you start in room 0. Each room has keys to other rooms. Can you visit all rooms?

```python
def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    """
    Check if all rooms can be visited.

    Example:
        Input: rooms = [[1],[2],[3],[]]
        Output: True
        Explanation: Start in room 0, get key to room 1,
                     then key to room 2, then key to room 3.

    Args:
        rooms: rooms[i] = list of keys in room i

    Returns:
        True if all rooms can be visited, False otherwise
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/keys-and-rooms/

---

### M10: Minimum Height Trees

Given a tree with `n` nodes, find all root nodes that result in minimum height trees.

```python
def find_min_height_trees(n: int, edges: List[List[int]]) -> List[int]:
    """
    Find roots that create minimum height trees.

    Example:
        Input: n = 4, edges = [[1,0],[1,2],[1,3]]
        Output: [1]
        Explanation: Node 1 as root gives minimum height.

    Args:
        n: Number of nodes
        edges: List of edges [u, v]

    Returns:
        List of root nodes that create MHTs
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/minimum-height-trees/

---

### M11: Accounts Merge

Given a list of accounts where each account has a name and list of emails, merge accounts belonging to the same person.

```python
def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    """
    Merge accounts with common emails.

    Example:
        Input: accounts = [["John","john@mail.com","john_work@mail.com"],
                          ["John","john@mail.com","john_home@mail.com"],
                          ["Mary","mary@mail.com"]]
        Output: [["John","john@mail.com","john_home@mail.com","john_work@mail.com"],
                 ["Mary","mary@mail.com"]]

    Args:
        accounts: List of [name, email1, email2, ...]

    Returns:
        Merged accounts with emails sorted
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/accounts-merge/

---

### M12: Evaluate Division

Given equations like `a / b = 2.0`, `b / c = 3.0`, evaluate queries like `a / c`.

```python
def calc_equation(equations: List[List[str]], values: List[float],
                  queries: List[List[str]]) -> List[float]:
    """
    Evaluate division queries using graph.

    Example:
        Input: equations = [["a","b"],["b","c"]],
               values = [2.0,3.0],
               queries = [["a","c"],["b","a"],["a","e"]]
        Output: [6.0,0.5,-1.0]
        Explanation: a/b=2.0, b/c=3.0, so a/c=6.0, b/a=0.5, a/e=undefined

    Args:
        equations: List of [dividend, divisor]
        values: Corresponding division results
        queries: List of queries to evaluate

    Returns:
        Query results, -1.0 for undefined
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/evaluate-division/

---

## Hard Problems

### H1: Word Ladder

Given two words and a dictionary, find the length of shortest transformation sequence from `beginWord` to `endWord`, changing one letter at a time.

```python
def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """
    Find shortest word transformation sequence.

    Example:
        Input: beginWord = "hit", endWord = "cog",
               wordList = ["hot","dot","dog","lot","log","cog"]
        Output: 5
        Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog"

    Args:
        begin_word: Starting word
        end_word: Target word
        word_list: List of valid words

    Returns:
        Length of shortest sequence, 0 if impossible
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/word-ladder/

---

### H2: Alien Dictionary

Given a sorted dictionary in an alien language, find the order of characters.

```python
def alien_order(words: List[str]) -> str:
    """
    Find alien alphabet order (topological sort).

    Example:
        Input: words = ["wrt","wrf","er","ett","rftt"]
        Output: "wertf"
        Explanation: Order is w < e < r < t < f

    Args:
        words: Sorted list of alien words

    Returns:
        Alien alphabet order, empty string if invalid
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/alien-dictionary/ (Premium)

---

### H3: Critical Connections in a Network

Find all critical connections (bridges) in a network. A critical connection is an edge whose removal disconnects the network.

```python
def critical_connections(n: int, connections: List[List[int]]) -> List[List[int]]:
    """
    Find all bridges in undirected graph.

    Example:
        Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
        Output: [[1,3]]
        Explanation: Removing [1,3] disconnects node 3.

    Args:
        n: Number of servers
        connections: List of connections [u, v]

    Returns:
        List of critical connections
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/critical-connections-in-a-network/

---

### H4: Minimum Number of Days to Disconnect Island

Given a 2D grid, find the minimum number of days to disconnect the island by changing land to water.

```python
def min_days(grid: List[List[int]]) -> int:
    """
    Minimum days to disconnect island.

    Each day you can change one land cell to water.

    Example:
        Input: grid = [[1,1,0],
                       [1,1,1],
                       [0,1,0]]
        Output: 2
        Explanation: Change cells to disconnect island.

    Args:
        grid: m x n grid with 1 (land) and 0 (water)

    Returns:
        Minimum number of days (0, 1, or 2)
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

---

### H5: Minimum Cost to Connect All Points

Given points on a 2D plane, find the minimum cost to connect all points where cost is the Manhattan distance.

```python
def min_cost_connect_points(points: List[List[int]]) -> int:
    """
    Find minimum cost to connect all points (Minimum Spanning Tree).

    Cost between two points = |x1-x2| + |y1-y2|

    Example:
        Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        Output: 20

    Args:
        points: List of [x, y] coordinates

    Returns:
        Minimum cost to connect all points
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/min-cost-to-connect-all-points/

---

### H6: Number of Islands II

Given an `m x n` grid initially filled with water, islands are added one by one. After each addition, return the number of islands.

```python
def num_islands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    """
    Count islands after each land addition (Union Find).

    Example:
        Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
        Output: [1,1,2,3]

    Args:
        m: Number of rows
        n: Number of columns
        positions: Land positions added in order

    Returns:
        Island count after each addition
    """
    pass
```

**LeetCode**: https://leetcode.com/problems/number-of-islands-ii/ (Premium)

---

## Summary

**Problem Distribution:**
- **Easy (7)**: Basic graph traversal, connectivity, simple DFS/BFS
- **Medium (12)**: Cycle detection, topological sort, bipartite, Union Find, complex DFS/BFS
- **Hard (6)**: Bridges, MST, advanced topological sort, optimization

**Key Patterns:**
- **DFS**: Path finding, cycle detection, connectivity
- **BFS**: Shortest path, level-order, transformations
- **Union Find**: Dynamic connectivity, connected components
- **Topological Sort**: Dependency resolution, course scheduling
- **Bipartite**: Graph coloring, two-set problems
- **Grid as Graph**: Islands, regions, flow problems

**Time Complexity Guide:**
- DFS/BFS: O(V + E)
- Union Find: O(E × α(V)) ≈ O(E)
- Topological Sort: O(V + E)

Practice these problems to master graph algorithms!
