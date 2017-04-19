"""Numbers with this digit inside"""

import pytest

from solutions.kyu_7.numbers_with_this_digit_inside import numbers_with_digit_inside

EXAMPLES = (
    ('args', 'expected'),
    [
        ((5, 6), [0, 0, 0]),
        ((7, 6), [1, 6, 6]),
        ((11, 1), [3, 22, 110]),
        ((20, 0), [2, 30, 200]),
        ((44, 4), [9, 286, 5955146588160]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert numbers_with_digit_inside(*args) == expected
