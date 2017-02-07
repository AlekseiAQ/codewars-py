"""Reduce My Fraction"""

import pytest

from solutions.kyu_7.reduce_my_fraction import reduce_

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([60, 20], [3, 1]),
        ([80, 120], [2, 3]),
        ([4, 2], [2, 1]),
        ([45, 120], [3, 8]),
        ([1000, 1], [1000, 1]),
        ([1, 1], [1, 1]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert reduce_(arg) == expected
