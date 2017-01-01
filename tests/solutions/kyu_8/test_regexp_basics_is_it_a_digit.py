"""Regexp Basics - is it a digit?"""

import pytest

from solutions.kyu_8.regexp_basics_is_it_a_digit import is_digit

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("", False),
        ("7", True),
        (" ", False),
        ("a", False),
        ("a5", False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert is_digit(arg) == expected
