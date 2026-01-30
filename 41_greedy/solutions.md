# Chapter 41: Greedy Algorithms - Solutions

## Easy Problems

### E1: Assign Cookies
```python
def find_content_children(g, s):
    g.sort()
    s.sort()
    child = cookie = 0
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1
    return child
```
**Time**: O(n log n), **Space**: O(1)

### E2: Lemonade Change
```python
def lemonade_change(bills):
    five = ten = 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:  # bill == 20
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True
```
**Time**: O(n), **Space**: O(1)

### E3: Best Time to Buy and Sell Stock II
```python
def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit
```
**Time**: O(n), **Space**: O(1)

---

## Medium Problems

### M1: Jump Game
```python
def can_jump(nums):
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
    return True
```
**Time**: O(n), **Space**: O(1)

### M2: Jump Game II
```python
def jump(nums):
    jumps = current_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps
```
**Time**: O(n), **Space**: O(1)

### M4: Non-overlapping Intervals
```python
def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    last_end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= last_end:
            last_end = intervals[i][1]
        else:
            count += 1
    return count
```
**Time**: O(n log n), **Space**: O(1)

### M9: Remove K Digits
```python
def remove_k_digits(num, k):
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    if k > 0:
        stack = stack[:-k]
    result = ''.join(stack).lstrip('0')
    return result if result else '0'
```
**Time**: O(n), **Space**: O(n)

---

## Hard Problems

### H1: Candy
```python
def candy(ratings):
    n = len(ratings)
    candies = [1] * n

    # Left to right: if rating higher than left, give more candy
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    # Right to left: if rating higher than right, adjust
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    return sum(candies)
```
**Time**: O(n), **Space**: O(n)

### H4: Minimum Number of Arrows
```python
def find_min_arrow_shots(points):
    points.sort(key=lambda x: x[1])
    arrows = 1
    current_end = points[0][1]

    for start, end in points[1:]:
        if start > current_end:
            arrows += 1
            current_end = end

    return arrows
```
**Time**: O(n log n), **Space**: O(1)

---

Practice these patterns - greedy solutions are elegant when they work!
