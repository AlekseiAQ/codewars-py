"""Selective fear of numbers"""

import pytest

from solutions.kyu_7.selective_fear_of_numbers import am_I_afraid

EXAMPLES = (
    ('args', 'expected'),
    [
        (("Monday", 13), False),
        (("Sunday", -666), True),
        (("Tuesday", 2), False),
        (("Tuesday", 965), True),
        (("Friday", 2), True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert am_I_afraid(*args) == expected
