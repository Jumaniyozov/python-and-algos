# Date and Time - Solutions

## Solution 1: Days Until Birthday

```python
from datetime import date

def days_until_birthday(birth_date):
    """Calculate days until next birthday."""
    today = date.today()

    # Get this year's birthday
    this_year_birthday = birth_date.replace(year=today.year)

    # If birthday already passed this year, use next year
    if this_year_birthday < today:
        next_birthday = birth_date.replace(year=today.year + 1)
    else:
        next_birthday = this_year_birthday

    return (next_birthday - today).days

# Test
birth = date(1990, 6, 15)
days = days_until_birthday(birth)
print(f"Days until birthday: {days}")
```

## Solution 2: Meeting Scheduler

```python
from datetime import datetime

def has_conflict(new_meeting, existing_meetings):
    """Check if new meeting conflicts with existing ones."""
    new_start, new_end = new_meeting

    for existing_start, existing_end in existing_meetings:
        # Check for overlap
        if new_start < existing_end and new_end > existing_start:
            return True

    return False

# Test
new = (datetime(2024, 3, 15, 10, 0), datetime(2024, 3, 15, 11, 0))
existing = [
    (datetime(2024, 3, 15, 9, 0), datetime(2024, 3, 15, 10, 30)),
    (datetime(2024, 3, 15, 14, 0), datetime(2024, 3, 15, 15, 0)),
]
print(f"Has conflict: {has_conflict(new, existing)}")  # True

# No conflict example
new2 = (datetime(2024, 3, 15, 11, 0), datetime(2024, 3, 15, 12, 0))
print(f"Has conflict: {has_conflict(new2, existing)}")  # False
```

## Solution 3: Time Zone Converter

```python
from datetime import datetime
from zoneinfo import ZoneInfo

def convert_timezone(dt, from_tz, to_tz):
    """Convert datetime from one timezone to another."""
    # Make datetime aware in source timezone
    dt_aware = dt.replace(tzinfo=ZoneInfo(from_tz))

    # Convert to target timezone
    dt_converted = dt_aware.astimezone(ZoneInfo(to_tz))

    # Format nicely
    return dt_converted.strftime("%Y-%m-%d %H:%M:%S %Z")

# Test
dt = datetime(2024, 3, 15, 14, 0, 0)
result = convert_timezone(dt, "America/New_York", "Asia/Tokyo")
print(result)

result2 = convert_timezone(dt, "UTC", "America/Los_Angeles")
print(result2)
```

## Solution 4: Work Hours Calculator

```python
from datetime import datetime, timedelta, time

def calculate_work_hours(start, end):
    """Calculate work hours between two datetimes (9 AM - 5 PM, Mon-Fri)."""
    work_start = time(9, 0)
    work_end = time(17, 0)
    total_hours = 0.0

    current = start.replace(hour=0, minute=0, second=0, microsecond=0)
    end_date = end.replace(hour=0, minute=0, second=0, microsecond=0)

    while current <= end_date:
        # Skip weekends
        if current.weekday() < 5:  # Monday = 0, Friday = 4
            # Determine work period for this day
            day_start = max(start if current.date() == start.date() else
                          datetime.combine(current.date(), work_start), start)
            day_end = min(end if current.date() == end.date() else
                        datetime.combine(current.date(), work_end), end)

            # Clip to work hours
            work_day_start = datetime.combine(current.date(), work_start)
            work_day_end = datetime.combine(current.date(), work_end)

            day_start = max(day_start, work_day_start)
            day_end = min(day_end, work_day_end)

            # Add hours if valid range
            if day_start < day_end:
                hours = (day_end - day_start).total_seconds() / 3600
                total_hours += hours

        current += timedelta(days=1)

    return total_hours

# Test
start = datetime(2024, 3, 15, 8, 0)   # Friday 8 AM
end = datetime(2024, 3, 18, 17, 0)    # Monday 5 PM
print(f"Work hours: {calculate_work_hours(start, end)}")
```

## Solution 5: Quarter Finder

```python
from datetime import date

def get_quarter(d):
    """Get the quarter for a given date."""
    quarter = (d.month - 1) // 3 + 1
    return f"Q{quarter}"

# Test
print(get_quarter(date(2024, 1, 15)))   # Q1
print(get_quarter(date(2024, 6, 15)))   # Q2
print(get_quarter(date(2024, 9, 15)))   # Q3
print(get_quarter(date(2024, 12, 15)))  # Q4

# Alternative with detailed info
def get_quarter_info(d):
    """Get quarter with start and end dates."""
    quarter = (d.month - 1) // 3 + 1
    start_month = (quarter - 1) * 3 + 1
    end_month = start_month + 2

    start = date(d.year, start_month, 1)

    # Last day of quarter
    if end_month == 12:
        end = date(d.year, 12, 31)
    else:
        next_quarter_start = date(d.year, end_month + 1, 1)
        end = next_quarter_start - timedelta(days=1)

    return f"Q{quarter}", start, end

# Test
from datetime import timedelta
q, start, end = get_quarter_info(date(2024, 6, 15))
print(f"{q}: {start} to {end}")
```

## Solution 6: Month Iterator

```python
from datetime import date

def month_range(start_date, end_date):
    """Generate first day of each month in range."""
    current = date(start_date.year, start_date.month, 1)
    end = date(end_date.year, end_date.month, 1)

    while current <= end:
        yield current

        # Move to next month
        if current.month == 12:
            current = date(current.year + 1, 1, 1)
        else:
            current = date(current.year, current.month + 1, 1)

# Test
print("First day of each month:")
for first_day in month_range(date(2024, 1, 15), date(2024, 6, 20)):
    print(first_day.strftime("%B %Y"))
```

## Solution 7: Date Formatter

```python
from datetime import datetime, timedelta

def relative_time(dt):
    """Convert datetime to relative time string."""
    now = datetime.now()
    diff = dt - now

    # Future or past
    is_future = diff.total_seconds() > 0
    diff = abs(diff)

    seconds = diff.total_seconds()
    minutes = seconds / 60
    hours = minutes / 60
    days = diff.days

    # Determine unit
    if seconds < 60:
        value, unit = int(seconds), "second"
    elif minutes < 60:
        value, unit = int(minutes), "minute"
    elif hours < 24:
        value, unit = int(hours), "hour"
    elif days < 30:
        value, unit = days, "day"
    elif days < 365:
        value, unit = days // 30, "month"
    else:
        value, unit = days // 365, "year"

    # Plural
    if value != 1:
        unit += "s"

    # Format
    if is_future:
        return f"in {value} {unit}"
    else:
        return f"{value} {unit} ago"

# Test
now = datetime.now()
print(relative_time(now - timedelta(seconds=30)))
print(relative_time(now - timedelta(minutes=45)))
print(relative_time(now - timedelta(hours=2)))
print(relative_time(now - timedelta(days=5)))
print(relative_time(now + timedelta(days=3)))
print(relative_time(now + timedelta(hours=12)))
```

## Solution 8: Week Number Calculator

```python
from datetime import date, timedelta

def get_week_dates(year, week_number):
    """Get all dates in a given ISO week."""
    # Get January 4th (always in week 1)
    jan_4 = date(year, 1, 4)

    # Find Monday of week 1
    week_1_monday = jan_4 - timedelta(days=jan_4.weekday())

    # Find Monday of target week
    target_monday = week_1_monday + timedelta(weeks=week_number - 1)

    # Generate all 7 days
    return [target_monday + timedelta(days=i) for i in range(7)]

# Test
dates = get_week_dates(2024, 10)
print(f"ISO Week 10 of 2024:")
for d in dates:
    print(f"{d} - {d.strftime('%A')}")

# Verify with isocalendar
print(f"\nVerification: {dates[0].isocalendar()}")
```

## Solution 9: End of Month Calculator

```python
from datetime import date
import calendar

def last_day_of_month(d):
    """Get the last day of the month for given date."""
    # Get number of days in month
    _, num_days = calendar.monthrange(d.year, d.month)
    return date(d.year, d.month, num_days)

# Alternative without calendar module
def last_day_of_month_alt(d):
    """Get last day of month without calendar module."""
    # Go to first of next month, then back one day
    if d.month == 12:
        next_month = date(d.year + 1, 1, 1)
    else:
        next_month = date(d.year, d.month + 1, 1)

    from datetime import timedelta
    return next_month - timedelta(days=1)

# Test
print(last_day_of_month(date(2024, 2, 15)))  # 2024-02-29 (leap year)
print(last_day_of_month(date(2023, 2, 15)))  # 2023-02-28
print(last_day_of_month(date(2024, 4, 1)))   # 2024-04-30
print(last_day_of_month(date(2024, 12, 1)))  # 2024-12-31

print("\nAlternative method:")
print(last_day_of_month_alt(date(2024, 2, 15)))
```

## Solution 10: Business Days in Month

```python
from datetime import date
import calendar

def count_business_days_in_month(year, month):
    """Count business days (Mon-Fri) in a month."""
    _, num_days = calendar.monthrange(year, month)
    count = 0

    for day in range(1, num_days + 1):
        d = date(year, month, day)
        if d.weekday() < 5:  # Monday=0 to Friday=4
            count += 1

    return count

# Test
print(f"Business days in March 2024: {count_business_days_in_month(2024, 3)}")
print(f"Business days in February 2024: {count_business_days_in_month(2024, 2)}")
print(f"Business days in December 2024: {count_business_days_in_month(2024, 12)}")

# Verify with manual calculation
year, month = 2024, 3
_, num_days = calendar.monthrange(year, month)
print(f"\nMarch 2024 has {num_days} days")
print(f"First day is {calendar.day_name[date(year, month, 1).weekday()]}")
```

## Solution 11: Time Duration Parser

```python
from datetime import timedelta
import re

def parse_duration(duration_str):
    """Parse duration string to timedelta."""
    # Pattern: number followed by unit (d, h, m, s)
    pattern = r'(\d+)([dhms])'
    matches = re.findall(pattern, duration_str.lower())

    units = {
        'd': 'days',
        'h': 'hours',
        'm': 'minutes',
        's': 'seconds'
    }

    kwargs = {}
    for value, unit in matches:
        unit_name = units.get(unit)
        if unit_name:
            kwargs[unit_name] = int(value)

    return timedelta(**kwargs)

# Test
print(parse_duration("2h 30m"))      # 2:30:00
print(parse_duration("1d 3h"))       # 1 day, 3:00:00
print(parse_duration("45m"))         # 0:45:00
print(parse_duration("2d 4h 30m"))   # 2 days, 4:30:00
print(parse_duration("90s"))         # 0:01:30

# Use in calculation
from datetime import datetime
now = datetime.now()
future = now + parse_duration("2h 30m")
print(f"\nNow: {now.strftime('%H:%M:%S')}")
print(f"Future: {future.strftime('%H:%M:%S')}")
```

## Solution 12: Overlapping Date Ranges

```python
from datetime import date

def get_overlap(range1, range2):
    """Find overlap between two date ranges."""
    start1, end1 = range1
    start2, end2 = range2

    # Find overlap start (later of two starts)
    overlap_start = max(start1, start2)

    # Find overlap end (earlier of two ends)
    overlap_end = min(end1, end2)

    # Check if valid overlap
    if overlap_start <= overlap_end:
        return (overlap_start, overlap_end)
    else:
        return None

# Test
range1 = (date(2024, 3, 1), date(2024, 3, 15))
range2 = (date(2024, 3, 10), date(2024, 3, 20))
overlap = get_overlap(range1, range2)
print(f"Overlap: {overlap}")  # (2024-03-10, 2024-03-15)

range3 = (date(2024, 3, 1), date(2024, 3, 10))
range4 = (date(2024, 3, 15), date(2024, 3, 20))
overlap = get_overlap(range3, range4)
print(f"Overlap: {overlap}")  # None

# Adjacent ranges
range5 = (date(2024, 3, 1), date(2024, 3, 10))
range6 = (date(2024, 3, 10), date(2024, 3, 20))
overlap = get_overlap(range5, range6)
print(f"Adjacent overlap: {overlap}")  # (2024-03-10, 2024-03-10)
```

## Solution 13: Age in Years, Months, Days

```python
from datetime import date

def exact_age(birth_date):
    """Calculate exact age in years, months, and days."""
    today = date.today()

    # Calculate years
    years = today.year - birth_date.year

    # Calculate months
    months = today.month - birth_date.month

    # Calculate days
    days = today.day - birth_date.day

    # Adjust if days negative
    if days < 0:
        months -= 1
        # Days in previous month
        if today.month == 1:
            prev_month = date(today.year - 1, 12, 1)
        else:
            prev_month = date(today.year, today.month - 1, 1)

        # Get days in previous month
        import calendar
        _, days_in_prev = calendar.monthrange(prev_month.year, prev_month.month)
        days = days_in_prev + days

    # Adjust if months negative
    if months < 0:
        years -= 1
        months = 12 + months

    return (years, months, days)

# Test
birth = date(1990, 6, 15)
years, months, days = exact_age(birth)
print(f"Age: {years} years, {months} months, {days} days")

# Edge cases
birth2 = date(2020, 2, 29)  # Leap year birthday
years2, months2, days2 = exact_age(birth2)
print(f"Leap year birth: {years2} years, {months2} months, {days2} days")
```

## Solution 14: Holiday Checker

```python
from datetime import date

def is_us_holiday(d):
    """Check if date is a US federal holiday."""
    year = d.year
    month = d.month
    day = d.day

    # Fixed date holidays
    fixed_holidays = [
        (1, 1),    # New Year's Day
        (7, 4),    # Independence Day
        (11, 11),  # Veterans Day
        (12, 25),  # Christmas
    ]

    if (month, day) in fixed_holidays:
        return True

    # MLK Day - 3rd Monday in January
    if month == 1 and d.weekday() == 0:
        # Count Mondays in January up to this date
        monday_count = (day - 1) // 7 + 1
        if monday_count == 3 and day >= 15 and day <= 21:
            return True

    # Memorial Day - Last Monday in May
    if month == 5 and d.weekday() == 0:
        # Check if this is last Monday
        next_week = date(year, month, day + 7) if day + 7 <= 31 else None
        if next_week is None or next_week.month != 5:
            return True

    # Labor Day - 1st Monday in September
    if month == 9 and d.weekday() == 0 and day <= 7:
        return True

    # Thanksgiving - 4th Thursday in November
    if month == 11 and d.weekday() == 3:
        thursday_count = (day - 1) // 7 + 1
        if thursday_count == 4 and day >= 22 and day <= 28:
            return True

    return False

# Test
holidays = [
    date(2024, 1, 1),    # New Year's
    date(2024, 7, 4),    # Independence Day
    date(2024, 12, 25),  # Christmas
    date(2024, 1, 15),   # MLK Day
    date(2024, 9, 2),    # Labor Day
]

for d in holidays:
    print(f"{d} ({d.strftime('%A')}): {is_us_holiday(d)}")

print(f"\nRegular day: {is_us_holiday(date(2024, 3, 15))}")
```

## Solution 15: Recurring Meeting Dates

```python
from datetime import date, timedelta

def recurring_meetings(start_date, weekday, num_occurrences):
    """Generate recurring meeting dates."""
    meetings = []

    # Find first occurrence on or after start_date
    days_ahead = (weekday - start_date.weekday()) % 7
    if days_ahead == 0 and start_date.weekday() == weekday:
        current = start_date
    else:
        current = start_date + timedelta(days=days_ahead)

    # Generate occurrences
    for _ in range(num_occurrences):
        meetings.append(current)
        current += timedelta(weeks=1)

    return meetings

# Test
# Next 5 Tuesdays starting from March 1, 2024
meetings = recurring_meetings(date(2024, 3, 1), 1, 5)  # 1 = Tuesday
print("Next 5 Tuesdays:")
for meeting in meetings:
    print(f"{meeting} - {meeting.strftime('%A')}")

# Next 4 Fridays starting from today
from datetime import date
meetings2 = recurring_meetings(date.today(), 4, 4)  # 4 = Friday
print("\nNext 4 Fridays:")
for meeting in meetings2:
    print(meeting)
```

## Solution 16: Date Range Merger

```python
from datetime import date

def merge_date_ranges(ranges):
    """Merge overlapping date ranges."""
    if not ranges:
        return []

    # Sort by start date
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    merged = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        # Check if overlapping or adjacent
        if current_start <= last_end + timedelta(days=1):
            # Merge by extending end date
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add as new range
            merged.append((current_start, current_end))

    return merged

# Test
from datetime import timedelta

ranges = [
    (date(2024, 3, 1), date(2024, 3, 10)),
    (date(2024, 3, 5), date(2024, 3, 15)),
    (date(2024, 3, 20), date(2024, 3, 25)),
    (date(2024, 3, 23), date(2024, 3, 30)),
]
merged = merge_date_ranges(ranges)
print("Merged ranges:")
for start, end in merged:
    print(f"  {start} to {end}")

# Test with adjacent ranges
ranges2 = [
    (date(2024, 3, 1), date(2024, 3, 5)),
    (date(2024, 3, 6), date(2024, 3, 10)),
    (date(2024, 3, 15), date(2024, 3, 20)),
]
merged2 = merge_date_ranges(ranges2)
print("\nAdjacent ranges merged:")
for start, end in merged2:
    print(f"  {start} to {end}")
```
