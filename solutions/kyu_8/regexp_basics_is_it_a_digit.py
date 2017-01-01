"""Regexp Basics - is it a digit?
https://www.codewars.com/kata/regexp-basics-is-it-a-digit

Implement `String#digit?` (in Java `StringUtils.isDigit(String)`), which should return `true` if given object is a digit (0-9), `false` otherwise.
"""


def is_digit(n):
    return n.isdigit() and len(n)==1
