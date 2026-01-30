# Chapter 39: Searching - Tips and Tricks

## Table of Contents
1. [Common Pitfalls](#common-pitfalls)
2. [Pattern Recognition](#pattern-recognition)
3. [Binary Search Templates](#binary-search-templates)
4. [Interview Tips](#interview-tips)
5. [Performance Optimization](#performance-optimization)
6. [LeetCode Practice Problems](#leetcode-practice-problems)

---

## Common Pitfalls

### 1. Integer Overflow in Mid Calculation

```python
# ❌ WRONG: Can overflow in languages like Java/C++
mid = (left + right) // 2  # left + right can overflow

# ✅ CORRECT: Avoids overflow
mid = left + (right - left) // 2

# ✅ ALTERNATIVE: Bit shift (same as //2)
mid = (left + right) >> 1
```

### 2. Infinite Loop with Wrong Update

```python
# ❌ WRONG: Can cause infinite loop
while left < right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid  # Infinite loop if left+1 == right!
    else:
        right = mid - 1

# ✅ CORRECT: Always make progress
while left < right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1  # Always advance
    else:
        right = mid
```

### 3. Off-by-One Errors

```python
# ❌ WRONG: Missing the last element
while left < right:  # Should be left <= right for inclusive search
    ...

# ❌ WRONG: Wrong range initialization
left, right = 0, len(arr)  # Should be len(arr) - 1 for inclusive

# ✅ CORRECT: Consistent with boundary conditions
left, right = 0, len(arr) - 1
while left <= right:
    ...
```

### 4. Not Handling Edge Cases

```python
# ❌ WRONG: No empty array check
def search(nums, target):
    left, right = 0, len(nums) - 1
    # Crashes if nums is empty!

# ✅ CORRECT: Handle edge cases
def search(nums, target):
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    # Rest of implementation
```

### 5. Wrong Condition for Finding Boundaries

```python
# Finding first occurrence
# ❌ WRONG: Returns any occurrence
while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == target:
        return mid  # Could be any occurrence!

# ✅ CORRECT: Continues searching left
while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == target:
        result = mid
        right = mid - 1  # Keep searching left
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return result
```

### 6. Using Binary Search on Unsorted Data

```python
# ❌ WRONG: Binary search requires sorted data
arr = [5, 2, 8, 1, 9]
binary_search(arr, 8)  # May return wrong result!

# ✅ CORRECT: Sort first or use linear search
arr.sort()  # O(n log n)
binary_search(arr, 8)

# OR use linear search for unsorted data
linear_search(arr, 8)  # O(n)
```

---

## Pattern Recognition

### Pattern 1: Standard Binary Search

**When to use:**
- Sorted array
- Find exact match
- Can check mid directly

```python
def binary_search_standard(nums, target):
    """Template for exact match."""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

**Problems:** LeetCode 704, 374

---

### Pattern 2: Finding Boundaries

**When to use:**
- Find first/last occurrence
- Find insertion position
- Handle duplicates

```python
def find_boundary_left(nums, target):
    """Find leftmost position of target."""
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid  # Could be the answer

    return left

def find_boundary_right(nums, target):
    """Find rightmost position of target."""
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left - 1  # Last position where nums[i] == target
```

**Problems:** LeetCode 34, 35, 278

---

### Pattern 3: Binary Search on Answer

**When to use:**
- Minimize/maximize something
- Answer has monotonic property
- Can check if answer X works

```python
def binary_search_on_answer(min_ans, max_ans, is_valid):
    """
    Find minimum/maximum answer satisfying condition.

    Args:
        min_ans: Minimum possible answer
        max_ans: Maximum possible answer
        is_valid: Function returning True if answer works

    Returns:
        Best answer, or -1 if none found
    """
    result = -1

    while min_ans <= max_ans:
        mid = min_ans + (max_ans - min_ans) // 2

        if is_valid(mid):
            result = mid
            max_ans = mid - 1  # Try smaller (for minimum)
            # OR: min_ans = mid + 1 for maximum
        else:
            min_ans = mid + 1  # OR: max_ans = mid - 1

    return result
```

**Example: Koko Eating Bananas**
```python
def min_eating_speed(piles, h):
    """
    Find minimum eating speed to finish in h hours.
    """
    def can_finish(speed):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed  # Ceiling division
        return hours <= h

    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2
        if can_finish(mid):
            right = mid  # Try smaller speed
        else:
            left = mid + 1

    return left
```

**Problems:** LeetCode 69, 875, 1011, 410, 1482

---

### Pattern 4: Rotated/Modified Arrays

**When to use:**
- Rotated sorted array
- Modified sorted structure
- Need to identify sorted portion

```python
def search_rotated(nums, target):
    """Search in rotated sorted array."""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Identify which half is sorted
        if nums[left] <= nums[mid]:  # Left is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

**Problems:** LeetCode 33, 81, 153, 154

---

### Pattern 5: Peak Finding

**When to use:**
- Find local maximum/minimum
- Unimodal array

```python
def find_peak_element(nums):
    """Find any peak element."""
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid  # Peak is on left (or at mid)
        else:
            left = mid + 1  # Peak is on right

    return left
```

**Problems:** LeetCode 162, 852, 1095

---

### Pattern 6: 2D Matrix Search

**When to use:**
- Sorted 2D matrix
- Can treat as 1D array

```python
def search_matrix(matrix, target):
    """
    Search in row-wise and column-wise sorted matrix.
    Treat as 1D sorted array.
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        row, col = mid // n, mid % n  # Convert to 2D

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
```

**Alternative: Staircase Search**
```python
def search_matrix_staircase(matrix, target):
    """
    Start from top-right or bottom-left.
    Time: O(m + n)
    """
    if not matrix or not matrix[0]:
        return False

    row, col = 0, len(matrix[0]) - 1  # Top-right

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False
```

**Problems:** LeetCode 74, 240

---

## Binary Search Templates

### Template 1: Exact Match (left <= right)

**Use for:** Finding exact target

```python
def template1(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

**Key points:**
- Loop: `left <= right`
- Update: `left = mid + 1` or `right = mid - 1`
- Termination: `left > right`
- Post-processing: None needed

---

### Template 2: Find Boundary (left < right)

**Use for:** Lower bound, upper bound, insert position

```python
def template2(nums, target):
    left, right = 0, len(nums)  # Note: right = len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid  # Don't exclude mid

    return left
```

**Key points:**
- Loop: `left < right`
- Update: `left = mid + 1` or `right = mid`
- Termination: `left == right`
- Post-processing: Check `left` if needed

---

### Template 3: Three Elements (left + 1 < right)

**Use for:** Comparing with neighbors, avoid adjacent elements

```python
def template3(nums, target):
    if not nums:
        return -1

    left, right = 0, len(nums) - 1

    while left + 1 < right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right

    return -1
```

**Key points:**
- Loop: `left + 1 < right`
- Update: `left = mid` or `right = mid` (no +1/-1)
- Termination: `left` and `right` are adjacent
- Post-processing: Check both `left` and `right`

---

## Interview Tips

### 1. Clarify the Problem

**Questions to ask:**
- Is the array sorted?
- Are there duplicates?
- What should I return if not found?
- What's the size range of input?
- Are there any special cases?

### 2. Choose the Right Template

**Decision tree:**
```
Can I check mid directly for answer?
├─ Yes → Use Template 1 (left <= right)
└─ No → Continue

Do I need to find a boundary/position?
├─ Yes → Use Template 2 (left < right)
└─ No → Continue

Do I need to compare with neighbors?
├─ Yes → Use Template 3 (left + 1 < right)
└─ No → Reconsider approach
```

### 3. Identify Binary Search Opportunities

**Signs that binary search might work:**
- "Find minimum/maximum X such that..."
- "Given sorted array..."
- "In O(log n) time..."
- Can eliminate half of search space
- Monotonic property exists

**Not obvious binary search:**
- Minimize maximum (e.g., split array largest sum)
- Maximize minimum (e.g., magnetic force between balls)
- Capacity/speed problems (e.g., Koko eating bananas)

### 4. Test Edge Cases

```python
# Always test:
test_cases = [
    [],                    # Empty array
    [1],                   # Single element
    [1, 1, 1, 1],         # All same
    [1, 2, 3, 4, 5],      # Already sorted
    [5, 4, 3, 2, 1],      # Reverse sorted
    [1, 2, 2, 3],         # Duplicates
]

# For rotated arrays:
rotated_tests = [
    [1, 2, 3, 4, 5],      # Not rotated
    [2, 3, 4, 5, 1],      # Rotated once
    [5, 1, 2, 3, 4],      # Rotated to extreme
]
```

### 5. Explain Your Approach

**Good interview answer structure:**
1. Identify why binary search works
2. Explain the monotonic property
3. Describe search space and update logic
4. State time and space complexity
5. Walk through example

**Example:**
```
"This problem can use binary search because:
1. The array is sorted
2. If mid element is less than target, answer must be in right half
3. We can eliminate half the search space each iteration
4. Time complexity: O(log n)
5. Space complexity: O(1)

Let me trace through an example..."
```

---

## Performance Optimization

### 1. Use Python's bisect Module

```python
import bisect

# Instead of implementing binary search
def find_insert_position(nums, target):
    # Custom implementation...
    pass

# Use bisect
def find_insert_position(nums, target):
    return bisect.bisect_left(nums, target)

# bisect functions:
# bisect_left(arr, x)   # Leftmost position to insert x
# bisect_right(arr, x)  # Rightmost position to insert x
# insort_left(arr, x)   # Insert x at leftmost position
# insort_right(arr, x)  # Insert x at rightmost position
```

### 2. Avoid Redundant Calculations

```python
# ❌ SLOW: Recalculate length each iteration
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        ...

# ✅ FAST: Calculate once
def search(nums, target):
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        ...
```

### 3. Early Termination

```python
# Check if target is in valid range
def search(nums, target):
    if not nums or target < nums[0] or target > nums[-1]:
        return -1

    # Proceed with binary search
    ...
```

### 4. Iterative vs Recursive

```python
# ✅ FASTER: Iterative (O(1) space)
def iterative_bs(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ❌ SLOWER: Recursive (O(log n) space)
def recursive_bs(nums, target, left=0, right=None):
    if right is None:
        right = len(nums) - 1
    if left > right:
        return -1

    mid = left + (right - left) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return recursive_bs(nums, target, mid + 1, right)
    else:
        return recursive_bs(nums, target, left, mid - 1)
```

---

## LeetCode Practice Problems

### Easy Problems (15 problems)

#### 1. Binary Search
**Link:** https://leetcode.com/problems/binary-search/
**Pattern:** Standard Binary Search
**Topics:** Binary Search, Array
**Description:** Classic binary search implementation
**Why Practice:** Foundation - must know this perfectly

#### 2. Search Insert Position
**Link:** https://leetcode.com/problems/search-insert-position/
**Pattern:** Find Boundary
**Topics:** Binary Search, Array
**Description:** Find position to insert target
**Why Practice:** Learn boundary finding

#### 3. Sqrt(x)
**Link:** https://leetcode.com/problems/sqrtx/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, Math
**Description:** Find integer square root
**Why Practice:** First binary search on answer problem

#### 4. First Bad Version
**Link:** https://leetcode.com/problems/first-bad-version/
**Pattern:** Find Boundary
**Topics:** Binary Search, Interactive
**Description:** Find first bad version
**Why Practice:** Classic boundary finding

#### 5. Valid Perfect Square
**Link:** https://leetcode.com/problems/valid-perfect-square/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, Math
**Description:** Check if number is perfect square
**Why Practice:** Binary search for verification

#### 6. Guess Number Higher or Lower
**Link:** https://leetcode.com/problems/guess-number-higher-or-lower/
**Pattern:** Standard Binary Search
**Topics:** Binary Search, Interactive
**Description:** Guess game using binary search
**Why Practice:** Interactive binary search

#### 7. Two Sum II - Input Array Is Sorted
**Link:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
**Pattern:** Two Pointers / Binary Search
**Topics:** Array, Two Pointers, Binary Search
**Description:** Two sum on sorted array
**Why Practice:** Binary search application

#### 8. Find Smallest Letter Greater Than Target
**Link:** https://leetcode.com/problems/find-smallest-letter-greater-than-target/
**Pattern:** Upper Bound
**Topics:** Binary Search, Array
**Description:** Find next greater letter
**Why Practice:** Upper bound practice

#### 9. Peak Index in a Mountain Array
**Link:** https://leetcode.com/problems/peak-index-in-a-mountain-array/
**Pattern:** Peak Finding
**Topics:** Binary Search, Array
**Description:** Find peak in mountain array
**Why Practice:** Peak finding pattern

#### 10. Count Negative Numbers in a Sorted Matrix
**Link:** https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
**Pattern:** Binary Search / Staircase
**Topics:** Binary Search, Matrix
**Description:** Count negatives in sorted matrix
**Why Practice:** 2D binary search

#### 11. Arranging Coins
**Link:** https://leetcode.com/problems/arranging-coins/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, Math
**Description:** Find rows that can be formed
**Why Practice:** Mathematical binary search

#### 12. Intersection of Two Arrays
**Link:** https://leetcode.com/problems/intersection-of-two-arrays/
**Pattern:** Binary Search / Hash Set
**Topics:** Binary Search, Hash Table
**Description:** Find intersection of arrays
**Why Practice:** Binary search for membership

#### 13. Intersection of Two Arrays II
**Link:** https://leetcode.com/problems/intersection-of-two-arrays-ii/
**Pattern:** Binary Search / Two Pointers
**Topics:** Binary Search, Hash Table
**Description:** Intersection with duplicates
**Why Practice:** Binary search with counting

#### 14. Fair Candy Swap
**Link:** https://leetcode.com/problems/fair-candy-swap/
**Pattern:** Binary Search / Hash Set
**Topics:** Binary Search, Array
**Description:** Find fair swap for equal sums
**Why Practice:** Binary search for pair

#### 15. Special Array With X Elements
**Link:** https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, Array
**Description:** Find special value
**Why Practice:** Counting with binary search

---

### Medium Problems (25 problems)

#### 16. Find First and Last Position of Element
**Link:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
**Pattern:** Find Boundaries
**Topics:** Binary Search, Array
**Description:** Find range of target in sorted array
**Why Practice:** Essential boundary finding problem

#### 17. Search in Rotated Sorted Array
**Link:** https://leetcode.com/problems/search-in-rotated-sorted-array/
**Pattern:** Modified Binary Search
**Topics:** Binary Search, Array
**Description:** Search in rotated array
**Why Practice:** Classic modified binary search

#### 18. Find Minimum in Rotated Sorted Array
**Link:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
**Pattern:** Modified Binary Search
**Topics:** Binary Search, Array
**Description:** Find minimum in rotated array
**Why Practice:** Identify sorted portion

#### 19. Find Peak Element
**Link:** https://leetcode.com/problems/find-peak-element/
**Pattern:** Peak Finding
**Topics:** Binary Search, Array
**Description:** Find any peak element
**Why Practice:** Peak finding technique

#### 20. Search a 2D Matrix
**Link:** https://leetcode.com/problems/search-a-2d-matrix/
**Pattern:** 2D Binary Search
**Topics:** Binary Search, Matrix
**Description:** Search in row/column sorted matrix
**Why Practice:** Convert 2D to 1D

#### 21. Search a 2D Matrix II
**Link:** https://leetcode.com/problems/search-a-2d-matrix-ii/
**Pattern:** Staircase Search
**Topics:** Binary Search, Matrix
**Description:** Search in sorted matrix
**Why Practice:** Staircase algorithm

#### 22. Koko Eating Bananas
**Link:** https://leetcode.com/problems/koko-eating-bananas/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, Array
**Description:** Minimum eating speed
**Why Practice:** Essential BS on answer problem

#### 23. Capacity To Ship Packages
**Link:** https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, Array
**Description:** Minimum capacity to ship in D days
**Why Practice:** Capacity problem pattern

#### 24. Split Array Largest Sum
**Link:** https://leetcode.com/problems/split-array-largest-sum/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, DP, Greedy
**Description:** Minimize largest sum of splits
**Why Practice:** Hard but important pattern

#### 25. Minimum Number of Days to Make Bouquets
**Link:** https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, Array
**Description:** Minimum days to make bouquets
**Why Practice:** Time-based binary search

#### 26. Find Right Interval
**Link:** https://leetcode.com/problems/find-right-interval/
**Pattern:** Binary Search + Sorting
**Topics:** Binary Search, Sorting
**Description:** Find next non-overlapping interval
**Why Practice:** Interval + binary search

#### 27. Single Element in a Sorted Array
**Link:** https://leetcode.com/problems/single-element-in-a-sorted-array/
**Pattern:** Modified Binary Search
**Topics:** Binary Search, Bit Manipulation
**Description:** Find single element in pairs
**Why Practice:** Clever binary search application

#### 28. Find K Closest Elements
**Link:** https://leetcode.com/problems/find-k-closest-elements/
**Pattern:** Binary Search + Two Pointers
**Topics:** Binary Search, Two Pointers
**Description:** Find k closest to target
**Why Practice:** Binary search for window

#### 29. Kth Smallest Element in a Sorted Matrix
**Link:** https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, Matrix, Heap
**Description:** Kth smallest in matrix
**Why Practice:** Binary search on value range

#### 30. Find the Duplicate Number
**Link:** https://leetcode.com/problems/find-the-duplicate-number/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, Two Pointers
**Description:** Find duplicate in array
**Why Practice:** Non-obvious binary search

#### 31. H-Index II
**Link:** https://leetcode.com/problems/h-index-ii/
**Pattern:** Binary Search
**Topics:** Binary Search, Array
**Description:** H-index in sorted citations
**Why Practice:** Binary search for metric

#### 32. Valid Triangle Number
**Link:** https://leetcode.com/problems/valid-triangle-number/
**Pattern:** Binary Search / Two Pointers
**Topics:** Binary Search, Array
**Description:** Count valid triangles
**Why Practice:** Binary search for counting

#### 33. Random Pick with Weight
**Link:** https://leetcode.com/problems/random-pick-with-weight/
**Pattern:** Binary Search + Prefix Sum
**Topics:** Binary Search, Random, Prefix Sum
**Description:** Weighted random selection
**Why Practice:** Prefix sum + binary search

#### 34. Time Based Key-Value Store
**Link:** https://leetcode.com/problems/time-based-key-value-store/
**Pattern:** Binary Search + HashMap
**Topics:** Binary Search, Hash Table, Design
**Description:** Get value at timestamp
**Why Practice:** Binary search in data structure

#### 35. Find Minimum in Rotated Sorted Array II
**Link:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
**Pattern:** Modified Binary Search
**Topics:** Binary Search, Array
**Description:** Find min with duplicates
**Why Practice:** Handle duplicates in rotation

#### 36. Search in Rotated Sorted Array II
**Link:** https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
**Pattern:** Modified Binary Search
**Topics:** Binary Search, Array
**Description:** Search in rotated with duplicates
**Why Practice:** Complex rotation handling

#### 37. Find Positive Integer Solution
**Link:** https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/
**Pattern:** Binary Search
**Topics:** Binary Search, Math
**Description:** Find solutions to equation
**Why Practice:** Binary search on function

#### 38. Maximum Value at a Given Index
**Link:** https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, Greedy
**Description:** Maximize value with sum constraint
**Why Practice:** Complex constraint checking

#### 39. Magnetic Force Between Two Balls
**Link:** https://leetcode.com/problems/magnetic-force-between-two-balls/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, Array
**Description:** Maximize minimum distance
**Why Practice:** Max-min pattern

#### 40. Minimize Maximum Pair Sum
**Link:** https://leetcode.com/problems/minimize-maximum-of-pair-sums-in-array/
**Pattern:** Binary Search / Greedy
**Topics:** Array, Two Pointers, Greedy
**Description:** Minimize maximum pair sum
**Why Practice:** Sorting + pairing strategy

---

### Hard Problems (12 problems)

#### 41. Find in Mountain Array
**Link:** https://leetcode.com/problems/find-in-mountain-array/
**Pattern:** Multiple Binary Searches
**Topics:** Binary Search, Array, Interactive
**Description:** Find in mountain array
**Why Practice:** Combine peak finding + search

#### 42. Median of Two Sorted Arrays
**Link:** https://leetcode.com/problems/median-of-two-sorted-arrays/
**Pattern:** Binary Search
**Topics:** Binary Search, Divide and Conquer
**Description:** Find median of two sorted arrays
**Why Practice:** Classic hard binary search problem

#### 43. Kth Smallest Number in Multiplication Table
**Link:** https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, Math
**Description:** Kth element in multiplication table
**Why Practice:** Binary search with counting formula

#### 44. Count of Smaller Numbers After Self (using Merge Sort)
**Link:** https://leetcode.com/problems/count-of-smaller-numbers-after-self/
**Pattern:** Merge Sort / Binary Search
**Topics:** Binary Search, Divide and Conquer
**Description:** Count smaller elements on right
**Why Practice:** Binary search tree or merge sort

#### 45. Ugly Number III
**Link:** https://leetcode.com/problems/ugly-number-iii/
**Pattern:** Binary Search on Answer
**Topics:** Binary Search, Math
**Description:** Find nth ugly number
**Why Practice:** Inclusion-exclusion with binary search

#### 46. Smallest Range Covering Elements from K Lists
**Link:** https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
**Pattern:** Binary Search / Sliding Window
**Topics:** Binary Search, Heap, Sliding Window
**Description:** Find smallest range covering all lists
**Why Practice:** Complex multi-list problem

#### 47. Count of Range Sum
**Link:** https://leetcode.com/problems/count-of-range-sum/
**Pattern:** Merge Sort / Binary Search Tree
**Topics:** Binary Search, Divide and Conquer
**Description:** Count subarray sums in range
**Why Practice:** Advanced counting technique

#### 48. Maximize Distance to Closest Person
**Link:** https://leetcode.com/problems/maximize-distance-to-closest-person/
**Pattern:** Binary Search / Math
**Topics:** Array
**Description:** Maximize distance to occupied seat
**Why Practice:** Max distance problem

#### 49. Russian Doll Envelopes
**Link:** https://leetcode.com/problems/russian-doll-envelopes/
**Pattern:** Binary Search + LIS
**Topics:** Binary Search, DP, Sorting
**Description:** Longest increasing subsequence in 2D
**Why Practice:** Sort + binary search for LIS

#### 50. Max Sum of Rectangle No Larger Than K
**Link:** https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
**Pattern:** Binary Search + Prefix Sum
**Topics:** Binary Search, DP, Matrix
**Description:** Maximum sum with constraint
**Why Practice:** Complex 2D binary search

#### 51. Shortest Subarray with Sum at Least K
**Link:** https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
**Pattern:** Monotonic Deque / Binary Search
**Topics:** Binary Search, Sliding Window, Deque
**Description:** Shortest subarray with sum >= k
**Why Practice:** Advanced sliding window

#### 52. Minimum Window Subsequence
**Link:** https://leetcode.com/problems/minimum-window-subsequence/
**Pattern:** Two Pointers / DP
**Topics:** String, Dynamic Programming
**Description:** Minimum window containing subsequence
**Why Practice:** Binary search for window size

---

## Pattern Mastery Checklist

### Core Patterns

- [ ] **Standard Binary Search**
  - Master: #1 (Binary Search)
  - Template: `left <= right`
  - Must know by heart

- [ ] **Find Boundaries**
  - Master: #2 (Insert Position), #4 (First Bad), #16 (Find Range)
  - Template: `left < right`
  - Handle duplicates

- [ ] **Binary Search on Answer**
  - Master: #3 (Sqrt), #22 (Koko), #23 (Ship Capacity), #24 (Split Array)
  - Pattern: Search answer space, not array
  - Check if answer works

- [ ] **Rotated Array**
  - Master: #17 (Search Rotated), #18 (Find Min)
  - Practice: #35, #36 (with duplicates)
  - Identify sorted portion

- [ ] **Peak Finding**
  - Master: #9 (Mountain Peak), #19 (Peak Element)
  - Practice: #41 (Find in Mountain)
  - Compare with neighbors

- [ ] **2D Matrix**
  - Master: #20 (2D Matrix I), #21 (2D Matrix II)
  - Practice: #29 (Kth Smallest Matrix)
  - Convert to 1D or staircase

- [ ] **Modified Binary Search**
  - Master: #27 (Single Element), #30 (Find Duplicate)
  - Practice: Problems with special properties

### Must-Know Problems

**Top 20 for Interviews:**
1. Binary Search (#1)
2. Search Insert Position (#2)
3. First Bad Version (#4)
4. Find Range (#16)
5. Search Rotated Array (#17)
6. Find Min Rotated (#18)
7. Find Peak Element (#19)
8. Search 2D Matrix (#20)
9. Koko Eating Bananas (#22)
10. Ship Capacity (#23)
11. Split Array Largest Sum (#24)
12. Single Element (#27)
13. Kth Closest Elements (#28)
14. Kth Smallest Matrix (#29)
15. Find in Mountain (#41)
16. Median Two Arrays (#42)
17. Sqrt(x) (#3)
18. 2D Matrix II (#21)
19. Time Based Store (#34)
20. Find Duplicate (#30)

---

## Practice Progression

### Week 1: Foundations (Easy)
**Goal:** Master basic binary search

- Day 1-2: #1, #2, #3 (Standard binary search)
- Day 3-4: #4, #5, #6 (Boundary finding)
- Day 5-6: #7, #8, #9 (Applications)
- Day 7: #10, #11, #12, #13, #14, #15 (Review)

### Week 2: Intermediate (Medium 1/2)
**Goal:** Learn variations and patterns

- Day 8-9: #16 (Find Range - crucial!)
- Day 10-11: #17, #18 (Rotated arrays)
- Day 12-13: #19, #20, #21 (Peak and 2D)
- Day 14-15: #22, #23 (BS on answer intro)
- Day 16-17: #24, #25 (BS on answer advanced)
- Day 18-19: #26, #27, #28 (Special cases)
- Day 20-21: #29, #30 (Complex problems)

### Week 3: Advanced (Medium 2/2 + Hard)
**Goal:** Master complex applications

- Day 22-23: #31, #32, #33, #34 (Medium practice)
- Day 24-25: #35, #36, #37, #38, #39, #40 (More medium)
- Day 26-27: #41, #42 (Hard - mountain, median)
- Day 28-29: #43, #44, #45 (Hard - counting)
- Day 30-31: #46-#52 (Remaining hard problems)

### Total Time Estimate
- Easy (15): ~15-20 hours
- Medium (25): ~40-50 hours
- Hard (12): ~25-35 hours
- **Total: 80-105 hours for complete mastery**

---

## Interview Preparation Checklist

### Before Interview

- [ ] Can implement binary search from memory (all 3 templates)
- [ ] Know when to use each template
- [ ] Understand binary search on answer pattern
- [ ] Can handle rotated arrays
- [ ] Can find peaks and boundaries
- [ ] Know Python's bisect module
- [ ] Practiced 40+ problems

### During Interview

- [ ] Identify if binary search is appropriate
- [ ] Choose correct template
- [ ] Explain monotonic property
- [ ] Handle mid calculation (avoid overflow)
- [ ] Check loop termination conditions
- [ ] Test edge cases
- [ ] State time/space complexity

### After Interview

- [ ] Review problems you struggled with
- [ ] Identify which template to use
- [ ] Understand why binary search worked
- [ ] Practice similar problems
- [ ] Add to review list

---

## Summary

**Binary search is essential** - appears in 20-25% of coding interviews!

**Key Takeaways:**
1. **Master the templates**: Three templates for different scenarios
2. **Binary search on answer**: Powerful pattern for optimization problems
3. **Identify monotonicity**: Key to recognizing binary search opportunities
4. **Common variations**: Rotated arrays, peaks, boundaries, 2D matrices
5. **Time complexity**: Always O(log n) for search, but check verification
6. **Practice**: 50+ problems to master all patterns

**Most Important Patterns:**
- Standard binary search (exact match)
- Find boundaries (first/last occurrence)
- Binary search on answer (minimize/maximize)
- Rotated array search
- Peak finding
- 2D matrix search

**Practice Strategy:**
- Implement all three templates from memory
- Do 15 easy problems first
- Master "binary search on answer" pattern
- Practice 25 medium problems
- Challenge yourself with 12 hard problems
- Review must-know 20 problems before interview

Good luck with your binary search mastery journey!
