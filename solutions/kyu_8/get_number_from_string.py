"""Get number from string
https://www.codewars.com/kata/get-number-from-string

Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56

Function:
####javascript
```
getNumberFromString(s)
```
####ruby
```
get_number_from_string(s)
```

####CSharp

```csharp
GetNumberFromString(string s)
```
"""


def get_number_from_string(string):
    return int(''.join(ch for ch in string if ch.isdigit()))
