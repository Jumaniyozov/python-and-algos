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

---

## LeetCode Practice Problems

### 📊 Problem Statistics
- **Total Problems:** 65+
- **Easy:** 20 problems
- **Medium:** 30 problems  
- **Hard:** 15 problems
- **Estimated Time:** 40-60 hours

---

## Easy Problems (20)

### 1. Two Sum
**Link:** https://leetcode.com/problems/two-sum/  
**Pattern:** Hash Table  
**Topics:** Array, Hash Table  
**Description:** Find two numbers that add up to target  
**Why Practice:** Foundation for many array problems, teaches hash table usage

### 2. Best Time to Buy and Sell Stock
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/  
**Pattern:** Single Pass  
**Topics:** Array, Dynamic Programming  
**Description:** Find maximum profit from stock prices  
**Why Practice:** Teaches tracking min/max in single pass

### 3. Contains Duplicate
**Link:** https://leetcode.com/problems/contains-duplicate/  
**Pattern:** Hash Set  
**Topics:** Array, Hash Table  
**Description:** Check if array has duplicates  
**Why Practice:** Basic hash set application

### 4. Valid Anagram
**Link:** https://leetcode.com/problems/valid-anagram/  
**Pattern:** Hash Map  
**Topics:** String, Hash Table, Sorting  
**Description:** Check if two strings are anagrams  
**Why Practice:** String comparison techniques

### 5. Valid Palindrome
**Link:** https://leetcode.com/problems/valid-palindrome/  
**Pattern:** Two Pointers  
**Topics:** String, Two Pointers  
**Description:** Check if string is palindrome  
**Why Practice:** Two pointers from both ends

### 6. Reverse String
**Link:** https://leetcode.com/problems/reverse-string/  
**Pattern:** Two Pointers  
**Topics:** String, Two Pointers  
**Description:** Reverse string in-place  
**Why Practice:** In-place modification basics

### 7. Move Zeroes
**Link:** https://leetcode.com/problems/move-zeroes/  
**Pattern:** Two Pointers  
**Topics:** Array, Two Pointers  
**Description:** Move all zeros to end  
**Why Practice:** In-place array rearrangement

### 8. Plus One
**Link:** https://leetcode.com/problems/plus-one/  
**Pattern:** Array Manipulation  
**Topics:** Array, Math  
**Description:** Add one to number represented as array  
**Why Practice:** Carry handling in arrays

### 9. Merge Sorted Array
**Link:** https://leetcode.com/problems/merge-sorted-array/  
**Pattern:** Two Pointers  
**Topics:** Array, Two Pointers, Sorting  
**Description:** Merge two sorted arrays in-place  
**Why Practice:** Backward two pointers technique

### 10. Remove Duplicates from Sorted Array
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/  
**Pattern:** Two Pointers  
**Topics:** Array, Two Pointers  
**Description:** Remove duplicates in-place  
**Why Practice:** Slow/fast pointer technique

### 11. Remove Element
**Link:** https://leetcode.com/problems/remove-element/  
**Pattern:** Two Pointers  
**Topics:** Array, Two Pointers  
**Description:** Remove all instances of value  
**Why Practice:** In-place removal pattern

### 12. Implement strStr()
**Link:** https://leetcode.com/problems/implement-strstr/  
**Pattern:** String Matching  
**Topics:** String, Two Pointers  
**Description:** Find substring in string  
**Why Practice:** Basic string search

### 13. Length of Last Word
**Link:** https://leetcode.com/problems/length-of-last-word/  
**Pattern:** String Traversal  
**Topics:** String  
**Description:** Return length of last word  
**Why Practice:** String parsing basics

### 14. Longest Common Prefix
**Link:** https://leetcode.com/problems/longest-common-prefix/  
**Pattern:** String Comparison  
**Topics:** String  
**Description:** Find longest common prefix  
**Why Practice:** Vertical scanning technique

### 15. Valid Parentheses
**Link:** https://leetcode.com/problems/valid-parentheses/  
**Pattern:** Stack  
**Topics:** String, Stack  
**Description:** Check if parentheses are valid  
**Why Practice:** Stack application (also in Ch 31)

### 16. Palindrome Number
**Link:** https://leetcode.com/problems/palindrome-number/  
**Pattern:** Math  
**Topics:** Math  
**Description:** Check if number is palindrome  
**Why Practice:** Number manipulation without string

### 17. Roman to Integer
**Link:** https://leetcode.com/problems/roman-to-integer/  
**Pattern:** Hash Map  
**Topics:** String, Math, Hash Table  
**Description:** Convert Roman numeral to integer  
**Why Practice:** Rule-based parsing

### 18. Find All Numbers Disappeared in an Array
**Link:** https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/  
**Pattern:** Index Marking  
**Topics:** Array, Hash Table  
**Description:** Find missing numbers  
**Why Practice:** In-place marking technique

### 19. Third Maximum Number
**Link:** https://leetcode.com/problems/third-maximum-number/  
**Pattern:** Tracking Variables  
**Topics:** Array  
**Description:** Find third maximum distinct number  
**Why Practice:** Tracking multiple values

### 20. Intersection of Two Arrays II
**Link:** https://leetcode.com/problems/intersection-of-two-arrays-ii/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table, Two Pointers, Binary Search, Sorting  
**Description:** Find intersection allowing duplicates  
**Why Practice:** Multiple solution approaches

---

## Medium Problems (30)

### 21. 3Sum
**Link:** https://leetcode.com/problems/3sum/  
**Pattern:** Two Pointers  
**Topics:** Array, Two Pointers, Sorting  
**Description:** Find all unique triplets that sum to zero  
**Why Practice:** Advanced two pointers, duplicate handling

### 22. Container With Most Water
**Link:** https://leetcode.com/problems/container-with-most-water/  
**Pattern:** Two Pointers  
**Topics:** Array, Two Pointers, Greedy  
**Description:** Find max area between vertical lines  
**Why Practice:** Greedy two pointers decision

### 23. Longest Substring Without Repeating Characters
**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/  
**Pattern:** Sliding Window  
**Topics:** String, Hash Table, Sliding Window  
**Description:** Find longest substring with unique chars  
**Why Practice:** Classic sliding window with hash table

### 24. Longest Palindromic Substring
**Link:** https://leetcode.com/problems/longest-palindromic-substring/  
**Pattern:** Expand Around Center  
**Topics:** String, Dynamic Programming  
**Description:** Find longest palindromic substring  
**Why Practice:** Expand from center technique

### 25. String to Integer (atoi)
**Link:** https://leetcode.com/problems/string-to-integer-atoi/  
**Pattern:** String Parsing  
**Topics:** String, Math  
**Description:** Implement atoi function  
**Why Practice:** Edge case handling, parsing

### 26. ZigZag Conversion
**Link:** https://leetcode.com/problems/zigzag-conversion/  
**Pattern:** String Manipulation  
**Topics:** String  
**Description:** Convert string to zigzag pattern  
**Why Practice:** 2D pattern in 1D array

### 27. Product of Array Except Self
**Link:** https://leetcode.com/problems/product-of-array-except-self/  
**Pattern:** Prefix/Suffix Product  
**Topics:** Array, Prefix Sum  
**Description:** Product except current element  
**Why Practice:** Prefix/suffix array technique

### 28. Rotate Image
**Link:** https://leetcode.com/problems/rotate-image/  
**Pattern:** Matrix Manipulation  
**Topics:** Array, Math, Matrix  
**Description:** Rotate matrix 90 degrees  
**Why Practice:** In-place matrix transformation

### 29. Spiral Matrix
**Link:** https://leetcode.com/problems/spiral-matrix/  
**Pattern:** Matrix Traversal  
**Topics:** Array, Matrix, Simulation  
**Description:** Return elements in spiral order  
**Why Practice:** Boundary tracking in traversal

### 30. Jump Game
**Link:** https://leetcode.com/problems/jump-game/  
**Pattern:** Greedy  
**Topics:** Array, Dynamic Programming, Greedy  
**Description:** Check if can reach last index  
**Why Practice:** Greedy approach to reachability

### 31. Minimum Window Substring
**Link:** https://leetcode.com/problems/minimum-window-substring/  
**Pattern:** Sliding Window  
**Topics:** String, Hash Table, Sliding Window  
**Description:** Find minimum window containing all characters  
**Why Practice:** Advanced sliding window with two hash maps

### 32. Subarray Sum Equals K
**Link:** https://leetcode.com/problems/subarray-sum-equals-k/  
**Pattern:** Prefix Sum + Hash Map  
**Topics:** Array, Hash Table, Prefix Sum  
**Description:** Count subarrays with sum K  
**Why Practice:** Prefix sum with hash map technique

### 33. Find All Anagrams in a String
**Link:** https://leetcode.com/problems/find-all-anagrams-in-a-string/  
**Pattern:** Sliding Window  
**Topics:** String, Hash Table, Sliding Window  
**Description:** Find all anagram start indices  
**Why Practice:** Fixed-size sliding window

### 34. Group Anagrams
**Link:** https://leetcode.com/problems/group-anagrams/  
**Pattern:** Hash Map  
**Topics:** Array, Hash Table, String, Sorting  
**Description:** Group strings that are anagrams  
**Why Practice:** Using sorted string as key

### 35. Sort Colors
**Link:** https://leetcode.com/problems/sort-colors/  
**Pattern:** Two Pointers (Dutch Flag)  
**Topics:** Array, Two Pointers, Sorting  
**Description:** Sort array with 0s, 1s, 2s  
**Why Practice:** Dutch national flag algorithm

### 36. Search in Rotated Sorted Array
**Link:** https://leetcode.com/problems/search-in-rotated-sorted-array/  
**Pattern:** Modified Binary Search  
**Topics:** Array, Binary Search  
**Description:** Search in rotated array  
**Why Practice:** Binary search variation

### 37. Find First and Last Position of Element
**Link:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/  
**Pattern:** Binary Search  
**Topics:** Array, Binary Search  
**Description:** Find range of target  
**Why Practice:** Binary search boundaries

### 38. Rotate Array
**Link:** https://leetcode.com/problems/rotate-array/  
**Pattern:** Array Rotation  
**Topics:** Array, Math, Two Pointers  
**Description:** Rotate array k steps  
**Why Practice:** Reversal technique

### 39. Next Permutation
**Link:** https://leetcode.com/problems/next-permutation/  
**Pattern:** Array Manipulation  
**Topics:** Array, Two Pointers  
**Description:** Find next lexicographic permutation  
**Why Practice:** Complex in-place manipulation

### 40. 3Sum Closest
**Link:** https://leetcode.com/problems/3sum-closest/  
**Pattern:** Two Pointers  
**Topics:** Array, Two Pointers, Sorting  
**Description:** Find three numbers closest to target  
**Why Practice:** Variation of 3Sum

### 41. 4Sum
**Link:** https://leetcode.com/problems/4sum/  
**Pattern:** Two Pointers  
**Topics:** Array, Two Pointers, Sorting  
**Description:** Find all unique quadruplets  
**Why Practice:** Extending k-sum pattern

### 42. Remove Duplicates from Sorted Array II
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/  
**Pattern:** Two Pointers  
**Topics:** Array, Two Pointers  
**Description:** Allow at most two duplicates  
**Why Practice:** Counting with two pointers

### 43. Search a 2D Matrix II
**Link:** https://leetcode.com/problems/search-a-2d-matrix-ii/  
**Pattern:** Matrix Search  
**Topics:** Array, Binary Search, Matrix, Divide and Conquer  
**Description:** Search in row/column sorted matrix  
**Why Practice:** Staircase search technique

### 44. Set Matrix Zeroes
**Link:** https://leetcode.com/problems/set-matrix-zeroes/  
**Pattern:** Matrix Manipulation  
**Topics:** Array, Hash Table, Matrix  
**Description:** Set row/column to zero  
**Why Practice:** In-place with O(1) space

### 45. Longest Increasing Subsequence
**Link:** https://leetcode.com/problems/longest-increasing-subsequence/  
**Pattern:** Dynamic Programming + Binary Search  
**Topics:** Array, Binary Search, Dynamic Programming  
**Description:** Find LIS length  
**Why Practice:** DP with binary search optimization

### 46. Maximum Subarray
**Link:** https://leetcode.com/problems/maximum-subarray/  
**Pattern:** Kadane's Algorithm  
**Topics:** Array, Divide and Conquer, Dynamic Programming  
**Description:** Find contiguous subarray with largest sum  
**Why Practice:** Kadane's algorithm

### 47. Maximum Product Subarray
**Link:** https://leetcode.com/problems/maximum-product-subarray/  
**Pattern:** Dynamic Programming  
**Topics:** Array, Dynamic Programming  
**Description:** Find contiguous subarray with largest product  
**Why Practice:** Tracking both min and max

### 48. Kth Largest Element in an Array
**Link:** https://leetcode.com/problems/kth-largest-element-in-an-array/  
**Pattern:** QuickSelect  
**Topics:** Array, Divide and Conquer, Sorting, Heap  
**Description:** Find kth largest element  
**Why Practice:** QuickSelect algorithm

### 49. Find Peak Element
**Link:** https://leetcode.com/problems/find-peak-element/  
**Pattern:** Binary Search  
**Topics:** Array, Binary Search  
**Description:** Find peak element  
**Why Practice:** Binary search on unsorted array

### 50. Permutation in String
**Link:** https://leetcode.com/problems/permutation-in-string/  
**Pattern:** Sliding Window  
**Topics:** String, Hash Table, Two Pointers, Sliding Window  
**Description:** Check if s2 contains permutation of s1  
**Why Practice:** Anagram detection with sliding window

---

## Hard Problems (15)

### 51. Median of Two Sorted Arrays
**Link:** https://leetcode.com/problems/median-of-two-sorted-arrays/  
**Pattern:** Binary Search  
**Topics:** Array, Binary Search, Divide and Conquer  
**Description:** Find median of two sorted arrays  
**Why Practice:** Binary search on two arrays, partitioning

### 52. Trapping Rain Water
**Link:** https://leetcode.com/problems/trapping-rain-water/  
**Pattern:** Two Pointers  
**Topics:** Array, Two Pointers, Dynamic Programming, Stack  
**Description:** Calculate trapped rainwater  
**Why Practice:** Multiple solution approaches

### 53. First Missing Positive
**Link:** https://leetcode.com/problems/first-missing-positive/  
**Pattern:** Index Marking  
**Topics:** Array, Hash Table  
**Description:** Find smallest missing positive  
**Why Practice:** O(1) space constant time technique

### 54. Substring with Concatenation of All Words
**Link:** https://leetcode.com/problems/substring-with-concatenation-of-all-words/  
**Pattern:** Sliding Window + Hash Map  
**Topics:** String, Hash Table, Sliding Window  
**Description:** Find substring with all word concatenations  
**Why Practice:** Complex sliding window

### 55. Text Justification
**Link:** https://leetcode.com/problems/text-justification/  
**Pattern:** String Manipulation  
**Topics:** Array, String, Simulation  
**Description:** Justify text to fit width  
**Why Practice:** Complex string formatting, edge cases

### 56. Maximum Gap
**Link:** https://leetcode.com/problems/maximum-gap/  
**Pattern:** Bucket Sort  
**Topics:** Array, Sorting, Bucket Sort  
**Description:** Find maximum difference in sorted array  
**Why Practice:** Bucket sort application

### 57. Sliding Window Maximum
**Link:** https://leetcode.com/problems/sliding-window-maximum/  
**Pattern:** Monotonic Queue  
**Topics:** Array, Queue, Sliding Window, Heap, Monotonic Queue  
**Description:** Max in each sliding window  
**Why Practice:** Monotonic deque technique

### 58. Minimum Window Subsequence
**Link:** https://leetcode.com/problems/minimum-window-subsequence/  
**Pattern:** Two Pointers  
**Topics:** String, Dynamic Programming, Sliding Window  
**Description:** Find minimum window subsequence  
**Why Practice:** Advanced two pointers

### 59. Shortest Subarray with Sum at Least K
**Link:** https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/  
**Pattern:** Monotonic Queue + Prefix Sum  
**Topics:** Array, Binary Search, Queue, Sliding Window, Heap, Prefix Sum, Monotonic Queue  
**Description:** Find shortest subarray with sum >= K  
**Why Practice:** Combining multiple techniques

### 60. Count of Smaller Numbers After Self
**Link:** https://leetcode.com/problems/count-of-smaller-numbers-after-self/  
**Pattern:** Merge Sort / Binary Indexed Tree  
**Topics:** Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort  
**Description:** Count smaller elements to the right  
**Why Practice:** Advanced sorting techniques

### 61. Longest Substring with At Most K Distinct Characters
**Link:** https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/  
**Pattern:** Sliding Window  
**Topics:** String, Hash Table, Sliding Window  
**Description:** Find longest substring with <= K distinct chars  
**Why Practice:** Variable size sliding window (Premium problem)

### 62. Subarrays with K Different Integers
**Link:** https://leetcode.com/problems/subarrays-with-k-different-integers/  
**Pattern:** Sliding Window  
**Topics:** Array, Hash Table, Sliding Window, Counting  
**Description:** Count subarrays with exactly K distinct  
**Why Practice:** At most K - at most K-1 technique

### 63. Minimum Number of K Consecutive Bit Flips
**Link:** https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/  
**Pattern:** Sliding Window + Greedy  
**Topics:** Array, Bit Manipulation, Sliding Window, Prefix Sum  
**Description:** Minimum flips to make all 1s  
**Why Practice:** Greedy with sliding window

### 64. Max Value of Equation
**Link:** https://leetcode.com/problems/max-value-of-equation/  
**Pattern:** Monotonic Queue  
**Topics:** Array, Queue, Sliding Window, Heap, Monotonic Queue  
**Description:** Maximize yi + yj + |xi - xj|  
**Why Practice:** Monotonic queue optimization

### 65. Longest Duplicate Substring
**Link:** https://leetcode.com/problems/longest-duplicate-substring/  
**Pattern:** Binary Search + Rabin-Karp  
**Topics:** String, Binary Search, Sliding Window, Rolling Hash, Suffix Array  
**Description:** Find longest duplicate substring  
**Why Practice:** Rolling hash technique

---

## Practice Progression

### Week 1-2: Foundation (Easy Problems)
Focus on problems 1-20. Master basic patterns:
- Two pointers (problems 5, 6, 7, 9, 10, 11)
- Hash table basics (problems 1, 3, 4, 17)
- String manipulation (problems 12, 13, 14)

### Week 3-4: Intermediate (Easy + Medium)
Add problems 21-35. Focus on:
- Advanced two pointers (21, 22, 35)
- Sliding window (23, 31, 33, 50)
- Array manipulation (27, 28, 29)

### Week 5-6: Advanced Medium
Problems 36-50. Master:
- Binary search variations (36, 37, 49)
- Complex array manipulation (38, 39, 44)
- DP basics (45, 46, 47)

### Week 7-8: Hard Problems
Problems 51-65. Challenge yourself:
- Start with 51, 52, 53 (most common in interviews)
- Move to 57, 60 (advanced techniques)
- Tackle 65 (combines multiple concepts)

---

## Similar Problems

### Two Pointers Family
- Two Sum II (Easy)
- 4Sum (Medium)
- Trapping Rain Water (Hard)

### Sliding Window Family
- Minimum Size Subarray Sum (Medium)
- Fruits Into Baskets (Medium)
- Longest Repeating Character Replacement (Medium)

### Array Manipulation Family
- Merge Intervals (Medium)
- Insert Interval (Medium)
- Meeting Rooms II (Medium)

---

## Tips for Success

1. **Start Easy:** Don't skip easy problems - they build intuition
2. **Identify Patterns:** Tag problems by pattern as you solve them
3. **Time Yourself:** Easy (15min), Medium (30min), Hard (45min)
4. **Review Solutions:** Learn from editorial and top solutions
5. **Revisit Problems:** Solve again after 1 week, 1 month
6. **Track Progress:** Use a spreadsheet to mark completed problems

---

**Total Practice Time Estimate:** 60-80 hours for all 65 problems  
**Recommended Pace:** 5-8 problems per week  
**Mastery Timeline:** 8-12 weeks with consistent practice

