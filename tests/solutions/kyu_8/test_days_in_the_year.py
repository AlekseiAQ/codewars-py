"""Days in the year"""

import pytest

from solutions.kyu_8.days_in_the_year import year_days

EXAMPLES = (
    ('arg', 'expected'),
    [
        (0, '0 has 366 days'),
        (-64, '-64 has 366 days'),
        (2016, '2016 has 366 days'),
        (1974, '1974 has 365 days'),
        (-10, '-10 has 365 days'),
        (666, '666 has 365 days'),
        (1857, '1857 has 365 days'),
        (2000, '2000 has 366 days'),
        (-300, '-300 has 365 days'),
        (-1, '-1 has 365 days'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert year_days(arg) == expected
