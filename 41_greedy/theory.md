# Chapter 41: Greedy Algorithms - Theory

## Table of Contents
1. [Introduction to Greedy Algorithms](#introduction-to-greedy-algorithms)
2. [Greedy Choice Property](#greedy-choice-property)
3. [Optimal Substructure](#optimal-substructure)
4. [When Greedy Works](#when-greedy-works)
5. [Classic Greedy Algorithms](#classic-greedy-algorithms)
6. [Proving Correctness](#proving-correctness)
7. [Greedy vs Dynamic Programming](#greedy-vs-dynamic-programming)

---

## Introduction to Greedy Algorithms

A **greedy algorithm** builds up a solution piece by piece, always choosing the next piece that offers the most immediate benefit (locally optimal choice).

### Key Characteristics

1. **Local optimization**: Make best choice at each step
2. **No backtracking**: Once choice made, never reconsidered
3. **Hope for global optimum**: Local choices lead to globally optimal solution

### Simple Example: Making Change

```python
def make_change_greedy(amount, coins=[25, 10, 5, 1]):
    """
    Greedy change-making (works for US coins).
    Always take largest coin that fits.
    """
    coins.sort(reverse=True)
    result = []

    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin

    return result

# Example: 63 cents
# Takes 25, 25, 10, 1, 1, 1 = 6 coins (optimal!)
print(make_change_greedy(63))  # [25, 25, 10, 1, 1, 1]
```

**Note**: Greedy change-making only works for certain coin systems (like US coins). For arbitrary coins, need dynamic programming.

---

## Greedy Choice Property

**Definition**: A globally optimal solution can be arrived at by making locally optimal (greedy) choices.

### Requirements

1. **Safety**: Greedy choice is always safe (never prevents optimal solution)
2. **Irreversibility**: Once made, choice never needs to be reconsidered

### Example: Activity Selection

**Problem**: Select maximum number of non-overlapping activities.

**Greedy choice**: Always pick activity that ends earliest.

**Why it works**: Picking earliest-ending activity leaves most room for future activities.

```python
def activity_selection(activities):
    """
    Select maximum non-overlapping activities.

    Greedy choice: Always pick activity ending earliest.

    Time: O(n log n)
    Space: O(1)
    """
    # Sort by end time
    activities.sort(key=lambda x: x[1])

    selected = [activities[0]]
    last_end = activities[0][1]

    for start, end in activities[1:]:
        if start >= last_end:  # Non-overlapping
            selected.append((start, end))
            last_end = end

    return selected

# Example
activities = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11)]
result = activity_selection(activities)
# Output: [(1,4), (5,7), (8,11)] - maximum 3 non-overlapping
```

---

## Optimal Substructure

**Definition**: An optimal solution contains optimal solutions to subproblems.

After making greedy choice, remaining subproblem has same form.

### Example: Fractional Knapsack

```python
def fractional_knapsack(capacity, items):
    """
    Maximize value in knapsack (can take fractions).

    Greedy choice: Take items by highest value/weight ratio.

    Args:
        capacity: Knapsack capacity
        items: List of (weight, value) tuples

    Returns:
        Maximum value achievable

    Time: O(n log n)
    Space: O(1)
    """
    # Sort by value/weight ratio (descending)
    items.sort(key=lambda x: x[1]/x[0], reverse=True)

    total_value = 0
    remaining_capacity = capacity

    for weight, value in items:
        if remaining_capacity >= weight:
            # Take whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            break

    return total_value

# Example
items = [(10, 60), (20, 100), (30, 120)]  # (weight, value)
capacity = 50
print(fractional_knapsack(capacity, items))  # 240.0
```

---

## When Greedy Works

### Common Indicators

✅ **Greedy likely works:**
- Sorting solves or simplifies problem
- "Maximum number of..." problems
- Interval/scheduling problems
- Always choosing min/max works intuitively

❌ **Greedy likely fails:**
- Need to consider all possibilities
- Overlapping subproblems
- Counterexample exists where greedy fails
- 0/1 choices (e.g., 0/1 knapsack)

---

## Classic Greedy Algorithms

### 1. Interval Scheduling

```python
def max_non_overlapping_intervals(intervals):
    """
    Time: O(n log n)
    Space: O(1)
    """
    intervals.sort(key=lambda x: x[1])  # Sort by end time

    count = 1
    last_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= last_end:
            count += 1
            last_end = end

    return count
```

### 2. Meeting Rooms

```python
import heapq

def min_meeting_rooms(intervals):
    """
    Find minimum rooms needed.

    Time: O(n log n)
    Space: O(n)
    """
    intervals.sort(key=lambda x: x[0])  # Sort by start time

    rooms = []  # Min-heap of end times
    heapq.heappush(rooms, intervals[0][1])

    for start, end in intervals[1:]:
        if start >= rooms[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)

    return len(rooms)
```

### 3. Jump Game

```python
def can_jump(nums):
    """
    Check if can reach last index.

    Time: O(n)
    Space: O(1)
    """
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False

        max_reach = max(max_reach, i + nums[i])

        if max_reach >= len(nums) - 1:
            return True

    return False
```

### 4. Gas Station Circuit

```python
def can_complete_circuit(gas, cost):
    """
    Find starting station to complete circuit.

    Returns starting index, or -1 if impossible.

    Time: O(n)
    Space: O(1)
    """
    total_surplus = 0
    current_surplus = 0
    start = 0

    for i in range(len(gas)):
        surplus = gas[i] - cost[i]
        total_surplus += surplus
        current_surplus += surplus

        if current_surplus < 0:
            start = i + 1
            current_surplus = 0

    return start if total_surplus >= 0 else -1
```

---

## Proving Correctness

### Exchange Argument (Greedy Stays Ahead)

**Template for proving greedy correctness:**

1. **Assume** optimal solution O exists, different from greedy G
2. **Find first difference** where G and O make different choices
3. **Exchange** O's choice with G's choice
4. **Show** new solution O' is at least as good as O
5. **Repeat** until O becomes G, proving G is optimal

### Example: Activity Selection Proof

**Claim**: Greedy (selecting earliest-ending activity) is optimal.

**Proof**:
1. Let G be greedy solution, O be any optimal solution
2. Let a₁ be first activity in G (earliest ending)
3. Let b₁ be first activity in O
4. If a₁ ≠ b₁:
   - Since a₁ ends first, replace b₁ with a₁ in O
   - No conflicts created (a₁ ends ≤ b₁)
   - New solution O' has same size as O
5. Repeat for remaining activities
6. Eventually O becomes G, so G is optimal. ∎

---

## Greedy vs Dynamic Programming

### Comparison

| Aspect | Greedy | DP |
|--------|--------|-----|
| **Choice** | Make best local choice | Consider all choices |
| **Subproblems** | Disjoint | Overlapping |
| **Reconsider** | Never | May backtrack |
| **Complexity** | Usually O(n log n) | Usually O(n²) or higher |

### When to Use Which

**Use Greedy when:**
- Greedy choice property holds
- Can prove correctness
- Problem has indicators (sorting helps, intervals, etc.)

**Use DP when:**
- Greedy has counterexample
- Overlapping subproblems
- Need to consider all possibilities

---

## Summary

**Key Principles:**
1. Greedy makes locally optimal choice, never reconsiders
2. Requires greedy choice property + optimal substructure
3. Needs proof of correctness (exchange argument)
4. Often O(n log n) due to sorting
5. Elegant and efficient when applicable

**Common Greedy Patterns:**
- Interval scheduling: Sort by end time
- Resource allocation: Sort by value/cost ratio
- Two pointers: Move greedily from extremes
- Priority queue: Always process best available

Master the theory, learn to recognize patterns, and always verify greedy choice is safe!
