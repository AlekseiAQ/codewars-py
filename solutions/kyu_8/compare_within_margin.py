"""Compare within margin
https://www.codewars.com/kata/compare-within-margin

Create a function `close_compare` that compares two numbers `a` and `b`.

When `a` is lower than `b`, return `-1`.

When `a` is higher than `b`, return `1`.

However when `a` and `b` are the same or close within `margin`, return `0`. Margin may not always be given.

Example: if `a = 3`, `b = 5` and the `margin` is 3, since `a` and `b` are no more than 3 apart, `close_compare` should return `0`. Otherwise, if `margin` is 0, `a` is less than `b` and `close_compare` should return `-1`.

Assume: `margin >= 0`

"""


def close_compare(a, b, margin=0):
    return 0 if abs(a - b) <= margin else -1 if b > a else 1
