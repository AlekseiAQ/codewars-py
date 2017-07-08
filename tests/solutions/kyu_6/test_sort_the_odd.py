"""Sort the odd"""

import pytest

from solutions.kyu_6.sort_the_odd import sort_array

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([5, 3, 2, 8, 1, 4], [1, 3, 2, 8, 5, 4]),
        ([5, 3, 1, 8, 0], [1, 3, 5, 8, 0]),
        ([], []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert sort_array(arg) == expected
