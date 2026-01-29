# Exercises: Performance Optimization

## Exercise 1: Profile and Identify Bottlenecks (Easy)

Write a program with performance issues and use cProfile to identify the bottleneck.

**Requirements**:
- Create a function with multiple operations
- Use cProfile to profile it
- Identify which operation is slowest
- Print top 5 slowest functions

**Example**:
```python
import cProfile
import pstats

def process_data():
    # Create a slow function with bottlenecks
    # Profile it and identify the slowest parts
    pass

# Your profiling code here
```

## Exercise 2: Optimize String Concatenation (Easy)

Given a function that builds a large string using +=, optimize it to use join().

**Requirements**:
- Original function builds string with += in loop
- Optimized version uses join()
- Benchmark both versions
- Calculate speedup

**Example**:
```python
def slow_concat(words):
    """Concatenate words using +=."""
    result = ""
    for word in words:
        result += word + " "
    return result

# Create optimized version and benchmark both
```

## Exercise 3: Choose Better Data Structure (Easy)

Optimize a program that checks if items exist in a collection.

**Requirements**:
- Original uses list for membership testing
- Convert to set
- Benchmark both approaches with 10000 items
- Show performance improvement

**Example**:
```python
def find_duplicates_slow(items):
    """Find duplicates using list."""
    seen = []
    duplicates = []
    for item in items:
        if item in seen:
            duplicates.append(item)
        else:
            seen.append(item)
    return duplicates

# Optimize using set
```

## Exercise 4: Add Caching to Expensive Function (Easy)

Add memoization to a recursive function that calculates factorials.

**Requirements**:
- Implement factorial recursively
- Add @lru_cache decorator
- Benchmark with and without cache
- Test with factorial(50), factorial(100)

**Example**:
```python
def factorial(n):
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Add caching and benchmark
```

## Exercise 5: Reduce Function Call Overhead (Easy)

Optimize a program that calls a simple function many times.

**Requirements**:
- Original: calls function in loop
- Optimized: inline operation or use list comprehension
- Benchmark both versions
- Calculate overhead percentage

**Example**:
```python
def square(x):
    return x ** 2

def process_slow(data):
    result = []
    for x in data:
        result.append(square(x))
    return result

# Create optimized version
```

## Exercise 6: Optimize Nested Loops (Medium)

Optimize a function with nested loops that finds common elements in two lists.

**Requirements**:
- Original: O(n*m) nested loops
- Optimized: O(n+m) using sets
- Benchmark with lists of 1000 elements each
- Show complexity improvement

**Example**:
```python
def find_common_slow(list1, list2):
    """Find common elements using nested loops."""
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in common:
                common.append(item1)
    return common

# Optimize to O(n+m)
```

## Exercise 7: Improve Algorithm Complexity (Medium)

Optimize a function that finds the most frequent element in a list.

**Requirements**:
- Original: O(n²) using count()
- Optimized: O(n) using Counter or dictionary
- Benchmark with list of 10000 elements
- Compare time complexity

**Example**:
```python
def most_frequent_slow(items):
    """Find most frequent element - O(n²)."""
    max_count = 0
    max_item = None
    for item in items:
        count = items.count(item)
        if count > max_count:
            max_count = count
            max_item = item
    return max_item

# Optimize to O(n)
```

## Exercise 8: Optimize Memory Usage (Medium)

Refactor a function that loads all data into memory to use generators.

**Requirements**:
- Original: loads all results into list
- Optimized: uses generator
- Compare memory usage using sys.getsizeof()
- Process only first 100 items from 1 million

**Example**:
```python
def process_all(n):
    """Process all items - memory intensive."""
    results = []
    for i in range(n):
        results.append(expensive_calculation(i))
    return results

def expensive_calculation(x):
    return x ** 2 + x ** 3

# Optimize with generator
```

## Exercise 9: Batch Processing Optimization (Medium)

Optimize database operations by batching them.

**Requirements**:
- Simulate database with list operations
- Original: updates one item at a time
- Optimized: batches updates
- Compare performance for 1000 operations

**Example**:
```python
class Database:
    def __init__(self):
        self.data = {}
        self.commit_count = 0

    def update(self, key, value):
        self.data[key] = value
        self.commit()

    def commit(self):
        # Simulate expensive commit operation
        self.commit_count += 1
        import time
        time.sleep(0.001)

# Implement batch update method
```

## Exercise 10: Lazy Evaluation Optimization (Medium)

Implement lazy evaluation for a data processing pipeline.

**Requirements**:
- Original: processes all data eagerly
- Optimized: uses generators for each stage
- Pipeline: filter -> transform -> aggregate
- Compare memory and time for 100000 items

**Example**:
```python
def eager_pipeline(data):
    """Eager evaluation - processes all at once."""
    filtered = [x for x in data if x % 2 == 0]
    transformed = [x ** 2 for x in filtered]
    aggregated = sum(transformed[:100])
    return aggregated

# Implement lazy version with generators
```

## Exercise 11: Optimize Full Application (Hard)

Profile and optimize a complete mini-application that processes log files.

**Requirements**:
- Read log file, parse entries, find errors, generate report
- Use cProfile to find bottlenecks
- Apply at least 3 different optimizations
- Achieve at least 5x speedup
- Document what you optimized and why

**Example**:
```python
class LogAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def analyze(self):
        """Analyze log file and return error statistics."""
        # Read entire file
        # Parse each line
        # Find errors
        # Count by type
        # Generate report
        pass

# Optimize this entire class
```

## Exercise 12: Find All Bottlenecks (Hard)

Given a complex program, find and fix all performance bottlenecks.

**Requirements**:
- Program has multiple performance issues
- Use cProfile, timeit, and memory_profiler
- Identify at least 5 bottlenecks
- Fix each one with appropriate technique
- Document before/after performance

**Example**:
```python
class DataProcessor:
    def __init__(self):
        self.cache = []

    def process(self, data):
        """Process data with multiple bottlenecks."""
        # Issue 1: String concatenation in loop
        result = ""
        for item in data:
            result += str(item) + ","

        # Issue 2: Inefficient membership testing
        seen = []
        unique = []
        for item in data:
            if item not in seen:
                seen.append(item)
                unique.append(item)

        # Issue 3: Repeated calculations
        squares = []
        for i in range(len(unique)):
            squares.append(self.expensive_calc(unique[i]))

        # Issue 4: Inefficient sorting
        for i in range(len(squares)):
            for j in range(i+1, len(squares)):
                if squares[i] > squares[j]:
                    squares[i], squares[j] = squares[j], squares[i]

        return result, unique, squares

    def expensive_calc(self, x):
        return sum(i**2 for i in range(x))

# Find and fix all issues
```

## Exercise 13: Optimize Database Queries (Hard)

Optimize a program that makes many database queries.

**Requirements**:
- Original: N+1 query problem
- Optimize using joins, batch queries, caching
- Implement query result caching
- Reduce query count by at least 90%

**Example**:
```python
import sqlite3

class UserManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        """Create sample tables."""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                amount REAL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        self.conn.commit()

    def get_user_orders_slow(self):
        """N+1 query problem."""
        cursor = self.conn.cursor()

        # Get all users
        cursor.execute('SELECT id, name FROM users')
        users = cursor.fetchall()

        # For each user, get their orders (N queries!)
        result = []
        for user_id, name in users:
            cursor.execute('SELECT * FROM orders WHERE user_id = ?', (user_id,))
            orders = cursor.fetchall()
            result.append({
                'user': name,
                'orders': orders,
                'total': sum(order[2] for order in orders)
            })

        return result

# Optimize using JOIN and reduce queries
```

## Exercise 14: Parallel Processing Optimization (Hard)

Optimize CPU-intensive operations using multiprocessing.

**Requirements**:
- Original: sequential processing
- Optimized: parallel processing with multiprocessing
- Process list of 100 items
- Each item takes significant CPU time
- Compare sequential vs parallel execution

**Example**:
```python
import time

def cpu_intensive_task(n):
    """Simulate CPU-intensive work."""
    result = 0
    for i in range(n):
        result += sum(j**2 for j in range(1000))
    return result

def process_sequential(items):
    """Process items sequentially."""
    results = []
    for item in items:
        results.append(cpu_intensive_task(item))
    return results

# Implement parallel version using multiprocessing.Pool
```

## Exercise 15: Advanced Caching Strategy (Hard)

Implement a multi-level caching system with TTL and size limits.

**Requirements**:
- L1 cache: LRU with max 100 entries
- L2 cache: File-based with TTL
- Automatic cache warming
- Cache invalidation strategy
- Benchmark cache hit rates

**Example**:
```python
import time
from functools import lru_cache

class MultiLevelCache:
    """Implement multi-level cache with TTL."""

    def __init__(self, l1_size=100, l2_ttl=3600):
        self.l1_size = l1_size
        self.l2_ttl = l2_ttl
        self.l2_cache = {}
        self.stats = {'l1_hits': 0, 'l2_hits': 0, 'misses': 0}

    def get(self, key, compute_func):
        """Get value from cache or compute it."""
        # Check L1 cache
        # Check L2 cache
        # Compute if not found
        # Update caches
        # Track statistics
        pass

    def invalidate(self, key):
        """Invalidate cache entry."""
        pass

    def warm_cache(self, keys, compute_func):
        """Pre-populate cache."""
        pass

# Implement complete caching system and benchmark
```

## Testing Guidelines

For all exercises:

1. **Measure first**: Always profile/benchmark before optimizing
2. **Document baseline**: Record original performance metrics
3. **Make incremental changes**: Optimize one thing at a time
4. **Verify correctness**: Ensure optimized version produces same results
5. **Measure improvement**: Document performance gains
6. **Compare complexity**: Analyze Big-O before and after

## Success Criteria

**Easy exercises**:
- Correct implementation
- Measurable speedup (at least 2x)
- Clear benchmarking code

**Medium exercises**:
- Significant improvement (at least 5x)
- Reduced time complexity where applicable
- Memory optimization demonstrated

**Hard exercises**:
- Comprehensive optimization (10x+ speedup)
- Multiple optimization techniques applied
- Production-ready code quality
- Detailed performance analysis
