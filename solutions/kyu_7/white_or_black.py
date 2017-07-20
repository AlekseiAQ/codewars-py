"""White or Black?
https://www.codewars.com/kata/white-or-black

In this kata you have a chess board 8x8. Create a function

```javascript
function mineColor(line, number)
```

```python
mine_color(line, number)
```

that calculate the color of the field and returns it(white / black)

Examples:
```javascript
mineColor(a, 8) ==> 'white'
mineColor(b, 1) ==> 'white'
mineColor(a, 1) ==> 'black'
```

```python
mine_color(a, 8) == 'white'
mine_color(b, 1) == 'white'
mine_color(a, 1) == 'black'
```

"""


def mine_color(line, number):
    return 'white' if (ord(line) + number) % 2 else 'black'
