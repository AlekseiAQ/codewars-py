"""Median fun fun"""

import pytest

from solutions.kyu_7.median_fun_fun import median

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1,2,3,4], 2.5),
        ([3,4,1,2,5], 3),
        ([10,29,23,94,76,96,5,85,4,33,47,41,87], 41),
        ([1], 1),
        ([1,-1], 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert median(arg) == expected
