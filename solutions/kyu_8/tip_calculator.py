"""Tip Calculator
https://www.codewars.com/kata/tip-calculator

Write a function, `calculateTip(amount, rating)` which calculates how much you need to tip based on the total amount of the bill and the service. 

You need to consider the following ratings:

- Terrible: tip 0%
- Poor: tip 5%
- Good: tip 10%
- Great: tip 15%
- Excellent: tip 20%

The rating is case insensitive. If an unrecognised rating is input, then you need to return:

* `"Rating not recognised"` in Javascript, Python and Ruby...
* ...or `null` in Java

Because you're a nice person, you always round up the tip, regardless of the service.
"""


import math


def calculate_tip(amount, rating):
    TIPS = {
        "terrible":  0,
        "poor":  0.05,
        "good":  0.10,
        "great":  0.15,
        "excellent": 0.20,
    }
    rating = rating.lower()
    return math.ceil(amount * TIPS[rating]) if rating in TIPS else 'Rating not recognised'
