"""Simple Fun #290: Sum Of Threes
https://www.codewars.com/kata/simple-fun-number-290-sum-of-threes

# Task
Given a number `n`, return a string representing it as a sum of distinct powers of three, or return `"Impossible"` if that's not possible to achieve.


# Input/Output


`[input]` integer `n`


A positive integer n.

`1 ≤ n ≤ 10^16`.

`[output]` a string

A string representing the sum of powers of three which adds up to n, or `"Impossible"` if there is no solution. If the solution does exist, it should be return as `"3^a1+3^a2+ ... +3^an"`, where ai for `0 ≤ i ≤ n` represents the corresponding exponent of the term. The terms in the string should also be sorted in descending order, meaning that higher powers should appear before the lower ones in the string (`"3^0+3^1"` is incorrect, whereas `"3^1+3^0"` is correct).

# Example

For `n = 4`, the output should be `"3^1+3^0"`.

4 can be represented as `3+1` which is in fact 3 to the power of 1 plus 3 to the power of 0

For `n = 2`, the output should be `"Impossible"`.

There is no way to represent 2 as a sum of `distinct powers` of 3.
"""


import numpy as np


def sum_of_threes(n: int) -> str:
    s = np.base_repr(n, 3)
    print
    if '2' in s:
        return 'Impossible'
    return '+'.join(
        ['3^{}'.format(i) for i, elem in enumerate(s[::-1]) if
         elem == '1'][::-1])
