# pylint: disable=unidiomatic-typecheck
"""Power of 4
https://www.codewars.com/kata/power-of-4

Write a method that returns true if a given parameter is a power of 4, and false if it's not. If parameter is not an Integer (eg String, Array) method should return false as well.
(In C# Integer means all integer Types like Int16,Int32,.....)

### Examples

```ruby
power_of_4(1024) => true
power_of_4(55)   => false
power_of_4("Four") => false
```

```haskell
isPowerOf4 1024 `shouldBe` True
isPowerOf4  102 `shouldBe` False
isPowerOf4   64 `shouldBe` True
```

```python
isPowerOf4 1024 #should return True
isPowerOf4  102 #should return False
isPowerOf4   64 #should return True
```

```javascript
powerOf4(1024) // returns true
powerOf4(44) // returns false
powerOf4("not a positive integer") // returns false
```

```clojure
(isPowerOf4? 3) ; returns false
(isPowerOf4? 4) ; returns true
```

```csharp
Power.PowerOf4(1024); // returns true
Power.PowerOf4(44); // returns false
Power.PowerOf4("not a positive integer"); // returns false
```

"""


from math import log


def powerof4(n):
    return n == 4**round(log(n, 4)) if (type(n) == int and n > 0) else False
