# Chapter 43: Bit Manipulation - Theory

## Table of Contents
1. [Binary Basics](#binary-basics)
2. [Bitwise Operators](#bitwise-operators)
3. [XOR Properties](#xor-properties)
4. [Common Bit Tricks](#common-bit-tricks)
5. [Bit Masks](#bit-masks)
6. [Applications](#applications)

---

## Binary Basics

### Binary Representation

```
Decimal: 13
Binary:  1101

Position: 3  2  1  0
Bit:      1  1  0  1
Value:    8  4  0  1  → 8+4+1 = 13
```

### Signed Integers (Two's Complement)

```
Positive 5:   0000 0101
Negative -5:  1111 1011  (flip bits and add 1)
```

---

## Bitwise Operators

### AND (&)
Both bits must be 1

```
  1101  (13)
& 1011  (11)
------
  1001  (9)
```

**Uses**: Check if bit is set, clear bits, mask operations

```python
# Check if bit i is set
def is_bit_set(n, i):
    return (n & (1 << i)) != 0
```

### OR (|)
At least one bit is 1

```
  1101  (13)
| 1011  (11)
------
  1111  (15)
```

**Uses**: Set bits, combine flags

```python
# Set bit i
def set_bit(n, i):
    return n | (1 << i)
```

### XOR (^)
Bits must be different

```
  1101  (13)
^ 1011  (11)
------
  0110  (6)
```

**Uses**: Toggle bits, find unique elements, swap without temp

```python
# Toggle bit i
def toggle_bit(n, i):
    return n ^ (1 << i)

# Swap without temp
a ^= b
b ^= a
a ^= b
```

### NOT (~)
Flip all bits

```
~ 0000 1101  (13)
  -----------
  1111 0010  (-14 in two's complement)
```

**Uses**: Create masks, bit manipulation

### Left Shift (<<)
Multiply by 2^k

```
13 << 2:
  1101  →  110100  (52)
Equivalent to: 13 * 4 = 52
```

### Right Shift (>>)
Divide by 2^k

```
13 >> 2:
  1101  →  11  (3)
Equivalent to: 13 // 4 = 3
```

---

## XOR Properties

### Key Properties

1. **Self-cancelling**: `a ^ a = 0`
2. **Identity**: `a ^ 0 = a`
3. **Commutative**: `a ^ b = b ^ a`
4. **Associative**: `(a ^ b) ^ c = a ^ (b ^ c)`
5. **Inverse**: `a ^ b ^ a = b`

### Applications

**Find unique element:**
```python
def single_number(nums):
    """All appear twice except one."""
    result = 0
    for num in nums:
        result ^= num
    return result
# [2,2,3,3,5] → 5
```

**Swap without temp:**
```python
a ^= b
b ^= a  # b = b ^ (a ^ b) = a
a ^= b  # a = (a ^ b) ^ a = b
```

**Check if two numbers are different:**
```python
def are_different(a, b):
    return (a ^ b) != 0
```

---

## Common Bit Tricks

### 1. Check Power of 2

```python
def is_power_of_two(n):
    """Power of 2 has exactly one bit set."""
    return n > 0 and (n & (n - 1)) == 0

# 8:  1000
# 7:  0111
# &:  0000  → True

# 6:  0110
# 5:  0101
# &:  0100  → False
```

### 2. Count Set Bits

```python
def hamming_weight(n):
    """Count number of 1 bits."""
    count = 0
    while n:
        n &= (n - 1)  # Clear rightmost set bit
        count += 1
    return count

# Alternative (Brian Kernighan's algorithm)
def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

### 3. Get Lowest Set Bit

```python
def lowest_set_bit(n):
    """Get rightmost set bit."""
    return n & -n

# 12:  1100
# -12: 0100  (two's complement)
# &:   0100  → 4
```

### 4. Clear Lowest Set Bit

```python
def clear_lowest_bit(n):
    """Remove rightmost set bit."""
    return n & (n - 1)

# 12:  1100
# 11:  1011
# &:   1000  → 8
```

### 5. Isolate Rightmost 1

```python
def isolate_rightmost_one(n):
    return n & -n
```

### 6. Isolate Rightmost 0

```python
def isolate_rightmost_zero(n):
    return ~n & (n + 1)
```

### 7. Check if i-th Bit is Set

```python
def is_bit_set(n, i):
    return (n >> i) & 1 == 1

# Alternative
def is_bit_set(n, i):
    return (n & (1 << i)) != 0
```

### 8. Set i-th Bit

```python
def set_bit(n, i):
    return n | (1 << i)
```

### 9. Clear i-th Bit

```python
def clear_bit(n, i):
    return n & ~(1 << i)
```

### 10. Toggle i-th Bit

```python
def toggle_bit(n, i):
    return n ^ (1 << i)
```

---

## Bit Masks

### Using Masks for State

```python
# Represent set of elements as bitmask
def has_element(mask, i):
    """Check if element i is in set."""
    return (mask >> i) & 1

def add_element(mask, i):
    """Add element i to set."""
    return mask | (1 << i)

def remove_element(mask, i):
    """Remove element i from set."""
    return mask & ~(1 << i)

def toggle_element(mask, i):
    """Toggle element i."""
    return mask ^ (1 << i)

# Iterate over all subsets
for mask in range(1 << n):
    # Process subset represented by mask
    subset = [i for i in range(n) if (mask >> i) & 1]
```

### Iterate Over All Subsets

```python
def all_subsets(nums):
    """Generate all subsets using bitmask."""
    n = len(nums)
    result = []

    for mask in range(1 << n):  # 2^n possibilities
        subset = []
        for i in range(n):
            if (mask >> i) & 1:
                subset.append(nums[i])
        result.append(subset)

    return result
```

---

## Applications

### 1. Find Missing Number

```python
def missing_number(nums):
    """Find missing number in 0..n."""
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result
```

### 2. Single Number

```python
def single_number(nums):
    """All appear twice except one."""
    result = 0
    for num in nums:
        result ^= num
    return result
```

### 3. Reverse Bits

```python
def reverse_bits(n):
    """Reverse bits of 32-bit integer."""
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```

### 4. Hamming Distance

```python
def hamming_distance(x, y):
    """Count positions where bits differ."""
    xor = x ^ y
    count = 0
    while xor:
        xor &= xor - 1
        count += 1
    return count
```

---

## Summary

**Key Operators:**
- AND (&): Mask and check
- OR (|): Set bits
- XOR (^): Toggle and find unique
- NOT (~): Flip bits
- Shifts (<<, >>): Multiply/divide by 2

**Essential Tricks:**
- Power of 2: `n & (n-1) == 0`
- Count bits: Keep clearing lowest bit
- Get lowest bit: `n & -n`
- XOR for uniqueness

**Common Patterns:**
- Use XOR to find unique elements
- Use bitmasks for state representation
- Use shifts for efficient multiplication/division
- Use AND/OR/XOR for flag operations

Master these fundamentals - bit manipulation is powerful!
