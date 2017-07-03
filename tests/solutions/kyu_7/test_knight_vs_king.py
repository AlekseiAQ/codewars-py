"""Knight vs King"""

import pytest

from solutions.kyu_7.knight_vs_king import knightVsKing

EXAMPLES = (
    ('args', 'expected'),
    [
        (([4, "C"], [6, "D"]), "Knight"),
        (([7, "B"], [6, "C"]), "King"),
        (([2, "F"], [6, "B"]), "None"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert knightVsKing(*args) == expected
