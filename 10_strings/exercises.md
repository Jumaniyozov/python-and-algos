# String Processing - Exercises

## Basic String Operations

### Exercise 1: Palindrome Checker
Write a function that checks if a string is a palindrome (reads the same forwards and backwards). Ignore spaces, punctuation, and case.

```python
def is_palindrome(s):
    """Check if string is palindrome."""
    pass

# Test cases
assert is_palindrome("racecar") == True
assert is_palindrome("A man a plan a canal Panama") == True
assert is_palindrome("hello") == False
```

### Exercise 2: Character Frequency
Write a function that counts the frequency of each character in a string. Return a dictionary with characters as keys and counts as values.

```python
def char_frequency(s):
    """Count frequency of each character."""
    pass

# Test cases
assert char_frequency("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
assert char_frequency("aabbcc") == {'a': 2, 'b': 2, 'c': 2}
```

### Exercise 3: Title Case Converter
Write a function that converts a string to title case, but keeps certain words lowercase (articles, prepositions, etc.) unless they're the first word.

```python
def smart_title_case(s):
    """Convert to title case with exceptions."""
    pass

# Test cases
assert smart_title_case("the lord of the rings") == "The Lord of the Rings"
assert smart_title_case("a tale of two cities") == "A Tale of Two Cities"
```

### Exercise 4: Reverse Words
Write a function that reverses the order of words in a sentence while preserving the order of characters in each word.

```python
def reverse_words(s):
    """Reverse order of words in string."""
    pass

# Test cases
assert reverse_words("hello world") == "world hello"
assert reverse_words("the quick brown fox") == "fox brown quick the"
```

### Exercise 5: Remove Duplicates
Write a function that removes consecutive duplicate characters from a string.

```python
def remove_consecutive_duplicates(s):
    """Remove consecutive duplicate characters."""
    pass

# Test cases
assert remove_consecutive_duplicates("hello") == "helo"
assert remove_consecutive_duplicates("aaabbbccc") == "abc"
assert remove_consecutive_duplicates("aabbccaabb") == "abcab"
```

## Regular Expressions

### Exercise 6: Username Validator
Write a function that validates usernames with these rules:
- 3-16 characters long
- Can contain letters, numbers, hyphens, and underscores
- Must start with a letter
- Cannot end with hyphen or underscore

```python
def validate_username(username):
    """Validate username format."""
    pass

# Test cases
assert validate_username("john_doe") == True
assert validate_username("user123") == True
assert validate_username("ab") == False  # Too short
assert validate_username("user-") == False  # Ends with hyphen
assert validate_username("123user") == False  # Starts with number
```

### Exercise 7: Extract Quoted Text
Write a function that extracts all text within quotes (both single and double) from a string.

```python
def extract_quotes(text):
    """Extract all quoted text."""
    pass

# Test cases
assert extract_quotes('He said "hello" and she said "world"') == ["hello", "world"]
assert extract_quotes("It's a 'beautiful' day") == ["beautiful"]
```

### Exercise 8: Credit Card Masking
Write a function that masks all but the last 4 digits of a credit card number. Support various formats.

```python
def mask_credit_card(card_number):
    """Mask credit card number."""
    pass

# Test cases
assert mask_credit_card("1234-5678-9012-3456") == "****-****-****-3456"
assert mask_credit_card("1234567890123456") == "************3456"
```

### Exercise 9: Parse HTML Tags
Write a function that extracts all HTML tag names from a string.

```python
def extract_html_tags(html):
    """Extract HTML tag names."""
    pass

# Test cases
assert extract_html_tags("<div><p>Hello</p></div>") == ["div", "p", "p", "div"]
assert extract_html_tags("<a href='#'><img src='pic.jpg'></a>") == ["a", "img", "a"]
```

### Exercise 10: Time Format Converter
Write a function that converts time from 12-hour format to 24-hour format.

```python
def convert_to_24h(time_str):
    """Convert 12-hour time to 24-hour format."""
    pass

# Test cases
assert convert_to_24h("12:00 AM") == "00:00"
assert convert_to_24h("12:00 PM") == "12:00"
assert convert_to_24h("11:30 PM") == "23:30"
assert convert_to_24h("01:45 AM") == "01:45"
```

## Text Processing

### Exercise 11: Word Count
Write a function that counts words in a text. Consider words separated by spaces or punctuation.

```python
def word_count(text):
    """Count words in text."""
    pass

# Test cases
assert word_count("Hello, world!") == 2
assert word_count("one two three") == 3
assert word_count("don't count-this as multiple") == 4
```

### Exercise 12: Expand Ranges
Write a function that expands range notation in a string. For example, "1-5" becomes "1,2,3,4,5".

```python
def expand_ranges(s):
    """Expand range notation to individual values."""
    pass

# Test cases
assert expand_ranges("1-5") == "1,2,3,4,5"
assert expand_ranges("1-3,7-9") == "1,2,3,7,8,9"
assert expand_ranges("5,8-10,12") == "5,8,9,10,12"
```

### Exercise 13: Acronym Generator
Write a function that generates an acronym from a phrase. Use the first letter of each word, but ignore common words like "the", "and", "of".

```python
def generate_acronym(phrase):
    """Generate acronym from phrase."""
    pass

# Test cases
assert generate_acronym("As Soon As Possible") == "ASAP"
assert generate_acronym("Central Processing Unit") == "CPU"
assert generate_acronym("Department of Motor Vehicles") == "DMV"
```

### Exercise 14: Text Alignment
Write a function that aligns text to a specified width. Support left, right, and center alignment.

```python
def align_text(text, width, alignment='left'):
    """Align text to specified width."""
    pass

# Test cases
assert align_text("hello", 10, 'left') == "hello     "
assert align_text("hello", 10, 'right') == "     hello"
assert align_text("hello", 10, 'center') == "  hello   "
```

### Exercise 15: Run-Length Encoding
Write functions to encode and decode strings using run-length encoding. For example, "aaabbc" becomes "3a2b1c".

```python
def run_length_encode(s):
    """Encode string using run-length encoding."""
    pass

def run_length_decode(s):
    """Decode run-length encoded string."""
    pass

# Test cases
assert run_length_encode("aaabbc") == "3a2b1c"
assert run_length_encode("hello") == "1h1e2l1o"
assert run_length_decode("3a2b1c") == "aaabbc"
assert run_length_decode("1h1e2l1o") == "hello"
```
