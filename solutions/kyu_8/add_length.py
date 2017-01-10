"""Add Length
https://www.codewars.com/kata/add-length

What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

```javascript
addLength('apple ban') => ["apple 5", "ban 3"]
addLength('you will win') => ["you 3", "will 4", "win 3"]
```
```python
add_length('apple ban') => ["apple 5", "ban 3"]
add_length('you will win') => ["you 3", "will 4", "win 3"]
```
```ruby
add_length('apple ban') => ["apple 5", "ban 3"]
add_length('you will win') => ["you 3", "will 4", "win 3"]
```
```coffeescript
addLength 'apple ban' => ["apple 5", "ban 3"]
addLength 'you will win' => ["you 3", "will 4", "win 3"]
```
```elixir
add_length("apple ban") => ["apple 5", "ban 3"]
add_length("you will win") => ["you 3", "will 4", "win 3"]
```
Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

**Note:** String will have at least one element; words will always be separated by a space. 

"""


def add_length(str_):
    return ["{} {}".format(word, len(word)) for word in str_.split(' ')]
