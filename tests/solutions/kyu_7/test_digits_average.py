"""Digits Average"""

import pytest

from solutions.kyu_7.digits_average import digits_average

EXAMPLES = (
    ('arg', 'expected'),
    [
        (246, 4),
        (89, 9),
        (2, 2),
        (245, 4),
        (345, 5),
        (346, 5),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert digits_average(arg) == expected
