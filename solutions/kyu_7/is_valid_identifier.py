"""Is valid identifier?
https://www.codewars.com/kata/is-valid-identifier

Given a string, determine if it's a valid identifier.

##Here is the syntax for valid identifiers:
* Each identifier must have at least one character.
* The first character must be picked from: alpha, underscore, or dollar sign. The first character can not be a digit.
* The rest of the characters (besides the first) can be from: alpha, digit, underscore, or dollar sign. In other words, it can be any valid identifier character.

###Examples of valid identifiers:
* i
* wo_rd
* b2h

###Examples of invalid identifiers:
* 1i
* wo rd 
* !b2h
"""


import re


def is_valid(idn):
    return re.match('^[a-zA-Z_\$][a-zA-Z0-9_\$]*$', idn) != None
