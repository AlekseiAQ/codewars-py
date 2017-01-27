"""Hex to Decimal"""

import pytest

from solutions.kyu_8.hex_to_decimal import hex_to_dec

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("1", 1),
        ("a", 10),
        ("10", 16),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert hex_to_dec(arg) == expected
