"""Tail Swap
https://www.codewars.com/kata/tail-swap

You'll be given a list of two strings, and each will contain exactly one colon in the middle (but not at beginning or end). The length of the strings, before and after the colon, are random.

Your job is to return a list of two strings (in the same order as the original list), but with the characters after each colon swapped.<br>
Python
```python
tail_swap(['abc:123', 'cde:456']) == ['abc:456', 'cde:123']
tail_swap(['a:12345', '777:xyz']) == ['a:xyz', '777:12345']
```
Javascript
```javascript
tailSwap(['abc:123', 'cde:456']) == ['abc:456', 'cde:123']
tailSwap(['a:12345', '777:xyz']) == ['a:xyz', '777:12345']
```


"""


def tail_swap(strings):
    s1, s2 = strings
    s1 = s1.split(':')
    s2 = s2.split(':')
    return [s1[0] + ':' + s2[1], s2[0] + ':' + s1[1]]
