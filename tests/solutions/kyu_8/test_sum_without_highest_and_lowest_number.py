"""Sum without highest and lowest number"""

import pytest

from solutions.kyu_8.sum_without_highest_and_lowest_number import sum_array

EXAMPLES = (
    ('arg', 'expected'),
    [
        (None, 0),
        ([], 0),
        ([3], 0),
        ([-3], 0),
        ([ 3, 5], 0),
        ([-3, -5], 0),
        ([6, 2, 1, 8, 10], 16),
        ([6, 0, 1, 10, 10], 17),
        ([-6, -20, -1, -10, -12], -28),
        ([-6, 20, -1, 10, -12], 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sum_array(arg) == expected
