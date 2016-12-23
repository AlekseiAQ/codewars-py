"""Sum of Pairs"""

import pytest

from solutions.kyu_5.sum_of_pairs import sum_pairs

EXAMPLES = (
    ('args', 'expected'),
    [
        (([1, 4, 8, 7, 3, 15], 8), [1, 7]),
        (([1, -2, 3, 0, -6, 1], -6), [0, -6]),
        (([20, -13, 40], -7), None),
        (([10, 5, 2, 3, 7, 5], 10), [3, 7]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert sum_pairs(*args) == expected
