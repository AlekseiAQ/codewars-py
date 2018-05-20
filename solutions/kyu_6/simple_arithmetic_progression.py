"""Simple arithmetic progression
https://www.codewars.com/kata/simple-arithmetic-progression

In this Kata, you will be given an array of integers and your task is to return the number of arithmetic progressions of size `3` that are possible from that list. In each progression, the differences between the elements must be the same.

```js
[1, 2, 3, 5, 7, 9] ==> 5
// [1, 2, 3], [1, 3, 5], [1, 5, 9], [3, 5, 7], and [5, 7, 9]
```

All inputs will be sorted. More examples in test cases.

Good luck!
"""


from itertools import combinations


def solve(arr):
    return sum(1 for a, b, c in combinations(arr, 3) if a - b == b - c)
