"""Digits explosion"""

import pytest

from solutions.kyu_7.digits_explosion import explode

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("312", "333122"),
        ("102269","12222666666999999999"),
        ("0", ""),
        ("000", ""),
        ("123", "122333"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert explode(arg) == expected
