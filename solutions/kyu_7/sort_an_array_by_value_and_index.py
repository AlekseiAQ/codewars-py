"""Sort an array by value and index
https://www.codewars.com/kata/sort-an-array-by-value-and-index

#Sort an array by value and index

Your task is to sort an array of integer numbers by the product of the value and the index of the positions.
<br><br>
For sorting the index starts at 1, NOT at 0!<br>
The sorting has to be ascending.<br>
The array will never be null and will always contain numbers.
<br><br>
Example:
```
Input: 23, 2, 3, 4, 5
Product of value and index:
23 => 23 * 1 = 23  -> Output-Pos 4
 2 =>  2 * 2 = 4   -> Output-Pos 1
 3 =>  3 * 3 = 9   -> Output-Pos 2
 4 =>  4 * 4 = 16  -> Output-Pos 3
 5 =>  5 * 5 = 25  -> Output-Pos 5

Output: 2, 3, 4, 23, 5
```
<br><br><br>
Have fun coding it and please don't forget to vote and rank this kata! :-) 

I have also created other katas. Take a look if you enjoyed this kata!
"""


def sort_by_value_and_index(arr):
    return [b for _, b in sorted(enumerate(arr, 1), key=lambda x: int.__mul__(*x))]
