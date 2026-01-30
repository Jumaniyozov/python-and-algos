# Chapter 36: Graphs

## Overview

Graphs are one of the most versatile and powerful data structures in computer science. This chapter covers fundamental graph algorithms that form the backbone of solving complex real-world problems, from social networks to navigation systems to dependency resolution.

## Learning Objectives

By the end of this chapter, you will be able to:

- Understand graph fundamentals (vertices, edges, directed vs undirected, weighted vs unweighted)
- Implement different graph representations (adjacency matrix, adjacency list, edge list)
- Master Depth-First Search (DFS) - both recursive and iterative approaches
- Master Breadth-First Search (BFS) for level-order traversal and shortest paths
- Implement topological sorting for directed acyclic graphs (DAGs)
- Detect cycles in both directed and undirected graphs
- Find connected components using DFS/BFS
- Implement Union Find (Disjoint Set) with path compression and union by rank
- Detect bipartite graphs
- Apply graph algorithms to solve complex interview problems

## Prerequisites

Before starting this chapter, you should be familiar with:

- **Trees** (Chapter 35) - Trees are special cases of graphs
- **Queues** (Chapter 28) - Essential for BFS implementation
- **Stacks** (Chapter 27) - Used in iterative DFS
- **Hash Tables** (Chapter 32) - For tracking visited nodes and building adjacency lists
- **Recursion** (Chapter 20) - For recursive DFS and backtracking

## Chapter Structure

1. **theory.md** - Comprehensive coverage of graph concepts, representations, and algorithms
2. **examples.md** - Annotated implementations of all major graph algorithms
3. **exercises.md** - 22-29 curated practice problems (Easy to Hard)
4. **solutions.md** - Detailed solutions with multiple approaches and complexity analysis
5. **tips.md** - Interview strategies, common pitfalls, and 70+ LeetCode problems

## Study Time Estimates

- **Theory**: 3-4 hours
- **Examples**: 4-5 hours
- **Exercises**: 12-16 hours
- **LeetCode Practice**: 60-80 hours (6-8 weeks)
- **Total**: 79-105 hours

## Key Concepts Overview

### Graph Representations

```python
# Adjacency List (Most Common)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

# Adjacency Matrix
graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0]
]
```

### Core Algorithms

1. **DFS (Depth-First Search)** - Explore as deep as possible before backtracking
   - Time: O(V + E), Space: O(V)
   - Applications: Cycle detection, topological sort, connected components

2. **BFS (Breadth-First Search)** - Explore level by level
   - Time: O(V + E), Space: O(V)
   - Applications: Shortest path (unweighted), level-order traversal

3. **Topological Sort** - Linear ordering of vertices in DAG
   - Kahn's Algorithm (BFS-based): O(V + E)
   - DFS-based approach: O(V + E)

4. **Union Find** - Efficiently manage disjoint sets
   - Find with path compression: O(α(n)) ≈ O(1)
   - Union by rank: O(α(n)) ≈ O(1)
   - Applications: Detecting cycles, connected components, minimum spanning tree

### Common Patterns

```python
# Pattern 1: DFS with Visited Set
def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, graph, visited)

# Pattern 2: BFS with Queue
def bfs(start, graph):
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Pattern 3: Building Adjacency List from Edges
def build_graph(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # For undirected graph
    return graph
```

## Real-World Applications

### Social Networks
- Friend recommendations (BFS for friends of friends)
- Influence propagation (DFS/BFS)
- Community detection (connected components)

### Navigation Systems
- Route finding (BFS for shortest path, Dijkstra for weighted)
- Network connectivity (Union Find)
- Traffic flow optimization

### Software Engineering
- Dependency resolution (topological sort)
- Build systems (DAG processing)
- Deadlock detection (cycle detection)

### Computer Networks
- Network topology (graph representation)
- Routing protocols (shortest path algorithms)
- Network reliability (connected components)

### Game Development
- Pathfinding (BFS, A*)
- State space exploration (DFS)
- Map generation (graph traversal)

## Why Graphs Are Important for Interviews

Graphs are among the most frequently tested topics in technical interviews because they:

1. **Test Multiple Skills**: Require knowledge of recursion, queues, stacks, and hash tables
2. **Real-World Relevance**: Model many practical problems
3. **Scalability Thinking**: Force consideration of time/space complexity
4. **Pattern Recognition**: Test ability to identify when DFS vs BFS vs Union Find
5. **Problem-Solving**: Often require creative approaches and multiple techniques

Common interview companies heavily testing graphs:
- **FAANG**: Facebook (social graphs), Amazon (logistics), Google (maps), Netflix (recommendations)
- **Tech Unicorns**: Uber (routing), Airbnb (recommendations), LinkedIn (connections)
- **Finance**: Trading networks, risk analysis

## Success Strategy

1. **Master the Fundamentals** (Week 1-2)
   - Understand graph representations thoroughly
   - Implement DFS and BFS from scratch multiple times
   - Practice building adjacency lists from edge lists

2. **Learn Core Algorithms** (Week 3-4)
   - Topological sort (both approaches)
   - Cycle detection (directed and undirected)
   - Union Find with optimizations

3. **Pattern Recognition** (Week 5-6)
   - Identify when to use DFS vs BFS
   - Recognize Union Find problems
   - Spot topological sort opportunities

4. **Advanced Problems** (Week 7-8)
   - Combine multiple techniques
   - Optimize solutions
   - Handle edge cases

## Next Steps

1. Read **theory.md** for comprehensive coverage of graph concepts
2. Study **examples.md** for annotated implementations
3. Solve problems in **exercises.md** progressively
4. Review **solutions.md** for detailed explanations
5. Follow the practice roadmap in **tips.md** (70+ LeetCode problems)

Remember: Graphs are challenging but incredibly rewarding. The key is consistent practice and pattern recognition. Start with simple DFS/BFS problems and gradually build up to complex scenarios.
