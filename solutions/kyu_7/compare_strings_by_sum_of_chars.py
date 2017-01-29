"""Compare Strings by Sum of Chars
https://www.codewars.com/kata/compare-strings-by-sum-of-chars

Compare two strings by comparing the sum of their values (ASCII character code).<br>
For comparing treat all letters as UpperCase.

Null-Strings should be treated as if they are empty strings.<br>
If the string contains other characters than letters, treat the whole string as it would be empty.<br>

Examples:<br>
<br>
"AD","BC" -> equal<br>
<br>
"AD","DD" -> not equal<br>
<br>
"gf","FG" -> equal<br>
<br>
"zz1","" -> equal<br>
<br>
"ZzZz", "ffPFF" -> equal<br>
<br>
"kl", "lz" -> not equal<br>
<br>
null, "" -> equal<br>

Your method should return true, if the strings are equal and false if they are not equal.
"""


def calc_value(s):
    try:
        return s.isalpha() and sum(ord(a) for a in s.upper())
    except AttributeError:
        return 0


def compare(s1, s2):
    return calc_value(s1) == calc_value(s2)
