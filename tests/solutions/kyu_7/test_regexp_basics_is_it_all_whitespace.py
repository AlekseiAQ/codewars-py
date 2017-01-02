"""Regexp Basics - is it all whitespace?"""

import pytest

from solutions.kyu_7.regexp_basics_is_it_all_whitespace import whitespace

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("", True),
        (" ", True),
        ("\n\r\n\r", True),
        ("a", False),
        ("w\n", False),
        ("\t", True),
        (" a\n", False),
        ("\t \n\r\n  ", True),
        ("\n\r\n\r ", True),
        ("\n\r\n\r 3", False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert whitespace(arg) == expected
