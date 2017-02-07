"""Reduce My Fraction
https://www.codewars.com/kata/reduce-my-fraction

Write a function which reduces fractions to their simplest form! Fractions will be presented as an array, and the reduced fraction must be returned as an array:

```javascript
input: [numerator, denominator]   output: [newNumerator, newDenominator]
                    Eg: [45, 120] --> [3, 8]
```
All numerators and denominators will be positive integers.

Note: This is an introductory Kata for a series... coming soon!
"""


from fractions import Fraction


def reduce_(fraction):
    fraction = Fraction(*fraction)
    return [fraction.numerator, fraction.denominator]
