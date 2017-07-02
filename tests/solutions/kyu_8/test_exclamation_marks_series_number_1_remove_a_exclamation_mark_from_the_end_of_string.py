"""Exclamation marks series #1: Remove a exclamation mark from the end of string"""

import pytest

from solutions.kyu_8.exclamation_marks_series_number_1_remove_a_exclamation_mark_from_the_end_of_string import remove

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("Hi!", "Hi"),
        ("Hi!!!", "Hi!!"),
        ("!Hi", "!Hi"),
        ("!Hi!", "!Hi"),
        ("Hi! Hi!", "Hi! Hi"),
        ("Hi", "Hi"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert remove(arg) == expected
