"""Frequency sequence
https://www.codewars.com/kata/frequency-sequence

Return an output string that translates an input string `s`/`$s` by replacing each character in `s`/`$s` with a number representing the number of times that character occurs in `s`/`$s` and separating each number with the character(s) `sep`/`$sep`.

```javascript
freqSeq('hello world', '-'); // => '1-1-3-3-2-1-1-2-1-3-1'
freqSeq('19999999',    ':'); // => '1:7:7:7:7:7:7:7'
freqSeq('^^^**$',      'x'); // => '3x3x3x2x2x1'
```
```php
freq_seq("hello world", "-"); // => "1-1-3-3-2-1-1-2-1-3-1"
freq_seq("19999999", ":"); // => "1:7:7:7:7:7:7:7"
freq_seq("^^^**$", "x"); // => "3x3x3x2x2x1"
```
"""


def freq_seq(s, sep):
    return sep.join(str(s.count(el)) for el in s)
