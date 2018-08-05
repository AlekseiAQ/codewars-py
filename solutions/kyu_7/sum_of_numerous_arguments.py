"""Sum of numerous arguments
https://www.codewars.com/kata/sum-of-numerous-arguments

After calling the function `findSum()` with any number of non-negative integer arguments, it should return the sum of all those arguments.  If no arguments are given, the function should return 0, if negative arguments are given, it should return -1.

eg

```javascript
findSum(1,2,3,4); // returns 10
findSum(1,-2);    // returns -1
findSum();        // returns 0
```
```python
find_sum(1,2,3,4); # returns 10
find_sum(1,-2);    # returns -1
find_sum();        # returns 0
```
```ruby
find_sum(1,2,3,4); # returns 10
find_sum(1,-2);    # returns -1
find_sum();        # returns 0 0
```

**Hint:** research the arguments object on google or read Chapter 4 from Eloquent Javascript

"""


def find_sum(*args):
    return sum(args) if all(number >= 0 for number in args) else -1
