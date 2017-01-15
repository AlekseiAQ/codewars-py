"""Exclamation marks series #6: Remove n exclamation marks in the sentence from left to right"""

import pytest

from solutions.kyu_8.exclamation_marks_series_number_6_remove_n_exclamation_marks_in_the_sentence_from_left_to_right import remove

EXAMPLES = (
    ('args', 'expected'),
    [
        (("Hi!",1) , "Hi"),
        (("Hi!",100) , "Hi"),
        (("Hi!!!",1) , "Hi!!"),
        (("Hi!!!",100) , "Hi"),
        (("!Hi",1) , "Hi"),
        (("!Hi!",1) , "Hi!"),
        (("!Hi!",100) , "Hi"),
        (("!!!Hi !!hi!!! !hi",1) , "!!Hi !!hi!!! !hi"),
        (("!!!Hi !!hi!!! !hi",3) , "Hi !!hi!!! !hi"),
        (("!!!Hi !!hi!!! !hi",5) , "Hi hi!!! !hi"),
        (("!!!Hi !!hi!!! !hi",100) , "Hi hi hi"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert remove(*args) == expected
