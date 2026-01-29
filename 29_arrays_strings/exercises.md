# Arrays and Strings - Exercises

## 20 Progressive Exercises

### Exercise 1: Three Sum
**Difficulty**: Medium

Find all unique triplets in array that sum to zero.

**Input**: `nums = [-1, 0, 1, 2, -1, -4]`
**Output**: `[[-1, -1, 2], [-1, 0, 1]]`

**Requirements:**
- Time complexity: O(n²)
- Space complexity: O(1) excluding output
- No duplicate triplets
- Use two pointers after sorting

**Hint**: Sort array, fix first element, use two pointers for remaining two.

---

### Exercise 2: Container With Most Water (Variant)
**Difficulty**: Medium

Given n non-negative integers representing heights, find two lines that form container holding most water. Return the maximum area and the indices.

**Input**: `heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
**Output**: `(49, 1, 8)` - area 49 between indices 1 and 8

**Requirements:**
- Time: O(n)
- Space: O(1)
- Return both maximum area and indices

---

### Exercise 3: Minimum Size Subarray Sum
**Difficulty**: Medium

Find minimum length of contiguous subarray with sum ≥ target.

**Input**: `target = 7, nums = [2, 3, 1, 2, 4, 3]`
**Output**: `2` (subarray `[4, 3]`)

**Requirements:**
- Time: O(n)
- Space: O(1)
- Use sliding window
- Return 0 if no such subarray exists

---

### Exercise 4: Longest Substring with At Most K Distinct Characters
**Difficulty**: Medium

Find length of longest substring with at most k distinct characters.

**Input**: `s = "eceba", k = 2`
**Output**: `3` (substring "ece")

**Requirements:**
- Time: O(n)
- Space: O(k)
- Use sliding window
- Also return the substring itself

---

### Exercise 5: Valid Anagram
**Difficulty**: Easy

Check if two strings are anagrams (same characters, different order).

**Input**: `s = "anagram", t = "nagaram"`
**Output**: `True`

**Requirements:**
- Implement three different methods:
  1. Sorting (O(n log n))
  2. Hash map (O(n))
  3. Character array (O(n))
- Compare performance for large strings

---

### Exercise 6: Implement strStr()
**Difficulty**: Medium

Find first occurrence of needle in haystack. Return index or -1.

**Input**: `haystack = "hello", needle = "ll"`
**Output**: `2`

**Requirements:**
- Time: O(n*m) brute force
- Space: O(1)
- Bonus: Implement KMP algorithm for O(n+m)

---

### Exercise 7: Reverse Words in String
**Difficulty**: Medium

Reverse order of words in a string.

**Input**: `"the sky is blue"`
**Output**: `"blue is sky the"`

**Requirements:**
- Time: O(n)
- Space: O(n)
- Remove extra spaces
- Words separated by spaces
- Bonus: In-place solution

---

### Exercise 8: Next Permutation
**Difficulty**: Medium

Find next lexicographically greater permutation of numbers.

**Input**: `[1, 2, 3]`
**Output**: `[1, 3, 2]`

**Input**: `[3, 2, 1]`
**Output**: `[1, 2, 3]` (wrap around)

**Requirements:**
- Time: O(n)
- Space: O(1)
- Modify array in-place
- Handle edge cases (all descending, all same)

---

### Exercise 9: Spiral Matrix
**Difficulty**: Medium

Return all elements of matrix in spiral order.

**Input**:
```
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
```
**Output**: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`

**Requirements:**
- Time: O(m*n)
- Space: O(1) excluding output
- Handle rectangular matrices
- Handle 1xN and Nx1 matrices

---

### Exercise 10: Rotate Image (Matrix)
**Difficulty**: Medium

Rotate n×n matrix 90 degrees clockwise in-place.

**Input**:
```
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```
**Output**:
```
[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
```

**Requirements:**
- Time: O(n²)
- Space: O(1)
- In-place rotation
- Explain the algorithm

---

### Exercise 11: Maximum Subarray (Kadane's Algorithm)
**Difficulty**: Medium

Find contiguous subarray with largest sum.

**Input**: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
**Output**: `6` (subarray `[4, -1, 2, 1]`)

**Requirements:**
- Time: O(n)
- Space: O(1)
- Also return the subarray itself
- Handle all negative numbers

---

### Exercise 12: Merge Intervals
**Difficulty**: Medium

Merge overlapping intervals.

**Input**: `[[1,3], [2,6], [8,10], [15,18]]`
**Output**: `[[1,6], [8,10], [15,18]]`

**Requirements:**
- Time: O(n log n)
- Space: O(n)
- Sort intervals first
- Handle edge cases (empty, single interval)

---

### Exercise 13: Missing Ranges
**Difficulty**: Medium

Find missing ranges between lower and upper bounds.

**Input**: `nums = [0, 1, 3, 50, 75], lower = 0, upper = 99`
**Output**: `["2", "4->49", "51->74", "76->99"]`

**Requirements:**
- Time: O(n)
- Space: O(1) excluding output
- Format single numbers without arrows
- Handle duplicates

---

### Exercise 14: Longest Consecutive Sequence
**Difficulty**: Hard

Find length of longest consecutive sequence (doesn't need to be contiguous in array).

**Input**: `nums = [100, 4, 200, 1, 3, 2]`
**Output**: `4` (sequence [1, 2, 3, 4])

**Requirements:**
- Time: O(n)
- Space: O(n)
- Must be O(n), not O(n log n) with sorting
- Use hash set

---

### Exercise 15: Minimum Window Substring (Extended)
**Difficulty**: Hard

Find minimum window in s containing all characters of t with their frequencies.

**Input**: `s = "ADOBECODEBANC", t = "AABC"`
**Output**: `"ADOBEC"` (contains 2 A's, 1 B, 1 C)

**Requirements:**
- Time: O(n + m)
- Space: O(k)
- Must handle character frequencies
- Return "" if no window exists

---

### Exercise 16: Sliding Window Maximum
**Difficulty**: Hard

Find maximum in each sliding window of size k.

**Input**: `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`
**Output**: `[3, 3, 5, 5, 6, 7]`

**Requirements:**
- Time: O(n)
- Space: O(k)
- Use deque for efficient solution
- Handle edge cases (k = 1, k = n)

---

### Exercise 17: Palindrome Partitioning
**Difficulty**: Hard

Partition string into palindromic substrings. Return all possible partitions.

**Input**: `s = "aab"`
**Output**: `[["a", "a", "b"], ["aa", "b"]]`

**Requirements:**
- Time: O(n * 2^n)
- Space: O(n)
- Use backtracking
- Optimize palindrome checking

---

### Exercise 18: Longest Valid Parentheses
**Difficulty**: Hard

Find length of longest valid (well-formed) parentheses substring.

**Input**: `s = ")()())"`
**Output**: `4` (substring "()()")

**Requirements:**
- Implement two methods:
  1. Stack-based: O(n) time, O(n) space
  2. Two-pass: O(n) time, O(1) space
- Handle edge cases

---

### Exercise 19: Median of Two Sorted Arrays
**Difficulty**: Hard

Find median of two sorted arrays.

**Input**: `nums1 = [1, 3], nums2 = [2]`
**Output**: `2.0`

**Input**: `nums1 = [1, 2], nums2 = [3, 4]`
**Output**: `2.5`

**Requirements:**
- Time: O(log(min(m, n)))
- Space: O(1)
- Use binary search
- Handle empty arrays

---

### Exercise 20: Text Justification
**Difficulty**: Hard

Format text to fit within maxWidth characters per line with full justification.

**Input**: `words = ["This", "is", "an", "example"], maxWidth = 16`
**Output**:
```
[
  "This    is    an",
  "example         "
]
```

**Requirements:**
- Time: O(n)
- Space: O(1) excluding output
- Distribute spaces evenly
- Left-justify last line
- Handle edge cases (single word, exact fit)

---

## Testing Guidelines

### Test Your Solutions

1. **Basic Cases**: Empty, single element, two elements
2. **Edge Cases**: All same, sorted, reverse sorted
3. **Large Cases**: Performance with 10^4 - 10^5 elements
4. **Special Cases**: Negative numbers, duplicates, overflow

### Verification Checklist

- [ ] Handles empty input
- [ ] Handles single element
- [ ] Handles all same elements
- [ ] Handles sorted input
- [ ] Handles reverse sorted input
- [ ] Meets time complexity requirement
- [ ] Meets space complexity requirement
- [ ] No off-by-one errors
- [ ] Proper boundary checks
- [ ] Clean, readable code

### Performance Testing

```python
import time
import random

def test_performance(func, n=10000):
    """Test function performance"""
    arr = [random.randint(1, 1000) for _ in range(n)]

    start = time.time()
    result = func(arr)
    end = time.time()

    print(f"Time for n={n}: {end - start:.4f}s")
    return result

# Example
test_performance(your_solution, 10000)
test_performance(your_solution, 100000)
```

---

## Bonus Challenges

### Bonus 1: K-th Largest Element
Find k-th largest element in unsorted array in O(n) average time using Quickselect.

### Bonus 2: Longest Increasing Subsequence
Find length of longest increasing subsequence in O(n log n) using binary search.

### Bonus 3: Edit Distance
Find minimum operations (insert, delete, replace) to convert string s1 to s2.

### Bonus 4: Wildcard Matching
Implement wildcard pattern matching with '*' and '?'.

### Bonus 5: Regular Expression Matching
Implement regex matching with '.' and '*'.

---

## Hints

### Exercise 1 (Three Sum)
- Sort array first
- Fix first element, use two pointers for other two
- Skip duplicates carefully

### Exercise 3 (Minimum Size Subarray)
- Use two pointers (left, right)
- Expand right, shrink left when sum ≥ target
- Track minimum length

### Exercise 14 (Longest Consecutive)
- Add all numbers to set
- For each number that starts a sequence (num-1 not in set)
- Count consecutive numbers

### Exercise 16 (Sliding Window Maximum)
- Use deque to store indices
- Keep deque in decreasing order
- Front of deque is always maximum

### Exercise 19 (Median of Two Arrays)
- Binary search on smaller array
- Partition both arrays
- Check if partition is valid

---

Good luck! These exercises cover the full spectrum of array and string problems you'll encounter in interviews.
