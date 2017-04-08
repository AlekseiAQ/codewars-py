"""Reverse and Invert
https://www.codewars.com/kata/reverse-and-invert

Reverse and invert all integer values in a given list. 

Python:

    reverse_invert([1,12,'a',3.4,87,99.9,-42,50,5.6]) = [-1,-21,-78,24,-5]
    
Ignore all other types than integer.
"""


def reverse_invert(lst):
    return [-int(str(abs(n))[::-1]) if n > 0 else int(str(abs(n))[::-1]) for n in lst if isinstance(n, int)]
