"""Find n'th Digit of a Number"""

import pytest

from solutions.kyu_8.find_nth_digit_of_a_number import find_digit

EXAMPLES = (
    ('num', 'nth', 'expected'),
    [
        (5673, 4, 5),
        (129, 2, 2),
        (-2825, 3, 8),
        (0, 20, 0),
        (65, 0, -1),
        (24, -8, -1),
        (-1234, 2, 3),
        (-5540, 1, 0),
        (678998, 0, -1),
        (-67854, -57, -1),
        (0, -3, -1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(num, nth, expected):
    assert find_digit(num, nth) == expected
