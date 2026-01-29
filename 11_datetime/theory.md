# Date and Time - Theory

## Core Concepts

### 1. datetime Module Classes

Python's `datetime` module provides four main classes:

**date**: Represents a date (year, month, day)
- Attributes: year, month, day
- Range: date.min (0001-01-01) to date.max (9999-12-31)

**time**: Represents a time (hour, minute, second, microsecond)
- Attributes: hour, minute, second, microsecond, tzinfo
- Independent of any particular day

**datetime**: Combines date and time
- Attributes: All from date + all from time
- Most commonly used class

**timedelta**: Represents a duration/difference between dates or times
- Used for date arithmetic
- Components: days, seconds, microseconds

### 2. Timezone Handling

**Naive vs Aware Objects**:
- Naive: No timezone information (tzinfo is None)
- Aware: Has timezone information (tzinfo is set)

**zoneinfo Module** (Python 3.9+):
- Provides IANA timezone database
- Replaces pytz for most use cases
- Use ZoneInfo for timezone-aware operations

**UTC**:
- Coordinated Universal Time
- Standard reference timezone
- Best practice: Store times in UTC, display in local timezone

### 3. String Formatting

**strftime** (string from time):
- Converts datetime object to string
- Uses format codes like %Y, %m, %d, %H, %M, %S

**strptime** (string parse time):
- Converts string to datetime object
- Must match exact format

**ISO Format**:
- Standard format: YYYY-MM-DDTHH:MM:SS
- Use .isoformat() and .fromisoformat()

### 4. Calendar Operations

**calendar Module**:
- Calendar-related functions
- Month/year calendars
- Day of week calculations
- Leap year checks

**Common Operations**:
- First/last day of month
- Weekday calculations
- Week numbers
- Business day calculations

### 5. Time Arithmetic

**Adding/Subtracting Time**:
- Use timedelta for duration
- datetime + timedelta = datetime
- datetime - datetime = timedelta

**Comparison**:
- datetime objects are comparable
- Can use <, >, ==, !=, <=, >=

**Replacing Components**:
- Use .replace() to change specific components
- Creates new object (immutable)

## Common Patterns

### Age Calculation
```python
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age
```

### Business Days
```python
from datetime import date, timedelta

def add_business_days(start_date, days):
    current = start_date
    while days > 0:
        current += timedelta(days=1)
        if current.weekday() < 5:  # Monday = 0, Sunday = 6
            days -= 1
    return current
```

### Date Ranges
```python
from datetime import date, timedelta

def date_range(start, end):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)
```

## Important Format Codes

| Code | Meaning | Example |
|------|---------|---------|
| %Y | Year (4 digits) | 2024 |
| %y | Year (2 digits) | 24 |
| %m | Month (01-12) | 03 |
| %B | Month name | March |
| %b | Month abbr | Mar |
| %d | Day of month | 15 |
| %A | Weekday name | Monday |
| %a | Weekday abbr | Mon |
| %H | Hour (24h) | 14 |
| %I | Hour (12h) | 02 |
| %M | Minute | 30 |
| %S | Second | 45 |
| %p | AM/PM | PM |
| %z | UTC offset | +0500 |
| %Z | Timezone name | EST |

## Best Practices

1. **Always use timezone-aware datetimes** for production code
2. **Store in UTC**, convert to local for display
3. **Use ISO format** for string representation
4. **Never use local time** for comparisons across timezones
5. **Be careful with DST** transitions
6. **Use timedelta** for all date arithmetic
7. **Prefer zoneinfo** over pytz (Python 3.9+)
8. **Validate user input** when parsing dates

## Performance Considerations

- datetime operations are fast (implemented in C)
- String parsing (strptime) is slower than construction
- Timezone conversions have overhead
- Use date instead of datetime when time not needed
- Cache timezone objects if used repeatedly

## Common Pitfalls

1. **Mixing naive and aware datetimes** - raises TypeError
2. **Forgetting DST transitions** - can cause hour shifts
3. **Using local time for persistence** - causes timezone issues
4. **Incorrect format strings** - causes ValueError
5. **Not handling leap years** - February 29th edge cases
6. **Wrong datetime.now()** - use utcnow() or now(tz=...) instead
