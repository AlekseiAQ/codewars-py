"""Correct the time-string"""

import pytest

from solutions.kyu_7.correct_the_time_string import time_correct

EXAMPLES = (
    ('arg', 'expected'),
    [
        (None, None),
        ("", ""),
        ("001122", None),
        ("00;11;22", None),
        ("0a:1c:22", None),
        ("09:10:01", "09:10:01"),
        ("11:70:10", "12:10:10"),
        ("19:99:99", "20:40:39"),
        ("24:01:01", "00:01:01"),
        ("52:01:01", "04:01:01"),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert time_correct(arg) == expected
