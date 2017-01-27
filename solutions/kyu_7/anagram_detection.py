"""Anagram Detection
https://www.codewars.com/kata/anagram-detection

An **anagram** is the result of rearranging the letters of a word to produce a new word. (*Ref wikipedia*).

*Note: anagrams are case insensitive*

Examples

* **foefet** is an anagram of **toffee**

* **Buckethead** is an anagram of **DeathCubeK**

The challenge is to write the function `isAnagram` (or `is_anagram` in Python) to return *true* if the word `test` is an anagram of the word `original` and *false* otherwise. The function prototype is as given below:

```js
var isAnagram = function(test, original) {
};
```

```python
def is_anagram(test, original):
  pass
```

```javascript
var isAnagram = function(test, original) {
};
```

```ruby
def is_anagram(test, original):
  #your code here
end
```

```haskell
isAnagramOf :: String -> String -> Bool
isAnagramOf test original = …
```
```csharp
public static bool IsAnagram(string test, string original)
{
}
```
```java
public static boolean isAnagram(String test, String original) {
}
```
"""


def is_anagram(test, original):
    return set(original.lower()) == set(test.lower())
