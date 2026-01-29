# Exercises: Context Managers

## Exercise 1: Logger Context Manager (Easy)

Create a context manager that logs when entering and exiting a code block, including execution time.

**Requirements**:
- Print "Entering [name]" on entry
- Print "Exiting [name] (took X.XX seconds)" on exit
- Handle exceptions gracefully
- Use @contextmanager decorator

**Example**:
```python
with logger("database_query"):
    # simulate work
    time.sleep(0.1)

# Expected Output:
# Entering database_query
# Exiting database_query (took 0.10 seconds)
```

## Exercise 2: Temporary File Writer (Easy)

Implement a context manager that creates a temporary file, allows writing to it, and automatically deletes it on exit.

**Requirements**:
- Create a temporary file with a given prefix
- Return the file object for writing
- Delete the file in __exit__, even if exception occurs
- Print the filename being created and deleted

**Expected Output**:
```python
with TempFileWriter('test_') as f:
    f.write('temporary data')
    print(f"Writing to: {f.name}")
# File should be deleted after exiting
```

## Exercise 3: List State Tracker (Easy)

Create a context manager that tracks changes to a list and can rollback on exception.

**Requirements**:
- Save the original state of a list on entry
- Allow modifications within the context
- Rollback to original state if exception occurs
- Print before/after states

**Example**:
```python
data = [1, 2, 3]
try:
    with ListStateTracker(data) as tracked_list:
        tracked_list.append(4)
        raise ValueError("Error!")
except ValueError:
    pass
print(data)  # Should be [1, 2, 3] (rolled back)
```

## Exercise 4: Retry Context Manager (Easy)

Implement a context manager that retries a block of code up to N times on specific exceptions.

**Requirements**:
- Accept max_retries and exception types to catch
- Retry the block on specified exceptions
- Print retry attempts
- Raise exception after max retries exceeded

**Example**:
```python
attempt = 0
with retry_on_exception(max_retries=3, exceptions=(ValueError,)):
    attempt += 1
    if attempt < 3:
        raise ValueError("Not yet")
    print("Success!")
```

## Exercise 5: Environment Variable Context Manager (Easy)

Create a context manager that temporarily sets environment variables and restores them afterward.

**Requirements**:
- Accept a dictionary of environment variables
- Set them on entry
- Restore original values on exit
- Handle variables that didn't exist before

**Example**:
```python
with temp_env({'DEBUG': 'True', 'API_KEY': 'test123'}):
    print(os.environ['DEBUG'])  # True
# Original values restored
```

## Exercise 6: Multi-Lock Context Manager (Medium)

Implement a context manager that acquires multiple threading locks in a deadlock-safe manner (sorted by id).

**Requirements**:
- Accept multiple locks as arguments
- Acquire them in a consistent order (sorted by id)
- Release all locks on exit
- Handle exceptions during lock acquisition

**Example**:
```python
lock1, lock2, lock3 = Lock(), Lock(), Lock()
with MultiLock(lock3, lock1, lock2):
    # All locks acquired safely
    shared_data.update()
# All locks released
```

## Exercise 7: Cache Context Manager (Medium)

Create a context manager that temporarily enables caching for expensive function calls.

**Requirements**:
- Cache function results during context
- Clear cache on exit
- Print cache hit/miss statistics
- Support any callable

**Example**:
```python
def expensive_func(n):
    time.sleep(0.1)
    return n ** 2

with function_cache(expensive_func) as cached_func:
    result1 = cached_func(5)  # Cache miss
    result2 = cached_func(5)  # Cache hit
# Cache cleared, statistics printed
```

## Exercise 8: Database Connection Pool (Medium)

Implement a context manager that manages a pool of database connections.

**Requirements**:
- Create a pool with max_connections limit
- Provide a connection on entry
- Return connection to pool on exit
- Raise error if pool is exhausted
- Track active connections

**Example**:
```python
pool = ConnectionPool(max_connections=3)
with pool.get_connection() as conn:
    conn.execute("SELECT * FROM users")
# Connection returned to pool
```

## Exercise 9: Atomic File Writer (Medium)

Create a context manager that writes to a temporary file and only replaces the target file on successful completion.

**Requirements**:
- Write to temporary file during context
- Move temp file to target only if no exception
- Keep original file if exception occurs
- Use fsync for durability

**Example**:
```python
with AtomicFileWriter('config.json') as f:
    json.dump(config, f)
# File only updated if no exception occurred
```

## Exercise 10: Profiler Context Manager (Medium)

Implement a context manager that profiles code execution and generates a report.

**Requirements**:
- Use cProfile to profile code block
- Generate statistics on exit
- Sort by specified metric (time, calls, cumulative)
- Print top N functions

**Example**:
```python
with profiler(top=5, sort_by='time'):
    # Code to profile
    process_data()
# Profile report printed
```

## Exercise 11: Async Rate Limiter (Hard)

Create an async context manager that implements rate limiting with a token bucket algorithm.

**Requirements**:
- Limit operations to max_rate per second
- Block (await) when rate exceeded
- Use asyncio primitives
- Track and report rate statistics

**Example**:
```python
async with AsyncRateLimiter(max_rate=10) as limiter:
    for i in range(100):
        await limiter.acquire()
        await api_call()
```

## Exercise 12: Transactional Dictionary (Hard)

Implement a context manager that provides transaction support for dictionary operations.

**Requirements**:
- Support nested transactions
- Implement commit and rollback
- Handle isolation between transactions
- Detect conflicts on commit

**Example**:
```python
data = {'balance': 100}
with Transaction(data) as txn:
    txn['balance'] -= 50
    with Transaction(data) as nested_txn:
        nested_txn['balance'] -= 20
        # nested commit
    # outer commit
print(data['balance'])  # 30
```

## Exercise 13: Resource Pool with Priorities (Hard)

Create a context manager for a priority-based resource pool.

**Requirements**:
- Support priority levels (HIGH, NORMAL, LOW)
- Higher priority requests get resources first
- Queue requests when pool exhausted
- Implement timeout for waiting
- Track resource usage statistics

**Example**:
```python
pool = PriorityResourcePool(max_resources=2)
with pool.acquire(priority=Priority.HIGH, timeout=5.0) as resource:
    resource.use()
```

## Exercise 14: Distributed Lock (Hard)

Implement a context manager that implements a distributed lock using file system.

**Requirements**:
- Use file-based locking mechanism
- Handle stale locks (timeout)
- Support lock renewal
- Handle process crashes gracefully
- Work across multiple processes

**Example**:
```python
with DistributedLock('my_resource', timeout=30) as lock:
    # Critical section - only one process can enter
    modify_shared_resource()
```

## Exercise 15: Async Context Manager Chain (Hard)

Create a utility that chains multiple async context managers and manages their lifecycle.

**Requirements**:
- Accept list of async context managers
- Enter all in order
- Exit all in reverse order (LIFO)
- Handle exceptions in any context manager
- Ensure all are cleaned up even if one fails

**Example**:
```python
async with AsyncContextChain([
    AsyncDatabase(),
    AsyncCache(),
    AsyncLogger()
]) as (db, cache, logger):
    await db.query()
    await cache.set('key', 'value')
    await logger.log('Operation complete')
```

