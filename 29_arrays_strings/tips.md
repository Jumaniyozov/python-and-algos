# Arrays and Strings - Tips and Best Practices

## Pattern Recognition

### When to Use Two Pointers

**Indicators:**
- Array is sorted or can be sorted
- Need to find pairs/triplets
- Checking palindrome
- Partitioning array
- Comparing from both ends

**Common Problems:**
- Two Sum (sorted array)
- Container with most water
- Valid palindrome
- Remove duplicates
- Dutch flag problem

**Template:**
```python
def two_pointers_opposite(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process arr[left] and arr[right]
        if condition:
            # Found solution
            return result
        elif need_larger:
            left += 1
        else:
            right -= 1
```

---

### When to Use Sliding Window

**Indicators:**
- Finding subarray/substring
- Contains keywords: "consecutive", "contiguous", "substring"
- Optimization problem on subarrays
- Window has specific constraint

**Fixed Window Problems:**
- Maximum sum of k consecutive elements
- Average of all k-size subarrays
- First negative in each window

**Variable Window Problems:**
- Longest substring without repeating chars
- Smallest subarray with sum ≥ target
- Minimum window substring

**Template:**
```python
# Fixed window
def fixed_window(arr, k):
    window = init_window(arr[:k])
    result = window

    for i in range(k, len(arr)):
        window = window - arr[i-k] + arr[i]
        result = update_result(result, window)

    return result

# Variable window
def variable_window(arr):
    left = 0
    window = init_window()

    for right in range(len(arr)):
        add_to_window(arr[right])

        while not valid():
            remove_from_window(arr[left])
            left += 1

        update_result(right - left + 1)
```

---

## Common Pitfalls

### 1. Off-by-One Errors

```python
# ✗ Wrong: Misses last element
for i in range(len(arr) - 1):
    process(arr[i])

# ✓ Correct
for i in range(len(arr)):
    process(arr[i])

# ✗ Wrong: Index out of bounds
for i in range(len(arr)):
    compare(arr[i], arr[i+1])  # Fails at last element

# ✓ Correct
for i in range(len(arr) - 1):
    compare(arr[i], arr[i+1])
```

### 2. String Immutability

```python
# ✗ Wrong: Creates new string each iteration - O(n²)
result = ""
for char in s:
    result += char

# ✓ Correct: Use list - O(n)
result = []
for char in s:
    result.append(char)
final = ''.join(result)

# ✓ Better: List comprehension
result = ''.join(char for char in s)
```

### 3. Modifying Array While Iterating

```python
# ✗ Wrong: Unpredictable behavior
for i in range(len(arr)):
    if condition:
        arr.pop(i)  # Shifts elements!

# ✓ Correct: Iterate backwards
for i in range(len(arr) - 1, -1, -1):
    if condition:
        arr.pop(i)

# ✓ Better: Use list comprehension
arr = [x for x in arr if not condition]
```

### 4. Not Handling Empty Input

```python
# ✗ Wrong: Crashes on empty array
def max_element(arr):
    max_val = arr[0]  # IndexError if arr is empty
    for num in arr[1:]:
        max_val = max(max_val, num)
    return max_val

# ✓ Correct: Check for empty
def max_element(arr):
    if not arr:
        return None  # or raise ValueError
    max_val = arr[0]
    for num in arr[1:]:
        max_val = max(max_val, num)
    return max_val
```

---

## Optimization Techniques

### 1. Hash Map for O(1) Lookup

```python
# ✗ Slow: O(n²) - nested loops
def two_sum_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]

# ✓ Fast: O(n) - hash map
def two_sum_fast(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

### 2. Sliding Window vs Brute Force

```python
# ✗ Slow: O(n*k) - recalculate each window
def max_sum_slow(arr, k):
    max_sum = float('-inf')
    for i in range(len(arr) - k + 1):
        window_sum = sum(arr[i:i+k])  # Recalculate each time
        max_sum = max(max_sum, window_sum)
    return max_sum

# ✓ Fast: O(n) - sliding window
def max_sum_fast(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

### 3. In-Place vs Extra Space

```python
# Uses O(n) extra space
def reverse_extra_space(arr):
    return arr[::-1]

# Uses O(1) space - in-place
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

---

## Debugging Tips

### 1. Print Window State

```python
def debug_sliding_window(arr, k):
    window_sum = sum(arr[:k])

    for i in range(k, len(arr)):
        # Debug: Show window state
        print(f"Window [{i-k}:{i}]: {arr[i-k:i]}, sum={window_sum}")

        window_sum = window_sum - arr[i-k] + arr[i]
```

### 2. Verify Invariants

```python
def two_pointers_debug(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # Verify invariant: left < right
        assert left < right, f"Invariant broken: {left} >= {right}"

        # Your logic here
        left += 1
```

### 3. Test Edge Cases

```python
def test_edge_cases(func):
    # Empty
    assert func([]) == expected_empty

    # Single element
    assert func([1]) == expected_single

    # Two elements
    assert func([1, 2]) == expected_two

    # All same
    assert func([1, 1, 1]) == expected_same

    # Already sorted
    assert func([1, 2, 3]) == expected_sorted

    # Reverse sorted
    assert func([3, 2, 1]) == expected_reverse
```

---

## Performance Tips

### 1. Choose Right Data Structure

```python
# ✗ Slow: List for membership testing - O(n)
seen = []
for item in items:
    if item in seen:  # O(n) lookup
        continue
    seen.append(item)

# ✓ Fast: Set for membership - O(1)
seen = set()
for item in items:
    if item in seen:  # O(1) lookup
        continue
    seen.add(item)
```

### 2. Avoid Unnecessary Copies

```python
# ✗ Creates copy
subarray = arr[i:j]  # O(j-i) space and time

# ✓ Use indices
start, end = i, j  # O(1)
```

### 3. Use Built-in Functions

```python
# ✗ Slower: Manual implementation
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# ✓ Faster: Built-in
max_val = max(arr)
```

---

## Interview Tips

### 1. Clarify Constraints

**Always ask:**
- Array size? (Can fit in memory?)
- Value range? (Overflow possible?)
- Duplicates allowed?
- Array sorted?
- Modify in-place?
- Empty input possible?

### 2. Start with Brute Force

```python
# Step 1: Brute force (clarify logic)
def solve_brute_force(arr):
    # O(n²) but correct
    pass

# Step 2: Optimize
def solve_optimized(arr):
    # O(n) optimized version
    pass
```

### 3. Explain Your Approach

**Template:**
1. **Understand**: Repeat problem in your words
2. **Example**: Walk through example
3. **Approach**: Explain algorithm choice
4. **Code**: Write clean code
5. **Test**: Test with examples
6. **Optimize**: Discuss improvements

### 4. Complexity Analysis

**Always state:**
- Time complexity with justification
- Space complexity
- Best/average/worst case if different

---

## Common Tricks

### 1. Two Pointers from Same Side

```python
# Remove duplicates in sorted array
def remove_duplicates(arr):
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1
```

### 2. Expand Around Center

```python
# Find palindrome by expanding
def expand_palindrome(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
```

### 3. Prefix Sum

```python
# Precompute prefix sums for range queries
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)

# Sum of arr[i:j] in O(1)
range_sum = prefix[j] - prefix[i]
```

### 4. Hash Map for Indices

```python
# Track last seen index
last_seen = {}
for i, char in enumerate(s):
    if char in last_seen:
        # Found duplicate
        distance = i - last_seen[char]
    last_seen[char] = i
```

---

## Complexity Cheat Sheet

### Time Complexity

| Operation | Complexity | Example |
|-----------|------------|---------|
| Single pass | O(n) | Linear search |
| Two pointers | O(n) | Two sum sorted |
| Sliding window | O(n) | Max sum subarray |
| Nested loops | O(n²) | Brute force |
| With hash map | O(n) | Two sum unsorted |
| With sorting | O(n log n) | Three sum |
| Binary search | O(log n) | Search sorted |

### Space Complexity

| Technique | Complexity | Example |
|-----------|------------|---------|
| In-place | O(1) | Two pointers |
| Hash map | O(n) | Seen elements |
| Recursion | O(h) | DFS depth h |
| Window map | O(k) | k distinct chars |

---

## Best Practices

### 1. Write Clean Code

```python
# ✗ Bad: Hard to read
def f(a,t):
    l,r=0,len(a)-1
    while l<r:
        if a[l]+a[r]==t:return [l,r]
        elif a[l]+a[r]<t:l+=1
        else:r-=1

# ✓ Good: Clear and readable
def two_sum_sorted(arr, target):
    """Find two numbers that sum to target."""
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None
```

### 2. Handle Edge Cases

```python
def safe_function(arr):
    # Check for None
    if arr is None:
        return None

    # Check for empty
    if not arr:
        return []

    # Check for single element
    if len(arr) == 1:
        return arr[0]

    # Main logic
    # ...
```

### 3. Use Meaningful Names

```python
# ✗ Bad
def f(a, k):
    s = 0
    for i in range(k):
        s += a[i]

# ✓ Good
def max_sum_subarray(arr, window_size):
    current_sum = 0
    for i in range(window_size):
        current_sum += arr[i]
```

---

## Quick Reference

### Two Pointers Patterns

```python
# Opposite direction
left, right = 0, len(arr) - 1
while left < right:
    # process and move pointers

# Same direction (fast-slow)
slow = 0
for fast in range(len(arr)):
    if condition:
        slow += 1
```

### Sliding Window Patterns

```python
# Fixed size
window = arr[:k]
for i in range(k, len(arr)):
    window = window - arr[i-k] + arr[i]

# Variable size
left = 0
for right in range(len(arr)):
    add_to_window(arr[right])
    while invalid():
        remove_from_window(arr[left])
        left += 1
```

### String Building

```python
# ✓ Use list for efficiency
chars = []
for char in string:
    chars.append(char)
result = ''.join(chars)
```

---

## Practice Strategy

1. **Master Patterns**: Learn 2-3 problems per pattern deeply
2. **Increase Difficulty**: Easy → Medium → Hard
3. **Time Yourself**: Practice under time pressure
4. **Explain Aloud**: Practice explaining your approach
5. **Review Solutions**: Learn from optimal solutions
6. **Identify Variations**: Recognize similar problems

### Recommended Practice Order

1. Two Pointers (5-10 problems)
2. Sliding Window (5-10 problems)
3. String Manipulation (5-10 problems)
4. Mixed Problems (10+ problems)

---

Remember: Arrays and strings are the foundation. Master these patterns and you'll solve 40%+ of interview problems!
