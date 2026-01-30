# Chapter 39: Searching - Exercises

## Instructions

- Try to solve each problem without looking at the solution first
- Start with Easy problems, then progress to Medium and Hard
- For each problem, analyze the time and space complexity
- Multiple approaches are encouraged

Solutions are available in `solutions.md`.

---

## Easy Problems

### E1: Binary Search

**LeetCode**: https://leetcode.com/problems/binary-search/

```python
def search(nums: List[int], target: int) -> int:
    """
    Example: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    """
    pass
```

### E2: Search Insert Position

**LeetCode**: https://leetcode.com/problems/search-insert-position/

```python
def search_insert(nums: List[int], target: int) -> int:
    """
    Example: nums = [1,3,5,6], target = 5
    Output: 2
    """
    pass
```

### E3: Sqrt(x)

**LeetCode**: https://leetcode.com/problems/sqrtx/

```python
def my_sqrt(x: int) -> int:
    """
    Example: x = 8
    Output: 2
    """
    pass
```

### E4: First Bad Version

**LeetCode**: https://leetcode.com/problems/first-bad-version/

```python
def first_bad_version(n: int) -> int:
    """
    Example: n = 5, bad = 4
    Output: 4
    """
    pass
```

### E5: Valid Perfect Square

**LeetCode**: https://leetcode.com/problems/valid-perfect-square/

```python
def is_perfect_square(num: int) -> bool:
    """
    Example: num = 16
    Output: True
    """
    pass
```

### E6: Guess Number Higher or Lower

**LeetCode**: https://leetcode.com/problems/guess-number-higher-or-lower/

```python
def guess_number(n: int) -> int:
    """
    Example: n = 10, pick = 6
    Output: 6
    """
    pass
```

### E7: Peak Index in a Mountain Array

**LeetCode**: https://leetcode.com/problems/peak-index-in-a-mountain-array/

```python
def peak_index_in_mountain_array(arr: List[int]) -> int:
    """
    Example: arr = [0,1,0]
    Output: 1
    """
    pass
```

---

## Medium Problems

### M1: Find First and Last Position

**LeetCode**: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

```python
def search_range(nums: List[int], target: int) -> List[int]:
    """
    Example: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    """
    pass
```

### M2: Search in Rotated Sorted Array

**LeetCode**: https://leetcode.com/problems/search-in-rotated-sorted-array/

```python
def search(nums: List[int], target: int) -> int:
    """
    Example: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    """
    pass
```

### M3: Find Minimum in Rotated Sorted Array

**LeetCode**: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

```python
def find_min(nums: List[int]) -> int:
    """
    Example: nums = [3,4,5,1,2]
    Output: 1
    """
    pass
```

### M4: Find Peak Element

**LeetCode**: https://leetcode.com/problems/find-peak-element/

```python
def find_peak_element(nums: List[int]) -> int:
    """
    Example: nums = [1,2,3,1]
    Output: 2
    """
    pass
```

### M5: Search a 2D Matrix

**LeetCode**: https://leetcode.com/problems/search-a-2d-matrix/

```python
def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    Example: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: True
    """
    pass
```

### M6: Koko Eating Bananas

**LeetCode**: https://leetcode.com/problems/koko-eating-bananas/

```python
def min_eating_speed(piles: List[int], h: int) -> int:
    """
    Example: piles = [3,6,7,11], h = 8
    Output: 4
    """
    pass
```

### M7: Capacity To Ship Packages

**LeetCode**: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

```python
def ship_within_days(weights: List[int], days: int) -> int:
    """
    Example: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    Output: 15
    """
    pass
```

### M8: Split Array Largest Sum

**LeetCode**: https://leetcode.com/problems/split-array-largest-sum/

```python
def split_array(nums: List[int], k: int) -> int:
    """
    Example: nums = [7,2,5,10,8], k = 2
    Output: 18
    """
    pass
```

### M9: Minimum Number of Days to Make m Bouquets

**LeetCode**: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

```python
def min_days(bloom_day: List[int], m: int, k: int) -> int:
    """
    Example: bloomDay = [1,10,3,10,2], m = 3, k = 1
    Output: 3
    """
    pass
```

### M10: Find K Closest Elements

**LeetCode**: https://leetcode.com/problems/find-k-closest-elements/

```python
def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    """
    Example: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]
    """
    pass
```

---

## Hard Problems

### H1: Median of Two Sorted Arrays

**LeetCode**: https://leetcode.com/problems/median-of-two-sorted-arrays/

```python
def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Example: nums1 = [1,3], nums2 = [2]
    Output: 2.0
    """
    pass
```

### H2: Find in Mountain Array

**LeetCode**: https://leetcode.com/problems/find-in-mountain-array/

```python
def find_in_mountain_array(target: int, mountain_arr: 'MountainArray') -> int:
    """
    Example: array = [1,2,3,4,5,3,1], target = 3
    Output: 2
    """
    pass
```

### H3: Kth Smallest Number in Multiplication Table

**LeetCode**: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

```python
def find_kth_number(m: int, n: int, k: int) -> int:
    """
    Example: m = 3, n = 3, k = 5
    Output: 3
    """
    pass
```

### H4: Minimize Max Distance to Gas Station

**LeetCode**: https://leetcode.com/problems/minimize-max-distance-to-gas-station/

```python
def min_max_gas_dist(stations: List[int], k: int) -> float:
    """
    Example: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
    Output: 0.50000
    """
    pass
```

### H5: Shortest Path to Get All Keys

**LeetCode**: https://leetcode.com/problems/shortest-path-to-get-all-keys/

```python
def shortest_path_all_keys(grid: List[str]) -> int:
    """
    Binary search + BFS combination
    """
    pass
```

---

## Summary

**Key Patterns:**
- Standard Binary Search
- Find Boundaries
- Binary Search on Answer
- Rotated Arrays
- 2D Matrix
- Peak Finding

Practice these to master binary search!
