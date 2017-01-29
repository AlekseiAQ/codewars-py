"""CompoundArray"""

import pytest

from solutions.kyu_7.compoundarray import compound_array

EXAMPLES = (
    ('a', 'b', 'expected'),
    [
        ([1,2,3,4,5,6], [9,8,7,6], [1,9,2,8,3,7,4,6,5,6]),
        ([0,1,2], [9,8,7,6,5,4,3,2,1,0], [0,9,1,8,2,7,6,5,4,3,2,1,0]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(a, b, expected):
    assert compound_array(a, b) == expected
