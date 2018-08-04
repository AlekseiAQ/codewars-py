"""Thinkful - List Drills: Longest word
https://www.codewars.com/kata/thinkful-list-drills-longest-word

Complete the function that takes one argument, a list of words, and returns the length of the longest word in the list.

For example:

```python
['simple', 'is', 'better', 'than', 'complex'] ==> 7
```

Do not modify the input list.
"""


def longest(words):
    return max(map(len, words))
