"""Kooka-Counter"""

import pytest

from solutions.kyu_7.kooka_counter import kooka_counter

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("", 0),
        ("hahahahaha", 1),
        ("hahahahahaHaHaHa", 2),
        ("HaHaHahahaHaHa", 3),
        ("HaHaHahaha", 2),
        ("hahahahahahahaHaHa", 2),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert kooka_counter(arg) == expected
