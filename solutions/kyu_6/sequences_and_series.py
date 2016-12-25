"""Sequences and Series
https://www.codewars.com/kata/sequences-and-series

Have a look at the following numbers.

```
 n | score
---+-------
 1 |  50
 2 |  150
 3 |  300
 4 |  500
 5 |  750
```

Can you find a pattern in it? If so, then write a function `getScore(n)` which returns the score for any positive number `n`:

```javascript
getScore(1); // === 50
getScore(2); // === 150
getScore(3); // === 300
// ...
```
```haskell
getScore 1 `shouldBe` 50
getScore 2 `shouldBe` 150
getScore 3 `shouldBe` 300
getScore 4 `shouldBe` 500
getScore 5 `shouldBe` 750
```
```java
getScore(1); // == 50
getScore(2); // == 150
getScore(3); // == 300
// ...
```
```python
get_score(1) #=> == 50
get_score(2) #=> == 150
get_score(3) #=> == 300
# ...
```

```ruby
get_score 1 #=> == 50
get_score 2 #=> == 150
get_score 3 #=> == 300
# ...
```
```coffeescript
getScore 1 #=> is 50
getScore 2 #=> is 150
getScore 3 #=> is 300
# ...
```

"""


def get_score(n):
    return n * (n + 1) * 25
