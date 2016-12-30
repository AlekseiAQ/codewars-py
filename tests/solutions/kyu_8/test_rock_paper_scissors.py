"""Rock Paper Scissors!"""

import pytest

from solutions.kyu_8.rock_paper_scissors import rps

EXAMPLES = (
    ('args', 'expected'),
    [
        (('rock', 'scissors'), "Player 1 won!"),
        (('scissors', 'paper'), "Player 1 won!"),
        (('paper', 'rock'), "Player 1 won!"),
        (('scissors', 'rock'), "Player 2 won!"),
        (('paper', 'scissors'), "Player 2 won!"),
        (('rock', 'paper'), "Player 2 won!"),
        (('rock', 'rock'), 'Draw!'),
        (('scissors', 'scissors'), 'Draw!'),
        (('paper', 'paper'), 'Draw!'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert rps(*args) == expected
