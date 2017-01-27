"""Is your period late?"""

import pytest

from solutions.kyu_8.is_your_period_late import period_is_late
from datetime import date

EXAMPLES = (
    ('last', 'today', 'cycle_length', 'expected'),
    [
        (date(2016, 6, 13), date(2016, 7, 16), 35, False),
        (date(2016, 6, 13), date(2016, 7, 16), 28, True),
        (date(2016, 6, 13), date(2016, 7, 16), 35, False),
        (date(2016, 6, 13), date(2016, 6, 29), 28, False),
        (date(2016, 7, 12), date(2016, 8, 9), 28, False),
        (date(2016, 7, 12), date(2016, 8, 10), 28, True),
        (date(2016, 7, 1), date(2016, 8, 1), 30, True),
        (date(2016, 6, 1), date(2016, 6, 30), 30, False),
        (date(2016, 1, 1), date(2016, 1, 31), 30, False),
        (date(2016, 1, 1), date(2016, 2, 1), 30, True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(last, today, cycle_length, expected):
    assert period_is_late(last, today, cycle_length) == expected
