"""Formatting decimal places #1"""

import pytest

from solutions.kyu_7.formatting_decimal_places_number_1 import two_decimal_places

EXAMPLES = (
    ('arg', 'expected'),
    [
        (10.1289767789, 10.12),
        (-7488.83485834983, -7488.83),
        (4.653725356, 4.65),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert two_decimal_places(arg) == expected
