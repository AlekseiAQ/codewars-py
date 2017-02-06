"""Some Circles
https://www.codewars.com/kata/some-circles

Write a function that takes as its parameters *one or more numbers which are the diameters of circles.* 

The function should return the *total area of all the circles*, rounded to the nearest integer in a string that says "We have this much circle: xyz". 

You don't know how many circles you will be given, but you can assume it will be at least one.

So: 
```javascript
sumCircles(2) == "We have this much circle: 3"
sumCircles(2, 3, 4) == "We have this much circle: 23"
```
```python
sum_circles(2) == "We have this much circle: 3"
sum_circles(2, 3, 4) == "We have this much circle: 23"
```
```ruby
sum_circles(2) == "We have this much circle: 3"
sum_circles(2, 3, 4) == "We have this much circle: 23"
```

Translations and comments (and upvotes!) welcome!
"""


import math


def sum_circles(*args):
    return 'We have this much circle: {}'.format(
        int(round(sum([(math.pi * 0.25 * (x ** 2)) for x in args]), 0)))
