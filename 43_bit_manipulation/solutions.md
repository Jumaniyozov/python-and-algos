# Chapter 43: Bit Manipulation - Solutions

## Easy Problems

### E1: Number of 1 Bits
```python
def hamming_weight(n):
    count = 0
    while n:
        n &= n - 1  # Clear rightmost set bit
        count += 1
    return count
```
**Time**: O(number of 1 bits), **Space**: O(1)

### E2: Power of Two
```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```
**Time**: O(1), **Space**: O(1)

### E3: Reverse Bits
```python
def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```
**Time**: O(32) = O(1), **Space**: O(1)

### E4: Single Number
```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```
**Time**: O(n), **Space**: O(1)

### E5: Missing Number
```python
def missing_number(nums):
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result
```
**Time**: O(n), **Space**: O(1)

### E6: Hamming Distance
```python
def hamming_distance(x, y):
    xor = x ^ y
    count = 0
    while xor:
        xor &= xor - 1
        count += 1
    return count
```
**Time**: O(log max(x,y)), **Space**: O(1)

### E7: Binary Number with Alternating Bits
```python
def has_alternating_bits(n):
    prev = n & 1
    n >>= 1
    while n:
        curr = n & 1
        if curr == prev:
            return False
        prev = curr
        n >>= 1
    return True
```
**Time**: O(log n), **Space**: O(1)

---

## Medium Problems

### M1: Single Number II
```python
def single_number_ii(nums):
    ones = twos = 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones
```
**Time**: O(n), **Space**: O(1)

### M2: Single Number III
```python
def single_number_iii(nums):
    xor = 0
    for num in nums:
        xor ^= num

    diff_bit = xor & -xor

    a = b = 0
    for num in nums:
        if num & diff_bit:
            a ^= num
        else:
            b ^= num

    return [a, b]
```
**Time**: O(n), **Space**: O(1)

### M3: Counting Bits
```python
def counting_bits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i & (i - 1)] + 1
    return dp
```
**Time**: O(n), **Space**: O(n)

### M4: Bitwise AND of Numbers Range
```python
def range_bitwise_and(left, right):
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift
```
**Time**: O(log n), **Space**: O(1)

### M5: Maximum XOR of Two Numbers
```python
def find_maximum_xor(nums):
    max_xor = 0
    mask = 0

    for i in range(31, -1, -1):
        mask |= (1 << i)
        prefixes = {num & mask for num in nums}
        temp = max_xor | (1 << i)

        for prefix in prefixes:
            if (temp ^ prefix) in prefixes:
                max_xor = temp
                break

    return max_xor
```
**Time**: O(32n), **Space**: O(n)

### M6: Subsets
```python
def subsets(nums):
    n = len(nums)
    result = []

    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if (mask >> i) & 1:
                subset.append(nums[i])
        result.append(subset)

    return result
```
**Time**: O(2^n * n), **Space**: O(2^n * n)

### M7: Total Hamming Distance
```python
def total_hamming_distance(nums):
    total = 0
    n = len(nums)

    for i in range(32):
        count_ones = sum((num >> i) & 1 for num in nums)
        count_zeros = n - count_ones
        total += count_ones * count_zeros

    return total
```
**Time**: O(32n) = O(n), **Space**: O(1)

---

## Hard Problems

### H2: Minimum XOR Sum (DP with Bitmask)
```python
def minimum_xor_sum(nums1, nums2):
    n = len(nums1)
    dp = [float('inf')] * (1 << n)
    dp[0] = 0

    for mask in range(1 << n):
        i = bin(mask).count('1')
        if i >= n:
            continue

        for j in range(n):
            if not (mask & (1 << j)):
                new_mask = mask | (1 << j)
                dp[new_mask] = min(dp[new_mask],
                                  dp[mask] + (nums1[i] ^ nums2[j]))

    return dp[(1 << n) - 1]
```
**Time**: O(2^n * n), **Space**: O(2^n)

---

Master these solutions - bit manipulation is elegant and powerful!
