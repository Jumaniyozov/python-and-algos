# Date and Time - Examples

## Example 1: Basic Date and Time Creation

```python
from datetime import date, time, datetime

# Create date
d = date(2024, 3, 15)
print(f"Date: {d}")  # Date: 2024-03-15

# Create time
t = time(14, 30, 45)
print(f"Time: {t}")  # Time: 14:30:45

# Create datetime
dt = datetime(2024, 3, 15, 14, 30, 45)
print(f"DateTime: {dt}")  # DateTime: 2024-03-15 14:30:45

# Current date and time
today = date.today()
now = datetime.now()
print(f"Today: {today}")
print(f"Now: {now}")
```

## Example 2: Accessing Components

```python
from datetime import datetime

dt = datetime(2024, 3, 15, 14, 30, 45, 123456)

# Access components
print(f"Year: {dt.year}")           # Year: 2024
print(f"Month: {dt.month}")         # Month: 3
print(f"Day: {dt.day}")             # Day: 15
print(f"Hour: {dt.hour}")           # Hour: 14
print(f"Minute: {dt.minute}")       # Minute: 30
print(f"Second: {dt.second}")       # Second: 45
print(f"Microsecond: {dt.microsecond}")  # Microsecond: 123456

# Day of week (Monday=0, Sunday=6)
print(f"Weekday: {dt.weekday()}")   # Weekday: 4 (Friday)
print(f"ISO Weekday: {dt.isoweekday()}")  # ISO Weekday: 5 (Friday)
```

## Example 3: Date Arithmetic with timedelta

```python
from datetime import datetime, timedelta

now = datetime(2024, 3, 15, 10, 0, 0)

# Add time
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
in_2_hours = now + timedelta(hours=2)
in_90_mins = now + timedelta(minutes=90)

print(f"Tomorrow: {tomorrow}")
print(f"Next week: {next_week}")
print(f"In 2 hours: {in_2_hours}")
print(f"In 90 minutes: {in_90_mins}")

# Subtract time
yesterday = now - timedelta(days=1)
last_month = now - timedelta(days=30)

print(f"Yesterday: {yesterday}")
print(f"~Last month: {last_month}")

# Calculate difference
future = datetime(2024, 12, 31, 23, 59, 59)
diff = future - now
print(f"Days until New Year: {diff.days}")
print(f"Total seconds: {diff.total_seconds()}")
```

## Example 4: String Formatting (strftime)

```python
from datetime import datetime

dt = datetime(2024, 3, 15, 14, 30, 45)

# Various formats
print(dt.strftime("%Y-%m-%d"))              # 2024-03-15
print(dt.strftime("%d/%m/%Y"))              # 15/03/2024
print(dt.strftime("%B %d, %Y"))             # March 15, 2024
print(dt.strftime("%A, %B %d, %Y"))         # Friday, March 15, 2024
print(dt.strftime("%I:%M %p"))              # 02:30 PM
print(dt.strftime("%H:%M:%S"))              # 14:30:45
print(dt.strftime("%Y-%m-%d %H:%M:%S"))     # 2024-03-15 14:30:45

# Custom format
custom = dt.strftime("Date: %d-%b-%Y, Time: %I:%M %p")
print(custom)  # Date: 15-Mar-2024, Time: 02:30 PM

# ISO format
print(dt.isoformat())  # 2024-03-15T14:30:45
```

## Example 5: String Parsing (strptime)

```python
from datetime import datetime

# Parse various formats
dt1 = datetime.strptime("2024-03-15", "%Y-%m-%d")
print(dt1)  # 2024-03-15 00:00:00

dt2 = datetime.strptime("15/03/2024", "%d/%m/%Y")
print(dt2)  # 2024-03-15 00:00:00

dt3 = datetime.strptime("March 15, 2024", "%B %d, %Y")
print(dt3)  # 2024-03-15 00:00:00

dt4 = datetime.strptime("15-Mar-2024 14:30:45", "%d-%b-%Y %H:%M:%S")
print(dt4)  # 2024-03-15 14:30:45

# ISO format parsing
dt5 = datetime.fromisoformat("2024-03-15T14:30:45")
print(dt5)  # 2024-03-15 14:30:45

# Handle parsing errors
try:
    invalid = datetime.strptime("invalid date", "%Y-%m-%d")
except ValueError as e:
    print(f"Parse error: {e}")
```

## Example 6: Timezone Handling (zoneinfo)

```python
from datetime import datetime
from zoneinfo import ZoneInfo

# Create timezone-aware datetime
utc_time = datetime(2024, 3, 15, 10, 0, 0, tzinfo=ZoneInfo("UTC"))
print(f"UTC: {utc_time}")

# Convert to different timezones
ny_time = utc_time.astimezone(ZoneInfo("America/New_York"))
tokyo_time = utc_time.astimezone(ZoneInfo("Asia/Tokyo"))
london_time = utc_time.astimezone(ZoneInfo("Europe/London"))

print(f"New York: {ny_time}")
print(f"Tokyo: {tokyo_time}")
print(f"London: {london_time}")

# Current time in specific timezone
now_utc = datetime.now(ZoneInfo("UTC"))
now_ny = datetime.now(ZoneInfo("America/New_York"))
print(f"Current UTC: {now_utc}")
print(f"Current NY: {now_ny}")

# Check if aware or naive
print(f"Is aware: {utc_time.tzinfo is not None}")
naive = datetime(2024, 3, 15)
print(f"Is naive: {naive.tzinfo is None}")
```

## Example 7: Age Calculator

```python
from datetime import date

def calculate_age(birth_date):
    """Calculate age in years."""
    today = date.today()
    age = today.year - birth_date.year
    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

# Examples
birth1 = date(1990, 6, 15)
birth2 = date(2000, 12, 25)
birth3 = date(2010, 1, 1)

print(f"Age 1: {calculate_age(birth1)} years")
print(f"Age 2: {calculate_age(birth2)} years")
print(f"Age 3: {calculate_age(birth3)} years")

# Calculate days lived
def days_lived(birth_date):
    """Calculate days lived."""
    return (date.today() - birth_date).days

print(f"Days lived: {days_lived(birth1)} days")
```

## Example 8: Business Days Calculator

```python
from datetime import date, timedelta

def is_business_day(d):
    """Check if date is a business day (Mon-Fri)."""
    return d.weekday() < 5

def add_business_days(start_date, days):
    """Add business days to a date."""
    current = start_date
    while days > 0:
        current += timedelta(days=1)
        if is_business_day(current):
            days -= 1
    return current

def count_business_days(start_date, end_date):
    """Count business days between two dates."""
    count = 0
    current = start_date
    while current <= end_date:
        if is_business_day(current):
            count += 1
        current += timedelta(days=1)
    return count

# Examples
start = date(2024, 3, 15)  # Friday
result = add_business_days(start, 5)
print(f"5 business days from {start}: {result}")

count = count_business_days(date(2024, 3, 1), date(2024, 3, 31))
print(f"Business days in March 2024: {count}")
```

## Example 9: Date Ranges and Iteration

```python
from datetime import date, timedelta

def date_range(start, end, step=1):
    """Generate dates between start and end."""
    current = start
    while current <= end:
        yield current
        current += timedelta(days=step)

# Iterate through March 2024
start = date(2024, 3, 1)
end = date(2024, 3, 31)

print("All dates in March 2024:")
for d in date_range(start, end):
    print(d, d.strftime("%A"))

# Every 7 days
print("\nEvery week:")
for d in date_range(start, end, step=7):
    print(d)

# List comprehension
march_dates = [d for d in date_range(start, end)]
print(f"\nTotal days: {len(march_dates)}")

# Filter weekends
weekends = [d for d in date_range(start, end) if d.weekday() >= 5]
print(f"Weekend days: {len(weekends)}")
```

## Example 10: Calendar Operations

```python
import calendar
from datetime import date, timedelta

# Get calendar information
year = 2024
month = 3

# Check if leap year
print(f"{year} is leap year: {calendar.isleap(year)}")

# Days in month
days_in_march = calendar.monthrange(year, month)[1]
print(f"Days in March {year}: {days_in_march}")

# First day of month (0=Monday, 6=Sunday)
first_weekday = calendar.monthrange(year, month)[0]
print(f"March 1st is: {calendar.day_name[first_weekday]}")

# Get first and last day of month
first_day = date(year, month, 1)
last_day = date(year, month, days_in_march)
print(f"First day: {first_day}")
print(f"Last day: {last_day}")

# Print calendar
print(f"\n{calendar.month(year, month)}")

# Week number
d = date(2024, 3, 15)
week_num = d.isocalendar()[1]
print(f"Week number for {d}: {week_num}")
```

## Example 11: Time Comparisons

```python
from datetime import datetime, timedelta

now = datetime.now()
past = now - timedelta(days=5)
future = now + timedelta(days=5)

# Comparisons
print(f"Past < Now: {past < now}")
print(f"Future > Now: {future > now}")
print(f"Now == Now: {now == now}")

# Sorting dates
dates = [
    datetime(2024, 3, 15),
    datetime(2024, 1, 1),
    datetime(2024, 6, 30),
    datetime(2024, 12, 31),
]

sorted_dates = sorted(dates)
print("\nSorted dates:")
for d in sorted_dates:
    print(d.strftime("%Y-%m-%d"))

# Find min/max
print(f"\nEarliest: {min(dates)}")
print(f"Latest: {max(dates)}")

# Check if date is in range
target = datetime(2024, 4, 1)
start = datetime(2024, 3, 1)
end = datetime(2024, 5, 1)
in_range = start <= target <= end
print(f"\n{target.date()} in range: {in_range}")
```

## Example 12: Replace Components

```python
from datetime import datetime

dt = datetime(2024, 3, 15, 14, 30, 45)

# Replace individual components
new_year = dt.replace(year=2025)
new_month = dt.replace(month=12)
new_day = dt.replace(day=1)
new_time = dt.replace(hour=0, minute=0, second=0)

print(f"Original: {dt}")
print(f"New year: {new_year}")
print(f"New month: {new_month}")
print(f"First of month: {new_day}")
print(f"Midnight: {new_time}")

# Start of day
start_of_day = dt.replace(hour=0, minute=0, second=0, microsecond=0)
print(f"Start of day: {start_of_day}")

# End of day
end_of_day = dt.replace(hour=23, minute=59, second=59, microsecond=999999)
print(f"End of day: {end_of_day}")
```

## Example 13: Working with Timestamps

```python
from datetime import datetime
import time

# Get Unix timestamp
dt = datetime(2024, 3, 15, 14, 30, 45)
timestamp = dt.timestamp()
print(f"Timestamp: {timestamp}")

# Convert from timestamp
dt_from_ts = datetime.fromtimestamp(timestamp)
print(f"From timestamp: {dt_from_ts}")

# Current timestamp
current_ts = time.time()
print(f"Current timestamp: {current_ts}")

# UTC from timestamp
utc_dt = datetime.utcfromtimestamp(current_ts)
print(f"UTC from timestamp: {utc_dt}")

# Measure elapsed time
start_time = time.time()
time.sleep(0.1)  # Simulate work
end_time = time.time()
elapsed = end_time - start_time
print(f"Elapsed: {elapsed:.3f} seconds")
```

## Example 14: Date Validation

```python
from datetime import datetime, date

def is_valid_date(year, month, day):
    """Check if date is valid."""
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def parse_flexible_date(date_str):
    """Try multiple formats to parse date."""
    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%B %d, %Y",
        "%d %B %Y",
        "%Y%m%d",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    raise ValueError(f"Cannot parse date: {date_str}")

# Test validation
print(is_valid_date(2024, 2, 29))  # True (leap year)
print(is_valid_date(2023, 2, 29))  # False (not leap year)
print(is_valid_date(2024, 13, 1))  # False (invalid month)

# Test flexible parsing
dates = [
    "2024-03-15",
    "15/03/2024",
    "03/15/2024",
    "March 15, 2024",
    "15 March 2024",
    "20240315",
]

for date_str in dates:
    try:
        parsed = parse_flexible_date(date_str)
        print(f"{date_str} -> {parsed.date()}")
    except ValueError as e:
        print(f"Failed: {e}")
```

## Example 15: Recurring Events

```python
from datetime import date, timedelta

def get_nth_weekday(year, month, weekday, n):
    """Get the nth occurrence of a weekday in a month.
    weekday: 0=Monday, 6=Sunday
    n: 1=first, 2=second, -1=last, etc.
    """
    first = date(year, month, 1)

    if n > 0:
        # First occurrence of weekday
        first_weekday = first + timedelta(days=(weekday - first.weekday()) % 7)
        # Add weeks
        result = first_weekday + timedelta(weeks=n-1)
        # Check still in month
        if result.month == month:
            return result
    else:
        # Start from next month
        if month == 12:
            next_month = date(year + 1, 1, 1)
        else:
            next_month = date(year, month + 1, 1)
        # Go back one day
        last_day = next_month - timedelta(days=1)
        # Find last occurrence
        days_back = (last_day.weekday() - weekday) % 7
        result = last_day - timedelta(days=days_back)
        # Go back more weeks if needed
        result += timedelta(weeks=n+1)
        if result.month == month:
            return result

    return None

# Examples
# Second Monday of March 2024
second_monday = get_nth_weekday(2024, 3, 0, 2)
print(f"Second Monday of March 2024: {second_monday}")

# Last Friday of March 2024
last_friday = get_nth_weekday(2024, 3, 4, -1)
print(f"Last Friday of March 2024: {last_friday}")

# First Sunday of each month in 2024
print("\nFirst Sunday of each month in 2024:")
for month in range(1, 13):
    first_sunday = get_nth_weekday(2024, month, 6, 1)
    print(f"{first_sunday.strftime('%B')}: {first_sunday}")
```
