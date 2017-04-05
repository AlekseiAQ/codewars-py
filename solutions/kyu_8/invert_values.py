"""Invert values
https://www.codewars.com/kata/invert-values

Invert a given list of integer values.

Python/JS/PHP:

    invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
    invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
    invert([]) == []
    
You can assume that all values are integers.
"""


def invert(lst):
    return [-x for x in lst]
