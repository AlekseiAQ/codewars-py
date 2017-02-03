"""How many are smaller than me?
https://www.codewars.com/kata/how-many-are-smaller-than-me

Write
```javascript
function smaller(arr)
```
```python
smaller(arr)
```
```ruby
smaller(arr)
```
```coffeescript
smaller(arr)
```
that given an array ```arr```, you have to return the amount of numbers that are smaller than ```arr[i]``` to the right.

For example:
```javascript
smaller([5, 4, 3, 2, 1]) === [4, 3, 2, 1, 0]
smaller([1, 2, 0]) === [1, 1, 0]
```
```python
smaller([5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]
smaller([1, 2, 0]) == [1, 1, 0]
```
```ruby
smaller([5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]
smaller([1, 2, 0]) == [1, 1, 0]
```
```coffeescript
smaller([5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]
smaller([1, 2, 0]) == [1, 1, 0]
```
``` haskell
smaller [5,4,3,2,1]  `shouldBe` [4,3,2,1,0]
smaller [1,2,3]      `shouldBe` [0,0,0]
smaller [1, 2, 0]    `shouldBe` [1, 1, 0]
```
If you've completed this one and you feel like testing your performance tuning of this same kata, head over to the much tougher version <a href = 'http://www.codewars.com/kata/56a1c63f3bc6827e13000006'>How many are smaller than me II?</a>

"""


def smaller(arr):
    return [sum(next_el < el for next_el in arr[i + 1:]) for i, el in enumerate(arr)]
