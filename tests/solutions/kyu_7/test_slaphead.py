"""Slaphead"""

import pytest

from solutions.kyu_7.slaphead import bald

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("/---------", ["----------", "Unicorn!"]),
        ("/-----/-", ["--------", "Homer!"]),
        ("--/--/---/-/---", ["---------------", "Careless!"]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert bald(arg) == expected
