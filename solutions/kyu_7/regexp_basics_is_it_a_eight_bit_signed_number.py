"""Regexp Basics - is it a eight bit signed number?
https://www.codewars.com/kata/regexp-basics-is-it-a-eight-bit-signed-number

Implement `String.eight_bit_signed_number?` (Ruby), `String.eightBitSignedNumber()` (Python), `eight_bit_signed_number()` (JS) or `StringUtils.isSignedEightBitNumber(String)` (Java) which should return `true/True` if given object is a number representable by 8 bit signed integer (-128 to -1 or 0 to 127), `false/False` otherwise.

It should only accept numbers in canonical representation, so no leading `+`, extra `0`s, spaces etc.
"""


def signed_eight_bit_number(number):
    return number in map(str, range(-128, 128))
