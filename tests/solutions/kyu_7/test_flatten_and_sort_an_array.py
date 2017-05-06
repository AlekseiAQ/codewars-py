"""Flatten and sort an array"""

import pytest

from solutions.kyu_7.flatten_and_sort_an_array import flatten_and_sort

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([], []),
        ([[], [1]], [1]),
        ([[3, 2, 1], [7, 9, 8], [6, 4, 5]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([[1, 3, 5], [100], [2, 4, 6]], [1, 2, 3, 4, 5, 6, 100]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert flatten_and_sort(arg) == expected
