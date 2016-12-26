"""Reversed Words
https://www.codewars.com/kata/reversed-words

Complete the solution so that it reverses all of the words within the string passed in. 

Example:

```ruby
solution("The greatest victory is that which requires no battle") 
# should return "battle no requires which that is victory greatest The"
```
```coffeescript
reverseWords "The greatest victory is that which requires no battle"
# should return "battle no requires which that is victory greatest The"
```
```haskell
reverseWords "The greatest victory is that which requires no battle"
-- should return "battle no requires which that is victory greatest The"
```
```javascript
reverseWords("The greatest victory is that which requires no battle")
// should return "battle no requires which that is victory greatest The"
```
```python
reverseWords("The greatest victory is that which requires no battle")
// should return "battle no requires which that is victory greatest The"
```
```csharp
Kata.ReverseWords("The greatest victory is that which requires no battle");
// should return "battle no requires which that is victory greatest The"
```
"""


def reverse_words(string):
    return ' '.join(reversed(string.split(' ')))
