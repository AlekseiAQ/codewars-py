"""Multiply the number
https://www.codewars.com/kata/multiply-the-number

Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:
```javascript
multiply(3)==15
multiply(10)==250
multiply(200)==25000
multiply(0)==0
multiply(-3)==-15
```
```python
multiply(3)==15
multiply(10)==250
multiply(200)==25000
multiply(0)==0
multiply(-3)==-15
```
```ruby
multiply(3)==15
multiply(10)==250
multiply(200)==25000
multiply(0)==0
multiply(-3)==-15
```
```haskell
multiply   3  `shouldBe`    15
multiply  10  `shouldBe`   250
multiply 200  `shouldBe` 25000
multiply   0  `shouldBe`     0
multiply (-3) `shouldBe`  (-15)
```
"""


def multiply(n):
    return n * 5 ** len(str(abs(n)))
