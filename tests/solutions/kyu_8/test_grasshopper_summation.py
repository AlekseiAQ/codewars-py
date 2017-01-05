"""Grasshopper - Summation"""

import pytest

from solutions.kyu_8.grasshopper_summation import summation

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1, 1),
        (8, 36),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert summation(arg) == expected
