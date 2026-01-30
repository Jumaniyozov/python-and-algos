# Chapter 39: Searching - Solutions

Complete solutions with detailed explanations and complexity analysis.

## Easy Problems

### E1: Binary Search

```python
def search(nums, target):
    """Time: O(log n), Space: O(1)"""
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

### E2: Search Insert Position

```python
def search_insert(nums, target):
    """Time: O(log n), Space: O(1)"""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Insert position
```

### E3: Sqrt(x)

```python
def my_sqrt(x):
    """Time: O(log x), Space: O(1)"""
    if x < 2:
        return x

    left, right = 1, x // 2

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1

    return right  # Floor of sqrt
```

---

## Medium Problems

### M1: Find First and Last Position

```python
def search_range(nums, target):
    """Time: O(log n), Space: O(1)"""
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                result = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    return [find_bound(True), find_bound(False)]
```

### M2: Search in Rotated Sorted Array

```python
def search(nums, target):
    """Time: O(log n), Space: O(1)"""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:  # Left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

### M6: Koko Eating Bananas

```python
def min_eating_speed(piles, h):
    """Time: O(n log m), Space: O(1)"""
    def can_finish(speed):
        hours = sum((pile + speed - 1) // speed for pile in piles)
        return hours <= h

    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1

    return left
```

### M7: Ship Packages

```python
def ship_within_days(weights, days):
    """Time: O(n log(sum)), Space: O(1)"""
    def can_ship(capacity):
        days_needed, current = 1, 0
        for weight in weights:
            if current + weight > capacity:
                days_needed += 1
                current = weight
            else:
                current += weight
        return days_needed <= days

    left, right = max(weights), sum(weights)

    while left < right:
        mid = left + (right - left) // 2
        if can_ship(mid):
            right = mid
        else:
            left = mid + 1

    return left
```

---

## Hard Problems

### H1: Median of Two Sorted Arrays

```python
def find_median_sorted_arrays(nums1, nums2):
    """Time: O(log(min(m,n))), Space: O(1)"""
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1

        max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float('inf') if partition1 == m else nums1[partition1]

        max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float('inf') if partition2 == n else nums2[partition2]

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            else:
                return max(max_left1, max_left2)
        elif max_left1 > min_right2:
            right = partition1 - 1
        else:
            left = partition1 + 1
```

---

## Key Patterns Summary

1. **Standard Binary Search**: Template 1 (left <= right)
2. **Find Boundaries**: Template 2 (left < right)
3. **Binary Search on Answer**: Check if answer works
4. **Rotated Arrays**: Identify sorted portion
5. **2D Matrix**: Convert to 1D or staircase

Master these patterns for interview success!
