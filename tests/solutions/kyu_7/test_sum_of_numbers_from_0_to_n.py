"""Sum of numbers from 0 to N"""

import pytest

from solutions.kyu_7.sum_of_numbers_from_0_to_n import show_sequence

EXAMPLES = (
    ('arg', 'expected'),
    [
        (6, "0+1+2+3+4+5+6 = 21"),
        (7, "0+1+2+3+4+5+6+7 = 28"),
        (0, "0=0"), 
        (-1, "-1<0"), 
        (-10, "-10<0"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert show_sequence(arg) == expected
