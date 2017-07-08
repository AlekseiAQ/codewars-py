"""Sort the odd
https://www.codewars.com/kata/sort-the-odd

You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

*Example*
```javascript
sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
```
```haskell
sortArray [5, 3, 2, 8, 1, 4] == [1, 3, 2, 8, 5, 4]
```
"""


def sort_array(source_array):
    if not source_array:
        return []
    sorted_odd = (elem for elem in sorted(
        el for el in source_array if el % 2 == 1))

    return [elem if elem % 2 == 0 else next(sorted_odd)
            for elem in source_array]
