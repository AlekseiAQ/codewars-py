"""Buying a car"""

import pytest

from solutions.kyu_6.buying_a_car import nbMonths

EXAMPLES = (
    ('args', 'expected'),
    [
        ((8000, 8000, 1000, 1.5), [0, 0]),
        ((2000, 8000, 1000, 1.5), [6, 766]),
        ((12000, 8000, 1000, 1.5), [0, 4000]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert nbMonths(*args) == expected
