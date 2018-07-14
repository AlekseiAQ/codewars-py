"""Simple Fun #144: Distinct Digit Year"""

import pytest

from solutions.kyu_7.simple_fun_number_144_distinct_digit_year import \
    distinct_digit_year

EXAMPLES = (
    ('arg', 'expected'),
    [
        (1987, 2013),
        (2013, 2014),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert distinct_digit_year(arg) == expected
