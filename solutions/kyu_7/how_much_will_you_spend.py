"""How much will you spend?
https://www.codewars.com/kata/how-much-will-you-spend

<h1>How much will you spend?</h1>

Given a dictionary of items and their costs and a array specifying the items bought, calculate the total cost of the items plus a given tax.

If item doesn't exist in the given cost values, the item is ignored.

Output should be rounded to two decimal places.

Python:
```python
costs = {'socks':5, 'shoes':60, 'sweater':30}
get_total(costs, ['socks', 'shoes'], 0.09)
#-> 5+60 = 65
#-> 65 + 0.09 of 65 = 70.85
#-> Output: 70.85
```
"""


def get_total(costs, items, tax):
    return round(sum(costs.get(item, 0) for item in items) * (1 + tax), 2)
