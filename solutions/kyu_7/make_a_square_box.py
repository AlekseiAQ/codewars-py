"""Make a square box!
https://www.codewars.com/kata/make-a-square-box

<h1>Easy; Make a box</h1>
Given a number as a parameter, return an array containing strings which form a box.

Like this:

n = `5`
```
[
  '-----',
  '-   -',
  '-   -',
  '-   -',
  '-----'
]
```
n = `3`
```
[
  '---',
  '- -',
  '---'
]
```
"""


def box(n):
    return ['-'*n] + ['-' + ' '*(n-2)  + '-']*(n-2) + ['-'*n]
