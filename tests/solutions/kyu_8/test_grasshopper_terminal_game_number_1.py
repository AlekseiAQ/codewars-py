"""Grasshopper - Terminal Game #1"""

import pytest

from solutions.kyu_8.grasshopper_terminal_game_number_1 import Hero


myHero = Hero()

EXAMPLES = (
    ('arg', 'expected'),
    [
        (myHero.name, 'Hero'),
        (myHero.experience, 0),
        (myHero.health, 100),
        (myHero.position, '00'),
        (myHero.damage, 5),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert arg == expected
