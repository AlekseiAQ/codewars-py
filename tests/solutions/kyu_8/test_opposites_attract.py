"""Opposites Attract"""

import pytest

from solutions.kyu_8.opposites_attract import lovefunc

EXAMPLES = (
    ('args', 'expected'),
    [
        ((1,4), True),
        ((2,2), False),
        ((0,1), True),
        ((0,0), False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert lovefunc(*args) == expected
