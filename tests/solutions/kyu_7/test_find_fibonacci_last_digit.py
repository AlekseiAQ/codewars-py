"""Find Fibonacci last digit"""

import pytest

from solutions.kyu_7.find_fibonacci_last_digit import get_last_digit

EXAMPLES = (
    ('arg', 'expected'),
    [
        (193150, 5),
        (300, 0),
        (20001, 6),
        (800, 5),
        (1001, 1),
        (100, 5),
        (260, 5),
        (1111, 9),
        (1234, 7),
        (99999, 6),
        (10, 5),
        (234, 2),
        (193241, 1),
        (79, 1),
        (270, 0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert get_last_digit(arg) == expected
