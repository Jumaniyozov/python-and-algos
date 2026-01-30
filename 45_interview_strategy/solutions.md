# Chapter 45: Interview Strategy - Solutions

## Problem-Solving Frameworks

This file contains proven frameworks and approaches for solving interview problems.

---

## The UMPIRE Framework (Detailed)

### U - Understand (5 minutes)

**Goal**: Fully comprehend the problem before attempting to solve.

**Actions**:
1. **Restate the problem** in your own words
   - "So we need to find..."
   - "Given X, return Y..."

2. **Identify inputs and outputs**
   - Input types and constraints
   - Output format
   - Edge cases

3. **Ask clarifying questions**
   ```
   Essential questions:
   - "Can the input be empty?"
   - "What's the size range?"
   - "Are there duplicates?"
   - "Is the input sorted?"
   - "What if no solution exists?"
   - "Should I optimize for time or space?"
   ```

4. **Work through examples**
   - Use provided examples
   - Create your own edge cases
   - Verify understanding

5. **Identify constraints**
   - Time limits
   - Space limits
   - Special requirements

**Example**:
```
Problem: Two Sum

Questions to ask:
✓ "Can I use the same element twice?" → No
✓ "Is there always a solution?" → Yes, guaranteed
✓ "Should I return indices or values?" → Indices
✓ "Is the array sorted?" → No
✓ "Can there be negative numbers?" → Yes
```

---

### M - Match (3 minutes)

**Goal**: Identify the pattern and select the right approach.

**Pattern Categories**:

1. **Arrays & Strings**
   - Two Pointers
   - Sliding Window
   - Prefix Sum
   - Hash Map

2. **Trees**
   - DFS (Pre/In/Post-order)
   - BFS (Level-order)
   - Binary Search Tree properties

3. **Graphs**
   - DFS/BFS traversal
   - Union Find
   - Topological Sort

4. **Dynamic Programming**
   - 1D DP
   - 2D DP
   - Memoization

5. **Design**
   - Hash Map + List
   - Heap + Hash Map
   - Stack/Queue

**Matching Process**:
```python
# Ask yourself:
1. "Have I seen a similar problem?"
2. "What data structure fits best?"
3. "What's the brute force approach?"
4. "Can I optimize?"
```

---

### P - Plan (5-7 minutes)

**Goal**: Outline solution before coding.

**Steps**:

1. **Start with brute force**
   ```
   "The naive approach would be:
   - Check all pairs → O(n²)
   - This works but can we optimize?"
   ```

2. **Optimize**
   ```
   "We can improve to O(n) using:
   - Hash map for O(1) lookup
   - Trade space for time"
   ```

3. **Write algorithm outline**
   ```
   Algorithm:
   1. Create hash map
   2. For each element:
      a. Calculate complement
      b. Check if in map
      c. If found, return
      d. Else, add to map
   ```

4. **Trace through example**
   ```
   Example: [2,7,11,15], target=9
   - i=0: 2, complement=7, map={}, add {2:0}
   - i=1: 7, complement=2, found! return [0,1]
   ```

5. **State complexity**
   ```
   Time: O(n) - single pass
   Space: O(n) - hash map
   ```

6. **Get buy-in**
   ```
   "Does this approach make sense?
   Should I proceed with implementation?"
   ```

---

### I - Implement (15-20 minutes)

**Goal**: Write clean, correct code.

**Best Practices**:

1. **Use descriptive names**
   ```python
   # ❌ Bad
   def f(a, t):
       d = {}
       for i, n in enumerate(a):
           c = t - n

   # ✅ Good
   def two_sum(nums, target):
       seen = {}
       for index, num in enumerate(nums):
           complement = target - num
   ```

2. **Write modular code**
   ```python
   # Break down complex logic
   def solve_problem(data):
       processed = preprocess(data)
       result = compute(processed)
       return format_result(result)
   ```

3. **Handle edge cases**
   ```python
   # Check early
   if not nums or len(nums) < 2:
       return []
   ```

4. **Explain while coding**
   ```
   "I'm creating a hash map here to store seen values..."
   "This loop iterates through the array once..."
   "If we find the complement, we return immediately..."
   ```

5. **Keep it readable**
   ```python
   # Use clear structure
   def solution():
       # Step 1: Initialize
       result = []

       # Step 2: Process
       for item in items:
           if condition(item):
               result.append(transform(item))

       # Step 3: Return
       return result
   ```

---

### R - Review (3-5 minutes)

**Goal**: Verify correctness before declaring done.

**Checklist**:

1. **Trace through code**
   ```
   "Let me walk through with the example:
   Input: [2,7,11,15], target=9

   i=0: num=2, complement=7
        seen={}, add {2:0}

   i=1: num=7, complement=2
        2 in seen! return [0,1] ✓"
   ```

2. **Test edge cases**
   ```python
   Edge cases to check:
   - Empty input: []
   - Minimum input: [1,2]
   - All same: [5,5,5,5]
   - Negative: [-1,-2,3]
   - Large numbers: [10^9, 10^9]
   ```

3. **Look for bugs**
   ```
   Common bugs:
   - Off-by-one errors
   - Null pointer exceptions
   - Integer overflow
   - Unhandled edge cases
   ```

4. **Verify logic**
   ```
   "Does this handle:
   - Empty input? ✓
   - Duplicates? ✓
   - Negative numbers? ✓
   - Single element? ✓"
   ```

---

### E - Evaluate (3-5 minutes)

**Goal**: Analyze and discuss trade-offs.

**Complexity Analysis**:

```python
def analyze_complexity():
    """
    Time Complexity:
    - Loop through array: O(n)
    - Hash map lookup: O(1)
    - Hash map insert: O(1)
    Overall: O(n)

    Space Complexity:
    - Hash map stores up to n elements: O(n)
    Overall: O(n)
    """
```

**Trade-offs Discussion**:

```
"We trade O(n) space for O(n) time:

Alternative 1: Brute force
- Time: O(n²)
- Space: O(1)
- Not optimal for large inputs

Alternative 2: Sort + Two pointers
- Time: O(n log n)
- Space: O(1)
- Loses original indices

Alternative 3: Hash map (current)
- Time: O(n)
- Space: O(n)
- Optimal for this problem"
```

**Optimizations**:

```
"Potential optimizations:
1. Early termination: Stop if target > 2*max(array)
2. Space optimization: Not possible without sacrificing time
3. Parallel processing: Not beneficial for this problem"
```

---

## Communication Templates

### Opening

```
"Thank you for the problem. Let me make sure I understand:
[Restate problem]
Can I clarify a few things?
[Ask questions]
Great, let me think about approaches..."
```

### Discussing Approaches

```
"I can think of a few approaches:

Approach 1: [Brute force]
- How it works: [explanation]
- Time: [complexity]
- Space: [complexity]
- Pros/Cons: [trade-offs]

Approach 2: [Optimized]
- How it works: [explanation]
- Time: [complexity]
- Space: [complexity]
- Pros/Cons: [trade-offs]

I think Approach 2 is better because [reason].
Should I proceed with this approach?"
```

### While Coding

```
"I'm creating a hash map here to track seen elements...
This loop goes through the array once...
Here I'm checking if the complement exists...
If found, we return the indices immediately..."
```

### When Stuck

```
"Hmm, I'm thinking about how to handle [specific case]...
Let me try a different approach...
Can we walk through an example together?
I'm considering [option A] vs [option B]..."
```

### Finishing

```
"Let me verify with the example:
[Trace through]

Edge cases:
[List and check]

Time complexity: O(n) because [reason]
Space complexity: O(n) because [reason]

Is there anything else you'd like me to optimize or explain?"
```

---

## Handling Different Scenarios

### When You Don't Know the Solution

```
1. Don't panic - this is expected
2. Start with brute force:
   "I can solve this in O(n²) by checking all pairs..."
3. Think out loud:
   "The bottleneck is [X]. If I could improve [X]..."
4. Try simpler examples:
   "What if n=2? What if all elements are same?"
5. Ask for hints:
   "Am I on the right track with [approach]?"
```

### When You Make a Mistake

```
1. Stay calm and positive
2. Acknowledge it:
   "Oh, I see the issue here..."
3. Fix it:
   "Let me correct this to..."
4. Verify:
   "Now if I trace through again..."
```

### When Interviewer Gives Hints

```
1. Thank them:
   "Thank you, that's a good point!"
2. Incorporate immediately:
   "So if I use [hint], I can..."
3. Show understanding:
   "That makes sense because..."
```

### When Running Out of Time

```
1. Prioritize correctness
2. Explain what's remaining:
   "I would add error handling here..."
   "For production, I'd also..."
3. Pseudocode if needed:
   "The rest would be:
    // Check edge cases
    // Validate input
    // Return formatted result"
```

---

## Problem-Solving Patterns

### Pattern 1: Two Pointers

**When to use**: Sorted arrays, palindromes, pair finding

**Template**:
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        if condition(arr[left], arr[right]):
            # Process and move pointers
            left += 1
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
```

### Pattern 2: Sliding Window

**When to use**: Subarray/substring problems

**Template**:
```python
def sliding_window(arr):
    window = {}
    left = 0
    result = 0

    for right in range(len(arr)):
        # Expand window
        window[arr[right]] = window.get(arr[right], 0) + 1

        # Shrink if needed
        while not valid(window):
            window[arr[left]] -= 1
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result
```

### Pattern 3: DFS/Backtracking

**When to use**: All combinations, permutations, paths

**Template**:
```python
def backtrack(path, choices):
    # Base case
    if is_valid_solution(path):
        result.append(path[:])
        return

    # Try all choices
    for choice in choices:
        # Make choice
        path.append(choice)

        # Recurse
        backtrack(path, next_choices)

        # Undo choice
        path.pop()
```

---

## Key Takeaways

**The UMPIRE Framework:**
1. **U**nderstand: 5 minutes - clarify everything
2. **M**atch: 3 minutes - identify pattern
3. **P**lan: 5-7 minutes - outline solution
4. **I**mplement: 15-20 minutes - write code
5. **R**eview: 3-5 minutes - test thoroughly
6. **E**valuate: 3-5 minutes - analyze complexity

**Communication is Key:**
- Think out loud
- Explain decisions
- Ask for feedback
- Stay positive

**When Stuck:**
- Try simpler examples
- Draw diagrams
- Think of similar problems
- Ask for hints

**Success Formula:**
Process > Solution
Communication > Code perfection
Problem-solving approach > Memorization

Practice this framework until it becomes natural!
