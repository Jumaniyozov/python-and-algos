# Date and Time - Tips and Best Practices

## Critical Best Practices

### 1. Always Use Timezone-Aware Datetimes in Production

**Bad**:
```python
# Naive datetime - no timezone info
now = datetime.now()
```

**Good**:
```python
from datetime import datetime
from zoneinfo import ZoneInfo

# Timezone-aware datetime
now = datetime.now(ZoneInfo("UTC"))
```

**Why**: Naive datetimes cause ambiguity and bugs when dealing with users in different timezones or during DST transitions.

### 2. Store in UTC, Display in Local

**Best Practice**:
```python
from datetime import datetime
from zoneinfo import ZoneInfo

# Store in database as UTC
utc_time = datetime.now(ZoneInfo("UTC"))
save_to_database(utc_time)

# Display in user's timezone
user_tz = ZoneInfo("America/New_York")
local_time = utc_time.astimezone(user_tz)
print(f"Your meeting: {local_time}")
```

**Why**: UTC is unambiguous and doesn't have DST. Converting to local timezone only for display prevents storage issues.

### 3. Use ISO Format for String Representation

**Good**:
```python
dt = datetime.now()
iso_string = dt.isoformat()  # "2024-03-15T14:30:45.123456"

# Parse back
dt_parsed = datetime.fromisoformat(iso_string)
```

**Why**: ISO 8601 format is internationally recognized, unambiguous, and sortable.

### 4. Prefer zoneinfo over pytz (Python 3.9+)

**Old Way (pytz)**:
```python
import pytz
tz = pytz.timezone("America/New_York")
dt = tz.localize(datetime(2024, 3, 15, 14, 0))
```

**New Way (zoneinfo)**:
```python
from zoneinfo import ZoneInfo
dt = datetime(2024, 3, 15, 14, 0, tzinfo=ZoneInfo("America/New_York"))
```

**Why**: zoneinfo is in the standard library, more Pythonic, and handles edge cases better.

## Common Pitfalls and Solutions

### 1. Mixing Naive and Aware Datetimes

**Problem**:
```python
naive = datetime(2024, 3, 15, 10, 0)
aware = datetime.now(ZoneInfo("UTC"))
diff = aware - naive  # TypeError!
```

**Solution**:
```python
# Make everything aware
naive_as_aware = naive.replace(tzinfo=ZoneInfo("UTC"))
diff = aware - naive_as_aware  # Works!
```

### 2. Using datetime.now() Without Timezone

**Problem**:
```python
now = datetime.now()  # Which timezone?
```

**Solution**:
```python
# Explicit timezone
now_utc = datetime.now(ZoneInfo("UTC"))
now_local = datetime.now(ZoneInfo("America/New_York"))
```

### 3. Forgetting Leap Years

**Problem**:
```python
# Will crash on Feb 29 in leap years
dt = datetime(year, 2, 29)
```

**Solution**:
```python
import calendar

if calendar.isleap(year):
    # Handle leap year
    pass
```

### 4. Incorrect String Parsing

**Problem**:
```python
# Format doesn't match
dt = datetime.strptime("15/03/2024", "%Y-%m-%d")  # ValueError!
```

**Solution**:
```python
# Match format exactly
dt = datetime.strptime("15/03/2024", "%d/%m/%Y")

# Or try multiple formats
def parse_flexible(date_str):
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Cannot parse: {date_str}")
```

### 5. DST Transition Issues

**Problem**:
```python
# During DST transition, some times don't exist or are ambiguous
# March 10, 2024, 2:30 AM doesn't exist in America/New_York (spring forward)
```

**Solution**:
```python
from zoneinfo import ZoneInfo

# Use UTC for calculations
utc_time = datetime.now(ZoneInfo("UTC"))

# Convert to local only for display
local_time = utc_time.astimezone(ZoneInfo("America/New_York"))
```

## Performance Tips

### 1. Cache Timezone Objects

**Slow**:
```python
for dt in dates:
    dt_local = dt.astimezone(ZoneInfo("America/New_York"))
```

**Fast**:
```python
ny_tz = ZoneInfo("America/New_York")  # Cache this
for dt in dates:
    dt_local = dt.astimezone(ny_tz)
```

### 2. Use date Instead of datetime When Appropriate

**Less Efficient**:
```python
dt = datetime.now()
if dt.date() == today:
    pass
```

**More Efficient**:
```python
from datetime import date
today = date.today()
if some_date == today:
    pass
```

### 3. Avoid Repeated String Parsing

**Slow**:
```python
for date_str in date_strings:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    process(dt)
```

**Better**:
```python
# If possible, store as datetime objects
dates = [datetime.strptime(s, "%Y-%m-%d") for s in date_strings]
for dt in dates:
    process(dt)
```

## Useful Patterns

### 1. Start and End of Day

```python
def start_of_day(dt):
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)

def end_of_day(dt):
    return dt.replace(hour=23, minute=59, second=59, microsecond=999999)
```

### 2. Start and End of Month

```python
import calendar
from datetime import date

def start_of_month(d):
    return d.replace(day=1)

def end_of_month(d):
    _, last_day = calendar.monthrange(d.year, d.month)
    return d.replace(day=last_day)
```

### 3. Business Day Calculator

```python
from datetime import date, timedelta

def next_business_day(d):
    next_day = d + timedelta(days=1)
    while next_day.weekday() >= 5:  # Saturday or Sunday
        next_day += timedelta(days=1)
    return next_day

def previous_business_day(d):
    prev_day = d - timedelta(days=1)
    while prev_day.weekday() >= 5:
        prev_day -= timedelta(days=1)
    return prev_day
```

### 4. Age Verification

```python
def is_adult(birth_date, adult_age=18):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age >= adult_age
```

### 5. Date Range Validation

```python
def is_valid_range(start, end):
    """Check if date range is valid."""
    if start > end:
        return False
    if (end - start).days > 365:  # More than a year
        return False
    return True
```

## Testing Tips

### 1. Use Fixed Dates in Tests

**Bad**:
```python
def test_age_calculation():
    birth = date.today() - timedelta(days=365 * 30)
    age = calculate_age(birth)
    assert age == 30  # Will fail eventually!
```

**Good**:
```python
def test_age_calculation():
    birth = date(1994, 1, 1)
    today = date(2024, 3, 15)
    age = calculate_age(birth, reference_date=today)
    assert age == 30
```

### 2. Test Timezone Conversions

```python
def test_timezone_conversion():
    utc_time = datetime(2024, 3, 15, 12, 0, tzinfo=ZoneInfo("UTC"))
    ny_time = utc_time.astimezone(ZoneInfo("America/New_York"))

    # EST is UTC-5 (or EDT is UTC-4 during DST)
    # Verify the conversion is correct
    assert ny_time.hour in (7, 8)  # Depends on DST
```

### 3. Test Edge Cases

```python
def test_leap_year():
    assert is_valid_date(2024, 2, 29)  # Leap year
    assert not is_valid_date(2023, 2, 29)  # Not leap year

def test_dst_transition():
    # Test dates around DST transitions
    pass
```

## Debugging Tips

### 1. Print with Timezone Info

```python
dt = datetime.now(ZoneInfo("UTC"))
print(f"{dt} (timezone: {dt.tzinfo})")
print(f"ISO format: {dt.isoformat()}")
print(f"Timestamp: {dt.timestamp()}")
```

### 2. Visualize Date Ranges

```python
def print_date_range(start, end):
    print(f"Range: {start} to {end}")
    print(f"Duration: {(end - start).days} days")
    print(f"Weekdays: {sum(1 for d in date_range(start, end) if d.weekday() < 5)}")
```

### 3. Check Timezone Offset

```python
dt = datetime.now(ZoneInfo("America/New_York"))
offset = dt.strftime("%z")  # e.g., "-0500" or "-0400"
print(f"Timezone offset: {offset}")
```

## Common Gotchas

### 1. Month Arithmetic is Tricky

**Problem**:
```python
# What is "one month" from Jan 31?
dt = date(2024, 1, 31)
# There's no Feb 31!
```

**Solution**:
```python
from datetime import date
import calendar

def add_months(d, months):
    month = d.month + months
    year = d.year + month // 12
    month = month % 12 or 12

    # Handle day overflow
    _, last_day = calendar.monthrange(year, month)
    day = min(d.day, last_day)

    return date(year, month, day)
```

### 2. Comparison of Naive and Aware

```python
# This raises TypeError
naive = datetime(2024, 3, 15)
aware = datetime.now(ZoneInfo("UTC"))
if naive > aware:  # TypeError!
    pass
```

### 3. timedelta Limitations

```python
# timedelta doesn't support months or years
# Because they vary in length
delta = timedelta(months=1)  # TypeError!

# Use dateutil or manual calculation instead
```

## Advanced Tips

### 1. Custom Date Formatting

```python
def format_date_range(start, end):
    if start == end:
        return start.strftime("%B %d, %Y")
    elif start.year == end.year:
        if start.month == end.month:
            return f"{start.strftime('%B %d')}-{end.day}, {start.year}"
        else:
            return f"{start.strftime('%B %d')} - {end.strftime('%B %d, %Y')}"
    else:
        return f"{start.strftime('%B %d, %Y')} - {end.strftime('%B %d, %Y')}"
```

### 2. Parsing Relative Dates

```python
def parse_relative_date(text):
    today = date.today()
    text = text.lower()

    if text == "today":
        return today
    elif text == "yesterday":
        return today - timedelta(days=1)
    elif text == "tomorrow":
        return today + timedelta(days=1)
    elif "ago" in text:
        # Parse "5 days ago", "2 weeks ago"
        parts = text.split()
        value = int(parts[0])
        unit = parts[1]
        if "day" in unit:
            return today - timedelta(days=value)
        elif "week" in unit:
            return today - timedelta(weeks=value)
    # Add more patterns as needed
```

### 3. Working with Business Hours

```python
from datetime import datetime, time, timedelta

def add_business_hours(dt, hours):
    """Add business hours (9 AM - 5 PM, Mon-Fri)."""
    work_day_hours = 8
    days, remaining_hours = divmod(hours, work_day_hours)

    # Add business days
    current = dt
    for _ in range(int(days)):
        current = next_business_day(current)

    # Add remaining hours
    result = current + timedelta(hours=remaining_hours)

    # Adjust if outside work hours
    if result.hour < 9:
        result = result.replace(hour=9)
    elif result.hour >= 17:
        days_ahead = result.hour - 17 + 1
        result = next_business_day(result.date())
        result = datetime.combine(result, time(9 + days_ahead, 0))

    return result
```

## Resources and Tools

### Libraries
- **zoneinfo**: Standard library (Python 3.9+)
- **dateutil**: Powerful date parsing and arithmetic
- **arrow**: Human-friendly dates and times
- **pendulum**: Drop-in datetime replacement
- **pytz**: Legacy timezone handling

### Debugging Tools
```python
# Print all available timezones
from zoneinfo import available_timezones
print(sorted(available_timezones()))

# Check current timezone
import time
print(time.tzname)
```

### Online Resources
- IANA Timezone Database: https://www.iana.org/time-zones
- ISO 8601 Format: https://en.wikipedia.org/wiki/ISO_8601
- Python datetime docs: https://docs.python.org/3/library/datetime.html
