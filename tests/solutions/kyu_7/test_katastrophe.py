"""Katastrophe!"""

import pytest

from solutions.kyu_7.katastrophe import strong_enough

EXAMPLES = (
    ('args', 'expected'),
    [
        (([[2,3,1],[3,1,1],[1,1,2]], 2), "Safe!"),
        (([[5,8,7],[3,3,1],[4,1,2]], 2), "Safe!"),
        (([[5,8,7],[3,3,1],[4,1,2]], 3), "Needs Reinforcement!"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert strong_enough(*args) == expected
