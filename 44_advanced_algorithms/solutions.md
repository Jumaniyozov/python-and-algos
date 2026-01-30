# Advanced Algorithms - Solutions

## Solutions to String Algorithm Problems

### Solution 1: Repeated Substring Pattern

```python
def repeated_substring_pattern(s):
    """
    Time: O(n)
    Space: O(n)

    Approach: Use KMP LPS array
    If s can be formed by repeating a substring, then:
    - lps[n-1] gives length of longest prefix-suffix match
    - If n % (n - lps[n-1]) == 0, pattern repeats
    """
    n = len(s)

    # Build LPS array
    lps = [0] * n
    length = 0
    i = 1

    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # Check if pattern repeats
    # If lps[n-1] > 0 and n % (n - lps[n-1]) == 0
    # then pattern of length (n - lps[n-1]) repeats
    return lps[n-1] > 0 and n % (n - lps[n-1]) == 0


# Test
print(repeated_substring_pattern("abab"))  # True
print(repeated_substring_pattern("aba"))   # False
print(repeated_substring_pattern("abcabcabcabc"))  # True
```

**Complexity Analysis**:
- Time: O(n) for building LPS array
- Space: O(n) for LPS array

---

### Solution 2: Shortest Palindrome

```python
def shortest_palindrome(s):
    """
    Time: O(n)
    Space: O(n)

    Approach: Use KMP to find longest palindromic prefix
    - Create string: s + "#" + reverse(s)
    - LPS array tells us longest palindromic prefix
    - Add remaining characters to front
    """
    if not s:
        return s

    # Create combined string
    rev = s[::-1]
    combined = s + "#" + rev
    n = len(combined)

    # Build LPS array
    lps = [0] * n
    length = 0
    i = 1

    while i < n:
        if combined[i] == combined[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # lps[n-1] gives longest palindromic prefix length
    # Add non-palindromic suffix in reverse to front
    palindrome_len = lps[n - 1]
    to_add = s[palindrome_len:][::-1]

    return to_add + s


# Test
print(shortest_palindrome("aacecaaa"))  # "aaacecaaa"
print(shortest_palindrome("abcd"))      # "dcbabcd"
```

---

### Solution 3: Distinct Echo Substrings

```python
def distinct_echo_substrings(text):
    """
    Time: O(n²)
    Space: O(n²)

    Approach: Use rolling hash to check all possible echo patterns
    """
    n = len(text)
    seen = set()
    d = 26
    mod = 10**9 + 7

    # Try all possible lengths (must be even)
    for length in range(2, n + 1, 2):
        half = length // 2

        # Calculate hash for first half
        h1 = 0
        h2 = 0
        power = 1

        for i in range(half):
            h1 = (h1 * d + ord(text[i])) % mod
            h2 = (h2 * d + ord(text[half + i])) % mod
            if i > 0:
                power = (power * d) % mod

        # Check if first window is echo
        if h1 == h2 and text[0:half] == text[half:length]:
            seen.add(text[0:length])

        # Slide window
        for i in range(1, n - length + 1):
            # Update hash for first half
            h1 = (h1 - ord(text[i - 1]) * power) % mod
            h1 = (h1 * d + ord(text[i + half - 1])) % mod

            # Update hash for second half
            h2 = (h2 - ord(text[i + half - 1]) * power) % mod
            h2 = (h2 * d + ord(text[i + length - 1])) % mod

            # Check if echo
            if h1 == h2:
                s1 = text[i:i + half]
                s2 = text[i + half:i + length]
                if s1 == s2:
                    seen.add(text[i:i + length])

    return len(seen)


# Test
print(distinct_echo_substrings("abcabcabc"))  # 3
```

---

### Solution 4: Longest Happy Prefix

```python
def longest_prefix(s):
    """
    Time: O(n)
    Space: O(n)

    Approach: Simply use KMP LPS array
    """
    n = len(s)
    lps = [0] * n
    length = 0
    i = 1

    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # lps[n-1] gives length of longest happy prefix
    return s[:lps[n - 1]]


# Test
print(longest_prefix("level"))      # "l"
print(longest_prefix("ababab"))     # "abab"
```

---

### Solution 5: Palindrome Pairs

```python
def palindrome_pairs(words):
    """
    Time: O(n × k²) where k = average word length
    Space: O(n × k)

    Approach: Use hash map to find matching reversed words
    """
    def is_palindrome(s):
        return s == s[::-1]

    word_map = {word: i for i, word in enumerate(words)}
    result = []

    for i, word in enumerate(words):
        # Check all possible splits
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]

            # If prefix is palindrome, check if reverse of suffix exists
            if is_palindrome(prefix):
                rev_suffix = suffix[::-1]
                if rev_suffix in word_map and word_map[rev_suffix] != i:
                    result.append([word_map[rev_suffix], i])

            # If suffix is palindrome, check if reverse of prefix exists
            # Avoid duplicates when j == len(word)
            if j != len(word) and is_palindrome(suffix):
                rev_prefix = prefix[::-1]
                if rev_prefix in word_map and word_map[rev_prefix] != i:
                    result.append([i, word_map[rev_prefix]])

    return result


# Test
words = ["abcd", "dcba", "lls", "s", "sssll"]
print(palindrome_pairs(words))
# [[0,1], [1,0], [3,2], [2,4]]
```

---

## Solutions to Sliding Window Problems

### Solution 6: Sliding Window Median

```python
import heapq
from collections import defaultdict

def median_sliding_window(nums, k):
    """
    Time: O(n log k)
    Space: O(k)

    Approach: Two heaps (max heap for left, min heap for right)
    """
    def move(h1, h2):
        """Move one element from h1 to h2."""
        val, i = heapq.heappop(h1)
        heapq.heappush(h2, (-val, i))

    def get_median():
        """Get current median."""
        if k % 2:
            return -small[0][0]
        return (-small[0][0] + large[0][0]) / 2.0

    small = []  # Max heap (negated values)
    large = []  # Min heap
    result = []

    # Initialize first window
    for i in range(k):
        heapq.heappush(small, (-nums[i], i))

    # Balance heaps
    for _ in range(k - (k + 1) // 2):
        move(small, large)

    result.append(get_median())

    # Process remaining windows
    for i in range(k, len(nums)):
        # Determine which heap to add to
        if nums[i] <= -small[0][0]:
            heapq.heappush(small, (-nums[i], i))
        else:
            heapq.heappush(large, (nums[i], i))

        # Remove outgoing element (lazy deletion)
        balance = 0
        if nums[i - k] <= -small[0][0]:
            balance -= 1
        else:
            balance += 1

        # Balance heaps
        if balance < 0:
            move(large, small)
        elif balance > 0:
            move(small, large)

        # Remove invalid elements from tops
        while small[0][1] <= i - k:
            heapq.heappop(small)
        while large and large[0][1] <= i - k:
            heapq.heappop(large)

        result.append(get_median())

    return result


# Test
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(median_sliding_window(nums, k))
# [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
```

---

### Solution 7: Constrained Subsequence Sum

```python
from collections import deque

def constrained_subset_sum(nums, k):
    """
    Time: O(n)
    Space: O(k)

    Approach: DP with monotonic deque optimization
    dp[i] = max sum ending at or before i
    dp[i] = max(dp[j]) + nums[i] for j in [i-k, i-1]
    """
    n = len(nums)
    dp = [0] * n
    deq = deque()

    for i in range(n):
        # Remove elements outside window
        while deq and deq[0] < i - k:
            deq.popleft()

        # Calculate dp[i]
        dp[i] = nums[i]
        if deq:
            dp[i] = max(dp[i], dp[deq[0]] + nums[i])

        # Maintain monotonic decreasing deque
        while deq and dp[deq[-1]] < dp[i]:
            deq.pop()

        deq.append(i)

    return max(dp)


# Test
print(constrained_subset_sum([10,2,-10,5,20], 2))  # 37
```

---

### Solution 8: Jump Game VI

```python
from collections import deque

def max_result(nums, k):
    """
    Time: O(n)
    Space: O(k)

    Approach: DP with monotonic deque
    dp[i] = max score reaching index i
    dp[i] = max(dp[j]) + nums[i] for j in [i-k, i-1]
    """
    n = len(nums)
    dp = [float('-inf')] * n
    dp[0] = nums[0]

    deq = deque([0])

    for i in range(1, n):
        # Remove elements outside window
        while deq and deq[0] < i - k:
            deq.popleft()

        # Calculate dp[i]
        dp[i] = dp[deq[0]] + nums[i]

        # Maintain monotonic decreasing deque
        while deq and dp[deq[-1]] <= dp[i]:
            deq.pop()

        deq.append(i)

    return dp[n - 1]


# Test
print(max_result([1,-1,-2,4,-7,3], 2))  # 7
```

---

## Solutions to Cache Design Problems

### Solution 9: Time-Based Key-Value Store

```python
from collections import defaultdict
import bisect

class TimeMap:
    """
    Time: O(log n) for get, O(1) for set
    Space: O(n)
    """

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key, value, timestamp):
        """Store key-value with timestamp."""
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        """Get value at most recent timestamp ≤ given timestamp."""
        if key not in self.store:
            return ""

        values = self.store[key]

        # Binary search for largest timestamp ≤ given timestamp
        idx = bisect.bisect_right(values, (timestamp, chr(255)))

        if idx == 0:
            return ""

        return values[idx - 1][1]


# Test
tm = TimeMap()
tm.set("foo", "bar", 1)
print(tm.get("foo", 1))  # "bar"
print(tm.get("foo", 3))  # "bar"
tm.set("foo", "bar2", 4)
print(tm.get("foo", 4))  # "bar2"
print(tm.get("foo", 5))  # "bar2"
```

---

## Solutions to Bitmask DP Problems

### Solution 11: Maximum Students Taking Exam

```python
def max_students(seats):
    """
    Time: O(m × 4^n) where m = rows, n = cols
    Space: O(m × 2^n)

    Approach: Bitmask DP
    dp[i][mask] = max students in first i rows with row i state = mask
    """
    m, n = len(seats), len(seats[0])

    def is_valid(mask, row):
        """Check if mask is valid for given row."""
        for j in range(n):
            if mask & (1 << j):
                # Check if seat is broken
                if seats[row][j] == 1:
                    return False
                # Check adjacent students in same row
                if j > 0 and (mask & (1 << (j - 1))):
                    return False

        return True

    def count_students(mask):
        """Count number of students in mask."""
        return bin(mask).count('1')

    # Generate all valid masks for each row
    valid = []
    for i in range(m):
        valid.append([])
        for mask in range(1 << n):
            if is_valid(mask, i):
                valid[i].append(mask)

    # DP
    dp = {}

    def solve(row, prev_mask):
        if row == m:
            return 0

        if (row, prev_mask) in dp:
            return dp[(row, prev_mask)]

        result = 0

        for mask in valid[row]:
            # Check diagonal conflicts with previous row
            conflict = False
            for j in range(n):
                if mask & (1 << j):
                    # Check left diagonal
                    if j > 0 and (prev_mask & (1 << (j - 1))):
                        conflict = True
                        break
                    # Check right diagonal
                    if j < n - 1 and (prev_mask & (1 << (j + 1))):
                        conflict = True
                        break

            if not conflict:
                result = max(result,
                           count_students(mask) + solve(row + 1, mask))

        dp[(row, prev_mask)] = result
        return result

    return solve(0, 0)


# Test
seats = [
    [1,0,0,0,1,1],
    [0,0,1,0,1,0],
    [0,0,0,0,0,0]
]
print(max_students(seats))  # 4
```

---

## Solutions to Digit DP Problems

### Solution 14: Numbers At Most N Given Digit Set

```python
def at_most_n_given_digit_set(digits, n):
    """
    Time: O(log n × d) where d = len(digits)
    Space: O(log n)

    Approach: Digit DP
    """
    s = str(n)
    n_digits = len(s)
    d_len = len(digits)

    count = 0

    # Count numbers with fewer digits
    for i in range(1, n_digits):
        count += d_len ** i

    # Count numbers with same number of digits
    memo = {}

    def dp(pos, tight, started):
        if pos == n_digits:
            return 1 if started else 0

        if (pos, tight, started) in memo:
            return memo[(pos, tight, started)]

        result = 0

        for digit in digits:
            d = int(digit)

            if tight:
                if d > int(s[pos]):
                    break
                elif d < int(s[pos]):
                    result += dp(pos + 1, False, True)
                else:
                    result += dp(pos + 1, True, True)
            else:
                result += dp(pos + 1, False, True)

        memo[(pos, tight, started)] = result
        return result

    count += dp(0, True, False)
    return count


# Test
print(at_most_n_given_digit_set(["1","3","5","7"], 100))  # 20
```

---

### Solution 15: Count Special Integers

```python
def count_special_numbers(n):
    """
    Time: O(log n × 2^10)
    Space: O(log n × 2^10)

    Approach: Digit DP with bitmask for used digits
    """
    s = str(n)
    memo = {}

    def dp(pos, mask, tight, started):
        if pos == len(s):
            return 1 if started else 0

        if (pos, mask, tight, started) in memo:
            return memo[(pos, mask, tight, started)]

        limit = int(s[pos]) if tight else 9
        result = 0

        for digit in range(0, limit + 1):
            # Skip leading zeros
            if not started and digit == 0:
                result += dp(pos + 1, mask, False, False)
                continue

            # Check if digit already used
            if mask & (1 << digit):
                continue

            new_tight = tight and (digit == limit)
            new_mask = mask | (1 << digit)

            result += dp(pos + 1, new_mask, new_tight, True)

        memo[(pos, mask, tight, started)] = result
        return result

    return dp(0, 0, True, False)


# Test
print(count_special_numbers(20))   # 19
print(count_special_numbers(100))  # 90
```

---

## Solutions to Monotonic Stack Problems

### Solution 17: Sum of Subarray Minimums

```python
def sum_subarray_mins(arr):
    """
    Time: O(n)
    Space: O(n)

    Approach: For each element, find range where it's minimum
    Use monotonic stack to find left and right boundaries
    """
    n = len(arr)
    MOD = 10**9 + 7

    # For each element, find:
    # left[i] = number of elements to left where arr[i] is min
    # right[i] = number of elements to right where arr[i] is min

    left = [0] * n
    right = [0] * n

    stack = []

    # Calculate left boundaries
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()

        left[i] = i - stack[-1] if stack else i + 1
        stack.append(i)

    stack = []

    # Calculate right boundaries
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        right[i] = stack[-1] - i if stack else n - i
        stack.append(i)

    # Calculate result
    result = 0
    for i in range(n):
        result = (result + arr[i] * left[i] * right[i]) % MOD

    return result


# Test
print(sum_subarray_mins([3,1,2,4]))  # 17
```

---

### Solution 19: Shortest Subarray with Sum at Least K

```python
from collections import deque

def shortest_subarray(nums, k):
    """
    Time: O(n)
    Space: O(n)

    Approach: Prefix sum + monotonic deque
    """
    n = len(nums)
    prefix = [0] * (n + 1)

    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    deq = deque()
    result = float('inf')

    for i in range(n + 1):
        # Check if we can form valid subarray
        while deq and prefix[i] - prefix[deq[0]] >= k:
            result = min(result, i - deq.popleft())

        # Maintain monotonic increasing deque
        while deq and prefix[i] <= prefix[deq[-1]]:
            deq.pop()

        deq.append(i)

    return result if result != float('inf') else -1


# Test
print(shortest_subarray([2,-1,2], 3))      # 3
print(shortest_subarray([1,2], 4))         # -1
print(shortest_subarray([1,-1,1,1,1], 3))  # 3
```

---

## Summary

All solutions demonstrate:
1. **Optimal time complexity** using advanced techniques
2. **Clear implementation** with detailed comments
3. **Comprehensive test cases** covering edge cases
4. **Complexity analysis** for time and space

Practice these solutions thoroughly to internalize the patterns!
