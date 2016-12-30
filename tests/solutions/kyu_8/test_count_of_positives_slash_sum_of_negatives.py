"""Count of positives / sum of negatives"""

import pytest

from solutions.kyu_8.count_of_positives_slash_sum_of_negatives import count_positives_sum_negatives

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15],[10,-65]),
        ([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14],[8,-50]),
        ([1],[1,0]),
        ([-1],[0,-1]),
        ([0,0,0,0,0,0,0,0,0],[0,0]),
        ([],[]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert count_positives_sum_negatives(arg) == expected
