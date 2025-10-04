import pandas as pd  
import numpy as np  
import datetime as dt 

# ------------------------------
# CREATING TIMESTAMP OBJECTS
# ------------------------------

# Creating a Timestamp object for a specific date
dd = pd.Timestamp('2025/8/1')
print(dd)  # 2025-08-01 00:00:00

# Creating a Timestamp with only the year provided
yy = pd.Timestamp('2025')
print(yy)  # 2025-01-01 00:00:00 (defaults to Jan 1st)

# Creating a Timestamp from a textual date
year = pd.Timestamp('4th October 2025')
print(year)  # 2025-10-04 00:00:00

# Creating a Timestamp with both date and time
year_time = pd.Timestamp('4th October 2025 9:21:9 AM')
print(year_time)  # 2025-10-04 09:21:09

# Creating Timestamp from a datetime.datetime object
x = pd.Timestamp(dt.datetime(2025, 2, 6, 12, 11, 43))
print(x)  # 2025-02-06 12:11:43

# ------------------------------
# FETCHING ATTRIBUTES FROM TIMESTAMP
# ------------------------------
print(x.year)    # 2025
print(x.month)   # 2
print(x.day)     # 6
print(x.hour)    # 12
print(x.minute)  # 11
print(x.second)  # 43

# ------------------------------
# DATETIMEINDEX OBJECT
# ------------------------------

# Creating a DatetimeIndex (for multiple datetime values)
dt_ind = pd.DatetimeIndex(['2025/7/1','2025/8/1','2025/9/1'])

# Using DatetimeIndex as Series index
a = pd.Series([1, 2, 3], index=dt_ind)
print(a)
# 2025-07-01    1
# 2025-08-01    2
# 2025-09-01    3
# dtype: int64

# ------------------------------
# DATE RANGE GENERATION
# ------------------------------

# Generate daily dates in a given range
a1 = pd.date_range(start='2025/1/5', end='2025/2/15', freq='D')  # Daily frequency

# Generate dates every 3 days
a2 = pd.date_range(start='2025/1/5', end='2025/2/15', freq='3D')  # Every 3 days

# Generate only business days (Mon-Fri)
a3 = pd.date_range(start='2025/1/5', end='2025/2/15', freq='B')  # Business days

# Generate weekly dates (Sunday by default)
a4 = pd.date_range(start='2025/1/5', end='2025/2/15', freq='W')  # Weekly frequency

# Generate hourly dates
a5 = pd.date_range(start='2025/1/5', end='2025/2/15', freq='H')  # Hourly

# Generate month-end dates
a6 = pd.date_range(start='2025/1/5', end='2025/2/15', freq='M')  # Month-end

# Generate month-start dates
a7 = pd.date_range(start='2025/1/5', end='2025/2/15', freq='MS')  # Month-start

# Generate annual dates (year-end)
a8 = pd.date_range(start='2025/1/5', end='2025/2/15', freq='A')  # Year-end

# Generate a range of 25 hourly periods starting from a given date
a9 = pd.date_range(start='2025/1/5', periods=25, freq='H')  # 25 hourly periods


# ------------------------------
# TO_DATETIME FUNCTION
# ------------------------------
# Convert a Series of strings into datetime objects
s = pd.Series(['2025/7/1', '2025/8/1', '2025/9/1','2025/13/3'])

# Get the day names for each date
ss = pd.to_datetime(s).dt.day_name()
print(ss)  


# Convert strings to datetime with error handling
# If a string cannot be converted, it will be set to NaT
print(pd.to_datetime(s, errors='coerce'))