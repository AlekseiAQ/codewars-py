"""Not all but sometimes all
https://www.codewars.com/kata/not-all-but-sometimes-all

Write
```javascript
function remove(str, what)
```
```csharp
public static string Remove(string str, Dictionary<char,int> what)
```
```python
remove(text, what)
```
```ruby
remove(text, what)
```
that takes in a string ```str```(```text``` in Python) and an object/hash/dict/Dictionary ```what``` and returns a string with the chars removed in ```what```.
For example:
```javascript
remove('this is a string',{'t':1, 'i':2}) === 'hs s a string'
// remove from 'this is a string' the first 1 't' and the first 2 i's.
remove('hello world',{'x':5, 'i':2}) === 'hello world'
// there are no x's or i's, so nothing gets removed
remove('apples and bananas',{'a':50, 'n':1}) === 'pples d bnns'
// we don't have 50 a's, so just remove it till we hit end of string.
```
```csharp
Kata.Remove("this is a string", new Dictionary<char,int> { {'t', 1 }, {'i', 2 }}); // --> "hs s a string"
// remove from 'this is a string' the first 1 't' and the first 2 i's.
Kata.Remove("hello world", new Dictionary<char,int> { { 'x',5 }, {'i',2 }}); // --> "hello world"
// there are no x's or i's, so nothing gets removed
Kata.Remove("apples and bananas", new Dictionary<char,int> { {'a', 50 }, {'n', 1 }}); // --> "pples d bnns"
// we don't have 50 a's, so just remove it till we hit end of string.
```
```python
remove('this is a string',{'t':1, 'i':2}) == 'hs s a string'
# remove from 'this is a string' the first 1 't' and the first 2 i's.
remove('hello world',{'x':5, 'i':2}) == 'hello world'
# there are no x's or i's, so nothing gets removed
remove('apples and bananas',{'a':50, 'n':1}) == 'pples d bnns'
# we don't have 50 a's, so just remove it till we hit end of string.
```
```ruby
remove('this is a string',{'t'=>1, 'i'=>2}) == 'hs s a string'
# remove from 'this is a string' the first 1 't' and the first 2 i's.
remove('hello world',{'x'=>5, 'i'=>2}) == 'hello world'
# there are no x's or i's, so nothing gets removed
remove('apples and bananas',{'a'=>50, 'n'=>1}) == 'pples d bnns'
# we don't have 50 a's, so just remove it till we hit end of string.
```
"""


def remove(text, what):
    for w in what:
        text = text.replace(w, '', what[w])
    return text
