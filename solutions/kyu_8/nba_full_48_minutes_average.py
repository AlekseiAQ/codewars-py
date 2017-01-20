"""NBA full 48 minutes average
https://www.codewars.com/kata/nba-full-48-minutes-average

An NBA game runs 48 minutes (Four 12 minute quarters). Players do not typically play the full game, subbing in and out as necessary. Your job is to extrapolate a player's points per game if they played the full 48 minutes.

Write a function that takes two arguments, ppg (points per game) and mpg (minutes per game) and returns a straight extrapolation of ppg per
48 minutes rounded to the nearest tenth.

Examples:
```python
nba_extrap(12, 20) #=> 28.8
nba_extrap(10, 10) #=> 48 
nba_extrap(5, 17) #=> 14.1 
nba_extrap(0, 0) #=> 0
```

Notes:<br>
All inputs will be either be an integer or float.<br>
Follow your dreams!

"""


def nba_extrap(ppg, mpg):
    return round(48.0 / mpg * ppg, 1) if mpg > 0 else 0
