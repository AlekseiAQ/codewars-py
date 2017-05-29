"""Filter Long Words"""

import pytest

from solutions.kyu_7.filter_long_words import filter_long_words

EXAMPLES = (
    ('args', 'expected'),
    [
        (("The quick brown fox jumps over the lazy dog", 4),
            ['quick', 'brown', 'jumps']),
        (('Write a function filter_long_words() that takes a sentence and an integer n and returns the list of words that are longer than n.', 6),
            ['function', 'filter_long_words()', 'sentence', 'integer', 'returns']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert filter_long_words(*args) == expected
