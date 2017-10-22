"""Converting 24-hour time to 12-hour time"""

import pytest

from solutions.kyu_7.converting_24_hour_time_to_12_hour_time import to12hourtime

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('0100', '1:00 am'),
        ('1300', '1:00 pm'),
        ('0630', '6:30 am'),
        ('2145', '9:45 pm'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert to12hourtime(arg) == expected
