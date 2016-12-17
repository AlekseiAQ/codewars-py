"""Reverse words"""

import pytest

from solutions.kyu_6.reverse_words import reverse_words

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('This is an example!', 'sihT si na !elpmaxe'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert reverse_words(arg) == expected
