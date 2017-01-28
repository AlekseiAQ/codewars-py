"""Find Count of Most Frequent Item in an Array"""

import pytest

from solutions.kyu_7.find_count_of_most_frequent_item_in_an_array import most_frequent_item_count

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([3, -1, -1], 2),
        ([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3], 5),
        ([], 0),
        ([9], 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert most_frequent_item_count(arg) == expected
