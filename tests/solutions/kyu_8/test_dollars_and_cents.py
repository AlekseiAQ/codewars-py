"""Dollars and Cents"""

import pytest

from solutions.kyu_8.dollars_and_cents import format_money

EXAMPLES = (
    ('arg', 'expected'),
    [
        (39.99, '$39.99'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert format_money(arg) == expected
