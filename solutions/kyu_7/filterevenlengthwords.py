"""filterEvenLengthWords
https://www.codewars.com/kata/filterevenlengthwords

Write a function called "filterEvenLengthWords".

Given an array of strings, "filterEvenLengthWords" returns an array containing only the elements of the given array whose length is an even number.

var output = filterEvenLengthWords(['word', 'words', 'word', 'words']);

console.log(output); // --> ['word', 'word']

"""


def filter_even_length_words(words):
    return [word for word in words if len(word) % 2 == 0]
