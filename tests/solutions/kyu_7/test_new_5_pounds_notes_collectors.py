"""New £5 notes collectors!"""

import pytest

from solutions.kyu_7.new_5_pounds_notes_collectors import get_new_notes

EXAMPLES = (
    ('args', 'expected'),
    [
        ((2000, [500, 160, 400]), 188),
        ((1260, [500, 50, 100]), 122),
        ((3600, [1800, 350, 460, 500, 15]), 95),
        ((1995, [1500, 19, 44]), 86),
        ((10000, [1800, 500, 1200, 655, 150]), 1139),
        ((2300, [590, 1500, 45, 655, 150]), 0),
        ((5300, [1190, 1010, 1045, 55, 10, 19, 55]), 383),
        ((2000, [500, 495, 100, 900]), 1),
        ((2000, [500, 496, 100, 900]), 0),
        ((2000, [500, 494, 100, 900]), 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert get_new_notes(*args) == expected
