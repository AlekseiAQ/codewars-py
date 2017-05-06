"""Transpose two strings in an array
https://www.codewars.com/kata/transpose-two-strings-in-an-array

You will be given an array that contains two strings. Your job is to create a function that will take those two strings and transpose them, so that the strings go from top to bottom instead of left to right.
```javascript
e.g. transposeTwoStrings(['Hello','World']);

should return

H W  
e o  
l r  
l l  
o d
```
A few things to note:

1. There should be one space in between the two characters
2. You don't have to modify the case (i.e. no need to change to upper or lower)
3. If one string is longer than the other, there should be a space where the character would be

"""


from itertools import zip_longest


def transpose_two_strings(arr):
    return '\n'.join(' '.join(x) for x in zip_longest(*arr, fillvalue=' '))
