"""Age in days
https://www.codewars.com/kata/age-in-days

Did you ever want to know how many days you are old?
Write a function ageInDays which returns your age in days.

For example if today is 30 November 2015 then
```python
ageInDays(2015, 11, 1) returns "You are 29 days old"
```

The birthday is entered as integers in the following order
```python
ageInDays(year, month, day)
```
For example if you are born 27 November 2007 then call ageInDays(2007, 11, 27).

Your birthday is expected to be in the past.

Suggestions on how to improve the kata are welcome!


"""


from datetime import date


def ageInDays(year, month, day):
    """ age_in_days == PEP8 (forced mixedCase by CodeWars) """
    days = (date.today() - date(year, month, day)).days
    return "You are {} day{} old".format(days, '' if days == 1 else 's')
