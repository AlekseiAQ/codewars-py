"""Find missing numbers
https://www.codewars.com/kata/find-missing-numbers

You will get an array of numbers. 

Every preceding number is smaller than the one following it.

Some numbers will be missing, for instance:
```
[-3,-2,1,5] //missing numbers are: -1,0,2,3,4
```
Your task is to return an array of those missing numbers:
```
[-1,0,2,3,4]
```

"""


def find_missing_numbers(arr):
    return sorted(set(range(min(arr), max(arr) + 1)).difference(arr)) if arr else []
