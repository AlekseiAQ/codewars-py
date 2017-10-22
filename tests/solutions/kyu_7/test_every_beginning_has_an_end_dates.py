"""Every beginning has an end (Dates)"""

from datetime import datetime

import pytest

from solutions.kyu_7.every_beginning_has_an_end_dates import (week_end_date,
                                                              week_start_date)

EXAMPLES_START = (
    ('arg', 'expected'),
    [
        (datetime(2016, 1, 28), datetime(2016, 1, 25)),
        (datetime(2016, 2, 29), datetime(2016, 2, 29)),
    ]
)

EXAMPLES_END = (
    ('arg', 'expected'),
    [
        (datetime(1957, 12, 25), datetime(1957, 12, 29)),
        (datetime(1954, 5, 16), datetime(1954, 5, 16)),
    ]
)


@pytest.mark.parametrize(*EXAMPLES_START)
def test_returns_correct_result_start(arg, expected):
    assert week_start_date(arg) == expected


@pytest.mark.parametrize(*EXAMPLES_END)
def test_returns_correct_result_end(arg, expected):
    assert week_end_date(arg) == expected
