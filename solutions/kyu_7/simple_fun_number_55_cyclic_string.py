"""Simple Fun #55: Cyclic String
https://www.codewars.com/kata/simple-fun-number-55-cyclic-string

# Task
 You're given a substring s of some cyclic string. What's the length of the smallest possible string that can be concatenated to itself many times to obtain this cyclic string?

# Example

 For` s = "cabca"`, the output should be `3`

 `"cabca"` is a substring of a cycle string "ab<b><font color='red'>cabca</font></b>bcabc..." that can be obtained by concatenating `"abc"` to itself. Thus, the answer is 3.

# Input/Output


 - `[input]` string `s`

  Constraints: `3 ≤ s.length ≤ 15.`


 - `[output]` an integer
"""


def cyclic_string(s: str) -> int:
    length_ = len(s)
    for i in range(1, length_+1):
        if s in s[:i] * length_:
            return i
