"""Show multiples of 2 numbers within a range"""

import pytest

from solutions.kyu_7.show_multiples_of_2_numbers_within_a_range import multiples

EXAMPLES = (
    ('args', 'expected'),
    [
        ((2, 4, 40), [4, 8, 12, 16, 20, 24, 28, 32, 36]),
        ((3, 4, 40), [12, 24, 36]),
        ((7, 4, 80), [28, 56]),
        ((7, 4, 20), []),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert multiples(*args) == expected
