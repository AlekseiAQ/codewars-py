"""Age in days"""

from datetime import date, timedelta

import pytest

from solutions.kyu_7.age_in_days import ageInDays

today = date.today()
birthday_one = today - timedelta(days=2)
birthday_two = today - timedelta(days=365)

EXAMPLES = (
    ('args', 'expected'),
    [
        ((birthday_one.year, birthday_one.month,
          birthday_one.day), 'You are 2 days old'),
        ((birthday_two.year, birthday_two.month,
          birthday_two.day), 'You are 365 days old'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert ageInDays(*args) == expected
