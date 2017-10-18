"""Pull your words together, man!
https://www.codewars.com/kata/pull-your-words-together-man

Your friend Robbie has successfully created an AI that is capable of communicating in English!

Robbie's almost done with the project, however the machine's output isn't working as expected. Here's a sample of a sentence that it outputs:

```
["this","is","a","sentence"]
```

Every time that it tries to say a sentence, instead of formatting it in normal English orthography, it just outputs a list of words.

Robbie has pulled multiple all-nighters to get this project finished, and he needs some beauty sleep. So, he wants you to write the last part of his code, a `sentencify` function, which takes the output that the machine gives, and formats it into proper English orthography.

Your function should:

1. Capitalise the first letter of the first word.
2. Add a period (`.`) to the end of the sentence.
3. Join the words into a complete string, with spaces.
4. Do *no other manipulation* on the words.

-----

Here are a few examples of what your function should do:

| Input | Output |
| --- | --- |
| `["i", "am", "an", "AI"]` | `"I am an AI."` |
| `["FIELDS","of","CORN","are","to","be","sown"]` | `"FIELDS of CORN are to be sown."` |
| `["i'm","afraid","I","can't","let","you","do","that"]` | `"I'm afraid I can't let you do that."` |

**_(Any translations (eg: to Java/C#/C++/Typescript) would be greatly appreciated!)_**
"""


def sentencify(words):
    strng = ' '.join(words)
    return '{}{}.'.format(strng[0].upper(), strng[1:])
