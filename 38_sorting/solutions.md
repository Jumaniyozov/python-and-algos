# Chapter 38: Sorting - Solutions

## Table of Contents
1. [Easy Problems (1-7)](#easy-problems)
2. [Medium Problems (8-14)](#medium-problems)
3. [Hard Problems (15-20)](#hard-problems)

---

## Easy Problems

### Solution 1: Sort an Array

```python
def sort_array(nums):
    """
    Sort array using merge sort.
    Time: O(n log n), Space: O(n)
    """
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = sort_array(nums[:mid])
    right = sort_array(nums[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Alternative: Use Python's built-in (Timsort)
def sort_array_builtin(nums):
    """Time: O(n log n), Space: O(n)"""
    return sorted(nums)
```

**Complexity Analysis:**
- **Time:** O(n log n) - Divide: O(log n) levels, Merge: O(n) per level
- **Space:** O(n) - Temporary arrays for merging

---

### Solution 2: Merge Sorted Array

```python
def merge(nums1, m, nums2, n):
    """
    Merge from back to avoid overwriting.
    Time: O(m + n), Space: O(1)
    """
    # Start from the end
    p1 = m - 1  # Last element in nums1
    p2 = n - 1  # Last element in nums2
    p = m + n - 1  # Last position in nums1

    # Merge from back to front
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If nums2 has remaining elements
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
```

**Key Insight:** Merge from back to avoid overwriting unprocessed elements.

**Complexity:**
- **Time:** O(m + n)
- **Space:** O(1)

---

### Solution 3: Sort Colors (Dutch National Flag)

```python
def sort_colors(nums):
    """
    Three-way partitioning.
    Time: O(n), Space: O(1)
    """
    low = 0  # Boundary for 0s
    mid = 0  # Current element
    high = len(nums) - 1  # Boundary for 2s

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Alternative: Counting sort
def sort_colors_counting(nums):
    """Time: O(n), Space: O(1)"""
    count = [0, 0, 0]

    # Count occurrences
    for num in nums:
        count[num] += 1

    # Overwrite array
    idx = 0
    for i in range(3):
        for _ in range(count[i]):
            nums[idx] = i
            idx += 1
```

**Complexity:**
- **Time:** O(n) - Single pass
- **Space:** O(1)

---

### Solution 4: Squares of a Sorted Array

```python
def sorted_squares(nums):
    """
    Two pointers from both ends.
    Time: O(n), Space: O(n)
    """
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1  # Fill from back

    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2

        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1
        pos -= 1

    return result
```

**Key Insight:** Largest squares are at the edges (negative or positive extremes).

**Complexity:**
- **Time:** O(n)
- **Space:** O(n) for result

---

### Solution 5: Sort Array By Parity

```python
def sort_array_by_parity(nums):
    """
    Two pointers in-place.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        # Find odd from left
        while left < right and nums[left] % 2 == 0:
            left += 1

        # Find even from right
        while left < right and nums[right] % 2 == 1:
            right -= 1

        # Swap
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums

# Alternative: Single pass
def sort_array_by_parity_v2(nums):
    """Time: O(n), Space: O(1)"""
    even_pos = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[even_pos], nums[i] = nums[i], nums[even_pos]
            even_pos += 1

    return nums
```

**Complexity:**
- **Time:** O(n)
- **Space:** O(1)

---

### Solution 6: Relative Sort Array

```python
def relative_sort_array(arr1, arr2):
    """
    Use counting sort with order mapping.
    Time: O(n + m + k), Space: O(k)
    """
    # Create order map
    order = {val: i for i, val in enumerate(arr2)}

    # Custom sort key
    def sort_key(x):
        if x in order:
            return (0, order[x])  # In arr2: sort by arr2 order
        else:
            return (1, x)  # Not in arr2: sort by value

    return sorted(arr1, key=sort_key)

# Alternative: Counting sort approach
def relative_sort_array_v2(arr1, arr2):
    """Time: O(n + m), Space: O(n)"""
    from collections import Counter

    count = Counter(arr1)
    result = []

    # Add elements in arr2 order
    for num in arr2:
        result.extend([num] * count[num])
        del count[num]

    # Add remaining elements sorted
    for num in sorted(count.keys()):
        result.extend([num] * count[num])

    return result
```

**Complexity:**
- **Time:** O(n log n) or O(n + m) with counting
- **Space:** O(n)

---

### Solution 7: Maximum Gap

```python
def maximum_gap(nums):
    """
    Use bucket sort to achieve O(n).
    Time: O(n), Space: O(n)
    """
    if len(nums) < 2:
        return 0

    min_val, max_val = min(nums), max(nums)

    if min_val == max_val:
        return 0

    # Bucket size (ceiling division)
    n = len(nums)
    bucket_size = max(1, (max_val - min_val) // (n - 1))
    bucket_count = (max_val - min_val) // bucket_size + 1

    # Initialize buckets
    buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

    # Fill buckets with min and max
    for num in nums:
        idx = (num - min_val) // bucket_size
        buckets[idx][0] = min(buckets[idx][0], num)
        buckets[idx][1] = max(buckets[idx][1], num)

    # Find maximum gap
    max_gap = 0
    prev_max = min_val

    for bucket_min, bucket_max in buckets:
        if bucket_min == float('inf'):  # Empty bucket
            continue
        max_gap = max(max_gap, bucket_min - prev_max)
        prev_max = bucket_max

    return max_gap

# Simple approach: Sort first
def maximum_gap_simple(nums):
    """Time: O(n log n), Space: O(1)"""
    if len(nums) < 2:
        return 0

    nums.sort()
    max_gap = 0

    for i in range(1, len(nums)):
        max_gap = max(max_gap, nums[i] - nums[i-1])

    return max_gap
```

**Complexity:**
- **Time:** O(n) with bucket sort, O(n log n) simple
- **Space:** O(n) for buckets

---

## Medium Problems

### Solution 8: Largest Number

```python
def largest_number(nums):
    """
    Custom comparator for concatenation.
    Time: O(n log n), Space: O(n)
    """
    from functools import cmp_to_key

    # Convert to strings
    nums_str = [str(num) for num in nums]

    # Custom comparator
    def compare(x, y):
        if x + y > y + x:
            return -1  # x should come first
        elif x + y < y + x:
            return 1   # y should come first
        else:
            return 0

    nums_str.sort(key=cmp_to_key(compare))

    # Edge case: all zeros
    if nums_str[0] == '0':
        return '0'

    return ''.join(nums_str)
```

**Key Insight:** Compare concatenations: "3" + "30" = "330" vs "30" + "3" = "303"

**Complexity:**
- **Time:** O(n log n)
- **Space:** O(n)

---

### Solution 9: Sort Characters By Frequency

```python
def frequency_sort(s):
    """
    Count frequencies and sort.
    Time: O(n log n), Space: O(n)
    """
    from collections import Counter

    # Count frequencies
    freq = Counter(s)

    # Sort by frequency (descending), then character
    result = []
    for char, count in sorted(freq.items(), key=lambda x: -x[1]):
        result.append(char * count)

    return ''.join(result)

# Alternative: Bucket sort (O(n))
def frequency_sort_bucket(s):
    """Time: O(n), Space: O(n)"""
    from collections import Counter

    freq = Counter(s)
    max_freq = max(freq.values())

    # Create buckets
    buckets = [[] for _ in range(max_freq + 1)]

    for char, count in freq.items():
        buckets[count].append(char)

    # Build result from highest frequency
    result = []
    for i in range(max_freq, 0, -1):
        for char in buckets[i]:
            result.append(char * i)

    return ''.join(result)
```

**Complexity:**
- **Time:** O(n log n) or O(n) with bucket sort
- **Space:** O(n)

---

### Solution 10: H-Index

```python
def h_index(citations):
    """
    Sort and find h-index.
    Time: O(n log n), Space: O(1)
    """
    citations.sort(reverse=True)

    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1
        else:
            break

    return h

# Alternative: Counting sort O(n)
def h_index_linear(citations):
    """Time: O(n), Space: O(n)"""
    n = len(citations)
    buckets = [0] * (n + 1)

    # Count papers
    for c in citations:
        if c >= n:
            buckets[n] += 1
        else:
            buckets[c] += 1

    # Find h-index
    count = 0
    for i in range(n, -1, -1):
        count += buckets[i]
        if count >= i:
            return i

    return 0
```

**Complexity:**
- **Time:** O(n log n) or O(n)
- **Space:** O(1) or O(n)

---

### Solution 11: Top K Frequent Elements

```python
def top_k_frequent(nums, k):
    """
    Use bucket sort for O(n).
    Time: O(n), Space: O(n)
    """
    from collections import Counter

    # Count frequencies
    freq = Counter(nums)

    # Bucket sort
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    # Get top k
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            break

    return result[:k]

# Alternative: Heap
def top_k_frequent_heap(nums, k):
    """Time: O(n log k), Space: O(n)"""
    import heapq
    from collections import Counter

    freq = Counter(nums)

    # Use min heap of size k
    return heapq.nlargest(k, freq.keys(), key=freq.get)
```

**Complexity:**
- **Time:** O(n) with bucket sort
- **Space:** O(n)

---

### Solution 12: Sort List

```python
def sort_list(head):
    """
    Merge sort for linked list.
    Time: O(n log n), Space: O(log n) recursion
    """
    if not head or not head.next:
        return head

    # Find middle using slow/fast pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Split list
    mid = slow.next
    slow.next = None

    # Recursively sort
    left = sort_list(head)
    right = sort_list(mid)

    # Merge
    return merge_lists(left, right)

def merge_lists(l1, l2):
    """Merge two sorted lists."""
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2
    return dummy.next
```

**Complexity:**
- **Time:** O(n log n)
- **Space:** O(log n) for recursion

---

### Solution 13: Wiggle Sort

```python
def wiggle_sort(nums):
    """
    One-pass swapping.
    Time: O(n), Space: O(1)
    """
    for i in range(len(nums) - 1):
        # Even index: ensure nums[i] <= nums[i+1]
        # Odd index: ensure nums[i] >= nums[i+1]
        if (i % 2 == 0 and nums[i] > nums[i+1]) or \
           (i % 2 == 1 and nums[i] < nums[i+1]):
            nums[i], nums[i+1] = nums[i+1], nums[i]
```

**Key Insight:** Local swaps maintain wiggle property.

**Complexity:**
- **Time:** O(n)
- **Space:** O(1)

---

### Solution 14: Kth Largest Element

```python
def find_kth_largest(nums, k):
    """
    Quickselect algorithm.
    Time: O(n) average, O(n²) worst
    Space: O(1)
    """
    def partition(left, right):
        pivot = nums[right]
        i = left

        for j in range(left, right):
            if nums[j] >= pivot:  # For kth largest
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[right] = nums[right], nums[i]
        return i

    left, right = 0, len(nums) - 1

    while True:
        pivot_idx = partition(left, right)

        if pivot_idx == k - 1:
            return nums[pivot_idx]
        elif pivot_idx < k - 1:
            left = pivot_idx + 1
        else:
            right = pivot_idx - 1

# Alternative: Heap
def find_kth_largest_heap(nums, k):
    """Time: O(n log k), Space: O(k)"""
    import heapq
    return heapq.nlargest(k, nums)[-1]
```

**Complexity:**
- **Time:** O(n) average with quickselect
- **Space:** O(1)

---

## Hard Problems

### Solution 15: Wiggle Sort II

```python
def wiggle_sort_ii(nums):
    """
    Find median, partition, interleave.
    Time: O(n), Space: O(n)
    """
    # Find median
    nums_sorted = sorted(nums)
    n = len(nums)
    mid = (n - 1) // 2

    # Split into small and large
    small = nums_sorted[:mid+1]
    large = nums_sorted[mid+1:]

    # Interleave from end to avoid adjacent duplicates
    small.reverse()
    large.reverse()

    for i in range(len(small)):
        nums[2*i] = small[i]
    for i in range(len(large)):
        nums[2*i+1] = large[i]
```

**Complexity:**
- **Time:** O(n log n) with sort, O(n) with quickselect
- **Space:** O(n)

---

### Solution 16: Count of Smaller Numbers After Self

```python
def count_smaller(nums):
    """
    Modified merge sort to count inversions.
    Time: O(n log n), Space: O(n)
    """
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                # Count elements in right that are smaller
                counts[left[i][0]] += j
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            counts[left[i][0]] += j
            result.append(left[i])
            i += 1

        result.extend(right[j:])
        return result

    # Create indexed array
    indexed = list(enumerate(nums))
    counts = [0] * len(nums)

    merge_sort(indexed)
    return counts
```

**Complexity:**
- **Time:** O(n log n)
- **Space:** O(n)

---

### Solution 17: Reverse Pairs

```python
def reverse_pairs(nums):
    """
    Modified merge sort.
    Time: O(n log n), Space: O(n)
    """
    def merge_sort(arr, left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2
        count = merge_sort(arr, left, mid) + merge_sort(arr, mid + 1, right)

        # Count reverse pairs
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and arr[i] > 2 * arr[j]:
                j += 1
            count += j - (mid + 1)

        # Merge
        arr[left:right+1] = sorted(arr[left:right+1])

        return count

    return merge_sort(nums, 0, len(nums) - 1)
```

**Complexity:**
- **Time:** O(n log n)
- **Space:** O(n)

---

### Solution 19: Find Median from Data Stream

```python
import heapq

class MedianFinder:
    """
    Use two heaps: max heap (left) and min heap (right).
    Time: add O(log n), find O(1)
    Space: O(n)
    """
    def __init__(self):
        self.small = []  # Max heap (negate values)
        self.large = []  # Min heap

    def add_num(self, num):
        # Add to max heap
        heapq.heappush(self.small, -num)

        # Balance: ensure all in small <= all in large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
```

**Complexity:**
- **add_num:** O(log n)
- **find_median:** O(1)
- **Space:** O(n)

---

## Summary

**Key Sorting Techniques:**

1. **Merge Sort**: Stable O(n log n), divide and conquer
2. **Quick Sort/Quickselect**: Average O(n log n)/O(n)
3. **Bucket/Counting Sort**: Linear time for specific cases
4. **Heap**: For kth element problems
5. **Custom Comparators**: For non-standard ordering
6. **Two Pointers**: For in-place partitioning

**Common Patterns:**
- Use merge sort for counting inversions
- Use quickselect for kth element
- Use bucket sort for frequency problems
- Use custom comparators for special orderings
- Use two heaps for median finding

Practice these solutions to master sorting techniques!
