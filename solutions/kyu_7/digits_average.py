"""Digits Average
https://www.codewars.com/kata/digits-average

Given an integer, take the (mean) average of each pair of consecutive digits. Repeat this process until you have a single integer, then return that integer. e.g.

```
digitsAverage(246)
average of 2 and 4 is 3, average of 4 and 6 is 5
so after first iteration 246 => 35
average of 3 and 5 is 4
so digitsAverage(246) returns 4
```

If the average of two digits is not an integer, round the result **up**. e.g.

```
digitsAverage(89)
average of 8 and 9 is 8.5 ==> return 9
```

p.s. for a bigger challenge, check out the [one line version](https://www.codewars.com/kata/one-line-task-digits-average) of this kata by myjinxin2015!
"""


from math import ceil


def digits_average(input):
    def return_average(a, b):
        return str(ceil((int(a) + int(b)) / 2))

    string_ = str(input)

    while len(string_) > 1:
        string_ = ''.join(
            return_average(a, b) for a, b in zip(string_, string_[1:]))

    return int(string_)
