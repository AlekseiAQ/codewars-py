"""Unary function chainer
https://www.codewars.com/kata/unary-function-chainer

Your task is to write a higher order function for chaining together
a list of unary functions. In other words, it should return a function
that does a left fold on the given functions.

```python
chained([a,b,c,d])(input)
```
Should yield the same result as
```python
d(c(b(a(input))))
```
"""


def chained(functions):
    def composite(arg):
        for function in functions:
            arg = function(arg)
        return arg
    return composite
