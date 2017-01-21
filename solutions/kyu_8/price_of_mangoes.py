"""Price of Mangoes
https://www.codewars.com/kata/price-of-mangoes

There's a 3 for 2 offer on mangoes. For a given price and quantity, calculate the total cost of the mangoes.
"""


def mango(quantity, price):
    return (quantity - quantity // 3) * price
