"""Perfect squares,  perfect fun
https://www.codewars.com/kata/perfect-squares-perfect-fun

Given an integer, if the length of it's digits is a perfect square, return a square block of sqroot(length) * sqroot(length). If not, simply return "Not a perfect square!".

Examples:

1212 returns:

>12<br>12

Note: 4 digits so 2 squared (2x2 perfect square). 2 digits on each line.

123123123 returns:
>123<br>123<br>123

Note: 9 digits so 3 squared (3x3 perfect square). 3 digits on each line.

"""

import math


def square_it(digits):
    digits_string = str(digits)
    square = math.sqrt(len(digits_string))
    if square == int(square):
        square = int(square)
        return "\n".join(
            digits_string[i * square : i * square + square]
            for i in range(int(square))
        )
    return "Not a perfect square!"
