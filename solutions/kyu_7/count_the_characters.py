"""Count the Characters
https://www.codewars.com/kata/count-the-characters

The goal of this kata is to write a function that takes two inputs: a string and a character. The function will count the number of times that character appears in the string. The count is case insensitive.

For example: 

```javascript
countChar("fizzbuzz","z") => 4
countChar("Fancy fifth fly aloof","f") => 5
```
```ruby
count_char("fizzbuzz","z") => 4
count_char("Fancy fifth fly aloof","f") => 5
```
```python
count_char("fizzbuzz","z") => 4
count_char("Fancy fifth fly aloof","f") => 5
```
```php
count_char("fizzbuzz", "z"); // => 4
count_char("Fancy fifth fly aloof", "f"); // => 5
```

The character can be any alphanumeric character. 

Good luck.
"""


def count_char(s, ch):
    return s.lower().count(ch.lower())
