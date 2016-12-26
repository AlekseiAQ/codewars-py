"""Stringy Strings"""

import pytest

from solutions.kyu_8.stringy_strings import stringy

EXAMPLES = (
    ('arg', 'expected'),
    [
        (3, '101'),
        (5, '10101'),
        (12, '101010101010'),
        (26, '10101010101010101010101010'),
        (28, '1010101010101010101010101010'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert stringy(arg) == expected
