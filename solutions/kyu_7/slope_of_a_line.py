"""Slope of a Line
https://www.codewars.com/kata/slope-of-a-line

Your challenge is to write a function named 
```
getSlope(p1, p2)
```
that calculates the slope of the line through two points. Each point that the function takes in is an array 2 elements long. The first number is the x coordinate and the second number is the y coordinate.
If the line through the two points is vertical, the function should return 

```javascript
null
```

```python
None
```

If the same point is given twice, the function should return


```javascript
null
```

```python
None
```

"""


def getSlope(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    try:
        return (y1 - y2) / (x1 - x2)
    except ZeroDivisionError:
        pass
