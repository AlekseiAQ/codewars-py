"""draw me a chessboard"""

import pytest

from solutions.kyu_7.draw_me_a_chessboard import chess_board

EXAMPLES = (
    ('args', 'expected'),
    [
        ((1, 1), [["O"]]),
        ((1, 2), [["O","X"]]),
        ((2, 1), [["O"],
                  ["X"]]),
        ((2, 2), [["O","X"],
                  ["X","O"]]),
        ((6, 6), [['O','X','O','X','O','X'],
                  ['X','O','X','O','X','O'],
                  ['O','X','O','X','O','X'],
                  ['X','O','X','O','X','O'],
                  ['O','X','O','X','O','X'],
                  ['X','O','X','O','X','O']]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert chess_board(*args) == expected
