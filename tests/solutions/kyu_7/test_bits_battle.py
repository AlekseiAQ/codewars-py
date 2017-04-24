"""Bits Battle"""

import pytest

from solutions.kyu_7.bits_battle import bits_battle

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([5, 3, 14], 'odds win'),
        ([3, 8, 22, 15, 78], 'evens win'),
        ([], 'tie'),
        ([1, 13, 16], 'tie'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert bits_battle(arg) == expected
