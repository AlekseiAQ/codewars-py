"""Circle area inside square
https://www.codewars.com/kata/circle-area-inside-square

# Circle area inside square

Turn an area of a square in to an area of a circle that fits perfectly inside the square.

![Example](http://calculus.seas.upenn.edu/uploads/Main/InscribedCircle.png)

You get the blue+red area and need to calculate the red area.

Your function gets a number which represents the size of the square and should return the size of the circle. The tests are rounded by 8 decimals to make sure multiple types of solutions work.

```
squareAreaToCircle(16); //should return size of the circle
```

You don't have to worry about error handling or negative number input: `size >= 0`.

This kata might be simpler than you expect, but good luck!

"""


from math import pi


def square_area_to_circle(size):
    return size * pi / 4
