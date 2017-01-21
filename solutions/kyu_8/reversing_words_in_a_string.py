"""Reversing Words in a String
https://www.codewars.com/kata/reversing-words-in-a-string

You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:


```javascript
reverse('Hello World') === 'World Hello'
reverse('Hi There.') === 'There. Hi'
```


```python
reverse('Hello World') == 'World Hello'
reverse('Hi There.') == 'There. Hi'
```

```csharp
Kata.Reverse("Hello World"); // -> "World Hello"
Kata.Reverse("Hi There."); // -> "There. Hi"
```

```php
reverse("Hello World") === "World Hello"
reverse("Hi There.") === "There. Hi"
```



Happy coding!

"""


def reverse(st):
    return ' '.join(st.split(' ')[::-1])
