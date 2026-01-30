# Chapter 38: Sorting - Tips and Tricks

## Table of Contents
1. [Common Pitfalls](#common-pitfalls)
2. [Pattern Recognition](#pattern-recognition)
3. [Interview Tips](#interview-tips)
4. [Performance Optimization](#performance-optimization)
5. [LeetCode Practice Problems](#leetcode-practice-problems)

---

## Common Pitfalls

### 1. Using Wrong Sorting Algorithm

```python
# ❌ WRONG: Using bubble sort for large arrays
def sort_large_array(nums):
    # O(n²) - too slow!
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

# ✅ CORRECT: Use appropriate algorithm
def sort_large_array(nums):
    return sorted(nums)  # Timsort O(n log n)
```

### 2. Ignoring Stability Requirements

```python
# ❌ WRONG: Using unstable sort when stability matters
students = [('Alice', 25), ('Bob', 25), ('Charlie', 25)]
students.sort(key=lambda x: x[1])  # Stable in Python
# But implementing custom quicksort would be unstable!

# ✅ CORRECT: Use stable sort (merge sort, Timsort)
students.sort(key=lambda x: x[1])  # Python's sort is stable
```

### 3. Modifying Array While Iterating

```python
# ❌ WRONG: Modifying during iteration
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        nums.remove(nums[i])  # Changes indices!

# ✅ CORRECT: Use separate result or iterate backwards
result = [x for x in nums if x % 2 != 0]
```

### 4. Inefficient Custom Comparators

```python
# ❌ WRONG: Expensive comparison function
def bad_sort(words):
    return sorted(words, key=lambda x: sorted(x))  # O(n² log n)

# ✅ CORRECT: Cache expensive computations
def good_sort(words):
    # Pre-compute keys if needed multiple times
    return sorted(words, key=lambda x: ''.join(sorted(x)))
```

### 5. Not Handling Edge Cases

```python
# ❌ WRONG: Assuming array is non-empty
def find_kth_largest(nums, k):
    return sorted(nums)[-k]  # Fails if k > len(nums)!

# ✅ CORRECT: Handle edge cases
def find_kth_largest(nums, k):
    if not nums or k > len(nums):
        return None
    return sorted(nums)[-k]
```

### 6. Integer Overflow in Comparators

```python
# ❌ WRONG: Can overflow with large numbers
def compare(a, b):
    return a - b  # Overflow possible!

# ✅ CORRECT: Use comparison operators
def compare(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0
```

---

## Pattern Recognition

### Pattern 1: When to Use Each Sort

#### Use Insertion Sort
```python
# Small arrays (n < 50)
if len(nums) < 50:
    return insertion_sort(nums)

# Nearly sorted data
def sort_nearly_sorted(nums, k):
    """Elements are at most k positions away from sorted position."""
    import heapq
    result = []
    heap = nums[:k+1]
    heapq.heapify(heap)

    for i in range(k+1, len(nums)):
        result.append(heapq.heappop(heap))
        heapq.heappush(heap, nums[i])

    while heap:
        result.append(heapq.heappop(heap))

    return result
```

#### Use Quick Sort/Quickselect
```python
# Finding kth element
def find_kth_largest(nums, k):
    """Quickselect: O(n) average."""
    # Implementation shown in solutions
    pass

# In-place sorting needed
def sort_inplace(nums):
    """Quick sort is in-place."""
    quick_sort(nums, 0, len(nums)-1)
```

#### Use Merge Sort
```python
# Need stability
def stable_sort(items):
    """Merge sort is stable."""
    return merge_sort(items)

# Counting inversions
def count_inversions(nums):
    """Use merge sort to count inversions."""
    # Implementation in solutions
    pass

# Sorting linked lists
def sort_list(head):
    """Merge sort works well on linked lists."""
    # No random access needed
    pass
```

#### Use Counting/Radix Sort
```python
# Small integer range
def sort_small_range(nums):
    """O(n + k) when k is small."""
    if max(nums) - min(nums) < len(nums):
        return counting_sort(nums)
    return sorted(nums)

# Fixed-length integers
def sort_integers(nums):
    """Radix sort for integers."""
    return radix_sort(nums)
```

---

### Pattern 2: Custom Comparisons

#### Multi-Key Sorting
```python
# Sort by multiple criteria
students = [('Alice', 25, 'A'), ('Bob', 20, 'B'), ('Charlie', 25, 'C')]

# Method 1: Tuple comparison
sorted(students, key=lambda x: (x[1], x[0]))  # By age, then name

# Method 2: Multiple sorts (stable)
students.sort(key=lambda x: x[0])  # First by name
students.sort(key=lambda x: x[1])  # Then by age (stable!)

# Method 3: itemgetter (fastest)
from operator import itemgetter
sorted(students, key=itemgetter(1, 0))
```

#### Custom Order
```python
# Sort by custom alphabet
def alien_order_sort(words, order):
    """Sort words by custom alphabet."""
    order_map = {c: i for i, c in enumerate(order)}
    return sorted(words, key=lambda w: [order_map[c] for c in w])

# Sort by frequency then value
from collections import Counter

def sort_by_frequency(nums):
    freq = Counter(nums)
    return sorted(nums, key=lambda x: (-freq[x], x))
```

#### Reverse and Conditional Sorting
```python
# Partial reverse
def sort_with_conditions(nums):
    """Sort evens ascending, odds descending."""
    evens = sorted([x for x in nums if x % 2 == 0])
    odds = sorted([x for x in nums if x % 2 == 1], reverse=True)
    return evens + odds

# Sort by absolute value
sorted(nums, key=abs)

# Sort by distance from target
target = 10
sorted(nums, key=lambda x: abs(x - target))
```

---

### Pattern 3: Sorting with Constraints

#### In-Place Sorting
```python
# Dutch National Flag (3 colors)
def sort_colors(nums):
    """Three-way partitioning."""
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Two-way partitioning
def partition(nums, pivot):
    """Partition around pivot value."""
    left = 0
    right = len(nums) - 1

    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

#### Partial Sorting
```python
# Top K elements (don't need full sort)
import heapq

def top_k_elements(nums, k):
    """O(n log k) instead of O(n log n)."""
    return heapq.nlargest(k, nums)

# Sort only first k elements
def partial_sort(nums, k):
    """Only sort first k elements."""
    # Use min heap of size k
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    return sorted(heap)
```

---

### Pattern 4: Sorting for Other Algorithms

#### Sorting for Binary Search
```python
def search_optimized(nums, target):
    """Sort once, search many times."""
    nums.sort()  # O(n log n) once

    # Now can binary search in O(log n)
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

#### Sorting for Two Pointers
```python
def two_sum_sorted(nums, target):
    """Sort to enable two pointers."""
    nums.sort()
    left, right = 0, len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    return []

def three_sum(nums):
    """Sort for 3Sum problem."""
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # Two pointers for remaining elements
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result
```

---

## Interview Tips

### 1. Clarify Requirements

**Questions to ask:**
- What's the size of the input? (Small vs large)
- Are there duplicates?
- What's the range of values? (Small range → counting sort)
- Is stability required?
- Is in-place sorting required?
- What's more important: time or space?

### 2. Choose Right Algorithm

**Decision tree:**
```
Is n small (< 50)?
├─ Yes → Insertion Sort
└─ No → Continue

Is data nearly sorted?
├─ Yes → Insertion Sort or Timsort
└─ No → Continue

Are elements small integers?
├─ Yes → Counting Sort or Radix Sort
└─ No → Continue

Is stability required?
├─ Yes → Merge Sort or Timsort
└─ No → Quick Sort or Heap Sort

Need in-place?
├─ Yes → Quick Sort or Heap Sort
└─ No → Merge Sort

Default: Use Python's sorted() (Timsort)
```

### 3. Analyze Complexity

Always state both time and space complexity:
```python
# ✅ Good interview answer
"""
Time Complexity: O(n log n) for sorting, O(n) for iteration
Space Complexity: O(n) for storing sorted array
Total: O(n log n) time, O(n) space
"""
```

### 4. Consider Trade-offs

```python
# Example: Finding kth largest

# Approach 1: Full sort
def kth_largest_v1(nums, k):
    """Time: O(n log n), Space: O(1)"""
    nums.sort()
    return nums[-k]

# Approach 2: Min heap
def kth_largest_v2(nums, k):
    """Time: O(n log k), Space: O(k)"""
    import heapq
    return heapq.nlargest(k, nums)[-1]

# Approach 3: Quickselect
def kth_largest_v3(nums, k):
    """Time: O(n) average, Space: O(1)"""
    # Quickselect implementation
    pass

# Explain trade-offs in interview!
```

### 5. Test Edge Cases

```python
# Always test:
# 1. Empty array
# 2. Single element
# 3. All same elements
# 4. Already sorted
# 5. Reverse sorted
# 6. Duplicates

def test_sorting():
    assert sort([]) == []
    assert sort([1]) == [1]
    assert sort([1,1,1]) == [1,1,1]
    assert sort([1,2,3]) == [1,2,3]
    assert sort([3,2,1]) == [1,2,3]
    assert sort([1,2,2,3]) == [1,2,2,3]
```

---

## Performance Optimization

### 1. Use Built-in Functions

```python
# ❌ Slower: Custom implementation
def sort_slow(nums):
    # Your merge sort implementation
    pass

# ✅ Faster: Built-in Timsort
def sort_fast(nums):
    return sorted(nums)  # Highly optimized!

# ✅ Fastest: In-place
def sort_fastest(nums):
    nums.sort()  # No copy overhead
```

### 2. Optimize Key Functions

```python
# ❌ Slow: Recompute key multiple times
def slow_sort(words):
    return sorted(words, key=lambda x: len(x) + sum(ord(c) for c in x))

# ✅ Fast: Simple key function
def fast_sort(words):
    # Pre-compute if needed many times
    keys = {w: (len(w), sum(ord(c) for c in w)) for w in words}
    return sorted(words, key=lambda x: keys[x])

# ✅ Fastest: Use built-in functions
def fastest_sort(words):
    return sorted(words, key=len)  # Built-in len is fast
```

### 3. Avoid Unnecessary Sorts

```python
# ❌ Inefficient: Multiple sorts
def process_data(nums):
    nums.sort()  # O(n log n)
    result1 = nums[:10]  # Top 10

    nums.sort(reverse=True)  # O(n log n) again!
    result2 = nums[:10]  # Bottom 10

    return result1, result2

# ✅ Efficient: Single sort
def process_data(nums):
    nums.sort()  # O(n log n) once
    return nums[:10], nums[-10:]
```

### 4. Use Appropriate Data Structures

```python
# For maintaining sorted data dynamically
import bisect

sorted_list = []

# Insert maintaining order: O(n)
bisect.insort(sorted_list, new_element)

# Better: Use heap for top-k
import heapq

heap = []
for num in nums:
    heapq.heappush(heap, num)  # O(log n)

# Best for sorted stream: Use SortedList (from sortedcontainers)
from sortedcontainers import SortedList

sl = SortedList()
sl.add(item)  # O(log n)
```

---

## LeetCode Practice Problems

### Easy Problems (12 problems)

#### 1. Sort an Array
**Link:** https://leetcode.com/problems/sort-an-array/
**Pattern:** Basic Sorting
**Topics:** Merge Sort, Quick Sort, Heap Sort
**Description:** Sort an array in ascending order
**Why Practice:** Implement sorting algorithms from scratch

#### 2. Merge Sorted Array
**Link:** https://leetcode.com/problems/merge-sorted-array/
**Pattern:** Two Pointers
**Topics:** Sorting, Two Pointers
**Description:** Merge two sorted arrays in-place
**Why Practice:** Learn to merge efficiently from back

#### 3. Squares of a Sorted Array
**Link:** https://leetcode.com/problems/squares-of-a-sorted-array/
**Pattern:** Two Pointers
**Topics:** Sorting, Two Pointers
**Description:** Return sorted squares of sorted array
**Why Practice:** Two pointers on sorted data

#### 4. Sort Array By Parity
**Link:** https://leetcode.com/problems/sort-array-by-parity/
**Pattern:** Two Pointers
**Topics:** Sorting, Array
**Description:** Move evens before odds
**Why Practice:** In-place partitioning

#### 5. Sort Array By Parity II
**Link:** https://leetcode.com/problems/sort-array-by-parity-ii/
**Pattern:** Two Pointers
**Topics:** Sorting, Array
**Description:** Evens at even indices, odds at odd indices
**Why Practice:** Conditional in-place sorting

#### 6. Relative Sort Array
**Link:** https://leetcode.com/problems/relative-sort-array/
**Pattern:** Custom Sort
**Topics:** Sorting, Hash Table
**Description:** Sort based on reference array
**Why Practice:** Custom ordering with counting sort

#### 7. Sort Colors
**Link:** https://leetcode.com/problems/sort-colors/
**Pattern:** Dutch National Flag
**Topics:** Two Pointers, Sorting
**Description:** Sort array of 0s, 1s, 2s
**Why Practice:** Classic three-way partitioning

#### 8. Intersection of Two Arrays II
**Link:** https://leetcode.com/problems/intersection-of-two-arrays-ii/
**Pattern:** Sorting + Two Pointers
**Topics:** Sorting, Hash Table
**Description:** Find intersection with duplicates
**Why Practice:** Sorting for efficient intersection

#### 9. Valid Anagram
**Link:** https://leetcode.com/problems/valid-anagram/
**Pattern:** Sorting for Comparison
**Topics:** Sorting, Hash Table, String
**Description:** Check if two strings are anagrams
**Why Practice:** Sorting for string comparison

#### 10. Height Checker
**Link:** https://leetcode.com/problems/height-checker/
**Pattern:** Sorting for Comparison
**Topics:** Sorting, Array
**Description:** Count positions different from sorted
**Why Practice:** Compare with sorted version

#### 11. Minimum Absolute Difference
**Link:** https://leetcode.com/problems/minimum-absolute-difference/
**Pattern:** Sorting for Comparison
**Topics:** Sorting, Array
**Description:** Find pairs with minimum absolute difference
**Why Practice:** Sorting to find min difference

#### 12. Maximum Product of Three Numbers
**Link:** https://leetcode.com/problems/maximum-product-of-three-numbers/
**Pattern:** Sorting for Selection
**Topics:** Sorting, Math, Array
**Description:** Maximum product of three numbers
**Why Practice:** Consider edge cases with negatives

---

### Medium Problems (20 problems)

#### 13. Sort Characters By Frequency
**Link:** https://leetcode.com/problems/sort-characters-by-frequency/
**Pattern:** Frequency Sort
**Topics:** Hash Table, Heap, Bucket Sort
**Description:** Sort string by character frequency
**Why Practice:** Bucket sort for frequency problems

#### 14. Top K Frequent Elements
**Link:** https://leetcode.com/problems/top-k-frequent-elements/
**Pattern:** Frequency Sort, Heap
**Topics:** Hash Table, Heap, Bucket Sort
**Description:** Find k most frequent elements
**Why Practice:** Essential heap/bucket sort problem

#### 15. Sort List
**Link:** https://leetcode.com/problems/sort-list/
**Pattern:** Merge Sort
**Topics:** Linked List, Merge Sort
**Description:** Sort linked list in O(n log n)
**Why Practice:** Merge sort on linked lists

#### 16. Kth Largest Element in an Array
**Link:** https://leetcode.com/problems/kth-largest-element-in-an-array/
**Pattern:** Quickselect, Heap
**Topics:** Divide and Conquer, Heap
**Description:** Find kth largest element
**Why Practice:** Master quickselect algorithm

#### 17. Largest Number
**Link:** https://leetcode.com/problems/largest-number/
**Pattern:** Custom Comparator
**Topics:** Sorting, String
**Description:** Arrange numbers to form largest number
**Why Practice:** Custom comparison function

#### 18. H-Index
**Link:** https://leetcode.com/problems/h-index/
**Pattern:** Sorting, Counting
**Topics:** Sorting, Array
**Description:** Calculate h-index from citations
**Why Practice:** Sorting for metric calculation

#### 19. Sort an Array
**Link:** https://leetcode.com/problems/sort-an-array/
**Pattern:** Implement Sorting
**Topics:** Merge Sort, Quick Sort, Heap Sort
**Description:** Implement efficient sorting
**Why Practice:** Fundamental sorting implementation

#### 20. 3Sum
**Link:** https://leetcode.com/problems/3sum/
**Pattern:** Sorting + Two Pointers
**Topics:** Array, Two Pointers, Sorting
**Description:** Find all triplets summing to zero
**Why Practice:** Classic sorting + two pointers

#### 21. 4Sum
**Link:** https://leetcode.com/problems/4sum/
**Pattern:** Sorting + Two Pointers
**Topics:** Array, Two Pointers, Sorting
**Description:** Find all quadruplets summing to target
**Why Practice:** Extension of 3Sum pattern

#### 22. Wiggle Sort
**Link:** https://leetcode.com/problems/wiggle-sort/
**Pattern:** In-place Swapping
**Topics:** Sorting, Array
**Description:** Create wiggle pattern
**Why Practice:** O(n) in-place sorting

#### 23. Wiggle Sort II
**Link:** https://leetcode.com/problems/wiggle-sort-ii/
**Pattern:** Quickselect + Virtual Indexing
**Topics:** Divide and Conquer, Sorting
**Description:** Create strict wiggle pattern
**Why Practice:** Advanced partitioning technique

#### 24. Maximum Gap
**Link:** https://leetcode.com/problems/maximum-gap/
**Pattern:** Bucket Sort
**Topics:** Sorting, Bucket Sort
**Description:** Find maximum gap in sorted array
**Why Practice:** Linear time with bucket sort

#### 25. Sort Transformed Array
**Link:** https://leetcode.com/problems/sort-transformed-array/
**Pattern:** Two Pointers
**Topics:** Math, Two Pointers, Sorting
**Description:** Sort array after quadratic transformation
**Why Practice:** Understand function properties

#### 26. Reordered Power of 2
**Link:** https://leetcode.com/problems/reordered-power-of-2/
**Pattern:** Sorting for Comparison
**Topics:** Sorting, Math
**Description:** Check if reordering gives power of 2
**Why Practice:** Sorting for digit comparison

#### 27. Advantage Shuffle
**Link:** https://leetcode.com/problems/advantage-shuffle/
**Pattern:** Greedy + Sorting
**Topics:** Array, Greedy, Sorting
**Description:** Maximize advantages over another array
**Why Practice:** Greedy strategy with sorting

#### 28. Merge Intervals
**Link:** https://leetcode.com/problems/merge-intervals/
**Pattern:** Sorting + Greedy
**Topics:** Array, Sorting
**Description:** Merge overlapping intervals
**Why Practice:** Classic interval problem

#### 29. Insert Interval
**Link:** https://leetcode.com/problems/insert-interval/
**Pattern:** Sorting + Merge
**Topics:** Array, Sorting
**Description:** Insert and merge new interval
**Why Practice:** Interval manipulation

#### 30. Meeting Rooms II
**Link:** https://leetcode.com/problems/meeting-rooms-ii/
**Pattern:** Sorting + Heap
**Topics:** Heap, Greedy, Sorting
**Description:** Minimum meeting rooms needed
**Why Practice:** Sorting events by time

#### 31. Car Fleet
**Link:** https://leetcode.com/problems/car-fleet/
**Pattern:** Sorting + Stack
**Topics:** Stack, Sorting
**Description:** Count car fleets arriving at destination
**Why Practice:** Sort by position, process by time

#### 32. Pancake Sorting
**Link:** https://leetcode.com/problems/pancake-sorting/
**Pattern:** Custom Sort
**Topics:** Array, Sorting, Greedy
**Description:** Sort using pancake flips
**Why Practice:** Unique sorting constraint

---

### Hard Problems (10 problems)

#### 33. Count of Smaller Numbers After Self
**Link:** https://leetcode.com/problems/count-of-smaller-numbers-after-self/
**Pattern:** Merge Sort for Counting
**Topics:** Divide and Conquer, BIT, Segment Tree
**Description:** Count smaller elements to the right
**Why Practice:** Modified merge sort for inversions

#### 34. Reverse Pairs
**Link:** https://leetcode.com/problems/reverse-pairs/
**Pattern:** Merge Sort for Counting
**Topics:** Divide and Conquer, BIT, Segment Tree
**Description:** Count reverse pairs
**Why Practice:** Counting during merge sort

#### 35. Create Maximum Number
**Link:** https://leetcode.com/problems/create-maximum-number/
**Pattern:** Greedy + Stack
**Topics:** Stack, Greedy
**Description:** Create maximum number from two arrays
**Why Practice:** Complex greedy with monotonic stack

#### 36. Count of Range Sum
**Link:** https://leetcode.com/problems/count-of-range-sum/
**Pattern:** Merge Sort + Prefix Sum
**Topics:** Divide and Conquer, BIT, Segment Tree
**Description:** Count range sums in given range
**Why Practice:** Advanced merge sort application

#### 37. Find Median from Data Stream
**Link:** https://leetcode.com/problems/find-median-from-data-stream/
**Pattern:** Two Heaps
**Topics:** Heap, Design
**Description:** Maintain median of stream
**Why Practice:** Essential two-heap pattern

#### 38. Sliding Window Median
**Link:** https://leetcode.com/problems/sliding-window-median/
**Pattern:** Two Heaps/Multiset
**Topics:** Heap, Sliding Window
**Description:** Median of sliding window
**Why Practice:** Dynamic median maintenance

#### 39. Maximum Sum of 3 Non-Overlapping Subarrays
**Link:** https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
**Pattern:** Dynamic Programming
**Topics:** Array, DP
**Description:** Find 3 non-overlapping subarrays with max sum
**Why Practice:** DP with sliding window

#### 40. Best Meeting Point
**Link:** https://leetcode.com/problems/best-meeting-point/
**Pattern:** Median Finding
**Topics:** Math, Sorting
**Description:** Find optimal meeting point
**Why Practice:** Median minimizes distance

#### 41. Russian Doll Envelopes
**Link:** https://leetcode.com/problems/russian-doll-envelopes/
**Pattern:** Sorting + LIS
**Topics:** Binary Search, DP, Sorting
**Description:** Longest increasing subsequence in 2D
**Why Practice:** Sort by one dimension, LIS on other

#### 42. The Skyline Problem
**Link:** https://leetcode.com/problems/the-skyline-problem/
**Pattern:** Sweep Line + Multiset
**Topics:** Heap, Divide and Conquer
**Description:** Generate skyline from buildings
**Why Practice:** Advanced sorting with events

---

## Pattern Mastery Checklist

### Core Patterns

- [ ] **Basic Sorting Algorithms**
  - Master: #1 (Implement merge sort, quick sort, heap sort)
  - Understand: Time/space complexity of each

- [ ] **Two Pointers After Sorting**
  - Master: #2, #3, #4, #7
  - Practice: #20, #21
  - Pattern: Sort first, then use two pointers

- [ ] **Custom Comparators**
  - Master: #17 (Largest Number)
  - Practice: #6 (Relative Sort), #13 (Frequency Sort)
  - Learn: functools.cmp_to_key

- [ ] **Frequency/Counting Sorts**
  - Master: #14 (Top K Frequent)
  - Practice: #13 (Sort by Frequency)
  - Technique: Bucket sort for O(n)

- [ ] **Kth Element (Quickselect)**
  - Master: #16 (Kth Largest)
  - Practice: Quickselect implementation
  - Time: O(n) average case

- [ ] **Sorting Linked Lists**
  - Master: #15 (Sort List)
  - Technique: Merge sort (no random access)

- [ ] **Interval Problems**
  - Master: #28 (Merge Intervals)
  - Practice: #29 (Insert Interval), #30 (Meeting Rooms)
  - Pattern: Sort by start time

- [ ] **Advanced Merge Sort**
  - Master: #33 (Count Smaller)
  - Practice: #34 (Reverse Pairs), #36 (Count Range Sum)
  - Pattern: Count during merge

- [ ] **Two Heaps**
  - Master: #37 (Median from Stream)
  - Practice: #38 (Sliding Window Median)
  - Pattern: Max heap (left) + Min heap (right)

---

## Practice Progression

### Week 1: Fundamentals (Easy)
**Goal:** Master basic sorting concepts

- Day 1-2: #1, #2, #3 (Implement algorithms)
- Day 3-4: #4, #5, #6 (Two pointers, custom sort)
- Day 5-6: #7, #8, #9 (Applications)
- Day 7: #10, #11, #12 (Review and variations)

### Week 2: Intermediate (Medium)
**Goal:** Learn sorting patterns

- Day 8-9: #13, #14 (Frequency sorting)
- Day 10-11: #15, #16 (Linked list, quickselect)
- Day 12-13: #17, #18 (Custom comparators)
- Day 14-15: #20, #21 (Two pointers after sorting)
- Day 16-17: #22, #23 (Wiggle sort)
- Day 18-19: #24, #28, #29 (Bucket sort, intervals)
- Day 20-21: #30, #31, #32 (Review medium problems)

### Week 3: Advanced (Hard)
**Goal:** Master complex applications

- Day 22-23: #33 (Count Smaller - modified merge sort)
- Day 24-25: #34 (Reverse Pairs)
- Day 26-27: #37 (Median from Stream - two heaps)
- Day 28-29: #38, #39 (Sliding window, DP)
- Day 30-31: #40, #41, #42 (Advanced patterns)

### Total Time Estimate
- Easy (12): ~12-15 hours
- Medium (20): ~30-40 hours
- Hard (10): ~20-30 hours
- **Total: 62-85 hours for mastery**

---

## Interview Preparation Checklist

### Before Interview

- [ ] Can implement merge sort from memory
- [ ] Can implement quick sort from memory
- [ ] Understand quickselect algorithm
- [ ] Know when to use each sorting algorithm
- [ ] Master Python's sort with key functions
- [ ] Understand stability and in-place sorting
- [ ] Can implement counting sort for small ranges

### During Interview

- [ ] Ask about input size and constraints
- [ ] Ask if stability is required
- [ ] Ask about space constraints
- [ ] Choose appropriate algorithm
- [ ] Mention time/space complexity
- [ ] Test with edge cases
- [ ] Consider if sorting is necessary

### After Interview

- [ ] Review problems you struggled with
- [ ] Implement alternative approaches
- [ ] Understand why your approach worked/didn't work
- [ ] Add to review list if needed

---

## Summary

**Sorting is fundamental** - appears in 15-20% of coding interviews!

**Key Takeaways:**
1. **Master basic algorithms**: Merge sort, quick sort, heap sort
2. **Use built-in sorts**: Python's Timsort is excellent
3. **Custom comparators**: Essential for complex sorting
4. **Choose wisely**: Algorithm depends on data characteristics
5. **Common patterns**: Two pointers, frequency sorting, intervals
6. **Advanced techniques**: Quickselect, modified merge sort, two heaps

**Most Important Problems:**
- Merge Sorted Array (#2)
- Sort Colors (#7)
- Kth Largest Element (#16)
- Top K Frequent (#14)
- Merge Intervals (#28)
- Count Smaller After Self (#33)
- Median from Stream (#37)

**Practice Strategy:**
- Start with implementing algorithms from scratch
- Master common patterns (two pointers, custom sort)
- Practice 40+ problems across difficulties
- Focus on choosing right algorithm for constraints
- Understand trade-offs between approaches

Good luck with your sorting mastery journey!
