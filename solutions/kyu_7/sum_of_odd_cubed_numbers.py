"""Sum of Odd Cubed Numbers
https://www.codewars.com/kata/sum-of-odd-cubed-numbers

Find the sum of the odd numbers within an array, after cubing the initial integers. This function will return `undefined` (`NULL` in PHP) if any of the values aren't numbers.

Note: There are ONLY integers in the JAVA and C# versions of this Kata.
"""


def cube_odd(arr):
    try:
        return sum([elem ** 3 for elem in arr if elem % 2 != 0])
    except TypeError:
        return None
