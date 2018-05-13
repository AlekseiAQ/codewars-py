"""Cat and Mouse - 2D Version
https://www.codewars.com/kata/cat-and-mouse-2d-version

You will be given a string (`map`) featuring a cat `"C"` and a mouse `"m"`. The rest of the string will be made up of dots (`"."`) The cat can move the given number of `moves` up, down, left or right, but **not diagonally**.

You need to find out if the cat can catch the mouse from it's current position and return `"Caught!"` or `"Escaped!"` respectively.

Finally, if one of two animals are not present, return `"boring without two animals"`.


## Examples

```
moves = 5

map =
..C......
.........
....m....

returns "Caught!" because the cat can catch the mouse in 4 moves
```
```
moves = 5

map =
.C.......
.........
......m..

returns "Escaped!" because the cat cannot catch the mouse in  5 moves
```

"""


def cat_mouse(map_, moves):
    cat, mouse = [], []
    for i, x in enumerate(map_.splitlines()):
        for j, y in enumerate(x):
            if y == "C":
                cat = [i, j]
            if y == "m":
                mouse = [i, j]
    if not cat or not mouse: return "boring without two animals"
    return "Caught!" if \
        abs(mouse[0] - cat[0]) + abs(cat[1] - mouse[1]) <= moves else \
        "Escaped!"
