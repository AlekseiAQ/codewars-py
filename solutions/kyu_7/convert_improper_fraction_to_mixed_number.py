"""Convert Improper Fraction to Mixed Number
https://www.codewars.com/kata/convert-improper-fraction-to-mixed-number

# Convert Improper Fraction to Mixed Number

You will need to convert an [improper fraction](https://www.mathplacementreview.com/arithmetic/fractions.php#improper-fractions) to a [mixed number](https://www.mathplacementreview.com/arithmetic/fractions.php#mixed-number). For example:

```javascript
getMixedNum('18/11'); // Should return '1 7/11'
getMixedNum('13/5'); // Should return '2 3/5'
getMixedNum('75/10'); // Should return '7 5/10'
```

```python
get_mixed_num('18/11') # Should return '1 7/11'
get_mixed_num('13/5') # Should return '2 3/5'
get_mixed_num('75/10') # Should return '7 5/10'
```

NOTE: All fractions will be greater than 0.
"""


def get_mixed_num(fraction):
    a, b = map(int, fraction.split('/'))
    return '{} {}/{}'.format(a // b, a % b, b)
