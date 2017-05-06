"""Decreasing  Inputs
https://www.codewars.com/kata/decreasing-inputs

This kata is all about adding numbers.

You will create a functin named add. This function will return the sum of all the arguments. Sounds easy, doesn't it??

Well Here's the Twist. The inputs will gradually decrease with their index as parameter to the function.


```javascript
  add(3,4,6); 
  /*
  returns ( 3 / 1 ) + ( 4 / 2 ) + ( 6 / 3 ) = 7
  */
```
```ruby
  add(3,4,6) #returns (3/1)+(4/2)+(6/3)=7
```
```python
  add(3,4,6) #returns (3/1)+(4/2)+(6/3)=7
```

Remember the function will return 0 if no arguments is passed and the function must round the values if sum is a float.

Example
```javascript
  add(); //=> 0
  add(1,2,3); //=> 3
  add(1,4,-6,20); //=> 6
```
```ruby
  add() #=> 0
  add(1,2,3) #=> 3
  add(1,4,-6,20) #=> 6
```
```python
  add() #=> 0
  add(1,2,3) #=> 3
  add(1,4,-6,20) #=> 6
```

Check my another kata here!! http://www.codewars.com/kata/555b73a81a6285b6ce000047

"""


def add(*args):
    return int(round(sum(arg / i for i, arg in enumerate(args, 1))))
