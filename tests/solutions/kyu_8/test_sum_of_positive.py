"""Sum of positive"""

import pytest

from solutions.kyu_8.sum_of_positive import positive_sum

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1,2,3,4,5],15),
        ([1,-2,3,4,5],13),
        ([-1,2,3,4,-5],9),
        ([],0),
        ([-1,-2,-3,-4,-5],0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert positive_sum(arg) == expected
