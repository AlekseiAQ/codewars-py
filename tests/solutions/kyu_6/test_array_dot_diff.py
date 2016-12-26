"""Array.diff"""

import pytest

from solutions.kyu_6.array_dot_diff import array_diff

EXAMPLES = (
    ('a', 'b','expected'),
    [
        ([1, 2], [1], [2]),
        ([1, 2, 2], [1], [2, 2]),
        ([1, 2, 2], [2], [1]),
        ([1, 2, 2], [], [1, 2, 2]),
        ([], [1, 2], []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(a, b, expected):
    assert array_diff(a, b) == expected
