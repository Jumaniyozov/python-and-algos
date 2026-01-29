# Hash Tables: Practice Exercises

## Instructions

Solve these problems without looking at the solutions first. Each problem includes difficulty level, problem statement, constraints, and example test cases.

---

## Exercise 1: Two Sum (Easy)

**LeetCode #1**

**Problem:**
Given an array of integers `nums` and an integer `target`, return indices of the two numbers that add up to `target`.

**Constraints:**
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Exactly one solution exists

**Examples:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
```

---

## Exercise 2: Valid Anagram (Easy)

**LeetCode #242**

**Problem:**
Given two strings `s` and `t`, return true if `t` is an anagram of `s`, and false otherwise.

**Constraints:**
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters

**Examples:**
```
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
```

---

## Exercise 3: Contains Duplicate (Easy)

**LeetCode #217**

**Problem:**
Given an integer array `nums`, return true if any value appears at least twice, and return false if every element is distinct.

**Constraints:**
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

**Examples:**
```
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
```

---

## Exercise 4: Single Number (Easy)

**LeetCode #136**

**Problem:**
Given a non-empty array of integers where every element appears twice except for one, find that single one. You must implement a solution with O(1) extra space.

**Constraints:**
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element appears twice except for one

**Examples:**
```
Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4
```

---

## Exercise 5: Intersection of Two Arrays (Easy)

**LeetCode #349**

**Problem:**
Given two integer arrays, return an array of their intersection. Each element in the result must be unique.

**Constraints:**
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

**Examples:**
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4] or [4,9]
```

---

## Exercise 6: First Unique Character (Easy)

**LeetCode #387**

**Problem:**
Given a string `s`, find the first non-repeating character and return its index. If it doesn't exist, return -1.

**Constraints:**
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters

**Examples:**
```
Input: s = "leetcode"
Output: 0

Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1
```

---

## Exercise 7: Ransom Note (Easy)

**LeetCode #383**

**Problem:**
Given two strings `ransomNote` and `magazine`, return true if `ransomNote` can be constructed by using the letters from `magazine`, false otherwise.

**Constraints:**
- 1 <= ransomNote.length, magazine.length <= 10^5
- Both consist of lowercase English letters

**Examples:**
```
Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "ab"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
```

---

## Exercise 8: Group Anagrams (Medium)

**LeetCode #49**

**Problem:**
Given an array of strings, group the anagrams together.

**Constraints:**
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters

**Examples:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
```

---

## Exercise 9: Longest Substring Without Repeating Characters (Medium)

**LeetCode #3**

**Problem:**
Given a string `s`, find the length of the longest substring without repeating characters.

**Constraints:**
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces

**Examples:**
```
Input: s = "abcabcbb"
Output: 3 (substring "abc")

Input: s = "bbbbb"
Output: 1 (substring "b")

Input: s = "pwwkew"
Output: 3 (substring "wke")
```

---

## Exercise 10: Longest Consecutive Sequence (Medium)

**LeetCode #128**

**Problem:**
Given an unsorted array of integers, return the length of the longest consecutive elements sequence. Must run in O(n) time.

**Constraints:**
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

**Examples:**
```
Input: nums = [100,4,200,1,3,2]
Output: 4 (sequence [1,2,3,4])

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9 (sequence [0,1,2,3,4,5,6,7,8])
```

---

## Exercise 11: Top K Frequent Elements (Medium)

**LeetCode #347**

**Problem:**
Given an integer array and an integer k, return the k most frequent elements.

**Constraints:**
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, number of unique elements]
- Answer is guaranteed to be unique

**Examples:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
```

---

## Exercise 12: Subarray Sum Equals K (Medium)

**LeetCode #560**

**Problem:**
Given an array of integers and an integer k, return the total number of subarrays whose sum equals to k.

**Constraints:**
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

**Examples:**
```
Input: nums = [1,1,1], k = 2
Output: 2 (subarrays [1,1] at indices [0,1] and [1,2])

Input: nums = [1,2,3], k = 3
Output: 2 (subarrays [1,2] and [3])
```

---

## Exercise 13: 4Sum II (Medium)

**LeetCode #454**

**Problem:**
Given four integer arrays, return the number of tuples (i, j, k, l) such that nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0.

**Constraints:**
- n == nums1.length == nums2.length == nums3.length == nums4.length
- 1 <= n <= 200
- -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28

**Examples:**
```
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
```

---

## Exercise 14: Find All Anagrams in a String (Medium)

**LeetCode #438**

**Problem:**
Given two strings s and p, return an array of all the start indices of p's anagrams in s.

**Constraints:**
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters

**Examples:**
```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Input: s = "abab", p = "ab"
Output: [0,1,2]
```

---

## Exercise 15: Isomorphic Strings (Easy)

**LeetCode #205**

**Problem:**
Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if characters in s can be replaced to get t.

**Constraints:**
- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s and t consist of any valid ascii character

**Examples:**
```
Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true
```

---

## Exercise 16: Word Pattern (Easy)

**LeetCode #290**

**Problem:**
Given a pattern and a string s, find if s follows the same pattern.

**Constraints:**
- 1 <= pattern.length <= 300
- pattern contains only lowercase English letters
- 1 <= s.length <= 3000
- s contains only lowercase English letters and spaces

**Examples:**
```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```

---

## Exercise 17: Minimum Window Substring (Hard)

**LeetCode #76**

**Problem:**
Given two strings s and t, return the minimum window substring of s such that every character in t is included in the window. If there is no such substring, return the empty string "".

**Constraints:**
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters

**Examples:**
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Input: s = "a", t = "a"
Output: "a"

Input: s = "a", t = "aa"
Output: ""
```

---

## Exercise 18: Design HashMap (Easy)

**LeetCode #706**

**Problem:**
Design a HashMap without using any built-in hash table libraries.

Implement:
- `put(key, value)`: Insert or update
- `get(key)`: Return value or -1 if not found
- `remove(key)`: Remove key-value pair

**Constraints:**
- 0 <= key, value <= 10^6
- At most 10^4 calls to put, get, and remove

---

## Exercise 19: Design HashSet (Easy)

**LeetCode #705**

**Problem:**
Design a HashSet without using any built-in hash table libraries.

Implement:
- `add(key)`: Insert key
- `remove(key)`: Remove key
- `contains(key)`: Returns true if exists

**Constraints:**
- 0 <= key <= 10^6
- At most 10^4 calls to add, remove, and contains

---

## Exercise 20: LRU Cache (Medium)

**LeetCode #146**

**Problem:**
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement:
- `get(key)`: Return value of key or -1
- `put(key, value)`: Update or insert. If at capacity, evict LRU key.

Both operations must run in O(1) average time.

**Constraints:**
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls to get and put

**Example:**
```python
lru = LRUCache(2)  # capacity 2
lru.put(1, 1)
lru.put(2, 2)
lru.get(1)         # returns 1
lru.put(3, 3)      # evicts key 2
lru.get(2)         # returns -1 (not found)
lru.put(4, 4)      # evicts key 1
lru.get(1)         # returns -1 (not found)
lru.get(3)         # returns 3
lru.get(4)         # returns 4
```

---

## Difficulty Breakdown

**Easy (9 problems):**
1. Two Sum
2. Valid Anagram
3. Contains Duplicate
4. Single Number
5. Intersection of Two Arrays
6. First Unique Character
7. Ransom Note
15. Isomorphic Strings
16. Word Pattern
18. Design HashMap
19. Design HashSet

**Medium (9 problems):**
8. Group Anagrams
9. Longest Substring Without Repeating
10. Longest Consecutive Sequence
11. Top K Frequent Elements
12. Subarray Sum Equals K
13. 4Sum II
14. Find All Anagrams
20. LRU Cache

**Hard (1 problem):**
17. Minimum Window Substring

---

## Tips for Solving

1. **Identify Pattern:**
   - Need to find pair/sum → Hash table
   - Frequency counting → Counter or defaultdict
   - Grouping by property → Hash table
   - Sliding window + lookup → Hash table + two pointers

2. **Hash Table Choice:**
   - Simple lookup: `dict` or `set`
   - Frequency counting: `Counter`
   - Auto-initialize: `defaultdict`
   - Order matters: `OrderedDict`

3. **Common Techniques:**
   - Complement pattern: `target - current`
   - Prefix sum: Track cumulative sums
   - Sliding window: Fixed or variable size
   - Two hash tables: Bidirectional mapping

4. **Edge Cases:**
   - Empty input
   - Single element
   - All duplicates
   - No solution
   - Multiple solutions

Good luck!
