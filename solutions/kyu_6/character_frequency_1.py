"""Character frequency
https://www.codewars.com/kata/character-frequency-1

Write a function that takes a piece of text in the form of a string and returns the letter frequency count for the text. This count excludes numbers, spaces and all punctuation marks. Upper and lower case versions of a character are equivalent and the result should all be in lowercase.

The function should return a list of tuples (in Python) or arrays (in other languages) sorted by the most frequent letters first. 
Letters with the same frequency are ordered alphabetically.
For example:

```python
  letter_frequency('aaAabb dddDD hhcc')
```  
```javascript
  letterFrequency('aaAabb dddDD hhcc')
```
```ruby
  letter_frequency('aaAabb dddDD hhcc')
```

will return

```python
  [('d',5), ('a',4), ('b',2), ('c',2), ('h',2)]
```  
```javascript
  [['d',5], ['a',4], ['b',2], ['c',2], ['h',2]]
```
```ruby
  [['d',5], ['a',4], ['b',2], ['c',2], ['h',2]]
```

Letter frequency analysis is often used to analyse simple substitution cipher texts like those created by the Caesar cipher.

"""


def letter_frequency(text):
    return sorted([(ch, text.lower().count(ch)) for ch in set(text.lower()) if ch.isalpha()], key=lambda t: (-t[1], t[0]))
