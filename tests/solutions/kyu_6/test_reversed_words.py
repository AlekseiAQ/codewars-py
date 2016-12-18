"""Reversed Words"""

import pytest

from solutions.kyu_6.reversed_words import reverse_words

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("hello world!", "world! hello"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert reverse_words(arg) == expected
