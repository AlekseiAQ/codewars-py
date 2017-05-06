"""Alternate case
https://www.codewars.com/kata/alternate-case

Write function alternateCase which switch every letter in string from upper to lower and from lower to upper.
E.g: Hello World -> hELLO wORLD
"""


def alternateCase(s):
    """ alternate_case == PEP8 (forced mixedCase by CodeWars) """
    return s.swapcase()
