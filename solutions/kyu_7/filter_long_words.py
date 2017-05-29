"""Filter Long Words
https://www.codewars.com/kata/filter-long-words

Write a function `filter_long_words` that takes a string `sentence` and an integer `n`.

Return a list of all words that are longer than `n`.

Example:

`filter_long_words("The quick brown fox jumps over the lazy dog", 4) = ['quick', 'brown', 'jumps']`

"""


def filter_long_words(sentence, n):
    return list(filter(lambda x: x if len(x) > n else None, sentence.split()))
