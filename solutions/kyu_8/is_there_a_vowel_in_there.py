"""Is there a vowel in there?
https://www.codewars.com/kata/is-there-a-vowel-in-there

Given an array of numbers (s), check if any of the numbers are the character codes for lower case vowels.

If they are, change the array value to a string of that vowel.

Return the resulting array.
"""


def is_vow(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]
