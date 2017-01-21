# pylint: disable=bare-except
"""Is it a number?
https://www.codewars.com/kata/is-it-a-number

Given a string s, write a method (function) that will return true if its a valid single integer or floating number or false if its not.

Valid examples, should return true:

```javascript
isDigit("3")
isDigit("  3  ")
isDigit("-3.23")
```

should return false:

```javascript
isDigit("3-4")
isDigit("  3   5")
isDigit("3 5")
isDigit("zero")
```
"""


def isDigit(string):
    try:
        float(string)
        return True
    except:
        return False
