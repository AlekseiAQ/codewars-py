"""Invert values"""

import pytest

from solutions.kyu_8.invert_values import invert

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1,2,3,4,5], [-1,-2,-3,-4,-5]),
        ([1,-2,3,-4,5], [-1,2,-3,4,-5]),
        ([], []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert invert(arg) == expected
