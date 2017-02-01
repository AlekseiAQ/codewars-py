"""Dropcaps"""

import pytest

from solutions.kyu_7.dropcaps import drop_cap

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('Apple Banana',"Apple Banana"),
        ('Apple',"Apple"),
        ('',""),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert drop_cap(arg) == expected
