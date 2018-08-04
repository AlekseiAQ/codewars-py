"""Thinkful - List Drills: Longest word"""

import pytest

from solutions.kyu_7.thinkful_list_drills_longest_word import longest

EXAMPLES = (
    ('arg', 'expected'),
    [
        (['simple', 'is', 'better', 'than', 'complex'], 7),
        (['explicit', 'is', 'better', 'than', 'implicit'], 8),
        (['beautiful', 'is', 'better', 'than', 'ugly'], 9),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert longest(arg) == expected
