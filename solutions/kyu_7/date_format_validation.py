"""Date Format Validation
https://www.codewars.com/kata/date-format-validation

Create a function that will return ```true``` if the input is in the following date time format ```01-09-2016 01:20``` and ```false``` if it is not.

This Kata has been inspired by the Regular Expressions chapter from the book Eloquent JavaScript.
"""


from re import match


def date_checker(date):
    return bool(match(r'\d{2}-\d{2}-\d{4}\s\d{2}:\d{2}', date))
