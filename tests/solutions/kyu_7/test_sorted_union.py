"""Sorted Union"""

import pytest

from solutions.kyu_7.sorted_union import unite_unique

EXAMPLES = (
    ('args', 'expected'),
    [
        (([1, 2], [3, 4]),[1, 2, 3, 4]),
        (([1, 3, 2], [5, 2, 1, 4], [2, 1]),[1, 3, 2, 5, 4]),
        (([4, "a", 2], []),[4, "a", 2]),
        (([], [4, "a", 2]),[4, "a", 2]),
        (([], [4, "a", 2], []),[4, "a", 2]),
        (([]),[]),
        (([],[]),[]),
        (([],[1, 2]),[1, 2]),
        (([],[1, 2, 1, 2],[2, 1, 1, 2, 1]),[1, 2]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert unite_unique(*args) == expected
