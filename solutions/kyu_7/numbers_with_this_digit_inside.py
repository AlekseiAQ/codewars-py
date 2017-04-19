"""Numbers with this digit inside
https://www.codewars.com/kata/numbers-with-this-digit-inside

You have to search all numbers from inclusive 1 to inclusive a given number x, that have the given digit d in it.<br>
The value of d will always be 0 - 9.<br>
The value of x will always be greater than 0.

You have to return as an array<br>
# the count of these numbers,<br>
# their sum <br>
# and their product.<br>
<br>
For example:<br>
```
x = 11
d = 1
->
Numbers: 1, 10, 11
Return: [3, 22, 110]
```
<br>
If there are no numbers, which include the digit, return [0,0,0]. 
<br>
<br>
Have fun coding it and please don't forget to vote and rank this kata! :-) <br>
<br>
I have created other katas. Have a look if you like coding and challenges.<br>

"""


from functools import reduce
from operator import mul


def numbers_with_digit_inside(x, d):
    num_str = str(d)
    nums = [el for el in range(1, x + 1) if num_str in str(el)]
    return [len(nums), sum(nums), reduce(mul, nums) if nums else 0]
