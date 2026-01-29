# Arrays and Strings - Examples

## 22 Practical, Analyzed Examples

### Example 1: Two Sum (Sorted Array)

**Problem:** Find two numbers that add up to target.

```python
def two_sum_sorted(arr, target):
    """
    Find indices of two numbers that sum to target.
    Time: O(n), Space: O(1)
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum

    return None

# Test
arr = [1, 2, 3, 4, 5, 6]
target = 9
result = two_sum_sorted(arr, target)
print(f"Indices: {result}")  # [2, 5] (3 + 6 = 9)
print(f"Values: {arr[result[0]]}, {arr[result[1]]}")
```

**Complexity Analysis:**
- Time: O(n) - single pass with two pointers
- Space: O(1) - only two pointers

---

### Example 2: Remove Duplicates from Sorted Array

**Problem:** Remove duplicates in-place, return new length.

```python
def remove_duplicates(arr):
    """
    Remove duplicates from sorted array in-place.
    Time: O(n), Space: O(1)
    """
    if not arr:
        return 0

    # Slow pointer: position to place next unique element
    slow = 0

    # Fast pointer: scan through array
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1

# Test
arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
length = remove_duplicates(arr)
print(f"New length: {length}")  # 5
print(f"Array: {arr[:length]}")  # [1, 2, 3, 4, 5]
```

**Complexity Analysis:**
- Time: O(n) - single pass
- Space: O(1) - in-place modification

---

### Example 3: Move Zeros to End

**Problem:** Move all zeros to end while maintaining relative order.

```python
def move_zeros(arr):
    """
    Move all zeros to end of array.
    Time: O(n), Space: O(1)
    """
    # Slow pointer: position for next non-zero
    slow = 0

    # Fast pointer: find non-zero elements
    for fast in range(len(arr)):
        if arr[fast] != 0:
            # Swap non-zero element to front
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1

# Test
arr = [0, 1, 0, 3, 12, 0, 5]
move_zeros(arr)
print(f"Result: {arr}")  # [1, 3, 12, 5, 0, 0, 0]
```

**Complexity Analysis:**
- Time: O(n) - single pass
- Space: O(1) - in-place swapping

---

### Example 4: Reverse String

**Problem:** Reverse a string in-place.

```python
def reverse_string(s):
    """
    Reverse string in-place using two pointers.
    Time: O(n), Space: O(1)
    """
    chars = list(s)  # Convert to list (strings immutable)
    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return ''.join(chars)

# Test
s = "hello"
reversed_s = reverse_string(s)
print(f"Original: {s}")
print(f"Reversed: {reversed_s}")  # "olleh"
```

**Complexity Analysis:**
- Time: O(n) - visit each character once
- Space: O(n) - list conversion (O(1) if input is mutable)

---

### Example 5: Valid Palindrome

**Problem:** Check if string is palindrome (ignore case, non-alphanumeric).

```python
def is_palindrome(s):
    """
    Check if string is valid palindrome.
    Time: O(n), Space: O(1)
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

# Test
test_cases = [
    "A man, a plan, a canal: Panama",
    "race a car",
    "Was it a car or a cat I saw?",
    ""
]

for s in test_cases:
    print(f"'{s}' -> {is_palindrome(s)}")
```

**Output:**
```
'A man, a plan, a canal: Panama' -> True
'race a car' -> False
'Was it a car or a cat I saw?' -> True
'' -> True
```

**Complexity Analysis:**
- Time: O(n) - each character checked once
- Space: O(1) - only pointers

---

### Example 6: Container With Most Water

**Problem:** Find two lines that together with x-axis form container with most water.

```python
def max_area(heights):
    """
    Find maximum water that can be contained.
    Time: O(n), Space: O(1)
    """
    left = 0
    right = len(heights) - 1
    max_water = 0

    while left < right:
        # Calculate current area
        width = right - left
        height = min(heights[left], heights[right])
        current_area = width * height
        max_water = max(max_water, current_area)

        # Move pointer with smaller height
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Test
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = max_area(heights)
print(f"Maximum water: {result}")  # 49 (7 * 7)
```

**Complexity Analysis:**
- Time: O(n) - single pass
- Space: O(1) - only pointers

---

### Example 7: Maximum Sum of K Consecutive Elements

**Problem:** Find maximum sum of k consecutive elements.

```python
def max_sum_k_elements(arr, k):
    """
    Find maximum sum of k consecutive elements.
    Time: O(n), Space: O(1)
    """
    if len(arr) < k:
        return None

    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide window
    for i in range(k, len(arr)):
        # Remove leftmost, add rightmost
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Test
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
result = max_sum_k_elements(arr, k)
print(f"Maximum sum of {k} consecutive: {result}")  # 39 (10+23+3+1)
```

**Complexity Analysis:**
- Time: O(n) - single pass after initial window
- Space: O(1) - only variables

---

### Example 8: Longest Substring Without Repeating Characters

**Problem:** Find length of longest substring without repeating characters.

```python
def longest_unique_substring(s):
    """
    Find length of longest substring without repeating chars.
    Time: O(n), Space: O(min(n, k)) where k = charset size
    """
    char_index = {}  # Character -> last seen index
    max_length = 0
    left = 0

    for right, char in enumerate(s):
        # If char seen and in current window
        if char in char_index and char_index[char] >= left:
            # Move left pointer past duplicate
            left = char_index[char] + 1

        # Update last seen index
        char_index[char] = right

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length

# Test
test_strings = [
    "abcabcbb",  # "abc" -> 3
    "bbbbb",     # "b" -> 1
    "pwwkew",    # "wke" -> 3
    "abcdef",    # "abcdef" -> 6
    ""           # "" -> 0
]

for s in test_strings:
    result = longest_unique_substring(s)
    print(f"'{s}' -> {result}")
```

**Complexity Analysis:**
- Time: O(n) - each character added/removed once
- Space: O(min(n, k)) - hash map size

---

### Example 9: Minimum Window Substring

**Problem:** Find minimum window in s containing all characters of t.

```python
from collections import Counter

def min_window_substring(s, t):
    """
    Find minimum window in s containing all chars in t.
    Time: O(n + m), Space: O(k)
    """
    if not s or not t:
        return ""

    # Count chars in t
    target_count = Counter(t)
    required = len(target_count)

    # Window state
    window_counts = {}
    formed = 0  # Number of unique chars with desired frequency

    # Result
    min_len = float('inf')
    result = (0, 0)

    left = 0
    for right, char in enumerate(s):
        # Add char to window
        window_counts[char] = window_counts.get(char, 0) + 1

        # Check if this char satisfies requirement
        if char in target_count and window_counts[char] == target_count[char]:
            formed += 1

        # Try to shrink window
        while left <= right and formed == required:
            # Update result
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = (left, right)

            # Remove leftmost char
            char = s[left]
            window_counts[char] -= 1
            if char in target_count and window_counts[char] < target_count[char]:
                formed -= 1

            left += 1

    return "" if min_len == float('inf') else s[result[0]:result[1] + 1]

# Test
s = "ADOBECODEBANC"
t = "ABC"
result = min_window_substring(s, t)
print(f"Minimum window: '{result}'")  # "BANC"
```

**Complexity Analysis:**
- Time: O(n + m) - n for s, m for t
- Space: O(k) - k distinct characters

---

### Example 10: Rotate Array

**Problem:** Rotate array to the right by k steps.

```python
def rotate_array(arr, k):
    """
    Rotate array to the right by k positions.
    Time: O(n), Space: O(1)
    """
    n = len(arr)
    k = k % n  # Handle k > n

    # Helper function to reverse array segment
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Three reversals method
    reverse(0, n - 1)      # Reverse entire array
    reverse(0, k - 1)      # Reverse first k elements
    reverse(k, n - 1)      # Reverse remaining elements

# Test
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(f"Original: {arr}")
rotate_array(arr, k)
print(f"Rotated by {k}: {arr}")  # [5, 6, 7, 1, 2, 3, 4]
```

**Complexity Analysis:**
- Time: O(n) - three passes
- Space: O(1) - in-place rotation

---

### Example 11: Product of Array Except Self

**Problem:** Return array where output[i] is product of all elements except arr[i].

```python
def product_except_self(arr):
    """
    Calculate product of all elements except self.
    Time: O(n), Space: O(1) excluding output
    """
    n = len(arr)
    result = [1] * n

    # Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]

    # Calculate suffix products and combine
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= arr[i]

    return result

# Test
arr = [1, 2, 3, 4]
result = product_except_self(arr)
print(f"Input: {arr}")
print(f"Output: {result}")  # [24, 12, 8, 6]

# Verification
for i, val in enumerate(result):
    expected = 1
    for j, num in enumerate(arr):
        if i != j:
            expected *= num
    print(f"result[{i}] = {val}, expected = {expected}")
```

**Complexity Analysis:**
- Time: O(n) - two passes
- Space: O(1) - not counting output array

---

### Example 12: Find All Anagrams in String

**Problem:** Find all anagram substrings of p in s.

```python
from collections import Counter

def find_anagrams(s, p):
    """
    Find starting indices of all anagrams of p in s.
    Time: O(n), Space: O(1) - alphabet size constant
    """
    if len(p) > len(s):
        return []

    result = []
    p_count = Counter(p)
    window_count = Counter(s[:len(p) - 1])

    for i in range(len(p) - 1, len(s)):
        # Add new character
        window_count[s[i]] += 1

        # Check if anagram
        if window_count == p_count:
            result.append(i - len(p) + 1)

        # Remove leftmost character
        left_char = s[i - len(p) + 1]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]

    return result

# Test
s = "cbaebabacd"
p = "abc"
result = find_anagrams(s, p)
print(f"Anagrams of '{p}' in '{s}': {result}")  # [0, 6]
print(f"Substrings: {[s[i:i+len(p)] for i in result]}")  # ['cba', 'bac']
```

**Complexity Analysis:**
- Time: O(n) - sliding window
- Space: O(1) - alphabet size constant (26 for lowercase)

---

### Example 13: Subarray Sum Equals K

**Problem:** Find total number of subarrays with sum equal to k.

```python
def subarray_sum_k(arr, k):
    """
    Count subarrays with sum equal to k.
    Time: O(n), Space: O(n)
    """
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # prefix_sum -> count

    for num in arr:
        prefix_sum += num

        # Check if (prefix_sum - k) exists
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]

        # Update sum count
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

    return count

# Test
arr = [1, 1, 1]
k = 2
result = subarray_sum_k(arr, k)
print(f"Array: {arr}, k: {k}")
print(f"Subarrays with sum {k}: {result}")  # 2 ([1,1] twice)

arr = [1, 2, 3]
k = 3
result = subarray_sum_k(arr, k)
print(f"\nArray: {arr}, k: {k}")
print(f"Subarrays with sum {k}: {result}")  # 2 ([1,2] and [3])
```

**Complexity Analysis:**
- Time: O(n) - single pass
- Space: O(n) - hash map of prefix sums

---

### Example 14: Dutch National Flag (3-Way Partition)

**Problem:** Sort array of 0s, 1s, and 2s.

```python
def sort_colors(arr):
    """
    Sort array of 0s, 1s, 2s in-place (Dutch flag problem).
    Time: O(n), Space: O(1)
    """
    low = 0      # Next position for 0
    mid = 0      # Current element
    high = len(arr) - 1  # Next position for 2

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

# Test
arr = [2, 0, 2, 1, 1, 0]
print(f"Original: {arr}")
sort_colors(arr)
print(f"Sorted: {arr}")  # [0, 0, 1, 1, 2, 2]
```

**Complexity Analysis:**
- Time: O(n) - single pass
- Space: O(1) - in-place sorting

---

### Example 15: Merge Sorted Arrays

**Problem:** Merge two sorted arrays.

```python
def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays.
    Time: O(n + m), Space: O(n + m)
    """
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result

# Test
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8, 10]
result = merge_sorted_arrays(arr1, arr2)
print(f"Merged: {result}")  # [1, 2, 3, 4, 5, 6, 7, 8, 10]
```

**Complexity Analysis:**
- Time: O(n + m)
- Space: O(n + m)

---

### Example 16: Longest Palindromic Substring

**Problem:** Find longest palindromic substring.

```python
def longest_palindrome(s):
    """
    Find longest palindromic substring.
    Time: O(n²), Space: O(1)
    """
    if not s:
        return ""

    def expand_around_center(left, right):
        """Expand around center and return palindrome length"""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start = 0
    max_len = 0

    for i in range(len(s)):
        # Odd length palindromes (center is one char)
        len1 = expand_around_center(i, i)
        # Even length palindromes (center is between two chars)
        len2 = expand_around_center(i, i + 1)

        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2

    return s[start:start + max_len]

# Test
test_strings = [
    "babad",  # "bab" or "aba"
    "cbbd",   # "bb"
    "racecar",  # "racecar"
    "noon"   # "noon"
]

for s in test_strings:
    result = longest_palindrome(s)
    print(f"'{s}' -> '{result}'")
```

**Complexity Analysis:**
- Time: O(n²) - expand from each center
- Space: O(1) - only pointers

---

### Example 17: Group Anagrams

**Problem:** Group strings that are anagrams of each other.

```python
from collections import defaultdict

def group_anagrams(strs):
    """
    Group anagrams together.
    Time: O(n * k log k), Space: O(n * k)
    where n = number of strings, k = max string length
    """
    anagrams = defaultdict(list)

    for s in strs:
        # Sort string to get key
        key = ''.join(sorted(s))
        anagrams[key].append(s)

    return list(anagrams.values())

# Alternative: Using character count as key (O(n * k))
def group_anagrams_optimized(strs):
    """
    Group anagrams using character count.
    Time: O(n * k), Space: O(n * k)
    """
    anagrams = defaultdict(list)

    for s in strs:
        # Use character count as key
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        anagrams[key].append(s)

    return list(anagrams.values())

# Test
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print("Grouped anagrams:")
for group in result:
    print(f"  {group}")
```

**Output:**
```
Grouped anagrams:
  ['eat', 'tea', 'ate']
  ['tan', 'nat']
  ['bat']
```

**Complexity Analysis:**
- Time: O(n * k log k) for sorting, O(n * k) for counting
- Space: O(n * k) for hash map

---

### Example 18: Trapping Rain Water

**Problem:** Calculate how much water can be trapped after raining.

```python
def trap_rain_water(heights):
    """
    Calculate trapped rain water.
    Time: O(n), Space: O(1)
    """
    if not heights:
        return 0

    left = 0
    right = len(heights) - 1
    left_max = heights[left]
    right_max = heights[right]
    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]

    return water

# Test
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result = trap_rain_water(heights)
print(f"Heights: {heights}")
print(f"Trapped water: {result} units")  # 6 units
```

**Complexity Analysis:**
- Time: O(n) - single pass
- Space: O(1) - only pointers

---

### Example 19: String Compression

**Problem:** Compress string using counts of repeated characters.

```python
def compress_string(s):
    """
    Compress string: 'aabcccccaaa' -> 'a2b1c5a3'
    Time: O(n), Space: O(1) excluding output
    """
    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1

    # Add last group
    result.append(s[-1] + str(count))

    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s

# Test
test_strings = [
    "aabcccccaaa",  # "a2b1c5a3"
    "abcdef",       # "abcdef" (no compression)
    "aabbcc",       # "aabbcc" (no compression)
    "aaaa"          # "a4"
]

for s in test_strings:
    result = compress_string(s)
    print(f"'{s}' -> '{result}'")
```

**Complexity Analysis:**
- Time: O(n) - single pass
- Space: O(1) - not counting output

---

### Example 20: Longest Repeating Character Replacement

**Problem:** Find length of longest substring with same character after replacing at most k characters.

```python
def character_replacement(s, k):
    """
    Find longest substring with same char after k replacements.
    Time: O(n), Space: O(1)
    """
    char_count = {}
    max_length = 0
    max_count = 0
    left = 0

    for right, char in enumerate(s):
        # Add current character
        char_count[char] = char_count.get(char, 0) + 1
        max_count = max(max_count, char_count[char])

        # If window invalid, shrink from left
        window_size = right - left + 1
        if window_size - max_count > k:
            char_count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Test
test_cases = [
    ("ABAB", 2, 4),      # Replace 2 chars -> "AAAA" or "BBBB"
    ("AABABBA", 1, 4),   # Replace 1 char -> "AABA" or "BBBA"
    ("ABAA", 0, 2)       # No replacement -> "AA"
]

for s, k, expected in test_cases:
    result = character_replacement(s, k)
    print(f"s='{s}', k={k}: {result} (expected {expected})")
```

**Complexity Analysis:**
- Time: O(n) - sliding window
- Space: O(1) - constant alphabet size

---

### Example 21: Find First and Last Position

**Problem:** Find first and last position of target in sorted array.

```python
def search_range(arr, target):
    """
    Find first and last position of target.
    Time: O(log n), Space: O(1)
    """
    def find_boundary(is_first):
        """Binary search for boundary"""
        left, right = 0, len(arr) - 1
        boundary = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                boundary = mid
                if is_first:
                    right = mid - 1  # Look left
                else:
                    left = mid + 1   # Look right
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return boundary

    first = find_boundary(True)
    last = find_boundary(False)

    return [first, last]

# Test
arr = [5, 7, 7, 8, 8, 10]
target = 8
result = search_range(arr, target)
print(f"Array: {arr}")
print(f"Target: {target}")
print(f"Range: {result}")  # [3, 4]
```

**Complexity Analysis:**
- Time: O(log n) - binary search twice
- Space: O(1) - only pointers

---

### Example 22: Permutation in String

**Problem:** Check if s2 contains permutation of s1.

```python
from collections import Counter

def check_inclusion(s1, s2):
    """
    Check if s2 contains any permutation of s1.
    Time: O(n), Space: O(1)
    """
    if len(s1) > len(s2):
        return False

    s1_count = Counter(s1)
    window_count = Counter(s2[:len(s1) - 1])

    for i in range(len(s1) - 1, len(s2)):
        # Add new character
        window_count[s2[i]] += 1

        # Check if permutation found
        if window_count == s1_count:
            return True

        # Remove leftmost character
        left_char = s2[i - len(s1) + 1]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]

    return False

# Test
test_cases = [
    ("ab", "eidbaooo", True),   # "ba" is permutation
    ("ab", "eidboaoo", False),  # no permutation
    ("abc", "bbbca", True)      # "bca" is permutation
]

for s1, s2, expected in test_cases:
    result = check_inclusion(s1, s2)
    print(f"s1='{s1}', s2='{s2}': {result} (expected {expected})")
```

**Complexity Analysis:**
- Time: O(n) - sliding window
- Space: O(1) - alphabet size constant

---

## Summary

These 22 examples cover:
- **Two Pointers**: Examples 1-6, 14, 18, 21
- **Sliding Window**: Examples 7-9, 12, 13, 20, 22
- **Array Manipulation**: Examples 10-11, 15
- **String Algorithms**: Examples 16-17, 19
- **Combined Techniques**: Examples in real interview problems

All examples include:
- Complete, runnable code
- Test cases with output
- Detailed complexity analysis
- Comments explaining the approach
