"""Welcome to the City
https://www.codewars.com/kata/welcome-to-the-city

Create a method `say_hello` that takes as input a name, city, and state to welcome a person. Note that `name` will be an array consisting of one or more values that should be joined together with one space betweeen each, and the length of the `name` array in test cases will vary.

Example

```javascript
sayHello(['John', 'Smith'], 'Phoenix', 'Arizona')
```
```python
say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')
```
```ruby
say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')
```
```elixir
say_hello(["John", "Smith"], "Phoenix", "Arizona")
```

This example will return the string `Hello, John Smith! Welcome to Phoenix, Arizona!`
"""


def say_hello(name, city, state):
    return 'Hello, {}! Welcome to {}, {}!'.format(' '.join(name), city, state)
