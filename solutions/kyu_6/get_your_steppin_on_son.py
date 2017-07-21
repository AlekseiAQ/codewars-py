"""Get your steppin' on son
https://www.codewars.com/kata/get-your-steppin-on-son

Write
```javascript
function wordStep(str)
```
that takes in a string and creates a step with that word. <br/>

E.g<br/>

```javascript
wordStep('SNAKES SHOE EFFORT TRUMP POTATO') ===

[['S','N','A','K','E','S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ','O',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ','E','F','F','O','R','T',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','R',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','U',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' '],
 [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','P','O','T','A','T','O']]

```
Every word will end with the character that the next word will start with. You will start top left of the array and end bottom right. All cells that are not occupied by a letter needs to be a space ```' '```
"""


def word_step(s):
    i, j = 0, 0
    flag = True
    matrix = {}
    index = 1
    matrix[(i, j)] = s[0]
    while index < len(s):
        if s[index] == " ":
            flag = not flag
            index += 2
            continue
        if flag:
            j += 1
        else:
            i += 1
        matrix[(i, j)] = s[index]
        index += 1

    result = []
    for ii in range(i+1):
        row = []
        for jj in range(j+1):
            row.append(matrix.get((ii, jj), " "))
        result.append(row)
    return result
