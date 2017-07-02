"""Smallest unused ID"""

import pytest

from solutions.kyu_8.smallest_unused_id import next_id

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11),
        ([5, 4, 3, 2, 1], 0),
        ([0, 1, 2, 3, 5], 4),
        ([0, 0, 0, 0, 0, 0], 1),
        ([], 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert next_id(arg) == expected
