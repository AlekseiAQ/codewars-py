# pylint: disable=abstract-method
"""Ordered Count of Characters
https://www.codewars.com/kata/ordered-count-of-characters

Count the number of occurencences of each character and return it as a list of tuples in order of appearance.

Example:
```python
ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
```
"""


from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    pass


def ordered_count(seq):
    return list(OrderedCounter(seq).items())
