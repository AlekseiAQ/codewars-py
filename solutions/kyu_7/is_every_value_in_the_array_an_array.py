"""Is every value in the array an array?
https://www.codewars.com/kata/is-every-value-in-the-array-an-array

Is every value in the array an array?

This should only test the second array dimension of the array. The values of the nested arrays don't have to be arrays. 

Examples:

```javascript
[[1],[2]] => true
['1','2'] => false
[{1:1},{2:2}] => false
```
```python
[[1],[2]] => true
['1','2'] => false
[{1:1},{2:2}] => false
```
```ruby
[[1],[2]] => true
['1','2'] => false
[{1:1},{2:2}] => false
```
```c
[[1],[2]] => true
['1','2'] => false
[{1:1},{2:2}] => false
```
```php
[[1], [2]] => true
["1", "2"] => false
[
  new class {
    public $one = 1;
  },
  new class {
    public $two = 2;
  }
] => false
```
"""


def arr_check(arr):
    return all(isinstance(el, list) for el in arr)
