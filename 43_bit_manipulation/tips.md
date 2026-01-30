# Chapter 43: Bit Manipulation - Tips and Tricks

## Common Pitfalls

### 1. Forgetting Negative Numbers
```python
# ❌ WRONG: Doesn't work for negative
def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1  # Infinite loop for negative!
    return count

# ✅ CORRECT: Handle 32 bits explicitly
def count_bits(n):
    count = 0
    for _ in range(32):
        count += n & 1
        n >>= 1
    return count
```

### 2. Operator Precedence
```python
# ❌ WRONG
if n & 1 == 0:  # Parsed as: n & (1 == 0)

# ✅ CORRECT
if (n & 1) == 0:  # Use parentheses
```

### 3. Not Using XOR Properties
```python
# ❌ WRONG: Using extra space
def single_number(nums):
    seen = set()
    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)
    return seen.pop()

# ✅ CORRECT: XOR all elements
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

---

## Pattern Recognition

### Pattern 1: XOR for Uniqueness
**Indicator**: Find element appearing odd times
**Approach**: XOR all elements

### Pattern 2: Bit Counting
**Indicator**: Count 1 bits, Hamming distance
**Approach**: Use `n & (n-1)` to clear bits

### Pattern 3: Power of 2
**Indicator**: Check/generate powers of 2
**Approach**: `n & (n-1) == 0`

### Pattern 4: Bitmask State
**Indicator**: Represent sets, subsets
**Approach**: Use integer as bitmask

### Pattern 5: Bit Shifts
**Indicator**: Multiply/divide by powers of 2
**Approach**: Use `<<` and `>>`

---

## Quick Reference

### Essential Tricks

```python
# Check if power of 2
n > 0 and (n & (n-1)) == 0

# Get lowest set bit
n & -n

# Clear lowest set bit
n & (n-1)

# Count 1 bits
count = 0
while n:
    n &= n-1
    count += 1

# Check bit i
(n >> i) & 1

# Set bit i
n | (1 << i)

# Clear bit i
n & ~(1 << i)

# Toggle bit i
n ^ (1 << i)

# Swap without temp
a ^= b; b ^= a; a ^= b

# Iterate all subsets
for mask in range(1 << n):
    # Process mask
```

---

## LeetCode Practice Problems (35+ problems)

### Basic Operations (10)
1. [Number of 1 Bits (191)](https://leetcode.com/problems/number-of-1-bits/)
2. [Reverse Bits (190)](https://leetcode.com/problems/reverse-bits/)
3. [Power of Two (231)](https://leetcode.com/problems/power-of-two/)
4. [Power of Four (342)](https://leetcode.com/problems/power-of-four/)
5. [Hamming Distance (461)](https://leetcode.com/problems/hamming-distance/)
6. [Counting Bits (338)](https://leetcode.com/problems/counting-bits/)
7. [Binary Number Alternating Bits (693)](https://leetcode.com/problems/binary-number-with-alternating-bits/)
8. [Number Complement (476)](https://leetcode.com/problems/number-complement/)
9. [Convert to Base -2 (1017)](https://leetcode.com/problems/convert-to-base-2/)
10. [Sum of Two Integers (371)](https://leetcode.com/problems/sum-of-two-integers/)

### XOR Problems (8)
11. [Single Number (136)](https://leetcode.com/problems/single-number/)
12. [Single Number II (137)](https://leetcode.com/problems/single-number-ii/)
13. [Single Number III (260)](https://leetcode.com/problems/single-number-iii/)
14. [Missing Number (268)](https://leetcode.com/problems/missing-number/)
15. [Find Duplicate (287)](https://leetcode.com/problems/find-the-duplicate-number/)
16. [XOR Queries (1310)](https://leetcode.com/problems/xor-queries-of-a-subarray/)
17. [XOR Operation in Array (1486)](https://leetcode.com/problems/xor-operation-in-an-array/)
18. [Decode XORed Array (1720)](https://leetcode.com/problems/decode-xored-array/)

### Bitmask/Subsets (7)
19. [Subsets (78)](https://leetcode.com/problems/subsets/)
20. [Subsets II (90)](https://leetcode.com/problems/subsets-ii/)
21. [Maximum Product of Word Lengths (318)](https://leetcode.com/problems/maximum-product-of-word-lengths/)
22. [Partition Equal Subset Sum (416)](https://leetcode.com/problems/partition-equal-subset-sum/)
23. [Shortest Path Visiting All Nodes (847)](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)
24. [Fair Distribution of Cookies (2305)](https://leetcode.com/problems/fair-distribution-of-cookies/)
25. [Maximum Students (1349)](https://leetcode.com/problems/maximum-students-taking-exam/)

### Advanced Bit Manipulation (10)
26. [Bitwise AND Range (201)](https://leetcode.com/problems/bitwise-and-of-numbers-range/)
27. [Maximum XOR (421)](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)
28. [Total Hamming Distance (477)](https://leetcode.com/problems/total-hamming-distance/)
29. [UTF-8 Validation (393)](https://leetcode.com/problems/utf-8-validation/)
30. [Bitwise ORs of Subarrays (898)](https://leetcode.com/problems/bitwise-ors-of-subarrays/)
31. [Smallest Sufficient Team (1125)](https://leetcode.com/problems/smallest-sufficient-team/)
32. [Find XOR Beauty (2527)](https://leetcode.com/problems/find-xor-beauty-of-array/)
33. [Minimum One Bit Operations (1611)](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/)
34. [Maximum XOR With Element (1707)](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)
35. [Number of Valid Words (1178)](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/)

### Hard Problems (5+)
36. [Minimum XOR Sum (1879)](https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/)
37. [Maximum Genetic Difference (1938)](https://leetcode.com/problems/maximum-genetic-difference-query/)
38. [Tiling Rectangle (1240)](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/)
39. [Count Triplets (982)](https://leetcode.com/problems/number-of-wonderful-substrings/)
40. [K-th Symbol (779)](https://leetcode.com/problems/k-th-symbol-in-grammar/)

---

## Study Plan

**Week 1**: Basic operations (1-10)
**Week 2**: XOR problems (11-18)
**Week 3**: Bitmask/subsets (19-25)
**Week 4**: Advanced (26-40)

---

## Optimization Tips

### 1. Use Bit Shifts for Powers of 2
```python
# Instead of
n * 8
n / 4

# Use
n << 3  # Multiply by 8
n >> 2  # Divide by 4
```

### 2. Check Even/Odd Efficiently
```python
# Instead of
if n % 2 == 0:

# Use
if (n & 1) == 0:
```

### 3. Clear All Bits After Position i
```python
n & ((1 << i) - 1)
```

### 4. Set All Bits After Position i
```python
n | ~((1 << (i + 1)) - 1)
```

---

## Summary

**Essential Operations:**
- XOR for uniqueness
- `n & (n-1)` for bit manipulation
- Bitmasks for state
- Shifts for efficiency

**Common Patterns:**
1. XOR all elements → find unique
2. Count bits with `n & (n-1)`
3. Use masks for subsets
4. Check power of 2 with `n & (n-1) == 0`

**Complexity:**
- Most operations: O(1) or O(log n)
- Bitmask DP: O(2^n)

Master bit manipulation - it's elegant, efficient, and powerful!
