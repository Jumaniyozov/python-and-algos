# Chapter 43: Bit Manipulation

## Overview

Bit manipulation involves using bitwise operators to solve problems efficiently. It's essential for optimization, low-level programming, and many interview problems. This chapter covers bitwise operators, common tricks, and problem-solving patterns.

## Learning Objectives

1. Master bitwise operators (&, |, ^, ~, <<, >>)
2. Understand XOR properties and applications
3. Apply common bit tricks and patterns
4. Use bit masks for state representation
5. Count and manipulate individual bits
6. Solve optimization problems with bits
7. Recognize when bit manipulation simplifies solutions

## Chapter Structure

- **theory.md** - Bitwise operators, properties, common tricks
- **examples.md** - Classic bit manipulation problems
- **exercises.md** - 15 practice problems
- **solutions.md** - Complete solutions with explanations
- **tips.md** - Tips, tricks, and 35+ LeetCode problems

## Prerequisites

- Binary number system
- Basic arithmetic
- Arrays (Chapter 29)
- Mathematics

## Key Concepts

### Bitwise Operators

- **AND (&)**: Both bits must be 1
- **OR (|)**: At least one bit must be 1
- **XOR (^)**: Bits must be different
- **NOT (~)**: Flip all bits
- **Left Shift (<<)**: Multiply by 2
- **Right Shift (>>)**: Divide by 2

### Common Tricks

- Check if power of 2: `n & (n-1) == 0`
- Get lowest set bit: `n & -n`
- Clear lowest set bit: `n & (n-1)`
- Set bit at position i: `n | (1 << i)`
- Clear bit at position i: `n & ~(1 << i)`
- Toggle bit at position i: `n ^ (1 << i)`
- Check bit at position i: `(n >> i) & 1`

### XOR Properties

- `a ^ a = 0`
- `a ^ 0 = a`
- `a ^ b ^ a = b`
- XOR is commutative and associative

## Time Complexity

Most bit operations: **O(1)** for fixed-size integers

## Navigation

- **Previous**: [Chapter 42: Backtracking](../42_backtracking/README.md)
- **Next**: [Chapter 44: Advanced Algorithms](../44_advanced_algorithms/README.md)
- **Home**: [Main README](../README.md)

---

## Quick Reference

### Common Bit Tricks

```python
# Check if number is power of 2
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Count number of 1 bits
def count_bits(n):
    count = 0
    while n:
        n &= n - 1  # Clear lowest set bit
        count += 1
    return count

# Get bit at position i
def get_bit(n, i):
    return (n >> i) & 1

# Set bit at position i
def set_bit(n, i):
    return n | (1 << i)

# Clear bit at position i
def clear_bit(n, i):
    return n & ~(1 << i)

# Toggle bit at position i
def toggle_bit(n, i):
    return n ^ (1 << i)

# Swap two numbers without temp
def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b
```

## Study Time

- Theory: 2-3 hours
- Examples: 3-4 hours
- Exercises: 6-8 hours
- LeetCode (35+ problems): 35-50 hours

**Total**: 46-65 hours for mastery

Happy learning! Bit manipulation is powerful and elegant!
