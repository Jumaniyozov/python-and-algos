# Problem-Solving Patterns - Tips and Practice Resources

## Pattern Recognition Guide

### Quick Identification Checklist

```
✓ Sorted array/list → Two Pointers or Binary Search
✓ Contiguous subarray/substring → Sliding Window
✓ Linked list with cycle/middle → Fast/Slow Pointers
✓ Overlapping intervals → Merge Intervals
✓ Array with numbers 1 to n → Cyclic Sort
✓ Tree level by level → BFS
✓ Tree root to leaf paths → DFS
✓ Find median or middle values → Two Heaps
✓ All combinations/permutations → Subsets/Backtracking
✓ K largest/smallest/frequent → Top K Elements
✓ Merge K sorted lists → K-way Merge
✓ Next greater/smaller element → Monotonic Stack
✓ Optimization problem → Dynamic Programming
```

### Common Mistakes to Avoid

1. **Two Pointers**
   - Forgetting to handle equal elements
   - Not considering edge cases (empty array, single element)
   - Moving both pointers when only one should move

2. **Sliding Window**
   - Not contracting window properly
   - Forgetting to update result after window adjustment
   - Incorrect window size calculation

3. **Tree Traversal**
   - Not handling null nodes
   - Incorrect recursion termination
   - Forgetting to process current node

4. **Dynamic Programming**
   - Not identifying base cases correctly
   - Incorrect state transition
   - Missing memoization opportunities

## Comprehensive Practice Resources

### Two Pointers Pattern (120+ problems)

**Easy (40 problems)**
1. Valid Palindrome - https://leetcode.com/problems/valid-palindrome/
2. Move Zeroes - https://leetcode.com/problems/move-zeroes/
3. Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/
4. Remove Element - https://leetcode.com/problems/remove-element/
5. Squares of a Sorted Array - https://leetcode.com/problems/squares-of-a-sorted-array/
6. Reverse String - https://leetcode.com/problems/reverse-string/
7. Two Sum II - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
8. Merge Sorted Array - https://leetcode.com/problems/merge-sorted-array/
9. Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/
10. Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

**Medium (60 problems)**
11. 3Sum - https://leetcode.com/problems/3sum/
12. 4Sum - https://leetcode.com/problems/4sum/
13. 3Sum Closest - https://leetcode.com/problems/3sum-closest/
14. Container With Most Water - https://leetcode.com/problems/container-with-most-water/
15. Sort Colors - https://leetcode.com/problems/sort-colors/
16. Partition Labels - https://leetcode.com/problems/partition-labels/
17. Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/
18. Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/
19. Number of Subsequences That Satisfy Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
20. Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

**Hard (20 problems)**
21. Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/
22. Minimum Window Subsequence - https://leetcode.com/problems/minimum-window-subsequence/
23. Substring with Concatenation of All Words - https://leetcode.com/problems/substring-with-concatenation-of-all-words/
24. Longest Duplicate Substring - https://leetcode.com/problems/longest-duplicate-substring/
25. Count of Range Sum - https://leetcode.com/problems/count-of-range-sum/

### Sliding Window Pattern (80+ problems)

**Easy (25 problems)**
26. Maximum Average Subarray I - https://leetcode.com/problems/maximum-average-subarray-i/
27. Minimum Value to Get Positive Step by Step Sum - https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
28. Maximum Number of Vowels in Substring - https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
29. Defanging an IP Address - https://leetcode.com/problems/defanging-an-ip-address/
30. Contains Duplicate II - https://leetcode.com/problems/contains-duplicate-ii/

**Medium (45 problems)**
31. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/
32. Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/
33. Permutation in String - https://leetcode.com/problems/permutation-in-string/
34. Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/
35. Longest Substring with At Least K Repeating Characters - https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
36. Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/
37. Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets/
38. Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/
39. Grumpy Bookstore Owner - https://leetcode.com/problems/grumpy-bookstore-owner/
40. Minimum Swaps to Group All 1s Together - https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

**Hard (10 problems)**
41. Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/
42. Sliding Window Maximum - https://leetcode.com/problems/sliding-window-maximum/
43. Longest Substring with At Most K Distinct Characters - https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
44. Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/
45. Minimum Number of K Consecutive Bit Flips - https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

### Fast and Slow Pointers (35+ problems)

**Easy (10 problems)**
46. Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/
47. Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/
48. Happy Number - https://leetcode.com/problems/happy-number/
49. Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/
50. Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

**Medium (20 problems)**
51. Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/
52. Reorder List - https://leetcode.com/problems/reorder-list/
53. Add Two Numbers - https://leetcode.com/problems/add-two-numbers/
54. Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/
55. Sort List - https://leetcode.com/problems/sort-list/
56. Rotate List - https://leetcode.com/problems/rotate-list/
57. Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/
58. Partition List - https://leetcode.com/problems/partition-list/
59. Intersection of Two Linked Lists - https://leetcode.com/problems/intersection-of-two-linked-lists/
60. Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

**Hard (5 problems)**
61. Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/
62. Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/
63. LRU Cache - https://leetcode.com/problems/lru-cache/

### Merge Intervals (40+ problems)

**Easy (10 problems)**
64. Meeting Rooms - https://leetcode.com/problems/meeting-rooms/
65. Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
66. Can Attend Meetings - https://leetcode.com/problems/meeting-rooms/

**Medium (25 problems)**
67. Merge Intervals - https://leetcode.com/problems/merge-intervals/
68. Insert Interval - https://leetcode.com/problems/insert-interval/
69. Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/
70. Meeting Rooms II - https://leetcode.com/problems/meeting-rooms-ii/
71. Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/
72. My Calendar I - https://leetcode.com/problems/my-calendar-i/
73. My Calendar II - https://leetcode.com/problems/my-calendar-ii/
74. My Calendar III - https://leetcode.com/problems/my-calendar-iii/
75. Car Pooling - https://leetcode.com/problems/car-pooling/
76. Remove Covered Intervals - https://leetcode.com/problems/remove-covered-intervals/

**Hard (5 problems)**
77. Employee Free Time - https://leetcode.com/problems/employee-free-time/
78. Data Stream as Disjoint Intervals - https://leetcode.com/problems/data-stream-as-disjoint-intervals/

### Tree BFS (50+ problems)

**Easy (20 problems)**
79. Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/
80. Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/
81. Minimum Depth of Binary Tree - https://leetcode.com/problems/minimum-depth-of-binary-tree/
82. Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/
83. Symmetric Tree - https://leetcode.com/problems/symmetric-tree/
84. Same Tree - https://leetcode.com/problems/same-tree/
85. Invert Binary Tree - https://leetcode.com/problems/invert-binary-tree/
86. Cousins in Binary Tree - https://leetcode.com/problems/cousins-in-binary-tree/
87. N-ary Tree Level Order Traversal - https://leetcode.com/problems/n-ary-tree-level-order-traversal/
88. Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

**Medium (25 problems)**
89. Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
90. Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/
91. Populating Next Right Pointers - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
92. All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
93. Find Bottom Left Tree Value - https://leetcode.com/problems/find-bottom-left-tree-value/
94. Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/
95. Add One Row to Tree - https://leetcode.com/problems/add-one-row-to-tree/

**Hard (5 problems)**
96. Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/
97. Serialize and Deserialize Binary Tree - https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

### Top K Elements (40+ problems)

**Easy (10 problems)**
98. Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/
99. Last Stone Weight - https://leetcode.com/problems/last-stone-weight/
100. Third Maximum Number - https://leetcode.com/problems/third-maximum-number/

**Medium (25 problems)**
101. Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/
102. Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/
103. K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/
104. Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/
105. Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/
106. Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
107. Reorganize String - https://leetcode.com/problems/reorganize-string/
108. Task Scheduler - https://leetcode.com/problems/task-scheduler/
109. Least Number of Unique Integers after K Removals - https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
110. Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/

**Hard (5 problems)**
111. Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/
112. IPO - https://leetcode.com/problems/ipo/

### Dynamic Programming (150+ problems)

**Easy (30 problems)**
113. Climbing Stairs - https://leetcode.com/problems/climbing-stairs/
114. House Robber - https://leetcode.com/problems/house-robber/
115. Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
116. Maximum Subarray - https://leetcode.com/problems/maximum-subarray/
117. Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/
118. Is Subsequence - https://leetcode.com/problems/is-subsequence/
119. Divisor Game - https://leetcode.com/problems/divisor-game/
120. Fibonacci Number - https://leetcode.com/problems/fibonacci-number/
121. N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/
122. Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/

**Medium (80 problems)**
123. Coin Change - https://leetcode.com/problems/coin-change/
124. Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/
125. Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/
126. Unique Paths - https://leetcode.com/problems/unique-paths/
127. Unique Paths II - https://leetcode.com/problems/unique-paths-ii/
128. Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/
129. Word Break - https://leetcode.com/problems/word-break/
130. Decode Ways - https://leetcode.com/problems/decode-ways/
131. Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/
132. House Robber II - https://leetcode.com/problems/house-robber-ii/
133. Jump Game - https://leetcode.com/problems/jump-game/
134. Jump Game II - https://leetcode.com/problems/jump-game-ii/
135. Target Sum - https://leetcode.com/problems/target-sum/
136. Perfect Squares - https://leetcode.com/problems/perfect-squares/
137. Maximal Square - https://leetcode.com/problems/maximal-square/
138. Count Square Submatrices - https://leetcode.com/problems/count-square-submatrices-with-all-ones/
139. Triangle - https://leetcode.com/problems/triangle/
140. Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/

**Hard (40 problems)**
141. Edit Distance - https://leetcode.com/problems/edit-distance/
142. Regular Expression Matching - https://leetcode.com/problems/regular-expression-matching/
143. Wildcard Matching - https://leetcode.com/problems/wildcard-matching/
144. Longest Valid Parentheses - https://leetcode.com/problems/longest-valid-parentheses/
145. Maximal Rectangle - https://leetcode.com/problems/maximal-rectangle/
146. Interleaving String - https://leetcode.com/problems/interleaving-string/
147. Distinct Subsequences - https://leetcode.com/problems/distinct-subsequences/
148. Word Break II - https://leetcode.com/problems/word-break-ii/
149. Burst Balloons - https://leetcode.com/problems/burst-balloons/
150. Best Time to Buy and Sell Stock IV - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

## Study Schedule

### Week 1-2: Foundation Patterns
- Two Pointers: 20 problems
- Sliding Window: 15 problems
- Fast/Slow Pointers: 10 problems

### Week 3-4: Intermediate Patterns
- Merge Intervals: 10 problems
- Cyclic Sort: 8 problems
- Tree BFS: 15 problems
- Tree DFS: 15 problems

### Week 5-6: Advanced Patterns
- Two Heaps: 8 problems
- Top K Elements: 12 problems
- Modified Binary Search: 12 problems
- K-way Merge: 8 problems

### Week 7-8: Expert Patterns
- Monotonic Stack: 10 problems
- Subsets/Backtracking: 15 problems
- Dynamic Programming: 30 problems

## Pattern Mastery Checklist

✓ Can identify pattern in under 1 minute
✓ Can write template code from memory
✓ Can explain time/space complexity
✓ Can solve Easy problems in 10-15 minutes
✓ Can solve Medium problems in 20-30 minutes
✓ Can modify pattern for variations
✓ Can combine multiple patterns when needed

