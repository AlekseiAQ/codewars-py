"""Vowel remover
https://www.codewars.com/kata/vowel-remover

Create a function called `shortcut` to remove all the **lowercase** vowels in a given string.

## Examples

```javascript
shortcut("codewars") // --> cdwrs
shortcut("goodbye")  // --> gdby
```
```python
shortcut("codewars") # --> cdwrs
shortcut("goodbye")  # --> gdby
```
```ruby
shortcut("codewars") # --> cdwrs
shortcut("goodbye")  # --> gdby
```
```csharp
Shortcut("codewars") # --> cdwrs
Shortcut("goodbye")  # --> gdby
```
```haskell
shortcut "codewars" -- > cdwrs
shortcut "goodbye"  -- > gdby
```

Don't worry about uppercase vowels.
"""


def shortcut(s):
    return ''.join(l for l in s if l not in 'aeiou')
