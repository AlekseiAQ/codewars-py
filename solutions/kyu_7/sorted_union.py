"""Sorted Union
https://www.codewars.com/kata/sorted-union

Write a function that takes one or more arrays and returns a new array of unique values in the order of the original provided arrays.

In other words, all values present from all arrays should be included in their original order, but with no duplicates in the final array.

The unique numbers should be sorted by their original order, but the final array should not be sorted in numerical order.

Check the assertion tests for examples.

*Courtesy of [FreeCodeCamp](https://www.freecodecamp.com/challenges/sorted-union), a great place to learn web-dev; plus, its founder Quincy Larson is pretty cool and amicable. I made the original one slightly more tricky ;)*
"""


from itertools import chain


def unite_unique(*args):
    tmp = []    
    for item in chain(*args):
        if item not in tmp:
            tmp.append(item)
    return tmp
