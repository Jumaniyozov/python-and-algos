# Complexity Analysis - Exercises

## 15 Progressive Challenges

### Analyzing Code Complexity

#### Exercise 1: Identify Complexity

For each code snippet, determine:
1. Time complexity (best, average, worst)
2. Space complexity
3. Why (explain your reasoning)

```python
# Code 1
def print_all(n):
    for i in range(n):
        print(i)

# Code 2
def print_pairs(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# Code 3
def print_half(n):
    while n > 1:
        print(n)
        n = n // 2

# Code 4
def find_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

#### Exercise 2: Complex Code Analysis

Analyze this function:

```python
def complex_function(n):
    # Phase 1
    for i in range(n):
        print(i)

    # Phase 2
    for i in range(n):
        for j in range(n):
            print(i, j)

    # Phase 3
    while n > 1:
        print(n)
        n = n // 2
```

Questions:
1. What is total time complexity?
2. Which phase dominates?
3. Would it change with different input?

#### Exercise 3: Recursive Complexity

Analyze time and space complexity:

```python
def mystery1(n):
    if n <= 1:
        return 1
    return mystery1(n - 1) + mystery1(n - 1)

def mystery2(n):
    if n <= 1:
        return 1
    return mystery2(n - 1)

def mystery3(n):
    if n <= 1:
        return 1
    return mystery3(n // 2) + mystery3(n // 2)
```

---

### Comparing Algorithms

#### Exercise 4: Linear vs Binary Search

Create two functions and compare:
1. Linear search - O(n)
2. Binary search - O(log n)

Test with sorted array of 1 million items. Measure time for:
- First element
- Last element
- Middle element
- Not found

Document performance difference.

#### Exercise 5: Sorting Algorithms

Implement and analyze:
1. Bubble sort - O(n²)
2. Merge sort - O(n log n)

Test with arrays of size:
- 1000
- 10000
- 100000

Create table showing:
- Array size
- Time for bubble sort
- Time for merge sort
- Speed ratio

#### Exercise 6: Better Algorithm Selection

For finding sum of products, analyze:

```python
# Approach 1: Brute force O(n²)
def sum_products_slow(arr1, arr2):
    total = 0
    for x in arr1:
        for y in arr2:
            total += x * y
    return total

# Approach 2: Mathematical O(n)
def sum_products_fast(arr1, arr2):
    return sum(arr1) * sum(arr2)
```

Show they're equivalent and prove O(n) is faster.

---

### Space-Time Tradeoffs

#### Exercise 7: Caching Example

Compare:
1. No caching - O(1) space, O(n) time
2. With caching - O(n) space, O(1) time

```python
# Without cache
def expensive_operation(x):
    # Simulate expensive calculation
    result = 0
    for i in range(1000000):
        result += i * x
    return result

# With cache
def expensive_with_cache(x):
    # Pre-compute and cache results
    cache = {}
    if x not in cache:
        result = 0
        for i in range(1000000):
            result += i * x
        cache[x] = result
    return cache[x]
```

Questions:
- How much memory does cache need?
- When is caching worth it?
- When should you avoid caching?

#### Exercise 8: In-place vs Extra Space

Compare:
1. In-place reversal - O(1) space
2. New array reversal - O(n) space

```python
# In-place
def reverse_inplace(arr):
    pass  # Your implementation

# With extra space
def reverse_extra(arr):
    pass  # Your implementation
```

Measure:
- Time for both
- Memory usage
- When each is preferred

---

### Analyzing Data Structures

#### Exercise 9: List vs Dictionary

For n = 1000:
1. List lookup by index - O(1)
2. List search by value - O(n)
3. Dictionary lookup - O(1)

Create test showing:
- Time for each operation
- When to use list vs dict
- Performance ratios

#### Exercise 10: Set Operations

Analyze:
1. Check membership in list - O(n)
2. Check membership in set - O(1)

```python
# For each operation below, calculate complexity
def find_common_elements_slow(list1, list2):
    # O(n²)
    common = []
    for item in list1:
        if item in list2:  # O(n) search
            common.append(item)
    return common

def find_common_elements_fast(list1, list2):
    # O(n)
    set2 = set(list2)  # O(n) to create
    return [item for item in list1 if item in set2]  # O(1) lookup
```

Show speed improvement with large lists.

---

### Real-World Scenarios

#### Exercise 11: Database Query Optimization

Given:
- 1 million users in database
- Need to find users by email

Compare:
1. Linear scan - O(n)
2. Indexed search - O(log n)

Calculate:
- Operations for each approach
- Time for 100 queries
- Practical speedup factor

#### Exercise 12: Web API Performance

Design API that:
1. Returns user data - should be O(1)
2. Returns all user posts - should be O(k)
3. Returns filtered posts - should be efficient

Analyze:
- Current approach complexity
- How to optimize with caching
- When to use database indexes

#### Exercise 13: Memory Constraints

Given only 1 GB RAM, analyze:
1. Can you process 1 billion integers in array?
2. What complexity is acceptable?
3. What data structures fit in memory?

Calculate:
- Memory needed for each approach
- Runtime for different algorithms
- Best compromise between time and space

---

### Optimization Challenges

#### Exercise 14: Optimize Given Code

Given inefficient code:

```python
def find_expensive_pairs(arr, target):
    """Find all pairs that sum to target"""
    pairs = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs
```

Optimize to:
- Faster time complexity
- Less space usage
- More readable

Show before and after analysis.

#### Exercise 15: Algorithm Selection Project

Build system that:
1. Stores 1 million records
2. Performs frequent searches
3. Handles 1000 queries per second

Decide:
1. What data structure to use? (array, list, dict, set, tree?)
2. What search algorithm? (linear, binary, hash?)
3. Should you cache? Why?
4. How to handle memory?

Provide:
- Complexity analysis of each decision
- Performance predictions
- Tradeoff justifications

---

## Analysis Template

For each exercise, use this template:

```
Analysis Template:

Code:
[Show the code]

Time Complexity:
- Best case: O(?) - when?
- Average case: O(?)
- Worst case: O(?)
- Explanation: [Why this complexity]

Space Complexity: O(?) - Explanation

Dominant Term: [Which term dominates as n grows]

Practical Implications:
- For n = 100: ? operations
- For n = 10,000: ? operations
- For n = 1,000,000: ? operations

Could it be improved? How?
```

---

## Hints

1. **Count loops**: Each loop adds to multiplier
2. **Nested loops multiply**: O(n) × O(n) = O(n²)
3. **Sequential adds**: O(n) + O(n) = O(n)
4. **Drop constants**: O(2n) → O(n)
5. **Drop low terms**: O(n² + n) → O(n²)
6. **Watch recursion**: Can be deceptive
7. **Track divisions**: Division by 2 → logarithm
8. **Measure real performance**: Theory + practice

---

## Challenge Progression

1. **Exercises 1-3**: Understanding complexity notation
2. **Exercises 4-6**: Comparing algorithms
3. **Exercises 7-8**: Space-time tradeoffs
4. **Exercises 9-10**: Data structure selection
5. **Exercises 11-13**: Real-world scenarios
6. **Exercises 14-15**: Optimization and decisions

Complete in order for best understanding.

---

## Grading Rubric

For each analysis:

- **Correct complexity**: ✓
- **Correct reasoning**: ✓
- **Considers all cases**: ✓ (best, avg, worst)
- **Practical examples**: ✓
- **Trade-off analysis**: ✓
- **Code optimization**: ✓
