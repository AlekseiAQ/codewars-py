"""Alternate Square Sum
https://www.codewars.com/kata/alternate-square-sum

Write a method `alternate_sq_sum` (JS: `alternateSqSum` ) that takes an array of Integers as Input and finds the sum of squares of the elements at even positions (i.e 2nd 4th 6th etc etc elements) and the rest of the elements at odd Position (i.e 1st 3rd etc elements) without squaring them (the odd ones) thus completing whole array.

<h2 style="color:red">NOTE:<h2>
<p style="color:yellow">Elements at EVEN POSITION need to be squared, like element at index ( assuming starting index of an array in language to be 0 ) 1,3,5,7.. etc because 1st elements will be at 1st position (though it would have 0 as its index).</p>

<h2 style="color:lightGreen">For Example:</h2>

```ruby
alternate_sq_sum([11, 12, 13, 14, 15]) #should return 379
```
```javascript
alternateSqSum([11, 12, 13, 14, 15]) // should return 379
```
```python
alternate_sq_sum([11, 12, 13, 14, 15]) #should return 379
```
```haskell
alternateSqSum [11..15] `shouldBe` Just 379
alternateSqSum [] `shouldBe` Nothing
```
```java
alternateSqSum(new int[] {11, 12, 13, 14, 15}) // should return 379
```

<h2 style="color:cyan">Explanation:</h2>

elements at indices 0, 2, 4 are 11, 13, 15 and they are at odd positions as 11 is at position #1, 13 is at position #3 and 15 at #5.

elements at indices 1, 3 are 12 and 14 and they are at even position.
So we need to add 11, 13, 15 as they are and square of 12 and 14

--> 11 + 13 + 15 + 12^2 + 14^2<br>
  = 11 + 13 + 15 + 144 + 196<br>
  = 379

<p style="color:lightBlue">For empty arrays, result should be 0 (zero) (Except for Haskell)</p>
"""


def alternate_sq_sum(arr):
    return sum(el**2 if i % 2 else el for i, el in enumerate(arr))
