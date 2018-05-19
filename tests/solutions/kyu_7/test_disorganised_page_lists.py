"""Disorganised page lists"""

import pytest

from solutions.kyu_7.disorganised_page_lists import find_page_number

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1,2,10,3,4,5,8,6,7], [10,8]),
        ([1,2,3,4,50,5,6,7,51,8,40,9], [50,51,40]),
        ([4,1,2,3,4,26,5,6], [4,26]),
        ([4,1,2,3,3,4,26,5,6], [4,3,26]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert find_page_number(arg) == expected
