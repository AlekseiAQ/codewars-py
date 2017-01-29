"""Simple Maths Test"""

import pytest

from solutions.kyu_7.simple_maths_test import is_prime, number_property

EXAMPLES = (
    ('arg', 'expected'),
    [
        (-10,[False,True,True]),
        (2,[True,True,False]),
        (120,[False,True,True]),
        (125,[False,False,False]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert number_property(arg) == expected
