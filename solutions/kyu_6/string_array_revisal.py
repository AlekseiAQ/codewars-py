"""String  array revisal
https://www.codewars.com/kata/string-array-revisal

In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

For example:

  * `dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"]`.

  * `dup(["kelless","keenness"]) = ["keles","kenes"]`.

Strings will be alphabet characters only. Don't worry about lower and upper case. See test cases for more examples.

Good luck!

If you like this Kata, please try:

[Alternate capitalization](https://www.codewars.com/kata/59cfc000aeb2844d16000075)

[Vowel consonant lexicon](https://www.codewars.com/kata/59cf8bed1a68b75ffb000026)
"""


from itertools import groupby

def dup(arry):
    return ["".join(char for char, _ in groupby(string_)) for
            string_ in arry]
