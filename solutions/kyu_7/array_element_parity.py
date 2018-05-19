"""Array element parity
https://www.codewars.com/kata/array-element-parity

In this Kata, you will be given an array of integers whose elements have both a negative and a positive value, except for one integer that is either only negative or only positive. Your task will be to find that integer.

For example,
```Haskell
solve[1,-1,2,-2,3] = 3  --> 3 only has a positive ocurrence.
solve([-3,1,2,3,-1,-4,-2]) = -4  --> -4 only has a negative occurence
solve([1,-1,2,-2,3,3]) = 3  --> the integer that is only positive or only negative my appear more than once.
```
Good luck!
"""


def solve(arr):
    for num in arr:
        if -num not in arr:
            return num
