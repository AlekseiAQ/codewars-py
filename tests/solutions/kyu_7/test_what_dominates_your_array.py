"""What dominates your array?"""

import pytest

from solutions.kyu_7.what_dominates_your_array import dominator

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([3,4,3,2,3,1,3,3],3),
        ([1,2,3,4,5],-1),
        ([1,1,1,2,2,2],-1),
        ([1,1,1,2,2,2,2],2),
        ([],-1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert dominator(arg) == expected
