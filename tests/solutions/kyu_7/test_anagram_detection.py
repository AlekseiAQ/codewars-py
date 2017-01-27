"""Anagram Detection"""

import pytest

from solutions.kyu_7.anagram_detection import is_anagram

EXAMPLES = (
    ('test', 'original', 'expected'),
    [
        ('Creative', 'Reactive', True),
        ('TYPHON', 'Python', True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(test, original, expected):
    assert is_anagram(test, original) == expected
