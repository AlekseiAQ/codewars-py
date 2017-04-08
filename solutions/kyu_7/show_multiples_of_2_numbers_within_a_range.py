"""Show multiples of 2 numbers within a range
https://www.codewars.com/kata/show-multiples-of-2-numbers-within-a-range

Print all numbers up to `3rd` parameter which are multiple of both `1st` and `2nd` parameter.

Python, Javascript, Java versions: return results in a list/array

NOTICE:

1. Do NOT worry about checking zeros or negative values.
2. To find out if `3rd` parameter (the upper limit) is inclusive or not, check the tests, it differs in each translation
"""


def multiples(s1, s2, s3):
    return [a for a in range(1, s3) if not(a % s1 or a % s2)]
