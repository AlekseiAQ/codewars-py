"""Find the first non-consecutive number"""

import pytest

from solutions.kyu_8.find_the_first_non_consecutive_number import first_non_consecutive

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1,2,3,4,6,7,8], 6),
        ([1,2,3,4,5,6,7,8], None),
        ([4,6,7,8,9,11], 6),
        ([4,5,6,7,8,9,11], 11),
        ([31,32], None),
        ([-3,-2,0,1], 0),
        ([-5,-4,-3,-1], -1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert first_non_consecutive(arg) == expected
