"""Determine if the poker hand is flush"""

import pytest

from solutions.kyu_7.determine_if_the_poker_hand_is_flush import is_flush

EXAMPLES = (
    ('arg', 'expected'),
    [
        (["AS", "3S", "9S", "KS", "4S"], True),
        (["AD", "4S", "7H", "KC", "5S"], False),
        (["AD", "4S", "10H", "KC", "5S"], False),
        (["QD", "4D", "10D", "KD", "5D"], True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert is_flush(arg) == expected
