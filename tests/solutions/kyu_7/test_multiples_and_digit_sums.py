"""Multiples and Digit Sums"""

import pytest

from solutions.kyu_7.multiples_and_digit_sums import procedure

EXAMPLES = (
    ('arg', 'expected'),
    [
        (30, 18),
        (12, 72),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert procedure(arg) == expected
