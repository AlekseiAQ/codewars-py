"""Fruit string calculator"""

import pytest

from solutions.kyu_7.fruit_string_calculator import calculate

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("Panda has 48 apples and loses 4", 44),
        ("Jerry has 34 apples and gains 6", 40),
        ("Tom has 20 apples and gains 15", 35),
        ("Fred has 110 bananas and loses 50", 60),
        ("Pippi has 20 tunas and gains 0", 20),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert calculate(arg) == expected
