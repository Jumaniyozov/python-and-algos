# Control Flow: Tips, Tricks, and Gotchas

## Conditional Tips

### Tip 1: Use Truthy/Falsy Idiomatically

**Good**:
```python
if items:
    process(items)

if not errors:
    continue_processing()
```

**Avoid**:
```python
if len(items) > 0:  # Verbose
    process(items)

if errors == []:  # Explicit but not Pythonic
    continue_processing()
```

### Tip 2: Ternary for Simple Conditionals

**Good**:
```python
status = "adult" if age >= 18 else "minor"
```

**Avoid** (when ternary is better):
```python
if age >= 18:
    status = "adult"
else:
    status = "minor"
```

### Gotcha 1: Chained Comparisons

```python
# Works!
if 0 < x < 10:
    print("x is between 0 and 10")

# Equivalent to
if 0 < x and x < 10:
    pass

# Be careful with logic
if x < y < z:  # y is between x and z
    pass
```

## Loop Tips

### Tip 1: enumerate() for Index and Value

**Good**:
```python
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

**Avoid**:
```python
for i in range(len(items)):
    print(f"{i}: {items[i]}")
```

### Tip 2: zip() for Parallel Iteration

```python
names = ["Alice", "Bob"]
ages = [30, 25]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

### Tip 3: dict.items() for Dictionaries

**Good**:
```python
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

**Avoid**:
```python
for key in my_dict:
    value = my_dict[key]
    print(f"{key}: {value}")
```

### Gotcha 1: Modifying List While Iterating

**Wrong**:
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Bad! Skips elements
```

**Right**:
```python
# Create new list
numbers = [num for num in numbers if num % 2 != 0]

# Or iterate over copy
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)
```

### Gotcha 2: Loop else Clause

```python
# else runs if NO break
for item in items:
    if condition:
        break
else:
    print("No break occurred")  # Runs if loop completes
```

## Exception Handling Tips

### Tip 1: Be Specific with Exceptions

**Good**:
```python
try:
    value = int(user_input)
except ValueError:
    print("Invalid number")
```

**Avoid**:
```python
try:
    value = int(user_input)
except:  # Too broad!
    print("Error")
```

### Tip 2: Use finally for Cleanup

```python
file = None
try:
    file = open("data.txt")
    process(file)
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()  # Always executes
```

### Tip 3: Context Managers Over try/finally

**Better**:
```python
with open("data.txt") as f:
    process(f)
```

**Instead of**:
```python
f = open("data.txt")
try:
    process(f)
finally:
    f.close()
```

### Gotcha 1: Catching Too Much

```python
# Bad - catches SystemExit, KeyboardInterrupt
try:
    run_server()
except:
    pass

# Good
try:
    run_server()
except Exception as e:
    log_error(e)
```

### Gotcha 2: Empty except Blocks

**Avoid**:
```python
try:
    risky_operation()
except ValueError:
    pass  # Silent failure - hard to debug
```

**Better**:
```python
try:
    risky_operation()
except ValueError as e:
    logger.error(f"Operation failed: {e}")
```

## Pattern Matching Tips (Python 3.10+)

### Tip 1: Use Guards for Complex Conditions

```python
match point:
    case (x, y) if x == y:
        print("On diagonal")
    case (x, y):
        print("Regular point")
```

### Tip 2: Capture with _ for Wildcards

```python
match command:
    case ["load", filename]:
        load_file(filename)
    case ["save", filename, _]:  # Ignore third arg
        save_file(filename)
```

### Tip 3: Combine Patterns with |

```python
match status_code:
    case 200 | 201 | 204:
        return "Success"
    case 400 | 401 | 403 | 404:
        return "Client Error"
```

## Context Manager Tips

### Tip 1: Multiple Context Managers

```python
with open("in.txt") as infile, open("out.txt", "w") as outfile:
    outfile.write(infile.read())
```

### Tip 2: Suppress Exceptions

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("temp.txt")  # No error if file doesn't exist
```

### Tip 3: ExitStack for Dynamic Resources

```python
from contextlib import ExitStack

with ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in filenames]
    # Process all files
    # All automatically closed
```

## Performance Tips

### Tip 1: Use any() and all()

**Efficient**:
```python
has_even = any(x % 2 == 0 for x in numbers)
all_positive = all(x > 0 for x in numbers)
```

**Inefficient**:
```python
has_even = False
for x in numbers:
    if x % 2 == 0:
        has_even = True
        break
```

### Tip 2: Short-Circuit Evaluation

```python
# Checks expensive_check() only if cheap_check() is True
if cheap_check() and expensive_check():
    do_something()
```

## Common Patterns

### Pattern 1: Safe Dictionary Access

```python
# EAFP (Easier to Ask Forgiveness than Permission)
try:
    value = my_dict[key]
except KeyError:
    value = default

# LBYL (Look Before You Leap)
if key in my_dict:
    value = my_dict[key]
else:
    value = default

# Best: use get()
value = my_dict.get(key, default)
```

### Pattern 2: Retry Logic

```python
max_retries = 3
for attempt in range(max_retries):
    try:
        result = risky_operation()
        break
    except TransientError:
        if attempt == max_retries - 1:
            raise
        time.sleep(2 ** attempt)  # Exponential backoff
```

### Pattern 3: Validation Chain

```python
def validate(data):
    if not data:
        return False, "Empty data"
    if "name" not in data:
        return False, "Missing name"
    if len(data["name"]) < 3:
        return False, "Name too short"
    return True, "Valid"
```

## Summary

**Do**:
- ✅ Use truthy/falsy values idiomatically
- ✅ Use enumerate() and zip() for iteration
- ✅ Be specific with exception types
- ✅ Use context managers for resources
- ✅ Use pattern matching (Python 3.10+) for complex conditionals

**Don't**:
- ❌ Modify collections while iterating
- ❌ Use bare except
- ❌ Ignore exceptions silently
- ❌ Forget to clean up resources
- ❌ Over-complicate simple conditionals

See examples.md for practical applications!
