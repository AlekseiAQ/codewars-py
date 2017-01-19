# pylint: disable=bare-except
"""Parse float
https://www.codewars.com/kata/parse-float

Write function `parseFloat` (for Javascript `parseF`) which takes a string and returns a number or `Nothing` (for Python `None`, for Javascript `null`) if conversion is not possible.
"""


def parse_float(string):
    try:
        return float(string)
    except:
        pass
