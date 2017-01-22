"""Leap Years"""

import pytest

from solutions.kyu_7.leap_years import isLeapYear

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1984, True),
        (2000, True),
        (1234, False),
        (1100, False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert isLeapYear(arg) == expected
