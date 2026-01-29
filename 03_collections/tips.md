# Collections: Tips, Tricks, and Gotchas

## List Tips

### Tip 1: Use List Comprehensions
**Prefer**:
```python
squares = [x**2 for x in range(10)]
```

**Over**:
```python
squares = []
for x in range(10):
    squares.append(x**2)
```

### Gotcha 1: Shallow Copy
```python
a = [[1, 2], [3, 4]]
b = a.copy()  # Shallow copy!
b[0].append(999)
# a is also modified: [[1, 2, 999], [3, 4]]

# Deep copy for nested structures
import copy
b = copy.deepcopy(a)
```

## Dictionary Tips

### Tip 1: Use get() for Safe Access
```python
# Avoid KeyError
value = d.get("key", "default")

# Instead of
if "key" in d:
    value = d["key"]
else:
    value = "default"
```

### Tip 2: defaultdict for Grouping
```python
from collections import defaultdict

# Grouping
groups = defaultdict(list)
for item in data:
    groups[item.category].append(item)
```

## Set Tips

### Tip 1: Remove Duplicates
```python
unique = list(set(items))
```

### Tip 2: Fast Membership Testing
```python
# set is O(1), list is O(n)
allowed = {1, 2, 3, 4, 5}
if x in allowed:  # Fast!
    pass
```

## Performance Tips

- Lists: Use when order matters
- Sets: Use for membership testing
- Dicts: Use for key-value lookups
- deque: Use for queue operations
- Counter: Use for counting

See theory.md for when to use which collection type.
