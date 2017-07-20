"""White or Black?"""

import pytest

from solutions.kyu_7.white_or_black import mine_color

EXAMPLES = (
    ('args', 'expected'),
    [
        (('a', 1), "black"),
        (('a', 2), "white"),
        (('c', 6), "white"),
        (('h', 6), "black"),
        (('h', 8), "black"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert mine_color(*args) == expected
