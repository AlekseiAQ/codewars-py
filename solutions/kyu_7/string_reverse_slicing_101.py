"""String reverse slicing 101
https://www.codewars.com/kata/string-reverse-slicing-101

You'll be given a string of characters as an input.

Create a function `reverse_slice`/`reverseSlice` that returns a _list_ of strings: 
(a) in the reverse order of the original string, and 
(b) with each successive string starting one character further in from the end of the original string.  

For example:
```
'123'  becomes  ['321','21','1']
```
and
```
'abcde'  becomes  ['edcba','dcba','cba', 'ba', 'a']
```

Assume the original string is at least 3 characters long.  _Try to do this using slices and avoid converting the string to a list._
"""


def reverse_slice(s):
    s = s[::-1]
    return [s[i:] for i in range(len(s))]
