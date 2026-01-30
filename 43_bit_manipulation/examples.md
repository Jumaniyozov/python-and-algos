# Chapter 43: Bit Manipulation - Examples

## Basic Bit Operations

### Example 1: Number of 1 Bits (LeetCode 191)
```python
def hamming_weight(n):
    """
    Count number of 1 bits.

    Time: O(number of 1 bits)
    Space: O(1)
    """
    count = 0
    while n:
        n &= n - 1  # Clear rightmost set bit
        count += 1
    return count

# Example: 11 (binary 1011) → 3
print(hamming_weight(11))  # 3
```

---

### Example 2: Power of Two (LeetCode 231)
```python
def is_power_of_two(n):
    """
    Check if n is power of 2.

    Key insight: Power of 2 has exactly one bit set.

    Time: O(1)
    Space: O(1)
    """
    return n > 0 and (n & (n - 1)) == 0

# Examples
print(is_power_of_two(16))  # True (10000)
print(is_power_of_two(6))   # False (110)
```

---

### Example 3: Reverse Bits (LeetCode 190)
```python
def reverse_bits(n):
    """
    Reverse bits of 32-bit integer.

    Time: O(32) = O(1)
    Space: O(1)
    """
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

# Example: reverse binary of 5 (00000101 → 10100000)
print(reverse_bits(5))
```

---

## XOR Problems

### Example 4: Single Number (LeetCode 136)
```python
def single_number(nums):
    """
    Find element appearing once (others appear twice).

    XOR property: a ^ a = 0, a ^ 0 = a

    Time: O(n)
    Space: O(1)
    """
    result = 0
    for num in nums:
        result ^= num
    return result

# Example: [2,2,1] → 1
print(single_number([2, 2, 1]))  # 1
```

---

### Example 5: Single Number III (LeetCode 260)
```python
def single_number_iii(nums):
    """
    Find two elements appearing once (others twice).

    Time: O(n)
    Space: O(1)
    """
    # Get XOR of two unique numbers
    xor = 0
    for num in nums:
        xor ^= num

    # Find rightmost set bit (where two numbers differ)
    diff_bit = xor & -xor

    # Partition into two groups and XOR each
    a = b = 0
    for num in nums:
        if num & diff_bit:
            a ^= num
        else:
            b ^= num

    return [a, b]

# Example: [1,2,1,3,2,5] → [3,5]
print(single_number_iii([1, 2, 1, 3, 2, 5]))
```

---

### Example 6: Missing Number (LeetCode 268)
```python
def missing_number(nums):
    """
    Find missing number in 0..n.

    XOR approach: XOR all indices and values.

    Time: O(n)
    Space: O(1)
    """
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result

# Alternative: sum approach
def missing_number_sum(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)

# Example: [0,1,3] → 2
print(missing_number([0, 1, 3]))  # 2
```

---

## Bit Counting and Manipulation

### Example 7: Counting Bits (LeetCode 338)
```python
def counting_bits(n):
    """
    Count 1 bits for each number from 0 to n.

    DP approach: dp[i] = dp[i & (i-1)] + 1

    Time: O(n)
    Space: O(n)
    """
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i & (i - 1)] + 1
    return dp

# Alternative: DP with right shift
def counting_bits_v2(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp

# Example: n=5 → [0,1,1,2,1,2]
print(counting_bits(5))
```

---

### Example 8: Hamming Distance (LeetCode 461)
```python
def hamming_distance(x, y):
    """
    Count positions where bits differ.

    Time: O(log(max(x,y)))
    Space: O(1)
    """
    xor = x ^ y
    count = 0
    while xor:
        xor &= xor - 1
        count += 1
    return count

# Example: 1 (0001) and 4 (0100) → 2
print(hamming_distance(1, 4))  # 2
```

---

## Bit Masks and State

### Example 9: Subsets Using Bitmask (LeetCode 78)
```python
def subsets(nums):
    """
    Generate all subsets using bitmask.

    Time: O(2^n * n)
    Space: O(2^n * n)
    """
    n = len(nums)
    result = []

    for mask in range(1 << n):  # 2^n possibilities
        subset = []
        for i in range(n):
            if (mask >> i) & 1:
                subset.append(nums[i])
        result.append(subset)

    return result

# Example: [1,2,3] → 8 subsets
print(subsets([1, 2, 3]))
```

---

### Example 10: Maximum XOR of Two Numbers (LeetCode 421)
```python
def find_maximum_xor(nums):
    """
    Find maximum XOR of two numbers in array.

    Time: O(32n)
    Space: O(n)
    """
    max_xor = 0
    mask = 0

    # Build result bit by bit from left (most significant)
    for i in range(31, -1, -1):
        mask |= (1 << i)

        # Get all prefixes with current mask
        prefixes = {num & mask for num in nums}

        # Try to maximize current bit
        temp = max_xor | (1 << i)

        # Check if we can achieve this
        for prefix in prefixes:
            if (temp ^ prefix) in prefixes:
                max_xor = temp
                break

    return max_xor

# Example: [3,10,5,25,2,8] → 28 (5 ^ 25)
print(find_maximum_xor([3, 10, 5, 25, 2, 8]))
```

---

## Bit Tricks

### Example 11: Swap Numbers Without Temp
```python
def swap(a, b):
    """
    Swap without temporary variable.

    Time: O(1)
    Space: O(1)
    """
    a ^= b
    b ^= a  # b = b ^ (a ^ b) = a
    a ^= b  # a = (a ^ b) ^ a = b
    return a, b

# Example
a, b = 5, 10
a, b = swap(a, b)
print(f"a={a}, b={b}")  # a=10, b=5
```

---

### Example 12: UTF-8 Validation (LeetCode 393)
```python
def valid_utf8(data):
    """
    Validate UTF-8 encoding.

    Time: O(n)
    Space: O(1)
    """
    n_bytes = 0

    for num in data:
        if n_bytes == 0:
            # Count leading 1s
            if (num >> 5) == 0b110:
                n_bytes = 1
            elif (num >> 4) == 0b1110:
                n_bytes = 2
            elif (num >> 3) == 0b11110:
                n_bytes = 3
            elif (num >> 7):
                return False
        else:
            # Must start with 10
            if (num >> 6) != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0

# Example: [197,130,1] → True
print(valid_utf8([197, 130, 1]))
```

---

## Summary

These examples demonstrate:

1. **Basic Operations**: Counting bits, checking power of 2
2. **XOR Tricks**: Finding unique elements, missing numbers
3. **Bit Counting**: DP approaches for counting bits
4. **Bitmasks**: State representation, generating subsets
5. **Advanced**: Maximum XOR, UTF-8 validation

**Key Techniques**:
- XOR for finding unique elements
- `n & (n-1)` for counting/clearing bits
- Bitmasks for state representation
- Left/right shifts for building results

Practice until bit manipulation becomes intuitive!
