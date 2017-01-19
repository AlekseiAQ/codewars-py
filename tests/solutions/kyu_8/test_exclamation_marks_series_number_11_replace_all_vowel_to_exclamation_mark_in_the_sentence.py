"""Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence"""

import pytest

from solutions.kyu_8.exclamation_marks_series_number_11_replace_all_vowel_to_exclamation_mark_in_the_sentence import replace_exclamation

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("Hi!", "H!!"),
        ("!Hi! Hi!", "!H!! H!!"),
        ("aeiou", "!!!!!"),
        ("ABCDE", "!BCD!"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert replace_exclamation(arg) == expected
