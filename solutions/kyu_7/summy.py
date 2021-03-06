"""Summy
https://www.codewars.com/kata/summy

Write a function that takes a string which has integers inside it separated by spaces, and your task is to convert each integer in the string into an integer and return their sum.

### Example
```py
summy("1 2 3")  ==> 6
```

Good luck!
"""


def summy(string_of_ints):
    return sum(map(int, string_of_ints.split()))
