"""Sum of integers in string
https://www.codewars.com/kata/sum-of-integers-in-string

Your task in this kata is to implement a function that calculates the sum of the integers inside a string. For example, in the string <code>"The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"</code>, the sum of the integers is <code>3635</code>.

*Note: only positive integers will be tested.*
"""


import re


def sum_of_integers_in_string(s: str) -> int:
    return sum(map(int, re.findall(r'\d+', s)))
