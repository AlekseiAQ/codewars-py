"""Double Char
https://www.codewars.com/kata/double-char

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

```python
double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> "11223344!!__  "
```
```ruby
double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> "11223344!!__  "
```
```javascript
doubleChar("String") ==> "SSttrriinngg"

doubleChar("Hello World") ==> "HHeelllloo  WWoorrlldd"

doubleChar("1234!_ ") ==> "11223344!!__  "
```
```coffeescript
doubleChar "String" ==> "SSttrriinngg"

doubleChar "Hello World" ==> "HHeelllloo  WWoorrlldd"

doubleChar "1234!_ " ==> "11223344!!__  "
```
```haskell
doubleChar "String" ==> "SSttrriinngg"

doubleChar "Hello World" ==> "HHeelllloo  WWoorrlldd"

doubleChar "1234!_ " ==> "11223344!!__  "
```
```csharp
DoubleChar("String") == "SSttrriinngg"

DoubleChar("Hello World") == "HHeelllloo  WWoorrlldd"

DoubleChar("1234!_ ") == "11223344!!__  "
```
Good Luck!
"""


def double_char(s):
    return ''.join(c*2 for c in s)
