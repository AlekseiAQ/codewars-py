"""Sum a list but ignore any duplicates
https://www.codewars.com/kata/sum-a-list-but-ignore-any-duplicates

Please write a function that sums a list, but ignores any duplicate items in the list.

For instance, for the list [3, 4, 3, 6] , the function should return 10.
"""


from collections import Counter


def sum_no_duplicates(nums):
    return sum(k for k, v in Counter(nums).items() if v == 1)
