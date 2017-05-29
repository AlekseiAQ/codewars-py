"""Narcissistic Numbers 
https://www.codewars.com/kata/narcissistic-numbers

A Narcissistic Number is a number of length n in which the sum of its digits to the power of n is equal to the original number. If this seems confusing, refer to the example below.

Ex: 153, where n = 3 (number of digits in 153)<br/>
1<sup>3</sup> + 5<sup>3</sup> + 3<sup>3</sup> = 153

Write a method <code>is_narcissistic(i)</code> which returns whether or not i is a Narcissistic Number.
"""


def is_narcissistic(i):
    length = len(str(i))
    return sum(el ** length for el in map(int, str(i))) == i
