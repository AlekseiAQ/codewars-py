"""Geometry Basics: Triangle Perimeter  in 2D
https://www.codewars.com/kata/geometry-basics-triangle-perimeter-in-2d

This series of katas will introduce you to basics of doing geometry with computers.

`Point` objects have `x`, `y` attributes. `Triangle` objects have attributes `a`, `b`, `c` describing their corners, each of them is a `Point`.

Write a function calculating perimeter of a `Triangle` defined this way.

Tests round answers to 6 decimal places.

"""


from math import hypot
from itertools import combinations


def triangle_perimeter(t):
    return sum(hypot(p.x-q.x,p.y-q.y) for p,q in combinations((t.a,t.b,t.c),2))
