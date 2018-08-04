"""Player Contact Manager"""

import pytest

from solutions.kyu_7.player_contact_manager import player_manager

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("John Doe, 8167238327, Jane Doe, 8163723827",
            [{"player": "John Doe", "contact": 8167238327},
             {"player": "Jane Doe", "contact": 8163723827}]),
        ("", []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert player_manager(arg) == expected
