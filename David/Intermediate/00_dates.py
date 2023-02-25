## Dates ##

# import datetime

# now = datetime.datetime

from datetime import date
from datetime import time
from datetime import datetime


def print_date(date: datetime):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


now = datetime.now()

print_date(now)

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)


current_time = time(1, 30, 50)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023, 11, 7)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date.year