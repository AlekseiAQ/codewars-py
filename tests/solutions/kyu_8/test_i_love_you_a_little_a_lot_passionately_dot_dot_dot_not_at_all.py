"""I love you,  a little ,  a lot,  passionately ... not at all"""

import pytest

from solutions.kyu_8.i_love_you_a_little_a_lot_passionately_dot_dot_dot_not_at_all import how_much_i_love_you

EXAMPLES = (
    ('arg', 'expected'),
    [
        (7,"I love you"),
        (3,"a lot"),
        (6,"not at all"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert how_much_i_love_you(arg) == expected
