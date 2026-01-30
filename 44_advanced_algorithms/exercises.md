# Advanced Algorithms - Exercises

## String Algorithms

### Exercise 1: Repeated Substring Pattern (Easy)
Given a string s, check if it can be constructed by taking a substring and repeating it multiple times.

```
Example 1:
Input: s = "abab"
Output: true
Explanation: "ab" repeated twice

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: "abc" repeated 4 times
```

**Hint**: Use KMP LPS array to detect repeating patterns.

---

### Exercise 2: Shortest Palindrome (Hard)
Given a string s, find the shortest palindrome by adding characters in front of it.

```
Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: s = "abcd"
Output: "dcbabcd"
```

**Hint**: Use KMP to find longest palindromic prefix.

---

### Exercise 3: Distinct Echo Substrings (Hard)
Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (i.e. "aa", "abab", "xyzxyz").

```
Example:
Input: text = "abcabcabc"
Output: 3
Explanation: "abcabc", "bcabca", "cabcab"
```

**Hint**: Use rolling hash (Rabin-Karp) to efficiently check echo patterns.

---

### Exercise 4: Longest Happy Prefix (Medium)
A string is called a happy prefix if it is a non-empty prefix which is also a suffix (excluding itself).

```
Example 1:
Input: s = "level"
Output: "l"

Example 2:
Input: s = "ababab"
Output: "abab"
```

**Hint**: Use KMP LPS array.

---

### Exercise 5: Palindrome Pairs (Hard)
Given a list of unique words, return all pairs of distinct indices (i, j) such that the concatenation of words[i] + words[j] is a palindrome.

```
Example:
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation:
- "abcddcba" (words[0] + words[1])
- "dcbaabcd" (words[1] + words[0])
- "slls" (words[3] + words[2])
- "llssssll" (words[2] + words[4])
```

**Hint**: Use Manacher's algorithm or hash map with reversed strings.

---

## Sliding Window Maximum

### Exercise 6: Sliding Window Median (Hard)
Given an array nums and window size k, return the median of each window.

```
Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1,-1,-1,3,5,6]

Window [1 3 -1] → median = 1
Window [3 -1 -3] → median = -1
Window [-1 -3 5] → median = -1
```

**Hint**: Use two heaps (max heap for left half, min heap for right half).

---

### Exercise 7: Constrained Subsequence Sum (Hard)
Return the maximum sum of a non-empty subsequence where the difference between consecutive indices is at most k.

```
Example:
Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: Subsequence is [10, 2, 5, 20]
```

**Hint**: Use monotonic deque with DP.

---

### Exercise 8: Jump Game VI (Medium)
Given array nums and integer k, you can jump at most k steps forward. Maximize the sum of elements you land on.

```
Example:
Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: Jump indices: 0 → 3 → 5 (1 + 4 + 3 = 7)
```

**Hint**: DP with monotonic deque optimization.

---

## Cache Design

### Exercise 9: Time-Based Key-Value Store (Medium)
Design a time-based key-value store that can store multiple values for the same key at different timestamps and retrieve the key's value at a certain timestamp.

```
Operations:
- set(key, value, timestamp)
- get(key, timestamp) → return value at most recent timestamp ≤ given timestamp
```

**Hint**: HashMap + binary search on timestamps.

---

### Exercise 10: LFU Cache with TTL (Hard)
Design an LFU cache with time-to-live functionality. Each entry expires after a given TTL.

```
Operations:
- get(key)
- put(key, value, ttl)
- Both O(1) excluding expired entries
```

**Hint**: Combine LFU with min-heap for expiration times.

---

## Bitmask DP

### Exercise 11: Maximum Students Taking Exam (Hard)
Given an m x n binary matrix seats where seats[i][j] = 1 represents a broken seat, return the maximum number of students that can take the exam so no two students cheat (adjacent horizontally or diagonally).

```
Example:
Input: seats = [
  [1,0,0,0,1,1],
  [0,0,1,0,1,0],
  [0,0,0,0,0,0]
]
Output: 4
```

**Hint**: Use bitmask DP where each state represents valid seating in a row.

---

### Exercise 12: Minimum Cost to Connect Two Groups (Hard)
You are given two groups of points. Each point in the first group must be connected to at least one point in the second group, and vice versa. Return the minimum cost.

```
Example:
Input: cost = [[15, 96], [36, 2]]
Output: 17
Explanation: Connect group1[0] to group2[1] (cost 96) and group1[1] to group2[1] (cost 2) = 98? No!
Connect group1[0] to group2[0] (15) and group1[1] to group2[1] (2) = 17
```

**Hint**: Bitmask DP to track which nodes in second group are connected.

---

### Exercise 13: Number of Ways to Wear Different Hats (Hard)
There are n people and 40 types of hats. Given a list of hats for each person, return the number of ways to assign hats such that no two people wear the same hat.

```
Example:
Input: hats = [[3,4],[4,5],[5]]
Output: 1
Explanation: Person 0 wears hat 3, person 1 wears hat 4, person 2 wears hat 5
```

**Hint**: Iterate over hats, use bitmask to track which people have hats.

---

## Digit DP

### Exercise 14: Numbers At Most N Given Digit Set (Hard)
Given an array of digits and integer n, return how many positive integers ≤ n can be formed using digits from the array (digits can be repeated).

```
Example:
Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation: 1,3,5,7,11,13,15,17,31,33,35,37,51,53,55,57,71,73,75,77
```

**Hint**: Digit DP with tight constraint.

---

### Exercise 15: Count Special Integers (Hard)
Count integers from 1 to n where all digits are distinct.

```
Example:
Input: n = 20
Output: 19
Explanation: All numbers except 11
```

**Hint**: Digit DP tracking used digits with bitmask.

---

### Exercise 16: Numbers With Repeated Digits (Hard)
Count integers from 1 to n with at least one repeated digit.

```
Example:
Input: n = 100
Output: 10
Explanation: 11,22,33,44,55,66,77,88,99,100
```

**Hint**: Count total minus count of numbers with distinct digits.

---

## Monotonic Stack/Queue

### Exercise 17: Sum of Subarray Minimums (Medium)
Given an array, return the sum of minimum values of all subarrays.

```
Example:
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays: [3]=3, [1]=1, [2]=2, [4]=4, [3,1]=1, [1,2]=1, [2,4]=2, [3,1,2]=1, [1,2,4]=1, [3,1,2,4]=1
Sum = 3+1+2+4+1+1+2+1+1+1 = 17
```

**Hint**: Use monotonic stack to find range where each element is minimum.

---

### Exercise 18: Maximum Width Ramp (Medium)
Given array A, a ramp is a pair (i, j) where i < j and A[i] ≤ A[j]. Find maximum j - i.

```
Example:
Input: A = [6,0,8,2,1,5]
Output: 4
Explanation: i=1, j=5 (A[1]=0, A[5]=5)
```

**Hint**: Monotonic stack to build potential starting points.

---

### Exercise 19: Shortest Subarray with Sum at Least K (Hard)
Return the length of the shortest non-empty subarray with sum ≥ K. Return -1 if no such subarray exists.

```
Example:
Input: nums = [2,-1,2], K = 3
Output: 3
Explanation: Entire array sums to 3
```

**Hint**: Prefix sum + monotonic deque.

---

### Exercise 20: Maximum Building Height (Hard)
You want to build n buildings in a row. Some buildings have height restrictions. Maximize the height of the tallest building while respecting restrictions and ensuring adjacent buildings differ by at most 1 in height.

```
Example:
Input: n = 5, restrictions = [[2,1],[4,1]]
Output: 2
Explanation: Build: [0,1,2,1,2] or [1,1,2,1,2]
```

**Hint**: Process restrictions in sorted order, calculate maximum possible height.

---

## Comprehensive Problems

### Exercise 21: Design Search Autocomplete System (Hard)
Design a search autocomplete system. Users type sentences and the system suggests top 3 historical hot sentences that start with the prefix.

```
Operations:
- input(c) → return list of top 3 suggestions
- If c == '#', save current sentence and reset
```

**Hint**: Trie + frequency tracking + sorting.

---

### Exercise 22: Count Unique Characters (Hard)
Let's define a function countUniqueChars(s) that returns the number of unique characters in s. Return sum of countUniqueChars(substring) for all substrings.

```
Example:
Input: s = "ABC"
Output: 10
Explanation:
"A" → 1, "B" → 1, "C" → 1
"AB" → 2, "BC" → 2, "ABC" → 3
Sum = 1+1+1+2+2+3 = 10
```

**Hint**: For each character, count subarrays where it appears exactly once.

---

## Bonus: Mixed Advanced Topics

### Exercise 23: Palindrome Partitioning IV (Hard)
Given a string s, return true if possible to partition into three non-empty palindromic substrings.

```
Example:
Input: s = "abcbdd"
Output: true
Explanation: "a" + "bcb" + "dd"
```

**Hint**: Precompute all palindromes using Manacher's or DP, then check partitions.

---

### Exercise 24: Minimum Window Subsequence (Hard)
Given strings s and t, find the minimum substring of s that contains all characters of t in order.

```
Example:
Input: s = "abcdebdde", t = "bde"
Output: "bcde"
```

**Hint**: Two-pointer approach with forward and backward passes.

---

### Exercise 25: K-th Smallest in Lexicographical Order (Hard)
Given integers n and k, return the kth lexicographically smallest integer in the range [1, n].

```
Example:
Input: n = 13, k = 2
Output: 10
Explanation: Lexicographic order: 1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9
```

**Hint**: Build prefix tree conceptually, count nodes in each subtree.

---

## Notes

- **Difficulty Distribution**: 8 medium, 17 hard
- **Time Estimates**:
  - Medium: 30-45 minutes each
  - Hard: 45-90 minutes each
- **Total Practice Time**: 20-30 hours

Focus on understanding patterns rather than memorizing solutions. Each problem teaches a specific technique applicable to similar problems.
