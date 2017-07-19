"""Square and Cubic Factors
https://www.codewars.com/kata/square-and-cubic-factors

#### Task:

Your job here is to implement a function `factors`, which takes a number `n`, and outputs an array of arrays comprised of two
parts, `sq` and `cb`. The part `sq` will contain all the numbers that, when squared, yield a number which is a factor of `n`,
while the `cb` part will contain all the numbers that, when cubed, yield a number which is a factor of `n`.  Discard all `1`s
from both arrays.

Both `sq` and `cb` should be sorted in ascending order.

#### What it looks like:

```ruby
factors(Integer) #=> [
  sq (all the numbers that can be squared to give a factor of n) : Array,
  cb (all the numbers that can be cubed   to give a factor of n) : Array
]
```
```crystal
factors(Int32) #=> [
  sq (all the numbers that can be squared to give a factor of n) : Array(Int32),
  cb (all the numbers that can be cubed   to give a factor of n) : Array(Int32)
]
```
```python
factors(int) #=> [
  sq (all the numbers that can be squared to give a factor of n) : list,
  cb (all the numbers that can be cubed   to give a factor of n) : list
]
```
```javascript
factors(Number) #=> [
  sq (all the numbers that can be squared to give a factor of n) : Array,
  cb (all the numbers that can be cubed   to give a factor of n) : Array
]
```
```coffeescript
factors(Number) #=> [
  sq (all the numbers that can be squared to give a factor of n) : Array,
  cb (all the numbers that can be cubed   to give a factor of n) : Array
]
```

#### Some examples:

```ruby
factors(1) #=> [[], []]
  # ones are discarded from outputs

factors(4) #=> [[2], []]
  # 2 squared is 4;   4 is a factor of 4

factors(16) #=> [[2, 4], [2]]
  # 2 squared is  4;  4 is a factor of 16
  # 4 squared is 16; 16 is a factor of 16
  # 2 cubed is    8;  8 is a factor of 16

factors(81) #=> [[3, 9], [3]]
  # 3 squared is  9;  9 is a factor of 81
  # 9 squared is 81; 81 is a factor of 81
  # 3 cubed is   27; 27 is a factor of 81
```

Also check out my other creations � [Keep the Order](https://www.codewars.com/kata/keep-the-order), [Naming Files](https://www.codewars.com/kata/naming-files), [Elections: Weighted Average](https://www.codewars.com/kata/elections-weighted-average), [Identify Case](https://www.codewars.com/kata/identify-case), [Split Without Loss](https://www.codewars.com/kata/split-without-loss), [Adding Fractions](https://www.codewars.com/kata/adding-fractions),
[Random Integers](https://www.codewars.com/kata/random-integers), [Implement String#transpose](https://www.codewars.com/kata/implement-string-number-transpose), [Implement Array#transpose!](https://www.codewars.com/kata/implement-array-number-transpose), [Arrays and Procs #1](https://www.codewars.com/kata/arrays-and-procs-number-1), and [Arrays and Procs #2](https://www.codewars.com/kata/arrays-and-procs-number-2).

If you notice any issues or have any suggestions/comments whatsoever, please don't hesitate to mark an issue or just comment. Thanks!
"""


def factors(n):
    sq = [a for a in range(2, n+1) if not n % (a**2)]
    cb = [b for b in range(2, n+1) if not n % (b**3)]
    return [sq, cb]
