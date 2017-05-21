"""Alphabetize a list by the nth character """

import pytest

from solutions.kyu_7.alphabetize_a_list_by_the_nth_character import sort_it

EXAMPLES = (
    ('args', 'expected'),
    [
        (('bill, bell, ball, bull', 2), 'ball, bell, bill, bull'),
        (('cat, dog, eel, bee', 3), 'bee, dog, eel, cat'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert sort_it(*args) == expected
