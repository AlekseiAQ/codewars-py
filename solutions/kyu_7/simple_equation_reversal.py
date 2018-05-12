"""Simple equation reversal
https://www.codewars.com/kata/simple-equation-reversal

Given a mathematical equation that has `*,+,-,/`, reverse it as follows:

```Haskell
solve("100*b/y") = "y/b*100"
solve("a+b-c/d*30") = "30*d/c-b+a"
```

More examples in test cases.

Good luck!
"""

import re


def solve(eq):
    return ''.join(reversed(re.findall('[a-zA-Z]+|[0-9]+|\*|\+|\-|\/', eq)))
