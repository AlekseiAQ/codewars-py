"""Reverse words
https://www.codewars.com/kata/reverse-words

Write a `reverseWords` function that accepts a string a parameter, and reverses each word in the string. Every space should stay, so you cannot use ```words``` from ```Prelude```.

Example:

````javascript
reverseWords("This is an example!"); // returns  "sihT si na !elpmaxe"
````
````python
reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"
````
```haskell
reverseWords "An example!"    -- "nA !elpmaxe"
reverseWords "double  spaces" -- "elbuod  secaps"
```

"""


def reverse_words(string):
    return ' '.join(word[::-1] for word in string.split(' '))
