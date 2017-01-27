"""Powers of 2
https://www.codewars.com/kata/powers-of-2

Write a function ```powersOfTwo``` which will return list of all powers of 2 from 0 to n (where n is an exponent).

E.g:

n = 0 -> 2^0           -> [1]

n = 1 -> 2^0, 2^1      -> [1,2]

n = 2 -> 2^0, 2^1, 2^2 -> [1,2,4]
"""


def powers_of_two(n):
    return [2 ** i for i in range(n+1)] 
