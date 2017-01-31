"""Count consonants
https://www.codewars.com/kata/count-consonants

Write a function `consonantCount`, `consonant_count` or `ConsonantCount` that takes a string of English-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels `a, e, i, o, u`.
"""


import re


def consonant_count(s):
    com = re.compile("[bcdfghjklmnpqrstvwxyz]", flags=re.I)
    result = len(com.findall(s))
    return result if result else 0
