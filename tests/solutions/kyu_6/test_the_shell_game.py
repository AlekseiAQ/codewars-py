"""The Shell Game"""

import pytest

from solutions.kyu_6.the_shell_game import find_the_ball

EXAMPLES = (
    ('args', 'expected'),
    [
        ((5, []), 5),
        ((0,[(0, 1), (2, 1), (0, 1)]), 2),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert find_the_ball(*args) == expected
