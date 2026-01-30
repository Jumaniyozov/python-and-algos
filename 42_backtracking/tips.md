# Chapter 42: Backtracking - Tips and Tricks

## Common Pitfalls

### 1. Forgetting to Copy Result
```python
# ❌ WRONG
result.append(path)  # Reference, will change later!

# ✅ CORRECT
result.append(path[:])  # Make copy
result.append(path.copy())
```

### 2. Not Handling Duplicates
```python
# ❌ WRONG: Will have duplicates
for i in range(start, len(nums)):
    backtrack(i + 1, path + [nums[i]])

# ✅ CORRECT: Skip duplicates
nums.sort()  # Sort first
for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i-1]:
        continue
    backtrack(i + 1, path + [nums[i]])
```

### 3. Wrong Base Case
```python
# ❌ WRONG: Missing all intermediate subsets
if len(path) == len(nums):
    result.append(path[:])

# ✅ CORRECT: All states are valid for subsets
result.append(path[:])  # Add before recursing
```

---

## Pattern Recognition

### Pattern 1: Permutations
**Indicator**: All arrangements, order matters
**Template**: Track remaining/used elements

### Pattern 2: Combinations
**Indicator**: Choose k from n, order doesn't matter
**Template**: Use start index

### Pattern 3: Subsets
**Indicator**: All possible subsets
**Template**: Every state is valid

### Pattern 4: Partition
**Indicator**: Split into valid groups
**Template**: Try all split points

### Pattern 5: Constraint Satisfaction
**Indicator**: N-Queens, Sudoku, etc.
**Template**: Check validity before recursing

---

## LeetCode Practice Problems (50+ problems)

### Permutations/Combinations/Subsets (12)
1. [Permutations (46)](https://leetcode.com/problems/permutations/)
2. [Permutations II (47)](https://leetcode.com/problems/permutations-ii/)
3. [Combinations (77)](https://leetcode.com/problems/combinations/)
4. [Combination Sum (39)](https://leetcode.com/problems/combination-sum/)
5. [Combination Sum II (40)](https://leetcode.com/problems/combination-sum-ii/)
6. [Combination Sum III (216)](https://leetcode.com/problems/combination-sum-iii/)
7. [Subsets (78)](https://leetcode.com/problems/subsets/)
8. [Subsets II (90)](https://leetcode.com/problems/subsets-ii/)
9. [Factor Combinations (254)](https://leetcode.com/problems/factor-combinations/)
10. [Letter Combinations (17)](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
11. [Generate Parentheses (22)](https://leetcode.com/problems/generate-parentheses/)
12. [Gray Code (89)](https://leetcode.com/problems/gray-code/)

### String Backtracking (10)
13. [Palindrome Partitioning (131)](https://leetcode.com/problems/palindrome-partitioning/)
14. [Palindrome Partitioning II (132)](https://leetcode.com/problems/palindrome-partitioning-ii/)
15. [Restore IP Addresses (93)](https://leetcode.com/problems/restore-ip-addresses/)
16. [Word Break II (140)](https://leetcode.com/problems/word-break-ii/)
17. [Different Ways to Add Parentheses (241)](https://leetcode.com/problems/different-ways-to-add-parentheses/)
18. [Remove Invalid Parentheses (301)](https://leetcode.com/problems/remove-invalid-parentheses/)
19. [Expression Add Operators (282)](https://leetcode.com/problems/expression-add-operators/)
20. [Additive Number (306)](https://leetcode.com/problems/additive-number/)
21. [Word Pattern II (291)](https://leetcode.com/problems/word-pattern-ii/)
22. [Strobogrammatic Number II (247)](https://leetcode.com/problems/strobogrammatic-number-ii/)

### Grid Backtracking (8)
23. [Word Search (79)](https://leetcode.com/problems/word-search/)
24. [Word Search II (212)](https://leetcode.com/problems/word-search-ii/)
25. [N-Queens (51)](https://leetcode.com/problems/n-queens/)
26. [N-Queens II (52)](https://leetcode.com/problems/n-queens-ii/)
27. [Sudoku Solver (37)](https://leetcode.com/problems/sudoku-solver/)
28. [Robot Room Cleaner (489)](https://leetcode.com/problems/robot-room-cleaner/)
29. [Unique Paths III (980)](https://leetcode.com/problems/unique-paths-iii/)
30. [Matchsticks to Square (473)](https://leetcode.com/problems/matchsticks-to-square/)

### Partition Problems (7)
31. [Partition to K Equal Sum Subsets (698)](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)
32. [Split Array into Fibonacci Sequence (842)](https://leetcode.com/problems/split-array-into-fibonacci-like-sequence/)
33. [Optimal Account Balancing (465)](https://leetcode.com/problems/optimal-account-balancing/)
34. [Partition Equal Subset Sum (416)](https://leetcode.com/problems/partition-equal-subset-sum/)
35. [Beautiful Arrangement (526)](https://leetcode.com/problems/beautiful-arrangement/)
36. [Construct the Lexicographically Largest (1718)](https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/)
37. [Verbal Arithmetic Puzzle (1307)](https://leetcode.com/problems/verbal-arithmetic-puzzle/)

### Advanced Backtracking (13)
38. [Sudoku Solver (37)](https://leetcode.com/problems/sudoku-solver/)
39. [Wildcard Matching (44)](https://leetcode.com/problems/wildcard-matching/)
40. [Regular Expression Matching (10)](https://leetcode.com/problems/regular-expression-matching/)
41. [Numbers With Same Consecutive Differences (967)](https://leetcode.com/problems/numbers-with-same-consecutive-differences/)
42. [Max Length of Concatenated String (1239)](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)
43. [Letter Tile Possibilities (1079)](https://leetcode.com/problems/letter-tile-possibilities/)
44. [Increasing Subsequences (491)](https://leetcode.com/problems/increasing-subsequences/)
45. [All Paths From Source to Target (797)](https://leetcode.com/problems/all-paths-from-source-to-target/)
46. [Shopping Offers (638)](https://leetcode.com/problems/shopping-offers/)
47. [Flatten Nested List Iterator (341)](https://leetcode.com/problems/flatten-nested-list-iterator/)
48. [Iterator for Combination (1286)](https://leetcode.com/problems/iterator-for-combination/)
49. [Flip Game II (294)](https://leetcode.com/problems/flip-game-ii/)
50. [Android Unlock Patterns (351)](https://leetcode.com/problems/android-unlock-patterns/)
51. [24 Game (679)](https://leetcode.com/problems/24-game/)
52. [Confusing Number II (1088)](https://leetcode.com/problems/confusing-number-ii/)

---

## Study Plan

**Week 1**: Permutations/Combinations/Subsets (1-12)
**Week 2**: String problems (13-22)
**Week 3**: Grid problems (23-30)
**Week 4**: Partition and Advanced (31-52)

Master backtracking - it's a powerful technique!
