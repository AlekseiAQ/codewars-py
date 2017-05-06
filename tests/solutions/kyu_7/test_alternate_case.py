"""Alternate case"""

import pytest

from solutions.kyu_7.alternate_case import alternateCase

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("ABC", "abc"),
        ("", ""),
        (" ", " "),
        ("Hello World", "hELLO wORLD"),
        ("cODEwARS", "CodeWars"),
        ("i LIKE MAKING KATAS VERY MUCH", "I like making katas very much"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert alternateCase(arg) == expected
