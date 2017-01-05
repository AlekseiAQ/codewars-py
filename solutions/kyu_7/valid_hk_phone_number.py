"""Valid HK Phone Number
https://www.codewars.com/kata/valid-hk-phone-number

# Valid HK Phone Number

## Overview

In Hong Kong, a valid phone number has the format ```xxxx xxxx``` where ```x``` is a decimal digit (0-9).  For example:

```js
"1234 5678" // is valid
"2359 1478" // is valid
"85748475" // invalid, as there are no spaces separating the first 4 and last 4 digits
"3857  4756" // invalid; there should be exactly 1 whitespace separating the first 4 and last 4 digits respectively
"sklfjsdklfjsf" // clearly invalid
"     1234 5678   " // is NOT a valid phone number but CONTAINS a valid phone number
"skldfjs287389274329dklfj84239029043820942904823480924293042904820482409209438dslfdjs9345 8234sdklfjsdkfjskl28394723987jsfss2343242kldjf23423423SDLKFJSLKsdklf" // also contains a valid HK phone number (9345 8234)
```

## Task

Define two functions, ```isValidHKPhoneNumber``` and ```hasValidHKPhoneNumber```, that ```return```s whether a given string is a valid HK phone number and contains a valid HK phone number respectively (i.e. ```true/false``` values).

If in doubt please refer to the example tests.
"""


import re

def is_valid_HK_phone_number(number):
    return bool(re.match(r'^\d{4} \d{4}$', number))

def has_valid_HK_phone_number(number):
    return bool(re.search(r'\d{4} \d{4}', number))
