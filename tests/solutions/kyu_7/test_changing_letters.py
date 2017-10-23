"""Changing letters"""

import pytest

from solutions.kyu_7.changing_letters import swap

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("HelloWorld!", "HEllOWOrld!"),
        ("Sunday", "SUndAy"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert swap(arg) == expected
