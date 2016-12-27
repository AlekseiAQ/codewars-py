"""Convert number to reversed array of digits
https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits

# Convert number to reversed array of digits

Given a random number:
<ul>
    <li><b>C#:</b> long;</li>
    <li><b>C++:</b> unsigned long;</li>
</ul>
You have to return the digits of this number within an array in reverse order.

## Example:

```
348597 => [7,9,5,8,4,3]
```
"""


def digitize(n):
    return list(map(int, str(n)[::-1]))
