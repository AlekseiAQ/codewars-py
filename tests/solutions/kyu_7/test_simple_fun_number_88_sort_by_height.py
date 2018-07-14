"""Simple Fun #88: Sort By Height"""

import pytest

from solutions.kyu_7.simple_fun_number_88_sort_by_height import sort_by_height

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([-1, 150, 190, 170, -1, -1, 160, 180],
         [-1, 150, 160, 170, -1, -1, 180, 190]),
        ([-1, -1, -1, -1, -1],
         [-1, -1, -1, -1, -1]),
        ([4, 2, 9, 11, 2, 16],
         [2, 2, 4, 9, 11, 16]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sort_by_height(arg) == expected
