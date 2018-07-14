"""Insert Dashes 2
https://www.codewars.com/kata/insert-dashes-2

This is a follow up from my kata <a href="http://www.codewars.com/kata/insert-dashes/">Insert Dashes</a>. <br/>
Write a function ```insertDashII(num)``` that will insert dashes ('-') between each two odd numbers and asterisk ('\*') between each even numbers in ```num``` <br/>
For example: <br/>
```insertDashII(454793)``` --> 4547-9-3  <br/>
```insertDashII(1012356895)``` --> 10123-56*89-5 <br/>

Zero shouldn't be considered even or odd.


"""

import re


def insert_dash2(num: int) -> str:
    return re.sub(r'[13579](?=[13579])|[2468](?=[2468])',
                  lambda m: m.group(0) + ("-" if int(m.group(0)) & 1 else "*"),
                  str(num))
