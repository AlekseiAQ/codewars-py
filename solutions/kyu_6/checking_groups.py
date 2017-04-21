"""Checking Groups
https://www.codewars.com/kata/checking-groups

In English and programming, groups can be made using symbols such as "()" and "{}" that change meaning. However, these groups must be closed in the correct order to maintain correct syntax.

Your job in this kata will be to make a program that checks a string for correct grouping. For instance, the following groups are done correctly:

```
({})
[[]()]
[{()}]
```
The next are done incorrectly
```
{(})
([]
[])
```

A correct string cannot close groups in the wrong order, open a group but fail to close it, or close a group before it is opened.

Your function will take an input string that may contain any of the symbols "()" "{}" or "[]" to create groups.

It should return True if the string is empty or otherwise grouped correctly, or False if it is grouped incorrectly.
"""


def group_check(s):
    if s == "":
        return True
    if len(s) % 2 != 0:
        return False
    for i in range(len(s) - 1):
        if s[i] + s[i + 1] in ["[]", "()", "{}"]:
            return group_check(s[:i] + s[i + 2:])
    return False
