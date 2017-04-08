"""Which string is worth more?
https://www.codewars.com/kata/which-string-is-worth-more

You will be given two ASCII strings, `a` and `b`. Your task is write a function to determine which one of these strings is "worth" more, and return it.

A string's worth is determined by the sum of its ASCII codepoint indexes. So, for example, the string `HELLO` has a value of 372: H is codepoint 72, E 69, L 76, and O is 79. The sum of these values is 372.

In the event of a tie, you should return the first string, i.e. `a`.
"""


def value(s):
    return sum(ord(ch) for ch in s)

def highest_value(a, b):
    return a if value(a) >= value(b) else b
