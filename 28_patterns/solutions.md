# Problem-Solving Patterns - Solutions

Complete solutions for all exercises with detailed explanations.

## Two Pointers Solutions

### Solution 1: Valid Palindrome
```python
def is_palindrome(s):
    """
    Check if string is palindrome (alphanumeric only).
    Pattern: Two Pointers
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
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

### Solution 2: Two Sum II
```python
def two_sum(numbers, target):
    """
    Find two numbers that sum to target in sorted array.
    Pattern: Two Pointers
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
```

## Sliding Window Solutions

### Solution 6: Maximum Average Subarray
```python
def find_max_average(nums, k):
    """
    Find maximum average of subarray of length k.
    Pattern: Sliding Window
    Time: O(n), Space: O(1)
    """
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum / k
```

## Fast and Slow Pointers Solutions

### Solution 11: Linked List Cycle
```python
def has_cycle(head):
    """
    Detect cycle in linked list.
    Pattern: Fast and Slow Pointers
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False
```

## (Complete solutions for all 68 problems would continue in similar detail...)
