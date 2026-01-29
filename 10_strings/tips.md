# String Processing - Tips and Best Practices

## General String Tips

### Immutability Matters
```python
# Bad: Inefficient string concatenation in loop
result = ""
for i in range(1000):
    result += str(i)  # Creates new string each iteration

# Good: Use join for multiple concatenations
result = ''.join(str(i) for i in range(1000))

# Good: Use list for building strings
parts = []
for i in range(1000):
    parts.append(str(i))
result = ''.join(parts)
```

### String Comparison
```python
# Use == for value comparison
s1 = "hello"
s2 = "hello"
s1 == s2  # True (compare values)

# Don't use 'is' for string comparison (checks identity)
s1 is s2  # May be True or False (implementation-dependent)

# Case-insensitive comparison
s1.lower() == s2.lower()
# Or use casefold() for international text
s1.casefold() == s2.casefold()
```

### String Checking
```python
# Prefer str methods over manual checks
# Bad
if s != "":
    pass

# Good
if s:
    pass

# Check prefixes/suffixes
# Bad
if s[:5] == "hello":
    pass

# Good
if s.startswith("hello"):
    pass
```

### String Formatting
```python
# Modern: Use f-strings (Python 3.6+)
name = "Alice"
age = 30
message = f"{name} is {age} years old"

# For templates with unknown values, use format()
template = "{name} is {age} years old"
message = template.format(name=name, age=age)

# Avoid % formatting (old style)
message = "%s is %d years old" % (name, age)  # Don't use
```

## Regular Expression Tips

### Compile Patterns for Reuse
```python
import re

# Bad: Compiling pattern every time
for text in texts:
    if re.match(r'\d+', text):
        pass

# Good: Compile once, reuse
pattern = re.compile(r'\d+')
for text in texts:
    if pattern.match(text):
        pass
```

### Use Raw Strings
```python
# Bad: Need to escape backslashes
pattern = "\\d+\\s*\\w+"

# Good: Use raw strings
pattern = r"\d+\s*\w+"
```

### Be Specific with Patterns
```python
# Bad: Too greedy
pattern = r'<.*>'  # Matches from first < to last >

# Good: Non-greedy
pattern = r'<.*?>'  # Matches each tag separately

# Better: Be specific
pattern = r'<[^>]+>'  # Match anything except >
```

### Use Non-Capturing Groups When Possible
```python
# If you don't need to capture, use (?:...)
# Less memory and faster

# Bad: Unnecessary capturing
pattern = r'(https?)://(\w+)\.(\w+)'

# Good: Only capture what you need
pattern = r'(https?)://(?:\w+)\.(\w+)'
```

### Verbose Mode for Complex Patterns
```python
import re

# Hard to read
pattern = r'^(\d{3})-(\d{3})-(\d{4})$'

# Better: Use verbose mode with comments
pattern = re.compile(r'''
    ^               # Start of string
    (\d{3})         # Area code
    -               # Separator
    (\d{3})         # Prefix
    -               # Separator
    (\d{4})         # Line number
    $               # End of string
''', re.VERBOSE)
```

### Common Pattern Gotchas
```python
# Gotcha: . doesn't match newline by default
text = "line1\nline2"
re.search(r'line1.line2', text)  # None

# Solution: Use DOTALL flag or \s
re.search(r'line1.line2', text, re.DOTALL)  # Matches
re.search(r'line1\s+line2', text)  # Matches

# Gotcha: ^ and $ match string start/end by default
text = "line1\nline2"
re.findall(r'^line', text)  # Finds only first line

# Solution: Use MULTILINE flag for line-by-line
re.findall(r'^line', text, re.MULTILINE)  # Finds both
```

### Escaping Special Characters
```python
import re

# Bad: Forget to escape
pattern = "test."  # . matches any character

# Good: Escape special characters
pattern = r"test\."

# Better: Use re.escape for user input
user_input = "test.file.txt"
pattern = re.escape(user_input)  # Escapes all special chars
```

## Performance Tips

### String Operations
```python
# Fast: String methods are optimized in C
s.startswith("prefix")
s.endswith("suffix")
s.find("substring")

# Slower: Manual iteration
all(s[i] == prefix[i] for i in range(len(prefix)))
```

### Substring Search
```python
# Fast: Use 'in' operator
if "substring" in text:
    pass

# Fast: Use str.find() to get position
pos = text.find("substring")

# Slower: Use regex for simple substring
import re
if re.search("substring", text):
    pass
```

### String Building
```python
import time

# Slow: Repeated concatenation
start = time.time()
result = ""
for i in range(10000):
    result += str(i)
print(f"Concatenation: {time.time() - start:.4f}s")

# Fast: Join
start = time.time()
result = ''.join(str(i) for i in range(10000))
print(f"Join: {time.time() - start:.4f}s")

# Fast: f-string with join for formatted strings
numbers = range(100)
result = '\n'.join(f"Number: {n}" for n in numbers)
```

### Splitting Strings
```python
# For simple splits, str.split() is faster than regex
# Fast
parts = text.split(',')

# Slower
import re
parts = re.split(',', text)

# But regex is better for complex patterns
parts = re.split(r'[,;:\s]+', text)  # Split by multiple delimiters
```

## Unicode and Encoding Tips

### Always Specify Encoding
```python
# Bad: Uses system default encoding
with open('file.txt', 'r') as f:
    content = f.read()

# Good: Explicit encoding
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

### Handle Encoding Errors
```python
# Strict (default): Raises exception on error
text.encode('ascii')  # UnicodeEncodeError if non-ASCII

# Ignore: Skip invalid characters
text.encode('ascii', errors='ignore')

# Replace: Use replacement character
text.encode('ascii', errors='replace')

# Backslashreplace: Use escape sequences
text.encode('ascii', errors='backslashreplace')
```

### Normalize Unicode
```python
import unicodedata

# Different representations of same character
s1 = '\u00e9'  # é (precomposed)
s2 = 'e\u0301'  # é (e + combining accent)

# They look the same but aren't equal
s1 == s2  # False

# Normalize for comparison
unicodedata.normalize('NFC', s1) == unicodedata.normalize('NFC', s2)  # True
```

### String vs Bytes
```python
# String: Unicode text
text = "hello"
type(text)  # str

# Bytes: Raw binary data
data = b"hello"
type(data)  # bytes

# Convert between them
text.encode('utf-8')  # str -> bytes
data.decode('utf-8')  # bytes -> str

# Don't mix them
text + data  # TypeError
```

## Common Pitfalls

### Mutable Default Arguments
```python
# Bad: Mutable default
def process_text(text, replacements={}):  # Don't do this!
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# Good: Use None as default
def process_text(text, replacements=None):
    if replacements is None:
        replacements = {}
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text
```

### String Comparison Case Sensitivity
```python
# Case-sensitive by default
"Hello" == "hello"  # False

# Case-insensitive comparison
"Hello".lower() == "hello".lower()  # True

# For internationalization
"Straße".casefold() == "strasse".casefold()  # True
```

### Empty String vs None
```python
# Empty string is truthy in boolean context
s = ""
if s:  # False
    pass

# Check explicitly if you need to distinguish
if s is None:
    pass
if s == "":
    pass
if not s:  # True for both None and ""
    pass
```

### String Interpolation Security
```python
# Dangerous: SQL injection
username = "admin' OR '1'='1"
query = f"SELECT * FROM users WHERE username = '{username}'"
# Results in: SELECT * FROM users WHERE username = 'admin' OR '1'='1'

# Safe: Use parameterized queries
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
```

### Regex Catastrophic Backtracking
```python
import re

# Dangerous: Catastrophic backtracking
# Pattern: (a+)+b
# Text: "aaaaaaaaaaaaaaaaaac"
# This can take exponential time!

# Safe: Be specific, avoid nested quantifiers
pattern = r'a+b'  # Instead of (a+)+b
```

## Best Practices

### 1. Choose the Right Tool
```python
# Use string methods for simple operations
text.startswith("prefix")
text.replace("old", "new")

# Use regex for pattern matching
re.search(r'\d{3}-\d{4}', text)

# Use parsing libraries for complex formats
import json
data = json.loads(json_string)
```

### 2. Validate Input Early
```python
def process_email(email):
    # Validate at the start
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValueError("Invalid email format")

    # Process knowing input is valid
    username, domain = email.split('@')
    return username, domain
```

### 3. Use Constants for Repeated Patterns
```python
# Bad: Pattern scattered throughout code
re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email1)
re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email2)

# Good: Define once, reuse
EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
EMAIL_PATTERN.match(email1)
EMAIL_PATTERN.match(email2)
```

### 4. Document Complex Patterns
```python
# Document what the pattern matches
EMAIL_PATTERN = re.compile(r'''
    ^                          # Start of string
    [a-zA-Z0-9._%+-]+          # Username: letters, digits, and special chars
    @                          # Literal @ symbol
    [a-zA-Z0-9.-]+             # Domain: letters, digits, dots, hyphens
    \.                         # Literal dot
    [a-zA-Z]{2,}               # TLD: at least 2 letters
    $                          # End of string
''', re.VERBOSE)
```

### 5. Handle Edge Cases
```python
def word_count(text):
    """Count words in text."""
    # Handle None
    if text is None:
        return 0

    # Handle empty string
    if not text:
        return 0

    # Handle normal case
    return len(text.split())
```

### 6. Use Type Hints
```python
import re
from typing import Optional, List

def extract_emails(text: str) -> List[str]:
    """Extract all email addresses from text."""
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(pattern, text)

def validate_email(email: str) -> bool:
    """Check if email is valid."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

### 7. Test Thoroughly
```python
# Test normal cases
assert word_count("hello world") == 2

# Test edge cases
assert word_count("") == 0
assert word_count(None) == 0
assert word_count("   ") == 0

# Test special characters
assert word_count("hello, world!") == 2

# Test unicode
assert word_count("hello мир") == 2
```

## String Security

### SQL Injection Prevention
```python
# Never do this
username = input("Username: ")
query = f"SELECT * FROM users WHERE username = '{username}'"

# Always use parameterized queries
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
```

### XSS Prevention
```python
import html

user_input = "<script>alert('XSS')</script>"

# Escape HTML
safe_output = html.escape(user_input)
# Result: &lt;script&gt;alert('XSS')&lt;/script&gt;
```

### Path Traversal Prevention
```python
import os

# Dangerous
filename = "../../../etc/passwd"
path = f"/app/uploads/{filename}"  # Could escape directory

# Safe: Normalize and validate path
from pathlib import Path

def safe_path(filename):
    base_dir = Path("/app/uploads")
    target = (base_dir / filename).resolve()

    # Ensure path is within base directory
    if not target.is_relative_to(base_dir):
        raise ValueError("Invalid path")

    return target
```

### Command Injection Prevention
```python
import subprocess

# Dangerous
filename = "file.txt; rm -rf /"
os.system(f"cat {filename}")  # Never do this!

# Safe: Use list arguments
subprocess.run(["cat", filename])
```
