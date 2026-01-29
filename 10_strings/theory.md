# String Processing - Theory

## String Methods

### Case Manipulation
```python
s = "Hello World"
s.upper()           # "HELLO WORLD"
s.lower()           # "hello world"
s.capitalize()      # "Hello world"
s.title()           # "Hello World"
s.swapcase()        # "hELLO wORLD"
s.casefold()        # More aggressive lowercase (for comparisons)
```

### Whitespace Handling
```python
s = "  hello  "
s.strip()           # "hello" (both ends)
s.lstrip()          # "hello  " (left)
s.rstrip()          # "  hello" (right)
s.strip("h")        # Remove specific characters from ends
```

### Searching and Testing
```python
s = "hello world"
s.find("world")         # 6 (returns -1 if not found)
s.index("world")        # 6 (raises ValueError if not found)
s.rfind("o")           # 7 (rightmost occurrence)
s.count("l")           # 3
s.startswith("hello")  # True
s.endswith("world")    # True
```

### String Checks
```python
s = "hello123"
s.isalpha()         # False (contains digits)
s.isdigit()         # False (contains letters)
s.isalnum()         # True (alphanumeric)
s.isspace()         # False
s.isupper()         # False
s.islower()         # True
```

### Splitting and Joining
```python
s = "a,b,c,d"
parts = s.split(",")           # ["a", "b", "c", "d"]
parts = s.split(",", 2)        # ["a", "b", "c,d"] (max splits)
lines = text.splitlines()      # Split by line breaks
words = s.split()              # Split by whitespace (default)

# Joining
",".join(parts)                # "a,b,c,d"
" ".join(["hello", "world"])   # "hello world"
```

### Replacing and Translating
```python
s = "hello world"
s.replace("world", "Python")   # "hello Python"
s.replace("l", "L", 1)         # "heLlo world" (replace first only)

# Translation table
trans = str.maketrans("aeiou", "12345")
s.translate(trans)             # "h2ll4 w4rld"

# Remove characters
trans = str.maketrans("", "", "aeiou")
s.translate(trans)             # "hll wrld"
```

### Alignment and Padding
```python
s = "hello"
s.center(10)        # "  hello   "
s.ljust(10)         # "hello     "
s.rjust(10)         # "     hello"
s.zfill(10)         # "00000hello"
s.center(10, "*")   # "**hello***"
```

### Partitioning
```python
s = "hello:world:python"
s.partition(":")     # ("hello", ":", "world:python")
s.rpartition(":")    # ("hello:world", ":", "python")
```

## Regular Expressions (re module)

### Basic Patterns
```python
import re

# Special characters
.       # Any character except newline
^       # Start of string
$       # End of string
*       # 0 or more repetitions
+       # 1 or more repetitions
?       # 0 or 1 repetition
{m,n}   # m to n repetitions
[]      # Character class
|       # OR operator
()      # Capturing group
\       # Escape special character
```

### Character Classes
```python
\d      # Digit [0-9]
\D      # Non-digit
\w      # Word character [a-zA-Z0-9_]
\W      # Non-word character
\s      # Whitespace
\S      # Non-whitespace
\b      # Word boundary
\B      # Non-word boundary
```

### Common Methods
```python
import re

text = "The price is 100 dollars and 50 cents"

# Search (returns first match or None)
match = re.search(r'\d+', text)
if match:
    print(match.group())  # "100"
    print(match.span())   # (13, 16)

# Match (from start of string)
match = re.match(r'The', text)  # Matches
match = re.match(r'price', text)  # None (not at start)

# Find all
numbers = re.findall(r'\d+', text)  # ["100", "50"]

# Find all with positions
for match in re.finditer(r'\d+', text):
    print(match.group(), match.span())

# Split
parts = re.split(r'\s+', text)  # Split by whitespace

# Replace
new_text = re.sub(r'\d+', 'X', text)  # Replace all digits
new_text = re.sub(r'\d+', lambda m: str(int(m.group()) * 2), text)  # Transform
```

### Groups and Capturing
```python
import re

# Basic groups
text = "John: 25, Jane: 30"
pattern = r'(\w+): (\d+)'

for match in re.finditer(pattern, text):
    name = match.group(1)    # First group
    age = match.group(2)     # Second group
    print(f"{name} is {age}")

# Named groups
pattern = r'(?P<name>\w+): (?P<age>\d+)'
match = re.search(pattern, text)
print(match.group('name'))   # "John"
print(match.groupdict())     # {'name': 'John', 'age': '25'}

# Non-capturing groups
pattern = r'(?:Mr|Ms)\. (\w+)'  # Don't capture Mr/Ms

# Backreferences
pattern = r'(\w+) \1'  # Matches repeated words like "hello hello"
```

### Flags
```python
import re

# Case insensitive
re.search(r'hello', text, re.IGNORECASE)  # or re.I

# Multiline (^ and $ match line starts/ends)
re.search(r'^word', text, re.MULTILINE)   # or re.M

# Dot matches newline
re.search(r'.*', text, re.DOTALL)         # or re.S

# Verbose (allows comments and whitespace)
pattern = re.compile(r'''
    (\d{3})  # Area code
    -        # Separator
    (\d{4})  # Number
''', re.VERBOSE)  # or re.X

# Combine flags
re.search(pattern, text, re.I | re.M)
```

### Lookahead and Lookbehind
```python
# Positive lookahead
r'\d+(?= dollars)'    # Match digits followed by " dollars"

# Negative lookahead
r'\d+(?! dollars)'    # Match digits NOT followed by " dollars"

# Positive lookbehind
r'(?<=\$)\d+'         # Match digits preceded by "$"

# Negative lookbehind
r'(?<!\$)\d+'         # Match digits NOT preceded by "$"
```

### Compiled Patterns
```python
import re

# Compile for reuse (more efficient)
pattern = re.compile(r'\d+')
pattern.search(text)
pattern.findall(text)

# With flags
pattern = re.compile(r'hello', re.I | re.M)
```

## String Formatting

### F-Strings (Python 3.6+)
```python
name = "Alice"
age = 30
pi = 3.14159

# Basic
f"Hello, {name}"                    # "Hello, Alice"

# Expressions
f"{age + 5}"                        # "35"
f"{name.upper()}"                   # "ALICE"

# Format specifications
f"{pi:.2f}"                         # "3.14"
f"{age:05d}"                        # "00030"
f"{1000000:,}"                      # "1,000,000"

# Alignment
f"{name:<10}"                       # "Alice     " (left)
f"{name:>10}"                       # "     Alice" (right)
f"{name:^10}"                       # "  Alice   " (center)

# Padding
f"{name:*^10}"                      # "**Alice***"

# Date/time
from datetime import datetime
now = datetime.now()
f"{now:%Y-%m-%d}"                   # "2024-01-28"

# Debug (Python 3.8+)
x = 10
f"{x=}"                             # "x=10"

# Multiline
message = (
    f"Name: {name}\n"
    f"Age: {age}"
)
```

### format() Method
```python
# Positional
"Hello, {}".format("Alice")
"{0} {1}".format("Hello", "World")
"{1} {0}".format("World", "Hello")  # "Hello World"

# Named
"{name} is {age}".format(name="Alice", age=30)

# With dict
person = {"name": "Alice", "age": 30}
"{name} is {age}".format(**person)

# Format specs
"{:.2f}".format(3.14159)            # "3.14"
"{:05d}".format(42)                 # "00042"
"{:>10}".format("test")             # "      test"
```

### % Formatting (Old Style)
```python
name = "Alice"
age = 30

"Hello, %s" % name                  # "Hello, Alice"
"%s is %d" % (name, age)            # "Alice is 30"
"%.2f" % 3.14159                    # "3.14"
"%10s" % "test"                     # "      test"

# Named
"%(name)s is %(age)d" % {"name": "Alice", "age": 30}
```

### Template Strings
```python
from string import Template

# Safe substitution (no code execution)
t = Template("Hello, $name")
t.substitute(name="Alice")          # "Hello, Alice"

# With braces
t = Template("${name} is ${age}")
t.substitute(name="Alice", age=30)

# Safe substitute (no error if missing)
t = Template("$name $age")
t.safe_substitute(name="Alice")     # "Alice $age"
```

## Text Processing

### textwrap Module
```python
import textwrap

text = "This is a very long line of text that needs to be wrapped."

# Wrap to width
wrapped = textwrap.wrap(text, width=20)
# ["This is a very long", "line of text that", "needs to be wrapped."]

# Fill (wrap and join)
filled = textwrap.fill(text, width=20)

# Indent
indented = textwrap.indent(text, "  ")

# Dedent (remove common leading whitespace)
dedented = textwrap.dedent("""
    Hello
    World
""")

# Shorten
short = textwrap.shorten(text, width=30, placeholder="...")
```

### difflib Module
```python
import difflib

# Similarity ratio
s1 = "hello world"
s2 = "hello word"
ratio = difflib.SequenceMatcher(None, s1, s2).ratio()  # 0.91

# Close matches
possibilities = ["apple", "ape", "apply"]
difflib.get_close_matches("aple", possibilities)  # ["apple", "ape"]

# Unified diff
diff = difflib.unified_diff(
    ["line1\n", "line2\n"],
    ["line1\n", "line2 modified\n"],
    fromfile="old.txt",
    tofile="new.txt"
)

# HTML diff
d = difflib.HtmlDiff()
html = d.make_file(["line1"], ["line2"])
```

### String Module
```python
import string

# Constants
string.ascii_lowercase      # "abcdefghijklmnopqrstuvwxyz"
string.ascii_uppercase      # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string.ascii_letters        # lowercase + uppercase
string.digits              # "0123456789"
string.hexdigits           # "0123456789abcdefABCDEF"
string.octdigits           # "01234567"
string.punctuation         # "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
string.whitespace          # " \t\n\r\v\f"
string.printable           # All printable characters
```

## Unicode and Encoding

### Unicode Basics
```python
# Unicode code points
ord('A')                # 65
chr(65)                 # 'A'
ord('\u03B1')          # 945 (Greek alpha)

# Unicode escapes
'\u03B1'               # α (4-digit hex)
'\U0001F600'           # 😀 (8-digit hex)
'\N{GREEK SMALL LETTER ALPHA}'  # α (name)

# String length vs bytes
s = "hello"
len(s)                 # 5 characters
len(s.encode())        # 5 bytes

s = "αβγ"
len(s)                 # 3 characters
len(s.encode())        # 6 bytes (UTF-8)
```

### Encoding and Decoding
```python
# String to bytes
s = "hello"
b = s.encode('utf-8')          # b'hello'
b = s.encode('ascii')          # b'hello'

# Bytes to string
b = b'hello'
s = b.decode('utf-8')          # "hello"

# Handle errors
s = "hello\xff"
s.encode('ascii', errors='ignore')      # Skip invalid
s.encode('ascii', errors='replace')     # Use ?
s.encode('ascii', errors='backslashreplace')  # Use \xff

# Common encodings
'utf-8'         # Default, variable width
'ascii'         # 7-bit, English only
'latin-1'       # 8-bit, Western European
'utf-16'        # 16-bit minimum
'cp1252'        # Windows encoding
```

### Normalization
```python
import unicodedata

# Different representations of é
s1 = '\u00e9'              # Single character é
s2 = 'e\u0301'             # e + combining accent

s1 == s2                   # False

# Normalize
unicodedata.normalize('NFC', s2) == s1   # True (composed)
unicodedata.normalize('NFD', s1) == s2   # True (decomposed)

# Category
unicodedata.category('A')   # 'Lu' (Letter, uppercase)
unicodedata.category('5')   # 'Nd' (Number, decimal)

# Name
unicodedata.name('α')       # 'GREEK SMALL LETTER ALPHA'
```

### Working with Files
```python
# Read text file
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Write text file
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write("Hello, world!")

# Read binary
with open('file.txt', 'rb') as f:
    bytes_content = f.read()

# Detect encoding (requires chardet package)
import chardet
with open('file.txt', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']
```

## Performance Considerations

### String Concatenation
```python
# Slow (creates new string each time)
result = ""
for i in range(1000):
    result += str(i)

# Fast (join is optimized)
result = "".join(str(i) for i in range(1000))

# For small strings, += is fine
s = "hello"
s += " world"
```

### String Interning
```python
# Python automatically interns some strings
a = "hello"
b = "hello"
a is b                 # True (same object)

# But not all
a = "hello world"
b = "hello world"
a is b                 # False (different objects)
a == b                 # True (same value)
```

### StringBuilder Pattern
```python
# For building strings incrementally
parts = []
for item in items:
    parts.append(process(item))
result = "".join(parts)
```
