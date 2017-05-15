"""Date Format Validation"""

import pytest

from solutions.kyu_7.date_format_validation import date_checker

EXAMPLES = (
    ('arg', 'expected'),
    [
        ("01-09-2016 01:20", True),
        ("01-09-2016 01;20", False),
        ("01_09_2016 01:20", False),
        ("14-10-1066 12:00", True),
        ("Tenth of January", False),
        ("20 Sep 1988", False),
        ("19-12-2050 13:34", True),
        ("Tue Sep 06 2016 01:46:38 GMT+0100", False),
        ("01-09-2016 00:00", True),
        ("01-09-2016 2:00", False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert date_checker(arg) == expected
