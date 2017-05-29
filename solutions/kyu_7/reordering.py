"""ReOrdering
https://www.codewars.com/kata/reordering

There is a sentence which has a mistake in it's ordering.

The part with a capital letter should be the first word.

Please build a function for re-ordering

---
# Examples

```python
>>> re_ordering('ming Yao')
'Yao ming'

>>> re_ordering('Mano donowana')
'Mano donowana'

>>> re_ordering('wario LoBan hello')
'LoBan wario hello'

>>> re_ordering('bull color pig Patrick')
'Patrick bull color pig'
```

"""


def re_ordering(name):
    return ' '.join(sorted(name.split(), key=str.islower))
