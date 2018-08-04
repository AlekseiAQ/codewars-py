"""
Simple Fun #182: Happy 'g'
https://www.codewars.com/kata/simple-fun-number-182-happy-g
"""


from itertools import groupby


def happy_g(s):
    return all(
        char != "g" or sum(1 for _ in group) > 1 for char, group in groupby(s)
    )
