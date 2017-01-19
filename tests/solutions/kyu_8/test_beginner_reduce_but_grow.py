"""Beginner - Reduce but Grow"""

import pytest

from solutions.kyu_8.beginner_reduce_but_grow import grow

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1, 2, 3], 6),
        ([4, 1, 1, 1, 4], 16),
        ([2, 2, 2, 2, 2, 2], 64),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert grow(arg) == expected
