"""Exclamation marks series #4: Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string"""

import pytest

from solutions.kyu_8.exclamation_marks_series_number_4_remove_all_exclamation_marks_from_sentence_but_ensure_a_exclamation_mark_at_the_end_of_string import remove

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("Hi!", "Hi!"),
        ("Hi!!!", "Hi!"),
        ("!Hi", "Hi!"),
        ("!Hi!", "Hi!"),
        ("Hi! Hi!", "Hi Hi!"),
        ("Hi", "Hi!"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert remove(arg) == expected
