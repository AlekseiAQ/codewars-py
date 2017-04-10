"""Format to the 2nd
https://www.codewars.com/kata/format-to-the-2nd

Given some positive integers, I wish to print the integers such that all take up the same width by adding a minimum number of leading zeroes. No leading zeroes shall be added to the largest integer.

For example, given `1, 23, 2, 17, 102`, I wish to print out these numbers as follows:

```Python
001
023
002
017
102```

Write a function `print_nums(n1, n2, n3, ...)` that takes a variable number of arguments and returns the string to be printed out.
"""


def print_nums(*args):
    if args:
        l = len(str(max(args)))
        return '\n'.join(str(arg).zfill(l) for arg in args)
    return ''
