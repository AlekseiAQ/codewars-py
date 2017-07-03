"""Countdown to Christmas"""
import datetime

import pytest

from solutions.kyu_7.countdown_to_christmas import days_until_christmas

EXAMPLES = (
    ('arg', 'expected'),
    [
        (datetime.date(2016, 12, 9), 16),
        (datetime.date(2016, 12, 8), 17),
        (datetime.date(1996, 12, 7), 18),
        (datetime.date(2015, 2, 23), 305),
        (datetime.date(2001, 7, 11), 167),
        (datetime.date(2000, 12, 9), 16),
        (datetime.date(1978, 3, 18), 282),
        (datetime.date(2016, 12, 25), 0),
        (datetime.date(2016, 12, 26), 364),
        (datetime.date(2015, 12, 26), 365),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert days_until_christmas(arg) == expected
