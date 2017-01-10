"""Name Shuffler
https://www.codewars.com/kata/name-shuffler

Write a function that returns a string in which firstname is swapped with last name.

```javascript
nameShuffler('john McClane'); => "McClane john"
```
```python
name_shuffler('john McClane'); => "McClane john"
```
```ruby
name_shuffler('john McClane'); => "McClane john"
```
```elixir
name_shuffler("john McClane"); => "McClane john"
```



"""


def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])
