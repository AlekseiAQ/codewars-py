"""Ultimate Array Reverser
https://www.codewars.com/kata/ultimate-array-reverser

## Task
Given an array of strings, reverse them and their order in such way that their length stays the same as the length of the original inputs.

### Example:

```
Input:  {"I", "like", "big", "butts", "and", "I", "cannot", "lie!"}
Output: {"!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"}
```

Good luck!
"""


def reverse(a):
    list_ = reversed("".join(a))
    return ["".join(next(list_) for _ in word) for word in a]
