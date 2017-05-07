"""The Office IV - Find a Meeting Room"""

import pytest

from solutions.kyu_7.the_office_iv_find_a_meeting_room import meeting

EXAMPLES = (
    ('arg', 'expected'),
    [
        (['X', 'O', 'X'], 1),
        (['O','X','X','X','X'], 0),
        (['X','X','O','X','X'], 2),
        (['X'], 'None available!'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert meeting(arg) == expected
