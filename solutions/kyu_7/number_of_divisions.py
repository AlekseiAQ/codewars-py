"""Number of Divisions
https://www.codewars.com/kata/number-of-divisions

Calculate how many times a number can be divided by a given number.

### Example

For example the number `6` can be divided by `2` two times:
```py
1. 6 / 2 = 3
2. 3 / 2 = 1 remainder = 1
```
`100` can be divided by `2` six times:

```py
1. 100 / 2 = 50
2. 50 / 2 = 25
3. 25 / 2 = 12 remainder 1
4. 12 / 2 = 6
5. 6 / 2 = 3
6. 3 / 2 = 1 remainder 1
```
"""


from math import log


def divisions(number, divisor):
    return int(log(number, divisor))
