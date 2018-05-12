"""Counting Array Elements
https://www.codewars.com/kata/counting-array-elements

Write a function that takes an array and counts the number of each unique element present.

```ruby
count(['james', 'james', 'john'])
#=> { 'james' => 2, 'john' => 1}
```

```javascript
count(['james', 'james', 'john'])
#=> { 'james': 2, 'john': 1}
```

```csharp
Kata.Count(new List<string> {"James", "James", "John"}) =>
  new Dictionary<string, int> {{"James", 2}, {"John", 1}};
```
"""


from collections import Counter


def count(array):
    return dict(Counter(array))
