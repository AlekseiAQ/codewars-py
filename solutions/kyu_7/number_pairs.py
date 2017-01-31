"""Number Pairs
https://www.codewars.com/kata/number-pairs

In this Kata the aim is to compare each pair of integers from 2 arrays, and return a new array of large numbers.

Note: Both arrays have the same dimensions.

Example:
```csharp
arr1 = new int[] { 13, 64, 15, 17, 88 };
arr2 = new int[] { 23, 14, 53, 17, 80 };

Kata.getLargerNumbers(arr1, arr2); // Returns {23, 64, 53, 17, 88}
```
```python
arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
get_larger_numbers(arr1, arr2) == [23, 64, 53, 17, 88]
```
```ruby
arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
get_larger_numbers(arr1, arr2) == [23, 64, 53, 17, 88]
```
```javascript
let arr1 = [13, 64, 15, 17, 88];
let arr2 = [23, 14, 53, 17, 80];
getLargerNumbers(arr1, arr2); // Returns [23, 64, 53, 17, 88]
```
```coffeescript
arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
getLargerNumbers(arr1, arr2) # Returns [23, 64, 53, 17, 88]
```
```haskell
arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
getLargerNumbers arr1 arr2 == [23, 64, 53, 17, 88]
```
```clojure
(= arr1 [13, 64, 15, 17, 88])
(= arr2 [23, 14, 53, 17, 80])
(= (getLargerNumbers arr1 arr2) [23 64 53 17 88])
```
"""


def get_larger_numbers(a, b):
    return list(map(max, zip(a, b)))
