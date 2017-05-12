"""regex  validation of 24 hours time."""

import pytest

from solutions.kyu_7.regex_validation_of_24_hours_time import validate_time

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('1:00', True),
        ('1:00', True),
        ('13:1', False),
        ('12:60', False),
        ('12: 60', False),
        ('24:00', False),
        ('00:00', True),
        ('24o:00', False),
        ('24:000', False),
        ('', False),
        ('09:00', True),
        ('2400', False),
        ('foo12:00bar', False),
        ('010:00', False),
        ('1;00', False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert validate_time(arg) == expected
