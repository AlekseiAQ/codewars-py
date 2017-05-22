"""Palindrome Pairs
https://www.codewars.com/kata/palindrome-pairs

Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Examples:
```ruby
["bat", "tab", "cat"] # [[0, 1], [1, 0]]
["dog", "cow", "tap", "god", "pat"] # [[0, 3], [2, 4], [3, 0], [4, 2]]
["abcd", "dcba", "lls", "s", "sssll"] # [[0, 1], [1, 0], [2, 4], [3, 2]]
```

Non-string inputs should be converted to strings.

Return an array of arrays containing pairs of distinct indices that form palindromes. Pairs should be reutrned in the order they appear in the original list.
"""


def palindrome_pairs(words):
    result = []
    for i, a in enumerate(words):
        for j, b in enumerate(words):
            if i != j:
                candidate = str(a) + str(b)
                if candidate == candidate[::-1]:
                    result.append([i, j])
    return result
