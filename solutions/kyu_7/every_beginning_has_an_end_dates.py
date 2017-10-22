"""Every beginning has an end (Dates)
https://www.codewars.com/kata/every-beginning-has-an-end-dates

I was working with some time series data in Python today and came across this problem and thought it would make a nice little kata for beginners.

###The problem:
You have a time series in Pandas or whatever, indexed by datetime objects. For any date in the time series, you want to find the **date** of the beginning of the week that it is in (Monday in the case of Python) or the end of the week that it is in (Sunday in the case of python).

You may use datetime module where necessary.

As you are going to TDD the solution, I've only stubbed one function, but you will be creating two in total. The tests will guide you as to the functions needed, types expected and returned.
"""

from datetime import timedelta


def week_start_date(dt):
    return dt - timedelta(days=dt.weekday())


def week_end_date(dt):
    return week_start_date(dt) + timedelta(days=6)
