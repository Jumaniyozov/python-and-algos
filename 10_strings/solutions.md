# String Processing - Solutions

## Basic String Operations

### Solution 1: Palindrome Checker
```python
import re

def is_palindrome(s):
    """Check if string is palindrome."""
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Check if string equals its reverse
    return cleaned == cleaned[::-1]

# Alternative without regex
def is_palindrome_alt(s):
    """Check if string is palindrome (alternative)."""
    # Filter alphanumeric and lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Two pointer approach
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

# Test cases
print(is_palindrome("racecar"))                    # True
print(is_palindrome("A man a plan a canal Panama")) # True
print(is_palindrome("hello"))                      # False
```

### Solution 2: Character Frequency
```python
def char_frequency(s):
    """Count frequency of each character."""
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Alternative using Counter
from collections import Counter

def char_frequency_alt(s):
    """Count frequency using Counter."""
    return dict(Counter(s))

# Alternative using defaultdict
from collections import defaultdict

def char_frequency_defaultdict(s):
    """Count frequency using defaultdict."""
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    return dict(freq)

# Test cases
print(char_frequency("hello"))   # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(char_frequency("aabbcc"))  # {'a': 2, 'b': 2, 'c': 2}
```

### Solution 3: Title Case Converter
```python
def smart_title_case(s):
    """Convert to title case with exceptions."""
    # Words to keep lowercase (unless first word)
    exceptions = {'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor',
                  'on', 'at', 'to', 'from', 'by', 'of', 'in'}

    words = s.lower().split()
    result = []

    for i, word in enumerate(words):
        # Always capitalize first word or non-exception words
        if i == 0 or word not in exceptions:
            result.append(word.capitalize())
        else:
            result.append(word)

    return ' '.join(result)

# Test cases
print(smart_title_case("the lord of the rings"))   # "The Lord of the Rings"
print(smart_title_case("a tale of two cities"))    # "A Tale of Two Cities"
print(smart_title_case("to kill a mockingbird"))   # "To Kill a Mockingbird"
```

### Solution 4: Reverse Words
```python
def reverse_words(s):
    """Reverse order of words in string."""
    return ' '.join(s.split()[::-1])

# Alternative with manual loop
def reverse_words_alt(s):
    """Reverse order of words (alternative)."""
    words = s.split()
    left, right = 0, len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    return ' '.join(words)

# Test cases
print(reverse_words("hello world"))         # "world hello"
print(reverse_words("the quick brown fox")) # "fox brown quick the"
```

### Solution 5: Remove Duplicates
```python
def remove_consecutive_duplicates(s):
    """Remove consecutive duplicate characters."""
    if not s:
        return s

    result = [s[0]]
    for char in s[1:]:
        if char != result[-1]:
            result.append(char)

    return ''.join(result)

# Alternative using regex
import re

def remove_consecutive_duplicates_regex(s):
    """Remove consecutive duplicates using regex."""
    return re.sub(r'(.)\1+', r'\1', s)

# Test cases
print(remove_consecutive_duplicates("hello"))       # "helo"
print(remove_consecutive_duplicates("aaabbbccc"))   # "abc"
print(remove_consecutive_duplicates("aabbccaabb"))  # "abcab"
```

## Regular Expressions

### Solution 6: Username Validator
```python
import re

def validate_username(username):
    """Validate username format."""
    # Pattern explanation:
    # ^        - Start of string
    # [a-zA-Z] - Must start with letter
    # [a-zA-Z0-9_-]{2,15} - 2-15 more chars (letters, digits, _, -)
    # (?<![_-]) - Must not end with _ or - (negative lookbehind)
    # $        - End of string
    pattern = r'^[a-zA-Z][a-zA-Z0-9_-]{2,15}(?<![_-])$'
    return re.match(pattern, username) is not None

# Alternative without lookbehind
def validate_username_alt(username):
    """Validate username (alternative)."""
    if len(username) < 3 or len(username) > 16:
        return False
    if not username[0].isalpha():
        return False
    if username[-1] in '_-':
        return False
    return all(c.isalnum() or c in '_-' for c in username)

# Test cases
print(validate_username("john_doe"))   # True
print(validate_username("user123"))    # True
print(validate_username("ab"))         # False (too short)
print(validate_username("user-"))      # False (ends with hyphen)
print(validate_username("123user"))    # False (starts with number)
```

### Solution 7: Extract Quoted Text
```python
import re

def extract_quotes(text):
    """Extract all quoted text."""
    # Match text within single or double quotes
    pattern = r'["\']([^"\']+)["\']'
    return re.findall(pattern, text)

# More robust version handling escaped quotes
def extract_quotes_robust(text):
    """Extract quoted text handling escapes."""
    # Match double-quoted text
    double = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', text)
    # Match single-quoted text
    single = re.findall(r"'([^'\\]*(?:\\.[^'\\]*)*)'", text)
    return double + single

# Test cases
print(extract_quotes('He said "hello" and she said "world"'))  # ["hello", "world"]
print(extract_quotes("It's a 'beautiful' day"))                # ["beautiful"]
```

### Solution 8: Credit Card Masking
```python
import re

def mask_credit_card(card_number):
    """Mask credit card number."""
    # Remove all non-digits to get pure number
    digits = re.sub(r'\D', '', card_number)

    if len(digits) < 4:
        return card_number

    # Keep last 4 digits, mask the rest
    masked_digits = '*' * (len(digits) - 4) + digits[-4:]

    # Preserve original format
    result = []
    digit_index = 0
    for char in card_number:
        if char.isdigit():
            result.append(masked_digits[digit_index])
            digit_index += 1
        else:
            result.append(char)

    return ''.join(result)

# Simpler version without format preservation
def mask_credit_card_simple(card_number):
    """Mask credit card (simple version)."""
    digits = re.sub(r'\D', '', card_number)
    return '*' * (len(digits) - 4) + digits[-4:]

# Test cases
print(mask_credit_card("1234-5678-9012-3456"))  # "****-****-****-3456"
print(mask_credit_card("1234567890123456"))     # "************3456"
```

### Solution 9: Parse HTML Tags
```python
import re

def extract_html_tags(html):
    """Extract HTML tag names."""
    # Match opening and closing tags
    pattern = r'</?(\w+)[^>]*>'
    return re.findall(pattern, html)

# Alternative to get only unique tags
def extract_html_tags_unique(html):
    """Extract unique HTML tag names."""
    pattern = r'</?(\w+)[^>]*>'
    return list(set(re.findall(pattern, html)))

# Test cases
print(extract_html_tags("<div><p>Hello</p></div>"))
# ["div", "p", "p", "div"]

print(extract_html_tags("<a href='#'><img src='pic.jpg'></a>"))
# ["a", "img", "a"]
```

### Solution 10: Time Format Converter
```python
import re

def convert_to_24h(time_str):
    """Convert 12-hour time to 24-hour format."""
    # Parse time components
    pattern = r'(\d{1,2}):(\d{2})\s*(AM|PM)'
    match = re.match(pattern, time_str, re.IGNORECASE)

    if not match:
        return None

    hour, minute, period = match.groups()
    hour = int(hour)
    period = period.upper()

    # Convert to 24-hour
    if period == 'AM':
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02d}:{minute}"

# Test cases
print(convert_to_24h("12:00 AM"))  # "00:00"
print(convert_to_24h("12:00 PM"))  # "12:00"
print(convert_to_24h("11:30 PM"))  # "23:30"
print(convert_to_24h("01:45 AM"))  # "01:45"
print(convert_to_24h("03:15 PM"))  # "15:15"
```

## Text Processing

### Solution 11: Word Count
```python
import re

def word_count(text):
    """Count words in text."""
    # Split by non-word characters
    words = re.findall(r'\b\w+\b', text)
    return len(words)

# Alternative using split
def word_count_alt(text):
    """Count words (alternative)."""
    # Remove punctuation and split
    cleaned = re.sub(r'[^\w\s]', ' ', text)
    words = cleaned.split()
    return len(words)

# Test cases
print(word_count("Hello, world!"))              # 2
print(word_count("one two three"))              # 3
print(word_count("don't count-this as multiple")) # 4
```

### Solution 12: Expand Ranges
```python
def expand_ranges(s):
    """Expand range notation to individual values."""
    parts = s.split(',')
    result = []

    for part in parts:
        part = part.strip()
        if '-' in part:
            # Range notation
            start, end = map(int, part.split('-'))
            result.extend(range(start, end + 1))
        else:
            # Single number
            result.append(int(part))

    return ','.join(map(str, result))

# Test cases
print(expand_ranges("1-5"))         # "1,2,3,4,5"
print(expand_ranges("1-3,7-9"))     # "1,2,3,7,8,9"
print(expand_ranges("5,8-10,12"))   # "5,8,9,10,12"
```

### Solution 13: Acronym Generator
```python
def generate_acronym(phrase):
    """Generate acronym from phrase."""
    # Words to ignore
    ignore = {'the', 'and', 'of', 'in', 'a', 'an', 'to', 'for'}

    words = phrase.split()
    acronym = []

    for word in words:
        if word.lower() not in ignore:
            acronym.append(word[0].upper())

    return ''.join(acronym)

# Alternative with regex
import re

def generate_acronym_regex(phrase):
    """Generate acronym using regex."""
    ignore = {'the', 'and', 'of', 'in', 'a', 'an', 'to', 'for'}
    words = phrase.split()

    # Get first letter of non-ignored words
    letters = [w[0].upper() for w in words if w.lower() not in ignore]
    return ''.join(letters)

# Test cases
print(generate_acronym("As Soon As Possible"))         # "ASAP"
print(generate_acronym("Central Processing Unit"))     # "CPU"
print(generate_acronym("Department of Motor Vehicles")) # "DMV"
```

### Solution 14: Text Alignment
```python
def align_text(text, width, alignment='left'):
    """Align text to specified width."""
    if len(text) >= width:
        return text

    padding = width - len(text)

    if alignment == 'left':
        return text + ' ' * padding
    elif alignment == 'right':
        return ' ' * padding + text
    elif alignment == 'center':
        left_pad = padding // 2
        right_pad = padding - left_pad
        return ' ' * left_pad + text + ' ' * right_pad
    else:
        raise ValueError(f"Invalid alignment: {alignment}")

# Using string methods
def align_text_builtin(text, width, alignment='left'):
    """Align text using built-in methods."""
    if alignment == 'left':
        return text.ljust(width)
    elif alignment == 'right':
        return text.rjust(width)
    elif alignment == 'center':
        return text.center(width)
    else:
        raise ValueError(f"Invalid alignment: {alignment}")

# Test cases
print(repr(align_text("hello", 10, 'left')))    # "hello     "
print(repr(align_text("hello", 10, 'right')))   # "     hello"
print(repr(align_text("hello", 10, 'center')))  # "  hello   "
```

### Solution 15: Run-Length Encoding
```python
def run_length_encode(s):
    """Encode string using run-length encoding."""
    if not s:
        return ""

    result = []
    count = 1
    current = s[0]

    for char in s[1:]:
        if char == current:
            count += 1
        else:
            result.append(f"{count}{current}")
            current = char
            count = 1

    # Don't forget last group
    result.append(f"{count}{current}")

    return ''.join(result)

def run_length_decode(s):
    """Decode run-length encoded string."""
    result = []
    i = 0

    while i < len(s):
        # Read count (one or more digits)
        count = ''
        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1

        # Read character
        if i < len(s):
            char = s[i]
            result.append(char * int(count))
            i += 1

    return ''.join(result)

# Alternative using regex
import re

def run_length_decode_regex(s):
    """Decode using regex."""
    result = []
    # Match number followed by character
    for match in re.finditer(r'(\d+)(.)', s):
        count = int(match.group(1))
        char = match.group(2)
        result.append(char * count)
    return ''.join(result)

# Test cases
print(run_length_encode("aaabbc"))     # "3a2b1c"
print(run_length_encode("hello"))      # "1h1e2l1o"
print(run_length_decode("3a2b1c"))     # "aaabbc"
print(run_length_decode("1h1e2l1o"))   # "hello"

# Test round-trip
original = "aaabbccccdd"
encoded = run_length_encode(original)
decoded = run_length_decode(encoded)
print(f"{original} -> {encoded} -> {decoded}")
print(f"Match: {original == decoded}")
```

## Additional Solutions

### Bonus: Longest Common Substring
```python
def longest_common_substring(s1, s2):
    """Find longest common substring."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_pos = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_pos = i

    return s1[end_pos - max_length:end_pos]

# Test
print(longest_common_substring("abcdef", "xbcde"))  # "bcde"
```

### Bonus: Anagram Checker
```python
def are_anagrams(s1, s2):
    """Check if two strings are anagrams."""
    # Remove spaces and convert to lowercase
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Compare sorted characters
    return sorted(s1) == sorted(s2)

# Alternative using Counter
from collections import Counter

def are_anagrams_counter(s1, s2):
    """Check anagrams using Counter."""
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return Counter(s1) == Counter(s2)

# Test
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
```
