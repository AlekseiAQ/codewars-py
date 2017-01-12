"""Calculate average 
https://www.codewars.com/kata/calculate-average

Write function avg which calaculates average of numbers in given list.
"""


def find_average(array):
    return sum(array)/len(array) if array else 0
