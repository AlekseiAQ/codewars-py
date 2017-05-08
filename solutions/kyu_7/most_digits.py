"""Most digits
https://www.codewars.com/kata/most-digits

Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.

"""


def find_longest(arr):
    return max(arr, key=lambda x: len(str(x)))
