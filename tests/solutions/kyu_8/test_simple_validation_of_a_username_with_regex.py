"""simple validation of a username with regex"""

import pytest

from solutions.kyu_8.simple_validation_of_a_username_with_regex import validate_usr

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('asddsa', True),
        ('a', False),
        ('Hass', False),
        ('Hasd_12assssssasasasasasaasasasasas', False),
        ('', False),
        ('____', True),
        ('012', False),
        ('p1pp1', True),
        ('asd43 34', False),
        ('asd43_34', True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert validate_usr(arg) == expected
