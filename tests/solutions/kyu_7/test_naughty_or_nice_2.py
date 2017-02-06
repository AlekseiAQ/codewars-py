"""Naughty or Nice?"""

import pytest

from solutions.kyu_7.naughty_or_nice_2 import whatListAmIOn

EXAMPLES = (
    ('arg', 'expected'),
    [
        (['broke someone\'s window', 'fought over a toaster', 'killed a bug'], 'naughty'),
        (['got someone a new car', 'saved a man from drowning', 'never got into a fight'], 'nice'),
        (['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes'], 'naughty'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert whatListAmIOn(arg) == expected
