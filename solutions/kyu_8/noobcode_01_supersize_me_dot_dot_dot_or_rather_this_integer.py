"""noobCode 01: SUPERSIZE ME.... or rather, this integer! 
https://www.codewars.com/kata/noobcode-01-supersize-me-dot-dot-dot-or-rather-this-integer

Write a function that rearranges an integer into its largest possible value. 

```javascript
superSize(123456) //654321
superSize(105) // 510
superSize(12) // 21
```
```python
super_size(123456) # 654321
super_size(105)    # 510
super_size(12)     # 21
```
```ruby
super_size(123456) # 654321
super_size(105)    # 510
super_size(12)     # 21
```

``` haskell
superSize 123456 `shouldBe` 654321
superSize    105 `shouldBe`    510
superSize     12 `shouldBe`     21
```
```coffeescript
superSize(123456) //654321
superSize(105) // 510
superSize(12) // 21
```

If the argument passed through is single digit or is already the maximum possible integer, your function should simply return it.




"""


def super_size(n):
    return int(''.join(sorted(str(n), reverse=True)))
