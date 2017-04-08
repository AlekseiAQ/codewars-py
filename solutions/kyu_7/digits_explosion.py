"""Digits explosion
https://www.codewars.com/kata/digits-explosion

#Description:

Given a string made of digits `[0-9]` returns a string where each digit is repeated a number of times equals to its value. 

#Examples

```csharp
s = "312"
Digits.Explode(s) = "333122"

s = "102269"
Digits.Explode(s) = "12222666666999999999"
```
"""


def explode(s):
    return ''.join(ch * int(ch) for ch in s)
