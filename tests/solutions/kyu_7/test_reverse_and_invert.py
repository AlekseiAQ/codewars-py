"""Reverse and Invert"""

import pytest

from solutions.kyu_7.reverse_and_invert import reverse_invert

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1,2,3,4,5], [-1,-2,-3,-4,-5]),
        ([-10], [1]),
        ([-9,-18,99], [9,81,-99]),
        ([1,12,'a',3.4,87,99.9,-42,50,5.6],[-1,-21,-78,24,-5]),
        ([], []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert reverse_invert(arg) == expected
