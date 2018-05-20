"""Sum squares of numbers in list that may contain more lists"""

import pytest

from solutions.kyu_7.sum_squares_of_numbers_in_list_that_may_contain_more_lists import \
    sumsquares

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1,2,3], 14),
        ([[1,2],3], 14),
        ([[[[[[[[[1]]]]]]]]], 1),
        ([10,[[10],10],[10]], 400),
        ([1,[[3],10,5,[2,[3],[4],[5,[6]]]],[10]], 325),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sumsquares(arg) == expected
