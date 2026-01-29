# Stacks and Queues: Exercise Solutions

## Solution 1: Implement Stack with Max

```python
class MaxStack:
    """
    Stack with O(1) getMax operation.

    Strategy: Maintain parallel stack tracking max at each level.

    Time Complexity: All operations O(1)
    Space Complexity: O(n) for two stacks
    """

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.max_stack:
            self.max_stack.append(val)
        else:
            self.max_stack.append(max(val, self.max_stack[-1]))

    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        self.max_stack.pop()
        return self.stack.pop()

    def top(self):
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def getMax(self):
        if not self.max_stack:
            raise IndexError("getMax from empty stack")
        return self.max_stack[-1]


# Test
stack = MaxStack()
stack.push(5)
stack.push(1)
stack.push(5)
assert stack.getMax() == 5
assert stack.pop() == 5
assert stack.getMax() == 5
print("✓ All tests passed")
```

**Complexity Analysis:**
- push(): O(1)
- pop(): O(1)
- top(): O(1)
- getMax(): O(1)
- Space: O(n)

---

## Solution 2: Valid Parentheses

```python
def isValid(s):
    """
    LeetCode #20

    Approach: Use stack to match opening/closing brackets.

    Time: O(n)
    Space: O(n)
    """
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0


# Test cases
assert isValid("()") == True
assert isValid("()[]{}") == True
assert isValid("(]") == False
assert isValid("([)]") == False
assert isValid("{[]}") == True
print("✓ All tests passed")
```

**Complexity Analysis:**
- Time: O(n) - single pass through string
- Space: O(n) - stack holds up to n/2 brackets

---

## Solution 3: Next Greater Element I

```python
def nextGreaterElement(nums1, nums2):
    """
    LeetCode #496

    Approach: Use monotonic decreasing stack on nums2,
    then build hashmap, finally construct result for nums1.

    Time: O(n + m) where n=len(nums2), m=len(nums1)
    Space: O(n) for stack and hashmap
    """
    # Build next greater map for nums2
    next_greater = {}
    stack = []

    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    # Remaining elements have no next greater
    for num in stack:
        next_greater[num] = -1

    # Build result for nums1
    return [next_greater[num] for num in nums1]


# Test cases
assert nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1]
assert nextGreaterElement([2,4], [1,2,3,4]) == [3,-1]
print("✓ All tests passed")
```

**Complexity Analysis:**
- Time: O(n + m)
- Space: O(n)

---

## Solution 4: Backspace String Compare

```python
def backspaceCompare(s, t):
    """
    LeetCode #844

    Approach: Build final strings using stack.

    Time: O(n + m)
    Space: O(n + m)
    """
    def build(s):
        stack = []
        for char in s:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)

    return build(s) == build(t)


# Test cases
assert backspaceCompare("ab#c", "ad#c") == True
assert backspaceCompare("ab##", "c#d#") == True
assert backspaceCompare("a#c", "b") == False
print("✓ All tests passed")
```

**Alternative O(1) Space Solution:**
```python
def backspaceCompare(s, t):
    """
    Two pointers from right to left.

    Time: O(n + m)
    Space: O(1)
    """
    def next_valid_char(s, i):
        backspace = 0
        while i >= 0:
            if s[i] == '#':
                backspace += 1
            elif backspace > 0:
                backspace -= 1
            else:
                return i
            i -= 1
        return i

    i, j = len(s) - 1, len(t) - 1

    while i >= 0 or j >= 0:
        i = next_valid_char(s, i)
        j = next_valid_char(t, j)

        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False

        if (i >= 0) != (j >= 0):
            return False

        i -= 1
        j -= 1

    return True
```

---

## Solution 5: Remove All Adjacent Duplicates In String

```python
def removeDuplicates(s):
    """
    LeetCode #1047

    Approach: Use stack, pop if top equals current char.

    Time: O(n)
    Space: O(n)
    """
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)


# Test cases
assert removeDuplicates("abbaca") == "ca"
assert removeDuplicates("azxxzy") == "ay"
print("✓ All tests passed")
```

**Complexity Analysis:**
- Time: O(n) - each character processed once
- Space: O(n) - worst case no duplicates

---

## Solution 6: Baseball Game

```python
def calPoints(operations):
    """
    LeetCode #682

    Approach: Use stack to track valid scores.

    Time: O(n)
    Space: O(n)
    """
    stack = []

    for op in operations:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            stack.append(2 * stack[-1])
        elif op == 'C':
            stack.pop()
        else:
            stack.append(int(op))

    return sum(stack)


# Test cases
assert calPoints(["5","2","C","D","+"]) == 30
assert calPoints(["5","-2","4","C","D","9","+","+"]) == 27
print("✓ All tests passed")
```

**Complexity Analysis:**
- Time: O(n)
- Space: O(n)

---

## Solution 7: Min Stack

```python
class MinStack:
    """
    LeetCode #155

    Strategy: Maintain parallel stack tracking min at each level.

    Time: All operations O(1)
    Space: O(n)
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# Test
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin() == -3
minStack.pop()
assert minStack.top() == 0
assert minStack.getMin() == -2
print("✓ All tests passed")
```

---

## Solution 8: Daily Temperatures

```python
def dailyTemperatures(temperatures):
    """
    LeetCode #739

    Approach: Monotonic decreasing stack storing indices.

    Time: O(n) - each index pushed/popped once
    Space: O(n)
    """
    n = len(temperatures)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day

        stack.append(i)

    return result


# Test cases
assert dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert dailyTemperatures([30,40,50,60]) == [1,1,1,0]
assert dailyTemperatures([30,60,90]) == [1,1,0]
print("✓ All tests passed")
```

**Complexity Analysis:**
- Time: O(n) - amortized O(1) per element
- Space: O(n) - stack size

---

## Solution 9: Evaluate Reverse Polish Notation

```python
def evalRPN(tokens):
    """
    LeetCode #150

    Approach: Use stack, push numbers, pop for operators.

    Time: O(n)
    Space: O(n)
    """
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:  # '/'
                result = int(a / b)  # Truncate toward zero

            stack.append(result)
        else:
            stack.append(int(token))

    return stack[0]


# Test cases
assert evalRPN(["2","1","+","3","*"]) == 9
assert evalRPN(["4","13","5","/","+"]) == 6
print("✓ All tests passed")
```

---

## Solution 10: Decode String

```python
def decodeString(s):
    """
    LeetCode #394

    Approach: Use stack to handle nested brackets.

    Time: O(n * max_k) where max_k is max repetition
    Space: O(n)
    """
    stack = []
    current_num = 0
    current_str = ""

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char

    return current_str


# Test cases
assert decodeString("3[a]2[bc]") == "aaabcbc"
assert decodeString("3[a2[c]]") == "accaccacc"
assert decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
print("✓ All tests passed")
```

---

## Solution 11: Asteroid Collision

```python
def asteroidCollision(asteroids):
    """
    LeetCode #735

    Approach: Use stack to handle collisions.

    Time: O(n) - each asteroid processed once
    Space: O(n)
    """
    stack = []

    for asteroid in asteroids:
        alive = True

        while alive and stack and asteroid < 0 < stack[-1]:
            if abs(asteroid) > abs(stack[-1]):
                stack.pop()
            elif abs(asteroid) == abs(stack[-1]):
                stack.pop()
                alive = False
            else:
                alive = False

        if alive:
            stack.append(asteroid)

    return stack


# Test cases
assert asteroidCollision([5,10,-5]) == [5,10]
assert asteroidCollision([8,-8]) == []
assert asteroidCollision([10,2,-5]) == [10]
assert asteroidCollision([-2,-1,1,2]) == [-2,-1,1,2]
print("✓ All tests passed")
```

---

## Solution 12: Remove K Digits

```python
def removeKdigits(num, k):
    """
    LeetCode #402

    Approach: Monotonic increasing stack.

    Time: O(n)
    Space: O(n)
    """
    stack = []
    to_remove = k

    for digit in num:
        while stack and to_remove > 0 and stack[-1] > digit:
            stack.pop()
            to_remove -= 1

        stack.append(digit)

    # Remove remaining from end
    if to_remove > 0:
        stack = stack[:-to_remove]

    # Remove leading zeros
    result = ''.join(stack).lstrip('0')
    return result if result else '0'


# Test cases
assert removeKdigits("1432219", 3) == "1219"
assert removeKdigits("10200", 1) == "200"
assert removeKdigits("10", 2) == "0"
print("✓ All tests passed")
```

---

## Solution 13: Simplify Path

```python
def simplifyPath(path):
    """
    LeetCode #71

    Approach: Split by '/', use stack for directory navigation.

    Time: O(n)
    Space: O(n)
    """
    stack = []
    components = path.split('/')

    for comp in components:
        if comp == '' or comp == '.':
            continue
        elif comp == '..':
            if stack:
                stack.pop()
        else:
            stack.append(comp)

    return '/' + '/'.join(stack)


# Test cases
assert simplifyPath("/home/") == "/home"
assert simplifyPath("/../") == "/"
assert simplifyPath("/home//foo/") == "/home/foo"
assert simplifyPath("/a/./b/../../c/") == "/c"
print("✓ All tests passed")
```

---

## Solution 14: Implement Queue using Stacks

```python
class MyQueue:
    """
    LeetCode #232

    Strategy: Two stacks - input and output.
    Transfer from input to output when output is empty.

    Time: push O(1), pop/peek O(1) amortized
    Space: O(n)
    """

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        self.input_stack.append(x)

    def pop(self):
        self._transfer()
        return self.output_stack.pop()

    def peek(self):
        self._transfer()
        return self.output_stack[-1]

    def empty(self):
        return not self.input_stack and not self.output_stack

    def _transfer(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())


# Test
q = MyQueue()
q.push(1)
q.push(2)
assert q.peek() == 1
assert q.pop() == 1
assert q.empty() == False
print("✓ All tests passed")
```

---

## Solution 15: Implement Stack using Queues

```python
from collections import deque


class MyStack:
    """
    LeetCode #225

    Strategy: Use single queue, rotate on push.

    Time: push O(n), pop/top O(1)
    Space: O(n)
    """

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


# Test
stack = MyStack()
stack.push(1)
stack.push(2)
assert stack.top() == 2
assert stack.pop() == 2
assert stack.empty() == False
print("✓ All tests passed")
```

---

## Solution 16: Online Stock Span

```python
class StockSpanner:
    """
    LeetCode #901

    Approach: Monotonic decreasing stack storing (price, span).

    Time: O(1) amortized per next()
    Space: O(n)
    """

    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))
        return span


# Test
ss = StockSpanner()
assert ss.next(100) == 1
assert ss.next(80) == 1
assert ss.next(60) == 1
assert ss.next(70) == 2
assert ss.next(60) == 1
assert ss.next(75) == 4
assert ss.next(85) == 6
print("✓ All tests passed")
```

**Complexity Analysis:**
- Time: O(1) amortized - each price pushed/popped once
- Space: O(n) - stack size

---

## Solution 17: Sliding Window Maximum

```python
from collections import deque


def maxSlidingWindow(nums, k):
    """
    LeetCode #239

    Approach: Monotonic decreasing deque storing indices.

    Time: O(n) - each element added/removed once
    Space: O(k)
    """
    result = []
    dq = deque()

    for i in range(len(nums)):
        # Remove elements outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Test cases
assert maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
assert maxSlidingWindow([1], 1) == [1]
print("✓ All tests passed")
```

---

## Solution 18: Largest Rectangle in Histogram

```python
def largestRectangleArea(heights):
    """
    LeetCode #84

    Approach: Monotonic increasing stack storing indices.

    Time: O(n) - each bar pushed/popped once
    Space: O(n)
    """
    max_area = 0
    stack = []

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h_idx = stack.pop()
            h = heights[h_idx]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)

        stack.append(i)

    while stack:
        h_idx = stack.pop()
        h = heights[h_idx]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * w)

    return max_area


# Test cases
assert largestRectangleArea([2,1,5,6,2,3]) == 10
assert largestRectangleArea([2,4]) == 4
print("✓ All tests passed")
```

---

## Solution 19: Trapping Rain Water

```python
def trap(height):
    """
    LeetCode #42

    Approach 1: Monotonic decreasing stack.

    Time: O(n)
    Space: O(n)
    """
    water = 0
    stack = []

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            bottom = stack.pop()

            if not stack:
                break

            left = stack[-1]
            width = i - left - 1
            bounded_height = min(height[left], height[i]) - height[bottom]
            water += width * bounded_height

        stack.append(i)

    return water


def trap_two_pointers(height):
    """
    Approach 2: Two pointers (more space efficient).

    Time: O(n)
    Space: O(1)
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


# Test cases
assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert trap([4,2,0,3,2,5]) == 9
assert trap_two_pointers([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert trap_two_pointers([4,2,0,3,2,5]) == 9
print("✓ All tests passed")
```

---

## Solution 20: Basic Calculator

```python
def calculate(s):
    """
    LeetCode #224

    Approach: Stack to handle parentheses.

    Time: O(n)
    Space: O(n)
    """
    stack = []
    result = 0
    sign = 1
    num = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            sign = 1
            num = 0
        elif char == '-':
            result += sign * num
            sign = -1
            num = 0
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            num = 0
            result *= stack.pop()  # Pop sign
            result += stack.pop()  # Pop previous result

    result += sign * num
    return result


# Test cases
assert calculate("1 + 1") == 2
assert calculate(" 2-1 + 2 ") == 3
assert calculate("(1+(4+5+2)-3)+(6+8)") == 23
print("✓ All tests passed")
```

---

## Summary of Approaches

**Pattern Recognition:**

1. **Matching/Nesting** → Stack
   - Valid parentheses
   - Decode string

2. **Next Greater/Smaller** → Monotonic Stack
   - Daily temperatures
   - Next greater element
   - Stock span

3. **Sliding Window Extrema** → Monotonic Deque
   - Sliding window maximum

4. **Area/Volume Calculation** → Monotonic Stack
   - Largest rectangle
   - Trapping rain water

5. **Design Problems** → Multiple Stacks/Queues
   - Queue with stacks
   - Stack with queues
   - Min/Max stack

6. **Expression Evaluation** → Stack
   - RPN evaluation
   - Basic calculator

All solutions provided include:
- Complete implementation
- Complexity analysis
- Test cases
- Alternative approaches where applicable
