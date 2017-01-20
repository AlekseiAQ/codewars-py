"""Sum Mixed Array
https://www.codewars.com/kata/sum-mixed-array

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.
"""


def sum_mix(arr):
    return sum(map(int, arr))
