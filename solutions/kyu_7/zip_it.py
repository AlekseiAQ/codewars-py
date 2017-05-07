"""Zip it!
https://www.codewars.com/kata/zip-it

Write
```javascript
Array.prototype.zip = function (arr, fn) {}
```
```ruby
Array#zip
```
```python
lstzip
```
that merges the corresponding elements of two sequences using a specified selector function ```fn``` (a `block` in Ruby)

For example:
```javascript
var a = [1, 2, 3, 4, 5];
var b = ['a','b'];
a.zip(b, (a, b) => a + b) === ['1a', '2b']

var a = [1, 2, 3, 4, 5];
var b = ['a','b','c','d','e'];
a.zip(b, (a, b) => a + b.charCodeAt(0)) === [98, 100, 102, 104, 106]
```
```csharp
var a = new object[] { 1, 2, 3, 4, 5 };
var b = new object[] { 'a','b' };
a.ZipIt(b, (c, d) => c + "" + d); --> new object[] { '1a', '2b' }

var a = new object[] { 1, 2, 3, 4, 5 };
var b = new object[] {'a','b','c','d','e'};
a.ZipIt(b, (c, d) => (int)c + (int)(char)d)); --> new object[] { 98, 100, 102, 104, 106 }
```
```ruby
a = [1, 2, 3, 4, 5]
b = ['a', 'b']
a.zip(b){|x, y| x.to_s + y} => ['1a', '2b']

a = [1, 2, 3, 4, 5]
b = ['a','b','c','d','e']
a.zip(b){|x, y| x + y.ord} => [98, 100, 102, 104, 106]
```
```python
a = [1, 2, 3, 4, 5]
b = ['a', 'b']
lstzip(a,b, lambda a,b: str(a)+str(b))

a = [1, 2, 3, 4, 5]
b = ['a','b','c','d','e']
lstzip(a,b, lambda a, b: a * ord(b[0]))
```
if arrays have different lengths, go up to the minimum length and then stop.

"""


def lstzip(a, b, fn):
    return [fn(x, y) for x, y in zip(a, b)]
