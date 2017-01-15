"""Multiply the number"""

import pytest

from solutions.kyu_8.multiply_the_number import multiply

EXAMPLES = (
    ('arg', 'expected'),
    [
        (10,250),
        (5,25),
        (200,25000),
        (0,0),
        (-2,-10),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert multiply(arg) == expected
