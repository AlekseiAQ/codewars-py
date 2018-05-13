"""Vowel-consonant lexicon"""

import pytest

from solutions.kyu_6.vowel_consonant_lexicon import solve

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('java', 'ajav'),
        ('oruder', 'edorur'),
        ('zodiac', 'acidoz'),
        ('apple', 'lapep'),
        ('acidity', 'caditiy'),
        ('codewars', 'failed'),
        ('orudere', 'ederoru'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert solve(arg) == expected
