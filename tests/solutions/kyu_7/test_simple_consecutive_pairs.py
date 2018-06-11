"""Simple consecutive pairs"""

import pytest

from solutions.kyu_7.simple_consecutive_pairs import pairs

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1, 2, 5, 8, -4, -3, 7, 6, 5], 3),
        ([21, 20, 22, 40, 39, -56, 30, -55, 95, 94], 2),
        ([81, 44, 80, 26, 12, 27, -34, 37, -35], 0),
        ([-55, -56, -7, -6, 56, 55, 63, 62], 4),
        ([73, 72, 8, 9, 73, 72], 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert pairs(arg) == expected
