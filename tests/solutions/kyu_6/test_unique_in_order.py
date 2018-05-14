"""Unique In Order"""

import pytest

from solutions.kyu_6.unique_in_order import unique_in_order

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('AAAABBBCCDAABBB', ['A','B','C','D','A','B']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert unique_in_order(arg) == expected
