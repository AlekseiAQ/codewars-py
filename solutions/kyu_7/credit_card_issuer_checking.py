"""Credit card issuer checking
https://www.codewars.com/kata/credit-card-issuer-checking

Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.

```
+============+=============+===============+
| Card Type  | Begins With | Number Length |
+============+=============+===============+
| AMEX       | 34 or 37    | 15            |
+------------+-------------+---------------+
| Discover   | 6011        | 16            |
+------------+-------------+---------------+
| Mastercard | 51-55       | 16            |
+------------+-------------+---------------+
| VISA       | 4           | 13 or 16      |
+------------+-------------+---------------+
```

Write a function (`getIssuer(number)` (`get_issuer(number)` for Python)) that will use the above known values to determine the card issuer given a card number. If the number cannot be matched then the function should return the string `Unknown`.

Some sample numbers and their issuer:

```
getIssuer(4111111111111111) == "VISA"
getIssuer(4111111111111) == "VISA"
getIssuer(4012888888881881) == "VISA"
getIssuer(378282246310005) == "AMEX"
getIssuer(6011111111111117) == "Discover"
getIssuer(5105105105105100) == "Mastercard"
getIssuer(5105105105105106) == "Mastercard"
getIssuer(9111111111111111) == "Unknown"
```

**Note:** ranges stated in this kata are inclusive.
"""


def get_issuer(number):
    num_str = str(number)
    if len(num_str) == 15 and num_str.startswith(('34', '37')):
        return 'AMEX'
    elif (len(num_str) == 13 or len(num_str) == 16) and num_str.startswith('4'):
        return 'VISA'
    elif len(num_str) == 16 and num_str.startswith('6011'):
        return 'Discover'
    elif len(num_str) == 16 and num_str.startswith(('51', '52', '53', '54', '55')):
        return 'Mastercard'
    return 'Unknown'
