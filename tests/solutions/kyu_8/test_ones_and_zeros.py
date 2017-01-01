"""Ones and Zeros"""

import pytest

from solutions.kyu_8.ones_and_zeros import binary_array_to_number

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([0,0,0,1], 1),
        ([0,0,1,0], 2),
        ([1,1,1,1], 15),
        ([0,1,1,0], 6),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert binary_array_to_number(arg) == expected
