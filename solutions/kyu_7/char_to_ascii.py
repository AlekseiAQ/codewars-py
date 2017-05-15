"""char_to_ascii
https://www.codewars.com/kata/char-to-ascii

Take a string and return a hash with all the ascii values of the characters in the string.
Returns nil if the string is empty.
The key is the character, and the value is the ascii value of the character.
Repeated characters are to be ignored and non-alphebetic characters as well.


"""


def char_to_ascii(strng):
    return {ch: ord(ch) for ch in set(strng) if ch.isalpha()} if strng else None
