"""Find missing numbers"""

import pytest

from solutions.kyu_7.find_missing_numbers import find_missing_numbers

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([-3,-2,1,4], [-1,0,2,3]),
        ([-1,0,1,2,3,4], []),
        ([], []),
        ([0], []),
        ([-4,4], [-3,-2,-1,0,1,2,3]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert find_missing_numbers(arg) == expected
