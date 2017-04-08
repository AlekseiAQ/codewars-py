"""Lucky Bus Ticket"""

import pytest

from solutions.kyu_7.lucky_bus_ticket import is_lucky

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('123321', True),
        ('12341234', False),
        ('100001', True),
        ('100200', False),
        ('912435', True),
        ('12a12a', False),
        ('999999', True),
        ('1111', False),
        ('000000', True),
        ('', False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert is_lucky(arg) == expected
