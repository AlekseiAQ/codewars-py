"""Centroid I
https://www.codewars.com/kata/centroid-i

Write a function `centroid(c)` to calculate the centroid of 3D coordinates. 

Return the results as a list of floats. Round the values to two decimal places.
"""


def centroid(c):
    return [round(sum(x) / len(c), 2) for x in zip(*c)]
