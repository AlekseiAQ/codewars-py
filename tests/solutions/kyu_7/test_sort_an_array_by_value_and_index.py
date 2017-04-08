"""Sort an array by value and index"""

import pytest

from solutions.kyu_7.sort_an_array_by_value_and_index import sort_by_value_and_index

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([23, 2, 3, 4, 5], [2, 3, 4, 23, 5]),
        ([26, 2, 3, 4, 5], [2, 3, 4, 5, 26]),
        ([9, 5, 1, 4, 3], [1, 9, 5, 3, 4]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sort_by_value_and_index(arg) == expected
