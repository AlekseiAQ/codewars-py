"""Pairs of integers from 0 to n
https://www.codewars.com/kata/pairs-of-integers-from-0-to-n

Write a function `generatePairs` that accepts an integer argument `n` and generates an array containing the pairs of integers `[a, b]` that satisfy the following conditions:
```
0 <= a <= b <= n
```

The pairs should be sorted by increasing values of `a` then increasing values of `b`.

For example, `generatePairs(2)` should return
```
[ [0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2] ]
```
"""


from itertools import combinations_with_replacement


def generate_pairs(n):
    return [list(x) for x in combinations_with_replacement(range(n+1), 2)]
