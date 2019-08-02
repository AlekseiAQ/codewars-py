"""Find sum of top-left to bottom-right diagonals"""

import pytest

from solutions.kyu_7.find_sum_of_top_left_to_bottom_right_diagonals import diagonal_sum

EXAMPLES = (
    ("arg", "expected"),
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15),
        ([[1, 2], [3, 4]], 5),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 34),
    ],
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert diagonal_sum(arg) == expected
