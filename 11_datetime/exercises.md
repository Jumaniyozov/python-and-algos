# Date and Time - Exercises

## Exercise 1: Days Until Birthday
Write a function that takes a birthdate and returns the number of days until the next birthday.

```python
def days_until_birthday(birth_date):
    """
    Calculate days until next birthday.

    Args:
        birth_date: date object representing birth date

    Returns:
        int: Number of days until next birthday
    """
    pass

# Test
from datetime import date
birth = date(1990, 6, 15)
print(days_until_birthday(birth))
```

## Exercise 2: Meeting Scheduler
Write a function that checks if a meeting time conflicts with existing meetings. Return True if there's a conflict.

```python
def has_conflict(new_meeting, existing_meetings):
    """
    Check if new meeting conflicts with existing ones.

    Args:
        new_meeting: tuple of (start_datetime, end_datetime)
        existing_meetings: list of tuples [(start, end), ...]

    Returns:
        bool: True if conflict exists
    """
    pass

# Test
from datetime import datetime
new = (datetime(2024, 3, 15, 10, 0), datetime(2024, 3, 15, 11, 0))
existing = [
    (datetime(2024, 3, 15, 9, 0), datetime(2024, 3, 15, 10, 30)),
    (datetime(2024, 3, 15, 14, 0), datetime(2024, 3, 15, 15, 0)),
]
print(has_conflict(new, existing))  # True
```

## Exercise 3: Time Zone Converter
Create a function that converts a time from one timezone to another and formats it nicely.

```python
def convert_timezone(dt, from_tz, to_tz):
    """
    Convert datetime from one timezone to another.

    Args:
        dt: datetime object (naive)
        from_tz: str, source timezone name
        to_tz: str, target timezone name

    Returns:
        str: Formatted time in target timezone
    """
    pass

# Test
from datetime import datetime
dt = datetime(2024, 3, 15, 14, 0, 0)
result = convert_timezone(dt, "America/New_York", "Asia/Tokyo")
print(result)
```

## Exercise 4: Work Hours Calculator
Write a function that calculates total work hours between two datetimes, excluding weekends and non-work hours (9 AM - 5 PM).

```python
def calculate_work_hours(start, end):
    """
    Calculate work hours between two datetimes.
    Work hours: 9 AM - 5 PM, Monday-Friday

    Args:
        start: datetime object
        end: datetime object

    Returns:
        float: Total work hours
    """
    pass

# Test
from datetime import datetime
start = datetime(2024, 3, 15, 8, 0)   # Friday 8 AM
end = datetime(2024, 3, 18, 17, 0)    # Monday 5 PM
print(calculate_work_hours(start, end))
```

## Exercise 5: Quarter Finder
Create a function that returns the quarter (Q1, Q2, Q3, Q4) for a given date.

```python
def get_quarter(d):
    """
    Get the quarter for a given date.

    Args:
        d: date object

    Returns:
        str: Quarter as "Q1", "Q2", "Q3", or "Q4"
    """
    pass

# Test
from datetime import date
print(get_quarter(date(2024, 1, 15)))   # Q1
print(get_quarter(date(2024, 6, 15)))   # Q2
print(get_quarter(date(2024, 9, 15)))   # Q3
print(get_quarter(date(2024, 12, 15)))  # Q4
```

## Exercise 6: Month Iterator
Write a generator that yields the first day of each month between two dates.

```python
def month_range(start_date, end_date):
    """
    Generate first day of each month in range.

    Args:
        start_date: date object
        end_date: date object

    Yields:
        date: First day of each month
    """
    pass

# Test
from datetime import date
for first_day in month_range(date(2024, 1, 15), date(2024, 6, 20)):
    print(first_day)
```

## Exercise 7: Date Formatter
Create a function that takes a datetime and returns a human-friendly relative time string like "2 hours ago", "in 3 days", etc.

```python
def relative_time(dt):
    """
    Convert datetime to relative time string.

    Args:
        dt: datetime object

    Returns:
        str: Relative time like "2 hours ago" or "in 3 days"
    """
    pass

# Test
from datetime import datetime, timedelta
now = datetime.now()
print(relative_time(now - timedelta(hours=2)))    # "2 hours ago"
print(relative_time(now + timedelta(days=3)))     # "in 3 days"
print(relative_time(now - timedelta(minutes=30))) # "30 minutes ago"
```

## Exercise 8: Week Number Calculator
Write a function that returns all dates in a given ISO week number for a year.

```python
def get_week_dates(year, week_number):
    """
    Get all dates in a given ISO week.

    Args:
        year: int, year
        week_number: int, ISO week number (1-53)

    Returns:
        list: List of date objects (Monday to Sunday)
    """
    pass

# Test
dates = get_week_dates(2024, 10)
for d in dates:
    print(d, d.strftime("%A"))
```

## Exercise 9: End of Month Calculator
Create a function that returns the last day of the month for any given date.

```python
def last_day_of_month(d):
    """
    Get the last day of the month for given date.

    Args:
        d: date object

    Returns:
        date: Last day of that month
    """
    pass

# Test
from datetime import date
print(last_day_of_month(date(2024, 2, 15)))  # 2024-02-29 (leap year)
print(last_day_of_month(date(2023, 2, 15)))  # 2023-02-28
print(last_day_of_month(date(2024, 4, 1)))   # 2024-04-30
```

## Exercise 10: Business Days in Month
Write a function that counts business days in a given month/year.

```python
def count_business_days_in_month(year, month):
    """
    Count business days (Mon-Fri) in a month.

    Args:
        year: int
        month: int (1-12)

    Returns:
        int: Number of business days
    """
    pass

# Test
print(count_business_days_in_month(2024, 3))  # March 2024
print(count_business_days_in_month(2024, 2))  # February 2024
```

## Exercise 11: Time Duration Parser
Create a function that parses duration strings like "2h 30m", "1d 3h", "45m" and returns a timedelta.

```python
def parse_duration(duration_str):
    """
    Parse duration string to timedelta.
    Supports: d (days), h (hours), m (minutes), s (seconds)

    Args:
        duration_str: str like "2h 30m" or "1d 3h 45m"

    Returns:
        timedelta object
    """
    pass

# Test
from datetime import timedelta
print(parse_duration("2h 30m"))      # 2:30:00
print(parse_duration("1d 3h"))       # 1 day, 3:00:00
print(parse_duration("45m"))         # 0:45:00
print(parse_duration("2d 4h 30m"))   # 2 days, 4:30:00
```

## Exercise 12: Overlapping Date Ranges
Write a function that finds the overlap between two date ranges. Return None if no overlap.

```python
def get_overlap(range1, range2):
    """
    Find overlap between two date ranges.

    Args:
        range1: tuple of (start_date, end_date)
        range2: tuple of (start_date, end_date)

    Returns:
        tuple: (overlap_start, overlap_end) or None if no overlap
    """
    pass

# Test
from datetime import date
range1 = (date(2024, 3, 1), date(2024, 3, 15))
range2 = (date(2024, 3, 10), date(2024, 3, 20))
print(get_overlap(range1, range2))  # (2024-03-10, 2024-03-15)

range3 = (date(2024, 3, 1), date(2024, 3, 10))
range4 = (date(2024, 3, 15), date(2024, 3, 20))
print(get_overlap(range3, range4))  # None
```

## Exercise 13: Age in Years, Months, Days
Write a function that calculates exact age in years, months, and days.

```python
def exact_age(birth_date):
    """
    Calculate exact age in years, months, and days.

    Args:
        birth_date: date object

    Returns:
        tuple: (years, months, days)
    """
    pass

# Test
from datetime import date
birth = date(1990, 6, 15)
years, months, days = exact_age(birth)
print(f"{years} years, {months} months, {days} days")
```

## Exercise 14: Holiday Checker
Create a function that checks if a date is a US federal holiday.

```python
def is_us_holiday(d):
    """
    Check if date is a US federal holiday.
    Include: New Year's, Independence Day, Christmas
    (You can add more)

    Args:
        d: date object

    Returns:
        bool: True if holiday
    """
    pass

# Test
from datetime import date
print(is_us_holiday(date(2024, 1, 1)))   # True (New Year's)
print(is_us_holiday(date(2024, 7, 4)))   # True (Independence Day)
print(is_us_holiday(date(2024, 12, 25))) # True (Christmas)
print(is_us_holiday(date(2024, 3, 15)))  # False
```

## Exercise 15: Recurring Meeting Dates
Write a function that generates dates for a recurring meeting (e.g., every Tuesday at 2 PM for the next N weeks).

```python
def recurring_meetings(start_date, weekday, num_occurrences):
    """
    Generate recurring meeting dates.

    Args:
        start_date: date object (starting from this date or after)
        weekday: int (0=Monday, 6=Sunday)
        num_occurrences: int, number of meetings

    Returns:
        list: List of date objects
    """
    pass

# Test
from datetime import date
# Next 5 Tuesdays starting from March 1, 2024
meetings = recurring_meetings(date(2024, 3, 1), 1, 5)
for meeting in meetings:
    print(meeting, meeting.strftime("%A"))
```

## Bonus Exercise 16: Date Range Merger
Write a function that merges overlapping date ranges.

```python
def merge_date_ranges(ranges):
    """
    Merge overlapping date ranges.

    Args:
        ranges: list of tuples [(start, end), ...]

    Returns:
        list: Merged non-overlapping ranges
    """
    pass

# Test
from datetime import date
ranges = [
    (date(2024, 3, 1), date(2024, 3, 10)),
    (date(2024, 3, 5), date(2024, 3, 15)),
    (date(2024, 3, 20), date(2024, 3, 25)),
    (date(2024, 3, 23), date(2024, 3, 30)),
]
merged = merge_date_ranges(ranges)
print(merged)  # [(2024-03-01, 2024-03-15), (2024-03-20, 2024-03-30)]
```
