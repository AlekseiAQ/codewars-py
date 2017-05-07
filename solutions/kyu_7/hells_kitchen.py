"""Hells Kitchen
https://www.codewars.com/kata/hells-kitchen

Gordon Ramsay shouts. He shouts and swears. There may be something wrong with him.

Anyway, you will be given a string of four words. Your job is to turn them in to Gordon language. 

Rules:

Obviously the words should be Caps,
Every word should end with '!!!!',
Any letter 'a' or 'A' should become '@',
Any other vowel should become '*'.

"""


def gordon(a):
    table = str.maketrans('AEUIO', '@****')
    return ' '.join(w + '!!!!' for w in a.upper().translate(table).split(' '))
