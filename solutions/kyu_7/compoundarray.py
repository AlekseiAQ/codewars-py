"""CompoundArray
https://www.codewars.com/kata/compoundarray

You have to create a method "compoundArray" which should take as input two int arrays of different length and return one int array with numbers of both arrays shuffled one by one. 
```Example: 
Input - {1,2,3,4,5,6} and {9,8,7,6} 
Output - {1,9,2,8,3,7,4,6,5,6}
```
"""


from itertools import zip_longest


def compound_array(a, b):
    result = []
    for pair in zip_longest(a, b):
        result.extend(list(filter(lambda value: value != None, pair)))
    return result
