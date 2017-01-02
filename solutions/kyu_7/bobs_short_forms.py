"""Bob's Short Forms
https://www.codewars.com/kata/bobs-short-forms

Bob is a theoretical coder - he doesn't write code, but comes up with theories, formulas and algorithm ideas. You are his secretary, and he has tasked you with writing the code for his newest project - a method for making the short form of a word. Write a function ```shortForm```(C# ```ShortForm```, Python ```short_form```) that takes a string and returns it converted into short form using the rule: <em>Remove all vowels, except for those that are the first or last letter. </em>Do not count 'y' as a vowel, and ignore case. Also note, the string given will not have any spaces; only one word, and only Roman letters. 
<br>
Example:
```
shortForm("assault");
short_form("assault")
ShortForm("assault");
// should return "asslt"
```

<br> <br>
Also, FYI: I got all the words with no vowels from <br>
https://en.wikipedia.org/wiki/English_words_without_vowels
"""


import re


def short_form(s):
    return re.sub(r"(?<!^)[aeiou](?=.)", '', s, flags=re.I)
