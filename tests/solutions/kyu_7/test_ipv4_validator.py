"""IPv4 Validator"""

import pytest

from solutions.kyu_7.ipv4_validator import ip_validator

EXAMPLES = (
    ('arg', 'expected'),
    [
        ('127.0.0.1', True),
        ('123.456.789.0', False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(arg, expected):
    assert ip_validator(arg) == expected
