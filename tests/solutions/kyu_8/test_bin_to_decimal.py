"""Bin to Decimal"""

import pytest

from solutions.kyu_8.bin_to_decimal import bin_to_decimal

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("1", 1),
        ("0", 0),
        ("1001001", 73),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert bin_to_decimal(arg) == expected
