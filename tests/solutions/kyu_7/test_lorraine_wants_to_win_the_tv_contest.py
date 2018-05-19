"""Lorraine Wants to Win the TV Contest"""

import pytest

from solutions.kyu_7.lorraine_wants_to_win_the_tv_contest import unscramble

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("shi", ['his']),
        ("nowk", ['know']),
        ("amle", ['male', 'meal']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert unscramble(arg) == expected
