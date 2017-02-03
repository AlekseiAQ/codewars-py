"""Char Code Calculation
https://www.codewars.com/kata/char-code-calculation

Given a string, first turn each letter into its ASCII char code.

example:<br><br>
`
'ABC' --> x=65, y=66, z=67 --> '656667'
`

Let's call this number 'total1'. 

Then replace any incidence of the number 7, with the number 1.<br><br>
`
'656667' ---> '656661'
`<br><br>
Lets call this number 'total2'.

Then return the difference between the sum of the digits in total1 and total2:

```
  (6 + 5 + 6 + 6 + 6 + 7)
- (6 + 5 + 6 + 6 + 6 + 1)
-------------------------
                       6
                       ```
"""


def calc(x):
    return ''.join(str(ord(ch)) for ch in x).count('7') * 6
