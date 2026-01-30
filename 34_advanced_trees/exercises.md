# Chapter 34: Advanced Trees - Exercises

## Table of Contents
1. [Easy Problems (8)](#easy-problems)
2. [Medium Problems (12)](#medium-problems)
3. [Hard Problems (5)](#hard-problems)

---

## Easy Problems

### 1. Implement Trie (Prefix Tree)
**Difficulty:** Easy
**Topics:** Trie, Design
**LeetCode:** 208

**Description:**
Implement a trie with `insert`, `search`, and `startsWith` methods.

**Example:**
```
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
```

**Hints:**
- Use dictionary/hashmap for children nodes
- Mark end of word with boolean flag
- For startsWith, don't need to check is_end_of_word

---

### 2. Longest Common Prefix
**Difficulty:** Easy
**Topics:** String, Trie
**LeetCode:** 14

**Description:**
Find the longest common prefix string amongst an array of strings.

**Example:**
```
Input: ["flower","flow","flight"]
Output: "fl"
```

**Hints:**
- Can solve with trie or without
- Insert all words and find common path
- Alternative: horizontal scanning or vertical scanning

---

### 3. Range Sum Query - Immutable
**Difficulty:** Easy
**Topics:** Array, Prefix Sum
**LeetCode:** 303

**Description:**
Given an integer array, find the sum of elements between indices i and j (i ≤ j), inclusive.

**Example:**
```
Input: nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

**Hints:**
- Build prefix sum array in constructor
- sum(i, j) = prefix[j+1] - prefix[i]
- Can also use Fenwick tree (overkill for immutable)

---

### 4. Range Sum Query - Mutable
**Difficulty:** Medium (listed as Easy for learning)
**Topics:** Array, Segment Tree, Fenwick Tree
**LeetCode:** 307

**Description:**
Given an integer array nums, find the sum of elements between indices i and j inclusive, and support updating values.

**Example:**
```
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 9
numArray.update(1, 2);
numArray.sumRange(0, 2); // return 8
```

**Hints:**
- Segment tree or Fenwick tree required
- O(log n) for both operations
- Prefix sum won't work (updates would be O(n))

---

### 5. Count Nodes Equal to Average of Subtree
**Difficulty:** Medium (Easy for advanced trees)
**Topics:** Tree, DFS
**LeetCode:** 2265

**Description:**
Given root of binary tree, return number of nodes where the value equals the average of values in its subtree.

**Example:**
```
Input: root = [4,8,5,0,1,null,6]
Output: 5
```

**Hints:**
- DFS to calculate sum and count for each subtree
- Return (sum, count, result_count) from each node
- Check if node.val == sum // count

---

### 6. Shortest Word Distance II
**Difficulty:** Medium (Easy with understanding)
**Topics:** Hash Table, Design
**Related to:** Trie applications

**Description:**
Design a class to find shortest distance between two words in a word list. The class will be called repeatedly.

**Example:**
```
WordDistance wd = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wd.shortest("coding", "practice"); // return 3
wd.shortest("makes", "coding");    // return 1
```

**Hints:**
- Store indices of each word in hash table
- Two pointers on two sorted lists
- O(m + n) where m, n are occurrence counts

---

### 7. Design Add and Search Words Data Structure
**Difficulty:** Medium
**Topics:** Trie, DFS, Design
**LeetCode:** 211

**Description:**
Design a data structure that supports adding new words and finding if a string matches any previously added string where '.' can match any letter.

**Example:**
```
WordDictionary wd = new WordDictionary();
wd.addWord("bad");
wd.addWord("dad");
wd.addWord("mad");
wd.search("pad"); // false
wd.search("bad"); // true
wd.search(".ad"); // true
wd.search("b.."); // true
```

**Hints:**
- Use trie structure
- For '.', recursively try all children
- DFS when encountering wildcard

---

### 8. Map Sum Pairs
**Difficulty:** Medium
**Topics:** Trie, Hash Table, Design
**LeetCode:** 677

**Description:**
Implement MapSum class with insert(key, val) and sum(prefix) methods. sum returns sum of all pairs' values whose key starts with prefix.

**Example:**
```
MapSum ms = new MapSum();
ms.insert("apple", 3);
ms.sum("ap");           // return 3
ms.insert("app", 2);
ms.sum("ap");           // return 5
```

**Hints:**
- Trie with value at each node
- Store cumulative sum at each prefix
- Handle updates (need to track previous values)

---

## Medium Problems

### 9. Replace Words
**Difficulty:** Medium
**Topics:** Trie, Hash Table, String
**LeetCode:** 648

**Description:**
Given dictionary of roots and a sentence, replace all successors in sentence with root forming it.

**Example:**
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

**Hints:**
- Build trie from dictionary
- For each word in sentence, find shortest matching root
- Stop at first complete word in trie

---

### 10. Implement Trie II (Prefix Tree)
**Difficulty:** Medium
**Topics:** Trie, Design
**LeetCode:** 1804

**Description:**
Implement Trie with insert, countWordsEqualTo, countWordsStartingWith, and erase methods.

**Example:**
```
Trie trie = new Trie();
trie.insert("apple");
trie.insert("apple");
trie.countWordsEqualTo("apple");    // return 2
trie.countWordsStartingWith("app"); // return 2
trie.erase("apple");
trie.countWordsEqualTo("apple");    // return 1
```

**Hints:**
- Store count at each node (not just boolean)
- Track prefix count separately from end count
- Erase decrements counts

---

### 11. Word Search II
**Difficulty:** Hard (Medium with Trie)
**Topics:** Trie, Backtracking, Matrix
**LeetCode:** 212

**Description:**
Given m x n board and list of words, return all words on the board.

**Example:**
```
Input: board = [["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]],
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

**Hints:**
- Build trie from words first
- DFS from each cell with trie navigation
- Prune trie nodes after finding words
- Much faster than checking each word individually

---

### 12. Range Sum Query 2D - Immutable
**Difficulty:** Medium
**Topics:** Array, Matrix, Prefix Sum
**LeetCode:** 304

**Description:**
Given 2D matrix, calculate sum of elements inside rectangle defined by its upper left and lower right corners.

**Example:**
```
Input: matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
sumRegion(2, 1, 4, 3) -> 8
```

**Hints:**
- 2D prefix sum array
- prefix[i][j] = sum from (0,0) to (i-1,j-1)
- Use inclusion-exclusion principle

---

### 13. Range Sum Query 2D - Mutable
**Difficulty:** Hard
**Topics:** Array, Matrix, Segment Tree, Fenwick Tree
**LeetCode:** 308

**Description:**
Given 2D matrix, support update and sumRegion queries.

**Example:**
```
NumMatrix nm = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1]]);
nm.sumRegion(2, 1, 4, 3);
nm.update(3, 2, 2);
nm.sumRegion(2, 1, 4, 3);
```

**Hints:**
- 2D Fenwick tree or 2D segment tree
- O(log m * log n) operations
- Each dimension uses BIT operations

---

### 14. Count of Smaller Numbers After Self
**Difficulty:** Hard (Medium with Fenwick/Segment)
**Topics:** Array, Fenwick Tree, Segment Tree
**LeetCode:** 315

**Description:**
For each element in array, count how many smaller elements are to its right.

**Example:**
```
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
```

**Hints:**
- Process from right to left
- Use Fenwick tree with coordinate compression
- Query count of numbers < current, then insert current

---

### 15. Count of Range Sum
**Difficulty:** Hard
**Topics:** Array, Fenwick Tree, Segment Tree
**LeetCode:** 327

**Description:**
Given integer array, count number of range sums that lie in [lower, upper] inclusive.

**Example:**
```
Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: [0,0], [2,2], [0,2]
```

**Hints:**
- Calculate prefix sums
- For each prefix, count previous prefixes in valid range
- Use Fenwick tree or merge sort

---

### 16. My Calendar I, II, III
**Difficulty:** Medium-Hard
**Topics:** Segment Tree, Design
**LeetCode:** 729, 731, 732

**Description:**
Implement calendar that can book events. Calendar I: no overlaps. Calendar II: at most 1 overlap. Calendar III: return max k-booking.

**Example:**
```
MyCalendar cal = new MyCalendar();
cal.book(10, 20); // true
cal.book(15, 25); // false (overlap)
cal.book(20, 30); // true
```

**Hints:**
- Segment tree with lazy propagation
- Track number of bookings at each point
- Can also use TreeMap/sorted map

---

### 17. Longest Word in Dictionary
**Difficulty:** Medium
**Topics:** Trie, DFS, Hash Table
**LeetCode:** 720

**Description:**
Given list of strings, find longest word that can be built one character at a time by other words.

**Example:**
```
Input: words = ["w","wo","wor","worl","world"]
Output: "world"
```

**Hints:**
- Build trie, marking each complete word
- DFS to find longest buildable word
- Every prefix must exist as complete word

---

### 18. Palindrome Pairs
**Difficulty:** Hard
**Topics:** Trie, String, Hash Table
**LeetCode:** 336

**Description:**
Given list of unique words, find all pairs of distinct indices (i, j) such that concatenation of words[i] + words[j] is a palindrome.

**Example:**
```
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
```

**Hints:**
- Build trie of reversed words
- For each word, search for complementary palindromes
- Check if remaining part is palindrome

---

### 19. Search Suggestions System
**Difficulty:** Medium
**Topics:** Trie, String, Sorting
**LeetCode:** 1268

**Description:**
Given array of products and searchWord, return list of at most 3 product names suggested after each character of searchWord.

**Example:**
```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
```

**Hints:**
- Build trie and sort products at each node
- For each prefix, return top 3 lexicographically
- Can also use binary search

---

### 20. Maximum XOR of Two Numbers in Array
**Difficulty:** Medium
**Topics:** Trie, Bit Manipulation
**LeetCode:** 421

**Description:**
Given array of integers, find maximum XOR of two numbers.

**Example:**
```
Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: 5 XOR 25 = 28
```

**Hints:**
- Build binary trie (0/1 children)
- For each number, greedily find opposite bits
- O(32n) time complexity

---

## Hard Problems

### 21. Maximum XOR Queries
**Difficulty:** Hard
**Topics:** Trie, Bit Manipulation, Array
**LeetCode:** 1707

**Description:**
Given array nums and queries [xi, mi], find maximum XOR of xi with any element from nums not exceeding mi.

**Example:**
```
Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
Output: [3,3,7]
```

**Hints:**
- Build trie with max value at each node
- Sort queries by mi descending
- Insert numbers <= mi before processing

---

### 22. Count Different Palindromic Subsequences
**Difficulty:** Hard
**Topics:** String, DP, Trie
**LeetCode:** 730

**Description:**
Given string, return number of different non-empty palindromic subsequences modulo 10^9+7.

**Example:**
```
Input: s = "bccb"
Output: 6
Explanation: "b", "c", "bb", "cc", "bcb", "bccb"
```

**Hints:**
- DP with trie for tracking unique subsequences
- dp[i][j] = count in substring s[i:j+1]
- Handle duplicates carefully

---

### 23. Stream of Characters
**Difficulty:** Hard
**Topics:** Trie, Design, Data Stream
**LeetCode:** 1032

**Description:**
Implement StreamChecker class that checks if suffix of characters queried so far matches any string in given word list.

**Example:**
```
StreamChecker sc = new StreamChecker(["cd","f","kl"]);
sc.query('a'); // false
sc.query('b'); // false
sc.query('c'); // false
sc.query('d'); // true (matches "cd")
```

**Hints:**
- Build trie of reversed words
- Store recent characters
- Search from end of stream

---

### 24. The Skyline Problem
**Difficulty:** Hard
**Topics:** Segment Tree, Line Sweep, Heap
**LeetCode:** 218

**Description:**
Given array of buildings [left, right, height], return skyline formed by these buildings.

**Example:**
```
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
```

**Hints:**
- Line sweep with segment tree or multiset
- Track maximum height at each x-coordinate
- Process start and end events

---

### 25. Falling Squares
**Difficulty:** Hard
**Topics:** Segment Tree, Coordinate Compression
**LeetCode:** 699

**Description:**
Squares are dropped onto 2D plane. Return list of heights after each square is dropped.

**Example:**
```
Input: positions = [[1,2],[2,3],[6,1]]
Output: [2,5,5]
```

**Hints:**
- Segment tree with lazy propagation
- Coordinate compression for large coordinates
- Track maximum height in each range

---

## Complexity Analysis

| Problem | Expected Time | Expected Space | Key Data Structure |
|---------|---------------|----------------|-------------------|
| Trie Implementation | O(m) per op | O(ALPHABET * m * n) | Trie |
| Range Sum Query | O(1) query | O(n) | Prefix Sum |
| Range Sum Mutable | O(log n) | O(n) | Fenwick/Segment |
| Word Search II | O(m * n * 4^L) | O(total chars) | Trie + DFS |
| Count Smaller After | O(n log n) | O(n) | Fenwick Tree |
| Maximum XOR | O(32n) | O(32n) | Binary Trie |
| Skyline Problem | O(n log n) | O(n) | Segment Tree/Heap |

---

## Practice Strategy

**Week 1:** Master Trie
- Problems 1, 2, 7, 8, 9, 10

**Week 2:** Trie Applications
- Problems 11, 17, 18, 19, 20

**Week 3:** Segment/Fenwick Trees
- Problems 3, 4, 12, 13, 14

**Week 4:** Advanced Problems
- Problems 15, 16, 21, 22, 23

**Week 5:** Expert Level
- Problems 24, 25

Focus on understanding the patterns rather than memorizing solutions.
