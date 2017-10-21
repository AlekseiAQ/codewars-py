"""Unlucky Days
https://www.codewars.com/kata/unlucky-days

_Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year._

Find the number of Friday 13th in the given year.

__Input:__ Year as an integer.

__Output:__ Number of Black Fridays in the year as an integer.

__Precondition:__ 1000 < |year| < 3000

__Examples:__

    unluckyDays(2015) == 3
    unluckyDays(1986) == 1

***Note:*** for Ruby consider using the Gregorian Calendar instead of the default one (Italian), to have results coherent with other languages.
"""


from calendar import weekday


def unlucky_days(year):
    return sum(weekday(year, month, 13) == 4 for month in range(1, 13))
