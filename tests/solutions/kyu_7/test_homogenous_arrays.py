"""Homogenous arrays"""

import pytest

from solutions.kyu_7.homogenous_arrays import filter_homogenous

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]],
            [[1, 5, 4], ['b']]),
        ([[123, 234, 432], ['', 'abc'], [''], ['', 1], ['', '1'], []],
            [[123, 234, 432], ['', 'abc'], [''], ['', '1']]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert filter_homogenous(arg) == expected
