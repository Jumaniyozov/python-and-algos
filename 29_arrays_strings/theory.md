# Arrays and Strings - Theory

## Table of Contents

1. [Array Fundamentals](#array-fundamentals)
2. [Two Pointers Pattern](#two-pointers-pattern)
3. [Sliding Window Pattern](#sliding-window-pattern)
4. [String Fundamentals](#string-fundamentals)
5. [Common Array Problems](#common-array-problems)
6. [Common String Problems](#common-string-problems)
7. [Complexity Analysis](#complexity-analysis)

---

## Array Fundamentals

### What is an Array?

An array is a contiguous block of memory storing elements of the same type, accessible by index.

```python
# Python lists are dynamic arrays
arr = [1, 2, 3, 4, 5]

# Access: O(1)
print(arr[0])  # 1

# Modify: O(1)
arr[0] = 10

# Append: O(1) amortized
arr.append(6)

# Insert at position: O(n)
arr.insert(0, 0)

# Delete at position: O(n)
del arr[0]
```

### Array Operations Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access by index | O(1) | O(1) |
| Search | O(n) | O(1) |
| Insert at end | O(1) amortized | O(1) |
| Insert at position | O(n) | O(1) |
| Delete at end | O(1) | O(1) |
| Delete at position | O(n) | O(1) |

### Array vs List in Python

```python
# Python list (dynamic array)
list_arr = [1, 2, 3]
list_arr.append(4)  # Resizes automatically

# Array module (fixed type)
import array
int_arr = array.array('i', [1, 2, 3])  # 'i' = integer

# NumPy array (fixed size, fast)
import numpy as np
np_arr = np.array([1, 2, 3])
```

---

## Two Pointers Pattern

### Concept

Use two pointers to traverse an array, often from different directions or at different speeds.

### Pattern 1: Left-Right Pointers

Start from both ends and move towards center.

```python
def two_pointers_opposite(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Process arr[left] and arr[right]
        # Move pointers based on condition
        left += 1
        right -= 1
```

**Use Cases:**
- Two Sum (sorted array)
- Palindrome check
- Reverse array
- Container with most water

**Complexity:** O(n) time, O(1) space

### Pattern 2: Fast-Slow Pointers

Two pointers moving at different speeds.

```python
def fast_slow_pointers(arr):
    slow = 0
    fast = 0

    while fast < len(arr):
        # Slow moves conditionally
        # Fast always moves
        if condition:
            slow += 1
        fast += 1
```

**Use Cases:**
- Remove duplicates
- Move zeros to end
- Partition array
- Cycle detection (linked lists)

**Complexity:** O(n) time, O(1) space

### Pattern 3: Same Direction Pointers

Both pointers start from the beginning.

```python
def same_direction(arr):
    left = 0

    for right in range(len(arr)):
        # Expand window with right
        # Shrink window with left if needed
        while condition:
            left += 1
```

**Use Cases:**
- Longest substring without repeating characters
- Variable-size sliding window
- Subarray with target sum

**Complexity:** O(n) time, O(1) space typically

---

## Sliding Window Pattern

### Concept

Maintain a window (subarray) and slide it across the array.

### Fixed-Size Sliding Window

Window size is constant.

```python
def fixed_window(arr, k):
    # Initialize window
    window_sum = sum(arr[:k])
    result = window_sum

    # Slide window
    for i in range(k, len(arr)):
        # Remove left element, add right element
        window_sum = window_sum - arr[i-k] + arr[i]
        result = max(result, window_sum)

    return result
```

**Template:**
```python
def fixed_sliding_window(arr, k):
    if len(arr) < k:
        return None

    # 1. Compute initial window
    window = compute_initial_window(arr[:k])

    # 2. Slide window
    for i in range(k, len(arr)):
        # Remove arr[i-k]
        # Add arr[i]
        window = update_window(window, arr[i-k], arr[i])

    return result
```

**Use Cases:**
- Maximum sum of k consecutive elements
- Average of all k-size subarrays
- First negative number in each window
- Maximum of all subarrays of size k

**Complexity:** O(n) time, O(1) space

### Variable-Size Sliding Window

Window size changes based on condition.

```python
def variable_window(arr, target):
    left = 0
    window_sum = 0
    min_length = float('inf')

    for right in range(len(arr)):
        # Expand window
        window_sum += arr[right]

        # Shrink window while condition met
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0
```

**Template:**
```python
def variable_sliding_window(arr, condition):
    left = 0
    result = 0

    for right in range(len(arr)):
        # 1. Expand window by adding arr[right]
        add_to_window(arr[right])

        # 2. Shrink window while invalid
        while not valid():
            remove_from_window(arr[left])
            left += 1

        # 3. Update result
        result = update_result(result, right - left + 1)

    return result
```

**Use Cases:**
- Smallest subarray with sum ≥ target
- Longest substring without repeating characters
- Longest substring with at most k distinct characters
- Minimum window substring

**Complexity:** O(n) time, O(k) space (k = distinct elements)

---

## String Fundamentals

### String Properties

```python
# Strings are immutable in Python
s = "hello"
# s[0] = 'H'  # Error!

# Create new string instead
s = 'H' + s[1:]  # "Hello"

# String concatenation: O(n)
result = ""
for char in "abc":
    result += char  # Creates new string each time!

# Better: use join - O(n)
result = ''.join(['a', 'b', 'c'])
```

### String Operations Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access char | O(1) | O(1) |
| Concatenation (+) | O(n) | O(n) |
| Join | O(n) | O(n) |
| Slice | O(k) | O(k) |
| Find substring | O(n*m) | O(1) |
| Replace | O(n) | O(n) |
| Split | O(n) | O(n) |

### Common String Methods

```python
s = "Hello World"

# Case conversion
s.lower()  # "hello world"
s.upper()  # "HELLO WORLD"
s.title()  # "Hello World"

# Searching
s.find("World")  # 6
s.index("World")  # 6 (raises error if not found)
"World" in s  # True

# Modification (returns new string)
s.replace("World", "Python")  # "Hello Python"
s.strip()  # Remove whitespace
s.split()  # ["Hello", "World"]

# Check properties
s.isalpha()  # False (has space)
s.isdigit()  # False
s.isalnum()  # False
s.startswith("Hello")  # True
s.endswith("World")  # True
```

### String Building

```python
# ✗ Bad: O(n²) due to string immutability
result = ""
for i in range(n):
    result += str(i)

# ✓ Good: O(n) using list
result = []
for i in range(n):
    result.append(str(i))
final = ''.join(result)

# ✓ Good: List comprehension
result = ''.join(str(i) for i in range(n))
```

---

## Common Array Problems

### 1. Array Rotation

**Problem:** Rotate array by k positions.

```python
def rotate_array(arr, k):
    """
    Rotate array to the right by k positions.
    Time: O(n), Space: O(1)
    """
    n = len(arr)
    k = k % n  # Handle k > n

    # Reverse entire array
    reverse(arr, 0, n - 1)
    # Reverse first k elements
    reverse(arr, 0, k - 1)
    # Reverse remaining elements
    reverse(arr, k, n - 1)

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
```

### 2. Partitioning (Dutch Flag)

**Problem:** Partition array into three parts based on pivot.

```python
def dutch_flag(arr, pivot):
    """
    Partition: elements < pivot, == pivot, > pivot
    Time: O(n), Space: O(1)
    """
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == pivot:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
```

### 3. Subarray Sum

**Problem:** Find subarray with given sum.

```python
def subarray_sum(arr, target):
    """
    Find subarray with sum = target.
    Time: O(n), Space: O(n)
    """
    prefix_sum = {0: -1}
    current_sum = 0

    for i, num in enumerate(arr):
        current_sum += num

        if current_sum - target in prefix_sum:
            start = prefix_sum[current_sum - target] + 1
            return (start, i)

        prefix_sum[current_sum] = i

    return None
```

### 4. Merge Sorted Arrays

**Problem:** Merge two sorted arrays.

```python
def merge_sorted(arr1, arr2):
    """
    Merge two sorted arrays.
    Time: O(n+m), Space: O(n+m)
    """
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result
```

---

## Common String Problems

### 1. Palindrome Check

```python
def is_palindrome(s):
    """
    Check if string is palindrome (ignore case/spaces).
    Time: O(n), Space: O(1)
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

### 2. Anagram Check

```python
def are_anagrams(s1, s2):
    """
    Check if two strings are anagrams.
    Time: O(n), Space: O(k) where k = distinct chars
    """
    if len(s1) != len(s2):
        return False

    # Method 1: Sorting - O(n log n)
    return sorted(s1) == sorted(s2)

    # Method 2: Hash map - O(n)
    from collections import Counter
    return Counter(s1) == Counter(s2)
```

### 3. Longest Substring Without Repeating Characters

```python
def longest_unique_substring(s):
    """
    Find length of longest substring without repeating chars.
    Time: O(n), Space: O(min(n, k)) where k = charset size
    """
    char_index = {}
    max_length = 0
    left = 0

    for right, char in enumerate(s):
        # If char seen and in current window
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length
```

### 4. Minimum Window Substring

```python
def min_window_substring(s, t):
    """
    Find minimum window in s containing all chars in t.
    Time: O(n + m), Space: O(k) where k = distinct chars
    """
    from collections import Counter

    if not s or not t:
        return ""

    # Count characters in t
    target_count = Counter(t)
    required = len(target_count)
    formed = 0

    window_counts = {}
    left = 0
    min_len = float('inf')
    min_window = (0, 0)

    for right, char in enumerate(s):
        # Add char to window
        window_counts[char] = window_counts.get(char, 0) + 1

        # Check if this char satisfies requirement
        if char in target_count and window_counts[char] == target_count[char]:
            formed += 1

        # Try to shrink window
        while left <= right and formed == required:
            # Update result
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = (left, right)

            # Remove leftmost char
            char = s[left]
            window_counts[char] -= 1
            if char in target_count and window_counts[char] < target_count[char]:
                formed -= 1

            left += 1

    return "" if min_len == float('inf') else s[min_window[0]:min_window[1] + 1]
```

---

## Complexity Analysis

### Time Complexity Patterns

| Pattern | Complexity | Reason |
|---------|------------|--------|
| Single pass | O(n) | Visit each element once |
| Two pointers | O(n) | Each pointer moves at most n times |
| Fixed window | O(n) | Slide window across array |
| Variable window | O(n) | Each element added/removed once |
| Nested loops | O(n²) | For each element, check all others |
| Binary search | O(log n) | Halve search space each time |
| Sorting | O(n log n) | Optimal comparison-based sort |

### Space Complexity Patterns

| Pattern | Complexity | Reason |
|---------|------------|--------|
| In-place | O(1) | Only pointers |
| Hash map | O(k) | Store k distinct elements |
| Recursion | O(h) | Call stack of height h |
| Array copy | O(n) | New array of size n |

### Optimization Strategies

1. **Avoid Nested Loops:** Use hash maps or two pointers
2. **Avoid Recreating:** Reuse data structures
3. **Use In-place:** Modify array directly
4. **Leverage Sorting:** Sometimes O(n log n) + O(n) < O(n²)
5. **Use Hash Maps:** Trade space for time

---

## Summary

### Key Patterns

1. **Two Pointers**
   - Left-right: Palindrome, two sum
   - Fast-slow: Remove duplicates
   - Same direction: Sliding window

2. **Sliding Window**
   - Fixed: Max sum k elements
   - Variable: Min window substring

3. **Array Manipulation**
   - Rotation: Three reversals
   - Partitioning: Dutch flag
   - Merging: Two pointers

4. **String Algorithms**
   - Palindrome: Two pointers
   - Anagram: Hash map
   - Substring: Sliding window

### When to Use What

```
Pair/triplet in sorted array? → Two pointers
Subarray/substring with constraint? → Sliding window
Partition array by property? → Two pointers
String matching? → Sliding window or KMP
Anagram/permutation? → Hash map
```

### Complexity Goals

- **Target Time:** O(n) for most problems
- **Target Space:** O(1) or O(k) where k << n
- **Avoid:** O(n²) time unless n is small

---

## Next Steps

After mastering arrays and strings:
1. Study linked lists (Chapter 29)
2. Learn stack and queue applications (Chapter 30)
3. Explore hash table implementations (Chapter 31)
4. Practice on LeetCode (Two Pointers, Sliding Window tags)
5. Analyze real-world string processing applications
