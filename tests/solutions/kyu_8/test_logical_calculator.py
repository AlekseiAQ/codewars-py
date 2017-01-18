"""Logical calculator"""

import pytest

from solutions.kyu_8.logical_calculator import logical_calc

EXAMPLES = (
    ('args', 'expected'),
    [
        (([True, False], "AND"), False),
        (([True, False], "OR"), True),
        (([True, False], "XOR"), True),
        (([True, True, False], "AND"), False),
        (([True, True, False], "OR"), True),
        (([True, True, False], "XOR"), False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert logical_calc(*args) == expected
