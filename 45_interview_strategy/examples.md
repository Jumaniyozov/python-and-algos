# Chapter 45: Interview Strategy - Examples

## Table of Contents
1. [Mock Interview Walkthrough 1: Two Sum](#mock-interview-1-two-sum)
2. [Mock Interview Walkthrough 2: Course Schedule](#mock-interview-2-course-schedule)
3. [Mock Interview Walkthrough 3: LRU Cache](#mock-interview-3-lru-cache)
4. [Mock Interview Walkthrough 4: Word Ladder](#mock-interview-4-word-ladder)
5. [Mock Interview Walkthrough 5: Design Hit Counter](#mock-interview-5-design-hit-counter)

---

## Mock Interview 1: Two Sum

**Problem**: Given an array of integers `nums` and an integer `target`, return indices of two numbers that add up to target.

### Candidate's Thought Process (UMPIRE Framework)

#### U - Understand (0:00-0:05)

**Candidate**: "Let me make sure I understand the problem. I'm given an array of integers and a target sum, and I need to find two indices where the values add up to the target. Can I clarify a few things?"

**Interviewer**: "Sure, go ahead."

**Candidate**:
- "Can the same element be used twice?" → **No**
- "Is there always exactly one solution?" → **Yes**
- "Can the array be empty or have just one element?" → **No, at least 2 elements**
- "Are the numbers sorted?" → **No, unsorted**
- "Can there be negative numbers?" → **Yes**
- "Should I return the values or the indices?" → **Indices**

"So to confirm: I need to find two distinct indices i and j where nums[i] + nums[j] = target, and return [i, j]."

**Interviewer**: "That's correct."

#### M - Match (0:05-0:08)

**Candidate**: "This is a search problem where for each number x, I need to find its complement (target - x). Let me think about approaches:

1. **Brute force**: Check all pairs → O(n²) time, O(1) space
2. **Sort + Two pointers**: Would lose original indices → Not suitable
3. **Hash map**: Store seen numbers with their indices → O(n) time, O(n) space

I'll use the hash map approach for optimal O(n) solution."

#### P - Plan (0:08-0:15)

**Candidate**: "Here's my plan:

1. Create an empty hash map to store {value: index}
2. Iterate through the array:
   - Calculate complement = target - current_number
   - If complement exists in hash map, return [hash_map[complement], current_index]
   - Otherwise, add current number to hash map
3. By problem guarantee, we'll find a solution

Let me trace through an example:
- nums = [2, 7, 11, 15], target = 9
- i=0, num=2: complement=7, not in map, add {2:0}
- i=1, num=7: complement=2, found in map! return [0, 1]

Time: O(n) - single pass
Space: O(n) - hash map

Does this approach sound good?"

**Interviewer**: "Yes, proceed with implementation."

#### I - Implement (0:15-0:25)

**Candidate**: "I'll write the solution now:"

```python
def two_sum(nums, target):
    """
    Find two indices that sum to target.

    Time: O(n)
    Space: O(n)

    Args:
        nums: List of integers
        target: Target sum

    Returns:
        List of two indices [i, j]
    """
    # Hash map to store {value: index}
    seen = {}

    # Single pass through array
    for i, num in enumerate(nums):
        complement = target - num

        # Check if complement exists
        if complement in seen:
            return [seen[complement], i]

        # Add current number to map
        seen[num] = i

    # Per problem constraints, will always find solution
    return []
```

"Let me explain as I code:
- I create a hash map called 'seen' to track numbers we've encountered
- For each number, I calculate its complement
- If the complement is in our map, we found the pair
- Otherwise, I add the current number for future lookups
- The order ensures we don't use the same element twice"

#### R - Review (0:25-0:30)

**Candidate**: "Let me trace through the example to verify:

nums = [2, 7, 11, 15], target = 9

- i=0, num=2: complement=7, seen={}, add {2:0}
- i=1, num=7: complement=2, 2 in seen! return [0, 1] ✓

Edge cases:
- **Negative numbers**: Works, hash map handles any integers ✓
- **Duplicates**: Uses first occurrence for complement ✓
- **Large numbers**: No overflow in Python ✓
- **Two elements**: Minimum size guaranteed by problem ✓

Looks correct!"

#### E - Evaluate (0:30-0:35)

**Candidate**: "Time Complexity: O(n)
- We iterate through the array once
- Hash map operations (lookup and insert) are O(1) average

Space Complexity: O(n)
- In worst case, we store n-1 elements before finding the pair

**Trade-offs**:
- We trade O(n) space for O(n) time
- Alternative: O(1) space but O(n²) time with nested loops
- For this problem, hash map is optimal since we must check all elements anyway

**Follow-up optimizations**:
- If input was sorted, could use two pointers in O(1) space
- But we'd lose original indices or need extra space to track them"

**Interviewer**: "Great! What if I wanted all pairs that sum to target?"

**Candidate**: "I'd modify to continue after finding pairs and store results in a list. Would need to avoid duplicates, possibly by sorting pairs or using a set."

---

## Mock Interview 2: Course Schedule

**Problem**: Given `numCourses` and `prerequisites` where `prerequisites[i] = [a, b]` means course a requires course b, determine if you can finish all courses.

### Candidate's Thought Process

#### U - Understand (0:00-0:05)

**Candidate**: "Let me understand this problem. We have courses numbered 0 to numCourses-1, and prerequisites represent dependencies. Can I clarify:

- Can there be duplicate prerequisites? → **Assume no**
- Can a course depend on itself? → **No**
- What if there are no prerequisites? → **Return true**
- Is this asking if there's a cycle? → **Yes, essentially**

So this is a cycle detection problem in a directed graph. If there's a cycle, courses can't be completed."

#### M - Match (0:05-0:08)

**Candidate**: "This is a directed graph problem. Course dependencies form edges:
[a, b] means a depends on b, so edge b → a

**Approaches**:
1. **DFS with 3 colors**: Track unvisited/visiting/visited states
2. **Topological sort (Kahn's)**: If all nodes processed, no cycle
3. **Union Find**: Doesn't work well for directed graphs

I'll use DFS with 3 states for elegant cycle detection."

#### P - Plan (0:08-0:15)

**Candidate**: "Algorithm:

1. Build adjacency list from prerequisites
2. Create state array: 0=white (unvisited), 1=gray (visiting), 2=black (visited)
3. For each unvisited course, run DFS:
   - If we encounter a gray node → cycle detected → return false
   - If we encounter a black node → already processed → continue
   - Mark current as gray, explore neighbors, mark as black
4. If no cycles found, return true

Example: numCourses=2, prerequisites=[[1,0]]
- Build graph: {0: [1], 1: []}
- DFS from 0: mark gray, visit 1, mark both black
- No cycle, return true

Time: O(V + E), Space: O(V + E)"

#### I - Implement (0:15-0:30)

```python
from collections import defaultdict

def can_finish(num_courses, prerequisites):
    """
    Check if all courses can be completed (no cycle).

    Time: O(V + E)
    Space: O(V + E)
    """
    # Build adjacency list
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # 0: white, 1: gray, 2: black
    state = [0] * num_courses

    def has_cycle(course):
        if state[course] == 1:
            return True  # Gray = cycle
        if state[course] == 2:
            return False  # Black = processed

        state[course] = 1  # Mark gray
        for neighbor in graph[course]:
            if has_cycle(neighbor):
                return True
        state[course] = 2  # Mark black
        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False

    return True
```

#### R - Review & E - Evaluate (0:30-0:40)

**Candidate**: "Let me verify with example: [[1,0],[0,1]]
- Graph: {0: [1], 1: [0]}
- Start DFS(0): state[0]=1, DFS(1): state[1]=1, DFS(0): state[0]=1 → cycle! ✓

Edge cases handled:
- No prerequisites: No cycles ✓
- Single course: Trivial ✓
- Linear dependencies: Works ✓

Complexity:
- Time: O(V + E) - visit each vertex and edge once
- Space: O(V + E) - graph + recursion stack

This is optimal for cycle detection in directed graphs."

---

## Mock Interview 3: LRU Cache

**Problem**: Design a data structure for Least Recently Used (LRU) cache.

### Candidate's Thought Process (Condensed)

#### U - Understand

**Candidate**: "I need to implement get(key) and put(key, value) operations. When capacity is reached, evict the least recently used item. Both operations should be O(1)."

#### M - Match

**Candidate**: "This requires:
- Fast lookup → **Hash map**
- Fast insertion/deletion → **Doubly linked list**
- Track usage order → **Move to front on access**

I'll use hash map + doubly linked list combination."

#### P - Plan

**Candidate**: "Structure:
- Doubly linked list: maintain LRU order (head=most recent, tail=least recent)
- Hash map: {key → list node} for O(1) access
- get(key): Move node to head, return value
- put(key, value): Add to head, evict tail if over capacity"

#### I - Implement

```python
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        """Add node after head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_head(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```

#### R & E - Review & Evaluate

**Candidate**: "Both get and put are O(1):
- Hash map lookup: O(1)
- List operations: O(1)
- Space: O(capacity)

This is the optimal solution for LRU cache."

---

## Mock Interview 4: Word Ladder

**Problem**: Find shortest transformation sequence from beginWord to endWord, changing one letter at a time using dictionary words.

### Candidate's Thought Process (Condensed)

#### U - Understand

**Candidate**: "This is a shortest path problem. I need to:
- Transform beginWord to endWord
- Change only one letter per step
- Each intermediate word must be in wordList
- Find minimum transformations

This is BFS on a word graph!"

#### P - Plan

**Candidate**: "Algorithm:
1. Use BFS for shortest path
2. For each word, try all 26 letters at each position
3. Track visited words to avoid cycles
4. Return steps when endWord is reached

Time: O(M² × N) where M=word length, N=word list size"

#### I - Implement

```python
from collections import deque

def ladder_length(begin_word, end_word, word_list):
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    queue = deque([(begin_word, 1)])
    visited = {begin_word}

    while queue:
        word, steps = queue.popleft()

        if word == end_word:
            return steps

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]

                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, steps + 1))

    return 0
```

---

## Mock Interview 5: Design Hit Counter

**Problem**: Design a hit counter that counts hits in the last 5 minutes (300 seconds).

### Candidate's Thought Process

#### U - Understand

**Candidate**: "I need to implement:
- hit(timestamp): Record a hit
- getHits(timestamp): Get hits in last 300 seconds

Clarifications:
- Timestamps are chronological? → **Yes**
- Multiple hits at same timestamp? → **Yes**
- Memory constraints? → **Important to consider**"

#### P - Plan

**Candidate**: "Two approaches:

**Approach 1**: Store all timestamps
- hit(): Append timestamp
- getHits(): Count timestamps >= current - 300
- Space: O(N) for all hits

**Approach 2**: Circular buffer (optimal)
- Use array of size 300
- Each index represents a second
- Store hit count for that second
- Space: O(300) = O(1)

I'll implement the circular buffer for O(1) space."

#### I - Implement

```python
class HitCounter:
    def __init__(self):
        self.times = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp):
        idx = timestamp % 300
        if self.times[idx] != timestamp:
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            self.hits[idx] += 1

    def get_hits(self, timestamp):
        total = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        return total
```

**Candidate**: "This uses circular buffer:
- hit(): O(1) - update single slot
- getHits(): O(1) - scan fixed 300 slots
- Space: O(1) - fixed size arrays"

---

## Key Takeaways from Examples

**Communication Patterns:**
1. Always restate the problem
2. Ask clarifying questions
3. Discuss multiple approaches
4. Explain while coding
5. Test with examples
6. Analyze complexity

**UMPIRE Framework:**
- Understand: 5 minutes
- Match: 3 minutes
- Plan: 5-7 minutes
- Implement: 15-20 minutes
- Review: 3-5 minutes
- Evaluate: 3-5 minutes

**Success Factors:**
- Clear communication
- Structured thinking
- Multiple approaches
- Testing awareness
- Complexity analysis
- Trade-off discussion

Practice these walkthroughs to internalize the interview process!
