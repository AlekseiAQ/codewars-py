"""First-Class Function Factory
https://www.codewars.com/kata/first-class-function-factory

Write a function, `factory`, that takes a number as its parameter and returns another function.

The returned function should take an array of numbers as its parameter, and return an array of those numbers *multiplied by the number that was passed into the first function*.

In the example below, 5 is the number passed into the first function. So it returns a function that takes an array and multiplies all elements in it by five.

Translations and comments (and upvotes) welcome!

## Example
```javascript
var fives = factory(5);       // returns a function - fives
var myArray = [1, 2, 3];
fives(myArray);               //returns [5, 10, 15];
```
```python
fives = factory(5)          # returns a function - fives
my_array = [1, 2, 3]
fives(my_array)             # returns [5, 10, 15]
```
```coffeescript
fives = factory(5)          # returns a function - fives
myArray = [1, 2, 3]
fives(myArray)             # returns [5, 10, 15]
```
```haskell
let fives = factory 5      -- returns a function - fives
fives [1, 2, 3]            -- returns [5, 10, 15]
```
```csharp
Func<int[],int[]> fives = FunctionFactory.factory(5);    // returns a function - fives
int[] myArray = new int[]{1, 2, 3};
fives(myArray);                  //returns [5, 10, 15];
```
```clojure
(let [fives (factory 5)]      ; returns a function - fives
  (fives [1 2 3]))            ; returns [5 10 15]
```
"""


def factory(x):
    return lambda b: map(lambda a: a * x, b)
