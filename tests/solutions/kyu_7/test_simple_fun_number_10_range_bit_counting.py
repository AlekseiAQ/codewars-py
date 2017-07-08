"""Simple Fun #10: Range Bit Counting"""

import pytest

from solutions.kyu_7.simple_fun_number_10_range_bit_counting import range_bit_count

EXAMPLES = (
    ('args', 'expected'),
    [
        ((2, 7), 11),
        ((0, 1), 1),
        ((4, 4), 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert range_bit_count(*args) == expected
