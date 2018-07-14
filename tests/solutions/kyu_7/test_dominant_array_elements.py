"""Dominant array elements"""

import pytest

from solutions.kyu_7.dominant_array_elements import solve

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([16, 17, 14, 3, 14, 5, 2], [17, 14, 5, 2]),
        ([92, 52, 93, 31, 89, 87, 77, 105], [105]),
        ([75, 47, 42, 56, 13, 55], [75, 56, 55]),
        ([67, 54, 27, 85, 66, 88, 31, 24, 49], [88, 49]),
        ([76, 17, 25, 36, 29], [76, 36, 29]),
        ([104, 18, 37, 9, 36, 47, 28], [104, 47, 28]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert solve(arg) == expected
