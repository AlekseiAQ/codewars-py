"""Array.diff
https://www.codewars.com/kata/array-dot-diff

Your goal in this kata is to implement an difference function, which subtracts one list from another.

It should remove all values from list `a`, which are present in list `b`.

```javascript
difference([1,2],[1]) == [2]
```
```ruby
array_diff([1,2],[1]) == [2]
```
```python
array_diff([1,2],[1]) == [2]
```
```coffeescript
difference([1,2],[1]) == [2]
```
```haskell
difference [1,2] [1] == [2]
```

If a value is present in `b`, all of its occurrences must be removed from the other:

```javascript
difference([1,2,2,2,3],[2]) == [1,3]
```
```ruby
array_diff([1,2],[1]) == [2]
```
```python
array_diff([1,2,2,2,3],[2]) == [1,3]
```
```coffeescript
difference([1,2,2,2,3],[2]) == [1,3]
```
```haskell
difference [1,2,2,2,3] [2] == [1,3]
```

"""


def array_diff(a, b):
    return [el for el in a if el not in b]
