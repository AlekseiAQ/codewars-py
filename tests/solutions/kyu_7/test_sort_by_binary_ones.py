"""Sort by binary ones"""

import pytest

from solutions.kyu_7.sort_by_binary_ones import sort_by_binary_ones

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([1, 3], [3, 1]),
        ([1, 2, 3, 4], [3, 1, 2, 4]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sort_by_binary_ones(arg) == expected
