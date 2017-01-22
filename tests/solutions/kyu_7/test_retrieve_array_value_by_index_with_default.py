"""Retrieve array value by index with default"""

import pytest

from solutions.kyu_7.retrieve_array_value_by_index_with_default import solution

rng = list(range(1, 4))

EXAMPLES = (
    ('items', 'index', 'default_value', 'expected'),
    [
        (rng, 1, 'a', 2),
        (rng, -1, 'a', 3),
        (rng, -5, 'a', 'a'),
        (rng, -3, 'a', 1),
        (range(1,6), 10, 'a', 'a'),
        ([None, None], 0, 'a', None),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(items, index, default_value, expected):
    assert solution(items, index, default_value) == expected
