"""Check for prime numbers
https://www.codewars.com/kata/check-for-prime-numbers

In this kata you will create a function to check a non-negative input to see if it is a prime number.

The function will take in a number and will return True if it is a prime number and False if it is not.

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.


### Examples
```coffeescript
isPrime(0) is false
isPrime(1) is false
isPrime(2) is true
isPrime(11) is true
isPrime(12) is false
```
"""


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, n))
