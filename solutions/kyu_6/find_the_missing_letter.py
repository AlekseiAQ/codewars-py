"""Find the missing letter
https://www.codewars.com/kata/find-the-missing-letter

#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.<br>
The array will always contain letters in only one case.

Example:
```
['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
```

(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!
"""


from string import ascii_letters


def find_missing_letter(chars):
    min_index = ascii_letters.index(min(chars))
    max_index = ascii_letters.index(max(chars))
    s = ascii_letters[min_index: max_index + 1]
    for elem in s:
        if elem not in chars:
            return elem
