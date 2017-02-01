"""Switcheroo"""

import pytest

from solutions.kyu_7.switcheroo import switcheroo

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("abc", "bac"),
        ('aaabcccbaaa', 'bbbacccabbb'),
        ('ccccc', 'ccccc'),
        ('abababababababab', 'babababababababa'),
        ('aaaaa', 'bbbbb'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert switcheroo(arg) == expected
