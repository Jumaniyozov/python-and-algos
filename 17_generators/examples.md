# Examples: Generators & Iterators

## Example 1: Custom Iterator Class

```python
class Countdown:
    """Iterator that counts down from start to zero"""
    
    def __init__(self, start):
        self.start = start
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        
        self.current -= 1
        return self.current + 1

# Usage
for num in Countdown(5):
    print(num)  # 5, 4, 3, 2, 1
```

## Example 2: Simple Generator Function

```python
def count_up(start, stop):
    """Generator that counts from start to stop"""
    current = start
    while current < stop:
        yield current
        current += 1

# Usage
for num in count_up(1, 6):
    print(num)  # 1, 2, 3, 4, 5

# Manual iteration
gen = count_up(10, 13)
print(next(gen))  # 10
print(next(gen))  # 11
print(next(gen))  # 12
# next(gen)  # Raises StopIteration
```

## Example 3: Generator with State

```python
def running_average():
    """Generator that maintains running average"""
    total = 0
    count = 0
    
    while True:
        value = yield (total / count if count > 0 else 0)
        if value is not None:
            total += value
            count += 1

# Usage
avg = running_average()
next(avg)  # Prime the generator

print(avg.send(10))  # 10.0
print(avg.send(20))  # 15.0
print(avg.send(30))  # 20.0
print(avg.send(40))  # 25.0
```

## Example 4: Fibonacci Generator

```python
def fibonacci(limit=None):
    """Generate Fibonacci sequence up to limit"""
    a, b = 0, 1
    count = 0
    
    while limit is None or count < limit:
        yield a
        a, b = b, a + b
        count += 1

# First 10 Fibonacci numbers
print(list(fibonacci(10)))

# Infinite sequence with islice
from itertools import islice
for num in islice(fibonacci(), 15):
    print(num, end=' ')
```

## Example 5: File Reader Generator

```python
def read_large_file(filename, chunk_size=1024):
    """Read file in chunks"""
    with open(filename, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

def read_lines(filename):
    """Read file line by line"""
    with open(filename) as f:
        for line in f:
            yield line.strip()

# Usage
for line in read_lines('data.txt'):
    if line:  # Skip empty lines
        process(line)
```

## Example 6: Generator Pipeline

```python
def read_csv(filename):
    """Read CSV file"""
    import csv
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

def filter_by_age(records, min_age):
    """Filter records by minimum age"""
    for record in records:
        if int(record['age']) >= min_age:
            yield record

def extract_names(records):
    """Extract names from records"""
    for record in records:
        yield record['name']

# Build pipeline
records = read_csv('users.csv')
adults = filter_by_age(records, 18)
names = extract_names(adults)

# Process
for name in names:
    print(name)
```

## Example 7: Generator Expression Examples

```python
# Sum of squares
total = sum(x**2 for x in range(1000))

# File processing
uppercase_lines = (line.upper() for line in open('file.txt'))

# Filtering
even_squares = (x**2 for x in range(100) if x % 2 == 0)

# Nested generator expressions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = (item for row in matrix for item in row)
print(list(flattened))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Finding first match (efficient - stops early)
first_big = next((x for x in range(10000) if x > 5000), None)
```

## Example 8: yield from Example

```python
def flatten(nested_list):
    """Recursively flatten nested lists"""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

# Usage
nested = [1, [2, 3, [4, 5]], 6, [[7], 8]]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6, 7, 8]

def chain(*iterables):
    """Chain multiple iterables"""
    for iterable in iterables:
        yield from iterable

print(list(chain([1, 2], [3, 4], [5, 6])))  # [1, 2, 3, 4, 5, 6]
```

## Example 9: Generator with send()

```python
def grep_generator(pattern):
    """Generator that filters lines matching pattern"""
    print(f"Looking for pattern: {pattern}")
    
    while True:
        line = yield
        if pattern in line:
            print(f"Match found: {line}")

# Usage
grepper = grep_generator("error")
next(grepper)  # Prime the generator

grepper.send("This is fine")
grepper.send("An error occurred")  # Match found: An error occurred
grepper.send("All good")
grepper.send("Another error")  # Match found: Another error
```

## Example 10: Generator with throw()

```python
def robust_processor():
    """Generator that handles exceptions"""
    while True:
        try:
            value = yield
            print(f"Processing: {value}")
            result = 100 / value
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        except ValueError as e:
            print(f"Value error: {e}")
            break

proc = robust_processor()
next(proc)

proc.send(10)  # Processing: 10, Result: 10.0
proc.send(0)   # Processing: 0, Cannot divide by zero!
proc.throw(ValueError, "Invalid input")  # Stops generator
```

## Example 11: Batching Generator

```python
def batch_iterable(iterable, batch_size):
    """Batch items from iterable"""
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    
    # Yield remaining items
    if batch:
        yield batch

# Usage
data = range(25)
for batch in batch_iterable(data, 10):
    print(f"Processing batch of {len(batch)} items: {batch}")
```

## Example 12: Infinite Sequence Generators

```python
def count(start=0, step=1):
    """Infinite counter"""
    n = start
    while True:
        yield n
        n += step

def cycle(iterable):
    """Cycle through iterable infinitely"""
    saved = []
    for item in iterable:
        yield item
        saved.append(item)
    
    while saved:
        for item in saved:
            yield item

def repeat(value, times=None):
    """Repeat value"""
    if times is None:
        while True:
            yield value
    else:
        for _ in range(times):
            yield value

# Usage
from itertools import islice

# First 5 counts from 10
print(list(islice(count(10), 5)))  # [10, 11, 12, 13, 14]

# Cycle through colors
colors = cycle(['red', 'green', 'blue'])
print([next(colors) for _ in range(7)])

# Repeat value
print(list(repeat('A', 5)))  # ['A', 'A', 'A', 'A', 'A']
```

## Example 13: Tree Traversal Generator

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder(node):
    """Inorder traversal generator"""
    if node:
        yield from inorder(node.left)
        yield node.value
        yield from inorder(node.right)

def preorder(node):
    """Preorder traversal generator"""
    if node:
        yield node.value
        yield from preorder(node.left)
        yield from preorder(node.right)

def postorder(node):
    """Postorder traversal generator"""
    if node:
        yield from postorder(node.left)
        yield from postorder(node.right)
        yield node.value

# Build tree
root = TreeNode(1,
    TreeNode(2, TreeNode(4), TreeNode(5)),
    TreeNode(3, TreeNode(6), TreeNode(7))
)

print("Inorder:", list(inorder(root)))     # [4, 2, 5, 1, 6, 3, 7]
print("Preorder:", list(preorder(root)))   # [1, 2, 4, 5, 3, 6, 7]
print("Postorder:", list(postorder(root))) # [4, 5, 2, 6, 7, 3, 1]
```

## Example 14: Sliding Window Generator

```python
def sliding_window(iterable, window_size):
    """Generate sliding windows over iterable"""
    from collections import deque
    
    window = deque(maxlen=window_size)
    
    for item in iterable:
        window.append(item)
        if len(window) == window_size:
            yield list(window)

# Usage
data = [1, 2, 3, 4, 5, 6, 7, 8]
for window in sliding_window(data, 3):
    print(window)

# Output:
# [1, 2, 3]
# [2, 3, 4]
# [3, 4, 5]
# ...
```

## Example 15: Async Generator

```python
import asyncio

async def async_countdown(n):
    """Async generator that counts down"""
    while n > 0:
        await asyncio.sleep(0.1)  # Simulate async operation
        yield n
        n -= 1

async def async_range(start, stop):
    """Async generator for range"""
    current = start
    while current < stop:
        await asyncio.sleep(0.05)
        yield current
        current += 1

async def main():
    # Using async for
    print("Countdown:")
    async for num in async_countdown(5):
        print(num)
    
    print("\nAsync range:")
    async for num in async_range(1, 6):
        print(num)
    
    # Async comprehension
    squares = [x**2 async for x in async_range(1, 6)]
    print(f"\nSquares: {squares}")

# Run
if __name__ == '__main__':
    asyncio.run(main())
```

## Running the Examples

All examples are self-contained and demonstrate:
1. Iterator protocol implementation
2. Generator functions and state management
3. Generator expressions for efficiency
4. Two-way communication with send()
5. Exception handling with throw()
6. Subgenerator delegation with yield from
7. Pipeline architectures
8. Infinite sequences
9. Batch processing
10. Tree traversal
11. Async generators

These patterns are fundamental to writing efficient Python code, especially when dealing with large datasets or streams.
