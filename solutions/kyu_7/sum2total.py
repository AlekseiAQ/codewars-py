"""sum2total
https://www.codewars.com/kata/sum2total

Write a function that takes an array/list of numbers and returns a number such that

Explanation
total([1,2,3,4,5]) => 48
<pre>
1+2=3--\ 3+5 =>     8 \
2+3=5--/ \            ==  8+12=>20\
          ==>5+7=> 12 / \           20+28 => 48
3+4=7--\ /            == 12+16=>28/
4+5=9--/ 7+9 =>     16  /
</pre><br/>

if total([1,2,3]) => 8 then

<pre>
first+second => 3 \
                   then 3+5 => 8
second+third => 5 /
</pre><br/>

### Examples
```javascript
total([-1,-1,-1]) => -4
total([1,2,3,4])  => 20
```
```python
total([-1,-1,-1]) => -4
total([1,2,3,4])  => 20
```
```ruby
total([-1,-1,-1]) => -4
total([1,2,3,4])  => 20
```
```haskell
total [1..5]     `shouldBe` (48)
total [5,4..1]   `shouldBe` (48)
total [-1,-1,-1] `shouldBe` (-4)
total [1,2,3,4]  `shouldBe` (20)
```

**Note:** each array/list will have at least an element and all elements will be valid numbers.
"""


def total(arr):
    while len(arr) > 1:
        arr = [a + b for a, b in zip(arr, arr[1:])]
    return arr[0]
