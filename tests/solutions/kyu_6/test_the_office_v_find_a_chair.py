"""The Office V - Find a Chair """

import pytest

from solutions.kyu_6.the_office_v_find_a_chair import meeting

EXAMPLES = (
    ('args', 'expected'),
    [
        (([["XXX", 3], ["XXXXX", 6], ["XXXXXX", 9]], 4), [0, 1, 3]),
        (([["XXX", 1], ["XXXXXX", 6], ["X", 2], ["XXXXXX", 8], ["X", 3], ["XXX", 1]], 5), [0, 0, 1, 2, 2]),
        (([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 0), "Game On"),
        (([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 8), "Not enough!"),
        (([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 2), [0, 2]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert meeting(*args) == expected
