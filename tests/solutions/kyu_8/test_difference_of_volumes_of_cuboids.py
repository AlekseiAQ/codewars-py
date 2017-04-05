"""Difference of Volumes of Cuboids"""

import pytest

from solutions.kyu_8.difference_of_volumes_of_cuboids import find_difference

EXAMPLES = (
    ('a', 'b', 'expected'),
    [
        ([3, 2, 5], [1, 4, 4], 14),
        ([9, 7, 2], [5, 2, 2], 106),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(a, b, expected):
    assert find_difference(a, b) == expected
