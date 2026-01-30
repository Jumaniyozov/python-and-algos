# Chapter 39: Searching - Examples

## Table of Contents
1. [Binary Search Basics](#binary-search-basics)
2. [Binary Search Variations](#binary-search-variations)
3. [Binary Search on Answer](#binary-search-on-answer)
4. [Rotated Array Search](#rotated-array-search)
5. [2D Matrix Search](#2d-matrix-search)
6. [Advanced Binary Search](#advanced-binary-search)

---

## Binary Search Basics

### Example 1: Standard Binary Search

```python
def binary_search(nums, target):
    """
    Find target in sorted array.

    Time: O(log n)
    Space: O(1)

    Args:
        nums: Sorted array
        target: Value to find

    Returns:
        Index of target, -1 if not found
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        # Avoid overflow: mid = (left + right) // 2 can overflow in some languages
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Not found


# Example usage:
nums = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(binary_search(nums, 7))   # Output: 3
print(binary_search(nums, 6))   # Output: -1
```

### Example 2: Recursive Binary Search

```python
def binary_search_recursive(nums, target, left=0, right=None):
    """
    Recursive implementation of binary search.

    Time: O(log n)
    Space: O(log n) for recursion stack

    Args:
        nums: Sorted array
        target: Value to find
        left: Left boundary
        right: Right boundary

    Returns:
        Index of target, -1 if not found
    """
    if right is None:
        right = len(nums) - 1

    # Base case: search space exhausted
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


# Example usage:
nums = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
print(binary_search_recursive(nums, 23))  # Output: 5
print(binary_search_recursive(nums, 24))  # Output: -1
```

---

## Binary Search Variations

### Example 3: Find First Occurrence (Lower Bound)

```python
def find_first(nums, target):
    """
    Find first (leftmost) occurrence of target.

    Time: O(log n)
    Space: O(1)

    Args:
        nums: Sorted array (may have duplicates)
        target: Value to find

    Returns:
        Index of first occurrence, -1 if not found
    """
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left for first occurrence
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


# Example usage:
nums = [1, 2, 2, 2, 3, 4, 5]
print(find_first(nums, 2))  # Output: 1 (first occurrence of 2)
```

### Example 4: Find Last Occurrence (Upper Bound)

```python
def find_last(nums, target):
    """
    Find last (rightmost) occurrence of target.

    Time: O(log n)
    Space: O(1)

    Args:
        nums: Sorted array (may have duplicates)
        target: Value to find

    Returns:
        Index of last occurrence, -1 if not found
    """
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right for last occurrence
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


# Example usage:
nums = [1, 2, 2, 2, 3, 4, 5]
print(find_last(nums, 2))  # Output: 3 (last occurrence of 2)
```

### Example 5: Find First and Last Position

```python
def search_range(nums, target):
    """
    Find range [first, last] of target.

    Time: O(log n)
    Space: O(1)

    Args:
        nums: Sorted array
        target: Value to find

    Returns:
        [first_index, last_index], or [-1, -1] if not found
    """
    def find_bound(nums, target, find_first):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                result = mid
                if find_first:
                    right = mid - 1  # Search left
                else:
                    left = mid + 1   # Search right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    first = find_bound(nums, target, True)
    last = find_bound(nums, target, False)

    return [first, last]


# Example usage:
nums = [5, 7, 7, 8, 8, 8, 10]
print(search_range(nums, 8))  # Output: [3, 5]
print(search_range(nums, 6))  # Output: [-1, -1]
```

### Example 6: Search Insert Position

```python
def search_insert(nums, target):
    """
    Find index where target should be inserted to maintain sorted order.

    Time: O(log n)
    Space: O(1)

    Args:
        nums: Sorted array
        target: Value to insert

    Returns:
        Index to insert target
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # When loop exits, left is the insertion position
    return left


# Example usage:
nums = [1, 3, 5, 6]
print(search_insert(nums, 5))  # Output: 2
print(search_insert(nums, 2))  # Output: 1
print(search_insert(nums, 7))  # Output: 4
print(search_insert(nums, 0))  # Output: 0
```

### Example 7: Count Occurrences

```python
def count_occurrences(nums, target):
    """
    Count how many times target appears.

    Time: O(log n)
    Space: O(1)

    Args:
        nums: Sorted array
        target: Value to count

    Returns:
        Number of occurrences
    """
    first = find_first(nums, target)
    if first == -1:
        return 0

    last = find_last(nums, target)
    return last - first + 1


# Example usage:
nums = [1, 2, 2, 2, 3, 4, 5]
print(count_occurrences(nums, 2))  # Output: 3
print(count_occurrences(nums, 6))  # Output: 0
```

---

## Binary Search on Answer

### Example 8: Square Root (Integer)

```python
def my_sqrt(x):
    """
    Find integer square root (floor of sqrt).

    Time: O(log x)
    Space: O(1)

    Args:
        x: Non-negative integer

    Returns:
        Floor of square root
    """
    if x < 2:
        return x

    left, right = 1, x // 2
    result = 0

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            result = mid  # Store as potential answer
            left = mid + 1
        else:
            right = mid - 1

    return result


# Example usage:
print(my_sqrt(8))   # Output: 2 (sqrt(8) ≈ 2.83)
print(my_sqrt(16))  # Output: 4
print(my_sqrt(17))  # Output: 4
```

### Example 9: Koko Eating Bananas

```python
def min_eating_speed(piles, h):
    """
    Find minimum eating speed to finish all bananas in h hours.

    Binary search on answer: speed from 1 to max(piles).

    Time: O(n log m) where m = max(piles)
    Space: O(1)

    Args:
        piles: List of banana piles
        h: Hours available

    Returns:
        Minimum eating speed
    """
    def can_finish(speed):
        """Check if can finish all piles at this speed."""
        hours = 0
        for pile in piles:
            # Ceiling division: (pile + speed - 1) // speed
            hours += (pile + speed - 1) // speed
        return hours <= h

    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2

        if can_finish(mid):
            right = mid  # Try slower speed
        else:
            left = mid + 1  # Need faster speed

    return left


# Example usage:
piles = [3, 6, 7, 11]
h = 8
print(min_eating_speed(piles, h))  # Output: 4
```

### Example 10: Ship Packages Within D Days

```python
def ship_within_days(weights, days):
    """
    Find minimum ship capacity to ship all packages in D days.

    Binary search on answer: capacity from max(weights) to sum(weights).

    Time: O(n log(sum - max))
    Space: O(1)

    Args:
        weights: Package weights
        days: Days available

    Returns:
        Minimum ship capacity
    """
    def can_ship(capacity):
        """Check if can ship all packages with this capacity."""
        days_needed = 1
        current_weight = 0

        for weight in weights:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = weight
            else:
                current_weight += weight

        return days_needed <= days

    left = max(weights)  # Must hold largest package
    right = sum(weights)  # Ship everything in one day

    while left < right:
        mid = left + (right - left) // 2

        if can_ship(mid):
            right = mid  # Try smaller capacity
        else:
            left = mid + 1  # Need larger capacity

    return left


# Example usage:
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(ship_within_days(weights, days))  # Output: 15
```

### Example 11: Split Array Largest Sum

```python
def split_array(nums, k):
    """
    Split array into k subarrays to minimize the largest sum.

    Binary search on answer: sum from max(nums) to sum(nums).

    Time: O(n log(sum - max))
    Space: O(1)

    Args:
        nums: Array of numbers
        k: Number of subarrays

    Returns:
        Minimum largest sum
    """
    def can_split(max_sum):
        """Check if can split into <= k subarrays with max_sum limit."""
        subarrays = 1
        current_sum = 0

        for num in nums:
            if current_sum + num > max_sum:
                subarrays += 1
                current_sum = num
                if subarrays > k:
                    return False
            else:
                current_sum += num

        return True

    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = left + (right - left) // 2

        if can_split(mid):
            right = mid  # Try smaller max sum
        else:
            left = mid + 1  # Need larger max sum

    return left


# Example usage:
nums = [7, 2, 5, 10, 8]
k = 2
print(split_array(nums, k))  # Output: 18
```

---

## Rotated Array Search

### Example 12: Search in Rotated Sorted Array

```python
def search_rotated(nums, target):
    """
    Search in rotated sorted array (no duplicates).

    Time: O(log n)
    Space: O(1)

    Args:
        nums: Rotated sorted array
        target: Value to find

    Returns:
        Index of target, -1 if not found
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Determine which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target in left half
            else:
                left = mid + 1   # Target in right half
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Target in right half
            else:
                right = mid - 1  # Target in left half

    return -1


# Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
print(search_rotated(nums, 0))  # Output: 4
print(search_rotated(nums, 3))  # Output: -1
```

### Example 13: Find Minimum in Rotated Sorted Array

```python
def find_min_rotated(nums):
    """
    Find minimum element in rotated sorted array.

    Time: O(log n)
    Space: O(1)

    Args:
        nums: Rotated sorted array (no duplicates)

    Returns:
        Minimum element
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # If mid > right, minimum is in right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Minimum is in left half or at mid
            right = mid

    return nums[left]


# Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
print(find_min_rotated(nums))  # Output: 0
```

### Example 14: Find Peak Element

```python
def find_peak_element(nums):
    """
    Find a peak element (element greater than neighbors).

    Time: O(log n)
    Space: O(1)

    Args:
        nums: Array of numbers

    Returns:
        Index of a peak element
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[mid + 1]:
            # Peak is in left half (or at mid)
            right = mid
        else:
            # Peak is in right half
            left = mid + 1

    return left


# Example usage:
nums = [1, 2, 3, 1]
print(find_peak_element(nums))  # Output: 2 (peak is 3)

nums = [1, 2, 1, 3, 5, 6, 4]
print(find_peak_element(nums))  # Output: 5 (peak is 6) or 1 (peak is 2)
```

---

## 2D Matrix Search

### Example 15: Search a 2D Matrix (Treat as 1D)

```python
def search_matrix(matrix, target):
    """
    Search in row-wise and column-wise sorted matrix.

    Treat matrix as 1D sorted array.

    Time: O(log(m × n))
    Space: O(1)

    Args:
        matrix: m × n sorted matrix
        target: Value to find

    Returns:
        True if found, False otherwise
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Convert 1D index to 2D coordinates
        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Example usage:
matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
print(search_matrix(matrix, 3))   # Output: True
print(search_matrix(matrix, 13))  # Output: False
```

### Example 16: Search a 2D Matrix II (Staircase)

```python
def search_matrix_ii(matrix, target):
    """
    Search in matrix where rows and columns are sorted independently.

    Staircase algorithm: start from top-right or bottom-left.

    Time: O(m + n)
    Space: O(1)

    Args:
        matrix: m × n matrix
        target: Value to find

    Returns:
        True if found, False otherwise
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1  # Start from top-right

    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False


# Example usage:
matrix = [
    [1,  4,  7, 11, 15],
    [2,  5,  8, 12, 19],
    [3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
print(search_matrix_ii(matrix, 5))   # Output: True
print(search_matrix_ii(matrix, 20))  # Output: False
```

---

## Advanced Binary Search

### Example 17: Find K Closest Elements

```python
def find_closest_elements(arr, k, x):
    """
    Find k closest elements to x.

    Binary search for starting window, then expand.

    Time: O(log n + k)
    Space: O(1)

    Args:
        arr: Sorted array
        k: Number of elements
        x: Target value

    Returns:
        k closest elements as sorted list
    """
    left, right = 0, len(arr) - k

    while left < right:
        mid = left + (right - left) // 2

        # Compare distances: arr[mid] vs arr[mid+k]
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1  # Window should be more to the right
        else:
            right = mid

    return arr[left:left + k]


# Example usage:
arr = [1, 2, 3, 4, 5]
k = 4
x = 3
print(find_closest_elements(arr, k, x))  # Output: [1, 2, 3, 4]

arr = [1, 2, 3, 4, 5]
k = 4
x = -1
print(find_closest_elements(arr, k, x))  # Output: [1, 2, 3, 4]
```

### Example 18: Median of Two Sorted Arrays

```python
def find_median_sorted_arrays(nums1, nums2):
    """
    Find median of two sorted arrays.

    Time: O(log(min(m, n)))
    Space: O(1)

    Args:
        nums1: First sorted array
        nums2: Second sorted array

    Returns:
        Median as float
    """
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    while left <= right:
        partition1 = left + (right - left) // 2
        partition2 = (m + n + 1) // 2 - partition1

        max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float('inf') if partition1 == m else nums1[partition1]

        max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float('inf') if partition2 == n else nums2[partition2]

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            # Found correct partition
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            else:
                return max(max_left1, max_left2)
        elif max_left1 > min_right2:
            right = partition1 - 1
        else:
            left = partition1 + 1

    raise ValueError("Arrays not sorted")


# Example usage:
nums1 = [1, 3]
nums2 = [2]
print(find_median_sorted_arrays(nums1, nums2))  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(find_median_sorted_arrays(nums1, nums2))  # Output: 2.5
```

---

## Summary

**Key Patterns:**

1. **Standard Binary Search**: Find exact target
2. **Find Boundaries**: First/last occurrence, insert position
3. **Binary Search on Answer**: Search solution space
4. **Rotated Arrays**: Identify sorted portion
5. **Peak Finding**: Compare with neighbors
6. **2D Matrix**: Convert to 1D or use staircase
7. **Advanced**: K closest, median finding

**Templates:**

```python
# Template 1: Exact match (left <= right)
while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == target: return mid
    elif nums[mid] < target: left = mid + 1
    else: right = mid - 1

# Template 2: Find boundary (left < right)
while left < right:
    mid = left + (right - left) // 2
    if condition: right = mid
    else: left = mid + 1

# Template 3: Binary search on answer
while left < right:
    mid = left + (right - left) // 2
    if is_valid(mid): right = mid  # Try smaller
    else: left = mid + 1  # Need larger
```

Practice these patterns until they become second nature!
