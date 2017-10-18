"""Alphabet symmetry
https://www.codewars.com/kata/alphabet-symmetry

Consider the word `"abode"`. We can see that the letter `a` is in position `1` and `b` is in position `2`. In the alphabet, `a` and `b` are also in positions `1` and `2`. Notice that `d` and `e` also occupy the positions they would occupy in the alphabet, which are positions `4` and `5`.

Given an array of words, return an array of the number of letters that occupy their positions in the alpahabet for each word. For example, `solve(["abode","ABc","xyzD"]) = [4,3,1]`. See test cases for more examples.

Input will consist of alphabet characters, both uppercase and lowercase. No spaces.

Good luck!
"""


from string import ascii_lowercase as alphabet


def solve(arr):
    return [sum(character == alphabet[i] for
                i, character in enumerate(word[:26].lower())) for word in arr]
