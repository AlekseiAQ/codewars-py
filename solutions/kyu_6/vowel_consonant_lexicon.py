"""Vowel-consonant lexicon
https://www.codewars.com/kata/vowel-consonant-lexicon

If we alternate the vowels and consonants in the string `"have"`, we get the following list, arranged alphabetically:
`['ahev', 'aveh', 'ehav', 'evah', 'vahe', 'veha']`. These are the only possibilities in which vowels and consonants are alternated. The first element, `ahev`, is alphabetically lowest.

Given a string:
* alternate the vowels and consonants and return the lexicographically lowest element in the list
* If any two or more vowels or consonants must follow each other, return `"failed"`
* if the number of vowels and consonants are equal, the first letter of the result must be a vowel.

Examples:

```Haskell
solve("codewars") = "failed". However you alternate vowels and consonants, two consonants must follow each other
solve("oruder") = "edorur"
solve("orudere") = "ederoru". This is the only option that allows you to alternate vowels & consonants.
```

Vowels will be any of "aeiou". Input will be a lowercase string, no spaces. See test cases for more examples.

Good luck!

If you like this Kata, please try:

[Consonant value](https://www.codewars.com/kata/59c633e7dcc4053512000073)

[Alternate capitalization](https://www.codewars.com/kata/59cfc000aeb2844d16000075)
"""


from itertools import zip_longest

def solve(s):
    vowels = sorted(char for char in s if char in "aeiou")
    consonants = sorted(char for char in s if char not in "aeiou")
    part1, part2 = sorted((vowels, consonants), key=len, reverse=True)
    if len(part1) > (len(part2) + 1):
        return "failed"
    return "".join(a + b for a, b in zip_longest(part1, part2, fillvalue=''))
