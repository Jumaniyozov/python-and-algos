# Stacks and Queues: Practice Exercises

## Instructions

Solve these problems without looking at the solutions first. Each problem includes:
- Difficulty level
- Problem statement
- Input/output format
- Constraints
- Example test cases

After attempting each problem, check your solution against `solutions.md`.

---

## Exercise 1: Implement Stack with Max (Easy)

**Problem:**
Design a stack that supports push, pop, top, and retrieving the maximum element in constant time.

Implement the `MaxStack` class:
- `MaxStack()` initializes the stack
- `void push(int val)` pushes val onto the stack
- `int pop()` removes the top element and returns it
- `int top()` gets the top element
- `int getMax()` retrieves the maximum element in the stack

**Constraints:**
- -10^9 <= val <= 10^9
- At most 10^4 calls to each function
- pop, top, and getMax will be called only on non-empty stacks

**Example:**
```python
stack = MaxStack()
stack.push(5)
stack.push(1)
stack.push(5)
print(stack.getMax())  # Output: 5
print(stack.pop())     # Output: 5
print(stack.getMax())  # Output: 5
```

---

## Exercise 2: Valid Parentheses (Easy)

**LeetCode #20**

**Problem:**
Given a string `s` containing just the characters `'(', ')', '{', '}', '[', ']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order
3. Every close bracket has a corresponding open bracket of the same type

**Constraints:**
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'

**Examples:**
```
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
```

---

## Exercise 3: Next Greater Element I (Easy)

**LeetCode #496**

**Problem:**
The next greater element of some element `x` in an array is the first greater element that is to the right of `x` in the same array.

You are given two distinct 0-indexed integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the next greater element of `nums2[j]` in `nums2`. If there is no next greater element, the answer is -1.

Return an array `ans` of length `nums1.length` such that `ans[i]` is the next greater element as described above.

**Constraints:**
- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10^4
- All integers in nums1 and nums2 are unique
- All elements of nums1 also appear in nums2

**Examples:**
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

---

## Exercise 4: Backspace String Compare (Easy)

**LeetCode #844**

**Problem:**
Given two strings `s` and `t`, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

**Constraints:**
- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters

**Examples:**
```
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both become "ac"

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both become ""

Input: s = "a#c", t = "b"
Output: false
```

---

## Exercise 5: Remove All Adjacent Duplicates In String (Easy)

**LeetCode #1047**

**Problem:**
You are given a string `s` consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

Repeatedly remove duplicates until no more removals possible.

**Constraints:**
- 1 <= s.length <= 10^5
- s consists of lowercase English letters

**Examples:**
```
Input: s = "abbaca"
Output: "ca"
Explanation: "bb" removed -> "aaca", then "aa" removed -> "ca"

Input: s = "azxxzy"
Output: "ay"
```

---

## Exercise 6: Baseball Game (Easy)

**LeetCode #682**

**Problem:**
You are keeping score for a baseball game with special rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

Operations:
- An integer `x`: Record a new score of `x`
- `"+"`: Record a new score that is the sum of the previous two scores
- `"D"`: Record a new score that is double the previous score
- `"C"`: Invalidate the previous score, removing it from the record

Return the sum of all scores after all operations.

**Constraints:**
- 1 <= operations.length <= 1000
- operations[i] is "C", "D", "+", or a string representing an integer

**Examples:**
```
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5, record is [5]
"2" - Add 2, record is [5, 2]
"C" - Invalidate 2, record is [5]
"D" - Add 10 (2 * 5), record is [5, 10]
"+" - Add 15 (5 + 10), record is [5, 10, 15]
Total: 30

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
```

---

## Exercise 7: Min Stack (Easy)

**LeetCode #155**

**Problem:**
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack
- `void push(int val)` pushes val onto the stack
- `void pop()` removes the top element
- `int top()` gets the top element
- `int getMin()` retrieves the minimum element

**Constraints:**
- -2^31 <= val <= 2^31 - 1
- pop, top and getMin operations will always be called on non-empty stacks
- At most 3 * 10^4 calls

**Example:**
```python
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # -3
minStack.pop()
print(minStack.top())     # 0
print(minStack.getMin())  # -2
```

---

## Exercise 8: Daily Temperatures (Medium)

**LeetCode #739**

**Problem:**
Given an array of integers `temperatures` representing daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i-th` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Constraints:**
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

**Examples:**
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]
```

---

## Exercise 9: Evaluate Reverse Polish Notation (Medium)

**LeetCode #150**

**Problem:**
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Division between two integers should truncate toward zero.

**Constraints:**
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator or an integer

**Examples:**
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
```

---

## Exercise 10: Decode String (Medium)

**LeetCode #394**

**Problem:**
Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times.

**Constraints:**
- 1 <= s.length <= 30
- s consists of lowercase English letters, digits, and square brackets '[]'
- s is guaranteed to be a valid input
- All the integers in s are in the range [1, 300]

**Examples:**
```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

---

## Exercise 11: Asteroid Collision (Medium)

**LeetCode #735**

**Problem:**
We are given an array `asteroids` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive = right, negative = left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

**Constraints:**
- 2 <= asteroids.length <= 10^4
- -1000 <= asteroids[i] <= 1000
- asteroids[i] != 0

**Examples:**
```
Input: asteroids = [5,10,-5]
Output: [5,10]

Input: asteroids = [8,-8]
Output: []

Input: asteroids = [10,2,-5]
Output: [10]

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
```

---

## Exercise 12: Remove K Digits (Medium)

**LeetCode #402**

**Problem:**
Given string `num` representing a non-negative integer, and an integer `k`, return the smallest possible integer after removing `k` digits from the number.

**Constraints:**
- 1 <= k <= num.length <= 10^5
- num consists of only digits
- num does not have any leading zeros except for the zero itself

**Examples:**
```
Input: num = "1432219", k = 3
Output: "1219"

Input: num = "10200", k = 1
Output: "200"

Input: num = "10", k = 2
Output: "0"
```

---

## Exercise 13: Simplify Path (Medium)

**LeetCode #71**

**Problem:**
Given a string `path`, which is an absolute path (starting with '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

Rules:
- "." refers to current directory
- ".." refers to parent directory
- Multiple consecutive slashes are treated as single slash
- The result should not end with '/' unless it's the root directory

**Constraints:**
- 1 <= path.length <= 3000
- path consists of English letters, digits, period '.', slash '/', or '_'
- path is a valid absolute Unix path

**Examples:**
```
Input: path = "/home/"
Output: "/home"

Input: path = "/../"
Output: "/"

Input: path = "/home//foo/"
Output: "/home/foo"

Input: path = "/a/./b/../../c/"
Output: "/c"
```

---

## Exercise 14: Implement Queue using Stacks (Easy)

**LeetCode #232**

**Problem:**
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

**Constraints:**
- 1 <= x <= 9
- At most 100 calls to push, pop, peek, and empty

**Example:**
```python
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())  # 1
print(q.pop())   # 1
print(q.empty()) # False
```

---

## Exercise 15: Implement Stack using Queues (Easy)

**LeetCode #225**

**Problem:**
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

**Constraints:**
- 1 <= x <= 9
- At most 100 calls to push, pop, top, and empty

**Example:**
```python
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())   # 2
print(stack.pop())   # 2
print(stack.empty()) # False
```

---

## Exercise 16: Online Stock Span (Medium)

**LeetCode #901**

**Problem:**
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

**Constraints:**
- 1 <= price <= 10^5
- At most 10^4 calls to next

**Example:**
```python
stockSpanner = StockSpanner()
print(stockSpanner.next(100))  # 1
print(stockSpanner.next(80))   # 1
print(stockSpanner.next(60))   # 1
print(stockSpanner.next(70))   # 2
print(stockSpanner.next(60))   # 1
print(stockSpanner.next(75))   # 4
print(stockSpanner.next(85))   # 6
```

---

## Exercise 17: Sliding Window Maximum (Hard)

**LeetCode #239**

**Problem:**
You are given an array of integers `nums`, and there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

**Constraints:**
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length

**Examples:**
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Input: nums = [1], k = 1
Output: [1]
```

---

## Exercise 18: Largest Rectangle in Histogram (Hard)

**LeetCode #84**

**Problem:**
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

**Constraints:**
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4

**Examples:**
```
Input: heights = [2,1,5,6,2,3]
Output: 10

Input: heights = [2,4]
Output: 4
```

---

## Exercise 19: Trapping Rain Water (Hard)

**LeetCode #42**

**Problem:**
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Constraints:**
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

**Examples:**
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input: height = [4,2,0,3,2,5]
Output: 9
```

---

## Exercise 20: Basic Calculator (Hard)

**LeetCode #224**

**Problem:**
Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

The expression may contain:
- Non-negative integers
- '+', '-' operators
- '(', ')' parentheses
- Spaces ' '

**Constraints:**
- 1 <= s.length <= 3 * 10^5
- s consists of digits, '+', '-', '(', ')', and ' '
- s represents a valid expression
- '+' is not used as a unary operation
- '-' could be used as a unary operation
- There will be no two consecutive operators

**Examples:**
```
Input: s = "1 + 1"
Output: 2

Input: s = " 2-1 + 2 "
Output: 3

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

---

## Difficulty Breakdown

**Easy (7 problems):**
1. Implement Stack with Max
2. Valid Parentheses
3. Next Greater Element I
4. Backspace String Compare
5. Remove All Adjacent Duplicates
6. Baseball Game
7. Min Stack
8. Implement Queue using Stacks
9. Implement Stack using Queues

**Medium (8 problems):**
10. Daily Temperatures
11. Evaluate Reverse Polish Notation
12. Decode String
13. Asteroid Collision
14. Remove K Digits
15. Simplify Path
16. Online Stock Span

**Hard (3 problems):**
17. Sliding Window Maximum
18. Largest Rectangle in Histogram
19. Trapping Rain Water
20. Basic Calculator

---

## Tips for Solving

1. **Identify the Pattern:**
   - Matching/nesting → Stack
   - First-come first-served → Queue
   - Next greater/smaller → Monotonic stack
   - Sliding window max/min → Monotonic deque

2. **Stack Problems:**
   - Use for reversing order
   - Maintain invariant (monotonic)
   - Track history or state

3. **Queue Problems:**
   - Process in arrival order
   - BFS-style level processing
   - Sliding window with deque

4. **Design Problems:**
   - Consider trade-offs
   - Use auxiliary data structures
   - Amortized analysis

5. **Common Pitfalls:**
   - Forgetting to check if stack/queue is empty
   - Not handling edge cases (empty input, size 1)
   - Off-by-one errors in sliding window

Good luck!
