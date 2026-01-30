# Chapter 41: Greedy Algorithms - Tips and Tricks

## Common Pitfalls

### 1. Not Verifying Greedy Works
Always verify with small examples or prove with exchange argument.

### 2. Wrong Sorting Criterion
```python
# ❌ WRONG: Sort by start time for interval scheduling
intervals.sort(key=lambda x: x[0])

# ✅ CORRECT: Sort by end time
intervals.sort(key=lambda x: x[1])
```

### 3. Forgetting Edge Cases
- Empty input
- Single element
- All same elements
- Already optimal

---

## Pattern Recognition

### Pattern 1: Interval Scheduling
**Indicator**: Non-overlapping intervals, maximum/minimum selection
**Approach**: Sort by end time

### Pattern 2: Two Pointers
**Indicator**: Pairing elements, allocation
**Approach**: Sort both arrays, use two pointers

### Pattern 3: Priority Queue
**Indicator**: Always process best available
**Approach**: Use heap

### Pattern 4: Stack
**Indicator**: Maintain increasing/decreasing order
**Approach**: Stack with greedy removal

---

## LeetCode Practice Problems (40+ problems)

### Interval Problems (10)
1. [Non-overlapping Intervals (435)](https://leetcode.com/problems/non-overlapping-intervals/)
2. [Meeting Rooms II (253)](https://leetcode.com/problems/meeting-rooms-ii/)
3. [Merge Intervals (56)](https://leetcode.com/problems/merge-intervals/)
4. [Insert Interval (57)](https://leetcode.com/problems/insert-interval/)
5. [Minimum Arrows (452)](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
6. [Interval List Intersections (986)](https://leetcode.com/problems/interval-list-intersections/)
7. [Car Pooling (1094)](https://leetcode.com/problems/car-pooling/)
8. [Video Stitching (1024)](https://leetcode.com/problems/video-stitching/)
9. [My Calendar I (729)](https://leetcode.com/problems/my-calendar-i/)
10. [Employee Free Time (759)](https://leetcode.com/problems/employee-free-time/)

### Jump/Reach Problems (6)
11. [Jump Game (55)](https://leetcode.com/problems/jump-game/)
12. [Jump Game II (45)](https://leetcode.com/problems/jump-game-ii/)
13. [Jump Game III (1306)](https://leetcode.com/problems/jump-game-iii/)
14. [Jump Game IV (1345)](https://leetcode.com/problems/jump-game-iv/)
15. [Minimum Jumps (1326)](https://leetcode.com/problems/jump-game-v/)
16. [Frog Jump (403)](https://leetcode.com/problems/frog-jump/)

### Scheduling/Task Problems (8)
17. [Task Scheduler (621)](https://leetcode.com/problems/task-scheduler/)
18. [Reorganize String (767)](https://leetcode.com/problems/reorganize-string/)
19. [Rearrange String k Distance (358)](https://leetcode.com/problems/rearrange-string-k-distance-apart/)
20. [Course Schedule III (630)](https://leetcode.com/problems/course-schedule-iii/)
21. [Single-Threaded CPU (1834)](https://leetcode.com/problems/single-threaded-cpu/)
22. [Furthest Building (1642)](https://leetcode.com/problems/furthest-building-you-can-reach/)
23. [Maximum Performance (1383)](https://leetcode.com/problems/maximum-performance-of-a-team/)
24. [Minimum Time (1834)](https://leetcode.com/problems/single-threaded-cpu/)

### Resource Allocation (7)
25. [Assign Cookies (455)](https://leetcode.com/problems/assign-cookies/)
26. [Boats to Save People (881)](https://leetcode.com/problems/boats-to-save-people/)
27. [Two City Scheduling (1029)](https://leetcode.com/problems/two-city-scheduling/)
28. [Minimum Cost to Hire K Workers (857)](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/)
29. [IPO (502)](https://leetcode.com/problems/ipo/)
30. [Maximum Units on Truck (1710)](https://leetcode.com/problems/maximum-units-on-a-truck/)
31. [Reduce Array Size (1338)](https://leetcode.com/problems/reduce-array-size-to-the-half/)

### String/Array Greedy (9)
32. [Partition Labels (763)](https://leetcode.com/problems/partition-labels/)
33. [Remove K Digits (402)](https://leetcode.com/problems/remove-k-digits/)
34. [Wiggle Subsequence (376)](https://leetcode.com/problems/wiggle-subsequence/)
35. [Queue Reconstruction (406)](https://leetcode.com/problems/queue-reconstruction-by-height/)
36. [Create Maximum Number (321)](https://leetcode.com/problems/create-maximum-number/)
37. [Maximum Swap (670)](https://leetcode.com/problems/maximum-swap/)
38. [Monotone Increasing Digits (738)](https://leetcode.com/problems/monotone-increasing-digits/)
39. [Split Array into Consecutive (659)](https://leetcode.com/problems/split-array-into-consecutive-subsequences/)
40. [Hand of Straights (846)](https://leetcode.com/problems/hand-of-straights/)

### Hard Greedy (5+)
41. [Candy (135)](https://leetcode.com/problems/candy/)
42. [Gas Station (134)](https://leetcode.com/problems/gas-station/)
43. [Best Time to Buy Sell Stock II (122)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
44. [Lemonade Change (860)](https://leetcode.com/problems/lemonade-change/)
45. [Advantage Shuffle (870)](https://leetcode.com/problems/advantage-shuffle/)

---

## Study Plan

**Week 1**: Intervals (problems 1-10)
**Week 2**: Jump/Reach (11-16) + Scheduling (17-24)
**Week 3**: Resource (25-31) + String/Array (32-40)
**Week 4**: Hard problems (41-45)

Master greedy by recognizing patterns!
