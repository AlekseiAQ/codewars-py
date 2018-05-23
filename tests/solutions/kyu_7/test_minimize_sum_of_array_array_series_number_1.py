"""Minimize  Sum Of Array (Array Series #1)   """

import pytest

from solutions.kyu_7.minimize_sum_of_array_array_series_number_1 import min_sum

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([5,4,2,3], 22),
        ([12,6,10,26,3,24], 342),
        ([9,2,8,7,5,4,0,6], 74),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert min_sum(arg) == expected
