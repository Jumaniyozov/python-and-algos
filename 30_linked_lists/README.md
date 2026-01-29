# Chapter 30: Linked Lists

## Overview

Linked lists are fundamental linear data structures where elements are stored in nodes, and each node points to the next node in the sequence. Unlike arrays, linked lists don't require contiguous memory allocation, making them efficient for insertions and deletions.

## What You'll Learn

- **Singly Linked Lists**: Nodes with single forward pointers
- **Doubly Linked Lists**: Nodes with forward and backward pointers
- **Circular Linked Lists**: Last node points back to first node
- **Two Pointer Techniques**: Fast/slow pointers, runner technique
- **Advanced Patterns**: Cycle detection, reversal, merging

## Structure

1. **Theory.md** - Complete theoretical foundations
   - Types of linked lists
   - Operations and complexity
   - Common patterns and techniques

2. **Examples.md** - 20+ complete, runnable examples
   - Basic operations
   - Classic problems (reverse, cycle detection, merge)
   - Advanced algorithms (LRU cache, flatten nested lists)

3. **Exercises.md** - 20 LeetCode-style problems
   - Easy, medium, and hard difficulty levels
   - Covers all important patterns

4. **Solutions.md** - Complete solutions with:
   - Multiple approaches
   - Complexity analysis
   - Visual diagrams
   - Edge cases

5. **Tips.md** - Practical patterns and common mistakes

## Key Concepts

### Why Linked Lists?

- **Dynamic Size**: No need to specify size upfront
- **Efficient Insertion/Deletion**: O(1) when you have the node reference
- **No Wasted Memory**: Allocate exactly what you need
- **Foundation for Other Structures**: Used in stacks, queues, graphs

### When to Use Linked Lists

✅ **Use when:**
- Frequent insertions/deletions at beginning or middle
- Don't know size in advance
- Don't need random access
- Implementing stacks, queues, or LRU caches

❌ **Avoid when:**
- Need fast random access (use arrays)
- Memory overhead is critical (pointers take extra space)
- Cache performance matters (arrays have better locality)

## Common Patterns

1. **Two Pointers**: Fast and slow pointers for cycle detection, finding middle
2. **Dummy Head**: Simplify edge cases for insertion/deletion
3. **Recursion**: Natural fit for many linked list problems
4. **Reversal**: Iterative and recursive approaches
5. **Runner Technique**: One pointer moves faster than another

## Complexity Quick Reference

| Operation | Singly Linked List | Doubly Linked List | Array |
|-----------|-------------------|-------------------|-------|
| Access | O(n) | O(n) | O(1) |
| Search | O(n) | O(n) | O(n) |
| Insert (at head) | O(1) | O(1) | O(n) |
| Insert (at tail) | O(n) or O(1)* | O(1) | O(1) or O(n)** |
| Insert (at position) | O(n) | O(n) | O(n) |
| Delete (at head) | O(1) | O(1) | O(n) |
| Delete (at tail) | O(n) | O(1) | O(1) |
| Delete (given node) | O(1)*** | O(1) | O(n) |

\* O(1) if maintaining tail pointer
\*\* O(n) if dynamic array needs resizing
\*\*\* O(1) only if you have reference to previous node

## Getting Started

Start with **Theory.md** to understand the fundamentals, then work through **Examples.md** to see implementations in action. Practice with **Exercises.md** and verify your solutions against **Solutions.md**.

## Prerequisites

- Basic Python knowledge
- Understanding of pointers/references
- Recursion concepts (helpful but not required)

## Practice Strategy

1. Master basic operations (insert, delete, traverse)
2. Learn two-pointer techniques
3. Practice reversal problems
4. Understand cycle detection
5. Solve merge and intersection problems
6. Tackle advanced problems (LRU cache, nested lists)

Happy coding!
