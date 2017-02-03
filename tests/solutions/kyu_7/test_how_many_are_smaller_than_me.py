"""How many are smaller than me?"""

import pytest

from solutions.kyu_7.how_many_are_smaller_than_me import smaller

EXAMPLES = (
    ('arg', 'expected'),
    [
        ([5, 4, 3, 2, 1], [4, 3, 2, 1, 0]),
        ([1, 2, 3], [0, 0, 0]),
        ([1, 2, 0], [1, 1, 0]),
        ([1, 2, 1], [0, 1, 0]),
        ([1, 1, -1, 0, 0], [3, 3, 0, 0, 0]),
        ([5, 4, 7, 9, 2, 4, 4, 5, 6], [4, 1, 5, 5, 0, 0, 0, 0, 0]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert smaller(arg) == expected
