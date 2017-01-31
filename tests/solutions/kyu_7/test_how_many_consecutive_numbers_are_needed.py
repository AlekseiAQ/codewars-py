"""How many consecutive numbers are needed?"""

import pytest

from solutions.kyu_7.how_many_consecutive_numbers_are_needed import consecutive

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([4,8,6],2),
        ([1,2,3,4],0),
        ([],0),
        ([1],0),
        ([-10],0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert consecutive(arg) == expected
