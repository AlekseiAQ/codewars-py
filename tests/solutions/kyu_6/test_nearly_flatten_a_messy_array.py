"""Nearly Flatten a Messy Array"""

import pytest

from solutions.kyu_6.nearly_flatten_a_messy_array import near_flatten

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([[1]], [[1]]),
        ([[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]),
        ([[1,2,3],[[4,5],[[6],[7,8]]]], [[1,2,3],[4,5],[6],[7,8]]),
        ([[[1,2,3],[9,10]],[[4,5],[6,7,8]]], [[1,2,3],[4,5],[6,7,8],[9,10]]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert near_flatten(arg) == expected
