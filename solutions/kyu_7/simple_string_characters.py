"""Simple string characters
https://www.codewars.com/kata/simple-string-characters

In this Kata, you will be given a string and your task will be to return a list
of ints detailing the count of uppercase letters, lowercase, numbers and special
characters, as follows.

```Haskell
solve("*'&ABCDabcde12345") = [4,5,5,3].
--the order is: uppercase letters, lowercase, numbers and special characters.
```

More examples in the test cases.

Good luck!
"""


def solve(s: str) -> list:
    upper_counter, lower_counter, number_counter, special_character_counter =\
        0, 0, 0, 0
    for char in s:
        if char.isupper():
            upper_counter += 1
        elif char.islower():
            lower_counter += 1
        elif char.isdigit():
            number_counter += 1
        else:
            special_character_counter += 1
    return [upper_counter,
            lower_counter,
            number_counter,
            special_character_counter]
