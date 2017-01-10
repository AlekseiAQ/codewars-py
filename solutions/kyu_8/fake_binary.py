"""Fake Binary
https://www.codewars.com/kata/fake-binary

Given a string of numbers, you should replace any number below 5 with '0' and any number 5 and above with '1'. Return the resulting string.
"""


def fake_bin(x):
    return ''.join('0' if int(el) < 5 else '1' for el in x)
