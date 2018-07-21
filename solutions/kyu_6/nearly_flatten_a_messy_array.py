"""Nearly Flatten a Messy Array
https://www.codewars.com/kata/nearly-flatten-a-messy-array

You are given an array that of arbitrary depth that needs to be nearly flattened into a 2 dimensional array. The given array's depth is also non-uniform, so some parts may be deeper than others.

All of lowest level arrays (most deeply nested) will contain only integers and none of the higher level arrays will contain anything but other arrays. All arrays given will be at least 2 dimensional. All lowest level arrays will contain at least one element.

Your solution should be an array containing all of the lowest level arrays and only these. The sub-arrays should be ordered by the smallest element within each, so `[1,2]` should preceed `[3,4,5]`. Note: integers will not be repeated.

For example:

If you receive `[[[1,2,3],[4,5]],[6,7]]`, your answer should be `[[1,2,3],[4,5],[6,7]]`.
"""


from itertools import chain


def flatten(list_: list) -> list:
    return [list_] if isinstance(list_[0], int) else\
        chain(*(flatten(l) for l in list_))


def near_flatten(nested: list) -> list:
    return sorted(chain(*(flatten(list_) for list_ in nested)))
