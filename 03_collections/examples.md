# Collections: Code Examples

## Example 1: List Operations

```python
# Creating and manipulating lists
numbers = [1, 2, 3, 4, 5]

# Indexing and slicing
print(f"First: {numbers[0]}")
print(f"Last: {numbers[-1]}")
print(f"First 3: {numbers[:3]}")
print(f"Reversed: {numbers[::-1]}")

# Modifying
numbers.append(6)
numbers.insert(0, 0)
numbers.extend([7, 8, 9])
print(f"Modified: {numbers}")

# List methods
numbers.sort(reverse=True)
print(f"Sorted desc: {numbers}")

# List comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
print(f"Squares: {squares}")
print(f"Evens: {evens}")
```

## Example 2: Dictionary Operations

```python
# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "NYC",
    "skills": ["Python", "JavaScript"]
}

# Accessing values
print(f"Name: {person['name']}")
print(f"City: {person.get('city', 'Unknown')}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")

# Iterating
for key, value in person.items():
    print(f"{key}: {value}")
```

## Example 3: Sets and Set Operations

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"Union: {a | b}")
print(f"Intersection: {a & b}")
print(f"Difference: {a - b}")
print(f"Symmetric diff: {a ^ b}")

# Remove duplicates
items = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(items))
print(f"Unique: {unique}")
```

## Example 4: Collections Module

```python
from collections import Counter, defaultdict, deque, namedtuple

# Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
print(f"Most common: {counts.most_common(2)}")

# defaultdict
groups = defaultdict(list)
for item in ["a1", "b1", "a2", "b2"]:
    groups[item[0]].append(item)
print(f"Groups: {dict(groups)}")

# deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(f"Deque: {dq}")

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Point: x={p.x}, y={p.y}")
```

See theory.md for detailed explanations of all examples.
