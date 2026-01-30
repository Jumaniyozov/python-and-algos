# Chapter 38: Sorting - Exercises

## Table of Contents
1. [Easy Problems (1-7)](#easy-problems)
2. [Medium Problems (8-14)](#medium-problems)
3. [Hard Problems (15-20)](#hard-problems)

---

## Easy Problems

### Problem 1: Sort an Array
**Difficulty:** Easy
**Topics:** Sorting, Implementation

Implement a function to sort an array in ascending order using any sorting algorithm of your choice.

```python
def sort_array(nums):
    """
    Sort array in ascending order.

    Args:
        nums: List[int] - Array of integers

    Returns:
        List[int] - Sorted array

    Example:
        >>> sort_array([5, 2, 3, 1])
        [1, 2, 3, 5]
        >>> sort_array([5, 1, 1, 2, 0, 0])
        [0, 0, 1, 1, 2, 5]
    """
    pass
```

---

### Problem 2: Merge Sorted Array
**Difficulty:** Easy
**Topics:** Two Pointers, Sorting

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order. Merge `nums2` into `nums1` as one sorted array.

```python
def merge(nums1, m, nums2, n):
    """
    Merge nums2 into nums1 in-place.

    Args:
        nums1: List[int] - First sorted array with extra space
        m: int - Number of elements in nums1
        nums2: List[int] - Second sorted array
        n: int - Number of elements in nums2

    Returns:
        None - Modify nums1 in-place

    Example:
        >>> nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3
        >>> merge(nums1, m, nums2, n)
        >>> nums1
        [1, 2, 2, 3, 5, 6]
    """
    pass
```

---

### Problem 3: Sort Colors (Dutch National Flag)
**Difficulty:** Medium (but can be Easy)
**Topics:** Two Pointers, Sorting

Given an array `nums` with `n` objects colored red, white, or blue (represented by 0, 1, 2), sort them in-place so that objects of the same color are adjacent.

```python
def sort_colors(nums):
    """
    Sort array of 0s, 1s, and 2s in-place.

    Args:
        nums: List[int] - Array containing only 0, 1, 2

    Returns:
        None - Sort in-place

    Example:
        >>> nums = [2,0,2,1,1,0]
        >>> sort_colors(nums)
        >>> nums
        [0, 0, 1, 1, 2, 2]
    """
    pass
```

---

### Problem 4: Squares of a Sorted Array
**Difficulty:** Easy
**Topics:** Two Pointers, Sorting

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

```python
def sorted_squares(nums):
    """
    Return sorted squares of sorted array.

    Args:
        nums: List[int] - Sorted array (may contain negatives)

    Returns:
        List[int] - Sorted array of squares

    Example:
        >>> sorted_squares([-4, -1, 0, 3, 10])
        [0, 1, 9, 16, 100]
        >>> sorted_squares([-7, -3, 2, 3, 11])
        [4, 9, 9, 49, 121]
    """
    pass
```

---

### Problem 5: Sort Array By Parity
**Difficulty:** Easy
**Topics:** Two Pointers, Sorting

Given an integer array `nums`, move all the even integers to the beginning followed by all the odd integers.

```python
def sort_array_by_parity(nums):
    """
    Move even numbers before odd numbers.

    Args:
        nums: List[int] - Array of integers

    Returns:
        List[int] - Array with evens before odds

    Example:
        >>> sort_array_by_parity([3,1,2,4])
        [2, 4, 3, 1]  # or any arrangement with evens first
    """
    pass
```

---

### Problem 6: Relative Sort Array
**Difficulty:** Easy
**Topics:** Sorting, Hash Table

Given two arrays `arr1` and `arr2`, sort `arr1` such that the relative ordering of items in `arr1` are the same as in `arr2`. Elements not in `arr2` should be placed at the end in ascending order.

```python
def relative_sort_array(arr1, arr2):
    """
    Sort arr1 according to arr2 order.

    Args:
        arr1: List[int] - Array to sort
        arr2: List[int] - Reference order

    Returns:
        List[int] - Sorted array

    Example:
        >>> relative_sort_array([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])
        [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    """
    pass
```

---

### Problem 7: Maximum Gap
**Difficulty:** Medium (but easier with bucket sort)
**Topics:** Sorting, Bucket Sort

Given an integer array `nums`, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

```python
def maximum_gap(nums):
    """
    Find maximum gap between successive elements.

    Args:
        nums: List[int] - Array of integers

    Returns:
        int - Maximum gap

    Example:
        >>> maximum_gap([3,6,9,1])
        3  # Sorted: [1,3,6,9], max gap is 6-3=3
        >>> maximum_gap([10])
        0
    """
    pass
```

---

## Medium Problems

### Problem 8: Largest Number
**Difficulty:** Medium
**Topics:** Sorting, Custom Comparator

Given a list of non-negative integers `nums`, arrange them such that they form the largest number.

```python
def largest_number(nums):
    """
    Arrange numbers to form largest number.

    Args:
        nums: List[int] - Non-negative integers

    Returns:
        str - Largest possible number as string

    Example:
        >>> largest_number([10, 2])
        "210"
        >>> largest_number([3, 30, 34, 5, 9])
        "9534330"
    """
    pass
```

---

### Problem 9: Sort Characters By Frequency
**Difficulty:** Medium
**Topics:** Sorting, Hash Table, Heap

Given a string `s`, sort it in decreasing order based on the frequency of the characters.

```python
def frequency_sort(s):
    """
    Sort string by character frequency.

    Args:
        s: str - Input string

    Returns:
        str - String sorted by frequency

    Example:
        >>> frequency_sort("tree")
        "eert"  # or "eetr"
        >>> frequency_sort("cccaaa")
        "aaaccc"  # or "cccaaa"
    """
    pass
```

---

### Problem 10: H-Index
**Difficulty:** Medium
**Topics:** Sorting, Binary Search

Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their ith paper, return the researcher's h-index.

The h-index is defined as the maximum value of h such that the researcher has published at least h papers that have each been cited at least h times.

```python
def h_index(citations):
    """
    Calculate h-index.

    Args:
        citations: List[int] - Citation counts

    Returns:
        int - H-index

    Example:
        >>> h_index([3, 0, 6, 1, 5])
        3  # 3 papers with >= 3 citations
        >>> h_index([1, 3, 1])
        1
    """
    pass
```

---

### Problem 11: Top K Frequent Elements
**Difficulty:** Medium
**Topics:** Sorting, Hash Table, Heap, Bucket Sort

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

```python
def top_k_frequent(nums, k):
    """
    Find k most frequent elements.

    Args:
        nums: List[int] - Array of integers
        k: int - Number of elements to return

    Returns:
        List[int] - K most frequent elements

    Example:
        >>> top_k_frequent([1,1,1,2,2,3], 2)
        [1, 2]
        >>> top_k_frequent([1], 1)
        [1]
    """
    pass
```

---

### Problem 12: Sort List
**Difficulty:** Medium
**Topics:** Linked List, Merge Sort

Sort a linked list in O(n log n) time and O(1) space.

```python
def sort_list(head):
    """
    Sort linked list using merge sort.

    Args:
        head: ListNode - Head of linked list

    Returns:
        ListNode - Head of sorted list

    Example:
        >>> head = [4,2,1,3]
        >>> sort_list(head)
        [1,2,3,4]
    """
    pass
```

---

### Problem 13: Wiggle Sort
**Difficulty:** Medium
**Topics:** Sorting, Array

Given an integer array `nums`, reorder it such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`

```python
def wiggle_sort(nums):
    """
    Sort array in wiggle pattern.

    Args:
        nums: List[int] - Array of integers

    Returns:
        None - Sort in-place

    Example:
        >>> nums = [3,5,2,1,6,4]
        >>> wiggle_sort(nums)
        >>> nums
        [3, 5, 1, 6, 2, 4]  # or similar wiggle pattern
    """
    pass
```

---

### Problem 14: Kth Largest Element in an Array
**Difficulty:** Medium
**Topics:** Sorting, Heap, Quickselect

Find the kth largest element in an unsorted array.

```python
def find_kth_largest(nums, k):
    """
    Find kth largest element.

    Args:
        nums: List[int] - Array of integers
        k: int - Position (1-indexed)

    Returns:
        int - Kth largest element

    Example:
        >>> find_kth_largest([3,2,1,5,6,4], 2)
        5
        >>> find_kth_largest([3,2,3,1,2,4,5,5,6], 4)
        4
    """
    pass
```

---

## Hard Problems

### Problem 15: Wiggle Sort II
**Difficulty:** Hard
**Topics:** Sorting, Quickselect

Given an integer array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]...`

```python
def wiggle_sort_ii(nums):
    """
    Sort array in strict wiggle pattern.

    Args:
        nums: List[int] - Array of integers

    Returns:
        None - Sort in-place

    Example:
        >>> nums = [1,5,1,1,6,4]
        >>> wiggle_sort_ii(nums)
        >>> nums
        [1, 6, 1, 5, 1, 4]  # One possible answer
    """
    pass
```

---

### Problem 16: Count of Smaller Numbers After Self
**Difficulty:** Hard
**Topics:** Merge Sort, Binary Indexed Tree, Segment Tree

Given an integer array `nums`, return an integer array `counts` where `counts[i]` is the number of smaller elements to the right of `nums[i]`.

```python
def count_smaller(nums):
    """
    Count smaller elements to the right.

    Args:
        nums: List[int] - Array of integers

    Returns:
        List[int] - Counts for each position

    Example:
        >>> count_smaller([5,2,6,1])
        [2, 1, 1, 0]
        >>> count_smaller([-1])
        [0]
    """
    pass
```

---

### Problem 17: Reverse Pairs
**Difficulty:** Hard
**Topics:** Merge Sort, Binary Indexed Tree

Given an integer array `nums`, return the number of reverse pairs in the array.

A reverse pair is a pair `(i, j)` where `i < j` and `nums[i] > 2 * nums[j]`.

```python
def reverse_pairs(nums):
    """
    Count reverse pairs.

    Args:
        nums: List[int] - Array of integers

    Returns:
        int - Number of reverse pairs

    Example:
        >>> reverse_pairs([1,3,2,3,1])
        2
        >>> reverse_pairs([2,4,3,5,1])
        3
    """
    pass
```

---

### Problem 18: Create Maximum Number
**Difficulty:** Hard
**Topics:** Greedy, Stack, Sorting

You are given two integer arrays `nums1` and `nums2` of lengths `m` and `n` respectively. Create the maximum number of length `k <= m + n` from digits of the two arrays while preserving relative order.

```python
def max_number(nums1, nums2, k):
    """
    Create maximum number from two arrays.

    Args:
        nums1: List[int] - First array
        nums2: List[int] - Second array
        k: int - Length of result

    Returns:
        List[int] - Maximum number of length k

    Example:
        >>> max_number([3,4,6,5], [9,1,2,5,8,3], 5)
        [9, 8, 6, 5, 3]
    """
    pass
```

---

### Problem 19: Find Median from Data Stream
**Difficulty:** Hard
**Topics:** Heap, Sorting, Design

Implement MedianFinder class that supports adding numbers and finding median.

```python
class MedianFinder:
    """
    Find median from data stream.

    Example:
        >>> mf = MedianFinder()
        >>> mf.add_num(1)
        >>> mf.add_num(2)
        >>> mf.find_median()
        1.5
        >>> mf.add_num(3)
        >>> mf.find_median()
        2.0
    """

    def __init__(self):
        """Initialize data structure."""
        pass

    def add_num(self, num: int) -> None:
        """Add number to data structure."""
        pass

    def find_median(self) -> float:
        """Return median of all numbers."""
        pass
```

---

### Problem 20: Maximum Sum of 3 Non-Overlapping Subarrays
**Difficulty:** Hard
**Topics:** Dynamic Programming, Sliding Window, Sorting

Find three non-overlapping subarrays of size `k` with maximum sum.

```python
def max_sum_of_three_subarrays(nums, k):
    """
    Find indices of 3 non-overlapping subarrays with max sum.

    Args:
        nums: List[int] - Array of integers
        k: int - Subarray size

    Returns:
        List[int] - Starting indices of 3 subarrays

    Example:
        >>> max_sum_of_three_subarrays([1,2,1,2,6,7,5,1], 2)
        [0, 3, 5]  # Subarrays: [1,2], [2,6], [7,5]
    """
    pass
```

---

## Challenge Problems

### Bonus Problem 1: Pancake Sorting
**Difficulty:** Medium
**Topics:** Sorting, Array

Given an array of integers `arr`, sort the array by performing a series of pancake flips.

```python
def pancake_sort(arr):
    """
    Sort array using pancake flips.
    A pancake flip reverses arr[0:k+1].

    Args:
        arr: List[int] - Array of integers

    Returns:
        List[int] - Sequence of k values for flips

    Example:
        >>> pancake_sort([3,2,4,1])
        [4, 2, 4, 3]  # One possible answer
    """
    pass
```

---

### Bonus Problem 2: Car Fleet
**Difficulty:** Medium
**Topics:** Sorting, Stack

Cars traveling to same destination. Given positions and speeds, calculate number of car fleets that arrive at destination.

```python
def car_fleet(target, position, speed):
    """
    Calculate number of car fleets.

    Args:
        target: int - Destination position
        position: List[int] - Starting positions
        speed: List[int] - Speeds of cars

    Returns:
        int - Number of car fleets

    Example:
        >>> car_fleet(12, [10,8,0,5,3], [2,4,1,1,3])
        3
    """
    pass
```

---

## Tips for Solving

### General Approach

1. **Understand the problem**: What needs to be sorted? What's the goal?
2. **Consider constraints**: Time/space limits, stability requirements
3. **Choose algorithm**: Based on data characteristics
4. **Optimize**: Use appropriate data structures and techniques

### Common Patterns

- **Two pointers**: For in-place sorting (Dutch flag, merge)
- **Custom comparators**: For non-standard ordering
- **Counting/bucket**: For small ranges or frequencies
- **Heap/quickselect**: For kth element problems
- **Merge sort variants**: For counting inversions, smaller elements

### Edge Cases

- Empty array
- Single element
- All same elements
- Already sorted
- Reverse sorted
- Duplicates

---

## Notes

- **Time Limits**: Most problems expect O(n log n) or better
- **Space Limits**: Some problems require O(1) extra space
- **Stability**: Consider whether maintaining relative order matters
- **Practice**: Implement algorithms from scratch to understand mechanics

Good luck with the exercises!
