"""Bouncy Numbers"""

import pytest

from solutions.kyu_7.bouncy_numbers import is_bouncy

EXAMPLES = (
    ('arg', 'expected'),
    [
        (0, False),
        (99, False),
        (101, True),
        (120, True),
        (122, False),
        (221, False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert is_bouncy(arg) == expected
