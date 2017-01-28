"""Alternate Square Sum"""

import pytest

from solutions.kyu_7.alternate_square_sum import alternate_sq_sum

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([], 0),
        ([-1, 0, -3, 0, -5, 3], 0),
        ([-1, 2, -3, 4, -5], 11),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 245),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert alternate_sq_sum(arg) == expected
