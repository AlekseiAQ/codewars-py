"""Find Factors Down to Limit
https://www.codewars.com/kata/find-factors-down-to-limit

<s>My first Kata! Yay!</s> Most Probably gonna remove this later

In this Kata you have to find the factors of <code>integer</code> down to the <code>limit</code> including the limiting number. There will be no negative numbers.

If the <code>limit</code> is more than the <code>integer</code>, return an empty list

As a challenge, see if you can do it in one line
"""


def factors(integer, limit):
    return [x for x in range(limit, integer + 1) if integer % x == 0]
