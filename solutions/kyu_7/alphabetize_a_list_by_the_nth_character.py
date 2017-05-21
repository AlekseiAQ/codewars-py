"""Alphabetize a list by the nth character 
https://www.codewars.com/kata/alphabetize-a-list-by-the-nth-character

Write a function that accepts two parameters, i) a string (containing a list of words) and ii) an integer (n).  The function should alphabetize the list based on the nth letter of each word.

example:
```javascript 
function sortIt('bid, zag', 2) //=> 'zag, bid'
```
```ruby 
function sortIt('bid, zag', 2) //=> 'zag, bid'
```
```python 
function sortIt('bid, zag', 2) #=> 'zag, bid'
```
```haskell
sortIt ["bid", "zag"] 2 `shouldBe` ["zag", "bid"]
```

The length of all words provided in the list will be >= n.  The format will be "x, x, x". In Haskell you'll get a list of `String`s instead.




"""


def sort_it(list_, n):
    return ", ".join(sorted(list_.split(", "), key=lambda w: w[n-1]))
