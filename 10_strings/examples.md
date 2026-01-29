# String Processing - Practical Examples

## String Manipulation

### Example 1: Text Cleaning
```python
def clean_text(text):
    """Remove extra whitespace and normalize text."""
    # Remove leading/trailing whitespace
    text = text.strip()

    # Replace multiple spaces with single space
    import re
    text = re.sub(r'\s+', ' ', text)

    # Remove special characters (keep alphanumeric and spaces)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    return text.lower()

text = "  Hello,   World!!!  \n  How are   you?  "
print(clean_text(text))  # "hello world how are you"
```

### Example 2: Camel Case to Snake Case
```python
import re

def camel_to_snake(name):
    """Convert CamelCase to snake_case."""
    # Insert underscore before uppercase letters
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # Insert underscore before uppercase letters preceded by lowercase
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

print(camel_to_snake("myVariableName"))    # "my_variable_name"
print(camel_to_snake("HTTPResponseCode"))  # "http_response_code"
print(camel_to_snake("getHTMLContent"))    # "get_html_content"
```

### Example 3: Snake Case to Camel Case
```python
def snake_to_camel(name, capitalize_first=False):
    """Convert snake_case to camelCase."""
    components = name.split('_')
    if capitalize_first:
        return ''.join(x.title() for x in components)
    return components[0] + ''.join(x.title() for x in components[1:])

print(snake_to_camel("my_variable_name"))           # "myVariableName"
print(snake_to_camel("my_variable_name", True))     # "MyVariableName"
```

### Example 4: Word Wrap
```python
def word_wrap(text, width):
    """Wrap text to specified width."""
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        word_length = len(word)
        # +1 for space
        if current_length + word_length + len(current_line) <= width:
            current_line.append(word)
            current_length += word_length
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
            current_length = word_length

    if current_line:
        lines.append(' '.join(current_line))

    return '\n'.join(lines)

text = "This is a long line of text that needs to be wrapped properly."
print(word_wrap(text, 20))
# This is a long line
# of text that needs
# to be wrapped
# properly.
```

### Example 5: Slugify (URL-friendly strings)
```python
import re

def slugify(text):
    """Convert text to URL-friendly slug."""
    # Lowercase
    text = text.lower()
    # Replace spaces and special chars with hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    # Remove leading/trailing hyphens
    return text.strip('-')

print(slugify("Hello World! This is a Test"))  # "hello-world-this-is-a-test"
print(slugify("Python 3.11 - New Features"))   # "python-311-new-features"
```

## Regular Expression Validation

### Example 6: Email Validation
```python
import re

def validate_email(email):
    """Validate email address."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# More comprehensive
def validate_email_strict(email):
    pattern = r'''
        ^                          # Start
        [a-zA-Z0-9._%+-]+          # Username
        @                          # @
        [a-zA-Z0-9.-]+             # Domain
        \.                         # Dot
        [a-zA-Z]{2,}               # TLD
        $                          # End
    '''
    return re.match(pattern, email, re.VERBOSE) is not None

print(validate_email("user@example.com"))      # True
print(validate_email("invalid.email"))         # False
print(validate_email("user@domain"))           # False
```

### Example 7: Phone Number Validation
```python
import re

def validate_phone(phone):
    """Validate US phone numbers in various formats."""
    patterns = [
        r'^\d{10}$',                          # 1234567890
        r'^\d{3}-\d{3}-\d{4}$',              # 123-456-7890
        r'^\(\d{3}\)\s?\d{3}-\d{4}$',        # (123) 456-7890
        r'^\+1\s?\d{3}\s?\d{3}\s?\d{4}$',    # +1 123 456 7890
    ]
    return any(re.match(pattern, phone) for pattern in patterns)

def normalize_phone(phone):
    """Extract and format phone number."""
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits[0] == '1':
        return f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    return None

print(validate_phone("123-456-7890"))    # True
print(validate_phone("(123) 456-7890"))  # True
print(normalize_phone("1234567890"))     # "(123) 456-7890"
print(normalize_phone("+1-123-456-7890")) # "+1 (123) 456-7890"
```

### Example 8: URL Validation and Parsing
```python
import re

def validate_url(url):
    """Validate URL format."""
    pattern = r'''
        ^
        (https?://)?                           # Protocol (optional)
        (www\.)?                               # www (optional)
        [a-zA-Z0-9-]+                          # Domain name
        (\.[a-zA-Z]{2,})+                      # TLD
        (/[a-zA-Z0-9-._~:/?#[\]@!$&'()*+,;=]*)? # Path (optional)
        $
    '''
    return re.match(pattern, url, re.VERBOSE) is not None

def parse_url(url):
    """Extract components from URL."""
    pattern = r'''
        ^
        (?P<protocol>https?://)?
        (?P<subdomain>www\.)?
        (?P<domain>[a-zA-Z0-9-]+)
        (?P<tld>\.[a-zA-Z]{2,}+)
        (?P<path>/.*)?
        $
    '''
    match = re.match(pattern, url, re.VERBOSE)
    return match.groupdict() if match else None

print(validate_url("https://www.example.com/path"))  # True
print(parse_url("https://www.example.com/path"))
# {'protocol': 'https://', 'subdomain': 'www.',
#  'domain': 'example', 'tld': '.com', 'path': '/path'}
```

### Example 9: Password Strength Validation
```python
import re

def validate_password(password):
    """
    Validate password strength:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters"

    if not re.search(r'[A-Z]', password):
        return False, "Password must contain uppercase letter"

    if not re.search(r'[a-z]', password):
        return False, "Password must contain lowercase letter"

    if not re.search(r'\d', password):
        return False, "Password must contain digit"

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain special character"

    return True, "Password is strong"

def password_strength(password):
    """Calculate password strength score."""
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    return score

print(validate_password("Pass123!"))     # (True, "Password is strong")
print(password_strength("Password123!")) # 6 (very strong)
```

### Example 10: Extract Information with Regex
```python
import re

def extract_dates(text):
    """Extract dates in various formats."""
    patterns = [
        r'\d{2}/\d{2}/\d{4}',        # MM/DD/YYYY
        r'\d{4}-\d{2}-\d{2}',        # YYYY-MM-DD
        r'\d{2}\.\d{2}\.\d{4}',      # DD.MM.YYYY
    ]
    dates = []
    for pattern in patterns:
        dates.extend(re.findall(pattern, text))
    return dates

def extract_emails(text):
    """Extract all email addresses."""
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(pattern, text)

def extract_hashtags(text):
    """Extract hashtags from text."""
    return re.findall(r'#\w+', text)

text = """
Meeting on 01/15/2024 or 2024-01-15.
Contact: john@example.com or jane@test.org
Topics: #python #programming #regex
"""

print(extract_dates(text))      # ["01/15/2024", "2024-01-15"]
print(extract_emails(text))     # ["john@example.com", "jane@test.org"]
print(extract_hashtags(text))   # ["#python", "#programming", "#regex"]
```

## Parsing Text Files

### Example 11: CSV-like Data
```python
def parse_csv_line(line, delimiter=','):
    """Parse CSV line handling quoted values."""
    pattern = f'{delimiter}(?=(?:[^"]*"[^"]*")*[^"]*$)'
    fields = re.split(pattern, line)
    return [field.strip().strip('"') for field in fields]

line = 'John Doe,30,"New York, NY",Engineer'
print(parse_csv_line(line))
# ['John Doe', '30', 'New York, NY', 'Engineer']
```

### Example 12: Log File Parsing
```python
import re
from datetime import datetime

def parse_log_line(line):
    """Parse Apache-style log line."""
    pattern = r'(\S+) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+)'
    match = re.match(pattern, line)

    if match:
        ip, timestamp, request, status, size = match.groups()
        return {
            'ip': ip,
            'timestamp': datetime.strptime(timestamp, '%d/%b/%Y:%H:%M:%S %z'),
            'request': request,
            'status': int(status),
            'size': int(size)
        }
    return None

log = '192.168.1.1 - - [28/Jan/2024:10:15:30 +0000] "GET /index.html HTTP/1.1" 200 1234'
print(parse_log_line(log))
# {'ip': '192.168.1.1', 'timestamp': datetime(...),
#  'request': 'GET /index.html HTTP/1.1', 'status': 200, 'size': 1234}
```

### Example 13: Configuration File Parser
```python
import re

def parse_config(text):
    """Parse simple INI-style config file."""
    config = {}
    current_section = None

    for line in text.split('\n'):
        line = line.strip()

        # Skip empty lines and comments
        if not line or line.startswith('#'):
            continue

        # Section header [section]
        section_match = re.match(r'\[(\w+)\]', line)
        if section_match:
            current_section = section_match.group(1)
            config[current_section] = {}
            continue

        # Key = value
        kv_match = re.match(r'(\w+)\s*=\s*(.+)', line)
        if kv_match and current_section:
            key, value = kv_match.groups()
            config[current_section][key] = value.strip()

    return config

config_text = """
[database]
host = localhost
port = 5432

[app]
name = MyApp
debug = true
"""

print(parse_config(config_text))
# {'database': {'host': 'localhost', 'port': '5432'},
#  'app': {'name': 'MyApp', 'debug': 'true'}}
```

### Example 14: Markdown Parser
```python
import re

def parse_markdown_headers(text):
    """Extract headers from markdown text."""
    pattern = r'^(#{1,6})\s+(.+)$'
    headers = []

    for line in text.split('\n'):
        match = re.match(pattern, line)
        if match:
            level = len(match.group(1))
            title = match.group(2)
            headers.append({'level': level, 'title': title})

    return headers

markdown = """
# Main Title
## Section 1
### Subsection 1.1
## Section 2
"""

print(parse_markdown_headers(markdown))
# [{'level': 1, 'title': 'Main Title'},
#  {'level': 2, 'title': 'Section 1'}, ...]
```

## String Formatting

### Example 15: Table Formatting
```python
def format_table(data, headers):
    """Format data as aligned table."""
    # Calculate column widths
    widths = [len(h) for h in headers]
    for row in data:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    # Format header
    header_line = ' | '.join(h.ljust(w) for h, w in zip(headers, widths))
    separator = '-+-'.join('-' * w for w in widths)

    # Format rows
    rows = []
    for row in data:
        row_line = ' | '.join(str(cell).ljust(w) for cell, w in zip(row, widths))
        rows.append(row_line)

    return '\n'.join([header_line, separator] + rows)

headers = ['Name', 'Age', 'City']
data = [
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

print(format_table(data, headers))
# Name    | Age | City
# --------+-----+------------
# Alice   | 30  | New York
# Bob     | 25  | Los Angeles
# Charlie | 35  | Chicago
```

### Example 16: Pretty Print Numbers
```python
def format_number(n):
    """Format number with thousand separators."""
    return f"{n:,}"

def format_currency(amount, symbol='$'):
    """Format amount as currency."""
    return f"{symbol}{amount:,.2f}"

def format_percentage(value, decimals=2):
    """Format value as percentage."""
    return f"{value:.{decimals}%}"

def format_filesize(bytes_size):
    """Format bytes as human-readable size."""
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = float(bytes_size)
    unit_idx = 0

    while size >= 1024 and unit_idx < len(units) - 1:
        size /= 1024
        unit_idx += 1

    return f"{size:.2f} {units[unit_idx]}"

print(format_number(1234567))           # "1,234,567"
print(format_currency(1234.56))         # "$1,234.56"
print(format_percentage(0.1234))        # "12.34%"
print(format_filesize(1536000))         # "1.46 MB"
```

## Text Diff and Comparison

### Example 17: Simple Diff
```python
import difflib

def show_diff(text1, text2):
    """Show differences between two texts."""
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()

    diff = difflib.unified_diff(
        lines1, lines2,
        lineterm='',
        fromfile='original',
        tofile='modified'
    )

    return '\n'.join(diff)

text1 = """Line 1
Line 2
Line 3"""

text2 = """Line 1
Line 2 modified
Line 3
Line 4"""

print(show_diff(text1, text2))
```

### Example 18: Find Similar Strings
```python
import difflib

def find_similar(word, candidates, n=3, cutoff=0.6):
    """Find similar strings from candidates."""
    return difflib.get_close_matches(word, candidates, n=n, cutoff=cutoff)

def string_similarity(s1, s2):
    """Calculate similarity ratio between strings."""
    return difflib.SequenceMatcher(None, s1, s2).ratio()

words = ['apple', 'application', 'apricot', 'banana', 'orange']
print(find_similar('aple', words))      # ['apple', 'apricot']
print(string_similarity('hello', 'hallo'))  # 0.8
```

### Example 19: Spell Checker (Simple)
```python
import difflib

class SimpleSpellChecker:
    def __init__(self, dictionary):
        self.dictionary = set(word.lower() for word in dictionary)

    def check(self, word):
        """Check if word is in dictionary."""
        return word.lower() in self.dictionary

    def suggest(self, word, max_suggestions=5):
        """Suggest corrections for misspelled word."""
        if self.check(word):
            return []

        return difflib.get_close_matches(
            word.lower(),
            self.dictionary,
            n=max_suggestions,
            cutoff=0.6
        )

dictionary = ['hello', 'world', 'python', 'programming', 'computer']
checker = SimpleSpellChecker(dictionary)

print(checker.check('python'))          # True
print(checker.check('pyton'))           # False
print(checker.suggest('pyton'))         # ['python']
print(checker.suggest('programing'))    # ['programming']
```

### Example 20: Text Sanitization
```python
import re
import html

def sanitize_html(text):
    """Remove HTML tags and decode entities."""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Decode HTML entities
    text = html.unescape(text)
    return text

def sanitize_sql(text):
    """Escape single quotes for SQL."""
    return text.replace("'", "''")

def sanitize_filename(filename):
    """Create safe filename."""
    # Remove invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Replace spaces with underscores
    filename = filename.replace(' ', '_')
    # Limit length
    name, ext = filename.rsplit('.', 1) if '.' in filename else (filename, '')
    if len(name) > 200:
        name = name[:200]
    return f"{name}.{ext}" if ext else name

html_text = "<p>Hello &amp; welcome!</p>"
print(sanitize_html(html_text))         # "Hello & welcome!"

print(sanitize_sql("O'Reilly"))         # "O''Reilly"

print(sanitize_filename("file:name?.txt"))  # "filename.txt"
```
