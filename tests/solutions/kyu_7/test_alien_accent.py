"""Alien Accent"""

import pytest

from solutions.kyu_7.alien_accent import convert

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('codewars', 'cudewors'),
        ('hello', 'hellu'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert convert(arg) == expected
