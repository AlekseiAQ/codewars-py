"""makeBackronym
https://www.codewars.com/kata/makebackronym

Definition-

back·ro·nym

noun

a fanciful expansion of an existing acronym or word, such as “port out, starboard home” for posh.

You will create a function called makeBackronym . There will be a preloaded dictionary to use. The dictionary is an object where the the keys are letters A-Z and the values are a predetermined word.

Use the variable name (its name is written in the code template) to reference the uppercase letters of the dictionary.
 
EXAMPLE:
```javascript
dict["P"]=="perfect"
```
```python
dictionary["P"]=="perfect"
```
```ruby
$dict["P"]=="perfect"
```
```csharp
dict['P']=="perfect"
```
```java
dictionary.get("P")=="perfect"
```
```haskell
dict 'P' == "perfect"
```

There will be a string(without spaces) passed into the function that you need to translate to a Backronym.

The preloaded dictionary can only read uppercase letters, and the value you return will have to be a string.

EXAMPLES:
```
"dgm" -> "disturbing gregarious mustache"

"lkj" -> "literal klingon joke"
```
"""


dictionary = {
    'H': 'hippy',
    'Y': 'yogic',
    'N': 'newtonian',
    'B': 'beautiful',
    'D': 'disturbing',
    'P': 'perfect',
    'L': 'literal',
    'G': 'gregarious',
    'F': 'fantastic',
    'Q': 'queen',
    'Z': 'zero',
    'S': 'stylish',
    'I': 'ingestable',
    'O': 'oscillating',
    'A': 'awesome',
    'R': 'rant',
    'W': 'weird',
    'U': 'underlying',
    'M': 'mustache',
    'T': 'turn',
    'X': 'xylophone',
    'V': 'volcano',
    'K': 'klingon',
    'C': 'confident',
    'J': 'joke',
    'E': 'eager'
}


def make_backronym(acronym):
    return ' '.join(dictionary[ch] for ch in acronym.upper())
