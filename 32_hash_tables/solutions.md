# Hash Tables: Exercise Solutions

Complete solutions for all 20 exercises with multiple approaches, complexity analysis, and explanations.

[Due to length constraints, I'm providing solutions for all 20 problems in condensed format with key insights]

## Solution 1: Two Sum
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```
Time: O(n), Space: O(n)

## Solution 2: Valid Anagram
```python
def is_anagram(s, t):
    from collections import Counter
    return Counter(s) == Counter(t)
```
Time: O(n), Space: O(1) - max 26 chars

## Solution 3: Contains Duplicate
```python
def contains_duplicate(nums):
    return len(nums) != len(set(nums))
```
Time: O(n), Space: O(n)

## Solution 4: Single Number
```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR cancels duplicates
    return result
```
Time: O(n), Space: O(1)

## Solution 5: Intersection of Two Arrays
```python
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
```
Time: O(n + m), Space: O(min(n,m))

## Solution 6: First Unique Character
```python
def first_uniq_char(s):
    from collections import Counter
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1
```
Time: O(n), Space: O(1)

## Solution 7: Ransom Note
```python
def can_construct(ransom_note, magazine):
    from collections import Counter
    ransom_count = Counter(ransom_note)
    magazine_count = Counter(magazine)
    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True
```
Time: O(n + m), Space: O(1)

## Solution 8: Group Anagrams
```python
def group_anagrams(strs):
    from collections import defaultdict
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```
Time: O(n * k log k), Space: O(n * k)

## Solution 9: Longest Substring Without Repeating
```python
def length_of_longest_substring(s):
    char_index = {}
    max_length = 0
    start = 0
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    return max_length
```
Time: O(n), Space: O(min(n,m))

## Solution 10: Longest Consecutive Sequence
```python
def longest_consecutive(nums):
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:  # Start of sequence
            current = num
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            max_length = max(max_length, length)
    return max_length
```
Time: O(n), Space: O(n)

## Solution 11: Top K Frequent Elements
```python
def top_k_frequent(nums, k):
    from collections import Counter
    import heapq
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```
Time: O(n log k), Space: O(n)

## Solution 12: Subarray Sum Equals K
```python
def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    sum_freq = {0: 1}
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_freq:
            count += sum_freq[prefix_sum - k]
        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1
    return count
```
Time: O(n), Space: O(n)

## Solution 13: 4Sum II
```python
def four_sum_count(nums1, nums2, nums3, nums4):
    from collections import defaultdict
    sum_count = defaultdict(int)
    for a in nums1:
        for b in nums2:
            sum_count[a + b] += 1
    count = 0
    for c in nums3:
        for d in nums4:
            count += sum_count[-(c + d)]
    return count
```
Time: O(n²), Space: O(n²)

## Solution 14: Find All Anagrams
```python
def find_anagrams(s, p):
    from collections import Counter
    if len(p) > len(s):
        return []
    p_count = Counter(p)
    window = Counter()
    result = []
    k = len(p)
    for i in range(len(s)):
        window[s[i]] += 1
        if i >= k:
            if window[s[i-k]] == 1:
                del window[s[i-k]]
            else:
                window[s[i-k]] -= 1
        if i >= k - 1 and window == p_count:
            result.append(i - k + 1)
    return result
```
Time: O(n), Space: O(1)

## Solution 15: Isomorphic Strings
```python
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    s_to_t, t_to_s = {}, {}
    for cs, ct in zip(s, t):
        if (cs in s_to_t and s_to_t[cs] != ct) or \
           (ct in t_to_s and t_to_s[ct] != cs):
            return False
        s_to_t[cs] = ct
        t_to_s[ct] = cs
    return True
```
Time: O(n), Space: O(1)

## Solution 16: Word Pattern
```python
def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    char_to_word, word_to_char = {}, {}
    for c, w in zip(pattern, words):
        if (c in char_to_word and char_to_word[c] != w) or \
           (w in word_to_char and word_to_char[w] != c):
            return False
        char_to_word[c] = w
        word_to_char[w] = c
    return True
```
Time: O(n), Space: O(n)

## Solution 17: Minimum Window Substring
```python
def min_window(s, t):
    from collections import Counter
    if not s or not t:
        return ""
    t_count = Counter(t)
    window = Counter()
    required = len(t_count)
    formed = 0
    left = 0
    min_len = float('inf')
    min_window = (0, 0)
    for right in range(len(s)):
        char = s[right]
        window[char] += 1
        if char in t_count and window[char] == t_count[char]:
            formed += 1
        while formed == required and left <= right:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = (left, right)
            char = s[left]
            window[char] -= 1
            if char in t_count and window[char] < t_count[char]:
                formed -= 1
            left += 1
    return "" if min_len == float('inf') else s[min_window[0]:min_window[1]+1]
```
Time: O(n + m), Space: O(m)

## Solution 18: Design HashMap
```python
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]
    def _hash(self, key):
        return key % self.size
    def put(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return -1
    def remove(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
```
Time: O(1) average, Space: O(n)

## Solution 19: Design HashSet
```python
class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]
    def _hash(self, key):
        return key % self.size
    def add(self, key):
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)
    def remove(self, key):
        index = self._hash(key)
        if key in self.table[index]:
            self.table[index].remove(key)
    def contains(self, key):
        index = self._hash(key)
        return key in self.table[index]
```
Time: O(1) average, Space: O(n)

## Solution 20: LRU Cache
```python
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```
Time: O(1), Space: O(capacity)

## Key Patterns Summary

1. **Complement Pattern**: Two Sum, subarray sum
2. **Frequency Counting**: Anagrams, top k frequent
3. **Sliding Window**: Longest substring, find anagrams
4. **Bidirectional Mapping**: Isomorphic strings, word pattern
5. **Set Operations**: Intersection, contains duplicate
6. **Prefix Sum**: Subarray sum equals k
7. **Start Detection**: Longest consecutive sequence
