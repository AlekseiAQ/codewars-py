"""Reversing Words in a String"""

import pytest

from solutions.kyu_8.reversing_words_in_a_string import reverse

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('Hello World', 'World Hello'),
        ('Hi There.', 'There. Hi'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert reverse(arg) == expected
