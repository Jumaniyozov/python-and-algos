# Control Flow: Practice Exercises

## Exercise 1: Number Classifier
Write a function `classify_number(n: int) -> str` that returns:
- "positive even" for positive even numbers
- "positive odd" for positive odd numbers
- "negative even" for negative even numbers
- "negative odd" for negative odd numbers
- "zero" for zero

## Exercise 2: Leap Year
Create `is_leap_year(year: int) -> bool`. A year is a leap year if:
- Divisible by 4 AND
- Not divisible by 100 OR divisible by 400

Examples: 2000 (yes), 1900 (no), 2024 (yes)

## Exercise 3: Find Duplicates
Write `find_duplicates(items: list) -> list` that returns a list of items appearing more than once. Use a loop with else clause.

## Exercise 4: Safe Division Calculator
Create `calculator(a: float, b: float, op: str) -> float | None` that:
- Supports +, -, *, /
- Returns None for division by zero
- Handles invalid operators
- Uses try/except and match/case

## Exercise 5: File Line Counter
Write `count_lines(filename: str) -> int` using context managers. Handle file not found gracefully.

## Exercise 6: Password Validator
Create `validate_password(password: str) -> tuple[bool, list[str]]` checking:
- At least 8 characters
- At least one uppercase
- At least one digit
- At least one special character (!@#$%^&*)

Return (is_valid, list_of_errors)

## Exercise 7: Pattern Matching Command Parser
Using match/case, parse commands:
- "help" -> show help
- "list" -> list items
- "add <item>" -> add item
- "remove <item>" -> remove item
- "clear" -> clear all

## Exercise 8: Fibonacci Generator
Write `fibonacci(n: int)` that yields first n Fibonacci numbers using a while loop.

## Exercise 9: Retry Decorator
Create a decorator `@retry(max_attempts=3)` that retries a function up to max_attempts times if it raises an exception.

## Exercise 10: Nested Data Navigator
Write `get_nested(data: dict, path: str) -> any` that safely navigates nested dicts:
```python
data = {"user": {"profile": {"name": "Alice"}}}
get_nested(data, "user.profile.name")  # "Alice"
get_nested(data, "user.settings.theme")  # None
```

## Challenge 1: Expression Evaluator
Build a simple calculator that evaluates expressions like "2 + 3 * 4" using pattern matching and proper operator precedence.

## Challenge 2: State Machine
Implement a traffic light state machine using match/case:
- States: red, yellow, green
- Transitions: red->green, green->yellow, yellow->red
- Actions based on current state and input

## Challenge 3: Context Manager for Timing
Create a context manager that times code execution and prints results in different formats (seconds, milliseconds, formatted).

See solutions.md for answers.
