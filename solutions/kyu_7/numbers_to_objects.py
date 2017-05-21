"""Numbers  to Objects
https://www.codewars.com/kata/numbers-to-objects

You will be given an array of numbers.

For each number in the array you will need to create an object. 

The object key will be the number, as a string. The value will be the corresponding character code, as a string.

Return an array of the resulting objects.

All inputs will be arrays of numbers. All character codes are valid lower case letters. The input array will not be empty.

"""


def num_obj(s):
    return [{str(n): chr(n)} for n in s]
