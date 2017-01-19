"""Beginner - Reduce but Grow
https://www.codewars.com/kata/beginner-reduce-but-grow

Given and array of integers (x), return the result of multiplying the values together in order. Example:

```
[1, 2, 3] --> 6
```

For the beginner, try to use the reduce method - it comes in very handy quite a lot so is a good one to know.

Array will not be empty.


"""


from functools import reduce
import operator


def grow(arr):
    return reduce(operator.mul, arr)
