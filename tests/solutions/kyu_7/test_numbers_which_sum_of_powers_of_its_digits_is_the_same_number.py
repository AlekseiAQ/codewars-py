"""Numbers Which Sum of Powers of Its Digits Is The Same Number"""

import pytest

from solutions.kyu_7.numbers_which_sum_of_powers_of_its_digits_is_the_same_number import eq_sum_powdig

EXAMPLES = (
    ('args', 'expected'),
    [
        ((100, 2), []),
        ((1000, 2), []),
        ((200, 3), [153]),
        ((370, 3), [153, 370]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert eq_sum_powdig(*args) == expected
