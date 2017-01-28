"""Slope of a Line"""

import pytest

from solutions.kyu_7.slope_of_a_line import getSlope

EXAMPLES = (
    ('p1', 'p2', 'expected'),
    [
        ([1,1],[2,2], 1),
        ([11,1],[1,11], -1),
        ([1,1],[1,2], None),
        ([1,1],[1,1], None),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(p1, p2, expected):
    assert getSlope(p1, p2) == expected
