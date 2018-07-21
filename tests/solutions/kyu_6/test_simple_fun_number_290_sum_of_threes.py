"""Simple Fun #290: Sum Of Threes"""

import pytest

from solutions.kyu_6.simple_fun_number_290_sum_of_threes import sum_of_threes

EXAMPLES = (
    ('arg', 'expected'),
    [
        (4, "3^1+3^0"),
        (2, "Impossible"),
        (28, "3^3+3^0"),
        (84, "3^4+3^1"),
        (1418194818, "Impossible"),
        (87754, "3^10+3^9+3^8+3^7+3^5+3^3+3^1+3^0"),
        (531441, "3^12"),
        (8312964441463288, "Impossible"),
        (5559060566575209, "3^33+3^9+3^1"),
        (243, "3^5"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sum_of_threes(arg) == expected
