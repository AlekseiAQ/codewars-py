"""Double Trouble
https://www.codewars.com/kata/double-trouble

Given an array of integers (x), and a target (t), you must find out if any two consecutive numbers in the array sum to t. If so, remove the second number.

Example:

x = [1, 2, 3, 4, 5]<br>
t = 3 <br>

1+2 = t, so remove 2. No other pairs = t, so rest of array remains:

[1, 3, 4, 5]

Work through the array from left to right.

Return the resulting array.
"""


def trouble(arr, t):
    for i in range(len(arr) - 1):
        if arr[i] + arr[i+1] == t:
            return trouble(arr[:i+1] + arr[i+2:], t)
    return arr
