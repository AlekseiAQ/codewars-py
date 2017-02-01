"""Sum of odd numbers"""

import pytest

from solutions.kyu_7.sum_of_odd_numbers import row_sum_odd_numbers

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1, 1),
        (2, 8),
        (13, 2197),
        (19, 6859),
        (41, 68921),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert row_sum_odd_numbers(arg) == expected
