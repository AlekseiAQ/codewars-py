"""Alien Accent
https://www.codewars.com/kata/alien-accent

<h3>The Story:</h3>
Aliens from Kepler 27b have immigrated to Earth! They have learned English and go to our stores, eat our food, dress like us, ride Ubers, use Google, etc. However, they speak English a little differently. Can you write a program that converts their Alien English to our English?

<h3>Task:</h3>

Write a function converting their speech to ours. They tend to speak the letter `a` like `o` and `o` like a `u`.
```python
>>> convert('hello')
'hellu'
>>> convert('codewars')
'cudewors'
```
```ruby
convert('hello') # => 'hellu'
convert('codewars') # =>'cudewors'
```
"""


def convert(st):
    return st.translate(str.maketrans('ao', 'ou'))
