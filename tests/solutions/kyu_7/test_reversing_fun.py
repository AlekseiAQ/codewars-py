"""Reversing Fun"""

import pytest

from solutions.kyu_7.reversing_fun import reverse_fun

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('012345', '504132'),
        ('jointhedarkside', 'ejdoiisnktrhaed'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert reverse_fun(arg) == expected
