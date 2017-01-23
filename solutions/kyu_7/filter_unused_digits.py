"""Filter unused digits
https://www.codewars.com/kata/filter-unused-digits

Given few numbers, you need to print out the digits that are not being used.

Example:

```ruby
unused_digits(12, 34, 56, 78) # "09"
unused_digits(2015, 8, 26) # "3479"
```
```python
unused_digits(12, 34, 56, 78) # "09"
unused_digits(2015, 8, 26) # "3479"
```
```javascript
unusedDigits(12, 34, 56, 78) // "09"
unusedDigits(2015, 8, 26) // "3479"
```

Note:

- Result string should be sorted
- The test case won't pass Integer with leading zero
"""


def unused_digits(*args):
    return ''.join(n for n in '0123456789' if n not in str(args))
