"""Can I play right now?"""

import pytest

from solutions.kyu_7.can_i_play_right_now import can_i_play

EXAMPLES = (
    ('args', 'expected'),
    [
        ((12, 10, 14), True),
        ((12, 13, 14), False),
        ((15, 12, 15), False),
        ((23, 22, 1), True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert can_i_play(*args) == expected
