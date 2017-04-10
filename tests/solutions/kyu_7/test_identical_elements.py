"""Identical Elements"""

import pytest

from solutions.kyu_7.identical_elements import duplicate_elements

EXAMPLES = (
    ('args', 'expected'),
    [
        (([1, 2, 3, 4, 5], [1, 6, 7, 8, 9]), True),
        (([9, 8, 7], [8, 1, 3]), True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert duplicate_elements(*args) == expected
