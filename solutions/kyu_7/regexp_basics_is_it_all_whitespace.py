"""Regexp Basics - is it all whitespace?
https://www.codewars.com/kata/regexp-basics-is-it-all-whitespace

Implement `String#whitespace?(str)` (Ruby), `String.prototype.whitespace(str)` (JavaScript), `String::whitespace(str)` (CoffeeScript), or `whitespace(str)` (Python), which should return `true/True` if given object consists exclusively of zero or more whitespace characters, `false/False` otherwise.
"""


import re


REGEX = re.compile(r'\s*$')

def whitespace(string):
    return bool(re.match(REGEX, string))
