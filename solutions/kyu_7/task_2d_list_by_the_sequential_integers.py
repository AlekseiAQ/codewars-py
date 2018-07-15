"""2D list by the sequential integers
https://www.codewars.com/kata/2d-list-by-the-sequential-integers

Make the 2D list by the sequential integers started by the ```head``` number.

See the example test cases for the expected output.

```
Note:

-10**20 < the head number <10**20
1 <=  the number of rows <= 1000
0 <=  the number of columms <= 1000
```
"""


def make_2d_list(head: int, row: int, col: int) -> list:
    return [[head + c + r * col for c in range(col)]
            for r in range(row)]
