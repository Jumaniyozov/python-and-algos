# Chapter 31: Stacks and Queues

## Overview

Stacks and queues are fundamental linear data structures that control the order in which elements are accessed. Unlike arrays and linked lists which allow arbitrary access, stacks and queues enforce specific access patterns that make them ideal for many algorithmic problems.

## What You'll Learn

- Stack ADT and implementations
- Queue ADT and implementations
- Deque (double-ended queue)
- Priority Queue
- Monotonic Stack patterns
- Monotonic Queue patterns
- Real-world applications
- LeetCode-style problem solving

## Topics Covered

### Core Concepts
1. **Stack (LIFO)** - Last In, First Out
2. **Queue (FIFO)** - First In, First Out
3. **Deque** - Double-ended queue
4. **Priority Queue** - Ordered by priority
5. **Circular Queue** - Fixed-size with wrap-around

### Advanced Patterns
6. **Monotonic Stack** - Maintaining order invariant
7. **Monotonic Queue** - Sliding window optimization
8. **Stack with Min/Max** - Constant time extrema
9. **Two-Stack Queue** - Queue using stacks
10. **Expression Evaluation** - Parsing and calculation

## Prerequisites

- Arrays and Lists (Chapter 28)
- Linked Lists (Chapter 29)
- Basic time/space complexity analysis

## Files in This Chapter

- `README.md` - This file, chapter overview
- `Theory.md` - Detailed explanations and concepts
- `examples.md` - 20 complete code examples
- `exercises.md` - 20 practice problems
- `solutions.md` - Complete solutions with analysis
- `tips.md` - Patterns and best practices

## Time Investment

- Theory: 45 minutes
- Examples: 2-3 hours
- Exercises: 3-4 hours
- Review: 1 hour

**Total: 7-9 hours**

## Why This Matters

Stacks and queues appear everywhere:
- **Function calls** - Call stack
- **Undo/Redo** - Command stack
- **BFS/DFS** - Graph traversal
- **Expression parsing** - Calculators, compilers
- **Task scheduling** - Job queues
- **Browser history** - Back/forward navigation

## Learning Path

1. Read Theory.md - Understand concepts
2. Study examples.md - See implementations
3. Attempt exercises.md - Practice problems
4. Check solutions.md - Verify approaches
5. Review tips.md - Learn patterns

## Quick Reference

### Stack Operations
```python
stack = []
stack.append(x)    # Push - O(1)
stack.pop()        # Pop - O(1)
stack[-1]          # Peek - O(1)
len(stack)         # Size - O(1)
bool(stack)        # IsEmpty - O(1)
```

### Queue Operations
```python
from collections import deque
queue = deque()
queue.append(x)    # Enqueue - O(1)
queue.popleft()    # Dequeue - O(1)
queue[0]           # Front - O(1)
len(queue)         # Size - O(1)
```

### Priority Queue Operations
```python
import heapq
pq = []
heapq.heappush(pq, x)     # Insert - O(log n)
heapq.heappop(pq)         # Remove min - O(log n)
pq[0]                     # Peek min - O(1)
```

## Common Patterns

1. **Matching Pairs** - Parentheses, brackets
2. **Function Calls** - Recursion simulation
3. **Undo Operations** - Command pattern
4. **Monotonic Stack** - Next greater/smaller element
5. **Level Order** - BFS traversal
6. **Sliding Window** - Maximum in window

## Interview Frequency

- **Very Common:** Valid parentheses, min stack, daily temperatures
- **Common:** Largest rectangle, sliding window maximum
- **Moderate:** Calculator problems, design problems

## Next Steps

After mastering this chapter:
- Chapter 31: Hash Tables
- Chapter 32: Trees
- Chapter 35: Graph Algorithms

## Additional Resources

- Python `collections.deque` documentation
- Python `heapq` module documentation
- LeetCode stack/queue tag
- Visualgo stack/queue animations
