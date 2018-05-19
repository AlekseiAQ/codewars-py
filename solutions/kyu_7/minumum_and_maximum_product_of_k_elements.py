"""Minumum and Maximum Product of k Elements
https://www.codewars.com/kata/minumum-and-maximum-product-of-k-elements

Given a list of numbers and a positive integer **k**, find the minimum and maximum possible product of **k** elements taken from the list.

If you cannot take enough elements from the list, return `None`/`nil`


## Examples

```python
numbers = [1, -2, -3, 4, 6, 7]

k = 1  ==>  -3, 7
k = 2  ==>  -21, 42    # -3*7, 6*7
k = 3  ==>  -126, 168  # -3*6*7, 4*6*7
k = 7  ==>  None       # there are only 6 elements in the list
```
```ruby
numbers = [1, -2, -3, 4, 6, 7]

k = 1  ==>  -3, 7
k = 2  ==>  -21, 42    # -3*7, 6*7
k = 3  ==>  -126, 168  # -3*6*7, 4*6*7
k = 7  ==>  nil        # there are only 6 elements in the list
```

Note: the test lists are sufficiently small (up to 20 elements) for a simple approach.

---

## My other katas

If you enjoyed this kata then please try [my other katas](https://www.codewars.com/collections/katas-created-by-anter69)! :-)

#### *Translations are welcome!*
"""


from functools import reduce
from itertools import combinations
from operator import mul

def find_min_max_product(arr, k):
    if k <= len(arr):
        products = [reduce(mul, nums) for nums in combinations(arr, k)]
        return min(products), max(products)
