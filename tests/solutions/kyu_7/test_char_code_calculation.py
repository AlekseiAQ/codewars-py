"""Char Code Calculation"""

import pytest

from solutions.kyu_7.char_code_calculation import calc

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('abcdef', 6),
        ('ifkhchlhfd', 6),
        ('aaaaaddddr', 30),
        ('jfmgklf8hglbe', 6),
        ('jaam', 12),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert calc(arg) == expected
