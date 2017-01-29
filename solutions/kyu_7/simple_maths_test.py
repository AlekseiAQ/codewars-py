"""Simple Maths Test
https://www.codewars.com/kata/simple-maths-test

Create a function which checks a number for three different properties.

- is the number prime?
- is the number even?
- is the number a multiple of 10?

Each should return either true or false, which should be given as an array. Remark: The Haskell variant uses `data Property`.

### Examples
```javascript
numberProperty(7)  // ==> [true,  false, false] 
numberProperty(10) // ==> [false, true,  true] 
```
```ruby
number_property(7)  # ==> [true,  false, false] 
number_property(10) # ==> [false, true,  true] 
```
```python
number_property(7)  # ==> [true,  false, false] 
number_property(10) # ==> [false, true,  true] 
```
```haskell
numberProperty 7  `shouldBe` Property True  False False
numberProperty 10 `shouldBe` Property False True  True
```
The number will always be an integer, either positive or negative. Note that negative numbers cannot be primes, but they can be multiples of 10:

```javascript
numberProperty(-7)  // ==> [false, false, false] 
numberProperty(-10) // ==> [false, true,  true] 
```
```ruby
number_property(-7)  # ==> [false, false, false] 
number_property(-10) # ==> [false, true,  true] 
```
```python
number_property(-7)  # ==> [false, false, false] 
number_property(-10) # ==> [false, true,  true] 
```
```haskell
numberProperty (-7)  `shouldBe` Property False False False
numberProperty (-10) `shouldBe` Property False True  True
```

"""


import math


def is_prime(n):
    if n % 2 == 0 and n > 2 or n < 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def number_property(n):
    return [is_prime(n), n % 2 == 0, n % 10 == 0]
