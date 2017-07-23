"""Character Concatenation
https://www.codewars.com/kata/character-concatenation

Given a string, you progressively need to concatenate the first letter from the left and the first letter to the right and "1", then the second letter from the left and the second letter to the right and "2", and so on.

If the string's length is odd drop the central element.

For example:
```python
char_concat("abcdef")    == 'af1be2cd3'
char_concat("abc!def")   == 'af1be2cd3' # same result
```
```javascript
charConcat("abcdef")    == 'af1be2cd3'
charConcat("abc!def")   == 'af1be2cd3' // same result
```
```ruby
char_concat("abcdef")    == 'af1be2cd3'
char_concat("abc!def")   == 'af1be2cd3' # same result
```

"""


def char_concat(word):
    return ''.join(word[i] + word[-i-1] + str(i+1)
                   for i in range(len(word)//2))
