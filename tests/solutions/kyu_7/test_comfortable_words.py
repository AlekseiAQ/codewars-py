"""Comfortable words"""

import pytest

from solutions.kyu_7.comfortable_words import comfortable_word

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('yams', True),
        ('test', False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert comfortable_word(arg) == expected
