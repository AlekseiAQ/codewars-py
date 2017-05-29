"""Find Duplicates 
https://www.codewars.com/kata/find-duplicates

Given an array, find the duplicates in that array, and return a new array of those duplicates.

__*Note*__: numbers and their corresponding string representations should not be treated as duplicates (i.e., `'1' !== 1`).
"""


def duplicates(array):
    seen = []
    dups = []
    for elem in array:
        if elem not in seen:
            seen.append(elem)
        elif elem not in dups:
            dups.append(elem)    
    return dups
