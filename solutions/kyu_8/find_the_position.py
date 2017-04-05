"""Find the position!
https://www.codewars.com/kata/find-the-position

When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1"

`This kata is meant for beginners. Rank and upvote to bring it out of beta`

"""


def position(alphabet):
    return "Position of alphabet: %s" % (ord(alphabet) - 96)
